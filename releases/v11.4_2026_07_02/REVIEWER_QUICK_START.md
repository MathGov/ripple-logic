# Reviewer Quick Start

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
- `docs/standards/RippleLogic_Cascade_Standard_v1.0.md`
- `docs/canon/RippleLogic_v11.4_Canon.md`

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

- `docs/aligners/RippleLogic_Aligners_Sheet_v4.4.xlsx`
- `docs/workbooks/ALIGNERS_SHEET_USER_GUIDE.md`
- `docs/validation/rls/`

Reviewer warning: the Aligners Sheet is a worked-run and training companion. It is not a reference calculator and not a validation result.

## 5. Check agent safety and table readability

Primary files:

- `docs/agents/RippleLogic_Agent_System_v11.4.docx`
- `docs/agents/RippleLogic_Agent_System_v11.4.pdf`
- `docs/agents/RippleLogic_Agent_System_v11.4.md`

The DOCX/PDF reading copy has table readability improvements: repeated header rows, professional spacing, top-aligned cells, narrower margins, landscape orientation, and clearer column sizing.

## 6. Check validation roadmap

Primary files:

- `docs/validation/VALIDATION_INDEX.md`
- `docs/validation/rls/`
- `docs/validation/sgp/SGP_VALIDATION_PROTOCOL_v1_0.md`
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
