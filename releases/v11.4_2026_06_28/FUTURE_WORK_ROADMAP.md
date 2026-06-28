# Future Work Roadmap: Not Yet Ready for Current v11.4 Release

This roadmap lists high-value work that should not be folded into the v11.4 core as if already complete. These items are future validation, tooling, and companion-package tasks. Their absence is intentional and does not weaken the v11.4 Tier 1-3 source/framework release as long as no stronger claim is made.

## 1. mathgov-reference v0.1

**Placement:** separate repository or `reference/` package.

**Contents:** JSON/YAML schemas for PCC, Decision Note, RG, RF/NCRC, TRC, CSV, RLS, SGP interface records; invalid fixtures; valid fixtures; edge-case test vectors; reference calculator; CLI validator.

**Reason:** Needed before any ProofPack, Tier 4, machine-verifiable, or reference-calculator claim.

## 2. CSV / UCI / HOI Measurement Annex

**Placement:** `docs/validation/csv/`.

**Contents:** UCI/HOI indicator dictionary, domain examples, structural-viability rater rubric, diagnostic severity anchors, calibration plan, inter-rater protocol, and known limitations.

**Reason:** CSV is architecturally strong, but UCI/HOI remain provisional diagnostics until measurement evidence exists.

## 3. SGP Biological Evaluation Annex

**Placement:** `docs/validation/sgp/`.

**Contents:** species-appropriate evidence batteries, comparative-cognition source map, welfare/valence evidence rules, evaluator qualifications, uncertainty labels, and anti-underprotection safeguards.

**Reason:** SGP biological evaluation is guidance-stage and should not be treated as validated measurement.

## 4. SGP Artificial Entity Evaluation Annex

**Placement:** `docs/validation/sgp/`.

**Contents:** architecture evidence requirements, continuity evidence, anti-fluency tests, deception/gaming tests, valence-evidence standards, adversarial evaluation, and uncertainty routing.

**Reason:** Current AI/digital-entity classifications must remain evidence-bound and non-overclaiming until stronger evaluation protocols exist.

## 5. Aligners Sheet Test Vector Pack

**Placement:** `docs/validation/workbook/` or `docs/validation/aligners/`.

**Contents:** rights-fail case, TRC-fail case, CSV-fail case, CSV_PASS_WITH_CONTROLS case, underdetermined case, non-decisive RLS case, tie case, and expected outputs.

**Reason:** The Aligners Sheet is a worked-run exemplar, not a validator. Test vectors are needed before stronger tooling claims.

## 6. RLS Inter-Rater Reliability Study

**Placement:** `docs/validation/rls/` plus research outputs.

**Contents:** preregistration, rater training, anonymized cases, scoring variance, inter-rater agreement, dimensional separability analysis, and failure modes.

**Reason:** RLS cell scoring remains M1 until reliability and separability evidence is produced.

## 7. Public Worked Casebook

**Placement:** `docs/examples/casebook/`.

**Contents:** at least 3-5 low- to medium-stakes examples with PCC-Lite, RG record, RF/NCRC check, TRC check, CSV check, RLS table, and non-overclaiming note.

**Reason:** Multiple examples will improve learnability and reduce overreliance on a single workbook exemplar.

## 8. Pilot Protocol and External Review Packet

**Placement:** `docs/pilots/` and release support.

**Contents:** reviewer roles, recruitment, ethics protocol, data collection, shadow-mode use, inter-rater plan, issue capture, limitation reporting, and revision process.

**Reason:** Needed before policy-facing, deployment, or empirical validation claims.

## 9. Persuasion Integrity and AI Self-Validation Guardrail

**Placement:** `docs/guides/`.

**Contents:** no AI self-validation, no persuasion bombing, no false certainty, no role-flattery, no urgency inflation, provenance disclosure, adversarial review, and high-stakes release blocking.

**Reason:** The Agent System already includes safeguards, but a short dedicated guide would make them easier to teach and audit.

## Current-release boundary

None of the above items should be treated as shipped, validated, or required for the current v11.4 Tier 1-3 source/framework release unless bundled later with hashes, release notes, and explicit claim boundaries.
