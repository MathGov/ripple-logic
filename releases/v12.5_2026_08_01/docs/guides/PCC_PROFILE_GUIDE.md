# PCC Profile Guide

**Status:** companion operational guide. Canon controls if conflict occurs.

## Purpose

The Provenance and Compliance Certificate makes decisions auditable, but a single full-burden record for every context can reduce adoption. PCC profiles preserve auditability while scaling effort to stakes.

## PCC profiles

| Profile    | Use                                                        | Minimum posture                                                                                    |
| ---------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| PCC-Lite   | Tier 1 training, low-stakes reflection, classroom examples | short decision note, declared cascade status, visible limitations                                  |
| PCC-Core   | Tier 2 ordinary consequential decisions                    | RG summary, gate outcomes, rationale, uncertainty, basic audit flags                               |
| PCC-Audit  | Tier 3 high-stakes or public-institutional decisions       | full reconstructable record, evidence trace, scenarios, subgroup handling, challengers, versioning |
| PCC-Agent  | agentic, automated, delegated, or high-autonomy workflows  | PCC-Audit plus mode, operator, NEI/firewall, control and rollback records                          |
| PCC-Public | public release, policy, website, or claims surface         | claim boundary, source hierarchy, non-claims, review status, and public language controls          |

## Profile selection rule

A lower PCC profile is not allowed if stakes, automation, rights exposure, catastrophe relevance, public claim-making, or affected-party burden require a higher profile.

## Escalation triggers

Escalate PCC profile when:

- any RF/NCRC cell is plausibly affected;
- catastrophe relevance is plausible;
- physical or causal execution can create non-trivial harm;
- CSV burden is material;
- AI/agentic execution is involved;
- public claims are made;
- affected parties cannot easily contest;
- decision owner has conflict of interest;
- repeated low-stakes decisions accumulate systemic effect.

## Physical/Causal Admissibility Evidence add-on

When the PC-AEP trigger holds, PCC-Core SHOULD include a compact profile and PCC-Audit or PCC-Agent MUST include a reconstructable profile. Required fields: physical_or_causal_model_used; validity_domain; boundary_conditions; uncertainty_range; failure_modes; reversibility_or_irreversibility_boundary; verification_simulation_empirical_test_or_expert_warrant; monitoring_and_shutoff_path; residual_unknowns; required_claim_action.

This add-on is not a sixth gate. It strengthens RG and CSV by making physical or causal evidence visible before execution.

## Plain-language rule

Small choices need a clear note. High-stakes choices need a record that another competent person can replay.
