# **Physical/Causal Admissibility Evidence Profile v2.3**

## **v2.3 Current Release Integration**

**Release: MathGov Core Release 2026.09 v12.6 / SGP v8.5 - Independent Open-Source Qualification-Continuity Release**

**Exact current companion pins:** Canon v12.6; SGP v8.5; ripple.md v5.5; Agent System v12.5; CSV v2.4; Cascade v2.6; Reproducibility v1.4; WDBIP v1.6; RLS Validation v2.6; Primer v4.4; Public Introduction v12.6; PC-AEP/MFDI/Source-Coupling v2.3; Aligners Sheet v5.6.

| **Integrity surface** | **Current requirement**                                                                                                                                | **Claim boundary**                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| External warrant      | Consequence-bearing actions identify a domain-appropriate engineering, clinical, scientific, regulatory, or formal warrant within its validity domain. | MathGov does not generate the missing domain proof. |
| Source separation     | Candidate generation, orchestration, guardrails, monitoring, and authorization are distinct from physical-admissibility evidence.                      | Generated or approved is not physically safe.       |
| Claim action          | Residual unknowns can force narrowing, controls, testing, redesign, escalation, delay, or refusal.                                                     | A profile is not deployment certification.          |

## **v2.2 Configuration-Bound Physical/Causal Evidence Extension**

A PC-AEP claim is valid only for the declared configuration and operating envelope. The minimum high-stakes record now includes hardware and software versions, model or policy version, parameters, sensors, actuators, tools, permissions, data sources, environment, active controls, authority state, validation version, timestamp, and configuration identifier or hash where feasible.

PC-AEP separately records current-state validity, transition admissibility, and resulting-state viability. Process success is partial evidence: it does not by itself establish the complete capability envelope, causal explanation, safety boundary, degradation boundary, or performance under a materially different configuration.

Compilation, synthesis, simulation, or hardware implementation establishes realizability of the represented architecture at that milestone only. Domain validity and physical safety require independent measurement, boundary testing, failure-mode analysis, and configuration-matched evidence.

Source-boundary rule: If this compact profile conflicts with the RippleLogic Canon, the Canon controls.

## **Purpose**

The Physical/Causal Admissibility Evidence Profile, abbreviated PC-AEP, is a compact evidence profile inside Reality Grounding and CSV. It prevents a RippleLogic run from treating a computed, generated, simulated, approved, certified, monitored, or compliance-accepted action as physically or causally admissible by default.

It is not a sixth gate. It does not alter the public cascade:

`RG -> RF -> TRC -> CSV -> RLS`

It also does not make MathGov a physics engine, control-system verifier, medical protocol, legal certification, deployment certification, or formal proof system. It asks whether the action has enough declared physical or causal warrant for the claim being made.

Formal-conformance boundary. Formal verification can establish that an implementation satisfies a declared specification under stated assumptions. It does not by itself establish that the specification accurately represents the physical or causal regime. When formal verification supports a physical claim, the profile MUST also record the specification, assumptions, validity domain, boundary conditions, and the separate evidence that connects the specification to the relevant reality surface.

Determinism boundary. PC-AEP does not require every admissibility warrant to be deterministic. The warrant must be strong enough for the consequence class and may combine formal verification, probabilistic risk analysis, empirical testing, validated simulation, standards-based safety cases, redundancy, bounded operating envelopes, monitoring, fail-safe behavior, and qualified residual-risk authorization. Deterministic conformance to an inadequate specification is insufficient; probabilistic evidence is admissible when uncertainty, tails, dependencies, limits, and refusal conditions are explicit.

## **Trigger**

PC-AEP is REQUIRED for Tier 3 runs and high-stakes Tier 2 runs when a candidate action materially affects bodily safety, medical treatment, robotics, vehicles, infrastructure, industrial systems, energy systems, environmental intervention, weapons or security systems, autonomous execution, cyber-physical operations, irreversible resource commitment, or any causal pathway where execution can create non-trivial physical, biological, ecological, or operational harm.

It is RECOMMENDED for ordinary Tier 2 runs when physical or causal uncertainty could change RF/NCRC, TRC, CSV, authority, or public claim strength.

## **Required fields**

