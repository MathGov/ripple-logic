# MathGov v12.6 Publication Deployment Checklist

**Status:** non-normative release-engineering checklist. This file does not amend the RippleLogic Canon or any governing standard.

Use this checklist when publishing the current stabilized Core so every public doorway points to the same release identity.

- [ ] GitHub default branch identifies **MathGov Core v12.6 / SGP v8.5 / Agent System v12.5** and exact build `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3`.
- [ ] GitHub Release tag/title and attached ZIP match the exact build and published SHA-256.
- [ ] `ripplelogic.org` Core/current-version page identifies the same semantic versions and exact build.
- [ ] `mathgov.org`, if it presents a current release, identifies the same release or is clearly labelled historical/archive.
- [ ] `/start-here/` uses the current five-stage spine `RG -> RF/NCRC -> TRC -> CSV -> RLS`; UCI/HOI are not presented as a cascade stage.
- [ ] Download links resolve to the final ZIP, not a superseded build.
- [ ] Published SHA-256 matches the shipped ZIP bytes.
- [ ] Current public wording preserves the release claim boundary: specification/conformance readiness is not empirical validation, legal certification, physical safety, or deployment assurance.
- [ ] Superseded releases remain available only as clearly labelled historical/archive material.
- [ ] Book/article/current-version references are updated when they make an explicit version claim; historical citations remain unchanged.
- [ ] MHIOS is presented separately as **v0.8 candidate experimental implementation companion**, not as part of the Core 15.

Deployment completion should be recorded in the release notes or external publication log.
