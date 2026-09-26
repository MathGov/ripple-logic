# Release H verification and readiness

**MathGov/RippleLogic v13.0 — MG-RL-13.0-20260926-RELEASE-H.** All component editions are unchanged. The manifest identifies twelve byte-preserved G masters and three narrowly corrected H masters.

## Verification scope

Checks cover the supplied artifact identities, complete document-body projections, existing equations and synthetic semantic fixtures, the frozen workbook's calculation corpus, reference/navigation integrity and static dashboard behavior. They do not certify every possible implementation or real-world evidence.

The 15 separately uploaded Core files match the supplied ZIP. The source archive passes ZIP CRC. Only the two recorded DOCX files and workbook have new Core bytes. All 336 existing document tables and section geometry remain unchanged. All 20,212 workbook formula texts and cached results, numerical inputs, styles, sheet order and geometry are preserved. Eight literal-string cells changed.

## Current execution record

The current machine execution receipt is `Verification/Final_H/Local_Suite_Receipt.json`. Final fresh-extraction checks are additionally recorded in the delivery receipt outside the immutable public ZIP. Those receipts identify the actual executed commands, result totals and whether the package remained unchanged. Results are scoped tests, not empirical validation.


### Executed pre-freeze results

All **18 substantive commands passed**, and the runner confirmed that package files were unchanged during execution. The final frozen archive is independently extracted and the full 19-command suite, including the final hash ledger, is executed again; that result is recorded in the external delivery receipt.

| Check | Executed result |
| --- | --- |
| Unit tests | 301 passed, including 28 new sensitivity/identity tests |
| Workbook formula replay | 20,212 formula cells; zero cached-formula dependencies; zero mismatches |
| Independent workbook arithmetic | 900 / 900 |
| Workbook publication / mutation / stored-formula checks | 55 / 55; 12 / 12; 10 / 10 |
| Retained correction suites | 80 / 80; 77 / 77; 74 / 74; 290 / 290; 857 / 857; 91 / 91 |
| New targeted H artifact assertions | 60 / 60 |
| Static numbered TOC references | 125 / 125 |
| Document-body / reading-link integrity | 798 / 798 in this pre-freeze suite |
| Dashboard tests | 15 / 15 |

Both amended DOCX masters were rendered and all 19 pages visually inspected. No clipping, overlapping content or broken table layout was observed. Twelve unchanged masters and their mirrors were preserved byte-for-byte, rather than claimed to have received a new full visual proofread. All 14 complete body projections and the 125 numbered references are checked by the supplied tools. These counts describe the executed tests, not exhaustive scientific correctness.

## Native application and tool boundary

**No new H native spreadsheet recalculation/save/reopen was executed.** G's LibreOffice Calc receipt is retained under Final_G for G's exact bytes, not relabeled as native H acceptance. Literal-only OOXML changes preserve the original workbook; no full XLSX export, formula rewrite or spreadsheet conversion was used. Fresh cache-independent formula replay and exact formula/cache preservation are separate evidence from native application parity. Microsoft Excel and arbitrary spreadsheet-engine compatibility are not claimed.

The working session was interrupted during preparation. The deliverable was rebuilt from the exact original ZIP, not from an assumed surviving temporary directory; the final receipts apply to the recovered deliverable. No lost/interrupted test is counted as a completed new test.

## Remaining evidence boundaries

No independent human rater study, empirical welfare calibration, completed L1 case/rater study packet, full production runtime, complete external canonical registry/schema conformance, active RPAP/PFAP bundle, legal authority, physical-safety certification, deployment authorization or Tier-4 ProofPack is established. The dependency inventory and each controlling component specify these boundaries.

No GitHub upload, hosted workflow, site promotion or hosted hash-back verification was performed. Those need a separate actual publication receipt. A trusted archive/ledger hash must be retained independently; a ledger and payload obtained from the same untrusted source are not independent evidence of authenticity.

## Reproduce

From the publication root, install the pinned `Reference/requirements.txt` dependencies and provide Node for the dashboard test. Run:

```bash
python -B verify_all.py --output-dir ../mathgov-test-results
```

Logs must stay outside the immutable package. Any later material edit creates a new exact build, requires affected checks and regenerates the hash ledger. Readiness here means readiness for the declared research/teaching publication, outside expert review and supplied scoped tests, not completion of the stronger unperformed claims above.
