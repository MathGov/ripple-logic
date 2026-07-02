# RELEASE_POLICY

This repository publishes RippleLogic canonical specification sets as **versioned releases**.

## 1) What a “Release” Means: Canon vs Draft

A GitHub **Release** with a tag is the public canonical snapshot for a specific version.

A commit to `main` may be:

- preparatory work for a future release, or
- post-release housekeeping, such as README edits, metadata updates, typo fixes, link corrections, or release-index cleanup.

**Canon is defined by the Release tag, the matching release folder, and the attached release assets, not by the moving head of `main`.**

## 2) Where Canon Lives

A canonical release should exist in two places:

- **Repository archive:** `releases/<version>_<YYYY_MM_DD>/`
- **GitHub Release page:** tag `vX.Y[.Z]_<YYYY_MM_DD>` with attached artifacts, where applicable.

Example:

```text
releases/v11.4_2026_07_02/
v11.4_2026_07_02
