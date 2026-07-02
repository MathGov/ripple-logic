# Stewardship Evasion Audit

**Status:** companion hardening guide for agentic and high-influence uses. Canon and Agent System control if conflict occurs.

## Purpose

Stewardship obligations can be evaded if a consequential action is mislabeled as merely informational, advisory, educational, experimental, or private. This audit detects such evasion.

## Evasion trigger questions

A run SHOULD escalate stewardship review if any answer is yes:

1. Could the output materially influence a real decision owner?
2. Could it narrow real options even if not formally binding?
3. Could it affect rights, livelihood, education, health, safety, public policy, employment, or ecological conditions?
4. Does the operator have execution capability or delegated authority?
5. Is there automation, agentic looping, bulk action, or workflow integration?
6. Are affected parties unable to see, contest, or appeal the influence?
7. Is the decision owner using an informational label to avoid PCC, RF/NCRC, TRC, CSV, or review?
8. Could repeated low-stakes outputs accumulate into high-stakes structural effect?

## Stewardship status labels

| Label | Meaning |
|---|---|
| NOT_STEWARDSHIP_MATERIAL | no material influence or execution pathway |
| STEWARDSHIP_PLAUSIBLE | influence pathway exists; document and monitor |
| STEWARDSHIP_REQUIRED | delegated influence, public/institutional impact, rights exposure, or execution pathway exists |
| STEWARDSHIP_EVASION_RISK | label appears to understate consequential influence |
| STEWARDSHIP_ESCALATE | independent review required before continuing |

## No-label-laundering rule

Calling a run educational, experimental, internal, or informational does not remove stewardship obligations if the output predictably influences consequential action.

## Plain-language rule

If the advice moves the hand that moves the world, it belongs under stewardship.
