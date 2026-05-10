# CLAUDE.md - Workspace Mandates

This file serves as the source of truth for Claude Code, synchronizing with `GEMINI.md` to provide consistent repository-wide mandates.

## 🏗 Repository Structure
- Follows the [skills.sh](https://skills.sh) standard.
- Core instructions reside in `.agent-skills/`.
- Packaged artifacts are located in `dist/`.

## 📜 Coding & Research Standards
- **Tier 2 Authority:** Treat this file and `GEMINI.md` as the primary source for workspace conventions.
- **Research Workflow:** Adhere to the `research-workspace-standard`. Always check `WORKSPACE.md` for project-specific paths before execution.
- **Vietnamese Orthography:** Follow `vietnamese-writing-standard` (Sentence case, no unnecessary caps).

## 🚀 Key Commands
- `make package`: Update all `.skill` files in `dist/`.
- `make validate`: Check skill integrity.

> *Note: For Gemini CLI specific settings, refer to `GEMINI.md`.*
