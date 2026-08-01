# MathGov v12.5 — Claude Feedback Disposition and Live-Recalculation Hardening Report

**Package:** `MathGov_Core_2026_09_v12_5_SGP_v8_4_FINAL_LIVE_RECALCULATION_AND_RELEASE_INTEGRITY_VERIFIED`  
**Date:** 25 July 2026  
**Version policy:** same-version release-integrity correction; MathGov v12.5, SGP v8.4, Aligners Sheet v5.5, and all companion versions preserved.

## Executive verdict

The external audit identified one genuine blocking defect class in the Aligners Sheet and one genuine Canon lineage error. Its principal release-identity and document-format blockers did **not** apply to the actual uploaded release because the audit was performed against a partial 59-file project bundle rather than the complete source package.

After applying the supported corrections, the framework substance remains affirmed. The final package is publication-ready within its declared Tier 1–3 public research/source specification scope, subject to the standing nonclaims concerning empirical validation, evidence truth, legal authority, physical safety, deployment readiness, and framework superiority.

## Accepted findings and corrections

### 1. Live workbook recalculation exposed malformed formula records

Static cached-value inspection was insufficient. Seven cells contained empty OOXML formula nodes that LibreOffice converted to `#ERR520!` / `#N/A` during live recalculation.

The repair was based on the actual v5.5 workbook semantics:

| Cell | Final treatment | Reason |
|---|---|---|
| `Containment!K14` | Restored live formula | Load-bearing UCI/HOI conformance status; preserves `PASS_ASSUMPTION_BOUND_TIER_2` and `UCI_NOT_MATERIAL_DECLARED`. |
| `Containment!K15` | Restored live formula | Load-bearing companion status with current v5.5 semantics. |
| `Containment!B19` | Restored `=K14` | Visible mirror of the controlling K14 result. |
| `Containment!E19` | Restored `=K15` | Visible mirror of the controlling K15 result. |
| `Sanity_Checklist!B34` | Converted to ordinary value | Current v5.5 label cell; restoring a v5.4 counting formula would overwrite current layout and semantics. |
| `Sanity_Checklist!B35` | Converted to ordinary value | Current v5.5 label cell, not the old v5.4 computed cell. |
| `Release_Notes!B21` | Converted to ordinary value | Current release-note content; not a formula surface in the present layout. |

`Sanity_Checklist!C30` was also restored from the frozen literal `0.0315` to the live reference `=CANON!B55`.

Final live LibreOffice recalculation: **zero errors**.

### 2. Duplicate synchronization surfaces

The workbook contained `v12_5_Sync` and `v12_5_Sync (2)`. They were consolidated into one authoritative `v12_5_Sync` sheet containing the complete current component inventory and authority statement.

### 3. Canon v12.4 lineage anachronism

The historical v12.4 entry incorrectly named SGP v8.4 and Aligners Sheet v5.5. It now correctly records **SGP v8.3** and **Aligners Sheet v5.4**. No current component pin changed.

### 4. Partial versus full package identity

The Canon's package-pins paragraph was clarified as a list of **core operating-document pins**, not the exhaustive file inventory. It now explicitly assigns full inventory authority to:

- `VERSION_MANIFEST.yaml`; and
- `release/release_manifest.yml`.

This removes competition between a concise human-readable list and the complete machine-readable release inventory.

### 5. Verification blind spot

The release gate now includes `VERIFY_WORKBOOK_LIVE_RECALCULATION.py`. It copies the workbook, forces headless LibreOffice recalculation, and rejects:

- formula errors;
- `ERR520` tokens;
- duplicate synchronization sheets;
- altered load-bearing Containment outputs; and
- loss of the live Canon cross-check.

Static formula verification separately rejects empty formula nodes and exact-formula drift.

## Rejected or already-resolved findings

| External finding | Disposition | Evidence in actual package |
|---|---|---|
| README still v12.4 / SGP v8.3 | Rejected as bundle-stale | Actual root README already identifies v12.5 / SGP v8.4. |
| No LICENSE | Rejected | Apache-2.0 `LICENSE` is present. |
| Only seven files hashed | Rejected for full package | Full active-file and Core 15 SHA-256 ledgers are present and verified. |
| No release manifest | Rejected | Both `VERSION_MANIFEST.yaml` and `release/release_manifest.yml` are present. |
| RLS Validation Workbook v0.3 absent | Rejected | Present at `docs/validation/rls/RLS_Validation_Workbook_v0_3.xlsx`. |
| DOCX files are plain text / rendering impossible | Rejected | Actual DOCX files are genuine ZIP/OOXML, with current PDF mirrors and completed render audits. |
| Superseded artifacts compete in the active directory | Rejected | Historical materials are separated under `archive/`; `core_15/` contains the exact current set. |
| Add duplicated full pin blocks to governing documents | Rejected | Manifest authority plus document-specific integration identity is less fork-prone than repeating a large pin list in every governing text. |
| Replace E33/E34 disclosed assertions with apparent computed passes | Rejected | The disclosed assertions remain more honest where the condition is not genuinely computed; no false automation was introduced. |
| Restore all seven cells directly from v5.4 | Partly rejected | Four formulas were restored, but three proposed formulas belonged to superseded cell roles and would have corrupted current v5.5 content. |
| Version bump to v5.5.1 is mandatory | Not adopted by user instruction | The same-version correction is explicitly patch-dated, package-name differentiated, hash-bound, and fully logged; no architecture or intended workbook behavior changed. |

## Document and table preservation verification

Only the Canon and Aligners Sheet required content changes. The other 14 Core artifacts were not rewritten. The Canon DOCX was re-rendered to a 260-page PDF; all 260 pages were reviewed through complete contact sheets, with full-resolution inspection of the changed package-inventory page, corrected lineage page, and Section 14.3 pages 94–99. The previously repaired five-column ownership registry and four-column audit-flag registry remain separate, readable, and correctly headed. The package-wide DOCX/PDF verifier continues to pass all 15 current document surfaces and all 286 native tables with no collapsed columns, vertical text, exact-height clipping, missing repeated headers, terminal-border defects, or blank/edge-breach pages.

## What remained affirmed

- Governing cascade: `RG -> RF/NCRC -> TRC -> CSV -> RLS`.
- No sixth gate or eighth Welfare Dimension.
- UCI/HOI remains inside CSV when material, with only restricted residual post-RLS use.
- Rights remain non-compensatory.
- TRC and CSV remain distinct.
- SGP protection remains separate from capability, participation, role eligibility, and authority.
- The SGP computational / functional / epistemic / phenomenal claim register remains a major strength.
- The Aligners Sheet remains a worked-run and training companion, not a validator.
- The framework's largest next scientific requirement is external empirical validation, not further unsupported conceptual expansion.

## Final workbook state

- 87 worksheets;
- 2,946 non-empty formulas;
- 2,350 serialized nonblank formula results;
- 596 independently audited intentional blank formula results;
- zero empty formula nodes;
- zero cached errors;
- zero errors after live LibreOffice recalculation;
- one authoritative `v12_5_Sync` surface;
- automatic, forced, full recalculation enabled;
- exact byte identity between `docs/aligners` and `core_15` copies.

## Claim boundary

This correction establishes stronger release, formula-interface, live-recalculation, identity, and inventory conformance. It does not establish empirical effectiveness, evidence truth, actual control performance, physical safety, legal authority, democratic legitimacy, consciousness detection, moral truth, deployment certification, ProofPack completion, or Tier 4 readiness.
