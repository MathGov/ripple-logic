# v12.0 Final Appendix AD Hybrid Finalization Report

## Summary

Appendix AD was finalized by preserving the latest human-readable split-table Canon layout and adding a one-row-per-cell CSV companion for tooling and audit use. This implements the selected best-of-both structure: the Canon remains readable for humans, while the older wide-record logic is preserved for implementation surfaces.

## Changes

- Kept the latest split Appendix AD as the governing human-readable Canon presentation.
- Added `docs/canon/AD_49_Cell_Welfare_Dictionary.csv` with 49 rows and separate fields for scope, dimension, cell ID, label, meaning, benefit movement, harm movement, evidence, gate cues, example, and reviewer check.
- Added a short Appendix AD companion note to Canon Markdown and DOCX.
- Added the CSV companion to reader maps and release support metadata.
- Regenerated the Canon PDF from the patched DOCX.

## No changes

No equations, cascade order, gates, SGP scoring, thresholds, workbook formulas, claim boundaries, or table styling logic were changed.

## Release boundary

The CSV is informative and machine-readable. The Canon text controls if any companion representation diverges.
