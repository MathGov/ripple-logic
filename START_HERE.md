# Start Here — Ripple_Logic v8.6

This file routes you to the right entry point depending on who you are
and what you need.

---

## I want to understand what Ripple_Logic is

Start with **[README.md](README.md)**. It explains the 7 × 7 welfare matrix,
the five-level lexicographic cascade, implementation tiers, stream binding,
and how the framework differs from standard governance approaches.

Then read the worked example:
**[`examples/ai_alignment_example.md`](examples/ai_alignment_example.md)**

This is a full Tier 2 illustrative run evaluating three options for frontier
AI deployment, showing the complete cascade with real numbers: stakeholder
instances, rights coverage sets and threshold checks, TRC scenario table and
CVaR computation, RLS with weights and cell-level impacts, UCI/HOI monitoring
flags, and a Five-Sentence Public Rationale.

---

## I want to implement the framework (Tier 1 or 2)

**Step 1.** Download the Foundation Paper:
[`releases/v8.6_2026_03_15/Ripple_Logic_v8.6_CANON_FINAL_RELEASE.docx`](releases/v8.6_2026_03_15/Ripple_Logic_v8.6_CANON_FINAL_RELEASE.docx)

**Step 2.** Read **Section 15** (Implementation Guidance and Tiers) and
**Appendix H** (PCC Template). These define the minimum obligations at
each tier and the structure of the required audit record.

**Step 3.** For Tier 2 calculation support, download the Ripple Aligners Sheet:
[`releases/v8.6_2026_03_15/Ripple_Aligners_Sheet_v2.2_CANON_FINAL_RELEASE.xlsx`](releases/v8.6_2026_03_15/Ripple_Aligners_Sheet_v2.2_CANON_FINAL_RELEASE.xlsx)

Note: the Aligners Sheet is configured for a two-option comparison.
Additional options require extension or sequential comparison using a
fresh run.

**Step 4.** Verify your downloaded files against the SHA-256 checksums:
[`releases/v8.6_2026_03_15/Ripple_Logic_Core_Package_FINAL_RELEASE_SHA256SUMS.txt`](releases/v8.6_2026_03_15/Ripple_Logic_Core_Package_FINAL_RELEASE_SHA256SUMS.txt)

---

## I want to use this for AI alignment or agent governance

**Step 1.** Read the Foundation Paper, focusing on:
- Section 7 — NCRC (Non-Compensatory Rights Constraint)
- Section 8 — TRC (Tail-Risk Constraint using CVaR)
- Section 9 — Containment
- Section 12 — SGP integration (moral status layer)
- Section 14.7 and Appendix N — Stewardship Layer

**Step 2.** Read the Agent System Specification:
[`releases/v8.6_2026_03_15/RippleLogic_Agent_System_v8.6_CANON_FINAL_RELEASE.docx`](releases/v8.6_2026_03_15/RippleLogic_Agent_System_v8.6_CANON_FINAL_RELEASE.docx)

**Step 3.** Read the worked AI example:
[`examples/ai_alignment_example.md`](examples/ai_alignment_example.md)

---

## I want to review or critique the framework academically

The Foundation Paper is the single canonical source. Cite it as:

McGaughran, J. (2026). Ripple_Logic Framework v8.6 [Specification]. MathGov Institute for Ethical Systems Design. Canonical filename: Ripple_Logic_v8.6_CANON_FINAL_RELEASE.docx SHA-256: 24741d46339073bb01331e7595e090bae38eadac1ab28e4a4909428d9a4b63b5 ORCID: 0009-0005-3324-7290


Key sections for critical review:
- **Section 0** — Specification contract, normative hierarchy, tier claims
- **Section 17** — Validation program, falsification criteria, empirical hypotheses
- **Appendix F** — Failure modes and anti-gaming controls
- **Appendix R** — Reference test vectors (normative; implementations must reproduce these)

---

## I want to check empirical and validation status

See **[`VALIDATION_STATUS.md`](VALIDATION_STATUS.md)** for the full phase
tracker, IRR commitment, and falsification criteria.

Summary: architecturally complete and Tier 1–2 ready. Tier 3 operational
readiness requires IRR evidence and empirical pilots (not yet complete).
Tier 4 claims are prohibited until a public ProofPack is independently
replayable.

---

## I want to contribute

See **[`CONTRIBUTING.md`](CONTRIBUTING.md)**.

The most valuable contributions right now are:

- **Independent implementation** of the Tier 1–3 algorithms from the spec
- **Pre-registered empirical pilots** using the Appendix J templates
- **IRR studies** on welfare-cell scoring and rights-floor evaluation
- **JSON Schema / PCC schema development** — the biggest tooling gap
- **Challenger review** of the worked examples and reference test vectors

---

## The five canonical documents

All five are in [`releases/v8.6_2026_03_15/`](releases/v8.6_2026_03_15/).

| Document | Version | Role |
|----------|---------|------|
| Ripple_Logic Foundation Paper | v8.6 | Single normative source of truth |
| Sentience Gradient Protocol (SGP) | v4.3 | Moral status layer; consumed via Appendix G binding interface |
| ripple.md Standard | v2.0 | Portable alignment contract, Decision Notes, feasibility gates |
| RippleLogic Agent System | v8.6 | Operational agent controls and stewardship instrumentation |
| Ripple Aligners Sheet | v2.2 | Tier 2 worked-run and local-scope calculation tool |

Verify all files against:
[`releases/v8.6_2026_03_15/Ripple_Logic_Core_Package_FINAL_RELEASE_SHA256SUMS.txt`](releases/v8.6_2026_03_15/Ripple_Logic_Core_Package_FINAL_RELEASE_SHA256SUMS.txt)

---

*Ripple_Logic v8.6 · ripplelogic.org · mathgov.org*
*github.com/MathGov/ripple-logic*