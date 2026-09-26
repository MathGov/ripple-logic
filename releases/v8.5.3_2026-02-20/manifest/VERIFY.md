# Verify this RippleLogic v8.5.3 release bundle

## Step 1: Verify SHA-256 checksums
From the release root:

- Linux:
  - `sha256sum -c manifest/SHA256SUMS.txt`
- macOS:
  - `shasum -a 256 -c manifest/SHA256SUMS.txt`
- Windows PowerShell:
  - `Get-Content manifest/SHA256SUMS.txt | ForEach-Object { $h,$p = $_ -split '\s{2,}'; if ($p) { $calc=(Get-FileHash $p -Algorithm SHA256).Hash.ToLower(); if ($calc -ne $h) { throw "Mismatch: $p" } } }`

If all lines verify, file integrity matches the manifest.

## Step 2: Spot-check pack-specific verification
- OperatorAuth pack: `companion/OperatorAuth_Pack_v8.5.3/VERIFY.md`
  - includes schema + signature verification instructions for the example envelope.
