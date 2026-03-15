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

The centerpiece of this repository is a specialized architecture toolkit designed for **Product Managers, Architects, and Developers**. It follows the **Design-to-Code Sync** philosophy and **Domain-Driven Design (DDD)** principles.

👉 **[Read the C4 Model & DDD Mapping Guide](./docs/ddd-c4-mapping.md)**

### For Product Managers & Founders 🎯

| Workflow | Skill | Outcome |
|:---|:---|:---|
| **Strategy & MVP** | [business-product-leadership](./.agent-skills/business-product-leadership) | LMR, JTBD, Ship != Release |
| **Discovery** | [ddd-core](./.agent-skills/ddd-core) | Event Storming → Domain Events, Subdomains |
| **Scoping** | [c4-level1-context](./.agent-skills/c4-level1-context) | System Context + User Journeys (Tech-free!) |
| **Roadmapping** | [c4-model](./.agent-skills/c4-model) | Stakeholder mapping, anti-patterns avoidance |

### Full Architecture Toolkit

| Category | Level | Skill | Audience |
|:---|:---|:---|:---|
| **Business Strategy**| - | [business-product-leadership](./.agent-skills/business-product-leadership) | Product Owners, Founders |
| **DDD Strategic** | - | [ddd-core](./.agent-skills/ddd-core) | PM, Architects |
| **DDD Tactical** | - | [ddd-tactical](./.agent-skills/ddd-tactical) | Developers |
| **DDD Patterns** | - | [ddd-patterns](./.agent-skills/ddd-patterns) | Architects |
| **C4 Hub** | - | [c4-model](./.agent-skills/c4-model) | Everyone |
| **C4 Level 1** | Context | [c4-level1-context](./.agent-skills/c4-level1-context) | **PM**, Executives |
| **C4 Level 2** | Container | [c4-level2-container](./.agent-skills/c4-level2-container) | Architects, DevOps |
| **C4 Level 3** | Component | [c4-level3-component](./.agent-skills/c4-level3-component) | Developers |
| **C4 Level 4** | Code | [c4-level4-code](./.agent-skills/c4-level4-code) | Developers |

---

## 📚 Full Skill Library

### 📈 Business & Product Strategy

| Category | Skill | Description |
|:---|:---|:---|
| **Leadership** | [business-product-leadership](./.agent-skills/business-product-leadership) | Strategic frameworks: LMR, JTBD, Ship != Release. |

### 🏗 Architecture & Design (DDD + C4)

| Category | Skill | Description |
|:---|:---|:---|
| **DDD** | [ddd-core](./.agent-skills/ddd-core) | Strategic DDD: Event Storming, Subdomains, Bounded Contexts. |
| | [ddd-tactical](./.agent-skills/ddd-tactical) | Tactical DDD: Aggregates, Value Objects, scoring rubric (0-10). |
| | [ddd-patterns](./.agent-skills/ddd-patterns) | Advanced: CQRS, Event Sourcing, Outbox, ACL. |
| **C4 Model** | [c4-model](./.agent-skills/c4-model) | Navigation hub, anti-patterns, stakeholder mapping. |
| | [c4-level1-context](./.agent-skills/c4-level1-context) | System Context & User Journeys (PM-friendly, tech-free). |
| | [c4-level2-container](./.agent-skills/c4-level2-container) | Infrastructure & Deployment (Docker/K8s). |
| | [c4-level3-component](./.agent-skills/c4-level3-component) | Internal Code Structure & Folder mapping. |
| | [c4-level4-code](./.agent-skills/c4-level4-code) | Implementation details (UML Class & ER Diagrams). |

### 💻 Development

| Category | Skill | Description |
|:---|:---|:---|
| **Languages** | [python-dev](./.agent-skills/python-development) | Best practices, patterns, and PEP8 standards. |
| | [js-ts-dev](./.agent-skills/javascript-typescript) | Modern JS/TS development guidelines. |

### ☁️ DevOps & Cloud

| Category | Skill | Description |
|:---|:---|:---|
| **Containers** | [docker](./.agent-skills/docker-containerization) | Containerization patterns and optimization. |
| **Orchestration** | [kubernetes](./.agent-skills/kubernetes-orchestration) | K8s orchestration and cloud-native patterns. |

### 🔒 Security

| Category | Skill | Description |
|:---|:---|:---|
| **Analysis** | [security](./.agent-skills/security-analysis) | SAST, OWASP, and vulnerability auditing. |

### 🔬 Research & ML

| Category | Skill | Description |
|:---|:---|:---|
| **Algorithms** | [scheduling](./.agent-skills/scheduling-algorithms) | GA-VNS, ACO, HEFT, Min-Min for distributed scheduling. |
| **ML** | [federated-ml](./.agent-skills/federated-learning-dqn) | Privacy-preserving FL + DQN for healthcare. |

## 📂 Repository Structure

```text
skills/
├── .agent-skills/      # SOURCE: Core SKILL.md and SKILL.toon files
├── dist/               # DISTRIBUTION: Packaged .skill files for sharing
├── docs/               # Documentation and mapping guides
├── skills.json         # Central manifest for all skills
├── Makefile            # Automation for packaging and validation
├── README.md           # This file - User documentation
├── GEMINI.md           # Context for Gemini CLI agent
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
