# Contributing to RippleLogic

Thanks for your interest in improving RippleLogic.

RippleLogic is published as **versioned canon releases**. The canonical snapshot is defined by the **GitHub Release tag + attached assets**, mirrored under `releases/<version>_<YYYY-MM-DD>/`.

That means:
- You can open issues and propose changes at any time.
- Changes are considered “canon” only when included in a tagged Release and its matching release folder.

## Ways to contribute

### 1) Report an issue (recommended starting point)
Please open a GitHub Issue and include:
- **What you observed** (include exact file name + version folder, e.g., `releases/v8.1_2026-02-14/...`)
- **Expected behavior**
- **Steps to reproduce** (if applicable)
- **Why it matters** (risk, rights-floor implications, audit clarity, implementability)

### 2) Propose a change (Pull Request)
A good PR includes:
- **Summary** of the change and motivation
- **Scope** (doc-only / schemas / templates / release packaging)
- **Impact** on:
  - rights floors / constraints language (NCRC, TRC, containment)
  - tier claims (avoid Tier-4 determinism claims)
  - auditability and reproducibility
- If editing release artifacts: propose changes against the next release folder, not retroactively rewriting past canon.

## Style and guardrails
- Prefer clarity over cleverness.
- Avoid overstating capabilities. RippleLogic does not claim omniscience or deterministic Tier-4 proofs in public releases unless explicitly supported by verified artifacts.
- Keep “canon” language aligned across:
  - Core spec
  - SGP
  - Agent System
  - Release notes and checksums

## Integrity and verification
If you add or modify binary artifacts in a release folder:
- Update the release checksum list (SHA256SUMS) and ensure it matches the exact bytes of uploaded assets.
- Keep filenames stable and versioned.

## License
By contributing, you agree your contributions are licensed under the repository’s license (see `LICENSE`).
