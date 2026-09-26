# Aligners Sheet User Guide

The Aligners Sheet is a worked-run and training companion for RippleLogic. It is not a validator, not a ProofPack, not a reference calculator, and not empirical validation.

## Current workbook status

- Workbook: `docs/aligners/RippleLogic_Aligners_Sheet_v5.5.xlsx`
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

## Calculation behavior and viewer boundary

The released workbook preserves its original formulas and is configured for automatic full recalculation when opened in a spreadsheet engine that supports OOXML calculation. Formula caches are not treated as an authoritative source surface. GitHub previewers and data-only readers may therefore show blanks or stale values until a compatible engine recalculates the workbook.

For review or replay:

1. open the workbook in a current formula-capable spreadsheet engine;
2. allow full recalculation;
3. save a local review copy if cached display values are needed;
4. treat the Markdown Canon and declared workbook formulas, not a previewer cache, as the governing sources;
5. report engine/version and any formula differences in the run record.

The workbook remains a worked-run exemplar, not a reference calculator or repository-level validator.


## Material obligation integrity

When `CSV_PASS_WITH_CONTROLS` depends on a control, complete the `Responsibility_Continuity` material-obligation table. Record the accountable authority, operational carrier or execution path, authority/capacity basis, trigger, scope, required action, response window, evidence, review/expiry, challenge route, accepted delegation, backup, nonperformance escalation, amendment/waiver authority, change-control rule, residual responsibility, obligation status, and effectiveness status. A named owner or completed checklist alone does not establish control effectiveness.

## Hidden human compensation

Use `Human_Compensation_Load` before automation, scaling, outsourcing, or role removal when current performance may depend on undocumented overrides, exception handling, reconciliation, memory, relationships, recovery work, weak-signal detection, or informal escalation. `NOT_MATERIAL` requires a bounded rationale and reopen trigger. Material hidden dependence routes to support, documentation, redistribution, binding controls, redesign, or escalation inside CSV; it is not a sixth gate.
