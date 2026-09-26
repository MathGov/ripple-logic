# Verify Release

Requires Python 3.8+ and only the Python standard library.

From the repository root, run:

```bash
python release/VERIFY_RELEASE.py
```

Expected output:

```text
VERIFY_RELEASE: PASS (17 files checked)
```

The verifier checks:

- every file listed in `release/SHA256SUMS.txt` exists;
- every listed file has the expected SHA-256 hash;
- no release path contains OS upload/copy suffixes such as `(1)`;
- all `.docx` and `.xlsx` files begin with OOXML ZIP magic bytes;
- all `.docx` and `.xlsx` files pass a ZIP integrity check.

`release/SHA256SUMS.txt` intentionally does not include itself.
