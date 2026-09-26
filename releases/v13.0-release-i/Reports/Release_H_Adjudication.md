# Release H: feedback adjudication and exact improvements

## Verdict and preserved scope

The feedback supports a small correction pass, not a new architecture. The separately uploaded 15 Core masters match the supplied ZIP. **Twelve masters, including Canon v13.0 and SGP v8.8, remain byte-identical.** Only Public Introduction v13.0, Cascade Standard v2.9 and Aligners v5.9 have new bytes. Existing component editions, numerical inputs/defaults, formulas, cached results, tables and section geometry remain unchanged.

## Accepted, qualified and rejected suggestions

| Feedback | Disposition and rationale |
| --- | --- |
| Active zero-valued cells influence uncertainty/Gap | Accept a clearer explanation and numerical regression tests. Do not automatically reduce sigma for a zero mean or alter the frozen Method C fixture. The evidence meaning and weight/dependence basis matter. |
| Epsilon changes the nominal comparison by about 2.4% | Verified at 2.3816%. Preserve the existing Canon disclosure; do not retune epsilon after observing the result. Even epsilon zero does not rescue the doubled-sigma comparison. Prospective alternatives are research, not this correction. |
| Five catastrophe floors imply .10 disjoint probability and necessarily swamp ordinary decisions | Reject the universal conclusion. Applicable categories may overlap, have context-specific exceptions, and sit within a declared exposure domain. Truly disjoint applicable floors do sum, but the actual loss distribution determines CVaR. |
| Make TRC loss reference explicit | Already controlled by Canon §8.4 / D.6: scenario-conditioned residual safe-corridor-relative Base-stream loss. Incremental continuation diagnostics do not replace it. Add a reading pointer, not a new loss definition. |
| Lead public reporting with profiles, not scalar | Accept a short Public Introduction clarification consistent with Canon §§10.0A–10.1A. A larger Gap is not statistical confidence or authority. |
| Add a parameter rationale annex | Accept an informative table of existing values, rationale, source and sensitivity, explicitly preserving absent empirical calibration. No invented justification or numerical optimum. |
| Merge state vocabularies | Accept a typed crosswalk; reject a universal interchangeable enum. Existing framework verdicts, formal decision/execution states, teaching labels, wrapper claims and capability states answer different questions. |
| Use one shared emergency record | Accept only an optional cover index linking existing evidence and pathway records. Do not weaken rights/tail/CSV/wrapper prerequisites or create a common emergency permit. |
| State ripple.md's current dependency boundary | Already stated near the beginning, before the abstract. Preserve the correct Core file; surface the conditional L0/L1 versus companion-dependent stronger-path boundary in the publication guide. |
| Referenced manifest/verification/calculator are absent | Partly a reviewer-access limitation. The full ZIP contains manifests, ledgers, scoped executable code and receipts. Exact external full interfaces, libraries and the prospective rater workbook are not supplied. The guide/inventory distinguishes presence from claimed completeness. |
| Stale workbook current-build date | Correct it to an authoritative release-appendix/manifest pointer; synchronize its typed snapshot. |
| Historical worksheet/section names are stale | Preserve their lineage/reference role. No renaming without a functional need. |
| Historical unverified v1.5 implementation pointer is in the public reading route | Relocate the complete pointer and caveat to the existing historical appendix in Public Introduction and Cascade. Keep v1.7 prominent. |
| Delete repeated release/history appendices | Do not perform a wholesale restructuring of already-correct masters in this freeze. Preserve standalone provenance and existing collapsed-history HTML reading behavior. |
| Begin empirical L1 validation | Accept as the next study stage, not a completed result. The design is specified; actual case/rater execution materials and data must be separately prepared and frozen. Local computation is not empirical validation. |

The source review's broad claims of superiority over other methods and lack of published results are not independently established by this correction pass. No such comparative or publication-status assertion is added. Hypothesis identifiers are kept document-specific: the RLS Validation Protocol's H3 is legibility and H5 is OptionClosureRecord improvement.

## Exact changed Core surfaces

**Public Introduction:** remove the historical v1.5 aside and duplicate compatibility caveat from the current v1.7 reading route; preserve both sentences in the historical appendix. Add one profile/uncertainty/decisiveness reading instruction. Update only necessary current-build/evidence pointers. A targeted page break keeps the “Public script” heading with its paragraph after the required reflow.

**Cascade Standard:** relocate the same historical pointer/caveat out of its “Reproducible run interface” paragraph and into history. Preserve all operative requirements. Update only necessary current-build/evidence pointers. No cascade, state, equation or table changes.

**Aligners workbook:** four principal literal strings and four typed snapshot counterparts:

| Current cell | Repair | Active counterpart |
| --- | --- | --- |
| Sanity_Checklist!G2 | Replace stale current date with Appendix_Release/manifest pointer | Build_Snapshot!CN666 |
| Config!B27 | Replace unsupported `python3 verify_release.py --recalc` with `python -B verify_all.py` | Build_Snapshot!CN1466 |
| Appendix_Release!B4 | Identify exact H build, retaining edition 5.9 | Build_Snapshot!CN10991 |
| Appendix_Release!B7 | Reference current H report and actual Workbook_Manifest.json | Build_Snapshot!CN10997 |

The obsolete command and missing Workbook_Verification.json reference were additional directly reproduced defects. Historical Build_Snapshot!B27 is deliberately untouched. All **20,212 formulas/caches, numerical inputs and 95-sheet structure** are preserved. All **336 existing DOCX tables**, including content and formatting, are unchanged.

Full before/after strings, source locations and rationale are in `Verification/Final_H/Exact_Document_Changes.json` and `Exact_Workbook_Changes.json`; independent preservation records sit alongside them.

## Publication and executable checks

`Publication/Feedback_Clarifications.md` gathers the accepted explanations without duplicating new mandatory architecture. Current root pages, dependency inventory and manifests identify H separately from inherited G source components and retained historical receipts.

Five inherited build-ID assertions are adapted to check each exact manifest-bound **component source ID**, not to require rewriting good G masters to display the later package date. Strict count, path, two-part version, size and hash checks remain. All previous semantic assertions and tolerances remain. New tests reproduce the feedback arithmetic and reject invalid inputs and malformed component identity. The change does not accept numerical drift.

## Identity and limits

**MathGov/RippleLogic v13.0 — MG-RL-13.0-20260926-RELEASE-H.** Same component editions; a distinct exact correction build, not replacement of a prior immutable archive. Source originals and raw review are retained privately. This is a research/teaching publication and scoped executable-test package, not empirical calibration, full production runtime, full external registry/schema conformance, domain authorization, new native H application certification or a Tier-4 ProofPack. Current verification is in `Release_H_Verification.md`.
