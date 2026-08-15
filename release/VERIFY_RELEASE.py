#!/usr/bin/env python3
"""Master verifier for MathGov Core v12.6 / SGP v8.5 build 2026.08.15.3."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SKIP_HASHES = "--skip-hashes" in sys.argv
RELEASE_ID = "MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3"
PACKAGE_NAME = "MathGov_Core_2026_09_v12_6_SGP_v8_5_BUILD_2026_08_15_3_FINAL_PUBLICATION_READY"
BUILD_ID = "2026.08.15.3"
SCHEMA_CONTRACT = "v4-build-2026.08.15.3"


def fail(message: str) -> None:
    raise SystemExit(f"VERIFY FAIL: {message}")


def run(command: list[str], label: str) -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=env)
    if result.returncode:
        fail(f"{label}\n{result.stdout}{result.stderr}")
    if result.stdout.strip():
        print(result.stdout.strip())


required_reports = [
    "release/MATHGOV_V12_6_CLAUDE_ADVERSARIAL_AUDIT_DISPOSITION_2026_08_11.md",
    "release/MATHGOV_V12_6_CLAUDE_ADVERSARIAL_AUDIT_DISPOSITION_2026_08_11.docx",
    "release/MATHGOV_V12_6_CLAUDE_ADVERSARIAL_AUDIT_DISPOSITION_2026_08_11.pdf",
    "release/V12_6_BUILD_2026_08_11_2_CHANGE_LEDGER.json",
    "release/V12_6_BUILD_2026_08_15_3_CHANGE_LEDGER.json",
    "release/GITHUB_AND_WEBSITE_RELEASE_READINESS_REPORT_2026_08_15.md",
    "release/FABLE_FINAL_RELEASE_AUDIT.md",
    "release/FINAL_VERIFICATION_REPORT.md",
    "release/RELEASE_NOTES.md",
    "release/DOCX_TABLE_AND_LAYOUT_AUDIT_v12_6.json",
    "release/WORKBOOK_FORMULA_CACHE_AUDIT.json",
    "release/DOCX_ACCESSIBILITY_AUDIT.json",
    "release/PDF_PREFLIGHT_ALL_FINAL.json",
]
for rel in required_reports:
    if not (ROOT / rel).is_file():
        fail(f"missing release artifact {rel}")

for rel in (
    "docs/agents/recursive_successor/profiles/RECURSIVE_SUCCESSOR_RUNTIME_PROFILE_v1_0.yaml",
    "docs/agents/recursive_successor/schemas/successor_integrity_record_v1_0.schema.json",
    "docs/agents/recursive_successor/tests/validate_successor_profile.py",
):
    if not (ROOT / rel).is_file():
        fail(f"missing Agent v12.5 successor-integrity artifact {rel}")


manifest = yaml.safe_load((ROOT / "VERSION_MANIFEST.yaml").read_text(encoding="utf-8"))
if manifest.get("release_id") != RELEASE_ID or manifest.get("exact_release_version") != "v12.6":
    fail("release identity")
if manifest.get("governing_cascade") != "RG -> RF/NCRC -> TRC -> CSV -> RLS":
    fail("governing cascade")
if manifest.get("release_date") != "2026-08-15" or manifest.get("publication_date") != "2026-08-15":
    fail("release or publication date")
if manifest.get("package_name") != PACKAGE_NAME:
    fail("package name")
if manifest.get("build_id") != BUILD_ID or manifest.get("build_date") != "2026-08-15":
    fail("build identity")
if manifest.get("schema_contract_revision") != SCHEMA_CONTRACT:
    fail("schema contract revision")

ledger = json.loads((ROOT / "release/V12_6_BUILD_2026_08_15_3_CHANGE_LEDGER.json").read_text(encoding="utf-8"))
if ledger.get("release_id") != RELEASE_ID or ledger.get("build_id") != BUILD_ID:
    fail("change-ledger identity")
if ledger.get("semantic_versions_changed") is not False:
    fail("final-freeze build semantic-version declaration")
if ledger.get("governing_cascade") != "RG -> RF/NCRC -> TRC -> CSV -> RLS":
    fail("change-ledger cascade")

cff = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
if str(cff.get("version")) != "12.6" or str(cff.get("date-released")) != "2026-08-15":
    fail("citation metadata")

configuration = manifest.get("configuration_assurance_release", {})
required_flags = (
    "evidence_stage_non_substitution",
    "projection_locked_test_boundary",
    "capability_claim_integrity",
    "composition_reductionism_non_substitution",
    "sensitivity_non_decisiveness_enforced",
    "measurement_resolution_declared",
    "appendix_b_standalone_completeness",
    "empty_set_dispositions_explicit",
    "nondefault_catastrophe_weight_governance",
    "post_saturation_threshold_scale_clarified",
    "emergency_tie_ordering_clarified",
    "rights_relevance_routing_clarified",
    "computational_context_preflight",
    "computational_context_derived_view",
    "consequence_interface_authority_noncollapse",
)
for flag in required_flags:
    if configuration.get(flag) is not True:
        fail(f"configuration flag {flag}")

maturity = (ROOT / "docs/assurance/SCIENTIFIC_MATURITY_LADDER.md").read_text(encoding="utf-8")
for token in (
    "## Evidence-stage non-substitution matrix",
    "Implementation conformance",
    "Projection and calibration lock",
    "Controlled empirical contact",
    "Operational qualification",
    "Outcome and requalification evidence",
    "**No-upward-inference rule.**",
):
    if token not in maturity:
        fail(f"scientific maturity ladder missing {token}")

canon = (ROOT / "docs/canon/RippleLogic_v12.6_Canon.md").read_text(encoding="utf-8")
canon_tokens = (
    "Gate-numbering clarification (Normative). Formal gate numbering counts only the three hard admissibility/selectability gates",
    "Cross-tier computed-sensitivity rule (Normative).",
    "Measurement-resolution rule (Normative).",
    "RLS_NO_ACTIVE_MASS",
    "CONTAINMENT_MAP_INCOMPLETE",
    "UCI_UNAVAILABLE",
    "Rights-relevance cue",
    "Catastrophe-weight governance (Normative).",
    "Threshold-scale clarification (Normative).",
    "Emergency comparison tie rule (Normative).",
    "G_RF` MUST NOT be empty for a material rights-covered cell",
)
for token in canon_tokens:
    if token not in canon:
        fail(f"Canon correction surface missing: {token}")

wdbip = (ROOT / "docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.md").read_text(encoding="utf-8")
for token in (
    "Rights-routing clarification (Normative).",
    "D6 records experiential meaning and cultural continuity",
    "D7 records environmental condition",
):
    if token.lower() not in wdbip.lower():
        fail(f"WDBIP rights-routing surface missing: {token}")

ripple = (ROOT / "docs/standards/ripple_md_Standard_v5.5.md").read_text(encoding="utf-8")
agent = (ROOT / "docs/agents/RippleLogic_Agent_System_v12.5.md").read_text(encoding="utf-8")
for token in ("Computational Context Preflight", "Section 50A: Computational Context Preflight before authorization", "Consequence interface ≠ legitimate authority"):
    if token not in agent:
        fail(f"Agent System computational-context surface missing: {token}")
if "Capability Claim Integrity and Capability-Authority Fields (Conditional; Canon §2.1C)" not in ripple:
    fail("ripple.md Capability Claim Integrity discoverability")
for token in ("Computational Context Decision Note View", "computational_context:", "A consequence-bearing output path and legitimate authority are separate properties"):
    if token not in ripple:
        fail(f"ripple.md computational-context surface missing: {token}")
sgp = (ROOT / "docs/sgp/SGP_v8.5.md").read_text(encoding="utf-8")
if "Capability Claim Integrity cross-reference (Normative; Canon §2.1C)" not in sgp:
    fail("SGP Capability Claim Integrity discoverability")

release_report = (ROOT / "release/GITHUB_AND_WEBSITE_RELEASE_READINESS_REPORT_2026_08_15.md").read_text(encoding="utf-8")
for token in (
    f"**Exact build:** `{RELEASE_ID}`",
    "Computational Context Preflight",
    "Consequence interface is not legitimate authority",
    "do not create a sixth gate",
):
    if token not in release_report:
        fail(f"current release-readiness report drift: {token}")

examples_index = (ROOT / "docs/examples/README.md").read_text(encoding="utf-8")
for token in (
    "Bounded AI-tutor pilot",
    "Controlled congestion-pricing pilot",
    "NEGATIVE_EXAMPLES_INDEX.md",
    "SCIENTIFIC_MATURITY_LADDER.md",
):
    if token not in examples_index:
        fail(f"examples index missing {token}")
negative_index = (ROOT / "docs/examples/NEGATIVE_EXAMPLES_INDEX.md").read_text(encoding="utf-8")
for token in ("fail_rank_nonselectable.json", "fail_execution_without_authority.json", "fail_capability_material_without_record.json"):
    if token not in negative_index:
        fail(f"negative-example index missing {token}")
for asset in ("release/assets/cascade_overview.svg", "release/assets/cascade_overview.png"):
    if not (ROOT / asset).is_file():
        fail(f"missing cascade asset {asset}")
print("PASS exact release identity, change ledger, correction surfaces, and claim boundaries")

subordinates = [
    "VERIFY_CURRENT_PINS.py",
    "VERIFY_AUDIT_FLAG_REGISTRY.py",
    "VERIFY_SEMANTIC_SURFACES.py",
    "VERIFY_STATE_SEMANTICS_AND_NON_DILUTION.py",
    "VERIFY_FORMULA_INTERFACE_INTEGRITY.py",
    "VERIFY_WORKBOOK_LIVE_RECALCULATION.py",
    "VERIFY_FORMAT_AND_REPRODUCIBILITY.py",
    "VERIFY_DOCX_TABLE_STYLE.py",
    "VERIFY_RELEASE_REALITY_COHERENCE.py",
]
for name in subordinates:
    run([sys.executable, str(ROOT / "release" / name), str(ROOT)], name)
print("PASS nine subordinate verification surfaces")

expected_core = {
    "CSV_Gate_Standard_v2.4.docx",
    "MATHGOV_3R_1_2_PUBLIC_INTRO_v12_6.docx",
    "MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.4.docx",
    "Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.3.docx",
    "Physical_Causal_Admissibility_Evidence_Profile_v2.3.docx",
    "RippleLogic_Agent_System_v12.5.docx",
    "RippleLogic_Aligners_Sheet_v5.6.xlsx",
    "RippleLogic_Cascade_Standard_v2.6.docx",
    "RippleLogic_Foundations_Primer_v4.4.docx",
    "RippleLogic_RLS_Validation_Protocol_v2_6.docx",
    "RippleLogic_v12.6_Canon.docx",
    "SGP_v8.5.docx",
    "Source_Coupling_Integrity_Standard_v2.3.docx",
    "Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.docx",
    "ripple_md_Standard_v5.5.docx",
}
actual_core = {p.name for p in (ROOT / "core_15").iterdir() if p.is_file() and p.name != "README.md"}
if actual_core != expected_core:
    fail(f"Core 15 inventory missing={expected_core-actual_core} extra={actual_core-expected_core}")
for name in expected_core:
    path = ROOT / "core_15" / name
    if path.suffix.lower() in {".docx", ".xlsx"} and path.read_bytes()[:4] != b"PK\x03\x04":
        fail(f"invalid OOXML {name}")
print("PASS exact Core 15 inventory and OOXML integrity")

run_validator_path = ROOT / "release/VALIDATE_MATHGOV_RUN.py"
run_validator_spec = importlib.util.spec_from_file_location("mathgov_run_validator", run_validator_path)
if run_validator_spec is None or run_validator_spec.loader is None:
    fail("run-record validator import")
run_validator = importlib.util.module_from_spec(run_validator_spec)
sys.modules[run_validator_spec.name] = run_validator
run_validator_spec.loader.exec_module(run_validator)


def validate_run_record(path: Path, expect_fail: bool) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        if expect_fail:
            print(f"PASS expected rejection vector: {path.relative_to(ROOT)} (parse: {exc})")
            return
        fail(f"run pass {path.name}: parse: {exc}")
    v0_errors, _ = run_validator.r0(data)
    v1_errors = []
    if not v0_errors:
        v1_errors, _ = run_validator.r1(data)
    rejected = bool(v0_errors or v1_errors)
    if expect_fail:
        if not rejected:
            fail(f"expected-failure vector unexpectedly conformed: {path.relative_to(ROOT)}")
        print(f"PASS expected rejection vector: {path.relative_to(ROOT)}")
        return
    if rejected:
        fail(f"positive run vector {path.relative_to(ROOT)}\n" + "\n".join(v0_errors + v1_errors))
    readiness = run_validator.r2(data)
    print(f"PASS run vector: {path.relative_to(ROOT)}; V2={'REVIEW_REQUIRED' if readiness else 'NO_AUTOMATED_ISSUES_DETECTED'}")


pass_runs = sorted((ROOT / "tests/run_records").glob("pass_*.json"))
fail_runs = sorted((ROOT / "tests/run_records").glob("fail_*.json"))
if len(pass_runs) != 6 or len(fail_runs) != 30:
    fail(f"run-vector inventory {len(pass_runs)} pass/{len(fail_runs)} fail")
for path in pass_runs:
    validate_run_record(path, expect_fail=False)
for path in fail_runs:
    validate_run_record(path, expect_fail=True)
examples = [
    ROOT / "docs/examples/reproducibility/reusable_cups_run_v4.json",
    ROOT / "docs/examples/reference_replays/ai_tutor_pilot/run_record_v4.json",
    ROOT / "docs/examples/reference_replays/congestion_pricing_pilot/run_record_v4.json",
]
for example in examples:
    validate_run_record(example, expect_fail=False)
print("PASS run-record v4 fixtures: 6 positive / 30 expected failures / 3 active reference replay examples")

sgp_schema = json.loads((ROOT / "schemas/sgp_rmcp_record_v8_4.schema.json").read_text(encoding="utf-8"))
sgp_validator = Draft202012Validator(sgp_schema)
sgp_pass = sorted((ROOT / "tests/sgp_rmcp").glob("pass_*.json"))
sgp_fail = sorted((ROOT / "tests/sgp_rmcp").glob("fail_*.json"))
if len(sgp_pass) != 1 or len(sgp_fail) != 1:
    fail("SGP RMCP vector inventory")
for path in sgp_pass:
    if list(sgp_validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))):
        fail(f"SGP positive fixture {path.name}")
for path in sgp_fail:
    if not list(sgp_validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))):
        fail(f"SGP expected-failure fixture {path.name}")
print("PASS SGP RMCP v8.4 fixtures: 1 positive / 1 expected failure")

wdbip_validator_path = ROOT / "docs/standards/wdbip/validate_wdbip_v1_6.py"
spec = importlib.util.spec_from_file_location("wdbip_validator", wdbip_validator_path)
if spec is None or spec.loader is None:
    fail("WDBIP validator import")
wdbip_module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = wdbip_module
spec.loader.exec_module(wdbip_module)
wdbip_schema = ROOT / "docs/standards/wdbip/wdbip_record_v1_6.schema.json"
wdbip_pass = sorted((ROOT / "docs/standards/wdbip/tests").glob("pass_*.json"))
wdbip_fail = sorted((ROOT / "docs/standards/wdbip/tests").glob("fail_*.json"))
if len(wdbip_pass) != 1 or len(wdbip_fail) != 18:
    fail("WDBIP vector inventory")
for path in wdbip_pass:
    if wdbip_module.validate(path, wdbip_schema):
        fail(f"WDBIP positive fixture {path.name}")
for path in wdbip_fail:
    if not wdbip_module.validate(path, wdbip_schema):
        fail(f"WDBIP expected-failure fixture {path.name}")
print("PASS WDBIP v1.6 fixtures: 1 positive / 18 expected failures")

layout = json.loads((ROOT / "release/DOCX_TABLE_AND_LAYOUT_AUDIT_v12_6.json").read_text(encoding="utf-8"))
totals = layout.get("totals", {})
if layout.get("status") != "PASS":
    fail("layout audit status")
expected_layout = {
    "documents": 15,
    "tables": 287,
    "table_rows": 2444,
    "headings": 1646,
    "pages": 595,
    "toc_entries": 125,
}
for key, value in expected_layout.items():
    if totals.get(key) != value:
        fail(f"layout audit metric {key}: {totals.get(key)} != {value}")
for key in ("comments_parts", "tracked_changes", "content_controls", "blank_pdf_pages", "confirmed_page_boundary_failures", "tiny_font_spans_under_6pt"):
    if totals.get(key) != 0:
        fail(f"layout audit defect {key}")

a11y = json.loads((ROOT / "release/DOCX_ACCESSIBILITY_AUDIT.json").read_text(encoding="utf-8"))
sev = a11y.get("totals", {}).get("findings_by_severity", {})
if a11y.get("release_id") != RELEASE_ID or sev != {"high": 0, "medium": 0, "low": 72}:
    fail("DOCX accessibility audit")

workbook = json.loads((ROOT / "release/WORKBOOK_FORMULA_CACHE_AUDIT.json").read_text(encoding="utf-8"))
if workbook.get("release_id") != RELEASE_ID or workbook.get("status") != "PASS":
    fail("workbook audit identity or status")
if workbook.get("worksheet_count") != 87 or workbook.get("formula_count") != 1643 or workbook.get("formula_error_cells") != 0:
    fail("workbook audit metrics")
if workbook.get("independent_recalculation", {}).get("status") != "PASS" or workbook.get("mirror", {}).get("byte_identical") is not True:
    fail("workbook live recalculation or exact mirror")

preflight = json.loads((ROOT / "release/PDF_PREFLIGHT_ALL_FINAL.json").read_text(encoding="utf-8"))
if preflight.get("release_id") != RELEASE_ID or preflight.get("status") != "PASS":
    fail("PDF preflight identity or status")
if preflight.get("documents") != 16 or preflight.get("pages") != 610 or preflight.get("warning_count") != 0:
    fail("PDF preflight metrics")
print("PASS publication, accessibility, workbook, and PDF-preflight metrics")

for path in ROOT.rglob("*"):
    if path.is_dir() and path.name == "__pycache__":
        fail(f"bytecode directory {path.relative_to(ROOT)}")
    if path.is_file() and path.suffix.lower() in {".pyc", ".pyo", ".tmp", ".bak", ".swp"}:
        fail(f"ephemeral source artifact {path.relative_to(ROOT)}")
    if path.is_file() and (path.name.startswith(".~lock.") or path.name.startswith("~$") or path.name in {".DS_Store", "Thumbs.db"}):
        fail(f"ephemeral office or editor artifact {path.relative_to(ROOT)}")
print("PASS public-source hygiene")

if not SKIP_HASHES:
    release_manifest = yaml.safe_load((ROOT / "release/release_manifest.yml").read_text(encoding="utf-8"))
    if release_manifest.get("release_id") != RELEASE_ID or release_manifest.get("build_id") != BUILD_ID:
        fail("release manifest identity")
    active_files = set(release_manifest.get("active_files", []))
    ledger_entries: dict[str, str] = {}
    for line in (ROOT / "release/SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            ledger_entries[rel] = digest
    if active_files != set(ledger_entries):
        fail("release manifest and SHA-256 ledger inventory differ")
    for rel, digest in ledger_entries.items():
        path = ROOT / rel
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            fail(f"SHA-256 mismatch {rel}")
    core_entries: dict[str, str] = {}
    for line in (ROOT / "release/SHA256SUMS_CORE15.txt").read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            core_entries[rel] = digest
    if {Path(rel).name for rel in core_entries} != expected_core:
        fail("Core 15 hash-ledger inventory")
    for rel, digest in core_entries.items():
        if hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() != digest:
            fail(f"Core 15 SHA-256 mismatch {rel}")
    print(f"PASS release SHA-256 ledger ({len(ledger_entries)} files) and Core 15 ledger")
else:
    print("PASS hash verification explicitly skipped")

print("FINAL VERIFICATION: PASS")
print("Claim boundary: artifact and tested-interface conformance only; construct validity remains UNTESTED.")
