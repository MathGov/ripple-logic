# Security and Misuse Reporting

This repository is a framework/source release, not a deployed system. Still, misuse can occur if someone claims certification, legal authorization, ethical approval, or automated moral truth based on partial or incorrect implementation.

Please report issues involving:

- false public claims of MathGov certification;
- misuse of RLS to override failed rights, tail-risk, or CSV gates;
- claims that SGP grants governance authority;
- unsafe autonomous-agent deployment claims;
- workbook formula bugs affecting admissibility or score outputs;
- security-sensitive disclosure problems in examples or audit records.

Do not publish exploit-enabling details if a vulnerability could create harm. Open an issue with a safe summary and request maintainer contact for responsible disclosure.

## Agentic security acceptance

The Agent System already contains an OWASP-aligned agentic threat map. `docs/assurance/AGENTIC_SECURITY_ACCEPTANCE_PACK_TEMPLATE.md` adds a test-evidence surface so conceptual controls can be exercised against attack fixtures, telemetry requirements, pass/fail rules, and regression cases. A completed mapping without executed tests is not deployment assurance.
