# MathGov / RippleLogic v10.6 + SGP v5.3 Core Release

This repository contains the public release package for the **RippleLogic Canon v10.6** and **Sentience Gradient Protocol (SGP) v5.3** line of the MathGov framework.

## Governing core

The strict governing core is:

1. `GOVERNING_CORE/RippleLogic_v10.6_Canon_FINAL_RELEASE_READY.docx`
2. `GOVERNING_CORE/SGP_v5.3_FINAL_RELEASE_READY.docx`

The Markdown files are GitHub-readable derivatives generated from the manifest-pinned DOCX files. For this v10.6 / SGP v5.3 release, if a Markdown rendering differs from the corresponding DOCX, the DOCX plus the SHA-256 manifest controls.

## Synchronized companions

- `COMPANIONS/ripple_md_Standard_v3.4_FINAL_RELEASE_READY.docx` and `.md`: portable assurance wrapper and alignment contract.
- `COMPANIONS/RippleLogic_Agent_System_v10.6_FINAL_RELEASE_READY.docx` and `.md`: AI/hybrid-agent runtime governance, control placement, audit, and deployment specification.
- `COMPANIONS/RippleLogic_Foundations_Primer_v2.4_FINAL_RELEASE_READY.docx` and `.md`: informative human doorway into MathGov / RippleLogic / SGP.
- `COMPANIONS/RippleLogic_Aligners_Sheet_v3.4_FINAL_RELEASE_READY.xlsx`: worked-run spreadsheet exemplar for training, replay, and demonstration. It is not a validator, ProofPack, empirical-validation package, or deployment certification.

## Release support

- `RELEASE_SUPPORT/RippleLogic_v10.6_Methodology_Completion_and_Companion_Synchronization_Summary_FINAL_RELEASE_READY.docx` and `.md`: informative release-summary companion.
- `RELEASE_SUPPORT/GITHUB_FINAL_VERIFICATION_REPORT.md`: final verification summary.
- `RELEASE_SUPPORT/FEEDBACK_INTEGRATION_REPORT.md`: accepted/rejected feedback and implementation rationale.
- `RELEASE_SUPPORT/PATCH_CHANGELOG_FINAL_June2.json`: machine-readable patch log.
- `RELEASE_SUPPORT/MARKDOWN_CONVERSION_REPORT.md`: Markdown conversion and symbol-scan summary.
- `RELEASE_SUPPORT/README_MARKDOWN_SET.md`: Markdown source-set guide.
- `RELEASE_SUPPORT/FINAL_RELEASE_BUILD_REPORT_2026-06-05.md`: final package build and verification note.

## Claim boundary

This is a **Tier 1-3 core-foundation and companion-synchronization release**. It does **not** claim:

- Tier 4 readiness
- ProofPack completeness
- empirical validation
- legal-compliance certification
- deployment-readiness certification
- machine-verifiable ecosystem completeness
- completed biological SGP measurement
- current-AI sentience

Stronger claims require separately published evidence, schemas, validators, reference calculators, test vectors, replay instructions, legal localization, pilots, independent review, and/or domain-specific validation.

## Recommended reading path

1. Start with the Primer for orientation.
2. Read the Canon for the governing RippleLogic decision architecture.
3. Read SGP for moral-status / protection handling.
4. Use ripple.md if implementing an assurance wrapper or decision-note protocol.
5. Use the Agent System if building or evaluating RippleLogic-governed AI/hybrid agents.
6. Use the Aligners Sheet only as a worked-run exemplar.

## Integrity verification

From the repository root:

```bash
sha256sum -c RELEASE_INTEGRITY/SHA256_MANIFEST_GITHUB_FINAL.txt
```

Office artifacts were checked for valid OOXML ZIP integrity. DOCX comments and tracked-change insertion/deletion/move markers were scanned. The workbook was imported and formula-error scanned.

## Citation

See `CITATION.cff`.

## License note

See `LICENSE_NOTICE.md`.

## GitHub packaging note

`.gitattributes` marks Office and archive artifacts as binary and normalizes text-file line endings for repository stability.
