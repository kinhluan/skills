---
name: code-quality-gate
description: Design, diagnose, or repair automated code quality gates using linters, type checkers, tests, coverage, SAST, and SonarQube or SonarCloud. Use when CI quality checks fail, a team needs a pre-merge policy, or static-analysis findings require triage.
metadata:
  tags: ["quality-gate", "static-analysis", "lint", "coverage", "sonarqube", "ci"]
---

# Code Quality Gate

Build a gate from project risks and observed baselines. Do not present a tool's sample threshold as a universal standard, and do not weaken a gate merely to make a pipeline green.

## Diagnose a Failure

1. Read the exact CI log and tool version.
2. Reproduce the narrow failing check locally when safe.
3. Separate:
   - product defect;
   - test defect or flaky signal;
   - configuration drift;
   - generated or third-party code;
   - credible false positive.
4. Fix the cause at the smallest responsible layer.
5. Re-run the failed check and relevant neighboring checks.
6. Record any accepted exception with owner, evidence, expiry, and review date.

Do not bulk-suppress rules, mark findings false-positive without evidence, or add tests that only execute lines without checking behavior.

## Design a Gate

Choose checks from the repository's languages and risks:

| Risk | Useful evidence |
|---|---|
| syntax or style drift | formatter and linter |
| invalid types or contracts | compiler or type checker |
| behavior regression | focused unit/integration tests |
| untested changed logic | diff or new-code coverage |
| known vulnerable patterns | SAST and dependency scanning |
| leaked credentials | secret scanning |
| architecture erosion | dependency or fitness-function checks |

Prefer checks on changed code for gradual adoption. Calibrate numeric thresholds from the current baseline, criticality, and improvement target. Protect critical paths with behavioral tests even when aggregate coverage is high.

## SonarQube/SonarCloud

Inspect the active quality profile and gate instead of assuming default conditions. Triage new-code findings first. Treat security hotspots as items requiring review, not automatically as confirmed vulnerabilities. Pin supported scanner/action versions according to the project's dependency policy.

## Verification

Report:

1. failing rule and evidence;
2. root cause classification;
3. files changed or exception rationale;
4. exact commands/checks run and results;
5. residual risk and follow-up owner.

Never report a gate as passing based only on local lint if the gate also depends on server-side analysis.
