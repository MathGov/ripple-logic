# MathGov Core Component Map v11.4

**Status:** Navigation and maturity dashboard. Informative unless explicitly incorporated by the release package.

**Purpose:** Show the role, authority, documentation completeness, and measurement maturity of each MathGov and RippleLogic artifact.

## 1. Two-axis honesty rule

This map reports two different maturity surfaces.

**Documentation / source completeness** asks:

- Is the artifact's scope defined?
- Are its inputs and outputs clear?
- Is its authority boundary clear?
- Are non-claims clear?
- Is it aligned with the Canon and source hierarchy?
- Is it usable as a Tier 1-3 source specification?

**Measurement maturity** asks:

- Does the artifact rely on measured quantities?
- Are those measurement instruments defined?
- Are they validated?
- Are they independently replayable?
- Is there reliability evidence?

A document can have high documentation completeness and low measurement maturity. That means the artifact is well-specified but not yet empirically instrumented.

Neither score is:

- empirical validation;
- ProofPack readiness;
- Tier 4 readiness;
- legal certification;
- deployment certification;
- reference-calculator status;
- evidence of superior decisions.

## 2. Measurement maturity scale

| Level | Name | Meaning |
|---|---|---|
| N/A | Not applicable | Conceptual, structural, or navigational artifact; no measurement instrument required |
| M0 | Undefined instrument | Measurement need identified, instrument not yet defined |
| M1 | Provisional heuristic | Guidance-stage or training-stage method; no reliability evidence |
| M2 | Domain-supported | Declared indicators or instruments exist; reliability not yet established |
| M3 | Reliability-tested | Inter-rater reliability, replay, or domain reliability evidence exists |
| M4 | Independently validated | External replay, validation, and cross-context evidence exist |

## 3. Core component map

| Component | Version | Role | Authority | Documentation status | Measurement maturity |
|---|---:|---|---|---|---|
| RippleLogic Canon | v11.4 | Governing decision architecture | Normative source | High documentation completeness | N/A for cascade specification; M1 for RLS cell scoring |
| Sentience Gradient Protocol | v6.4 | Moral-status and rights-of-protection interface | Companion protocol | High documentation completeness | M1 artificial-entity guidance; M0-M1 biological evaluation |
| RippleLogic Agent System | v11.4 | Agent runtime, controls, audit, conformance | Operational companion | High documentation completeness | M1 procedural architecture; field validation not yet complete |
| ripple.md Standard | v4.4 | Portable assurance and Decision Note wrapper | Interoperability standard | High documentation completeness | N/A process wrapper; M1 for real-world adoption evidence |
| RippleLogic Cascade Standard | v1.0 | Compact cascade reference | Release standard | High documentation completeness | N/A specification summary |
| CSV Gate Standard | v1.2 | Containment and Structural Viability gate standard | Gate standard | High documentation completeness | M1 structural-viability heuristics; UCI/HOI not validated |
| Source-Coupling Integrity Standard | v1.0 | Reality Grounding and CSV diagnostic for capability-source traceability | Companion standard | High documentation completeness | M1 diagnostic; no independent validation claim |
| Foundations Primer | v3.4 | Human doorway and teaching artifact | Informative companion | High documentation completeness | N/A |
| Aligners Sheet | v4.4 | Worked-run exemplar workbook | Tier 1-3 exemplar, not validator | Substantial worked-run completeness | M1 worked-run model; formulas verified in release QA; not calibrated |
| RLS Validation Protocol | v1.0 | Study design for RLS reliability and non-redundancy | Companion validation artifact | Substantial protocol-design completeness | M0->M1; defines path toward M3 |
| UCI / HOI diagnostics | within Canon and CSV | Structural coherence and hollowing / overhang diagnostics | Load-bearing diagnostic when material | Included in Canon / CSV | M0-M1; no cross-domain validated instrument |
| Computability vs Realizability Bridge | v11.4 surface | Generated != grounded != selectable != ethical guard | Canon bridge / guide surface | High documentation completeness | N/A |

