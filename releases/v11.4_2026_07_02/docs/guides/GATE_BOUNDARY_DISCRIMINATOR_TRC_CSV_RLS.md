# Gate Boundary Discriminator: TRC, CSV, and RLS

**Status:** companion hardening guide for MathGov Core Release 2026.09 v11.4. Canon controls if conflict occurs.

## Purpose

The RippleLogic cascade is intentionally ordered:

**RG -> RF -> TRC -> CSV -> RLS**

This guide prevents a common implementation error: treating Tail-Risk Constraint, Containment and Structural Viability, and RippleLogic Score as overlapping welfare buckets. They are not the same operation.

## Boundary rule

| Layer | Primary question | Failure type | Selection consequence |
|---|---|---|---|
| TRC | Could this option expose the decision surface to catastrophic, irreversible, ruinous, or lock-in tail loss? | Tail exposure beyond the declared catastrophe corridor. | Option is not selectable in normal mode. |
| CSV | Can this option deliver its claimed good without hollowing, overloading, externalizing, or breaking its containing systems or execution substrate? | Structural non-viability, uncontained burden, hidden dependency, hollowing, or execution contradiction. | Option is not selectable as specified, may require controls or redesign. |
| RLS | Among options that already survived RG, RF/NCRC, TRC, and CSV, which has the best residual welfare profile? | Residual welfare tradeoff among selectable options. | Ranks options only after prior gates clear. |

## Double-materiality rule

Some harms are both catastrophic and structurally degrading. Example: an AI infrastructure path that creates governance lock-in and also hollows public accountability.

When a harm is double-material:

1. evaluate it in TRC if it plausibly affects the tail-risk scenario set;
2. evaluate it in CSV if it affects containing-system viability, dependency, execution feasibility, or structural integrity;
3. record the relationship in the PCC;
4. do not double-count the same effect-token as a residual welfare cost in RLS unless the residual effect remains after gate treatment.

## Routing tests

| Ask this | Route |
|---|---|
| Is the issue a worst-tail catastrophe or ruin path? | TRC |
| Is the issue a host-system hollowing, execution, dependency, capacity, legitimacy, or containment failure? | CSV |
| Is the issue an ordinary bounded cost or benefit after gates clear? | RLS |
| Is the issue insufficiently evidenced for the claim being made? | RG |
| Is the issue a protected rights-floor violation? | RF/NCRC |

## Non-collapse rule

TRC is not CSV. CSV is not RLS. RLS is not a rescue layer. If a decision-maker is tempted to say, "the score is good enough to compensate for the tail exposure or structural failure," the run has violated the cascade.

## Implementation note

A high-quality run SHOULD include a short gate-routing paragraph before TRC/CSV/RLS calculations:

> Gate-routing statement: The following harms are routed to TRC because they represent modeled tail exposure. The following harms are routed to CSV because they affect containment or structural viability. The following residual harms remain visible in RLS because they are bounded, controlled, and not gate-failing.
