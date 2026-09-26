# Reproduce Release I

Build: `MG-RL-13.0-20260926-RELEASE-I`. Hosted reference environment: Ubuntu 24.04, Python 3.13, Node.js 22. Reading the publication requires no installation.

## From the GitHub repository

```sh
git clone https://github.com/MathGov/ripple-logic.git
cd ripple-logic
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-ci.txt
python -B releases/v13.0-release-i/verify_all.py --output-dir ../mathgov-results
```

On Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1`, or invoke `.\.venv\Scripts\python.exe` directly if activation is restricted. One supplied loopback HTTP test can encounter a Windows file-deletion race. Ubuntu hosted checks are the reference; a Windows failure must be inspected rather than dismissed as a pass.

## From the original publication ZIP

Download `MathGov_RippleLogic_v13.0_Final_Publication_I.zip` and its `.sha256` file from [Release I](https://github.com/MathGov/ripple-logic/releases/tag/v13.0-20260926-release-i). Verify the ZIP before extraction:

```sh
sha256sum -c MathGov_RippleLogic_v13.0_Final_Publication_I.zip.sha256
```

On Windows use `Get-FileHash -Algorithm SHA256 <zip-path>` and compare with the checksum file. The expected original ZIP SHA-256 is:

```text
c7ece3a604980fa859e41cd63bbebe6d9adc0953e795737c8a38c16b82ac4d85
```

Extract to a new directory. In the extracted directory containing `verify_all.py` and `Reference/`, create and activate a virtual environment **outside** the extracted publication, then run:

```sh
python -m pip install -r Reference/requirements.txt
python -m pip install rfc3339-validator==0.1.4 six==1.17.0
python -B verify_all.py --output-dir ../mathgov-results
```

The original requirements omit the optional RFC 3339 validator. Without it, JSON Schema date-time validation is not enforced and the invalid-timestamp test fails. The two additional pins correct the environment; they do not modify the frozen ZIP or specification. The release's `requirements-ci.txt` companion contains the complete direct dependency set and may instead be installed from outside the extraction.

Keep generated results and virtual environments outside the frozen publication. Scoped test success does not establish empirical validity, certification, native Excel recalculation, or production readiness. Read the [verification report](https://mathgov.github.io/ripple-logic/Reports/Release_I_Verification.html).

## Maintained reading site

With Python and Node.js available, run:

```sh
python scripts/build_site.py
python scripts/check_site.py
npm ci
npx playwright install chromium
npm run test:site
```

The builder copies the frozen publication to a new `_site/` directory, preserves its homepage as `publication-index.html`, and adds the maintained doorway. It refuses an existing output directory. For a fresh subsequent build, choose a new directory with `--output <new-directory>` or remove only your disposable `_site/` output. Tests use the default `_site/` location.
