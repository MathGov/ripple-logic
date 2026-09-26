# Missing by Design: Referenced Future Artifacts Not Bundled in This Release

This release intentionally references some future or companion artifacts that are not shipped as active release assets. Their absence is not a broken link if they are listed here. No one should infer that this package claims to include them.

## Not bundled and not claimable

| Artifact | Status in this release | Why it is not bundled | What would be required |
|---|---|---|---|
| ProofPack | Not included | Tier 4 claims remain prohibited | independently replayable reference implementation, schemas, fixtures, test vectors, and validation evidence |
| Reference calculator | Not included | current package is documentation/source plus worked-run workbook | tested implementation reproducing the canonical equations and edge cases |
| Machine-readable Appendix R vectors | Not included as complete machine package | Canon preserves mathematical specification, not full machine fixture suite | schema-bound test vectors and replay harness |
| RPAP / redaction protocol companion | Referenced where relevant, not active in this package | redaction protocol remains separate/future support | bundled protocol, examples, and conformance checks |
| PFAP / projection protocol companion | Referenced where relevant, not active in this package | projection protocol remains separate/future support | bundled protocol, examples, and conformance checks |
| Full schemas | Not included as a complete schema package | release does not claim schema validation | JSON/YAML schemas, examples, invalid fixtures, validator script |
| UCI measurement annex | Not included | UCI/HOI measurement maturity remains future validation work | domain indicators, calibration evidence, and inter-rater reliability |
| SGP biological evaluation annex | Not included | biological evaluation remains guidance-stage | species-appropriate batteries and comparative-cognition review |
| SGP artificial-entity annex | Not included | artificial-entity evaluation requires anti-fluency and anti-gaming test batteries | architecture/evidence standards, deception tests, and controlled evaluation protocols |
| Realizability-native compute kernel | Not included | this release governs selectability and execution authority, not substrate-level prevention of unrealizable state representation | formal methods, simulation constraints, physics/engineering validity checks, and a reference implementation interface |

| Aligners Sheet test-vector pack | Not included as a validation asset | current workbook is a worked-run exemplar, not a validator | known input/output fixtures, edge cases, recalculation protocol, and independent replay |
| Pilot protocol / external review packet | Not included as completed validation | no empirical validation or policy-facing claim is made | reviewer roles, shadow-mode protocol, inter-rater design, and limitation reporting |
| Persuasion Integrity / AI self-validation guardrail | Not included as a standalone guide | safeguards are distributed across Agent System and claim-boundary files | short guide, checklist, provenance rules, adversarial review, and high-stakes release block |

## Rule for readers

If an artifact is mentioned in the core files but is listed above, treat it as a roadmap dependency or future validation asset unless it is later bundled with hashes and release notes. Do not cite it as shipped, active, validated, or required for current Tier 1-3 source-release status.


Lineage note: see `LINEAGE.md` for how to read superseded historical release-line material. Current component pins and hashes control.
