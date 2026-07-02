# Subgroup Discovery and Worst-Affected Groups Guide

**Status:** companion hardening guide for RF/NCRC, RLS, and PCC practice. Canon controls if conflict occurs.

## Purpose

Worst-off subgroup semantics prevent averages from hiding protected harms. This guide strengthens subgroup discovery without requiring unsafe or unnecessary sensitive-data collection.

## Discovery rule

A run SHOULD ask not only "who is affected?" but also "who could be affected worst, indirectly, invisibly, or with least ability to contest?"

## Minimum subgroup discovery steps

1. **Map exposure pathways.** Identify how the option could affect people or systems through access, enforcement, information, environment, labor, cost, coercion, infrastructure, or dependency.
2. **Identify likely vulnerability classes.** Consider age, disability, dependency, poverty, language, geography, legal status, digital access, caregiver status, minority exposure, occupational exposure, ecological dependency, and other context-specific factors.
3. **Check intersectional exposure.** Where lawful and ethical, examine whether combined conditions create worse exposure than any single category alone.
4. **Avoid unnecessary sensitive data.** If direct protected-attribute data collection is unsafe or unlawful, use pathway analysis, proxy-risk statements, consultation, or conservative bounds.
5. **Invite challenge.** Tier 3 and public Tier 2 runs SHOULD include a missing-subgroup challenge opportunity.
6. **Record limitations.** Unknown subgroup exposure is not zero. Record it as a limitation, assumption-bound estimate, or escalation trigger.

## Worst-affected-group record

| Field | Required content |
|---|---|
| subgroup_label | human-readable group or exposure pathway |
| basis_for_identification | data, consultation, prior case, law, expert judgment, challenger claim, or pathway inference |
| affected_rights | rights potentially implicated |
| affected_cells | RLS/RF cells plausibly affected |
| evidence_status | grounded, estimated, assumption-bound, unknown, contested |
| worst-case concern | why this subgroup may experience worse impact |
| mitigation or redesign | action taken before scoring or selection |
| residual uncertainty | what remains unknown |

## No-erasure rule

If a subgroup is plausibly rights-relevant but evidence is incomplete, the run must not average the group away. It should narrow the claim, use a conservative rights bound, collect evidence, escalate, or refuse the stronger selection claim.

## Subgroup omission flag

Use a PCC flag when any of the following occurs:

- credible subgroup was identified after initial scoring;
- subgroup data were missing for a rights-covered cell;
- subgroup exposure could not be mapped;
- decision owner rejected a plausible subgroup without independent review;
- subgroup status materially changed RF/NCRC or selection.

## Plain-language rule

The average person is not the protected person. Find the person, group, or system most likely to bear the hidden cost.
