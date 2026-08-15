#!/usr/bin/env python3
"""Check the synchronized semantic surfaces introduced or preserved in v12.6."""
from pathlib import Path
import json, sys

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]

def require(rel: str, phrases: list[str]) -> None:
    value = (ROOT / rel).read_text(encoding="utf-8", errors="replace").lower()
    for phrase in phrases:
        if phrase.lower() not in value:
            raise SystemExit(f"FAIL semantic surface: {rel} missing {phrase}")

require("docs/canon/RippleLogic_v12.6_Canon.md", [
    "RG -> RF/NCRC -> TRC -> CSV -> RLS", "No sixth gate", "seven Welfare Dimensions",
    "Qualification Continuity for Consequence-Bearing Action", "Outcome Observation and Requalification",
    "action_instance_id", "action_specification_hash", "qualification_snapshot_hash",
    "rights non-compensation", "refusal",
])
require("docs/agents/RippleLogic_Agent_System_v12.5.md", [
    "Qualification Continuity", "ACTION_INSTANCE_ID", "ACTION_SPECIFICATION_HASH",
    "QUALIFICATION_SNAPSHOT_HASH", "capability", "authority", "requalification",
])
require("docs/standards/ripple_md_Standard_v5.5.md", [
    "action-bound qualification", "outcome observation", "requalification", "not a sixth gate",
])
require("docs/primer/RippleLogic_Foundations_Primer_v4.4.md", [
    "Qualification Continuity", "observed outcomes", "requalification", "five-stage",
])
require("docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.md", [
    "seven welfare dimensions", "not an eighth dimension", "WDBIP v1.6", "RippleLogic v12.6",
])

schema = json.loads((ROOT / "schemas/mathgov_run_record_v4.schema.json").read_text())
props = schema["properties"]["configuration_assurance"]["properties"]
for field in ("qualified_option_id", "action_instance_id", "action_specification_hash", "qualification_snapshot_hash"):
    if field not in props:
        raise SystemExit(f"FAIL semantic surface: schema missing {field}")
print("PASS five-stage architecture, non-dilution, action-bound qualification continuity, and outcome requalification surfaces")
