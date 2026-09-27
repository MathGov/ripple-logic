# Current publication status and maintenance record

Updated 27 September 2026 (Asia/Bangkok).

The current research publication is **MathGov / RippleLogic v13.0, Release I**,
build `MG-RL-13.0-20260926-RELEASE-I`.
[Read online](https://mathgov.github.io/ripple-logic/) or
[download the fixed release](https://github.com/MathGov/ripple-logic/releases/tag/v13.0-20260926-release-i).

## Publication identity and immutability

The original ZIP SHA-256 remains
`c7ece3a604980fa859e41cd63bbebe6d9adc0953e795737c8a38c16b82ac4d85`.
It contains 288 files, including 287 ledger-controlled files and the ledger.
GitHub's release API reports this exact release as immutable. Earlier statements
that Release I was not asset-locked are outdated. The old receipts retain their
original dates and tested commits; they are historical evidence, not silently
updated reports. Release metadata and maintained guidance are distinct from
immutable assets and tags.

Preparation-time statements such as `PREPARED_NOT_PUBLISHED` inside the frozen
package remain accurate records of its preparation. The actual public hosting
status is recorded here, in release receipts and in
[GitHub Actions](https://github.com/MathGov/ripple-logic/actions/workflows/verify.yml).

## Completed Windows correction

[PR #11](https://github.com/MathGov/ripple-logic/pull/11) adds `PYTHONUTF8=1`
and complete PowerShell commands to the maintained installation guide. This
prevents legacy-default-encoding errors in the frozen verifier's subprocesses.
Use [INSTALLATION.md](INSTALLATION.md) for repository and ZIP setup.
The existing Windows loopback file-lock race remains disclosed. Ubuntu is the
hosted reference; no complete native Windows pass or Excel parity is claimed.

## Safe source and packaging workflow

Build from a clean tracked checkout or the verified original publication ZIP.
Do not package a whole working directory with miscellaneous untracked files.
The site checker requires exactly 288 files in the frozen current release tree,
and the site builder now checks that inventory before copying anything.

The publication audit found older, untracked material in a local working folder.
It was outside the public tracked inventory. Local recovery handling preserves
those files separately with hashes; it is not part of the public research bundle.
The local recovery inventory must be checked before any later cleanup.

## Owner authorization and review classification

After the four-item audit, the repository owner instructed: “finish those all
in full depth, form and detail.” This authorizes completion of the Windows
guidance, recoverable separation of extra local files, corrected release-status
wording, and a documented/enforced maintenance contribution process.

This work is **maintenance**, with automated assistance disclosed. It does not
change frozen specifications, results or normative claims. The authorization is
a bounded delegation to implement, test and publish these changes; it is not
evidence of a human line-by-line code review or independent scientific review.

The [governance policy](GOVERNANCE.md) distinguishes owner-authorized maintenance
from normative changes and outside contributions requiring another trusted human
reviewer. The required contribution check validates sign-off syntax, frozen-tree
protection, declared change class and the applicable approval record. It cannot
prove the truth of authorization claims or the quality of a review.

## Evidence and remaining research boundaries

The 27 September audit checked all 287 raw GitHub ledger entries, all 283
non-hidden ledger entries served through Pages, all seven release downloads,
and 1,414 local links across 39 HTML pages. Original publication bytes matched;
no broken local HTML targets were found. All fourteen live readers fit a
390-pixel viewport and live search opened its intended passage.

This establishes publication integrity and accessibility checks within their
tested scope. It does not independently validate every scientific or normative
claim. The [dependency inventory](releases/v13.0-release-i/Publication/Dependency_Status.json)
and [conformance boundary](releases/v13.0-release-i/Publication/Conformance_Boundary.md)
still apply: unbundled registries/profiles, complete machine-vector and study
packets, independent empirical validation and native Excel verification are
additional research/implementation work. No placeholders or invented evidence
have been added to make these claims appear complete.
