# Governance and Release Policy

## Authority and scope

James McGaughran is the originating system architect and current release steward. Maintainer authority is custodial rather than evidential: it can merge, label, version, and publish, but it cannot convert an unsupported claim into a grounded one or waive the Rights Floor, TRC, or CSV.

## Source hierarchy

The governing hierarchy is defined in `SOURCE_HIERARCHY.md`. Canonical Markdown controls semantic interpretation when a DOCX or PDF reading mirror diverges. Release manifests and SHA-256 records control the identity of shipped byte streams.

## Change classes

- **Patch:** wording, formatting, navigation, metadata, examples, verification, or corrections that do not alter normative equations, thresholds, gate order, or protected semantics.
- **Minor version:** backward-compatible additions, optional profiles, validation instruments, or implementation surfaces.
- **Major version:** changes to normative equations, rights semantics, gate order, scope coordinates, thresholds, or compatibility expectations.

Every normative change must state dependencies, migration impact, falsification or revision triggers, and the artifacts that require regeneration.

## Pull requests

A pull request should identify its change class, affected canonical sections, claim type, evidence basis, compatibility impact, and verification performed. Normative changes require at least one independent adversarial review before merge. Machine-generated edits require human review and accountable sign-off.

## Branch and release practice

- `main` contains the current public source line.
- Substantive work occurs in reviewable branches.
- Public releases are tagged and accompanied by `CITATION.cff`, release manifests, checksums, release notes, and successful automated verification.
- Historical production reports belong under `archive/release_history/`, not in the public release doorway.

## Contributions and sign-off

Contributions use Developer Certificate of Origin sign-off. A signed-off commit states that the contributor has the right to submit the work under the project license. No contributor or maintainer may claim empirical, legal, safety, or deployment certification beyond the released evidence.

## Disputes and appeals

Disputes should be resolved through source evidence, explicit definitions, dependency tracing, reproducible tests, and recorded counterarguments. Maintainer decisions may be challenged through a focused issue or pull request that identifies the exact source surface and proposed correction.
