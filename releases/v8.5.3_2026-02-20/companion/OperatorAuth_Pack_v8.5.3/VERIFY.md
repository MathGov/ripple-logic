# OperatorAuth Pack Verification (OACP-1.0)

This folder contains the **Operator Auth Canon Pack** referenced by *RippleLogic Agent System v8.5.3* Appendix D.

## What is in this pack

- `operator_command_envelope.schema.json`  (schema for signed command envelopes)
- `jwks.schema.json`  (schema for Ed25519 JWKS)
- `jwks_example.json`  (example JWKS containing a single Ed25519 public key)
- `command_example_01.json`  (example signed command envelope)
- `manifest.json`  (SHA-256 for every file in this folder)

> Note: In the Agent System text these are sometimes referred to as `schemas/...` and `examples/...`.  
> This release ships them flattened at pack root to match the Document Completion Statement.

## Two-step verification (human-readable)

### Step 1: Verify file integrity with SHA-256
Compute SHA-256 for every file and compare to `manifest.json`.

- Linux:
  - `sha256sum *`
- macOS:
  - `shasum -a 256 *`
- Windows PowerShell:
  - `Get-FileHash * -Algorithm SHA256`

### Step 2: Verify the example signature
`command_example_01.json` has:
- `payload` (object)
- `sig` (base64url, **raw 64-byte Ed25519 signature**)

Verification procedure (normative in Appendix D):
1. Validate the envelope against `operator_command_envelope.schema.json`.
2. Resolve the public key by `payload.meta.kid` from `jwks_example.json`.
3. Canonicalize `payload` using RFC 8785 (JCS) and sign/verify **the UTF-8 bytes**.
4. Verify Ed25519(sig, payload_bytes, public_key).
5. Enforce nonce/time-window checks in runtime deployments.

Practical note for this example:
- The payload contains **no floats**, so `jq -S -c` produces the same stable ordering used by many JCS implementations.

Example (Linux/macOS) using `jq`:
- `PAYLOAD_BYTES=$(jq -S -c '.payload' command_example_01.json | iconv -t utf-8)`
- Verify with any Ed25519 tool/library using the JWKS public key `x`.

If you want a minimal Python verifier, use `cryptography` and ensure the payload canonicalization follows RFC 8785 (JCS).