## 4. Companion guidance additions

These artifacts are informative and non-normative. They sit below the Canon, SGP, Agent System, ripple.md Standard, Cascade Standard, and CSV Gate Standard.

| Artifact | Role | Authority | Documentation completeness | Measurement maturity |
|---|---|---|---:|---|
| `RIPPLELOGIC_PLAIN_ENGLISH_SUMMARY.md` | Public orientation doorway | Informative, non-normative | New | N/A |
| `RIPPLELOGIC_COMPARATIVE_POSITIONING_AND_RELATED_WORK.md` | Academic positioning and related work note | Informative, non-normative | New | N/A |
| `RIPPLELOGIC_IMPLEMENTATION_SCAFFOLDING.md` | Provisional heuristics, PCC profiles, roles, and fast-path guidance | Informative, non-normative | New | M1 only; heuristics capped at E1-E2 unless independently supported |
| `PCC_LITE_WORKED_EXAMPLE_REUSABLE_CUPS.md` | Minimal worked example | Informative, non-normative | New | M1 training-grade example |

## 5. Honest dashboard reading

The MathGov Core is strong on documentation and source completeness. Its major governing artifacts are mature as Tier 1-3 specifications.

The main measurement surfaces are less mature:

- **RLS cell scoring:** M1 until rater studies and dimensional separability tests are completed.
- **UCI/HOI:** M0-M1 until a measurement annex and domain indicators are validated.
- **Biological SGP:** M0-M1 until biological evaluation batteries are specified and tested.
- **Artificial-entity SGP:** M1 until architecture, continuity, valence, robustness, and anti-gaming tests are validated.
- **Aligners Sheet:** M1 as a worked-run exemplar until formula audit, test vectors, and reference-calculator replay are complete.

This is not a weakness if stated honestly. It means the framework is ready for validation work, not finished with validation work.

## 6. Priority maturity roadmap

| Priority | Target | Current maturity | Desired next maturity | Next step |
|---|---|---:|---:|---|
| 1 | RLS cell scoring | M1 | M3 | Inter-rater reliability and dimensional separability study |
| 2 | RLS 49-cell non-redundancy | M1 | M3 | Separability-case protocol plus correlation/factor analysis |
| 3 | UCI/HOI | M0-M1 | M2 | Provisional UCI Measurement Annex |
| 4 | Aligners Sheet | M1 | M2 | Formula audit and public test vectors |
| 5 | SGP biological evaluation | M0-M1 | M2 | Biological Evaluation Annex |
| 6 | SGP artificial-entity evaluation | M1 | M2 | Artificial Entity Evaluation Annex |
| 7 | Reference calculator | M0 | M2 | `mathgov-reference v0.1` replay of Canon test vectors |
| 8 | Pilot use | P1-P3 preparation | P3 | Shadow-mode pilot design |

## 7. Score boundary

Documentation status labels are internal source-completeness indicators, not numeric validation scores.

Measurement maturity scores are self-assessed instrument-readiness indicators.

They are not:

- empirical validation;
- proof of better decisions;
- legal certification;
- deployment certification;
- ProofPack status;
- Tier 4 readiness;
- automated moral truth.

## 8. Final component-map statement

**MathGov Core v11.4 is source-complete enough to proceed toward validation, but its major measurement surfaces must be advanced through reliability testing, measurement annexes, reference-calculator replay, and pilots before stronger empirical claims are made.**


Legacy verifier phrase: documentation/source-completeness scores are documentation/source completeness indicators only, not validation claims.


## Source-Coupling Integrity note

This release includes `docs/standards/Source_Coupling_Integrity_Standard_v1.0.md` and Canon Appendix AL as a MathGov-native Reality Grounding and CSV hardening diagnostic. It is not a sixth gate. It does not import external text. It cites Strüver (2026), *Source Amnesia*, only as related external scholarship.
