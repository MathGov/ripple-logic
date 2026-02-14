# Security Policy

## Supported Versions
RippleLogic is a specification repository with versioned releases. Security-sensitive issues may involve:
- tampered release artifacts
- checksum mismatch
- misleading claims in release notes that could cause unsafe implementation

We treat the **latest tagged Release** as the primary supported public snapshot.

## Reporting a Vulnerability
If you believe you’ve found a security issue, please do not open a public issue immediately.

Instead:
1) Contact the maintainers privately with:
   - a clear description
   - affected version/tag
   - reproduction steps or proof (if applicable)
   - suggested mitigation (if known)
2) We will acknowledge receipt and coordinate a fix and disclosure timeline.

## What counts as a security issue here
- Release artifact integrity problems (mismatched hashes, incorrect assets)
- Malicious or confusing packaging that could lead to unsafe downstream use
- Vulnerabilities in any scripts/tools that may be added to support verification or evaluation

## Disclosure
We aim for responsible disclosure: verify, patch, and publish a note in a tagged Release when appropriate.
