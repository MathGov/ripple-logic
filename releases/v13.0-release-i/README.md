# MathGov / RippleLogic v13.0
## Final Tier 1–3 Research and Teaching Specification

Exact build: **`MG-RL-13.0-20260926-RELEASE-I`**. All component editions are unchanged.

**[Reading home](index.html)** · [Freeze record](FINAL_FREEZE.md) · [Changes](Reports/Release_I_Adjudication.md) · [Verification](Reports/Release_I_Verification.md) · [Manifest](VERSION_MANIFEST.json) · [Checksums](SHA256SUMS.txt)

The method remains **RG → RF/NCRC → TRC → CSV → RLS**: qualify first, then rank only survivors. This is the complete current Core 15 reading and scoped reference-testing package, not an empirically validated moral oracle or production runtime.

## What this correction contains
Eight reproduced errata are addressed in three Word masters and the workbook: print-area ownership, a local-guard claim, a raw-difference label, local flag classification, the wrapper's inter-rater metric relationship, the Primer's selection and validation wording, and a malformed WDBIP example table. All 336 inherited document tables are preserved; one genuine four-column table replaces the malformed paragraph. The workbook's numerical inputs, all 20,212 formulas and cached formula results, sheet order, styles and geometry are unchanged.

**Eleven Core files, including Canon and SGP, are unchanged byte-for-byte from H.** Their G/H source-build identifiers remain intact. Four corrected masters carry I. This is intentional source preservation; the manifest identifies each exact hash and edition. No gate, score equation, uncertainty parameter or worked verdict was changed.

## Read
Start with the Public Introduction and Foundations Primer. Use the Canon for controlling semantics and the named companions for their own requirements. `Core_15/` contains fourteen DOCX files and the Aligners XLSX. `Reading_PDFs/`, `Reading_HTML/` and `Sources/` contain complete synchronized reading projections. Static numbered TOCs are checked against the packaged PDFs; other Word environments may repaginate an editable DOCX.

## Test
```bash
python -m pip install -r Reference/requirements.txt
python -B verify_all.py --output-dir ../mathgov-test-results
python -B Reference/Workbook_Verifier.py Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx
```
Write test outputs outside the immutable tree. The local workbook guard checks a deliberately limited surface. Replacing a verdict display or changing a formula without changing its result can evade local checks; the external exact-file verifier is required. Verification is meaningful only against a trusted manifest, not a manifest edited by the same actor.

Cache-independent replay is current numerical evidence, not native-application certification. No new native Calc or Excel recalculation was executed for I. The reviewer's reported Calc test belongs to the H input hash, and retained older native receipts keep their original scope. The optional `Native_Verification/verify_native_roundtrip.py` command requires LibreOffice and Python with UNO; its presence is not evidence of execution on I.

## Publish
Publish this directory at repository or static-site root, preserving paths. Use the distinct exact build/tag rather than overwrite an earlier immutable release. Expose `FINAL_FREEZE.md`, the component manifest and the hash ledger. Run hosted CI, download the hosted files, compare them against a trusted local ledger, and record the actual URL, tag, commit and results in a separate publication receipt. No upload or hosted workflow was performed here.

The separate Complete archive retains the untouched H ZIP and the reviewer input under `Private_Provenance/`. Do not publish that folder by default.

## Claim boundary
Complete for this declared Tier 1–3 specification, frozen worked example, public reading and supplied scoped tests. Not empirical construct validity, universal welfare measurement, legal authority, physical-safety certification, a full operational selector/runtime, complete canonical registry or WDBIP machine conformance, every ripple.md L2/L3 pathway, Microsoft Excel compatibility, Tier-4 ProofPack or domain execution authorization. The wrapper clarification does not supply the absent RPAP/PFAP protocols or demonstrate any actual L2/L3 audit.

Retain `LICENSE`, `NOTICE` and all component and third-party rights statements. See [dependency limits](Publication/Dependency_Status.json), [workbook guide](Publication/Workbook_Reading_Guide.md) and [earlier accepted-feedback explanations](Publication/Feedback_Clarifications.html).
