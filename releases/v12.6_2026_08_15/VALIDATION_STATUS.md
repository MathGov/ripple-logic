# Validation Status - MathGov Core v12.6

**Exact release:** `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3`  
**Artifact-integrity status:** PASS  
**Construct validity:** UNTESTED  
**Deployment authorization:** NOT PROVIDED

- Core run-record conformance: 6 positive fixtures accepted; 30 expected-failure fixtures rejected; 3 active reference replay examples accepted.
- Sensitivity/decisiveness contradiction: new adversarial fixture rejected; current worked run is non-decisive and uses a separate authority selection.
- SGP RMCP conformance: 1 positive accepted; 1 expected failure rejected.
- WDBIP v1.6 conformance: 1 positive accepted; 17 expected failures rejected.
- Aligners Sheet v5.6: 87 worksheets, 1,643 formulas, zero formula-error cells after isolated live recalculation, and exact Core 15 mirror.
- Reading surfaces: 15 current Markdown/DOCX/PDF triples, 287 tables, 2,439 table rows, 1,634 headings, and 598 PDF pages.
- Navigation: 125 complete linked TOC entries across Canon, SGP, and WDBIP; Canon's 70 entries match the final 275-page PDF.
- Document integrity: zero comments, tracked changes, content controls, confirmed page-boundary failures, tiny-font spans, drawings, charts, or embedded PDF image blocks.
- Accessibility: zero high- or medium-severity findings; 76 low findings are raw URL display text in reference lists.
- PDF preflight: 16 current PDFs totaling 613 pages, with zero openability, encryption, scan, XFA, or font-embedding warnings.
- Active release inventory: 286 files in the current manifest and SHA-256 ledger, plus the separate exact 15-file Core ledger.
- Release integrity: exact inventories, current companion pins, source hygiene, table styles, live workbook recalculation, and SHA-256 ledgers are verified by `release/VERIFY_RELEASE.py`.

These results establish conformance of the supplied artifacts and tested rules only. RLS, SGP, WDBIP, MHIOS, and the framework as a whole remain research specifications requiring independent empirical study.
