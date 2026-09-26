# MathGov v12.2 / SGP v8.1 Reproducibility and Format-Integrity Hardening Report

**Date:** 13 July 2026  
**Release posture:** Tier 1-3 public research/source specification and validation-preparation package  
**Component-version policy:** no existing component version changed; one new bounded implementation standard is introduced as v1.0.

## Problem addressed

The framework had a strong qualification-before-ranking architecture but imposed too much interpretive burden through a very large Canon, overlapping companion surfaces, numerous records and flags, and manually maintained examples. That created an assurance risk: a comprehensive system can still fail in practice if controlling rules are hard to identify, two implementers cannot replay the same run, missing parameters silently enter calculations, or examples drift from normative rules.

The formatting layer also required release-wide normalization. Tables and prose had accumulated style differences, including inconsistent font sizes in earlier SGP reading artifacts.

## Work plan executed

1. Freeze the five-stage architecture and source hierarchy. No sixth gate and no semantic rewrite.
2. Extract a compact twelve-rule implementation kernel with exact controlling-source pointers.
3. Define proportional Quick, Standard, and Audit profiles so ordinary decisions are not forced through institutional bureaucracy.
4. Define deterministic option states, selectable-set logic, explicit refusal/non-decisive states, and authority/execution separation.
5. Require decision-material parameters to be declared and locked before outcome-sensitive ranking; `UNKNOWN` cannot enter arithmetic as zero.
6. Publish a minimum machine-readable run record and a standard-library semantic validator.
7. Add passing and intentionally failing conformance vectors so contradictions are mechanically testable.
8. Add a two-implementer replay protocol and discrepancy taxonomy.
9. Add a workbook reproducibility sheet with live version and type-separation checks.
10. Normalize every active DOCX and table with one controlled typography and table-format system, regenerate all PDFs, and visually inspect every page.
11. Add automated format and reproducibility verification to the release workflow.
12. Preserve strict claim boundaries: conformance is not evidence truth, empirical validation, legal authority, physical safety, or moral truth.

## New reproducibility layer

### Normative implementation companion

`docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.1.md`

The standard defines K01-K12:

- identity and scope;
- parameter lock;
- Reality Grounding;
- Rights Floor/NCRC;
- Tail-Risk Constraint;
- Containment and Structural Viability;
- selectable-set formation;
- residual ranking only among survivors;
- explicit decision states;
- authority and execution separation;
- controls and monitoring;
- append-only audit and requalification.

It does not replace the Canon. The Canon remains the controlling semantic source.

### Machine-facing artifacts

- `docs/implementation/NORMATIVE_KERNEL_INDEX_v1.0.yaml`
- `schemas/mathgov_run_record_v2.schema.json`
- `release/VALIDATE_MATHGOV_RUN.py`
- `tests/run_records/`
- `docs/examples/reproducibility/reusable_cups_run_v2.json`
- `docs/examples/reproducibility/REPRODUCIBLE_RUN_WALKTHROUGH_v1.md`

The validator rejects, among other defects:

- ranking a non-selectable option;
- letting a failed gate be rescued by aggregate benefit;
- using an `UNKNOWN` parameter in arithmetic;
- claiming decisiveness when the declared test fails;
- selecting non-decisively without a bounded authority rationale;
- authorizing execution without authority evidence;
- failing to reopen a run after material distribution shift.

## Proportional burden

| Profile | Typical use | Minimum rigor |
|---|---|---|
| Quick / Tier 1 | personal, family, classroom, low-stakes reversible | short qualitative facts, gates, ripples, controls, and reopen record |
| Standard / Tier 2 | organization, community, programme, bounded policy | evidence, parameter lock, gate records, uncertainty, controls, and audit trace |
| Audit / Tier 3 | public, contested, high-impact, irreversible, or high-stakes | full schema, hashes, independent review, governed scenarios, subgroup analysis, and replay packet |

Escalation is triggered by material rights, ruin, vulnerable-group, physical-execution, consequential-agent, public-claim, or sensitivity conditions. A lower profile cannot be used to avoid a material safeguard.

## Ecosystem boundary

The package now states the ecosystem layers explicitly:

1. Core MathGov architecture and RippleLogic decision method.
2. SGP moral-status, protection, participation, power-readiness, intelligence, and RMCP/P100 companion.
3. Primer and public-introduction communication layer.
4. Independent applications such as AIAP and Auditable Flourishing.

AIAP and Auditable Flourishing are not retrospective proof of MathGov. Their validity must stand on their own literatures, methods, data, and results.

## Format integrity

All 14 active DOCX reading artifacts were normalized to a controlled role-based typography:

- Arial body text;
- 19 pt document title;
- 16 pt Heading 1;
- 13 pt Heading 2;
- 11.5 pt Heading 3;
- 10.5 pt body text;
- 9.5 pt compact text;
- 8.5 pt Courier New code;
- 8 pt Arial table text.

All active tables use a common blue header, white bold header text, alternating pale-blue/white rows, blue borders, top alignment, repeated semantic header rows, consistent padding, and non-splitting rows. SGP v8.1 now uses the same controlled table and typography system as the rest of the package.

The regenerated 14 PDFs contain 478 pages. All pages were visually reviewed through complete contact sheets, including all 241 Canon pages, all 65 Agent System pages, all 57 ripple.md pages, all 37 SGP pages, and every smaller companion page. No clipping, overlap, malformed table, unintended blank page, or uncontrolled font-size shift was observed.

## Automated assurance

`release/VERIFY_FORMAT_AND_REPRODUCIBILITY.py` checks:

- presence and parseability of the new reproducibility artifacts;
- passing and intentionally failing validator vectors;
- the controlled DOCX font and size set;
- 8 pt Arial table text;
- repeating table headers and non-splitting rows;
- absence of tracked changes and macros;
- workbook reproducibility surfaces and absence of external links/macros.

The GitHub workflow runs this verifier in addition to current-pin, semantic-surface, and full-release verification.

## Scientific and claim boundary

This hardening makes the framework easier to execute and audit. It does not establish that:

- evidence is true or complete;
- UCI/HOI, RLS, or RMCP/P100 instruments are empirically validated;
- legal thresholds or authority are correct;
- a physical or digital deployment is safe;
- one moral conclusion is objectively or automatically true;
- MathGov is superior to alternative frameworks.

Those remain empirical, legal, technical, participatory, and philosophical questions requiring independent evidence and review.
