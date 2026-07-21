# MathGov Measurement and Parameter Maturity Register v1.0

## Status

Candidate Canon-owned registry for the next synchronized MathGov core release. This file does not alter an already released Canon until listed in that release's manifest and source hierarchy.

## Purpose

MathGov contains several load-bearing surfaces whose architecture is specified before their empirical calibration is complete. It also contains normative priors and governance conventions that should never be misdescribed as empirical constants. A single untyped "provisional measurement" list would collapse those categories.

This register therefore assigns every listed object a **status class**, **maturity token**, **maximum permissible claim**, and **promotion or review condition**.

## Status classes

| Status class | Meaning |
|---|---|
| `EMPIRICAL_CONSTRUCT` | Intended to represent a measurable feature and eligible for empirical validation. |
| `MODEL_COMPONENT` | Computational structure whose performance requires calibration/backtesting. |
| `NORMATIVE_PRIOR` | Explicit ethical or constitutional commitment; not promoted into an empirical fact. |
| `GOVERNANCE_CONVENTION` | Decision rule chosen for consistency or caution; requires justification and sensitivity, not discovery as a natural constant. |
| `DESIGN_TARGET` | Future capability not available in the present release. |

## Register

| Construct | Owner | Status class | Current token | Load-bearing use | Maximum permissible claim | Promotion or review condition |
|---|---|---|---|---|---|---|
| UCI | Canon | EMPIRICAL_CONSTRUCT | UCI-M1_PROVISIONAL framework-wide | CSV diagnostics and permitted tie-break use | Domain-bounded use with declared indicators and uncertainty; no claim of cross-domain validated UCI | Domain annex with reliability, construct validity, normalization, structural independence, and external review |
| Kernel K | Canon | MODEL_COMPONENT | K0_NONE default; K1_STARTER where used | Ripple propagation | K0_NONE is conformant; K1 supports only bounded sensitivity use | Domain calibration, backtesting, error bounds, and independent replay for K3/K4 |
| HOI | Canon | EMPIRICAL_CONSTRUCT | HOI-PROVISIONAL | Monitoring and residual diagnostic | Monitoring and caution only; not an independent gate | Longitudinal evidence of incremental prediction and failure bounds |
| PLSS prominence model | Canon | MODEL_COMPONENT | PLSS-UNVALIDATED | Residual local-scope weighting | Formal floor and admissibility invariance may be claimed; empirical convergence and anti-gaming performance may not | Reliability, boundary-gaming, and decision-utility studies |
| MPS thresholds and evidence intervals | SGP | EMPIRICAL_CONSTRUCT | SGP-PROVISIONAL-THRESHOLD | Protection posture and welfare-inclusion hypotheses | Evidence posture only; not probability of consciousness, moral worth, or direct multiplier | Calibration against expert review, decision-error costs, and cross-substrate evidence |
| RMCP / RMCI_L / P100 | SGP | EMPIRICAL_CONSTRUCT | SGP-RMCP-PROVISIONAL | Informative capacity profile; GPR/SPR input | Capacity evidence only; not sentience, worth, wisdom, or authority | Discriminant, predictive, cross-domain, cross-substrate, weaponization, and replication studies |
| Rights thresholds | Canon | NORMATIVE_PRIOR | GOVERNANCE-PRIOR | RF/NCRC | Versioned ethical floor with sensitivity and legal-context disclosure | Reconsidered only through governed normative revision, not "validated" as a natural constant |
| Constitutional weight floors | Canon | NORMATIVE_PRIOR | GOVERNANCE-PRIOR | RLS anti-erasure floor | Explicit constitutional prior | Governed normative revision |
| Subgroup fallback multiplier | Canon | GOVERNANCE_CONVENTION | GOVERNANCE-PRIOR | Conservative subgroup protection | Conservative fallback, not empirical constant | Domain calibration and sensitivity review |
| Missing-data phantom magnitude | Canon | GOVERNANCE_CONVENTION | GOVERNANCE-PRIOR | Ignorance penalty | Challengeable conservative prior | Reference-suite sensitivity and error-cost analysis |
| RLS decisiveness delta | Canon | GOVERNANCE_CONVENTION | GOVERNANCE-CONVENTION | Decisive/non-decisive classification | Conservative rule, not literal z-score guarantee | Domain calibration against selection-error costs |
| ProofPack / Tier 4 | Canon | DESIGN_TARGET | UNAVAILABLE | Strong machine-verifiable ecosystem claim | Must not be claimed as available | Complete hash-pinned artifacts and independent replay |

SGP-owned rows are synchronized mirrors. SGP controls their definitions and statuses.

## Hard claim-boundary rule

A framework-level empirical performance, validation, superiority, or deployment-readiness claim SHALL NOT rest decisively on an empirical construct or model component below the maturity required by that claim. A normative prior or governance convention SHALL NOT be presented as an empirical finding.

Run-level conformance is distinct from framework-level empirical validation.

## PCC binding

For each materially used listed object, a Tier 2 or Tier 3 PCC SHOULD record:

- construct identifier;
- owner and version;
- status class;
- maturity token;
- role in the run;
- whether it controlled a gate, tie-break, protection, authority, or public claim;
- maximum claim applied;
- sensitivity or fallback used;
- registry hash reference.

## Audit flags

- `MATURITY_REGISTER_BLOCK_MISSING`: listed object materially used without the required PCC maturity block.
- `MATURITY_OVERCLAIM_INVALID`: stronger empirical or performance claim exceeds the listed maturity ceiling.
- `NORMATIVE_PRIOR_LAUNDERED_AS_EMPIRICAL`: normative prior or convention described as an empirical constant.
- `DESIGN_TARGET_AVAILABILITY_FALSE`: unavailable roadmap artifact described as released or operational.
