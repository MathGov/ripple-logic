# Physical Admissibility and Execution Boundary

Release: MathGov Core Release 2026.09 v12.6 / SGP v8.5 - Configuration-Bound Assurance Public Research Source Release

This guide states the v12.0 boundary for consequence-bearing physical execution.

## Core rule

Governance permission is not physical admissibility. Certification, approval, monitoring, documentation, conformity, and authority can determine whether an action may proceed under a governance regime, but they do not by themselves demonstrate that the action can safely exist in physical reality.

For autonomous robots, vehicles, industrial control, medical robotics, critical infrastructure, energy systems, aerospace, manufacturing, security systems, weapons systems, environmental interventions, and other cyber-physical systems, MathGov MUST NOT treat `ALLOW`, `SELECTABLE`, `CSV_PASS`, or any governance approval as a physical-safety proof.

## What MathGov can and cannot do

MathGov can require, structure, audit, and refuse claims based on physical or causal admissibility evidence. MathGov does not itself compute physics, certify engineering safety, validate medical treatment, replace formal methods, or generate domain-specific physical proof.

## Computational-source boundary

For physical or causal execution, the record should distinguish the source that generated the candidate from the source that warrants admissibility. Candidate-generation sources may include a model, planner, optimizer, simulator, controller, human procedure, application, or orchestration layer. Admissibility-warrant sources must come from a domain-appropriate method. Candidate generation, filtering, monitoring, policy routing, and approval are not physical-safety evidence by themselves.

Therefore, a MathGov run may support physical execution only when the run includes a declared external warrant appropriate to the domain: formal verification, validated simulation, empirical test, standards-based safety case, certified controller envelope, qualified engineering review, clinical warrant, regulator-recognized method, or another explicitly named objective method.

## Consequence-bearing execution rule

For any material physical or causal execution claim:

1. The Physical/Causal Admissibility Evidence Profile (PC-AEP) must be completed.
2. The evidence source must be named and bounded by validity domain.
3. Failure modes and irreversibility boundaries must be disclosed.
4. Monitoring, shutoff, rollback, sandboxing, or containment must be described where applicable.
5. If evidence is missing or weak, the claim action must be narrow, control, redesign, escalate, or refuse.
6. RLS must not rank an execution option as selectable when physical admissibility is unknown, unsupported, or outside validity domain.

## Language rule

Use `governance permission` when the decision only shows authority or process approval.

Use `physical admissibility supported within declared validity domain` only when a domain-appropriate external method supports the claim.

Use `physical admissibility not established` when MathGov has process approval but lacks domain evidence.

## Relationship to the cascade

The public cascade remains:

`RG -> RF -> TRC -> CSV -> RLS`

PC-AEP is not a sixth gate. It strengthens Reality Grounding and CSV. If PC-AEP discovers catastrophic or irreversible harm not yet represented in TRC, TRC must reopen before RLS.


## Reality Grounding as verifiable admissibility

For consequence-bearing domains, especially life-critical systems, weapons, nuclear command and control, planetary-scale cognition, critical infrastructure, medical systems, ecological interventions, and cyber-physical execution, Reality Grounding must do more than collect plausible facts. It must establish whether the claim is testable or otherwise warranted, bounded to a validity domain, auditable, correctable, and refusible.

The operational rule is: ground the claim, protect the right, bound the ruin, verify the system, make exit and correction real, and rank only what survives qualification. If the evidence surface cannot support that claim posture, MathGov must narrow, escalate, mark non-decisive or exploratory, or refuse the stronger claim.
