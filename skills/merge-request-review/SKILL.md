---
name: merge-request-review
description: Review a GitHub pull request, GitLab merge request, or local proposed change against its stated intent, or prepare your own PR for review. Use when the user asks for a PR/MR review, issue-link verification, risk assessment, an approve/request-changes recommendation, or help authoring and answering review comments.
metadata:
  tags: ["code-review", "pull-request", "merge-request", "review-comments", "risk", "testing"]
---

# Merge Request Review

Review evidence before style. A review request authorizes read-only inspection; it does not authorize posting comments, changing branches, approving, merging, or modifying the change unless the user asks.

**User sovereignty:** the agent proposes findings, comments, and a verdict. The user (or a designated maintainer) decides and merges. Never merge on your own initiative, and never override a red build to "just ship".

Authoring your own PR or answering review comments? Follow [the PR author guide](references/pr-author-guide.md).

## Role Boundaries

| Concern | Owner | Do not do here |
|---|---|---|
| Correctness, design, tests, readability | This review | — |
| Coverage thresholds, Sonar, SAST gate | `code-quality-gate` | Do not pass a PR on lint score alone |
| Threat model, vulnerability class, secrets policy | `security-analysis`, `threat-modeling` | Do not claim a security sign-off |
| Architecture drift, C4 vs code | `architecture-review` | Do not relitigate an accepted ADR |

Language details: `python-development`, `javascript-typescript`, `golang-development`. Design checks: `clean-architecture`, `ddd-tactical`. Tests first: `tdd-red-green-refactor`.

## Workflow

1. Read repository instructions and the PR/MR description.
2. Identify the base and head revisions without disturbing unrelated local work.
3. Read linked issues and acceptance criteria when accessible. If you cannot restate the intent in one sentence, say so and stop: the PR is not ready.
4. Check fit: does the change belong in this component or bounded context? A new dependency, table, or public API may need an ADR.
5. Read **tests before production code**. Would they fail for the right reason if the code broke? Missing tests for the claimed behavior is a blocker.
6. Inspect the complete diff, then trace high-risk behavior into surrounding code.
7. Check validation, documentation, compatibility, security, and rollback.
8. Report only actionable findings supported by a concrete failure mode.

If the working tree is dirty, avoid checkout operations that could overwrite user changes. Prefer platform APIs, `git diff <base>...<head>`, or an isolated worktree when authorized.

Timebox a human-sized review to 30–45 minutes. Needing much longer usually means the PR should be split; recommend the split instead of hero-reviewing it. On a follow-up push, re-review the delta unless the intent changed.

## Finding Standard

Each blocking finding must contain:

- severity and concise title;
- file and precise location;
- behavior that fails;
- conditions that trigger it;
- impact;
- the smallest credible fix or test.

Do not label preferences as defects. Avoid requesting broad refactors unless the current change is unsafe or incorrect without them.

## Severity

**Blocker** — must change before merge:

- behavior contradicts the stated intent;
- missing or misleading tests for the claimed behavior;
- broken invariant (aggregate consistency, money/time units, authorization in the wrong layer);
- dependency rule violation (framework or ORM leaking into the domain);
- data loss, race, or resource leak;
- secrets or PII in the diff.

**Should-fix** — request changes unless the author records a reason:

- duplication or dead code the change just introduced;
- an API that makes an invalid state representable when a type could prevent it;
- a swallowed error path (`except: pass`, ignored `err`);
- a breaking on-disk or schema change without a migration or flag.

**Nit** — non-blocking; prefix `nit:` so the author can batch or skip.

## Review Priorities

1. correctness and data integrity;
2. security and permissions;
3. concurrency, failure handling, and operational risk;
4. compatibility and migration safety;
5. tests that would catch regressions;
6. maintainability and readability;
7. style not enforced automatically.

## Comment Style

One comment, one action: say **what**, **why**, and **what done looks like**, on the line that should change.

```text
blocker: allocate() still admits a second patient when capacity is 1.
Add test_allocate_rejects_when_capacity_exceeded, then reject in the aggregate, not the HTTP handler.
```

```text
question: is ESI-1 meant to bypass this cap?
```

Use `question:` when you lack context instead of a fake blocker. Offer a suggestion diff rather than a lecture. No sarcasm, and no "this is messy" without a concrete fix.

## Verdict

- `Approve`: no material findings remain, and you would ship it. Never approve code you did not read.
- `Comment`: questions or non-blocking improvements only, or a partial review.
- `Request changes`: at least one material, reproducible defect remains. Do not request changes on nits alone.

If no findings exist, say so and name residual risks or tests not run. Never claim a command or CI check passed unless it was actually run or verified.

## Output

Lead with findings ordered by severity. Follow with assumptions/questions, then a short change summary and verification note. Keep praise and recap subordinate to defects.
