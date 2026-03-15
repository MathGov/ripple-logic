# Ripple_Logic

**Canonical decision operating system for rights-constrained, ripple-aware
ethical governance**

| | |
|---|---|
| **Version** | v8.6 |
| **Status** | Architecturally complete — Tier 1–3 implementable now from the Foundation Paper — Tier 4 non-claimable until ProofPack is publicly replayable |
| **License** | CC BY 4.0 (text) · MIT (reference implementations and schemas) |
| **Canonical sites** | ripplelogic.org · mathgov.org |
| **Repository** | github.com/MathGov/ripple-logic |
| **Author** | James McGaughran · ORCID: 0009-0005-3324-7290 |

---

## What Ripple_Logic Is

Ripple_Logic is a general-purpose ethical operating system that evaluates
decisions across nested stakeholder scopes while enforcing:

- **Non-compensatory rights floors** — rights violations cannot be traded
  away for aggregate benefit elsewhere
- **Catastrophic tail-risk control** — using Conditional Value-at-Risk
  (CVaR) over a governed scenario library, not expected value
- **Containment** — local gains may not degrade the coherence of containing
  Union Scopes beyond governed tolerance
- **Welfare ranking** — only among options that pass the above gates,
  scored across a 7 × 7 welfare matrix of Union Scopes × Welfare Dimensions
- **Structural diagnostics** — Union Coherence Index (UCI) and
  Hollowing-Out Index (HOI) for long-run integrity monitoring and
  tie-breaking

It is designed for use in governance and public policy analysis, AI
alignment and safety evaluation, institutional and organizational
decision-making, and any high-stakes situation requiring auditable,
rights-respecting reasoning under uncertainty.

**Canonical name:** Ripple_Logic is the canonical name from v8.6 forward.
MathGov is the historical umbrella term for the broader lineage and
ecosystem and remains a valid narrative reference.

**Single source of truth:** The Foundation Paper
(`Ripple_Logic_v8.6_CANON_FINAL_RELEASE.docx`) is the single canonical
artifact for v8.6. In case of any conflict between this README and the
Foundation Paper, the Foundation Paper governs per Section 0.1.

---

## The 7 × 7 Welfare Matrix

Every decision is evaluated across **49 cells**:
**7 Union Scopes (rows) × 7 Welfare Dimensions (columns)**.

Impact instances from real stakeholders feed each cell. Union Scopes are
the stable aggregation rows. Rights-covered and catastrophe cells are
**non-maskable** — they cannot be excluded from admissibility evaluation
or welfare ranking regardless of scope or masking choices.

### Union Scopes (rows)

| Code | Scope | Timescale |
|------|-------|-----------|
| U1 | Self | Seconds to decades |
| U2 | Household | Days to decades |
| U3 | Community | Months to generations |
| U4 | Organization | Years to centuries |
| U5 | Polity | Decades to centuries |
| U6 | Humanity / CMIU | Generations to millennia |
| U7 | Biosphere | Centuries to epochs |

Canonical nesting chain: U1 ⊂ U2 ⊂ U3 ⊂ U4 ⊂ U5 ⊂ U6 ⊂ U7

### Welfare Dimensions (columns)

| Code | Dimension | What it measures |
|------|-----------|-----------------|
| D1 | Material | Resources, income, economic security |
| D2 | Health | Physical and mental wellbeing, safety |
| D3 | Social | Trust, belonging, relational integrity |
| D4 | Knowledge | Epistemic access, information quality, learning |
| D5 | Agency | Autonomy, freedom from coercion, self-determination |
| D6 | Meaning | Purpose, coherence, valued projects |
| D7 | Environment | Ecological and infrastructure integrity |

All welfare impacts are computed and compared on the canonical **[−1, +1]
scale** (baseline-zero: 0 means no change from baseline). A UI points
display (×100) is a non-normative presentation layer only — all gates and
RLS must be computed on the canonical scale.

---

## The Five-Level Lexicographic Cascade

Options are filtered in strict order. An option eliminated at any stage is
not scored at later stages. Later benefits **cannot** compensate for
earlier failures.

Copy
┌─────────────────────────────────────────────────────┐ │ NCRC Non-Compensatory Rights Constraint │ │ → eliminates rights-violating options │ └───────────────────────┬─────────────────────────────┘ │ admissible options only ▼ ┌─────────────────────────────────────────────────────┐ │ TRC Tail-Risk Constraint (CVaR) │ │ → eliminates options with unacceptable tail risk │ └───────────────────────┬─────────────────────────────┘ │ admissible options only ▼ ┌─────────────────────────────────────────────────────┐ │ Containment Structural Integrity Gate │ │ → eliminates options that degrade containing │ │ Union Scopes beyond governed tolerance │ └───────────────────────┬─────────────────────────────┘ │ selectable options only ▼ ┌─────────────────────────────────────────────────────┐ │ RLS Ripple Logic Score │ │ → ranks selectable options by weighted welfare │ │ improvement across all 49 cells │ └───────────────────────┬─────────────────────────────┘ │ top-ranked option ▼ ┌─────────────────────────────────────────────────────┐ │ UCI / HOI Structural Diagnostics │ │ → tie-breaking and long-run monitoring │ └───────────────────────┬─────────────────────────────┘ │ ▼ Selected option + PCC (audit record)