| **Field**                                                  | **Required content**                                                                                                                                                                                                                                            |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `candidate_generation_source`                              | The model, optimizer, planner, simulator, controller, human procedure, dataset, or orchestration layer that produced the candidate state or action.                                                                                                             |
| `physical_or_causal_model_used`                            | The model, theory, mechanism, safety case, expert method, or domain analysis relied on.                                                                                                                                                                         |
| `validity_domain`                                          | The conditions, scale, population, environment, load, context, time horizon, and operating range in which the model or warrant is claimed to hold.                                                                                                              |
| `boundary_conditions`                                      | Initial, environmental, operational, legal, resource, dependency, and interface conditions that bound the claim.                                                                                                                                                |
| `uncertainty_range`                                        | Quantitative or qualitative uncertainty, confidence limits, error range, sensitivity range, or evidence-status limitation.                                                                                                                                      |
| `failure_modes`                                            | Known plausible ways the candidate can fail, degrade, harm, drift, destabilize, or become invalid.                                                                                                                                                              |
| `reversibility_or_irreversibility_boundary`                | What can be undone, stopped, repaired, rolled back, compensated, or not restored after execution.                                                                                                                                                               |
| `verification_simulation_empirical_test_or_expert_warrant` | Formal verification, simulation, empirical test, field evidence, expert review, standards-based warrant, or explicit statement that no adequate warrant exists. When formal verification supports a physical claim, record the verified specification, assumptions, and separate specification-to-reality evidence. |
| `admissibility_warrant_source`                             | The qualified domain method, verification process, test regime, standards-based safety case, or evidence source that evaluates admissibility. Institutional permission or execution authority is recorded separately and cannot serve as the warrant by itself. |
| `monitoring_and_shutoff_path`                              | How the action will be observed, interrupted, rolled back, sandboxed, contained, or stopped if assumptions fail.                                                                                                                                                |
| `residual_unknowns`                                        | Material unknowns that remain after the evidence review.                                                                                                                                                                                                        |
| `required_claim_action`                                    | One of proceed, narrow, control, redesign, escalate, or refuse.                                                                                                                                                                                                 |

## **Status values**

- `PCAE_SUPPORTED`: evidence is sufficient for the declared claim boundary.
- `PCAE_ASSUMPTION_BOUND`: action depends on assumptions that must be visible and rechecked.
- `PCAE_PARTIAL`: evidence supports only a narrower or controlled claim.
- `PCAE_CONTESTED`: relevant data, experts, stakeholders, or reviewers materially dispute the admissibility account.
- `PCAE_UNKNOWN`: evidence is insufficient to support the requested claim.
- `PCAE_VERIFICATION_REQUIRED`: stronger formal, empirical, simulation, or expert warrant is required before the stronger claim can proceed.
- `PCAE_CONTROL_REQUIRED`: binding controls, monitoring, shutoff, rollback, or containment are required for selectability.
- `PCAE_REDESIGN_REQUIRED`: the candidate is not selectable as specified but may be reformulated.
- `PCAE_REFUSE_OR_BLOCK`: the action or claim must be refused or blocked under the declared evidence.

## **Claim actions**

Proceed means the profile supports the declared claim boundary and all other cascade requirements must still pass. Narrow means reduce the claim, scope, action, environment, population, duration, or authority. Control means add binding safeguards as part of the option. Redesign means the candidate is not selectable as specified. Escalate means obtain domain review or stronger evidence. Refuse means the requested claim or execution is not admissible.

## **Relationship to Reality Grounding**

Reality Grounding records the reality surface, evidence trace, unknowns, transition boundary, consequence pathways, and claim boundary. PC-AEP is linked to Reality Grounding when the claimed action depends on physical or causal constraints. It strengthens claim discipline by forcing the run to state the candidate-generation source, model, domain, limits, uncertainty, failure modes, reversibility, warrant, monitoring/shutoff path, residual unknowns, and claim action.

## **Computational-source boundary**

PC-AEP separates two questions that are often collapsed: what generated the candidate action, and what establishes that the candidate is physically or causally admissible. The candidate-generation source may be a model, planner, optimizer, simulator, controller, human procedure, agent workflow, or orchestration layer. The admissibility warrant must be a domain-appropriate evidence surface. A candidate generator may propose an action, but it does not become the proof of admissibility merely because it generated the action. If the candidate-generation source and the admissibility-warrant source are the same system, the run MUST disclose why that is not circular, what independent checks or validity-domain limits apply, and what refusal condition prevents self-confirming execution.

## **Relationship to CSV**

CSV consumes PC-AEP when structural viability depends on physical or causal adequacy, dependency closure, resource closure, operational capacity, reversibility, monitoring adequacy, containment, authority, or host-system integrity.

A weak PC-AEP does not automatically fail every option, but it prevents strong selectability, conformance, deployment, safety, reliability, or alignment claims until the weakness is resolved, controlled, narrowed, escalated, redesigned, or refused.

## **Relationship to TRC**

If PC-AEP reveals a catastrophic, irreversible, lock-in, ruin-path, or severe-harm scenario not represented in TRC, the run MUST reopen TRC before RLS. CSV may discover TRC-relevant material, but it does not absorb or replace TRC.

