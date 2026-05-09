# GEMINI.md - Skills Repository Context

This directory is a publishable skills repository for AI coding agents (Gemini, Claude, Qwen, Cursor), following the [skills.sh](https://skills.sh) standard.

## 📁 Directory Overview

This repository contains modular, self-contained "skills" that provide specialized knowledge, workflows, and guidelines for AI agents. These skills transform general-purpose agents into specialized experts in domains like DevOps, Security, Research, and Software Architecture.

## 🏗 Repository Structure

- **`.agent-skills/`**: The core directory containing all skill source definitions.
  - Each sub-directory (e.g., `python-development/`) represents a single skill source.
  - **`SKILL.md`**: The primary instruction file for the AI agent.
- **`dist/`**: The distribution directory containing packaged `*.skill` files. These are forced-committed to allow direct installation.
- **`skills.json`**: The central manifest file listing all available skills for the `skills.sh` format.
- **`gemini-extension.json`**: The official manifest for Gemini CLI listing.

## 🛠 Available Skills (v1.1.0)

| Category | Skills |
| :--- | :--- |
| **Strategy & Biz** | `art-of-war-software-engineering`, `business-product-leadership`, `why-strategic-rationale`, `diffusion-release-tracking` |
| **Development** | `python-development`, `javascript-typescript`, `collaborative-engineering-agent`, `dora-core` |
| **DevOps** | `docker-containerization`, `kubernetes-orchestration` |
| **Security** | `security-analysis` |
| **Architecture** | `c4-model`, `c4-level1-context`, `c4-level2-container`, `c4-level3-component`, `c4-level4-code`, `ddd-core`, `ddd-tactical`, `ddd-patterns` |
| **Research (General)**| `scheduling-algorithms`, `federated-learning-dqn`, `academic-research-excellence` |
| **Research (PhD Lifecycle)**| `sota-survey`, `research-question`, `phd-proposal`, `research-design`, `experiment-tracking`, `paper-writing`, `internal-critique`, `publication-strategy`, `defense-prep`, `milestone-tracker` |

## 🚀 Usage & Integration

### Gemini CLI (Official Extension)
The most direct way to install this repository as a Gemini extension:
```bash
gemini extensions install https://github.com/kinhluan/skills
```

### For AI Agents (Manual Loading)
- Agents should look into `.agent-skills/` to discover specialized procedural knowledge.
- The `SKILL.md` files should be treated as foundational mandates for specific tasks.

### Tool Integration
- **Gemini CLI**: To use workspace-specific skills, copy `.agent-skills/` and this `GEMINI.md` into your project's root. For global use, use the `extensions install` command above.
- **Cursor**: Reference `.cursor/README.md` for rule application.
- **Qwen Code**: Configure the source path to `./.agent-skills`.
- **Claude Code**: Add the `.agent-skills` path to the tool's settings.

## 📝 Maintenance Guidelines

1.  **New Skill Creation**: 
    - Use the `init_skill.py` script to bootstrap.
    - Update `skills.json` and ensure `SKILL.md` has clear triggers.
2.  **Packaging**: Run `make package` to generate and update `.skill` files in `dist/`.
3.  **Validation**: Run `make validate` to ensure all skills follow the standard.

## ⚠️ Current TODOs
- [ ] Merge PR #5 into `main` to finalize the 1.1.0 release.
- [ ] Add the `gemini-cli-extension` topic to the GitHub repository.
