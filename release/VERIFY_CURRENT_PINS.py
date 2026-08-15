#!/usr/bin/env python3
"""Verify the active v12.6 identity and exact component pins."""
from __future__ import annotations
import json, re, sys, zipfile
from pathlib import Path
import yaml

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
RELEASE_ID = "MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3"

def fail(message: str) -> None:
    raise SystemExit(f"FAIL current pins: {message}")

def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")

manifest = yaml.safe_load(text("VERSION_MANIFEST.yaml"))
if manifest.get("release_id") != RELEASE_ID:
    fail("release_id")
if manifest.get("release_date") != "2026-08-15" or manifest.get("package_name") != "MathGov_Core_2026_09_v12_6_SGP_v8_5_BUILD_2026_08_15_3_FINAL_PUBLICATION_READY":
    fail("release date or package name")
if manifest.get("publication_date") != "2026-08-15" or manifest.get("build_id") != "2026.08.15.3" or manifest.get("build_date") != "2026-08-15":
    fail("publication/build identity")
if manifest.get("schema_contract_revision") != "v4-build-2026.08.15.3":
    fail("schema contract revision")
if manifest.get("exact_release_version") != "v12.6" or manifest.get("release_line") != "v12.6":
    fail("release line")
if manifest.get("governing_cascade") != "RG -> RF/NCRC -> TRC -> CSV -> RLS":
    fail("five-stage cascade")

expected = {
    "docs/canon/RippleLogic_v12.6_Canon.md": "v12.6",
    "docs/sgp/SGP_v8.5.md": "v8.5",
    "docs/standards/ripple_md_Standard_v5.5.md": "v5.5",
    "docs/agents/RippleLogic_Agent_System_v12.5.md": "v12.5",
    "docs/standards/CSV_Gate_Standard_v2.4.md": "v2.4",
    "docs/standards/RippleLogic_Cascade_Standard_v2.6.md": "v2.6",
    "docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.4.md": "v1.4",
    "docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.md": "v1.6",
    "docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_6.md": "v2.6",
    "docs/primer/RippleLogic_Foundations_Primer_v4.4.md": "v4.4",
    "docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_6.md": "v12.6",
    "docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.3.md": "v2.3",
    "docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.3.md": "v2.3",
    "docs/standards/Source_Coupling_Integrity_Standard_v2.3.md": "v2.3",
}
for rel, version in expected.items():
    path = ROOT / rel
    if not path.is_file() or version.lower() not in text(rel).lower():
        fail(f"missing or unpinned {rel}")

core_expected = {
    "RippleLogic_v12.6_Canon.docx", "SGP_v8.5.docx", "ripple_md_Standard_v5.5.docx",
    "RippleLogic_Agent_System_v12.5.docx", "CSV_Gate_Standard_v2.4.docx",
    "RippleLogic_Cascade_Standard_v2.6.docx", "MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.4.docx",
    "Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.docx",
    "RippleLogic_RLS_Validation_Protocol_v2_6.docx", "RippleLogic_Foundations_Primer_v4.4.docx",
    "MATHGOV_3R_1_2_PUBLIC_INTRO_v12_6.docx",
    "Physical_Causal_Admissibility_Evidence_Profile_v2.3.docx",
    "Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.3.docx",
    "Source_Coupling_Integrity_Standard_v2.3.docx", "RippleLogic_Aligners_Sheet_v5.6.xlsx",
}
actual = {p.name for p in (ROOT / "core_15").iterdir() if p.is_file() and p.name != "README.md"}
if actual != core_expected:
    fail(f"Core 15 mismatch missing={core_expected-actual} extra={actual-core_expected}")
for p in (ROOT / "core_15").iterdir():
    if p.suffix.lower() in {".docx", ".xlsx"} and p.read_bytes()[:4] != b"PK\x03\x04":
        fail(f"not genuine OOXML: {p.name}")

schema = json.loads(text("schemas/mathgov_run_record_v4.schema.json"))
if schema["properties"]["identity"]["properties"]["package_release_id"].get("const") != RELEASE_ID:
    fail("run-record v4 release binding")
