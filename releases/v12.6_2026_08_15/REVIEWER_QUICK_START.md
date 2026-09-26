# Reviewer Quick Start

The active release is organized by typed artifact sets in `START_HERE_RELEASE_INDEX_v12.6.md`; the Canon and SGP are the two principal governing sources, with subordinate standards, operational companions, validation tools, guides, and lineage clearly separated.

> **Release index:** Start with `START_HERE_RELEASE_INDEX_v12.6.md` for the shortest source map, reader lanes, claims/non-claims, and release-boundary summary.
Use this file to audit the package quickly without losing the source hierarchy.

## 1. Check the active architecture

- Umbrella framework: MathGov
- Decision architecture inside MathGov: RippleLogic
- Public cascade: `RG -> RF -> TRC -> CSV -> RLS`
- Formal shorthand: `RG/RSG -> RF/NCRC -> TRC -> CSV -> RLS`
- Public teaching line: **Ground reality. Protect rights. Bound ruin. Preserve the structure. Score the ripples.**

Primary files:

- `README.md`
- `MATHGOV_ESSENTIALS.md`
- `docs/standards/RippleLogic_Cascade_Standard_v2.6.md`
- `docs/canon/RippleLogic_v12.6_Canon.md`

## 2. Check claim boundaries

Primary files:

- `CLAIMS_AND_NONCLAIMS.md`
- `RELEASE_CLAIMS_AND_NON_CLAIMS.md`
- `VALIDATION_STATUS.md`
- `MISSING_BY_DESIGN.md`

Safe release claim: Tier 1-3 framework/source release for review, worked-run learning, and pilot design.

Not claimable: ProofPack, Tier 4, empirical validation, legal certification, deployment certification, reference calculator, or automated moral truth.

## 3. Check the governing source hierarchy

Primary files:

- `SOURCE_HIERARCHY.md`
- `ARTIFACT_ROLE_MAP.md`
- `docs/CORE_COMPONENT_MAP.md`
- `docs/canon/CANONICAL_MAP.md`

## 4. Check calculability and workbook posture

Primary files:

- `docs/aligners/RippleLogic_Aligners_Sheet_v5.6.xlsx`
- `docs/workbooks/ALIGNERS_SHEET_USER_GUIDE.md`
- `docs/validation/rls/`

Reviewer warning: the Aligners Sheet is a worked-run and training companion. It is not a reference calculator and not a validation result.

## 5. Check agent safety and table readability

Primary files:

- `docs/agents/RippleLogic_Agent_System_v12.5.docx`
- `docs/agents/RippleLogic_Agent_System_v12.5.pdf`
- `docs/agents/RippleLogic_Agent_System_v12.5.md`

The DOCX/PDF reading copy has table readability improvements: repeated header rows, professional spacing, top-aligned cells, narrower margins, landscape orientation, and clearer column sizing.

## 6. Check validation roadmap

Primary files:

- `docs/validation/VALIDATION_INDEX.md`
- `docs/validation/rls/`
- `docs/validation/sgp/SGP_VALIDATION_PROTOCOL_v2_1.md`
- `docs/validation/trc/TRC_SCENARIO_DISCOVERY_PROTOCOL_v1_0.md`
- `docs/validation/csv/CSV_MEASUREMENT_MATURITY_NOTE_v1_0.md`
- `docs/validation/rights/RIGHTS_THRESHOLD_GOVERNANCE_NOTE_v1_0.md`

## 7. Check release integrity

Primary files:

- `release/SHA256SUMS.txt`
- `release/VERIFY_RELEASE.py`
- `release/VERIFY_SEMANTIC_SURFACES.py`
- `release/release_manifest.yml`

Run:

```bash
python release/VERIFY_RELEASE.py .
python release/VERIFY_SEMANTIC_SURFACES.py .
```
## 8. Check examples and reference replay

Primary files:

- `docs/examples/README.md`
- `docs/examples/reference_replays/ai_tutor_pilot/`
- `docs/examples/reference_replays/congestion_pricing_pilot/`
- `docs/examples/NEGATIVE_EXAMPLES_INDEX.md`
- `docs/validation/WORKED_RUN_REGISTRY.md`

Reference replay packets are informative. They demonstrate schema and semantic use, not empirical effectiveness or deployment assurance.

## 9. Check maturity and physical-execution boundaries

- `docs/assurance/SCIENTIFIC_MATURITY_LADDER.md`
- `docs/examples/PC_AEP_HIGH_STAKES_WORKED_EXAMPLE.md`
- `docs/guides/PHYSICAL_ADMISSIBILITY_AND_EXECUTION_BOUNDARY.md`
- `docs/validation/V12_6_SAFETY_CONFORMANCE_VECTORS.md`

