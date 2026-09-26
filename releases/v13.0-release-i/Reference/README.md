# Scoped reference implementation and tests

Run the public package root `verify_all.py` for the complete supplied suite. See Publication/Reviewer_And_Testing_Guide.md and Reports/Verification_and_Readiness.md.

The existing core_reference, recovery_checks and publication_checks modules provide finite arithmetic and record demonstrations. decision_fixture adds synthetic verdict-serialization regressions. validate_records applies the two supplemental schemas, not the absent legacy run schema. Workbook_Verifier checks frozen XML/formula/cache identity against a separately trusted manifest. workbook_probe interprets the changed stored-formula paths with explicitly listed retained dependencies.

No module is an actuator, universal moral calculator, evidence oracle, full external-registry validator or production authorization service. Test fixture names and local diagnostic strings are not new Canon machine tokens. The state_crosswalk is a scoped reading aid sourced from the governing prose.

The manifest creation option is a build operation, not independent verification. Do not regenerate a manifest to hide an unexplained mismatch.

export_reading.py regenerates Sources and Reading_HTML; it is a build operation that changes reading bytes and requires a new manifest/ledger freeze. It does not modify Word masters or render PDFs. Exact PDF rendering was performed with the documented external Word rendering tool; the runtime needed for that build step is not bundled.

Release E adds dependence_sensitivity.py (bounded pairwise sensitivity only), minimum_records.py and schemas/pcc_minimum_records.schema.json (supplemental content serialization), and derived record/token indexes. These do not establish the complete external canonical state/audit registry or v4.1 run schema. See their local boundaries and positive/negative fixtures.


Historical Release F evidence note: its separate artifact_tool export failed parity and was rejected. That experiment is retained as history. The source G workbook has its own native Calc receipt. H has no new native application receipt; its literal corrections and unchanged formula/cache corpus are checked independently. Microsoft Excel parity, empirical validation and complete external interface conformance remain unclaimed. See Reports/Release_H_Verification.md.

## Full stored-formula replay

`full_formula_replay.py` shares only the safe parser and OOXML inventory reader with older tools. Its evaluation path recursively computes all formula dependencies from literals, not caches; unsupported syntax raises an error rather than taking a stored value. It supports the exact function corpus and tested forms used by this frozen workbook, not arbitrary Excel features. `test_full_formula_replay.py` supplies independent expected values for blank handling, exact lookup, formula identity/presence, error routing, arithmetic and rounding. Outputs are a saved/reopened JSON ledger; no master is edited.

## Final micro-patch tests
`final_patch_checks.py` and its tests implement only synthetic recovery and joint-stress predicates. `check_release_g.py` checks the actual amended artifacts and independent example arithmetic. Existing semantic tests remain; historical byte-identity assertions in Release E/F checks now compare the current manifest and the unchanged full formula/cache fingerprint, because approved literal labels changed. This is not permission to regenerate a manifest after an unexplained numerical mismatch.

Native Calc tests are a separate command in `Native_Verification/`; they operate on disposable copies and leave Core masters untouched. A successful local test suite is not hosted CI or deployment authorization.
