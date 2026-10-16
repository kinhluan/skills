---
name: code-review-pr
description: Author and review pull requests as a software engineer. Use when opening a PR, reviewing a teammate's diff, or answering review comments. Complements QC gates; does not replace them.
metadata:
  tags: ["code-review", "pull-request", "pr", "diff", "review-comments", "conventional-commits"]
  version: 1.0.0
---

# Code Review & Pull Requests (Software Engineer)

This skill is the **engineer's** PR loop: small diffs, intent-first review, actionable comments. It is not a quality-gate or security sign-off.

**User sovereignty:** the agent proposes (review comments, Approve, merge checklist). The user decides. The agent **never merges** a PR — not theirs, not a teammate's.

| Concern | Owner | Do not do here |
|---------|-------|----------------|
| Correctness, design, tests, readability | **SE (this skill)** | — |
| Coverage thresholds, Sonar, SAST gate | QC (`code-quality-gate`) | Do not "pass" a PR on lint score alone |
| Threat model, vuln class, secrets policy | SecOps | Do not claim a security review |
| DORA / pipeline health | SRE | Do not block on MTTR commentary |

`merge-request-review` (QC checkout playbook) is a different role. If you are the author or the engineering reviewer, stay here.

Language details: `python-development`, `javascript-typescript`, `golang-development`. Design checks: `clean-architecture`, `ddd-tactical`. Decision already made? Read the ADR (`architecture-decision-records`) instead of relitigating it in comments.

---

## 1. Author: before you open

A reviewable PR is a gift to the reviewer. Unreviewable PRs get rubber stamps or stall.

**Size:** one intent. If you need "and also", split. Rule of thumb: a reviewer can hold the change in their head in one sitting (typically <400 lines of real code, not lockfiles).

**Branch:** `type/short-topic` (`feat/`, `fix/`, `refactor/`, `chore/`). No `misc-fixes`.

**Commits:** Conventional Commits, one logical change per commit if you expect bisect.

```
feat(ward): refuse allocate when capacity is full

Closes #142
```

Types: `feat` `fix` `refactor` `test` `docs` `chore` `perf`. Breaking change: `feat!:` or a `BREAKING CHANGE:` footer.

**Description (required):**

```markdown
## Why
<problem in one or two sentences, link the issue>

## What
<what the diff does, not a file list>

## How to check
- [ ] tests: `...`
- [ ] manual: <only if tests cannot cover it>

## Out of scope
<what you deliberately did not change>
```

**Self-review the diff** before requesting review:

- [ ] Tests exist for the new behavior (`tdd-red-green-refactor`). No production-only dump.
- [ ] No secrets, no credentials, no accidental lockfile churn.
- [ ] Public APIs/types match the ubiquitous language.
- [ ] Dependency Rule: domain does not import adapters (`clean-architecture`).
- [ ] You would know how to revert this PR in one click.

---

## 2. Reviewer: order of work

Do not start at line 1 of the largest file. Read **intent → tests → production**.

1. **Intent.** PR description + linked issue. If you cannot restate the intent in one sentence, comment that and stop — the PR is not ready.
2. **Fit.** Does this belong in this bounded context / component (`c4-level3-component`, `ddd-tactical`)? New dependency, new table, new public API → should an ADR exist?
3. **Tests.** Do they fail for the right reason if you break the code? Missing tests for the claimed behavior is a **blocker**, not a nit.
4. **Diff.** Correctness, then design, then style.
5. **Leave or approve.** Every review ends with a decision (see below). Silent unread diffs are not a review.

Timebox: 30–45 minutes. Longer means the PR is too big — request a split rather than hero-reviewing it.

---

## 3. What to look for (engineering)

**Blockers (must change before merge):**

- Wrong behavior vs the stated intent.
- Missing or misleading tests.
- Invariant break (aggregate consistency, money/time units, authz checks in the wrong layer).
- Dependency Rule violation (framework/ORM leaking into domain).
- Data loss, race, or obvious resource leak.
- Secrets or PII in the diff.

**Should-fix (request changes unless author has a written reason):**

- Unnamed magic; dead code; duplication the author just introduced.
- API that makes an invalid state representable when a type could prevent it.
- Error path swallowed (`except: pass`, ignored `err`).
- Feature-flag / migration missing for a breaking on-disk change.

**Nits (non-blocking):**

- Naming taste, import order, comment wording.
- Prefix `nit:` so the author can batch or skip.

Do **not** bikeshed an accepted ADR. Do **not** demand a rewrite to your preferred framework in this PR.

---

## 4. Comment style

One comment = one action. Say **what**, **why**, and **what done looks like**.

```
blocker: allocate() still admits a 2nd patient when capacity is 1.
Add a test like test_allocate_rejects_when_capacity_exceeded, then reject in the aggregate (not in the HTTP handler).
```

```
should: Ward.capacity is an int. A Capacity value object would make 0/-1 unrepresentable — follow-up is fine if this PR is already about the reject path.
```

```
nit: prefer patients over pts in the log field name.
```

Rules:

- Comment on the line that should change, not a nearby bystander.
- Questions are ok when you lack context: `question: is ESI-1 meant to bypass this cap?` — not a fake blocker.
- No sarcasm. No "this is messy" without a concrete fix.
- If you wrote a patch in your head, offer it as a suggestion diff, not a lecture.

GitHub suggestion:

````
```suggestion
if ward.IsFull() {
    return ErrWardFull
}
```
````

---

## 5. Review outcomes

| Outcome | When |
|---------|------|
| **Approve** | Intent met, tests pin it, no blockers. Nits may remain. |
| **Request changes** | At least one blocker or unaddressed should-fix. |
| **Comment only** | You reviewed part of it, or you need the author to answer a question first. |

Approve is a statement that **you** would ship this. Do not approve code you did not read. Do not request changes on nits alone.

After the author pushes: re-review the **delta**, not the whole PR from scratch, unless the intent moved.

---

## 6. Author: responding

- Reply to every blocker. "Fixed in <sha>" or "Won't: <reason + ADR/issue>".
- Do not force-push over commits the reviewer already commented on unless the team agreed (rebase-on-merge is fine at the end).
- Do not hide a design change inside "address review comments". Call it out in a new PR description section.
- When you disagree: one short technical argument, then follow the team's decision path. Escalation is an ADR, not a 40-comment thread.

---

## 7. Merge bar (SE)

Ready to merge when:

- [ ] CI on this branch is green (you do not override a red build to "just ship").
- [ ] Required engineering review is Approve.
- [ ] Issue link is real; changelog/commit type matches the diff.
- [ ] QC/SRE/SecOps gates, if they exist on the repo, are **their** jobs — ping those roles, do not impersonate them in this review.

**Propose, do not merge.** Report that the bar is met and wait. Merging is the user's (or a designated maintainer's) action. An agent clicking Merge is out of scope for this skill.

Revert plan: the PR should reverse cleanly. If it needs a forward-fix only, say so in the description.

---

## Anti-patterns

| Smell | Fix |
|-------|-----|
| 2k-line "misc" PR | Split by intent before review starts |
| Review that only lints | Leave nits; look at tests and invariants |
| LGTM without opening the diff | Not a review |
| Relitigating an accepted ADR | Link the ADR and move on |
| Blocking on coverage % | QC gate, not this skill |
| Author and sole approver on a risky path | Get a second engineer |
