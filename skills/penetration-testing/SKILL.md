---
name: penetration-testing
description: Plan and conduct authorized, bounded penetration tests with non-destructive validation and defensible reporting. Use for a system the user owns or is explicitly authorized to assess, including rules of engagement, evidence collection, vulnerability verification, remediation, and retesting.
metadata:
  tags: ["security", "penetration-testing", "authorized-assessment", "reporting", "remediation"]
---

# Penetration Testing

Treat written authorization and a precise rules-of-engagement document as prerequisites. If ownership, scope, or permission is unclear, stop before active testing and help define the engagement. Educational practice must use an intentionally vulnerable lab or CTF target.

## Authorization Gate

Record and verify:

- authorizing organization and named contact;
- in-scope domains, IP ranges, applications, APIs, accounts, and environments;
- explicitly excluded assets and third parties;
- allowed techniques and maximum request/concurrency rates;
- test window and time zone;
- test accounts and data handling requirements;
- emergency contact and stop signal;
- outage, data modification, social engineering, physical access, and denial-of-service rules;
- evidence retention and destruction policy.

Authorization to assess one asset does not extend to connected services, cloud tenants, employees, vendors, or discovered infrastructure.

## Stop Conditions

Pause immediately when:

- scope cannot be unambiguously resolved;
- a third-party or production-critical system may be affected;
- service health degrades or a stop request arrives;
- sensitive data appears beyond the minimum proof;
- testing would require persistence, destructive change, uncontrolled code execution, credential harvesting, or lateral movement not explicitly approved;
- the observed impact exceeds the agreed validation method.

Notify the engagement contact and preserve a factual timeline.

## Assessment Workflow

### 1. Plan

Translate objectives into test cases and safe evidence:

| Objective | Safe validation |
|---|---|
| identify exposed services | rate-limited enumeration inside approved ranges |
| verify access control | designated test accounts and synthetic records |
| verify injection risk | benign marker or transaction rollback |
| verify data exposure | minimum metadata or one synthetic record |
| verify privilege boundary | demonstrate denied/allowed action with test roles |
| verify remediation | repeat only the original bounded test |

Choose a standard appropriate to the target, such as OWASP WSTG/ASVS/API Security, NIST SP 800-115, or a documented internal methodology.

### 2. Discover

Begin with passive and authenticated inventory supplied by the owner. Confirm each discovered host or endpoint against scope before active interaction. Use conservative rates and log tool versions, configuration, timestamps, and source address.

Do not use leaked credentials, secret-search results, or unrelated public data to access an account. Report exposed secrets through the agreed channel without attempting them.

### 3. Analyze

Combine automated findings with manual verification. Scanners produce hypotheses, not confirmed vulnerabilities. For each candidate:

1. reproduce with the least invasive request;
2. rule out environmental and authorization artifacts;
3. capture request/response metadata with secrets redacted;
4. map the affected boundary and preconditions;
5. stop once business impact is credibly demonstrated.

### 4. Validate Impact

Prefer a benign proof:

- a unique marker instead of reading arbitrary data;
- a test tenant instead of another customer's tenant;
- a harmless command such as an agreed identity query in an isolated lab;
- a rollback transaction instead of persistent modification;
- a canary callback controlled by the client instead of an external listener.

Do not install backdoors, create users, add startup tasks, establish persistence, dump password databases, pivot to additional hosts, or leave remote access. If advanced adversary emulation is explicitly contracted, it requires a separate technique matrix, safety controls, monitoring coordination, and cleanup verification; do not infer that authority from a generic pentest request.

### 5. Remediate and Retest

Give the owner a root-cause fix, compensating controls, and a regression test. Retest the exact finding and nearby variants without expanding scope. Record `fixed`, `partially fixed`, `not fixed`, or `not retested`, with evidence and date.

## Evidence Handling

- Minimize collection and redact tokens, credentials, personal data, and customer content.
- Encrypt evidence using the engagement's approved mechanism.
- Keep a chain of custody when required.
- Never place secrets in chat, issue trackers, screenshots, or source control.
- Destroy or return evidence according to the signed retention policy and confirm completion.

## Reporting

For each finding include:

```markdown
### [Finding title]

**Affected asset:** [in-scope identifier]
**Severity:** [organization-approved method and vector]
**Preconditions:** [access, role, state]
**Evidence:** [minimal redacted proof]
**Impact:** [credible business/security consequence]
**Root cause:** [control failure]
**Remediation:** [specific durable fix]
**Regression test:** [safe verification]
**Limitations:** [what was not tested or inferred]
```

Separate confirmed findings from observations and scanner-only candidates. Do not invent remediation deadlines; map severity to the owner's risk policy. State coverage gaps, unreachable assets, partial-source failures, and tests omitted by the rules of engagement.

## Completion Checklist

- all testing stopped and temporary artifacts removed;
- no accounts, keys, tunnels, callbacks, or modified data remain;
- service health confirmed with the owner;
- evidence inventory and retention action recorded;
- urgent findings communicated through the agreed channel;
- final report and retest scope accepted by the engagement contact.

## Primary References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security Project](https://owasp.org/www-project-api-security/)
- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)
- [FIRST CVSS](https://www.first.org/cvss/)
