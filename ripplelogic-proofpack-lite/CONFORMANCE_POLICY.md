# CONFORMANCE_POLICY.md

## Profile
**LITE_BETA_STRICT**

This beta profile defines the minimum comparison rules for the ProofPack-Lite conformance set.

## Required comparison behavior
Implementations under test MUST match the expected output exactly for the following fields:
- `schema_id`
- `vector_id`
- `admissibility_status`
- `decision_classification`
- `primary_decision_path` (ordered equality)
- `required_flags` (ordered equality for this beta set)
- `uci_status`

Implementations under test MUST also match the following `conformance_payload` fields exactly:
- `proofpack_version`
- `comparison_profile`
- `numeric_mode`
- `rounding_policy`

## Permitted variation in this beta pack
The following fields MAY vary unless a downstream test profile says otherwise:
- most `diagnostic_metrics`
- free-text explanations
- additional diagnostic metadata
- internal trace payloads

## UCI behavior in this beta set
The 5-vector beta set intentionally allows UCI to be `DECLARED_UNAVAILABLE` in non-UCI vectors.
This tests explicit handling of unavailable structural coherence inputs without silent omission.

## Goal
The purpose of this pack is to stabilize **behavioral conformance semantics** before expanding to richer numeric parity and full deterministic runtime verification.
