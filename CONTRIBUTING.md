# Contributing and Review

Start with the [current publication](README.md) and [source hierarchy](releases/v13.0-release-i/SOURCE_HIERARCHY.md). Do not edit frozen files under `releases/` in place. Propose specification corrections in an issue or separately versioned publication; navigation, site, and CI changes belong outside those snapshots.

Run the checks in [INSTALLATION.md](INSTALLATION.md). For presentation changes, install `requirements-site.txt`, then run `python scripts/build_site.py`, `python scripts/check_site.py`, `npm ci`, `npx playwright install chromium`, and `npm run test:site`. The builder requires an unused output directory. Hosted checks use Ubuntu, Python 3.13, and Node.js 22.

Contributions should identify the affected artifact, cite the relevant Canon section, and distinguish content changes from release-engineering changes.

Useful issue categories: claim-boundary issue, terminology/collapse issue, calculation issue, citation issue, release-integrity issue, workbook issue, and implementation question.

Do not propose Tier 4, ProofPack, empirical-validation, legal-certification, deployment-certification, current-AI-sentience, or automatic moral-truth claims unless the required evidence package exists.

## Governance, conduct, and sign-off

Contributions are governed by `GOVERNANCE.md` and `CODE_OF_CONDUCT.md`. Commits must include Developer Certificate of Origin sign-off:

```text
Signed-off-by: Your Name <your.email@example.com>
```

Use `git commit -s` to add the line. Sign-off asserts that you have the right to submit the contribution under Apache-2.0; it is not a claim that MathGov has validated or certified the contribution.
