# MathGov / RippleLogic Core Release 2026.07

This repository package contains the MathGov / RippleLogic Core 6 for the v10.8 Category Grounding release line.

## Core method

Public method:

**Reality Grounding -> Rights Floor -> Tail-Risk Bound -> Containment -> Ripple Score**

Formal shorthand:

**RSG -> NCRC -> TRC -> Containment -> RLS**

Category Grounding is a required subdiscipline of Reality Grounding when category choice materially affects rights, tail risk, containment, SGP interpretation, authority, conformance, public claims, or optimized metrics. It is not a sixth public step or additional cascade gate.

UCI/HOI are structural diagnostics, not headline cascade stages. Gate-relevant UCI/HOI belongs inside Containment. Residual UCI/HOI is used only as special-case tie-break or monitoring evidence when RLS is tied, close, uncertainty-overlapped, or non-decisive.

## Core files

| Area | Markdown mirror | DOCX publication artifact |
|---|---|---|
| Canon | `docs/canon/RippleLogic_v10.8_Canon.md` | `docs/canon/RippleLogic_v10.8_Canon.docx` |
| SGP | `docs/sgp/SGP_v5.5.md` | `docs/sgp/SGP_v5.5.docx` |
| Agent System | `docs/agents/RippleLogic_Agent_System_v10.8.md` | `docs/agents/RippleLogic_Agent_System_v10.8.docx` |
| ripple.md Standard | `docs/standards/ripple_md_Standard_v3.6.md` | `docs/standards/ripple_md_Standard_v3.6.docx` |
| Foundations Primer | `docs/primer/RippleLogic_Foundations_Primer_v2.6.md` | `docs/primer/RippleLogic_Foundations_Primer_v2.6.docx` |
| Aligners Sheet | n/a | `docs/aligners/RippleLogic_Aligners_Sheet_v3.6.xlsx` |

## Canonical source policy

The DOCX files are the controlling publication byte streams for the Core 6 text artifacts in this release. This aligns the repository package with the RippleLogic Canon's Single Canonical Artifact Rule.

The Markdown (`.md`) files are GitHub-readable synchronization mirrors generated for review, diffing, AI parsing, and web documentation. They should remain synchronized in substance with the matching DOCX files.

If a discrepancy exists between a Markdown file and its DOCX equivalent, the discrepancy is a release defect to correct. Until corrected, the matching DOCX governs the text artifact.

For cross-artifact interpretation, the RippleLogic Canon's internal normative hierarchy controls.

## Release boundaries

This package is the MathGov / RippleLogic Core Release 2026.07 documentation package. It does not by itself claim:

- empirical validation,
- legal certification,
- deployment certification,
- schema completeness,
- validator completeness,
- ProofPack readiness,
- Tier 4 readiness,
- current-AI sentience,
- solved AI alignment,
- deterministic framework selection where the framework verdict is non-decisive.

Mathematical outputs are only as valid as the declared Reality Grounding evidence surface, data provenance, assumptions, uncertainty treatment, and claim boundary.

## Repository structure

```text
MathGov-Core/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── docs/
│   ├── canon/
│   │   ├── RippleLogic_v10.8_Canon.md
│   │   └── RippleLogic_v10.8_Canon.docx
│   ├── sgp/
│   │   ├── SGP_v5.5.md
│   │   └── SGP_v5.5.docx
│   ├── agents/
│   │   ├── RippleLogic_Agent_System_v10.8.md
│   │   └── RippleLogic_Agent_System_v10.8.docx
│   ├── standards/
│   │   ├── ripple_md_Standard_v3.6.md
│   │   └── ripple_md_Standard_v3.6.docx
│   ├── primer/
│   │   ├── RippleLogic_Foundations_Primer_v2.6.md
│   │   └── RippleLogic_Foundations_Primer_v2.6.docx
│   └── aligners/
│       └── RippleLogic_Aligners_Sheet_v3.6.xlsx
└── release/
    ├── RELEASE_NOTES.md
    ├── VERIFY_RELEASE.md
    ├── VERIFY_RELEASE.py
    └── SHA256SUMS.txt
```

## Verification

Requires Python 3.8+ and only the Python standard library.

See `release/VERIFY_RELEASE.md` for manual verification instructions.

To run automated verification from the repository root:

```bash
python release/VERIFY_RELEASE.py
```

Expected output:

```text
VERIFY_RELEASE: PASS (17 files checked)
```

## Licensing

The root repository license is Apache-2.0 for repository tooling, verification scripts, and code unless a specific file states a different license.

Core framework and specification text may contain artifact-level license notices such as CC BY 4.0. When a document contains an explicit artifact-level license notice, that notice controls for that artifact.

Future schemas, validators, reference calculators, or other code artifacts may declare their own permissive license in the relevant release record.
