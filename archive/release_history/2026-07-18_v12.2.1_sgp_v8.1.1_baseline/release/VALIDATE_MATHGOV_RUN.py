#!/usr/bin/env python3
"""Validate MathGov run-record completeness and cascade semantics.

This is a conformance checker, not a reference calculator, evidence verifier,
legal instrument, or moral-truth engine. It intentionally uses only the Python
standard library so a release recipient can replay it without extra packages.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

REQUIRED_TOP = [
    "identity", "decision", "profile_and_stakes", "evidence_and_claim_boundary",
    "parameter_lock", "stakeholders", "options", "gate_results", "ranking",
    "decision_state", "authority_and_execution", "controls_monitoring_and_reopen",
    "audit_and_signoff",
]
CSV_SELECTABLE = {"CSV_PASS", "CSV_PASS_WITH_CONTROLS", "CSV_NOT_MATERIAL"}
FINAL_WITH_SELECTION = {"SELECTED_DECISIVE", "SELECTED_BY_AUTHORITY_NON_DECISIVE", "PROVISIONAL_WITH_CONTROLS", "EMERGENCY_PROVISIONAL"}


def nonempty(value):
    return value not in (None, "", [], {})


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"missing top-level object: {key}")
    if errors:
        return errors

    ident = data["identity"]
    if ident.get("canon_version") != "v12.2.1":
        errors.append("identity.canon_version must be v12.2.1")
    if ident.get("sgp_version") not in {"v8.1.1", "NOT_TRIGGERED"}:
        errors.append("identity.sgp_version must be v8.1.1 or NOT_TRIGGERED")

    decision = data["decision"]
    option_ids = decision.get("option_ids") or []
    if len(set(option_ids)) != len(option_ids) or len(option_ids) < 2:
        errors.append("decision.option_ids must contain at least two unique IDs")
    options = data["options"]
    declared = [o.get("id") for o in options]
    if set(declared) != set(option_ids):
        errors.append("decision.option_ids and options[].id must match exactly")

    lock = data["parameter_lock"]
    if lock.get("locked") is not True:
        errors.append("parameter_lock.locked must be true")
    for name in ["locked_utc", "evidence_cutoff_utc", "amendment_policy"]:
        if not nonempty(lock.get(name)):
            errors.append(f"parameter_lock.{name} is required")
    for p in lock.get("parameters", []):
        status = p.get("status")
        if status == "UNKNOWN" and p.get("used_in_arithmetic"):
            errors.append(f"parameter {p.get('name')!r}: UNKNOWN cannot enter arithmetic")
        if status == "NOT_MATERIAL" and not nonempty(p.get("not_material_rationale")):
            errors.append(f"parameter {p.get('name')!r}: NOT_MATERIAL requires rationale")
        for name in ["name", "status", "source"]:
            if not nonempty(p.get(name)):
                errors.append(f"parameter entry missing {name}")

    evidence = data["evidence_and_claim_boundary"]
    for name in ["reality_surface", "evidence_trace", "consequence_pathways", "claim_boundary", "rg_status"]:
        if not nonempty(evidence.get(name)):
            errors.append(f"evidence_and_claim_boundary.{name} is required")

    gate_rows = data["gate_results"]
    by_id = {r.get("option_id"): r for r in gate_rows}
    if set(by_id) != set(option_ids) or len(by_id) != len(gate_rows):
        errors.append("gate_results must contain exactly one row per option")
    selectable_ids = set()
    for oid in option_ids:
        row = by_id.get(oid)
        if not row:
            continue
        expected = (
            row.get("rg") in {"RG_SUPPORTED", "RG_NARROWED"}
            and row.get("rf") == "RF_PASS"
            and row.get("trc") == "TRC_PASS"
            and row.get("csv") in CSV_SELECTABLE
        )
        if bool(row.get("selectable")) != expected:
            errors.append(f"{oid}: selectable flag contradicts RG/RF/TRC/CSV states")
        if expected:
            selectable_ids.add(oid)

    ranking = data["ranking"]
    ranked = ranking.get("ranked_option_ids") or []
    extra_ranked = set(ranked) - selectable_ids
    if extra_ranked:
        errors.append(f"ranking includes non-selectable option(s): {sorted(extra_ranked)}")
    if ranking.get("method") == "NOT_APPLICABLE" and ranked:
        errors.append("ranking.method NOT_APPLICABLE cannot have ranked_option_ids")
    if ranking.get("method") != "NOT_APPLICABLE" and selectable_ids and set(ranked) != selectable_ids:
        errors.append("ranking must include every and only selectable option when ranking is applied")

    state = data["decision_state"]
    final_state = state.get("state")
    selected = state.get("selected_option_id")
    if final_state in FINAL_WITH_SELECTION:
        if selected not in selectable_ids and final_state != "EMERGENCY_PROVISIONAL":
            errors.append("selected option must be selectable for ordinary selection states")
        if selected is None:
            errors.append("selected_option_id required for selection state")
    elif selected is not None:
        errors.append("selected_option_id must be null for a non-selection state")
    if final_state == "SELECTED_DECISIVE" and ranking.get("decisive") is not True:
        errors.append("SELECTED_DECISIVE requires ranking.decisive=true")
    if final_state == "SELECTED_BY_AUTHORITY_NON_DECISIVE":
        if ranking.get("decisive") is not False:
            errors.append("authority non-decisive selection requires ranking.decisive=false")
        if not nonempty(state.get("authority_selection_rationale")):
            errors.append("authority non-decisive selection requires authority_selection_rationale")
    if final_state == "NO_SELECTABLE_OPTION" and selectable_ids:
        errors.append("NO_SELECTABLE_OPTION contradicts nonempty selectable set")

    auth = data["authority_and_execution"]
    executing = auth.get("execution_state") in {"AUTHORIZED_WITHIN_SCOPE", "EXECUTED_UNDER_MONITORING"}
    if executing and auth.get("authority_basis_present") is not True:
        errors.append("execution authorization requires authority_basis_present=true")
    if executing and (not nonempty(auth.get("authority_role")) or not nonempty(auth.get("mandate_scope"))):
        errors.append("execution authorization requires authority_role and mandate_scope")
    if final_state == "SELECTED_BY_AUTHORITY_NON_DECISIVE" and auth.get("authority_basis_present") is not True:
        errors.append("authority selection requires authority basis")

    controls = data["controls_monitoring_and_reopen"]
    if controls.get("material_change_requires_requalification") is not True:
        errors.append("material_change_requires_requalification must be true")
    if not nonempty(controls.get("reopen_triggers")):
        errors.append("at least one reopen trigger is required")
    if any(by_id.get(oid, {}).get("csv") == "CSV_PASS_WITH_CONTROLS" for oid in selectable_ids):
        if not nonempty(controls.get("controls")) or not nonempty(controls.get("monitoring")):
            errors.append("CSV_PASS_WITH_CONTROLS requires controls and monitoring")

    profile = data["profile_and_stakes"]
    if profile.get("profile") == "QUICK" and profile.get("tier") != 1:
        errors.append("QUICK profile must use Tier 1")
    if profile.get("profile") == "AUDIT" and profile.get("tier") != 3:
        errors.append("AUDIT profile must use Tier 3")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("record", type=Path)
    ap.add_argument("--expect-fail", action="store_true")
    args = ap.parse_args()
    try:
        data = json.loads(args.record.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: cannot parse {args.record}: {exc}")
        return 0 if args.expect_fail else 1
    errors = validate(data)
    if errors:
        print("FAIL:")
        for e in errors:
            print(f"- {e}")
        return 0 if args.expect_fail else 1
    print("PASS: R0 record completeness and R1 cascade conformance checks")
    return 1 if args.expect_fail else 0

if __name__ == "__main__":
    raise SystemExit(main())