---

### Level 1 — NCRC: Non-Compensatory Rights Constraint

Eight canonical rights are checked across their coverage sets in the
welfare matrix. For rights-covered cells, the **worst-off subgroup**
impact is used — aggregate averages cannot mask harm to vulnerable groups.

Any option that drives the worst-off subgroup below a rights threshold is
**eliminated**, regardless of aggregate benefit elsewhere.

**Gate baseline rule:** Rights and catastrophe cells are evaluated against
a **floor-reference baseline** — what rights-safe conditions require — not
merely the status quo. An option that merely maintains an ongoing
rights-violating status quo does not pass NCRC.

| Right | Code | Threshold θ_r |
|-------|------|---------------|
| Life | LIFE | −0.90 |
| Bodily Integrity | BODY | −0.70 |
| Liberty | LBTY | −0.65 |
| Ecological Integrity | ECOL | −0.65 |
| Dignity | DIGN | −0.55 |
| Basic Needs | NEED | −0.50 |
| Due Process | PROC | −0.45 |
| Information | INFO | −0.40 |

---

### Level 2 — TRC: Tail-Risk Constraint

TRC bounds catastrophic exposure using **CVaR** (Conditional Value-at-Risk)
over a governed scenario library, evaluated across three base catastrophe
cells:

- **(U6 × D2)** — Humanity/CMIU Health: civilizational health viability
- **(U6 × D7)** — Humanity/CMIU Environment: civilization-scale habitability
- **(U7 × D7)** — Biosphere Environment: Earth-system integrity

Five mandatory tail categories must appear with per-category probability
≥ 0.02 each: pandemic/biological disruption, climate tipping cascade,
financial system collapse, major conflict escalation, and critical
infrastructure failure.

TRC uses the **Base stream** only (sentience multiplier s_k := 1).
Welfare-stream impacts must not be used for TRC.

---

### Level 3 — Containment

Containment prevents pathological local optimization. A sub-union scope
may not improve its own welfare by degrading the coherence or viability of
its containing Union Scopes beyond governed tolerance (default τ_c = −0.10
on the UCI scale).

Assessed via **ΔUCI** (prospective change in Union Coherence Index) for
containing scopes. At Tier 3, Containment Mode A is a **binding gate**,
not an advisory check.

---

### Level 4 — RLS: Ripple Logic Score

Among selectable options, RLS ranks by weighted welfare improvement across
the 49-cell matrix using the **Welfare stream**:


$$\text{RLS}(a) = \sum_{u}\sum_{d}\, w_u \times v_d \times m(u,d) \times I_{\text{prop,welfare}}(u,d,a)$$

Weights are governed by **Hybrid Democratic Weighting (HDW)** with
constitutional floor minimums that cannot be reduced to zero regardless of
democratic input. Rights-covered and catastrophe cells remain
**non-maskable** in RLS aggregation.

---

### Level 5 — UCI / HOI: Structural Diagnostics

**Union Coherence Index (UCI)** measures structural health of each Union
Scope across four components — Cohesion, Flow, Resilience, and Equity.
Used in Containment evaluation and RLS tie-breaking.

**Hollowing-Out Index (HOI)** is a monitoring diagnostic that detects
welfare-up / coherence-down drift over time. It feeds the **NCAR Reflect**
cycle and flags situations where apparent welfare gains are masking
structural erosion.

---

## Stream Binding

Two impact streams are maintained throughout every run:

| Stream | Sentience multiplier | Used by |
|--------|---------------------|---------|
| Base stream | s_k := 1 (fixed for all instances) | NCRC, TRC, Containment |
| Welfare stream | s_k from SGP interface (= 1 for all humans, Human Plateau Rule) | RLS only |

These must never be mixed. The Human Plateau Rule is non-overridable:
every human person has s_k := 1.0 regardless of any SGP scoring outcome.

---

## Auditability — PCC and NCAR

Every Tier 2–3 run produces a **Provenance and Compliance Certificate
(PCC)** — a structured, immutable record of all inputs, intermediate
computations, gate outcomes, weights, scenario tables, stakeholder
instances, redundancy handling declarations, sensitivity results, and
audit flags.

The PCC enables decisions to be reconstructed, challenged, and corrected.
It includes a **Five-Sentence Public Rationale (5SPR)** accessible to
affected stakeholders.

All runs are embedded in the **NCAR learning loop**:

Notice → Choose → Act → Reflect


NCAR Reflect feeds observed outcomes back into kernels, scenario
libraries, and weight governance through versioned, auditable updates.

---

## Implementation Tiers

Tier 1–3 are **implementable and claimable now** from the Foundation Paper
and its appendices. Tier 4 is a design target only.

