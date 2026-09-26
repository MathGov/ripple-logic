# Publication acceptance checklist
Prepared build: `MG-RL-13.0-20260926-RELEASE-I`. This is a checklist, not evidence of a completed upload.

1. Review the change report, source ownership and current claim boundaries. Preserve the exact prior archive privately.
2. Freeze master edits, reading copies, TOC labels, metadata, names and inventory before creating manifests and the final checksum ledger.
3. Extract the finished public ZIP and run `python -B verify_all.py --output-dir ../mathgov-tests`. Keep output outside the immutable package.
4. Reproduce native Calc acceptance as needed with `python -B Native_Verification/verify_native_roundtrip.py --output-dir ../mathgov-native`. Claim only the engine/version and exact bytes actually tested.
5. Publish these exact public-root files to a distinct release directory/tag. Do not overwrite a previous immutable release or silently replace earlier v13.0 bytes. Component editions and build identity are separate.
6. Align public release title, directory/date, manifest and download index. Retrieve all 15 hosted Core files and compare their SHA-256 hashes with the locally trusted manifest. Record actual commit, tag, URL, hosted workflow result and verification date in a separate publication receipt.
7. State: final Tier 1–3 research-and-teaching specification, bounded worked example and scoped tests. No empirical validation, complete external-registry conformance, production certification or execution authority is conferred. Companions outside Core 15 do not inherit Core assurance.
8. Retain an independent archive. Further empirical, machine-conformance and domain-validation work must not be represented as already completed.

Read-only download verification after upload:

```bash
python -B Publication/verify_hosted.py --base-url https://YOUR-SITE/RELEASE-DIRECTORY/ --output ../hosted-receipt.json
```

The tool compares the hosted Core bytes with the trusted local manifest; it does not upload or establish hosted CI, empirical validity or host ownership. `--all-files` checks the ledger inventory.
