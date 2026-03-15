# 🚀 Multi-Agent Skills Repository

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: skills.sh](https://img.shields.io/badge/Format-skills.sh-green.svg)](https://skills.sh)

A professional collection of modular, self-contained skills for AI coding agents (Gemini, Claude, Cursor, Qwen). This repository follows the **Design-to-Code Sync** philosophy, ensuring architectural diagrams stay aligned with actual codebase reality.

## 📦 Installation

Install any skill directly using the [skills.sh](https://skills.sh) CLI:

```bash
# Add the entire repository
npx skills add luan.bui/skills
```

## 🏗 Featured: C4 Model & DDD Architecture Set
The centerpiece of this repository is a specialized architecture toolkit designed for professional architects and developers, heavily influenced by **Domain-Driven Design (DDD)** principles and Martin Fowler's "heart of software" philosophy.

👉 **[Read the C4 Model & DDD Mapping Guide](./docs/ddd-c4-mapping.md)**

| Category | Level | Skill | Focus |
|:---|:---|:---|:---|
| **Hub** | - | [c4-model](./.agent-skills/c4-model) | Navigation, Anti-patterns, and Stakeholder mapping |
| **Strategic** | L1 | [ddd-core](./.agent-skills/ddd-core) | Event Storming, Bounded Contexts, and Subdomains |
| **Tactical** | L3/L4 | [ddd-tactical](./.agent-skills/ddd-tactical) | Rich Domain Models, Scoring Rubric (0-10) |
| **Containers** | L2 | [c4-level2-container](./.agent-skills/c4-level2-container) | Infrastructure & Deployment mapping (Docker/K8s) |
| **Patterns** | - | [ddd-patterns](./.agent-skills/ddd-patterns) | Advanced: CQRS, Event Sourcing, Outbox, ACL |

---

## 📚 Full Skill Library

| Category | Skill | Description |
|:---|:---|:---|
| **Architecture** | [c4-model](./.agent-skills/c4-model) | Professional C4 Architecture Hub |
| | [ddd-core](./.agent-skills/ddd-core) | Strategic DDD Hub & Workshop |
| | [ddd-tactical](./.agent-skills/ddd-tactical) | Tactical DDD with Scoring Rubric |
| | [ddd-patterns](./.agent-skills/ddd-patterns) | Advanced DDD Integration Patterns |
| **Development** | [python-dev](./.agent-skills/python-development) | Best practices, patterns, and PEP8 standards. |
| | [js-ts-dev](./.agent-skills/javascript-typescript) | Modern JS/TS development guidelines. |
| **DevOps** | [docker](./.agent-skills/docker-containerization) | Containerization patterns and optimization. |
| | [kubernetes](./.agent-skills/kubernetes-orchestration) | K8s orchestration and cloud-native patterns. |
| **Security** | [security](./.agent-skills/security-analysis) | SAST, OWASP, and vulnerability auditing. |
| **Research** | [scheduling](./.agent-skills/scheduling-algorithms) | GA-VNS, ACO, and distributed scheduling. |
| | [federated-ml](./.agent-skills/federated-learning-dqn) | Privacy-preserving FL + DQN for healthcare. |

## 📂 Repository Structure

```text
skills/
├── .agent-skills/      # SOURCE: Core SKILL.md and SKILL.toon files
├── dist/               # DISTRIBUTION: Packaged .skill files for sharing
├── docs/               # Documentation and architectural guides
├── skills.json         # Central manifest for all skills
├── Makefile            # Automation for packaging and validation
├── GEMINI.md           # Instructional context for AI Agents
└── LICENSE             # MIT License
```

## ⚙️ Automation & Development

This repository uses a `Makefile` to simplify skill management:

- `make validate`: Check all skills for YAML and structural errors.
- `make package`: Pack all skills from `.agent-skills/` into `dist/*.skill`.
- `make clean-dist`: Wipe the distribution folder.

## 🎯 Platform Support

- **Gemini CLI**: Automatically discovers context via `GEMINI.md`.
- **Claude Code**: Add `.agent-skills/` to your skill sources.
- **Cursor**: Use rules from `.cursor/rules/`.
- **Qwen Code**: Configure via `.qwen/settings.json`.

## 👥 Author

- **Luân B.** - [luanbhk@gmail.com](mailto:luanbhk@gmail.com)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
