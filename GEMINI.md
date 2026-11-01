# Gemini CLI Repository Context

This repository is a Gemini CLI extension and portable Agent Skills collection.

Gemini discovers the canonical skill sources directly through the real `skills/` directory. Synchronize release artifacts after edits:

```bash
make sync-manifest
make package
make check
```

## Rules

- Each published skill has one authoritative `SKILL.md`.
- Keep `SKILL.md` below 500 lines and link detailed references directly.
- Do not add `SKILL.toon` or installer-generated lock state.
- Add or update router tests for changed activation behavior.
- Verify time-sensitive APIs, versions, metrics, and venue policies from current primary sources.
- Keep release versions consistent across `skills.json`, Claude metadata, marketplace metadata, and `gemini-extension.json`.

See [README.md](README.md) for installation and [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.
