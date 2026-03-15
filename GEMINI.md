# GEMINI.md - Skills Repository Context

This directory is a publishable skills repository for AI coding agents (Gemini, Claude, Qwen, Cursor), following the [skills.sh](https://skills.sh) standard.

## 📁 Directory Overview

This repository contains modular, self-contained "skills" that provide specialized knowledge, workflows, and guidelines for AI agents. These skills transform general-purpose agents into specialized experts in domains like DevOps, Security, Research, and Software Architecture.

## 🏗 Repository Structure

- **`.agent-skills/`**: The core directory containing all skill source definitions.
  - Each sub-directory (e.g., `python-development/`) represents a single skill source.
  - **`SKILL.md`**: The primary instruction file for the AI agent.
- **`dist/`**: The distribution directory containing packaged `*.skill` files. Use these for sharing or installing directly.
- **`skills.json`**: The central manifest file listing all available skills.

## 🛠 Available Skills

| Category | Skills |
| :--- | :--- |
| **Product & Biz** | `business-product-leadership` |
| **Development** | `python-development`, `javascript-typescript` |
| **DevOps** | `docker-containerization`, `kubernetes-orchestration` |
| **Security** | `security-analysis` |
| **Research** | `academic-research-excellence`, `scheduling-algorithms`, `mlfq-scheduling-expert`, `federated-learning-dqn` |
| **Architecture** | `c4-model`, `c4-level1-context`, `c4-level2-container`, `c4-level3-component`, `c4-level4-code`, `ddd-core`, `ddd-tactical`, `ddd-patterns` |

## 🚀 Usage & Integration

### For AI Agents (Gemini/Claude/Qwen)
- Agents should look into `.agent-skills/` to discover specialized procedural knowledge.
- The `SKILL.md` files should be treated as foundational mandates for specific tasks.

### Tool Integration
- **Cursor**: Reference `.cursor/README.md` for rule application.
- **Qwen Code**: Configure the source path to `./.agent-skills`.
- **Claude Code**: Add the `.agent-skills` path to the tool's settings.

## 📝 Maintenance Guidelines

1.  **New Skill Creation**: 
    - Use the `init_skill.py` script (if available in the skill-creator toolkit) to bootstrap the directory.
    - Ensure `SKILL.md` has clear triggers in the description.
    - **Crucial**: Update `skills.json` after adding a new skill to ensure it's discoverable.
2.  **Validation**: Run validation scripts (e.g., `package_skill.py`) to ensure YAML frontmatter and directory structures are correct.
3.  **Packaging**: Use the packaging tools to generate `.skill` files for distribution.

## ⚠️ Current TODOs
- [ ] Update `skills.json` to include the recently added `c4-model` and its specialized level skills.
- [ ] Ensure all `.skill` packages are up-to-date with the latest content in `.agent-skills/`.
