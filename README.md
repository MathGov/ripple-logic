# MathGov / RippleLogic

**A rights-constrained, uncertainty-aware decision framework for research and teaching.**

RippleLogic asks whether an option is grounded in evidence, respects rights, meets tail-risk and structural-viability constraints, and only then how it compares with other qualifying options.

**Current publication: v13.0 / SGP v8.8 — Release I**

Exact build: `MG-RL-13.0-20260926-RELEASE-I`

[![Publication verification](https://github.com/MathGov/ripple-logic/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/MathGov/ripple-logic/actions/workflows/verify.yml)

## Start here

- **New to the framework:** [Public Introduction](releases/v13.0-release-i/Sources/MATHGOV_3R_1_2_PUBLIC_INTRO_v13.0.md), then the [Foundations Primer](releases/v13.0-release-i/Sources/RippleLogic_Foundations_Primer_v4.7.md).
- **Read the controlling specification:** [RippleLogic Canon v13.0](releases/v13.0-release-i/Sources/RippleLogic_v13.0_Canon.md) and [Sentience Gradient Protocol v8.8](releases/v13.0-release-i/Sources/SGP_v8.8.md).
- **Download the publication:** [Release I and its assets](https://github.com/MathGov/ripple-logic/releases/tag/v13.0-20260926-release-i).
- **Browse every format:** [PDF reading copies](releases/v13.0-release-i/Reading_PDFs/), [Markdown sources](releases/v13.0-release-i/Sources/), and [editable Word/Excel masters](releases/v13.0-release-i/Core_15/).
- **Review or reproduce:** [Reviewer and testing guide](releases/v13.0-release-i/Publication/Reviewer_And_Testing_Guide.md), [verification workflow](https://github.com/MathGov/ripple-logic/actions/workflows/verify.yml), and [publication integration notes](PUBLICATION.md).

## The decision sequence

**RG → RF/NCRC → TRC → CSV → RLS**

Reality grounding → rights floor / non-compensable rights constraint → tail-risk constraint → containment and structural viability → comparison of qualifying options using the RippleLogic Score.

## What this release contains

The complete Core 15 consists of fourteen Word documents and the Aligners Excel workbook, with synchronized reading formats, worked examples, scoped reference implementations, and reproducibility checks. Release I records eight reproduced errata and their associated corrections; see the [change report](releases/v13.0-release-i/Reports/Release_I_Adjudication.md).

The supplied publication is preserved byte-for-byte under [`releases/v13.0-release-i/`](releases/v13.0-release-i/). Repository navigation and GitHub integration live outside that frozen directory. The [manifest](releases/v13.0-release-i/VERSION_MANIFEST.json), [SHA-256 ledger](releases/v13.0-release-i/SHA256SUMS.txt), and [freeze record](releases/v13.0-release-i/FINAL_FREEZE.md) identify the exact files.

## Reproduce the checks

Use Python 3.13 and Node.js 22 on Linux for the hosted reference environment:

```sh
python -m pip install -r requirements-ci.txt
python -B releases/v13.0-release-i/verify_all.py --output-dir ../mathgov-results
```

The repository dependency wrapper adds the RFC 3339 date-time validator required by the supplied record tests. See [PUBLICATION.md](PUBLICATION.md) for the dependency correction and Windows test limitation. Test output belongs outside the frozen directory.

## Scope and limitations

This is a Tier 1–3 research-and-teaching specification with a bounded worked example and scoped tests. Passing those tests does not establish empirical validity, production readiness, Microsoft Excel certification, legal authority, physical-safety certification, or permission to execute decisions. See the [claim boundary](releases/v13.0-release-i/Publication/Conformance_Boundary.md) and [dependency limits](releases/v13.0-release-i/Publication/Dependency_Status.json).

## Citation, feedback, and history

Use [CITATION.cff](CITATION.cff) or cite **James McGaughran, MathGov / RippleLogic v13.0, Release I, 26 September 2026**, with the exact build and [versioned release URL](https://github.com/MathGov/ripple-logic/releases/tag/v13.0-20260926-release-i).

Report reproducible problems through [GitHub Issues](https://github.com/MathGov/ripple-logic/issues). Include the build, component, relevant passage or example, and expected versus observed behavior. Avoid sharing confidential case data.

Earlier publications remain available in [Releases](https://github.com/MathGov/ripple-logic/releases), including [v12.6](https://github.com/MathGov/ripple-logic/releases/tag/v12.6), and in Git history.

Licensed under [Apache 2.0](LICENSE), subject to the retained [NOTICE](NOTICE) and component/third-party rights statements.
