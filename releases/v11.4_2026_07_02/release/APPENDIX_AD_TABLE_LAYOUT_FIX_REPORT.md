# Appendix AD Table Layout Fix Report

This patch restores the Appendix AD Canon table layout using the prior verified Canon layout as the reference.

Scope of change:
- Restored Appendix AD to the seven union-scope tabular dictionary format.
- Preserved the table content and canonical material.
- Used landscape/wide-page layout for the Appendix AD tables so the 49-cell welfare dictionary remains readable.
- Regenerated the Canon DOCX, Canon PDF, and Canon Markdown source.
- No governing framework wording, equations, cascade semantics, thresholds, rights coverage, TRC logic, CSV logic, SGP interface, or RLS semantics were intentionally changed.

Verification:
- Canon DOCX rendered to PDF.
- Appendix AD pages were visually checked after rendering.
- Release verification scripts passed.
- ZIP integrity passed.
