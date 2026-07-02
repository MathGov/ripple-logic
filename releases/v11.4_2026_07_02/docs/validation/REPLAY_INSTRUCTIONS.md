# Replay Instructions - Validation Scaffolding

This file prepares future independent replay. It is not a ProofPack and does not certify the current package as empirically validated.

## Minimal replay path

1. Record the package hash from `release/SHA256SUMS.txt`.
2. Open the applicable worked-run artifact, such as the Aligners Sheet.
3. Recalculate formulas in Excel or LibreOffice.
4. Record RF/NCRC, TRC, CSV, RLS, Gap, FrameworkVerdict, authority-selected option, invalid/escalate/review flag counts, and sanity-pass count.
5. Compare outputs against the released report or workbook dashboard.
6. Record all divergences in `docs/validation/RESULTS_CATALOG_TEMPLATE.csv` or a future results catalog.

## Boundary

Replay instructions prepare validation. They do not constitute independent replay results until an external reviewer performs and records the replay.
