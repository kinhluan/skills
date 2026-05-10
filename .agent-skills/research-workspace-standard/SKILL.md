---
name: research-workspace-standard
description: Standardized directory structure and artifact management for agentic research. Ensures consistent data flow across all agent platforms (Gemini, Claude, Antigravity).
metadata:
  version: 1.0.0
  triggers:
    - "Setup research workspace"
    - "Organize research artifacts"
    - "Research data structure"
    - "Standardize my PhD project"
---

# Research Workspace Standard

This skill establishes a unified environment for research data, enabling agents (Researcher, Writer, Reviewer) to collaborate using either a structured physical directory or a "Smart Discovery" virtual map of an existing codebase.

## 🎯 Triggers
- "khởi tạo thư mục nghiên cứu"
- "setup research workspace"
- "organize my PhD files"
- "đọc cấu trúc codebase để nghiên cứu"
- "map existing docs to research"

## 🏛 Workspace Modes

### Mode 1: Physical (Greenfield)
...

### Mode 2: Virtual (Brownfield & Monorepo)
Use this for existing codebases or Monorepos. Create a **`WORKSPACE.md`** at the root to map logical research roles. 

#### 📦 Monorepo & Submodule Support
If the project uses submodules or a monorepo structure (e.g., Nx, Turborepo), the `WORKSPACE.md` must explicitly map them:
```markdown
# Research Workspace Map
- **Core Engine:** `packages/core/`, `.gitmodules:engine-v1`
- **Sub-module Research:** `submodules/research-utils/`
- **Cross-Linkage:** `../neighbor-project/research/notes/` (Relative path to related research)
```

## 🔍 Smart Discovery Heuristics
When in an existing codebase, the Agent must:
1. **Locate Architecture:** Search for C4 models, design docs, or `*.gitmodules`.
2. **Identify Experiments:** Scan for performance logs, benchmark scripts, or `tests/`.
3. **Cross-Project Context:** If a neighboring directory contains a `WORKSPACE.md`, read its **State** section to establish research continuity.

## 🔄 Artifact Contracts (I/O)
Regardless of the mode, skills communicate via these core artifacts (mapped in `WORKSPACE.md`):
- **`sota-matrix.md`**: Systematic comparison of current works (Output of `sota-survey`).
- **`rq-statement.md`**: Formal research questions (Output of `research-question`).
- **`protocol.json`**: Experimental setup (Output of `research-design`).
- **`results.csv`**: Raw results (Output of `experiment-tracking`).

## ⚖️ Decision Hierarchy (Lex Specialis)
To ensure consistency, the Agent must resolve conflicts using this priority ladder:
1. **Tier 1: `WORKSPACE.md` (Highest)** — Project-specific paths, state, and domain constraints.
2. **Tier 2: `GEMINI.md` / `CLAUDE.md`** — Repository-wide shared conventions and mandates.
3. **Tier 3: `MEMORY.md`** — Personal preferences, cross-project lessons, and style.
4. **Tier 4: System Defaults (Lowest)** — General AI behavior.

*Rule: If a project-specific constraint in WORKSPACE.md contradicts a general preference in MEMORY.md, the Tier 1 constraint MUST prevail.*

## 🚀 Initialization Workflow
1. **Discovery:** Scan root for `docs/`, `research/`, `tests/`, or `.gitmodules`.
2. **Mapping:** Create or update `WORKSPACE.md` with discovered paths and submodule roles.
3. **Memory Linkage:** Instruct sub-agents: *"Read WORKSPACE.md for project paths, then cross-reference with MEMORY.md for relevant lessons learned, adhering to the Hierarchy of Authority."*
