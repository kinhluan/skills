# Skills Repository - Project Context

## Project Overview

This is a **publishable skills repository** for AI coding agents, following the [skills.sh](https://skills.sh) standard. It contains a curated collection of development guidelines, best practices, and domain knowledge that can be consumed by AI assistants like Qwen Code, Claude Code, and Cursor.

**Purpose:** Provide reusable, standardized skill definitions that enhance AI agent capabilities across multiple domains including software development, DevOps, security, and research.

**License:** MIT

## Repository Structure

```
skills/
├── .agent-skills/          # Main skills directory (skills.sh standard)
│   ├── c4-level1-context/  # C4 System Context diagrams
│   ├── c4-level2-container/# C4 Container diagrams
│   ├── c4-level3-component/# C4 Component diagrams
│   ├── c4-level4-code/     # C4 Code-level diagrams
│   ├── c4-model/           # C4 Model navigation hub
│   ├── docker-containerization/
│   ├── federated-learning-dqn/
│   ├── javascript-typescript/
│   ├── kubernetes-orchestration/
│   ├── python-development/
│   ├── scheduling-algorithms/
│   └── security-analysis/
├── .qwen/                  # Qwen Code configuration
├── .claude/                # Claude Code configuration
├── .cursor/                # Cursor rules
├── skills.json             # Skills manifest (skills.sh format)
├── README.md               # User-facing documentation
└── QWEN.md                 # This file - AI agent context
```

## Available Skills

| Skill | Domain | Tags |
|-------|--------|------|
| `python-development` | Backend | python, programming, backend |
| `javascript-typescript` | Frontend/Backend | javascript, typescript, frontend, backend |
| `docker-containerization` | DevOps | docker, containers, devops, deployment |
| `kubernetes-orchestration` | DevOps/Cloud | kubernetes, k8s, orchestration, devops, cloud |
| `security-analysis` | Security | security, sast, vulnerability, audit, owasp |
| `scheduling-algorithms` | Research/Algorithms | scheduling, algorithms, optimization, parallel-computing |
| `federated-learning-dqn` | ML/Research | federated-learning, dqn, reinforcement-learning, privacy, healthcare |
| `c4-model` | Architecture | c4, architecture, diagrams |

## Skill Format

Each skill is a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: skill-name
description: What this skill does
tags: [tag1, tag2]
---
```

Followed by Markdown content with sections:
- **When to Use** - Trigger conditions for applying the skill
- **Guidelines** - Best practices, patterns, and procedures
- **Examples** - Code snippets and implementations
- **Resources** - Links to external documentation

## Building and Running

This is a **documentation/knowledge repository** - no build process required.

### Installation (for use with skills.sh)

```bash
# Via npx
npx skills add luan.bui/skills

# Local clone
git clone https://github.com/luan.bui/skills.git
npx skills add ./skills
```

### Platform Configuration

**Qwen Code:** Skills are auto-discovered from `.agent-skills/` directory.

**Claude Code:** Add to `~/.claude/settings.json`:
```json
{
  "skills": {
    "sources": ["./path/to/skills/.agent-skills"]
  }
}
```

**Cursor:** Copy `.cursor/rules/*.mdc` to your project or create symlinks.

## Development Conventions

### Creating New Skills

1. Create a new folder in `.agent-skills/` with kebab-case naming
2. Add `SKILL.md` with proper YAML frontmatter
3. Update `skills.json` manifest with new skill entry
4. Test discovery with `npx skills add`

### Skill Content Guidelines

- Use clear, actionable language in guidelines
- Include both vulnerable and secure code examples where applicable
- Reference official documentation in Resources section
- Keep skills focused on a single domain or topic
- Use tables for metrics, comparisons, and severity levels

### File Naming

- Skill directories: `kebab-case` (e.g., `python-development`)
- Skill files: `SKILL.md` (uppercase, consistent across all skills)
- Additional resources: lowercase with hyphens (e.g., `validation-checklist.md`)

## Key Files Reference

| File | Purpose |
|------|---------|
| `skills.json` | Skills manifest for skills.sh - defines name, version, and skill entries |
| `README.md` | User-facing documentation with installation and usage instructions |
| `QWEN.md` | This file - provides context for AI agents |
| `.gitignore` | Excludes dependencies, build artifacts, secrets, and IDE files |
| `.agent-skills/*/SKILL.md` | Individual skill definitions with guidelines and examples |

## Domain Coverage

### Software Development
- Python programming patterns and project structure
- JavaScript/TypeScript best practices and strict mode
- C4 model for software architecture documentation

### DevOps & Cloud
- Docker multi-stage builds and security practices
- Kubernetes deployment patterns and orchestration
- Container optimization and .dockerignore

### Security
- OWASP Top 10 vulnerability analysis
- SAST (Static Application Security Testing) procedures
- Privacy taint analysis (sources → sinks)
- Severity assessment (Critical/High/Medium/Low)

### Research & Algorithms
- Scheduling algorithms (HEFT, Min-Min, GA, VNS, ACO)
- Metaheuristic optimization techniques
- Hybrid algorithm design (GA-VNS, ACO-GA)

### Machine Learning
- Federated learning architectures (FedAvg)
- Deep Q-Networks (DQN) for reinforcement learning
- Privacy-preserving ML (differential privacy, secure aggregation)
- Healthcare scheduling applications

## Related Documentation

- **Extensions:** Check `.qwen/extensions/` for additional agent capabilities (security analysis, code review)
- **C4 References:** See `c4-model/references/` for templates and validation checklists
- **Configuration:** Platform-specific configs in `.claude/`, `.cursor/`, `.qwen/`
