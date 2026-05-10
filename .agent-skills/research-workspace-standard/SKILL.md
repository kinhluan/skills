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

This skill establishes a unified structure for research data, enabling different agents (Researcher, Writer, Reviewer) to collaborate using shared artifacts.

## 🎯 Triggers
- "khởi tạo thư mục nghiên cứu"
- "setup research workspace"
- "organize my PhD files"

## 🏛 Directory Structure (Standard)
```text
/research/
├── papers/            # Downloaded PDFs and .bib files
├── notes/             # Raw observations, Gap Matrix, summaries
├── artifacts/         # Experiment code, logs, and datasets
├── drafts/            # Manuscript drafts (Markdown/LaTeX)
└── workspace.json     # Metadata tracking the current research state
```

## 🔄 Artifact Contracts (I/O)
Skills communicate via these files in `/research/notes/`:
- **`sota-matrix.md`**: Output of `sota-survey`.
- **`rq-statement.md`**: Output of `research-question`.
- **`protocol.json`**: Output of `research-design`.
- **`results.csv`**: Output of `experiment-tracking`.

## 🚀 Initialization Workflow
1. **Create Folders:** Initialize the 5 core directories.
2. **Setup Tracking:** Create `workspace.json` with topic and current milestone.
3. **Agent Persona:** Set the global instruction: *"Always look for research artifacts in the /research/ folder before starting a task."*
