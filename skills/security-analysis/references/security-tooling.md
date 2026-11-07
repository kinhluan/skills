# Codebase Security Tooling

Build a pipeline that finds problems early, fails only on what matters, and gets stricter over time. Commands were verified in November 2026 with Semgrep 1.184.0 and gitleaks 8.30.1. Re-check flags when upgrading, and pin every tool and action version.

## Layers

| Layer | Finds | Open-source options | Where it runs |
|---|---|---|---|
| Secret scanning | Keys, tokens, and passwords in code and history | gitleaks, TruffleHog (verifies live credentials) | pre-commit, PR, full history once |
| SAST | Injection, unsafe APIs, insecure configuration in code | Semgrep CE, CodeQL\*, language linters (SpotBugs + Find Security Bugs, Bandit, gosec, ESLint security plugins) | PR (diff-aware), nightly (full) |
| SCA / dependencies | Known-vulnerable libraries | OSV-Scanner, Grype, OWASP Dependency-Check, `npm audit`, `pip-audit`, `govulncheck` | PR plus daily (new CVEs appear without code changes) |
| Container images | OS and library CVEs, misconfiguration | Grype, Trivy, Syft (SBOM) | image build plus a registry rescan |
| IaC and configuration | Public buckets, open security groups, privileged pods | Checkov, Trivy config, kube-linter, conftest/OPA | PR |
| CI/CD workflows | Script injection, excessive token permissions, unpinned actions | zizmor, actionlint | PR |
| DAST | Runtime issues: headers, auth, exposure | OWASP ZAP baseline or API scan | staging, nightly |

\*CodeQL is free for public repositories. Private repositories need GitHub Code Security, which is licensed.

Dependency triage and upgrade policy belong to [dependency-management](../../dependency-management/SKILL.md).

## Commands

```bash
# Secrets
gitleaks git --redact --report-path gitleaks.json .            # full history
gitleaks git --staged --redact                                 # pre-commit
gitleaks dir --redact .                                        # working tree only
trufflehog git file://. --results=verified                     # live-verified secrets only

# SAST
semgrep scan --config p/default --metrics off --error .                       # full scan, non-zero exit on findings
semgrep scan --config p/java --config p/secrets --baseline-commit "$BASE" --error .   # PR: only new findings

# IaC, containers, workflows
checkov -d infra/ --compact --quiet
grype <image> --fail-on high
zizmor .github/workflows/
```

With `--baseline-commit`, Semgrep reports only findings introduced after that commit. Gitleaks' `--baseline-path` ignores findings recorded in an earlier report. Both were verified to suppress old findings and still report new ones.

## Rollout: Baseline, Then Ratchet

Turning on every scanner at once with blocking gates produces thousands of findings and gets the gates disabled. Instead:

1. **Inventory and baseline.** Run every scanner in report-only mode on the default branch. Record the counts by severity and rule.
2. **Stop the bleeding.** Fail PRs only on **new** findings (diff-aware SAST, baselined secrets), and on any *verified* live secret or KEV-listed dependency.
3. **Rotate before you clean.** A secret found in git history is compromised. Revoke and rotate it first; history rewriting is optional cleanup afterwards.
4. **Burn down the baseline** by rule, starting with the highest-impact categories: injection, auth bypass, deserialization, then secrets in history.
5. **Ratchet.** Lower the allowed counts or raise the severity threshold each sprint, and never let the baseline grow. Track it as a fitness function ([evolutionary-architecture](../../evolutionary-architecture/SKILL.md)).

## Suppressions and Tuning

- Every suppression (`# nosemgrep: <rule>`, `.gitleaksignore` fingerprint, Checkov skip) carries a **reason** and, for risk acceptances, an owner and an expiry. Review suppressions in PRs like code.
- Track the false-positive rate per rule. Disable or fork noisy rules instead of training developers to ignore the tool.
- Add **custom rules** for your own dangerous APIs: internal SQL helpers that concatenate, logging helpers that could log PII, or deprecated authentication wrappers. Semgrep rules are YAML and testable with `semgrep --test`.

## Harden the Pipeline Itself

- Set `permissions:` on every GitHub workflow, least privilege per job. Default to `contents: read`.
- Pin third-party actions to a **full commit SHA**. In March 2026, attackers force-pushed most `aquasecurity/trivy-action` and `setup-trivy` tags to malicious commits (CVE-2026-33634). Every workflow that referenced a tag ran the payload and exposed its secrets.
- Do not run untrusted PR code with secrets (`pull_request_target` combined with checking out the PR head is the classic mistake). Treat `${{ github.event.* }}` values as untrusted input in `run:` steps; pass them through `env:`.
- Scanner output can contain secrets: redact it (`gitleaks --redact`), restrict artifact access, and expire artifacts.
- Run scanners from pinned images or versions. Verify the checksums or signatures of downloaded binaries.

## Reporting

Report findings in SARIF where the platform supports it (GitHub code scanning, GitLab), so they appear inline on the diff. Aggregate counts by repository, severity, and age into one dashboard. Mean time to remediate by severity is the metric that shows whether the program works.
