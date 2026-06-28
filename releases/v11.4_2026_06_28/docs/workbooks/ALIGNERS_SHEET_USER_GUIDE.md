# Aligners Sheet User Guide

The Aligners Sheet is a worked-run and training companion for RippleLogic. It is not a validator, not a ProofPack, not a reference calculator, and not empirical validation.

## Current workbook status

- Workbook: `docs/aligners/RippleLogic_Aligners_Sheet_v4.4.xlsx`
- Formula-error scan in this release polish found no visible `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or `#N/A` cells in the imported workbook surface.
- This is a sanity check, not a full formula audit.

## Safe use

1. Make a copy before editing.
2. Start with `How_To_Use`, `CANON`, and `User_Guide`.
3. Fill inputs before interpreting dashboards.
4. Treat `COMPUTABLE_BUT_INADMISSIBLE`, `IND`, `REFUSE`, and `ESCALATE` states as governance signals, not spreadsheet errors.
5. Do not use an RLS result to override failed RG, RF/NCRC, TRC, or CSV.
6. Export a completed workbook only with a corresponding narrative Decision Note or PCC record.

## Minimum decision-run sequence

1. `Reality_Grounding`
2. `Category_Grounding` and `Term_Discrimination` when material
3. `Rights_Floor` / `NCRC`
4. `TRC`
5. `Containment`, `Structural_Viability`, and `CSV`
6. `RLS`
7. `Dashboard`
8. `Audit_Flags`
9. `PCC`

## Required future workbook work

Before stronger public claims, the workbook needs:

- independent formula audit;
- canonical test vectors;
- edge-case examples for unknown cells, non-decisive RLS, PLSS escalation, CSV emergency-provisional handling, and rights-floor failure;
- automated validator or reference-calculator comparison;
- at least three completed sample workbooks using real-world-style decisions.
