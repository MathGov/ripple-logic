# Governance and Release Policy

## Authority and scope

James McGaughran is the originating system architect and current release steward. Maintainer authority is custodial rather than evidential: it can merge, label, version, and publish, but it cannot convert an unsupported claim into a grounded one or waive the Rights Floor, TRC, or CSV.

## Source hierarchy

The current governing hierarchy is defined in [the v13.0 source hierarchy](releases/v13.0-release-i/SOURCE_HIERARCHY.md). The fourteen DOCX masters control specification semantics under Canon/SGP precedence. HTML, PDF, and Markdown are reading projections; the XLSX controls its frozen worked example only. Release manifests and SHA-256 records control shipped byte identity. Historical versions retain their own hierarchies.

## Change classes

- **Patch:** wording, formatting, navigation, metadata, examples, verification, or corrections that do not alter normative equations, thresholds, gate order, or protected semantics.
- **Minor version:** backward-compatible additions, optional profiles, validation instruments, or implementation surfaces.
- **Major version:** changes to normative equations, rights semantics, gate order, scope coordinates, thresholds, or compatibility expectations.

Every normative change must state dependencies, migration impact, falsification or revision triggers, and the artifacts that require regeneration.

## Pull requests

A pull request must identify its change class, affected canonical sections, claim type, evidence basis, compatibility impact, and verification performed. Automated assistance must be disclosed. Normative changes require independent human adversarial review before merge; a passing test suite is not that review.

### Solo-maintainer maintenance and delegation

The owner may explicitly authorize a bounded maintenance task and delegate its
implementation, checks and merge to an assistant. The PR must identify the
authorization record and exact scope. This is owner-authorized maintenance,
not a claim that the owner or an independent reviewer read every generated line.
The owner remains accountable for the authorization and resulting publication.
No further approval is required within an already authorized maintenance task.

This route covers publication navigation, installation guidance, CI, integrity
checks and accurate status documentation. It does not authorize a change to
normative equations, thresholds, rights semantics, scientific conclusions or
frozen research files. Unclear scope must be classified for human review rather
than silently treated as maintenance.

### Automated gate and its limits

The required `contribution-policy` check validates DCO sign-off trailers on PR
commits, rejects every change within an existing release directory, and requires
an explicit `Change-Class: maintenance` or `Change-Class: normative` declaration.
New release directories, declared normative changes, changes outside the
maintenance path set, and PRs from accounts other than the repository owner
require an approving review of the exact head commit by a different trusted
human collaborator. Self-approval, bot approval, stale approval and dismissed
approval do not qualify. A normative review must also explain its substantive
evidence and objections; CI checks the approval record, not the quality of its
scientific reasoning.

Owner maintenance PRs instead require an `Owner-Authorization:` reference.
This records a human responsibility; neither a text field nor a sign-off proves
authorization, authorship, rights ownership or review quality. The check is a
repository workflow safeguard, not a tamper-proof independent audit. Changes to
the check itself must be disclosed and examined as policy changes.

Main requires `verify`, `site` and `contribution-policy`. GitHub's blanket
approving-review count remains zero so authorized solo maintenance is possible;
the contribution gate applies the narrower review requirement above. This is
intentional and must not be described as universal independent review.

## Branch and release practice

- `main` contains the current public source line.
- Substantive work occurs in reviewable branches.
- Public releases are tagged and accompanied by `CITATION.cff`, release manifests, checksums, release notes, and successful automated verification.
- Historical publication directories retain their published paths under `releases/` so old citations remain usable. The root README and maintained site identify the current version.
- Frozen publication files are never edited in place. Corrections require a separately identified release; repository presentation and CI integration live outside the frozen directory.

## Contributions and sign-off

Contributions use Developer Certificate of Origin sign-off. A signed-off commit states that the contributor has the right to submit the work under the project license. No contributor or maintainer may claim empirical, legal, safety, or deployment certification beyond the released evidence.

Use `git commit -s`. A squash merge must retain the contributor's sign-off in its
message. Existing history is not rewritten to manufacture retrospective sign-offs.

## Disputes and appeals

Disputes should be resolved through source evidence, explicit definitions, dependency tracing, reproducible tests, and recorded counterarguments. Maintainer decisions may be challenged through a focused issue or pull request that identifies the exact source surface and proposed correction.
