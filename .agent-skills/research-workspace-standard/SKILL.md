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
Use this when starting a new project. Create:
```text
/research/
├── papers/            # PDFs and .bib files
├── notes/             # Gap Matrix, summaries, observations
├── artifacts/         # Experiment code, logs, results
├── drafts/            # Markdown/LaTeX manuscripts
└── WORKSPACE.md       # Central index & state tracking
```

### Mode 2: Virtual (Brownfield Discovery)
Use this for existing codebases. Instead of moving files, create a **`WORKSPACE.md`** at the root to map logical research roles to existing paths:

```markdown
# Research Workspace Map
- **Architecture:** `docs/architecture/`, `*.c4`, `*.puml`
- **Documentation:** `README.md`, `wiki/`
- **Experiments:** `tests/benchmarks/`, `notebooks/`, `scripts/`
- **State:** [Current Research Milestone]
```

## 🔍 Smart Discovery Heuristics
When in an existing codebase, the Agent must:
1. **Locate Architecture:** Search for C4 models or design docs (`grep -r "System Context" .`).
2. **Identify Experiments:** Scan for performance logs or benchmark scripts.
3. **Trace Methodology:** Look for `CONTRIBUTING.md` or `DEVELOPMENT.md` to understand system constraints.

## 🔄 Artifact Contracts (I/O)
Regardless of the mode, skills communicate via these core artifacts (mapped in `WORKSPACE.md`):
- **`sota-matrix.md`**: Systematic comparison of current works.
- **`rq-statement.md`**: Formal research questions and hypotheses.
- **`protocol.json`**: Experimental setup and parameters.
- **`results.csv`**: Raw output from experiments.

## 🚀 Initialization Workflow
1. **Discovery:** Scan the root for `docs/`, `research/`, or `tests/`.
2. **Mapping:** Create or update `WORKSPACE.md` with the discovered paths.
3. **Agent Setup:** Instruct sub-agents: *"Consult WORKSPACE.md to find relevant artifacts before starting."*
