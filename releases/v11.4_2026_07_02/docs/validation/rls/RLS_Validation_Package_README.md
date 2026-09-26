# RLS Validation Package v1.0

Companion validation package for MathGov Core Release 2026.09 v11.4 and the RippleLogic v11.4 Canon.

## Contents

- `RippleLogic_RLS_Validation_Protocol_v1_0.docx` - polished protocol document for the RLS validation sprint and calibration study.
- `RippleLogic_RLS_Validation_Protocol_v1_0.md` - editable Markdown source for the protocol.
- `RLS_Validation_Workbook_v0_1.xlsx` - rater-entry and analysis-prep workbook with the 49-cell dictionary, 10 synthetic cases, and 1,470 scoring rows per rater.
- `RLS_Calibration_Note_v1_0_TEMPLATE.md` - template for reporting the first validation sprint results after raters complete the workbook.

## Status

This is a companion validation package. It is not governing core, not empirical validation by itself, not legal certification, and not deployment authorization.

## Use

1. Give each rater a copy of `RLS_Validation_Workbook_v0_1.xlsx`.
2. Ask them to fill the `Rater_Entry_Template` sheet independently.
3. Append all completed rater rows into one CSV or workbook.
4. Run inter-rater reliability, cell-correlation, redundancy, factor/PCA, and decision-value analyses.
5. Record findings in the calibration note template.
6. Update the RLS scoring manual, Canon companion materials, or workbook based on the revision rules in the protocol.

## Core boundary

MathGov is the umbrella framework. RippleLogic is the decision architecture inside MathGov. The public cascade is RG -> RF -> TRC -> CSV -> RLS. RLS ranks only selectable options and cannot rescue an RF/NCRC, TRC, or CSV failure.
