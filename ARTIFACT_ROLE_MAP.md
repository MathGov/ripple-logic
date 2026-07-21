# Artifact Role Map

This release separates governing sources, companion standards, worked-run exemplars, and release-engineering files.

| Role                                  | Artifact                                                                     | Authority                                     | Notes                                                                                                                   |
| ------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Governing source                      | `docs/canon/RippleLogic_v12.4_Canon.md`                                      | Highest RippleLogic semantic authority        | Markdown source controls over derived DOCX/PDF renderings.                                                              |
| Moral-status companion                | `docs/sgp/SGP_v8.3.md`                                                       | Governs SGP outputs and moral-status handling | Does not alter RF/NCRC, TRC, CSV, or RLS gates.                                                                         |
| Portable wrapper standard             | `docs/standards/ripple_md_Standard_v5.3.md`                                  | Wrapper obligations only                      | Adds assurance/reconstructability; does not reorder the Canon cascade.                                                  |
| Agent deployment spec                 | `docs/agents/RippleLogic_Agent_System_v12.2.md`                              | Runtime-control companion                     | Governs agent control surfaces and hard invariants.                                                                     |
| Informative primer                    | `docs/primer/RippleLogic_Foundations_Primer_v4.2.md`                         | Informative                                   | Public doorway; does not control the Canon.                                                                             |
| Worked-run exemplar                   | `docs/aligners/RippleLogic_Aligners_Sheet_v5.4.xlsx`                         | Exemplar/training tool                        | Not a validator, not a ProofPack, not empirical validation.                                                             |
| Compact reference                     | `docs/standards/RippleLogic_Cascade_Standard_v2.4.md`                        | Summary reference                             | Canon controls if conflict occurs.                                                                                      |
| CSV compact reference                 | `docs/standards/CSV_Gate_Standard_v2.2.md`                                   | Summary reference                             | Canon controls if conflict occurs.                                                                                      |
| Release support                       | README, CHANGELOG, manifest, verification scripts, reports                   | Release engineering                           | Do not define framework theory.                                                                                         |
| Computability vs Realizability Bridge | `docs/guides/COMPUTABILITY_VS_REALIZABILITY_BRIDGE.md` and Canon Appendix AK | Companion clarification                       | Prevents generated/computable artifacts from being mistaken for grounded, selectable, executable, or ethical decisions. |

| RLS validation package | `docs/validation/rls/` | Research support | Protocol/workbook for testing RLS dimensional non-overlap and inter-rater reliability; not validation results. |
| Examples | `docs/examples/` | Informative | Public learning examples; Canon controls if conflict occurs. |
| Diagrams | `docs/diagrams/` | Informative | Visual navigation aids; Canon controls if conflict occurs. |

## v12.0 hardening additions

| Artifact family            | Location                                                                                                                   | Role                                                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Hardening guides           | `docs/guides/`                                                                                                             | implementation guidance; Canon controls if conflict occurs                |
| Validation scaffolding     | `docs/validation/`                                                                                                         | research and calibration protocols; not validation evidence by themselves |
| Historical release integration report | `archive/release_history/IMPLEMENTED_IMPROVEMENTS_COMPANION_READINESS.md`                                                      | archived reviewer-feedback integration and companion-readiness lineage; not current authority |
| Historical implemented-improvements reports | `archive/release_history/IMPLEMENTED_IMPROVEMENTS_FINAL.md` and `archive/release_history/IMPLEMENTED_IMPROVEMENTS_LAYOUT_FINAL.md` | archived production lineage; current release reports are under `release/` |

## Companion readability, positioning, and implementation additions

| Artifact                   | Location                                                                | Role                                                                           | Authority                                                            |
| -------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| Plain-English summary      | `docs/guides/RIPPLELOGIC_PLAIN_ENGLISH_SUMMARY.md`                      | Public orientation doorway                                                     | Informative, non-normative; Canon controls if conflict occurs        |
| Public 3R / 1-2 intro      | `docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_4.md` / `.docx` / `.pdf`   | Human-first teaching companion                                                 | Informative, non-normative; Canon controls if conflict occurs        |
| Comparative positioning    | `docs/research/RIPPLELOGIC_COMPARATIVE_POSITIONING_AND_RELATED_WORK.md` | Academic related-work and positioning note                                     | Informative, non-normative; Canon controls if conflict occurs        |
| Implementation scaffolding | `docs/guides/RIPPLELOGIC_IMPLEMENTATION_SCAFFOLDING.md`                 | Provisional heuristics, PCC profiles, fast-path rules, and institutional roles | Informative, non-normative; heuristics are not validated instruments |
| PCC-Lite worked example    | `docs/examples/PCC_LITE_WORKED_EXAMPLE_REUSABLE_CUPS.md`                | Minimal training-grade worked run                                              | Informative, non-normative; not validation                           |


## Source-Coupling Integrity note

This release includes `docs/standards/Source_Coupling_Integrity_Standard_v2.1.md` and Canon Appendix AL as a MathGov-native Reality Grounding and CSV hardening diagnostic. It is not a sixth gate, does not import any external ontology, and defines Source-Coupling Integrity entirely in MathGov-native language.


- `docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.1.md`: v12.0 compact evidence profile inside Reality Grounding and CSV for material physical or causal action. Canon controls if conflict occurs.


## Appendix AD machine-readable companion

| Artifact | Role | Authority | Notes |
|---|---|---|---|
| `docs/canon/AD_49_Cell_Welfare_Dictionary.csv` | One-row-per-cell companion for Appendix AD | Informative companion; Canon controls | Preserves the wide-record structure for implementation, audits, and future schema work. |

## Operational assurance companion set

`docs/assurance/` is an informative implementation-preparation layer. It does not outrank the Canon, SGP, or release manifest. It provides reusable records for alignment-scope boundaries, parameter and authority locking, governance-parameter attacks, distribution shift, domain profiles, security acceptance, independent replay, maturity claims, and reference-semantics planning.

## Reproducibility implementation layer

| Artifact | Role | Authority boundary |
|---|---|---|
| Reproducibility and Use Standard v1.0 | Normative implementation companion | Canon controls semantics; this standard controls run record, state machine, and replay |
| Normative Kernel Index v1.0 | Machine-readable pointer map | Not an alternate Canon |
| Run Record Schema v1 | Structural record contract | Does not prove evidence or measurement validity |
| Run Validator | Semantic contradiction checker | Not a reference calculator or moral-truth engine |


## v12.3 integration note

WDBIP v1.4 is included as a Canon-subordinate normative implementation companion beneath RLS. ripple.md v5.3 controls its wrapper assurance surface. Run-record v2 separates V0 schema validity, V1 semantic conformance, and V2 evidence/use review. The two principal governing sources remain the Canon and SGP.
