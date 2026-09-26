# Reviewer and testing guide
Current build: `MG-RL-13.0-20260926-RELEASE-I`. Audit the actual files and distinguish a frozen worked example from a full operational runtime.

Start with `Reports/Release_I_Adjudication.md`, `Reports/Release_I_Verification.md`, `Verification/Final_I/Exact_Document_Changes.json` and `Verification/Final_I/Exact_Workbook_Changes.json`. Read the controlling Canon/SGP text rather than treating a report as replacement doctrine.

Default suite: `python -B verify_all.py --output-dir ../mathgov-tests`.
Native calculation/save/cold reopen: `python -B Native_Verification/verify_native_roundtrip.py --output-dir ../mathgov-native`.
Exact workbook: `python -B Reference/Workbook_Verifier.py Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx`.
Cache-independent replay: `python -B Reference/full_formula_replay.py --output-dir ../mathgov-formulas`.

The new `test_final_patch_checks.py` exercises recovery and compatible joint-stress predicates. These are scoped synthetic tests, not a deployed controller or complete risk model. `check_release_g.py` independently checks actual patched text, full-precision Appendix P/R.19 arithmetic, unchanged numerical workbook fingerprint and snapshot mutations. Prior G native receipts test G application execution. No native I calculation/save/reopen was performed. The earlier H sensitivity and source-identity tests remain, with I adding print-scope, guard-boundary, local-token, wrapper-metric and document-content regressions.

No token occurrence count proves executable coverage; no signature proves evidence truth; no prior freeze receipt establishes a changed file. A changed fixture premise must be disclosed and requalified rather than silently chosen for a passing result. Preserve originals while testing disposable copies.
