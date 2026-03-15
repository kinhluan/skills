# 🚀 Multi-Agent Skills: Product-Led Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: skills.sh](https://img.shields.io/badge/Format-skills.sh-green.svg)](https://skills.sh)

A professional collection of modular skills for AI coding agents (Gemini, Claude, Cursor, Qwen). This repository is built on the philosophy of **Product-Led Engineering**: bridging the gap between business strategy and technical execution.

## 💡 Core Philosophy

1.  **Design-to-Code Sync:** Architectural diagrams (C4) must reflect the reality of the codebase.
2.  **Domain-Driven Excellence:** The "heart of software" is the domain model (DDD).
3.  **Ship != Release:** Decouple technical deployment from business value delivery.
4.  **Evidence-Based Discovery:** Use Labor Market Research (LMR) and Jobs-To-Be-Done (JTBD) to build what matters.

## 🏗 Featured: The Architect's Toolkit

Designed for **Product Owners, Architects, and Developers** to work in total alignment.

👉 **[Business & Product Leadership Guide](./docs/business-product-leadership.md)** | **[C4 & DDD Mapping Guide](./docs/ddd-c4-mapping.md)**

### For Product Leaders & Founders 🎯
| Phase | Skill | Outcome |
|:---|:---|:---|
| **Strategy** | [business-leadership](./.agent-skills/business-product-leadership) | LMR Validation & JTBD Definition |
| **Discovery** | [ddd-core](./.agent-skills/ddd-core) | Event Storming → Bounded Contexts |
| **Delivery** | [business-leadership](./.agent-skills/business-product-leadership) | Separation of **Ship** vs. **Release** |

### For Architects & Developers 🛠️
| Level | Skill | Focus |
|:---|:---|:---|
| **L1** | [c4-level1-context](./.agent-skills/c4-level1-context) | System Scope & User Journeys (Tech-free) |
| **L2** | [c4-level2-container](./.agent-skills/c4-level2-container) | Infrastructure & Deployment (Docker/K8s) |
| **L3** | [c4-level3-component](./.agent-skills/c4-level3-component) | Internal Code Structure & Folder Mapping |
| **Tactical** | [ddd-tactical](./.agent-skills/ddd-tactical) | Rich Domain Models & Scoring Rubric (0-10) |
| **Advanced** | [ddd-patterns](./.agent-skills/ddd-patterns) | CQRS, Event Sourcing, Outbox, ACL |

---

## 📚 Full Skill Library

### 📈 Business & Strategy
| Skill | Description |
|:---|:---|
| [leadership](./.agent-skills/business-product-leadership) | Strategic frameworks: LMR, JTBD, MVP Planning, Ship != Release. |

### 🏗 Architecture (DDD + C4)
| Skill | Description |
|:---|:---|
| [ddd-core](./.agent-skills/ddd-core) | Strategic DDD: Event Storming, Subdomains, Bounded Contexts. |
| [ddd-tactical](./.agent-skills/ddd-tactical) | Tactical DDD: Aggregates, Value Objects, Scoring Rubric. |
| [ddd-patterns](./.agent-skills/ddd-patterns) | Advanced: CQRS, Event Sourcing, Outbox, ACL. |
| [c4-model](./.agent-skills/c4-model) | Navigation hub, anti-patterns, stakeholder mapping. |
| [c4-level1-context](./.agent-skills/c4-level1-context) | System Context & User Journeys (PM-friendly). |
| [c4-level2-container](./.agent-skills/c4-level2-container) | Infrastructure & Deployment Mapping. |
| [c4-level3-component](./.agent-skills/c4-level3-component) | Internal Code Structure & Folder Mapping. |
| [c4-level4-code](./.agent-skills/c4-level4-code) | Implementation details (UML & ER Diagrams). |

### 💻 Technology & Research
| Category | Skills |
|:---|:---|
| **Languages** | [Python](./.agent-skills/python-development), [JS/TS](./.agent-skills/javascript-typescript) |
| **Infrastructure**| [Docker](./.agent-skills/docker-containerization), [Kubernetes](./.agent-skills/kubernetes-orchestration) |
| **Security** | [Security Analysis](./.agent-skills/security-analysis) |
| **Research/ML** | [Scheduling Algorithms](./.agent-skills/scheduling-algorithms), [Federated RL](./.agent-skills/federated-learning-dqn) |

---

## 📦 Installation

```bash
npx skills add luan.bui/skills
```

## ⚙️ Automation & Maintenance

- `make validate`: Ensure all skills follow the [skills.sh](https://skills.sh) standard.
- `make package`: Build `.skill` distribution files in `dist/`.

## 👥 Author

- **Luân B.** - [luanbhk@gmail.com](mailto:luanbhk@gmail.com)

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
