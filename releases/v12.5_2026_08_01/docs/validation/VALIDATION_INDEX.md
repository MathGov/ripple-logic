# Validation Index

This directory collects validation and calibration scaffolding. These files support future empirical work; they do not by themselves validate the framework.

## Current validation packages

| Area    | File or folder                                                    | Purpose                                                                             |
| ------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| RLS     | `docs/validation/rls/`                                            | correlation/factor analysis, inter-rater reliability, scalar-comparator testing     |
| RF/NCRC | `docs/validation/rights/RIGHTS_THRESHOLD_GOVERNANCE_NOTE_v1_0.md` | threshold governance and calibration plan                                           |
| TRC     | `docs/validation/trc/TRC_SCENARIO_DISCOVERY_PROTOCOL_v1_0.md`     | scenario discovery, red-team, rejected-scenario log                                 |
| CSV     | `docs/validation/csv/CSV_MEASUREMENT_MATURITY_NOTE_v1_0.md`       | maturity ladder for qualitative, indicator-supported, calibrated, and validated CSV |
| SGP     | `docs/validation/sgp/SGP_VALIDATION_PROTOCOL_v2_1.md`             | SGP MPS/FPP/GPR/SPR/ICP/RMCP/P100 reliability, construct-validity, anti-theatre, and cross-substrate validation planning   |

## Boundary

Validation scaffolding is not validation evidence. Public claims must distinguish protocol existence from completed empirical validation.

## Operational assurance companions

The non-normative `docs/assurance/` directory provides the parameter lock, attack model, requalification, domain-profile, security-acceptance, replay, maturity, and reference-semantics templates needed to turn validation plans into reproducible studies. These are scaffolds, not results.

## Run-record conformance

`release/VALIDATE_MATHGOV_RUN.py` and `tests/run_records/` provide executable R0/R1 conformance vectors for the minimum run record, cascade semantics, material-obligation integrity, carrier nonperformance, control-change boundaries, and hidden-human-compensation routing. This is software/conformance testing, not empirical outcome validation.
