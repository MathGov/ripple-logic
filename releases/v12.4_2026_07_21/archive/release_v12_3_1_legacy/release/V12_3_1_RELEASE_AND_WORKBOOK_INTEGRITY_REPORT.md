# MathGov v12.3.1 / SGP v8.2.1 Release and Workbook Integrity Report

**Date:** 19 July 2026  
**Change class:** bounded patch release  
**Architecture change:** none

## Purpose

This patch resolves reproducible release, pin, workbook, and public-surface defects identified during the 15-file core audit. It preserves the canonical cascade:

`RG -> RF/NCRC -> TRC -> CSV -> RLS`

It does not add a sixth gate, an eighth welfare dimension, a new RLS equation, a new SGP protection threshold, or a deployment-certification claim.

## Audit disposition

Two headline audit findings were rejected after direct inspection of the supplied ZIP:

- the active DOCX files were already genuine OOXML Word files;
- the Reproducibility and Use Standard v1.1 was present in `docs/implementation/`.

The following genuine defects were corrected:

- current-version split-brain across documents and workbook control surfaces;
- stale Canon, SGP, ripple.md, Agent, WDBIP, RLS-validation, Primer, and Public Introduction pins;
- duplicated and incorrect entries in the ripple.md companion matrix;
- workbook flag-integrity and sanity-summary defects;
- machine named-range off-by-one errors;
- workbook-local publication states that were labeled computed but were not formula-driven;
- typed CVaR worked-run outputs replaced by calculations from the displayed sorted scenario tables;
- incomplete five-level Dashboard status wiring;
- WDBIP title and package-registration clarity;
- SGP explicit no-P101 wording and exact running version;
- the exact 15-file review selection.

## Workbook integrity

Aligners Sheet v5.3.1 now contains:

- 83 visible worksheets;
- 2,716 formulas;
- no macros, external links, hidden sheets, or detected spreadsheet error tokens;
- a current `v12_3_1_Sync` control surface;
- formula-presence verification outside the workbook and portable token-integrity checking inside it;
- PASS, FAIL, ERROR, manual-review, and unclassified-state accounting;
- corrected `CANON_SCHEMA_FAIL_COUNT` and `CANON_PLACEHOLDER_COUNT` named ranges;
- formula-derived CVaR A and B values from displayed scenario tables;
- formula-linked RG, RF/NCRC, TRC, CSV, and RLS Dashboard results;
- a forced full recalculation request on workbook open;
- an Edit Integrity Map rather than a misleading claim that weak sheet passwords provide security.

The workbook remains a bounded Tier-2 worked-run exemplar and audit/training surface, not a validator or empirically validated reference calculator.

## WDBIP placement

WDBIP v1.3.1 remains inside the complete release and the selected 15-file review bundle because it supplies the boundary, interaction, dependence, subgroup, time-window, and migration discipline needed to construct RLS welfare inputs. It remains subordinate to the Canon and SGP and is neither a third principal governing source nor a gate.

## Claim boundary

This patch establishes release synchronization, structural integrity, formula/interface consistency, deterministic conformance testing, and procedural replay support. It does not establish evidence truth, empirical validity, legal authority, physical safety, consciousness detection, metaphysical proof, moral truth, framework superiority, or Tier-4 ProofPack readiness.
