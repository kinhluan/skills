# PR Author Guide

A reviewable PR gets a real review. An unreviewable one gets a rubber stamp or stalls.

## Before Opening

**Size:** one intent. If the description needs "and also", split it. A reviewer should be able to hold the change in their head in one sitting (typically under 400 lines of real code, excluding lockfiles).

**Branch:** `type/short-topic` (`feat/`, `fix/`, `refactor/`, `chore/`). Avoid `misc-fixes`.

**Commits:** Conventional Commits, one logical change per commit when bisect matters.

```text
feat(ward): refuse allocate when capacity is full

Closes #142
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`. Mark breaking changes with `feat!:` or a `BREAKING CHANGE:` footer.

## Description Template

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

## Self-Review Checklist

- [ ] Tests exist for the new behavior and fail without the change.
- [ ] No secrets, credentials, or accidental lockfile churn.
- [ ] Public APIs and types match the domain language.
- [ ] Domain code does not import adapters or frameworks.
- [ ] The PR reverts cleanly, or the description states that only a forward-fix is possible.

## Responding to Review

- Reply to every blocker: "Fixed in `<sha>`" or "Won't: `<reason + ADR/issue>`".
- Do not force-push over commits a reviewer already commented on unless the team agreed; squashing at merge time is fine.
- Do not hide a design change inside "address review comments". Call it out in the description.
- When you disagree, give one short technical argument, then follow the team's decision path. Escalate with an ADR, not a long comment thread.

## Merge Bar

Ready when:

- [ ] CI on the branch is green.
- [ ] Required review is `Approve`.
- [ ] The issue link is real and the commit type matches the diff.
- [ ] Quality, security, and operations gates that exist on the repository have been run by their owners.

Report that the bar is met and wait. Merging is the user's or a designated maintainer's action.