| Requirement | Tier 1 (Heuristic) | Tier 2 (Core) | Tier 3 (Auditable) |
|-------------|-------------------|---------------|-------------------|
| NCRC | Heuristic screen | Required | Required + subgroup disaggregation |
| TRC | Optional qualitative | Required when catastrophe relevance plausible (≥ 5 scenarios) | Required (≥ 20 scenarios) |
| Containment Mode A | Optional | Recommended | Required — binding gate |
| RLS | Optional | Required | Required |
| Uncertainty / discrimination | Optional | Required (active cells) | Required |
| Sensitivity analysis | Optional | Recommended | Required |
| PCC | Optional | Required (basic) | Required (full) |
| Stakeholder instances (SCI) | Optional | SCI ≥ 1 required | SCI ≥ 2 required |
| Stewardship | Optional | Required if Stw_req = 1 | Required (Stw_req = 1 by default) |

**Tier 4** — deterministic hash-bound replayability via ProofPack —
is a design target. Tier 4 compliance claims are **prohibited** until a
public ProofPack is independently replayable.

---

## Worked Example

[`examples/ai_alignment_example.md`](examples/ai_alignment_example.md)
presents a full Tier 2 illustrative run evaluating three options for
frontier AI model deployment by a national government.

It shows the complete cascade with:

- stakeholder instance mapping to Union Scopes
- rights coverage sets, threshold checks, and floor-reference baseline
- TRC scenario table (8 scenarios across all 5 mandatory categories),
  CVaR computation, and the "unioning" redesign that turns B into B+
- RLS calculation with declared weights, cell-level impacts, and
  decisiveness test (Gap ≈ 4.5 σ)
- ΔUCI / HOI monitoring flags at U3, U6, and U7
- Five-Sentence Public Rationale (5SPR)

---

## Repository Structure

Ripple_Logic_v8.6_CANON_FINAL_RELEASE.docx ← Single canonical Foundation Paper examples/ ai_alignment_example.md ← Tier 2 illustrative run releases/ ripplelogic-proofpack-lite/ README.md START_HERE.md VALIDATION_STATUS.md RELEASE_HISTORY.md RELEASE_POLICY.md SECURITY.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE CITATION.cff


---

## Companion Artifacts

The Foundation Paper is the single normative source of truth. The
following companion artifacts extend or operationalize it. In case of
conflict, the Foundation Paper governs.

| Artifact | Version | Role |
|----------|---------|------|
| Sentience Gradient Protocol (SGP) | v4.3 | Sentience scoring and rights-of-protection gating; consumed by Ripple_Logic via Appendix G binding interface |
| ripple.md Standard | v2.0 | Portable alignment contract, Decision Notes, feasibility gates, interface between ripple.md and Ripple_Logic cascade |
| RippleLogic Agent System | v8.6 | Operational agent controls, verification obligations, and stewardship instrumentation |
| Ripple Aligners Sheet | v2.2 | Tier 2 worked-run and local-scope tool; configured for two-option comparison |

---

## Validation Status

Ripple_Logic v8.6 is **architecturally complete**. Tiers 1–3 are
implementable and claimable now from the Foundation Paper.

| Phase | Status |
|-------|--------|
| Foundation Paper — formal specification complete | ✅ Complete |
| Tier 1–2 illustrative runs and reference test vectors (Appendix P, R) | ✅ Complete |
| Inter-rater reliability study (required before Tier 3 operational-readiness claim) | 🔲 Planned |
| Empirical validation — Phase 1: formal verification and implementation testing | 🔲 Planned |
| Empirical validation — Phase 2: measurement validation | 🔲 Planned |
| Empirical validation — Phase 3: controlled pilots | 🔲 Planned |
| ProofPack publication (required for Tier 4 claims) | 🔲 Not yet published — Tier 4 claims prohibited |

---

## Relationship to MathGov

MathGov is the historical umbrella term for the lineage and ecosystem from
which Ripple_Logic emerged. It remains a valid narrative reference in
lineage documents, affiliated publications, and prior PCCs.

From v8.6 forward, **Ripple_Logic** is the canonical name of the
specification. Union-Based Reality (UBR) and Union-Based Ethics (UBE) —
the ontological and normative foundations of the system — are defined
within the Foundation Paper itself, not in a separate document above it.

---

## Citation

McGaughran, J. (2026). Ripple_Logic Framework v8.6 [Specification]. MathGov Institute for Ethical Systems Design. Canonical filename: Ripple_Logic_v8.6_CANON_FINAL_RELEASE.docx ORCID: 0009-0005-3324-7290 Canonical sites: ripplelogic.org · mathgov.org Repository: github.com/MathGov/ripple-logic License: CC BY 4.0


Pin downstream work to the canonical filename + SHA-256 hash from the
release manifest, per Section 0.6 of the Foundation Paper. Do not cite
variant copies, forks, or regenerated versions — only the byte-identical
canonical artifact is authoritative.

---

## License

The text of the Foundation Paper is released under
**Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Reference implementations, schemas, and test fixtures are released under
the **MIT License**.

See `LICENSE` for details.

---

## Author

**James McGaughran**
Creator and system architect of Ripple_Logic and the MathGov lineage.
ORCID: 0009-0005-3324-7290

---

*Ripple_Logic v8.6 · ripplelogic.org · mathgov.org*
*github.com/MathGov/ripple-logic*