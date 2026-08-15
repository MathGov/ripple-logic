# Roadmap


For the expanded future-work list, see `FUTURE_WORK_ROADMAP.md`. Items listed there are intentionally not claimed as complete in this release.

## Current v12.6 / SGP v8.5 public research/source release

Current status: source/specification and validation-preparation package hardened for public review, teaching, controlled pilot design, and structured critique. It is not empirically validated or deployment-certified. Next work should prioritize evidence: RLS rater sprints, UCI/HOI measurement development, SGP and RMCP/P100 validation studies, independent replay, reference-calculator planning, and low-risk pilot design.


## Phase 1 - Public review release

- Maintain clear source hierarchy.
- Collect terminology, calculation, and claim-boundary issues through GitHub templates.
- Add polished visuals and public examples.
- Carry the computability-vs-realizability boundary into public on-ramps so generated possibilities are never treated as selectable decisions by default.

## Phase 1B - Hardening adoption

- Apply gate-boundary discriminator to 3 public worked examples.
- Test PCC profiles across low-, medium-, and high-stakes examples.
- Run a rights-threshold governance review on at least one rights-sensitive scenario.
- Apply subgroup discovery guide to every public worked example.
- Run a TRC scenario-discovery red-team exercise.
- Apply CSV maturity labels to every public worked example.
- Pilot the SGP validation protocol with controlled entity profiles.

## Phase 2 - Worked-run evidence

- Complete 3-5 public worked examples with PCC records.
- Publish completed Aligners Sheet workbooks.
- Run RLS inter-rater reliability and factor/correlation pilot.

## Phase 3 - Reference implementation

- Extend the bundled minimum run-record schema and contradiction validator into complete JSON/YAML schemas for PCC, Decision Note, RG, RF/NCRC, TRC, CSV, RLS, and SGP interface records.
- Build the reference calculator and a general validator CLI that reproduces Canon equations and Appendix R vectors.
- Add canonical test vectors and edge-case cases.
- Explore a future realizability-interface package that can connect RippleLogic RG/CSV records to formal methods, simulation constraints, physical feasibility checks, and system-stability tooling without changing the canonical cascade.

## Phase 4 - External review and pilots

- Invite independent review by AI governance, public policy, law, ethics, and systems experts.
- Run shadow-mode pilots in low-risk settings.
- Publish limitations, defects, disagreements, and revisions.

## Phase 5 - ProofPack candidate

No Tier 4 or ProofPack claim is available until a public, independently replayable package exists with schemas, validators, reference calculator, test vectors, replayable records, and independent verification.


## Historical carried-forward v12.0 Core Completion Polish

This patch preserves the v12.0 content line and v12.0 hardening posture while improving public release integrity: Agent System table readability, Aligners Sheet sanity-surface correction, Gap/δ caveat, historical-lineage disambiguation, reviewer quick-start navigation, missing-by-design artifact disclosure, compact claim-boundary doorway, and Canon navigation map. It adds no ProofPack, Tier 4, empirical validation, legal certification, deployment certification, reference-calculator, or automated moral-truth claim.


## Historical carried-forward v12.0 Realizability Bridge

Added the computability-vs-realizability boundary as a public and technical bridge. Future work may explore formal-methods interfaces, simulation/physics constraints, and system-stability tooling that can feed RG and CSV records without changing the canonical cascade.


## RLS dimensional separability priority

The seven welfare dimensions should be treated as a minimal conceptual covering set, not as statistically independent variables. Future RLS validation should test conceptual non-redundancy through separability cases, then use correlation and factor analysis as secondary diagnostics.

## v12.2 Operational Assurance Programme

Current v12.6 source work is frozen after same-version release-integrity hardening. The next workstream is evidence and implementation, not another broad philosophical rewrite:

1. reference semantics and deterministic evaluator;
2. parameter and authority locking;
3. adversarial configuration and security acceptance testing;
4. domain profiles and distribution-shift requalification;
5. independent replay, reliability studies, construct validation, and shadow-mode pilots.

The `docs/assurance/` templates prepare this programme without claiming it is complete.
