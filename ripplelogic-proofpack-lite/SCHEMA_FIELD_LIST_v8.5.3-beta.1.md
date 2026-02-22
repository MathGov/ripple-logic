# SCHEMA_FIELD_LIST_v8.5.3_beta.1.md

## Schemas included
- `schemas/decision_input.schema.json`
- `schemas/decision_output.schema.json`
- `schemas/weights.schema.json`
- `schemas/rights_coverage.schema.json`
- `schemas/uci_structural_input.schema.json`
- `schemas/audit_flags.schema.json`

## Notes
These are **ProofPack-Lite beta schemas**.
They are intentionally stricter on required top-level conformance fields and intentionally permissive on many diagnostic / extension fields.

## Design rationale
- Stabilize interoperability and conformance checking early
- Prevent accidental omission of key fields
- Avoid blocking progress on richer later schemas while canonical semantics settle
