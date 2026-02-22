# RippleLogic ProofPack-Lite v8.5.3-beta.1

This bundle is the minimum public conformance substrate for RippleLogic v8.5.3 Tier 1-3 style behavioral testing.

## What this pack is
A hash-pinned, schema-backed, test-vector bundle used to:
1. validate vector structure
2. compare candidate outputs to expected outputs
3. prevent silent drift in core conformance behavior

## What this pack is not
- Not the full RippleLogic runtime engine
- Not Tier-4 deterministic runtime proof
- Not a replacement for the canonical RippleLogic / SGP / Agent System documents

## Included conformance behaviors (5-vector beta set)
- TV-0001 baseline admissible
- TV-0002 NCRC rights-floor rejection
- TV-0003 TRC tail-risk review escalation
- TV-0004 containment trigger
- TV-0005 non-decisive review (no containment)

## Quick start (Windows PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -File .\tools\generate_sha256sums.ps1
py .\tools\validate_proofpack.py .
powershell -ExecutionPolicy Bypass -File .\tools\build_bundle.ps1
```

If `jsonschema` is installed, schema validation is enabled automatically. If not, the validator still performs file checks and output comparisons.

## Conformance profile
`LITE_BETA_STRICT`
- exact comparison for key output fields
- explicit path labels required
- explicit flags required
- UCI may be declared unavailable in this beta set

## Version pins
See `VERSION_PINS.json` and `manifest.json`.

## Upstream artifact hashes
See `UPSTREAM_ARTIFACT_HASHES.json` for hashes computed from the local uploaded RippleLogic canonical files used during pack assembly.
