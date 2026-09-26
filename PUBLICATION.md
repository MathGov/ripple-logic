# Release I: GitHub publication integration

The user-supplied `MathGov_RippleLogic_v13.0_Final_Publication_I.zip` is the source of the frozen directory `releases/v13.0-release-i/`.

- Build: `MG-RL-13.0-20260926-RELEASE-I`
- Original archive SHA-256: `c7ece3a604980fa859e41cd63bbebe6d9adc0953e795737c8a38c16b82ac4d85`
- Inventory: 288 files, including 287 files controlled by `SHA256SUMS.txt`.
- The supplied publication files, including their historical preparation statements, are unchanged. Actual hosted publication evidence belongs in release assets and GitHub Actions records.
- Private provenance is not part of this publication.

## Reproducibility correction outside the frozen publication

The supplied `Reference/requirements.txt` pins `jsonschema==4.26.0` but does not install the optional date-time format validator. In a clean environment, `FormatChecker` then lacks `date-time` support, and `test_records.RecordTests.test_timestamp` fails because an invalid timestamp is accepted.

The repository-level `requirements-ci.txt` repeats the original direct dependency pins and explicitly pins `rfc3339-validator==0.1.4` and its `six==1.17.0` dependency. It is maintained independently so dependency-update proposals cannot rewrite the frozen package. No test, validator, mathematical definition, reading copy, checksum, or publication master is edited to achieve this fix. Consumers should follow [INSTALLATION.md](INSTALLATION.md).

## Maintained site and repository history

`scripts/build_site.py` copies the frozen publication to a new output directory, preserves its original homepage as `publication-index.html`, and adds the maintained `site/` doorway. Existing document URLs and all original document bytes are preserved. The homepage reports current hosting status; frozen preparation statements remain historical evidence. `scripts/check_site.py` pins the trusted original ledger, checks every frozen file, compares deployed bytes, and checks maintained navigation links. Browser tests cover desktop/mobile overflow, component filtering, no-JavaScript access, and automated WCAG checks on the maintained homepage; they are not a complete accessibility certification of all publication documents.

Historical release directories are restored byte-for-byte from commit `97d7a3f` to keep incoming GitHub links usable. Updates to `ripplelogic.org` and `mathgov.org` are a separate stage.

Future releases use GitHub immutable releases. Release I was published before that setting and remains non-immutable at the asset level; tag rules prevent normal tag updates/deletion. Original ZIP bytes and existing receipt assets remain unchanged. New installation instructions and requirements are explicitly separate integration companions.

The active workflow is the repository-root `.github/workflows/verify.yml`. The frozen package's original workflow is retained as provenance inside its versioned directory; nested workflows are not active GitHub workflows.

## Platform scope

The supplied loopback HTTP test can race with Windows file locking when it deletes a file immediately after serving it. The reference CI therefore uses the publication's intended Ubuntu environment. A Windows file-lock failure must not be described as a successful run. No new native Excel or LibreOffice recalculation is claimed.

## Release and hosted-byte evidence

The release uses the distinct tag `v13.0-20260926-release-i`. The original uploaded ZIP remains the trusted archive; the repository's surrounding integration files are a separate layer. Previous releases and tags are preserved.

Verification should record the tag, final commit, workflow URLs, and the result of downloading the hosted files against the local trusted ledger. The package provides:

```sh
python -B releases/v13.0-release-i/Publication/verify_hosted.py \
  --base-url https://raw.githubusercontent.com/MathGov/ripple-logic/COMMIT/releases/v13.0-release-i/ \
  --all-files --commit COMMIT --tag v13.0-20260926-release-i \
  --output ../hosted-publication-receipt.json
```

The hosted verifier checks file identity. Its output does not itself check GitHub Actions or establish scientific validity.
