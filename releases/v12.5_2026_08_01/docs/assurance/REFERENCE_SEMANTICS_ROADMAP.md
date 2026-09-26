# MathGov Reference Semantics Roadmap

**Status:** Informative future-work specification. No reference evaluator or ProofPack is claimed in v12.2.

## Target workstream

A separate `mathgov-reference` package should eventually provide:

1. canonical JSON/YAML schemas for run identity, evidence, RG, NCRC, TRC, CSV, RLS, SGP interfaces, authority, and execution boundaries;
2. valid and invalid fixtures;
3. deterministic parsing and status resolution;
4. golden vectors and cross-engine numerical tolerances;
5. version-aware migrations;
6. a parameter and authority lockfile;
7. replay instructions and discrepancy taxonomy;
8. machine-readable reason codes;
9. independent implementation and review;
10. signed releases and compatibility tests.

## Required separation

- Schema validity is not empirical validity.
- A deterministic evaluator is not automated moral truth.
- Reference-calculator agreement is not proof that inputs, thresholds, scenarios, or value choices are correct.
- Machine conformance is not legal authority, deployment permission, or physical safety certification.

## Entry condition for stronger claims

No ProofPack, Tier 4, reference-calculator, or machine-verifiable-ecosystem claim is available until the package is publicly released, independently replayed, and governed by explicit compatibility and correction procedures.
