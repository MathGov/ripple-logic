#!/usr/bin/env python3
"""Validate a WDBIP v1.4 record.

Uses JSON Schema when installed, then applies semantic conformance checks.
Exit 0 = valid; exit 1 = invalid; exit 2 = invocation error.
Record conformance does not verify evidence truth, construct validity, causal truth,
rights compliance, gate passage, lawful authority, or decision correctness.
"""
from pathlib import Path
import json
import math
import sys

SCOPES = {
    "U1_SELF", "U2_HOUSEHOLD", "U3_COMMUNITY", "U4_ORGANIZATION",
    "U5_POLITY", "U6_HUMANITY_GLOBAL_COORDINATION", "U7_BIOSPHERE"
}
PATHWAY_PREFIX = "PATHWAY_"
EVIDENCE_PREFIX = "EVIDENCE_"
DIRECTION_PREFIX = "DIRECTION_"
SEVERE_SUBGROUP = {"RIGHTS_MATERIAL", "TRC_MATERIAL", "CSV_MATERIAL"}


def validate(record_path: Path, schema_path: Path):
    errors = []
    try:
        data = json.loads(record_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"parse failure: {exc}"]

    try:
        import jsonschema
        validator = jsonschema.Draft202012Validator(schema)
        for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
            path = ".".join(str(x) for x in err.absolute_path) or "$"
            errors.append(f"schema {path}: {err.message}")
    except ImportError:
        pass

    def fail(message):
        errors.append(message)

    if data.get("protocol_version") != "WDBIP v1.4":
        fail("protocol_version must be WDBIP v1.4")
    if data.get("schema_version") != "wdbip_record_v1_4":
        fail("schema_version must be wdbip_record_v1_4")
    if data.get("welfare_dimension_set_version") != "WELFARE_DIMENSION_SET_7D_V1":
        fail("welfare_dimension_set_version must be WELFARE_DIMENSION_SET_7D_V1 unless a future schema explicitly permits migration")
    if data.get("canon_version") != "RippleLogic v12.4":
        fail("canon_version pin mismatch for this standalone v1.4 package")

    tier = data.get("tier")
    use_class = data.get("use_class")

    pcc = data.get("pcc_link", {})
    if not pcc.get("pcc_record_id"):
        fail("PCC link missing")
    attachment_mode = pcc.get("attachment_mode")
    if attachment_mode == "PCC_HASH_REFERENCED" and not pcc.get("record_hash"):
        fail("PCC_HASH_REFERENCED requires record_hash")
    if attachment_mode == "PCC_IMMUTABLE_LOCATOR" and not pcc.get("artifact_locator"):
        fail("PCC_IMMUTABLE_LOCATOR requires artifact_locator")

    declared_scopes = set(data.get("declared_scopes", []))
    scope_mode = data.get("scope_mode")
    if scope_mode == "FULL_SCOPE" and declared_scopes != SCOPES:
        fail("FULL_SCOPE requires all seven canonical Union Scopes")
    if scope_mode == "REDUCED_SCOPE" and not data.get("scope_coverage_declaration_ref"):
        fail("REDUCED_SCOPE requires scope_coverage_declaration_ref")

    time_alignment = data.get("time_window_alignment", {})
    time_status = time_alignment.get("status")
    if time_status == "TIME_MODEL_DECLARED" and not time_alignment.get("temporal_model_ref"):
        fail("TIME_MODEL_DECLARED requires temporal_model_ref")
    if time_status == "TIME_MISMATCH_UNRESOLVED":
        if not time_alignment.get("mismatch_rationale"):
            fail("TIME_MISMATCH_UNRESOLVED requires mismatch_rationale")
        if not time_alignment.get("sensitivity_ref"):
            fail("TIME_MISMATCH_UNRESOLVED requires sensitivity_ref")
        if data.get("record_status") == "WDBIP_RECORD_COMPLETE":
            fail("COMPLETE status incompatible with unresolved time-window mismatch")

    subgroup = data.get("subgroup_review", {})
    if tier in (2, 3) and subgroup.get("completed") is not True:
        fail("Tier 2 and Tier 3 require completed subgroup review")
    if subgroup.get("aggregate_sign") == "BENEFICIAL" and subgroup.get("worst_subgroup_sign") == "HARMFUL":
        if subgroup.get("masking_review_completed") is not True:
            fail("beneficial aggregate with harmful worst subgroup requires masking_review_completed")
    if subgroup.get("severe_harm_status") in SEVERE_SUBGROUP and not subgroup.get("gate_routing_ref"):
        fail("severe subgroup harm requires gate_routing_ref")

    weights = data.get("weight_sensitivity", {})
    if weights.get("material") is True:
        if weights.get("status") in ("NOT_TESTED", "UNKNOWN") and tier == 3:
            fail("Tier 3 material weight sensitivity must be tested or the stronger ranking claim narrowed")
        if weights.get("status") in ("WEIGHT_SENSITIVE", "WEIGHT_ROBUST") and not weights.get("analysis_ref"):
            fail("tested weight-sensitivity status requires analysis_ref")
        if weights.get("status") == "WEIGHT_SENSITIVE" and not weights.get("authority_selection_ref"):
            fail("WEIGHT_SENSITIVE selection requires authority_selection_ref or a narrowed non-selection claim")
    else:
        if weights.get("status") == "NOT_MATERIAL" and not weights.get("not_material_rationale"):
            fail("NOT_MATERIAL weight sensitivity requires rationale")

    migration = data.get("dimension_migration", {})
    if migration.get("applicable"):
        if not migration.get("target_dimension_set"):
            fail("dimension migration requires target_dimension_set")
        if not migration.get("crosswalk_ref"):
            fail("dimension migration requires crosswalk_ref")
        if migration.get("comparability_status") == "NOT_APPLICABLE":
            fail("applicable dimension migration cannot use NOT_APPLICABLE comparability")
        if migration.get("rerun_required") and not migration.get("rerun_ref"):
            fail("required dimension rerun requires rerun_ref")
    else:
        if migration.get("record_dimension_set") != data.get("welfare_dimension_set_version"):
            fail("non-migrated record dimension set must match welfare_dimension_set_version")

    reliability = data.get("boundary_reliability", {})
    if use_class in ("REPEATED_INSTITUTIONAL_USE", "VALIDATION_STUDY"):
        if not reliability or reliability.get("applicable") is not True:
            fail("repeated institutional or validation use requires boundary_reliability block")
    if reliability.get("applicable"):
        contested = reliability.get("boundary_contested_rate")
        review_status = reliability.get("review_status")
        trigger = 0.10 if tier == 3 else 0.20
        if contested is not None and contested > trigger and review_status not in ("REVIEW_TRIGGERED", "REVISION_REQUIRED"):
            fail(f"boundary_contested_rate {contested:g} exceeds provisional review trigger {trigger:g}")
        if review_status in ("REVIEW_TRIGGERED", "REVISION_REQUIRED") and not reliability.get("review_ref"):
            fail("triggered boundary review requires review_ref")

    tokens = data.get("effect_tokens", [])
    token_ids = set()
    token_map = {}
    window_ids = set()
    for idx, token in enumerate(tokens):
        tid = token.get("token_id") or f"effect_tokens[{idx}]"
        if tid in token_ids:
            fail(f"duplicate token_id {tid}")
        token_ids.add(tid)
        token_map[tid] = token

        evidence = str(token.get("evidence_status", ""))
        if not evidence.startswith(EVIDENCE_PREFIX):
            fail(f"{tid}: evidence_status must use EVIDENCE_* namespace")

        tw = token.get("time_window", {})
        wid = tw.get("window_id")
        if not wid:
            fail(f"{tid}: time_window.window_id missing")
        elif wid in window_ids:
            # Shared windows are allowed, but must be explicitly the same. This is not an error.
            pass
        else:
            window_ids.add(wid)

        assignment = token.get("scope_assignment", {})
        primary = assignment.get("primary_scope")
        represented = assignment.get("represented_scopes", [])
        represented_set = set(represented)
        method = assignment.get("redundancy_method")
        if not represented_set.issubset(declared_scopes):
            fail(f"{tid}: represented scope lies outside declared_scopes")
        if primary and primary not in represented_set:
            fail(f"{tid}: primary_scope must be in represented_scopes")
        if method == "NOT_APPLICABLE" and len(represented) != 1:
            fail(f"{tid}: NOT_APPLICABLE requires exactly one represented scope")
        if method == "DEDUPLICATION" and not primary:
            fail(f"{tid}: DEDUPLICATION requires primary_scope")
        if method == "EMERGENT_SCALE_JUSTIFICATION" and len(represented) < 2:
            fail(f"{tid}: EMERGENT_SCALE_JUSTIFICATION requires at least two represented scopes")
        if len(represented) > 1 and method in (None, "NOT_APPLICABLE"):
            fail(f"{tid}: multi-scope representation requires a Canon redundancy method")
        if method == "ALLOCATION":
            allocation = assignment.get("allocation", [])
            if not allocation:
                fail(f"{tid}: ALLOCATION requires coefficients")
            total = sum(float(item.get("coefficient", 0)) for item in allocation)
            if total > 1 + 1e-12:
                fail(f"{tid}: allocation coefficients sum to {total:g} > 1")
            allocation_scopes = [item.get("scope") for item in allocation]
            if len(allocation_scopes) != len(set(allocation_scopes)):
                fail(f"{tid}: allocation scopes must be unique")
            if not set(allocation_scopes).issubset(represented_set):
                fail(f"{tid}: allocation scope not represented")
            residual = max(0.0, 1.0 - total)
            declared_residual = assignment.get("allocation_residual")
            if declared_residual is None or abs(float(declared_residual) - residual) > 1e-9:
                fail(f"{tid}: allocation_residual must equal 1 - sum(coefficients) = {residual:g}")
            residual_status = assignment.get("allocation_residual_status")
            if residual <= 1e-12 and residual_status != "NO_RESIDUAL":
                fail(f"{tid}: zero allocation residual requires NO_RESIDUAL")
            if residual > 1e-12:
                if residual_status in (None, "NO_RESIDUAL"):
                    fail(f"{tid}: nonzero allocation residual requires a classified status")
                if not assignment.get("allocation_residual_rationale"):
                    fail(f"{tid}: nonzero allocation residual requires rationale")

        if evidence == "EVIDENCE_UNKNOWN":
            for key in ("magnitude", "value", "score"):
                if token.get(key) == 0:
                    fail(f"{tid}: EVIDENCE_UNKNOWN cannot be represented as zero")
        if evidence == "EVIDENCE_NOT_MATERIAL":
            if not token.get("not_material_rationale"):
                fail(f"{tid}: EVIDENCE_NOT_MATERIAL requires not_material_rationale")
            if not token.get("reopen_trigger"):
                fail(f"{tid}: EVIDENCE_NOT_MATERIAL requires reopen_trigger")

        profile = token.get("profile", {})
        if tier in (2, 3) and not profile:
            fail(f"{tid}: Tier {tier} requires a dimension profile")
        if profile:
            if profile.get("aggregate_sign") == "BENEFICIAL" and profile.get("worst_subgroup_sign") == "HARMFUL" and not profile.get("worst_affected_subgroups"):
                fail(f"{tid}: harmful worst subgroup requires subgroup identification")

    path_ids = set()
    interactions = data.get("interactions", [])
    for idx, path in enumerate(interactions):
        pid = path.get("path_id") or f"interactions[{idx}]"
        if pid in path_ids:
            fail(f"duplicate path_id {pid}")
        path_ids.add(pid)
        source, target = path.get("source_token"), path.get("target_token")
        if source not in token_map:
            fail(f"{pid}: unknown source_token {source}")
        if target not in token_map:
            fail(f"{pid}: unknown target_token {target}")
        pathway_type = str(path.get("pathway_type", ""))
        evidence = str(path.get("evidence_status", ""))
        direction = str(path.get("direction", ""))
        if not pathway_type.startswith(PATHWAY_PREFIX):
            fail(f"{pid}: pathway_type must use PATHWAY_* namespace")
        if not evidence.startswith(EVIDENCE_PREFIX):
            fail(f"{pid}: evidence_status must use EVIDENCE_* namespace")
        if not direction.startswith(DIRECTION_PREFIX):
            fail(f"{pid}: direction must use DIRECTION_* namespace")

        if source in token_map and target in token_map:
            src_win = token_map[source].get("time_window", {}).get("window_id")
            tgt_win = token_map[target].get("time_window", {}).get("window_id")
            if path.get("source_window_id") and path.get("source_window_id") != src_win:
                fail(f"{pid}: source_window_id does not match source token")
            if path.get("target_window_id") and path.get("target_window_id") != tgt_win:
                fail(f"{pid}: target_window_id does not match target token")
            if src_win != tgt_win and not path.get("temporal_model_ref"):
                fail(f"{pid}: different source/target windows require temporal_model_ref")

            source_assignment = token_map[source].get("scope_assignment", {})
            target_assignment = token_map[target].get("scope_assignment", {})
            source_anchor = source_assignment.get("primary_scope") or (
                source_assignment.get("represented_scopes", [None])[0]
                if len(source_assignment.get("represented_scopes", [])) == 1 else None
            )
            target_anchor = target_assignment.get("primary_scope") or (
                target_assignment.get("represented_scopes", [None])[0]
                if len(target_assignment.get("represented_scopes", [])) == 1 else None
            )
            relation = path.get("scope_relation")
            if source_anchor is not None and target_anchor is not None:
                if source_anchor == target_anchor and relation == "CROSS_SCOPE":
                    fail(f"{pid}: CROSS_SCOPE conflicts with equal anchor scopes")
                if source_anchor != target_anchor and relation == "SAME_SCOPE":
                    fail(f"{pid}: SAME_SCOPE conflicts with different anchor scopes")

        if evidence == "EVIDENCE_UNKNOWN" and path.get("magnitude") == 0:
            fail(f"{pid}: EVIDENCE_UNKNOWN cannot be represented as zero magnitude")
        if pathway_type == "PATHWAY_NOT_MATERIAL" or evidence == "EVIDENCE_NOT_MATERIAL":
            if not path.get("not_material_rationale"):
                fail(f"{pid}: NOT_MATERIAL pathway requires not_material_rationale")
            if not path.get("reopen_trigger"):
                fail(f"{pid}: NOT_MATERIAL pathway requires reopen_trigger")

    unresolved = any(
        token.get("boundary_status") in ("BOUNDARY_CONTESTED", "BOUNDARY_UNKNOWN")
        or token.get("evidence_status") in ("EVIDENCE_CONTESTED", "EVIDENCE_UNKNOWN", "EVIDENCE_HYPOTHESIZED")
        for token in tokens
    ) or any(
        path.get("pathway_type") in ("PATHWAY_CONTESTED", "PATHWAY_UNKNOWN", "PATHWAY_HYPOTHESIZED")
        or path.get("evidence_status") in ("EVIDENCE_CONTESTED", "EVIDENCE_UNKNOWN", "EVIDENCE_HYPOTHESIZED")
        for path in interactions
    )
    status = data.get("record_status")
    if status == "WDBIP_RECORD_COMPLETE" and unresolved:
        fail("COMPLETE status incompatible with unresolved or hypothesized material items")
    if status == "WDBIP_RECORD_NOT_MATERIAL":
        if not data.get("not_material_rationale"):
            fail("NOT_MATERIAL status requires rationale")
        if not data.get("reopen_trigger"):
            fail("NOT_MATERIAL status requires reopen_trigger")

    sgp = data.get("sgp_link", {})
    if sgp.get("applicable") and not sgp.get("record_ref"):
        fail("applicable SGP link requires record_ref")

    return list(dict.fromkeys(errors))


def main():
    if len(sys.argv) not in (2, 3):
        print("usage: validate_wdbip_v1_4.py RECORD.json [SCHEMA.json]", file=sys.stderr)
        return 2
    record = Path(sys.argv[1])
    schema = Path(sys.argv[2]) if len(sys.argv) == 3 else Path(__file__).with_name("wdbip_record_v1_4.schema.json")
    errors = validate(record, schema)
    if errors:
        print("WDBIP v1.4 INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("WDBIP v1.4 VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