for field in ("qualified_option_id", "action_instance_id", "action_specification_hash", "qualification_snapshot_hash"):
    if field not in schema["properties"]["configuration_assurance"]["properties"]:
        fail(f"run-record v4 missing {field}")

# Active human-readable pin mirrors must exactly match the manifest.
active_pin_requirements = {
    "START_HERE.md": [
        "ripple.md Standard v5.5",
        "Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.md",
        "RippleLogic Aligners Sheet v5.6",
    ],
    "START_HERE_RELEASE_INDEX_v12.6.md": [
        "ripple.md Standard v5.5",
        "Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.md",
        "RippleLogic Aligners Sheet v5.6",
    ],
    "docs/CORE_COMPONENT_MAP.md": [
        "| Sentience Gradient Protocol | v8.5 |",
        "| CSV Gate Standard | v2.4 |",
        "| RippleLogic Cascade Standard | v2.6 |",
        "| WDBIP | v1.6 |",
        "| RLS Validation Protocol | v2.6 |",
        "| PC-AEP | v2.3 |",
        "| MFDI Standard | v2.3 |",
        "| Source-Coupling Integrity Standard | v2.3 |",
    ],
    "docs/implementation/NORMATIVE_KERNEL_INDEX_v1.0.yaml": [
        "Canon CSV sections and CSV Gate Standard v2.4",
    ],
    "docs/canon/RippleLogic_v12.6_Canon.md": [
        "- SGP: v8.5", "- Cascade Standard: v2.6", "- CSV Gate Standard: v2.4",
        "- RLS Validation Protocol: v2.6", "- PC-AEP: v2.3", "- MFDI: v2.3",
        "- Source-Coupling Integrity Standard: v2.3", "Companion v8.5 interface note",
    ],
    "docs/sgp/SGP_v8.5.md": [
        "Current conformance is governed by the active v8.5 sections",
    ],
    "docs/agents/RippleLogic_Agent_System_v12.5.md": [
        "Current release-line note (August 2026)", "SGP: v8.5",
    ],
    "docs/standards/RippleLogic_Cascade_Standard_v2.6.md": [
        "ripple.md v5.5 governs consequence-tempo",
    ],
}
for rel, tokens in active_pin_requirements.items():
    value = text(rel)
    for token in tokens:
        if token not in value:
            fail(f"active pin mirror {rel}: {token}")

for rel, forbidden in {
    "START_HERE.md": ["Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.md"],
    "START_HERE_RELEASE_INDEX_v12.6.md": ["ripple.md Standard v5.4", "Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.md", "RippleLogic Aligners Sheet v5.5"],
    "docs/CORE_COMPONENT_MAP.md": ["| Sentience Gradient Protocol | v8.4 |", "| CSV Gate Standard | v2.3 |", "| RippleLogic Cascade Standard | v2.5 |", "| WDBIP | v1.5 |", "| RLS Validation Protocol | v2.5 |", "| PC-AEP | v2.2 |", "| MFDI Standard | v2.2 |", "| Source-Coupling Integrity Standard | v2.2 |"],
    "docs/implementation/NORMATIVE_KERNEL_INDEX_v1.0.yaml": ["CSV Gate Standard v2.3"],
}.items():
    value = text(rel)
    if any(token in value for token in forbidden):
        fail(f"stale active pin mirror {rel}")

def docx_body_text(rel: str) -> str:
    with zipfile.ZipFile(ROOT / rel) as archive:
        raw = archive.read("word/document.xml").decode("utf-8", errors="replace")
    return re.sub(r"<[^>]+>", "", raw)

