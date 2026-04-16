# RippleLogic

Canonical decision operating system for rights-constrained, ripple-aware ethical governance and intelligence alignment.

| Field | Value |
|---|---|
| Version | v9.5 |
| Status | Canonical core release (Tier 1–3), with a synchronized document/workbook set and integrity layer |
| License | CC BY-ND 4.0 (spec text) · MIT (code) · CC BY 4.0 (examples) |
| Canonical sites | ripplelogic.org · mathgov.org |
| Repository | github.com/MathGov/ripple-logic |
| Author | James McGaughran · ORCID: 0009-0005-3324-7290 |

## Latest Release

**v9.5 — Canonical Core Bundle (Tier 1–3)**  
Release tag: `v9.5`  
Release folder: `releases/v9.5_2026-04-16`

This release includes:

- RippleLogic v9.5 Canon
- Sentience Gradient Protocol (SGP) v4.6
- ripple.md Standard v2.0
- RippleLogic Agent System v9.0
- RippleLogic Aligners Sheet v2.3 (worked-run exemplar)
- ProofPack v0.3
- Release manifest
- SHA-256 manifest
- Bundle inventory

This is the current stable release line.

## What RippleLogic Is

RippleLogic is a general-purpose ethical operating system that evaluates decisions across nested stakeholder scopes while enforcing:

- **Non-compensatory rights floors** so rights violations cannot be traded away for aggregate benefit elsewhere
- **Catastrophic tail-risk control** using Conditional Value-at-Risk (CVaR) over a governed scenario library rather than expected value
- **Containment** so local gains may not degrade the coherence of containing union scopes beyond governed tolerance
- **Welfare ranking only among options that pass the admissibility gates**, scored across a 7 × 7 welfare matrix of union scopes × welfare dimensions
- **Structural diagnostics** through Union Coherence Index (UCI) and Hollowing-Out Index (HOI) for long-run integrity monitoring and tie-breaking

It is designed for governance and public policy analysis, AI alignment and safety evaluation, institutional and organizational decision-making, and other high-stakes environments requiring auditable, rights-respecting reasoning under uncertainty.

**Canonical naming:** RippleLogic is the canonical release-line name. MathGov remains the historical umbrella term for the broader lineage and ecosystem.

**Single source of truth:** The Foundation Canon (`RippleLogic_v9.5_Canon_FINAL.docx`) is the governing artifact for the v9.5 release line. If any companion artifact conflicts with the Canon, the Canon governs.

## Current Canonical Release

**Current release:** v9.5  
**Release type:** Canonical core release  
**Core bundle:** Tier 1–3 publication-ready core bundle

The v9.5 line contains the following synced core artifacts:

- `RippleLogic_v9.5_Canon_FINAL.docx`
- `SGP_v4.6_FINAL.docx`
- `ripple_md_Standard_v2.0_RELEASE_READY_FINAL.docx`
- `RippleLogic_Agent_System_v9.0_RELEASE_READY.docx`
- `RippleLogic_Aligners_Sheet_v2.3_RELEASE_READY_FINAL.xlsx`

The release package also includes:

- `RippleLogic_v9.5_ProofPack_v0.3.docx`
- `RippleLogic_v9.5_release_manifest_FINAL.yaml`
- `RippleLogic_v9.5_release_sha256_FINAL.txt`
- `RippleLogic_v9.5_bundle_inventory_FINAL.txt`

## The Core Decision Cascade

RippleLogic filters and ranks options in a fixed lexicographic order:

**NCRC → TRC → Containment → RLS → UCI / HOI**

- **NCRC** removes rights-violating options
- **TRC** removes options with unacceptable catastrophic tail risk
- **Containment** blocks local optimization that degrades containing scopes
- **RLS** ranks the remaining selectable options by weighted welfare improvement
- **UCI / HOI** provide structural diagnostics, tie-breaking support, and longitudinal monitoring

Later-stage gains cannot compensate for earlier-stage failure.

## The 7 × 7 Welfare Matrix

Every decision is evaluated across 49 cells, formed by 7 union scopes × 7 welfare dimensions.

### Union Scopes

| Code | Scope |
|---|---|
| U1 | Self |
| U2 | Household |
| U3 | Community |
| U4 | Organization |
| U5 | Polity |
| U6 | Humanity / CMIU |
| U7 | Biosphere |

### Welfare Dimensions

| Code | Dimension |
|---|---|
| D1 | Material |
| D2 | Health |
| D3 | Social |
| D4 | Knowledge |
| D5 | Agency |
| D6 | Meaning |
| D7 | Environment |

All normative computation is performed on the canonical `[-1, +1]` scale.

## Companion Artifacts

The Canon is the normative source of truth. The following companion artifacts extend or operationalize the v9.5 core line:

| Artifact | Version | Role |
|---|---|---|
| Sentience Gradient Protocol (SGP) | v4.6 | Sentience scoring and rights-of-protection interface consumed by RippleLogic |
| ripple.md Standard | v2.0 | Portable alignment contract and wrapper/interface standard |
| RippleLogic Agent System | v9.0 | Operational agent controls, evaluation harness expectations, stewardship, and deployment mode governance |
| RippleLogic Aligners Sheet | v2.3 | Worked-run and audit-ready workbook companion |

## Validation and Claim Status

RippleLogic v9.5 is release-ready as the core synced document/workbook bundle for the declared Tier 1–3 scope.

This means the v9.5 release line now provides:

- a synced canonical document stack
- a calculable and publication-clean workbook companion within its declared role
- release hashes and manifest surfaces suitable for GitHub and website publication
- a bounded release integrity layer through the ProofPack and metadata surfaces

This does **not** mean the system is fully empirically validated or that Tier 4 replay claims are open.

### Claim boundary

- **Core synced canon line:** ready
- **Tier 1–3 specification/use as a documented framework:** claimable within the stated boundaries of the Canon and companion documents
- **Tier 4 independent replay claim:** prohibited until validator/schema surfaces and any optional executable companion assets are separately published and pinned

## Scope of the Current Release

This repository currently provides:

- Tier 1–3 canonical framework and documentation
- worked-run exemplar support
- release-layer integrity metadata

This repository does **not** yet provide:

- a Tier 4 independently replayable validator system
- a full validator/schema/reference-calculator ecosystem
- a deployment evidence pack proving live Agent System conformance

The Aligners Sheet is included as a **worked-run exemplar companion**, not as the repository-level validator/schema surface.

## Repository Structure

```text
releases/
  v7.4.5_2026-01-25/
  v8.1_2026-02-14/
  v8.5.3_2026-02-20/
  v8.6_2026_03_15/
  v9.0_2026-03-24/
  v9.5_2026-04-16/
examples/
ripplelogic-proofpack-lite/
README.md
RELEASE_HISTORY.md
RELEASE_MANIFEST.json
RELEASE_POLICY.md
START_HERE.md
