# RELEASE_POLICY

This repository publishes RippleLogic canonical specification sets as *versioned releases*.

## 1) What a “Release” Means (Canon vs Draft)

A GitHub **Release** (tagged) is the public, canonical snapshot for a specific version.

A **commit** to `main` may be:
- preparatory work for a future release, or
- a post-release housekeeping change (README edits, metadata, etc.)

**Canon is defined by the Release tag + attached assets**, not by the moving head of `main`.

## 2) Where Canon Lives

- **Repository archive:** `releases/<version>_<YYYY-MM-DD>/`
- **GitHub Release page:** tag `vX.Y[.Z]` with attached artifacts (DOCX/XLSX/ZIP/TXT)

Rule: The Release page should correspond to the contents of its matching `releases/...` folder.

## 3) Versioning

Tags use: `vMAJOR.MINOR[.PATCH]`

Guidance:
- **MAJOR**: structural or governance changes that meaningfully alter interpretation/implementation.
- **MINOR**: additive or clarifying changes that preserve prior intent and interfaces.
- **PATCH**: corrections (typos, formatting, minor clarifications) with no semantic change.

File names may include internal patch identifiers (e.g., `PATCH2`) for provenance.  
The **tag** is the public version anchor.

## 4) Tier Claims and Non-Claims

Each release must clearly state what it *does* and *does not* claim.

Default stance for public canon releases:
- Supports **Tier 1–3** usage and evaluation based on released artifacts and worked examples.
- **No Tier-4 determinism claims** unless explicitly stated and independently validated.

## 5) Integrity and Verification

Each canon release should include:
- A `SHA256SUMS_*.txt` file for the release artifacts, and/or
- Equivalent integrity metadata.

Verification expectation:
- Users can download an asset and verify its hash against `SHA256SUMS_*.txt`.

## 6) What Goes Into a Canon Release (Recommended Minimum)

A canonical spec release should include (as applicable):
- Core specification document(s)
- SGP (Sentience Gradient Protocol) spec (if pinned)
- Agent System spec (if pinned)
- A worked exemplar (e.g., Ripple Aligners Sheet)
- ProofPack skeleton or verification artifacts
- SHA256 integrity file
- Optional convenience bundle (zip)

## 7) How Releases Are Created (Operational Checklist)

1. Ensure `releases/<version>_<date>/` exists in the repo and contains the canon artifacts.
2. Update top-level `README.md` to point to the current canon folder.
3. Create the GitHub Release **online** (preferred) to:
   - set tag `vX.Y[.Z]` targeting `main`
   - add release title + notes
   - attach the same canon artifacts as assets
   - avoid pre-release checkbox unless intentionally non-canon
4. After publishing, verify:
   - the folder is visible in repo web view
   - assets download successfully
   - hashes match for at least one downloaded file

## 8) Backward Compatibility and Deprecation

Older releases remain accessible under `releases/` and via the Releases page.  
If a release is superseded, it should remain intact and should not be rewritten.

Rule: **Do not rewrite published tags** (no force-updating canon tags).

## 9) Contact / Governance Notes

RippleLogic is published as a rights-first, audit-oriented governance framework.  
Interpretation and implementation should respect the release’s stated tier boundaries and rights constraints.