## **Plain-language rule**

Before MathGov allows action in the physical or causal world, it asks what model of reality is being used, where that model stops, what could fail, whether harm is reversible, what evidence or expert warrant supports the action, how the action will be monitored or stopped, what remains unknown, and whether the right answer is proceed, narrow, control, redesign, escalate, or refuse.

## **Methodological integrity linkage**

PC-AEP evidence MUST state the claim type, model dependency, validity-domain limit, alternative-explanation status, falsification or revision trigger, and re-derivation scope where material. If physical or causal evidence fails, a run MUST NOT preserve the same safety, reliability, deployment, or admissibility claim through silent model tuning. It must version the change and rerun the affected chain.

## **Physical execution boundary**

For consequence-bearing physical systems, MathGov distinguishes governance permission from physical admissibility. `ALLOW`, `SELECTABLE`, `CSV_PASS`, certification, conformity, documentation, monitoring, or authority approval MUST NOT be read as physical-safety proof. They mean only that the governance record supports the declared claim after the required evidence has been reviewed. **Material-unknown action rule.** If the validity domain, safe operating envelope, or failure boundary is materially unknown, a governance body may authorize only explicitly bounded testing, sandboxing, containment, monitoring, or evidence collection whose own risk posture is qualified. It MUST NOT convert the unknown into a safe or ordinarily executable state, and operator acceptance cannot waive third-party rights or ruin constraints.

If a candidate action affects a physical system, PC-AEP must state where admissibility comes from: formal verification, validated simulation, empirical testing, standards-based safety case, certified controller envelope, qualified engineering or clinical warrant, regulator-recognized method, or another objective domain method. If that source is absent, contested, outside validity domain, or insufficient, the required claim action cannot be ordinary proceed. It must be narrow, control, redesign, escalate, or refuse.

## **Physical execution claim ladder**

| **Claim posture**                        | **Meaning**                                                                                                   | **Required treatment**                                                                  |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `PHYSICAL_ADMISSIBILITY_SUPPORTED`       | External domain evidence supports the declared action inside the stated validity domain.                      | May proceed only if RG, RF/NCRC, TRC, CSV, authority, and audit requirements also pass. |
| `GOVERNANCE_PERMISSION_ONLY`             | Authority or procedure permits the action, but physical admissibility has not been independently established. | Do not claim physical safety; narrow, control, escalate, or refuse.                     |
| `PHYSICAL_ADMISSIBILITY_NOT_ESTABLISHED` | The evidence source is missing, weak, out of domain, or unable to answer the execution question.              | Block strong execution claims; redesign, escalate, or refuse.                           |
| `PHYSICAL_ADMISSIBILITY_CONTRAINDICATED` | Evidence indicates instability, unsafe operation, irreversible harm, or unacceptable failure mode.            | Refuse or block; reopen TRC if catastrophic or irreversible risk is material.           |

Plain-language boundary: governance decides whether a decision is permitted; domain evidence determines whether the physical action is admissible within a declared validity domain. MathGov can require and audit that evidence. It does not manufacture the evidence.

## **Placement in the two-phase method**

PC-AEP supports Phase 1 qualification. It can strengthen, narrow, control, redesign, escalate, or refuse a physical-execution claim before RLS ranking. It does not add points to RLS and does not allow a high RLS score to compensate for missing physical or causal admissibility evidence.

## **Domain examples of admissibility warrant**

| **Domain**                               | **Example admissibility warrant**                                                                                                           | **Boundary**                                                                                         |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Robotics or autonomous mobility          | Certified controller envelope, simulation under declared conditions, field test evidence, and independent safety review.                    | Only supports the declared environment, payload, weather, sensor, and control limits.                |
| Medical or health action                 | Clinical protocol, licensed clinician review, trial evidence, or approved standard of care.                                                 | Does not generalize beyond the population, indication, contraindications, and care setting reviewed. |
| Infrastructure or engineering            | Engineering safety case, code compliance, load/traffic model, inspection record, and qualified engineer signoff.                            | Does not prove safety outside the design envelope or after material condition changes.               |
| Cyber-physical or security system        | Threat model, red-team results, rollback plan, access-control review, and monitored deployment envelope.                                    | Does not authorize unbounded persistence, privilege escalation, or uncontrolled downstream action.   |
| Ecological or environmental intervention | Environmental impact assessment, domain expert panel, monitoring plan, and reversibility/mitigation assessment.                             | Does not support irreversible action when residual unknowns remain gate-material.                    |
| Military, weapons, or command context    | Legal review, rules-of-engagement authority, human-command accountability, system test evidence, fail-safe review, and escalation controls. | Does not delegate life-taking or nuclear launch authority to an algorithmic process.                 |
