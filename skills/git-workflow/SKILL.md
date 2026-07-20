---
name: git-workflow
description: Design or apply a Git collaboration workflow, including trunk-based development, release branches, branch naming, commits, and tags. Use when a user is choosing a branching model, documenting repository conventions, preparing commits, or planning releases.
metadata:
  tags: ["git", "branching", "commits", "releases", "collaboration"]
---

# Git Workflow

Choose the smallest workflow that satisfies the repository's release, review, and support constraints. Inspect existing contribution docs and branch protection before proposing a new convention.

## Workflow

1. Establish constraints:
   - release cadence and supported versions;
   - CI reliability and deployment automation;
   - review or regulatory gates;
   - team size, time zones, and merge frequency.
2. Inspect current conventions with read-only Git commands.
3. Select a model:
   - Prefer trunk-based development with short-lived branches for continuous delivery.
   - Use release branches when multiple supported versions or scheduled stabilization require them.
   - Use a GitFlow-style `develop` branch only when its extra integration stage solves a documented constraint.
4. Document branch, commit, review, merge, and tag rules together.
5. Test the workflow on one representative change before rolling it out.

## Branch Rules

Follow repository-local rules first. When none exist, use:

```text
<type>/<optional-issue>-<short-description>
```

Keep branches short-lived and delete them after merge. Common types are `feat`, `fix`, `docs`, `test`, `refactor`, and `chore`. Do not invent an issue identifier.

## Commit Rules

Write an imperative subject that states the outcome. Explain the reason and important tradeoffs in the body. Use Conventional Commits only when the repository already uses them or release automation depends on them.

```text
fix(router): rank specific security routes first

The previous first-match strategy hid container-security behind
generic Docker and security matches.
```

Separate unrelated changes. Do not rewrite shared history, force-push, create tags, or publish commits unless the user explicitly requests that external mutation.

## Release Rules

- Derive the version from the repository's documented policy.
- Verify that the tagged commit passed required checks.
- Prefer annotated tags for human-created releases.
- Treat a tag or published release as an external mutation requiring explicit user intent.
- For hotfixes, record how the fix returns to every maintained branch.

## Output

Return:

1. constraints and current-state evidence;
2. recommended model with rejected alternatives;
3. concrete branch, commit, merge, and release rules;
4. migration steps and rollback;
5. unresolved decisions.

## Sources

- [Trunk Based Development](https://trunkbaseddevelopment.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Git documentation](https://git-scm.com/docs)
