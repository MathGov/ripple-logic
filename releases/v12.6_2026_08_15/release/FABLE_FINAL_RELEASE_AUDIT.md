# Final External Release Audit - Claude Fable 5

**Target build:** `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3`

## Preferred access route

Audit the complete repository or complete unzipped package, not only the Core 15 reading mirrors. Select every tracked file and folder required for the release, including `docs/`, `schemas/`, `tests/`, `release/`, `core_15/`, `.github/`, and all root governance and metadata files.

## Reviewer instruction

Act as an independent release gate. Inspect actual file contents and bytes. Run available validators and verification scripts. Do not assume a claim is true because a filename, README, or prior report says it is true.

Return only:

1. S0 critical blockers;
2. S1 release blockers;
3. S2 material improvements;
4. exact file and location;
5. reproducible evidence;
6. proposed correction and downstream synchronization;
7. final `PASS`, `PASS WITH CORRECTIONS`, or `FAIL`.

Do not propose new gates, welfare dimensions, rights expansions, terminology, diagrams, standards, or examples unless a concrete unresolved failure cannot be handled by an existing artifact. Do not treat stylistic preference as a defect. The burden of proof is on every proposed change.

## Required checks

- exact release identity and semantic-version preservation;
- Canon/SGP source hierarchy and cascade consistency;
- schema and validator behavior;
- positive and expected-failure vectors;
- all three active reference replay packets;
- Core 15 OOXML magic and exact mirror hashes;
- PDF/DOCX readability and current QA reports;
- manifest and SHA-256 inventory;
- clean-extraction replay of `python release/VERIFY_RELEASE.py`;
- absence of stale pins, placeholders, broken links, or unsupported completion claims.

## Claim boundary

A release PASS establishes artifact and tested-interface conformance only. It does not prove evidence truth, empirical effectiveness, legal authority, physical safety, moral truth, framework superiority, or deployment readiness.
