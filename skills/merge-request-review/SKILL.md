---
name: merge-request-review
description: Review a GitHub pull request, GitLab merge request, or local proposed change against its stated intent. Use when the user asks for a PR/MR review, issue-link verification, risk assessment, or an approve/request-changes recommendation.
metadata:
  tags: ["code-review", "pull-request", "merge-request", "risk", "testing"]
---

# Merge Request Review

Review evidence before style. A review request authorizes read-only inspection; it does not authorize posting comments, changing branches, approving, merging, or modifying the change unless the user asks.

## Workflow

1. Read repository instructions and the PR/MR description.
2. Identify the base and head revisions without disturbing unrelated local work.
3. Read linked issues and acceptance criteria when accessible.
4. Inspect the complete diff, then trace high-risk behavior into surrounding code.
5. Check tests, validation, documentation, compatibility, security, and rollback.
6. Report only actionable findings supported by a concrete failure mode.

If the working tree is dirty, avoid checkout operations that could overwrite user changes. Prefer platform APIs, `git diff <base>...<head>`, or an isolated worktree when authorized.

## Finding Standard

Each blocking finding must contain:

- severity and concise title;
- file and precise location;
- behavior that fails;
- conditions that trigger it;
- impact;
- the smallest credible fix or test.

Do not label preferences as defects. Avoid requesting broad refactors unless the current change is unsafe or incorrect without them.

## Review Priorities

1. correctness and data integrity;
2. security and permissions;
3. concurrency, failure handling, and operational risk;
4. compatibility and migration safety;
5. tests that would catch regressions;
6. maintainability and readability;
7. style not enforced automatically.

## Verdict

- `Approve`: no material findings remain.
- `Comment`: questions or non-blocking improvements only.
- `Request changes`: at least one material, reproducible defect remains.

If no findings exist, say so and name residual risks or tests not run. Never claim a command or CI check passed unless it was actually run or verified.

## Output

Lead with findings ordered by severity. Follow with assumptions/questions, then a short change summary and verification note. Keep praise and recap subordinate to defects.
