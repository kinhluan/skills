---
name: security-analysis
description: Review code, configuration, dependencies, architecture, or CI for security vulnerabilities and missing controls. Use for secure code review, vulnerability triage, OWASP-oriented audits, secrets handling, DevSecOps checks, remediation, or security regression testing.
metadata:
  tags: ["security-review", "vulnerability", "sast", "sca", "secrets", "remediation"]
---

# Security Analysis

Identify credible attack paths and durable fixes without expanding into active exploitation. A code/config review authorizes inspection of the supplied scope, not testing unrelated systems.

## Workflow

1. Define assets, trust boundaries, actors, sensitive data, deployment context, and review scope.
2. Read the actual data/control flow before running broad scanners.
3. Enumerate threats relevant to the technology and business impact.
4. Use static analysis, dependency/secret scanning, IaC checks, or dynamic testing as evidence sources where configured.
5. Manually verify each material candidate and eliminate false positives.
6. Trace root cause, reachable preconditions, affected versions/tenants, and existing mitigations.
7. Propose the smallest durable fix plus a regression test.
8. Re-run the original proof/check and relevant neighboring controls.

Treat scanner output as hypotheses. Do not report a vulnerability solely because a rule fired or a package appears in a lockfile; confirm reachability and context when feasible.

## Review Lenses

- authentication, session, and credential lifecycle;
- object/function/property-level authorization;
- input parsing, injection, output encoding, and file/path handling;
- SSRF, redirect, URL, webhook, and outbound network controls;
- cryptographic purpose, key management, and secret exposure;
- race conditions, resource exhaustion, and abuse controls;
- dependency, build, artifact, and update supply chain;
- logging, privacy, tenant isolation, and error leakage;
- unsafe defaults and environment/IaC drift;
- incident detection, recovery, and auditability.

Check the current applicable standard rather than freezing one historical OWASP list.

## Finding Standard

```markdown
### [Severity] [Title]

**Location/asset:** [...]
**Reachability and preconditions:** [...]
**Observed behavior:** [...]
**Impact:** [...]
**Evidence:** [minimal redacted trace or test]
**Root cause:** [...]
**Remediation:** [...]
**Regression test:** [...]
**Residual risk/limits:** [...]
```

Severity must combine technical exploitability with business context and existing controls. State the scoring method/vector when used. Do not invent remediation deadlines; map to the owner's policy.

## Safe Handling

- Never print or commit discovered secrets.
- Redact personal/customer data and minimize evidence.
- Do not execute suspicious payloads or dependencies on the host; use an approved isolated environment if analysis requires execution.
- Do not modify production, publish findings, revoke credentials, or contact third parties without authority.
- Route authorized active testing to `penetration-testing` and design-stage analysis to `threat-modeling`.

## Output

Lead with confirmed findings ordered by severity, then assumptions, coverage, tools/checks actually run, non-findings worth noting, and residual risk. If no findings exist, say so without implying the scope is vulnerability-free.

Read [references/detailed-guide.md](references/detailed-guide.md) only for the relevant technology/checklist. Verify tool commands, standards, and version-specific advice against current primary documentation.
