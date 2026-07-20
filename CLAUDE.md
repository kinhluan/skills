# Claude Code Repository Context

This is the `kinhluan-skills` plugin and a portable Agent Skills repository.

## Source of Truth

- Edit `skills/<name>/SKILL.md` and its directly linked resources.
- `skills/` is a real directory so plugin discovery works across operating systems.
- `skills.json` and `dist/*.skill` are generated release surfaces.
- Do not recreate `SKILL.toon` or commit installer-generated `skills-lock.json`.

## Commands

```bash
make sync-manifest
make validate
make test
make package
make check
```

Install development dependencies with `python3 -m pip install -r requirements-dev.txt`.

## Change Rules

- Keep `SKILL.md` below 500 lines; use directly linked `references/` for details.
- Add a route and regression test for every published skill.
- Keep release versions synchronized across all four manifests.
- Rebuild and commit deterministic packages after source changes.
- Preserve unrelated work and do not publish external changes unless requested.

The portable `UserPromptSubmit` hook in `hooks/hooks.json` runs `scripts/skill_router.py`. Router suggestions are hints; skill metadata and the actual task remain authoritative.
