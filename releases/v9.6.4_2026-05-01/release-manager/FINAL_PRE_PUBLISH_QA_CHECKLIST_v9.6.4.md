# Final Pre-Publish QA Checklist - RippleLogic v9.6.4

## Content and boundary
- [ ] Country starter annex metadata status lines read: `Draft - review pending; not approved for pilot use`.
- [ ] Country starter annexes include the pilot-posture line.
- [ ] Pilot Readiness Memo uses safe Vietnam translation-source wording.
- [ ] SGP filename is consistently `SGP_v4.7.1.docx` across public release surfaces.
- [ ] No public release artifact points to any SGP draft, review-copy, or process-suffix variant.
- [ ] Agent System Section 47.2 JSON block uses valid plain quotes.
- [ ] Aligners Sheet Parameters rights coverage summaries match the canon.

## Manifest and checksum
- [ ] Manifest path policy is stated as repository-relative for the tagged release tree.
- [ ] Core manifest regenerated from exact final bytes.
- [ ] Combined manifest regenerated from exact final bytes.
- [ ] SHA256SUMS regenerated from exact final bytes.
- [ ] Convenience ZIPs are not treated as canonical artifacts.

## Claim boundary
- [ ] No Tier 4 claim.
- [ ] No autonomous public-authority deployment claim.
- [ ] No legal approval claim.
- [ ] No claim that SGP grants governance authority.
- [ ] Pilot localization artifacts remain pilot-grade planning material only.

## Upload
- [ ] Upload the `releases/v9.6.4_2026-05-01/` folder to the repo tree.
- [ ] Use tag `v9.6.4_2026-05-01`.
- [ ] Use the GitHub release body from `GITHUB_RELEASE_DESCRIPTION_v9.6.4.md`.
- [ ] After upload, verify representative hashes against `manifests/SHA256SUMS.txt`.