for rel, required_tokens, forbidden_tokens in [
    ("docs/CORE_COMPONENT_MAP.docx", ["MathGov Core Component Map - v12.6 / SGP v8.5", "v5.5", "v5.6"], ["MathGov Core Component Map - v12.5 / SGP v8.4"]),
    ("docs/canon/RippleLogic_v12.6_Canon.docx", ["SGP: v8.5", "Cascade Standard: v2.6", "CSV Gate Standard: v2.4", "RLS Validation Protocol: v2.6", "Companion v8.5 interface note"], ["SGP: v8.4", "Cascade Standard: v2.5", "CSV Gate Standard: v2.3", "RLS Validation Protocol: v2.5"]),
    ("docs/sgp/SGP_v8.5.docx", ["Current conformance is governed by the active v8.5 sections"], ["Current conformance is governed by the active v8.4 sections"]),
    ("docs/agents/RippleLogic_Agent_System_v12.5.docx", ["Current release-line note (August 2026)", "SGP: v8.5"], ["Current release-line note (July 2026): Governing framework is RippleLogic Canon v12.6; SGP is pinned to v8.4"]),
]:
    value = docx_body_text(rel)
    if any(token not in value for token in required_tokens) or any(token in value for token in forbidden_tokens):
        fail(f"DOCX active pin mirror {rel}")

wdbip = json.loads(text("docs/standards/wdbip/wdbip_record_v1_6.schema.json"))
if wdbip["properties"]["protocol_version"].get("const") != "WDBIP v1.6":
    fail("WDBIP protocol pin")
if wdbip["properties"]["canon_version"].get("const") != "RippleLogic v12.6":
    fail("WDBIP Canon pin")

reality = yaml.safe_load(text("docs/assurance/RELEASE_REALITY_REGISTER_v1.0.yaml"))
if reality.get("release_id") != RELEASE_ID or reality.get("build_id") != "2026.08.15.3":
    fail("release-reality build identity")

cff = yaml.safe_load(text("CITATION.cff"))
if str(cff.get("version")) != "12.6" or str(cff.get("date-released")) != "2026-08-15":
    fail("CITATION.cff version/date")
if "v12.6" not in str(cff.get("title", "")):
    fail("CITATION.cff title")

current_surfaces = [
    "NOTICE", "CITATION.cff", "START_HERE_RELEASE_INDEX_v12.6.md", "REVIEWER_QUICK_START.md",
    "docs/assurance/RELEASE_REALITY_REGISTER_v1.0.yaml",
    "docs/implementation/CANONICAL_AUDIT_FLAG_REGISTRY_v1.0.yaml",
    "docs/implementation/CANONICAL_STATE_REGISTRY_v1.0.yaml",
    "docs/implementation/NORMATIVE_KERNEL_INDEX_v1.0.yaml",
    "docs/implementation/STATE_TRANSITION_MATRIX_v1.0.json",
]
for rel in current_surfaces:
    value = text(rel)
    if re.search(r"MathGov(?: Core)?(?: Release 2026\.09)? v12\.5|MathGov_v12\.5|RippleLogic_v12\.5", value):
        fail(f"stale current identity in {rel}")

excluded_terms = ("Ely" + "ria", "S" + "OS")
for path in ROOT.rglob("*"):
    if path.is_dir() and path.name == "__pycache__":
        fail(f"bytecode directory {path.relative_to(ROOT)}")
    if path.is_file() and path.suffix.lower() in {".pyc", ".pyo"}:
        fail(f"compiled artifact {path.relative_to(ROOT)}")
    if path.is_file() and (path.name.startswith(".~lock.") or path.name.startswith("~$") or path.name in {".DS_Store", "Thumbs.db"} or path.suffix.lower() in {".tmp", ".bak", ".swp"}):
        fail(f"ephemeral office or editor artifact {path.relative_to(ROOT)}")
    if path.is_file() and path.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".cff", ""}:
        value = path.read_text(encoding="utf-8", errors="ignore")
        if any(re.search(rf"\b{re.escape(term)}\b", value, re.I) for term in excluded_terms):
            fail(f"excluded-lineage term in active source {path.relative_to(ROOT)}")

print("PASS current v12.6 / SGP v8.5 pins, run-record v4, WDBIP v1.6, exact Core 15, and independent-source hygiene")
