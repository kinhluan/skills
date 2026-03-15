# Contributing to Multi-Agent Skills

Thank you for your interest in contributing to this repository! We aim to build the most comprehensive collection of skills for **Product-Led Engineering**.

## 🚀 How to Contribute

1.  **Fork** the repository on GitHub.
2.  **Clone** your fork locally.
3.  **Create a new branch** for your skill: `git checkout -b feat/my-new-skill`.
4.  **Develop your skill** in the `.agent-skills/` directory.
5.  **Validate and Package** your skill using the `Makefile`.
6.  **Commit and Push** your changes.
7.  **Submit a Pull Request** to the `main` branch.

## 📝 Skill Standards

To maintain high quality, every skill must adhere to the following standards:

### 1. Directory Structure
```text
.agent-skills/my-skill/
├── SKILL.md    # Mandatory: Primary instructions
└── SKILL.toon  # Mandatory: Summarized version for context efficiency
```

### 2. SKILL.md Requirements
- Must contain valid **YAML frontmatter** with `name`, `description`, and `metadata`.
- Description must be clear and include "triggers" (when the AI should use the skill).
- Use **Professional Tone** and focus on actionable workflows.

### 3. SKILL.toon Requirements
- Mirror the content of `SKILL.md` but in a highly condensed format.
- Focus on key patterns, code snippets, and rules.

## ⚙️ Development Workflow

We use a `Makefile` to ensure all skills are valid before they are merged.

### Validate your skills:
```bash
make validate
```
*Your skill must pass validation (✅ Skill is valid!) to be accepted.*

### Package your skills:
```bash
make package
```
*This updates the `dist/` folder with your packaged `.skill` file.*

## 🤝 Code of Conduct

- Be respectful to other contributors.
- Focus on providing value to the AI community.
- Ensure all content is technically accurate and follows modern best practices.

## 👥 Need Help?

If you have questions about creating a new skill, feel free to open an Issue or contact the author: **Luân B.** ([luanbhk@gmail.com](mailto:luanbhk@gmail.com)).
