# RippleLogic (MathGov)

RippleLogic is a safety-first decision framework for humans and AI systems making high-stakes choices. It works like a governance seatbelt: it rejects any option that violates basic rights, then rules out options with unacceptable catastrophic tail risk, then protects the integrity of the systems that must keep functioning, and only then ranks the remaining options by net welfare impact across stakeholders.

Stakeholders are modeled as seven nested unions (from Self through Biosphere), and impacts are recorded in a transparent 49-cell matrix.

RippleLogic is built for verification, not belief. You do not have to trust it. You can audit how it reached its conclusion. Claims are limited to Tier 1–3 evaluation, outputs are reconstructible by independent reviewers, and explicit falsification criteria define what evidence would show the framework fails.

The canonical v8.1 specification and companion artifacts are published for open review and pilot testing at ripplelogic.org.
------------------------------------------------------------------------

## Current Canon Release

**RippleLogic v8.1 (2026-02-14)** is the current canonical specification
set.

Start here: - `releases/v8.1_2026-02-14/`

This release folder contains: - Core specification (Ripple_Logic_v8.1) -
Sentience Gradient Protocol (SGP v4.2.3) - Agent System specification -
Ripple Aligners Tier-2 worked exemplar - ProofPack skeleton - SHA256
integrity file - Full release bundle (optional)

------------------------------------------------------------------------

## What RippleLogic Claims (and What It Does Not)

### Tier Claims

RippleLogic supports Tier 1--3 usage and evaluation based on released
artifacts and worked examples.

Tier 4 is a design target only.\
No Tier-4 determinism or guaranteed alignment claims are made in this
repository.

### Core Guarantee Boundary

RippleLogic is designed to: - Protect non-compensable rights floors -
Bound catastrophic tail-risk - Make tradeoffs explicit and auditable
across unions

RippleLogic does not claim: - omniscience - perfect prediction - moral
infallibility - unconstrained optimization

------------------------------------------------------------------------

## Conceptual Overview

RippleLogic evaluates decisions using a rights-first lexicographic
cascade:

1.  NCRC (Non-Compensatory Rights Constraint)\
2.  TRC (Tail-Risk Constraint)\
3.  Containment (prevent runaway propagation of harm)\
4.  RLS (Ripple Logic Score across unions and welfare dimensions)\
5.  UCI/HOI (uncertainty and horizon-impact handling)

RippleLogic operates across nested operational unions and structured
welfare dimensions, implemented in exemplar form in the Ripple Aligners
sheet.

------------------------------------------------------------------------

## Repository Structure

All publishable canonical artifacts are stored under versioned release
folders:

releases/ v7.4.5_2026-01-25/ v8.1_2026-02-14/

Each release folder is: - complete - auditable - versioned and
date-stamped

------------------------------------------------------------------------

## Integrity Verification

Each release includes a SHA256SUMS file for verifying artifact
integrity.

Example (macOS/Linux): sha256sum -c SHA256SUMS_file.txt

Windows (PowerShell): Get-FileHash .`\filename`{=tex}.ext -Algorithm
SHA256

------------------------------------------------------------------------

## License

See LICENSE.

------------------------------------------------------------------------

## Provenance

RippleLogic / MathGov originates from a vertically stacked provenance
chain:

James McGaughran (originator, system architect, accountability) →\
Digital intelligence tools (synthesis and amplification instruments) →\
Humanity (knowledge substrate) →\
Lived reality and constraints (empirical pressure and training signal)

------------------------------------------------------------------------

## Canonical Links

-   ripplelogic.org\
-   mathgov.org\
-   GitHub: MathGov/ripple-logic
