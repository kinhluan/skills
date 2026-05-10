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
...

## 🔄 Session Evolution Protocol (Living Knowledge)
`WORKSPACE.md` is not static; it must evolve after every research session. The Agent is responsible for:

1.  **State Updates:** Move the "Current Milestone" forward as tasks are completed.
2.  **Insight Logging:** Add a `## 🧠 Recent Insights` section to `WORKSPACE.md` to capture new findings, rejected hypotheses, or architecture discoveries.
3.  **Dependency Mapping:** If a new library, submodule, or external dataset is introduced, update the `🗺 Path Mapping`.
4.  **Closing Ritual:** Before ending a session, the Agent MUST propose a diff for `WORKSPACE.md` summarizing:
    - What was achieved.
    - What new "Knowledge Artifacts" were created.
    - What the next logical research step is.

## 🚀 Initialization Workflow
1. **Discovery:** Scan root for `docs/`, `research/`, `tests/`, or `.gitmodules`.
2. **Mapping:** Create or update `WORKSPACE.md` with discovered paths and submodule roles.
3. **Memory Linkage:** Instruct sub-agents: *"Read WORKSPACE.md for project paths and recent insights, then cross-reference with MEMORY.md for relevant lessons learned, adhering to the Hierarchy of Authority."*
4. **Evolution:** Ensure `WORKSPACE.md` is updated with any new knowledge gained during the task execution.
