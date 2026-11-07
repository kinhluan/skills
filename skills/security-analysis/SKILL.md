---
name: security-analysis
description: Review code, configuration, dependencies, architecture, CI, or LLM/agent integrations for security vulnerabilities and missing controls. Use for secure code review, vulnerability and dependency-alert triage, OWASP-oriented audits, secrets handling, supply-chain and DevSecOps checks, prompt-injection and agent-permission review, remediation, or security regression testing.
metadata:
  tags: ["security-review", "vulnerability", "sast", "sca", "secrets", "supply-chain", "ai-security", "remediation"]
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
- object/function/property-level authorization, including SSRF and other server-side request paths;
- input parsing, injection, output encoding, and file/path handling;
- cryptographic purpose, key management, and secret exposure;
- exceptional conditions: fail-open error handling, partial failures, and resource cleanup;
- race conditions, resource exhaustion, and abuse controls;
- software supply chain: dependencies, build, CI/CD, artifacts, and update channels;
- LLM and agent integrations (below);
- logging, alerting, privacy, tenant isolation, and error leakage;
- unsafe defaults and environment/IaC drift.

Map findings to the current OWASP Top 10 (2025 edition at time of writing) and CWE identifiers. Check the current edition rather than freezing a historical list.

## LLM and Agent Integrations

Treat every model output and every piece of retrieved or tool-returned content as untrusted input.

- **Prompt injection:** can content from documents, web pages, issues, emails, or tool results change instructions or trigger actions? Delimiting text is not a control; privilege separation is.
- **Excessive agency:** list each tool the model can call, its credentials, and its blast radius. Require human confirmation for irreversible or outward-facing actions.
- **Output handling:** model output reaching a shell, SQL, HTML, file path, URL fetch, or deserializer is an injection sink.
- **Data exposure:** secrets, other tenants' data, or system prompts reachable through context, retrieval indexes, logs, or traces.
- **Extensions and plugins:** skills, MCP servers, hooks, and editor/agent plugins run with the user's privileges. Review their code, pin versions, and grant the least capability that works.
- **Consumption:** unbounded loops, recursion, or token/tool spend that an attacker can trigger.

Use the OWASP Top 10 for LLM Applications as a checklist, not as proof of coverage.

## Dependency Alert Triage

Triage each alert before ranking it, establishing:

- **Exposure:** is the dependency in runtime, build, or dev only?
- **Reachability:** is the vulnerable code actually used?
- **Exploit signals:** CISA KEV, EPSS, and the CVSS vector.
- **Fix path:** what change removes it?

A critical CVSS score in an unreachable, dev-only package can rank below a medium in an internet-facing parser. Say which signals you actually checked. The full triage flow, VEX statements, SBOMs, end-of-life status, and upgrade paths are in [dependency-management](../dependency-management/SKILL.md).

## Finding Standard

```markdown
### [Severity] [Title]

**Location/asset:** [...]
**Classification:** [OWASP category, CWE]
**Reachability and preconditions:** [...]
**Observed behavior:** [...]
**Impact:** [...]
**Evidence:** [minimal redacted trace or test]
**Root cause:** [...]
**Remediation:** [...]
**Regression test:** [...]
**Residual risk/limits:** [...]
```

Severity must combine technical exploitability with business context and existing controls. State the scoring method/vector when used (CVSS v4.0 or v3.1). Do not invent remediation deadlines; map to the owner's policy.

## Safe Handling

- Never print or commit discovered secrets.
- Redact personal/customer data and minimize evidence.
- Do not execute suspicious payloads or dependencies on the host; use an approved isolated environment if analysis requires execution.
- Do not modify production, publish findings, revoke credentials, or contact third parties without authority.

## Routing

| Need | Skill |
|---|---|
| Design-stage threats, STRIDE, attack trees | `threat-modeling` |
| Authorized active testing | `penetration-testing` |
| REST, GraphQL, webhook, OAuth, gateway | `api-security` |
| Images, Kubernetes, registries, provenance | `container-security` |
| IAM, network, storage, cloud posture | `cloud-security` |
| CI quality and SAST gate policy | `code-quality-gate` |
| Whole-PR review beyond security | `merge-request-review` |
| CVE triage, SBOM, EOL, framework upgrades | `dependency-management` |
| Payments, ledgers, idempotency, PCI DSS | `payment-systems` |
| Schema, tenancy, row-level security, encrypted columns | `database-design` |

## Output

Lead with confirmed findings ordered by severity, then assumptions, coverage, tools/checks actually run, non-findings worth noting, and residual risk. If no findings exist, say so without implying the scope is vulnerability-free.

Load references only as needed:

| Reference | Covers |
|---|---|
| [detailed-guide](references/detailed-guide.md) | OWASP Top 10:2025 checklist with fixes, for each technology |
| [java-jvm](references/java-jvm.md) | Java, Quarkus, Vert.x, and Spring: deserialization, Jackson typing, XXE, injection sinks, framework security configuration |
| [security-tooling](references/security-tooling.md) | Secret, SAST, SCA, IaC, and CI scanners; baseline-then-ratchet rollout; pipeline hardening |

Verify tool commands, standards, and version-specific advice against current primary documentation.
