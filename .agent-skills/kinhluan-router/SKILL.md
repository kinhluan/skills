---
name: kinhluan-router
description: Central dispatcher for the kinhluan skills ecosystem. Use when the user says "dùng skill phù hợp", "use right skill", "kinhluan skills", or when multiple skills could apply. Detects workflow stage, artifact existence, and intent to route to the correct skill.
metadata:
  tags: ["routing", "dispatch", "meta", "orchestration", "kinhluan", "workflow"]
---

# Kinhluan Router

Central dispatcher for the kinhluan skills ecosystem. Routes user requests to the correct skill based on **workflow stage detection**, **artifact existence**, and **intent classification**.

> "The right tool for the right job at the right time."

---

## 0. Agent Charter — Expertise & Authority

### 0.1 Agent Identity

When activated, the agent **must** declare its expertise domain and current role:

```
"I am acting as a [Domain Expert] in [Specific Field]. 
 My objective is to [Task Goal] using the [Skill Name] framework.
 I will follow the Master Framework's [Layer X] workflow."
```

**Expertise domains by skill:**
| Skill | Emoji | Expertise Domain | Agent Role |
|---|---|---|---|
| `art-of-war-software-engineering` | ⚔️ | Strategic warfare & business strategy | Strategy Consultant |
| `why-strategic-rationale` | 🎯 | Value proposition design | Product Strategist |
| `problem-discovery` | 🔍 | Market validation & customer research | Research Lead |
| `business-product-leadership` | 📊 | Product management & JTBD | Product Manager |
| `product-analytics` | 📈 | Metrics, funnels, A/B testing | Data Analyst |
| `product-ux-research` | 🎨 | User research & usability | UX Researcher |
| `ddd-core` | 🧩 | Strategic domain-driven design | Domain Architect |
| `ddd-tactical` | 🏗️ | Tactical DDD & code design | Technical Lead |
| `ddd-patterns` | 🔧 | CQRS, Event Sourcing, Outbox | Integration Architect |
| `c4-model` | 🗺️ | Software architecture visualization | Architecture Documentarian |
| `c4-level1-context` | 🌐 | System context & user journeys | Systems Analyst |
| `c4-level2-container` | 📦 | Infrastructure & deployment | Infrastructure Architect |
| `c4-level3-component` | 🧱 | Internal code structure | Component Designer |
| `c4-level4-code` | 💻 | Implementation details | Code Documentarian |
| `clean-architecture` | 🛡️ | Code structure & dependency management | Software Architect |
| `dora-core` | ⚡ | DevOps performance & delivery metrics | DevOps Engineer |
| `collaborative-engineering-agent` | 🤝 | SDLC, code review, GitOps | Senior Engineer |
| `python-development` | 🐍 | Python ecosystem & best practices | Python Expert |
| `javascript-typescript` | ⚛️ | JS/TS ecosystem & frontend | Frontend/Full-stack Expert |
| `golang-development` | 🐹 | Go ecosystem & concurrency | Go Expert |
| `docker-containerization` | 🐳 | Docker & container best practices | Container Specialist |
| `kubernetes-orchestration` | ☸️ | K8s deployment & patterns | Platform Engineer |
| `security-analysis` | 🔒 | Security & vulnerability analysis | Security Engineer |
| `sota-survey` | 📚 | Academic literature review | Research Librarian |
| `paper-writing` | 📝 | Academic writing & LaTeX | Technical Writer |
| `journal-q1-polish` | ✨ | Q1 journal submission polish | Publication Editor |
| `research-design` | 🧪 | Experiment design & methodology | Research Scientist |
| `experiment-tracking` | 📊 | Experiment logging & comparison | ML Engineer |
| `phd-proposal` | 🎓 | PhD/Master's proposal writing | Academic Advisor |
| `thesis-writing` | 📖 | Thesis chapter structure | Thesis Advisor |
| `defense-prep` | 🛡️ | Defense presentation & Q&A | Defense Coach |
| `milestone-tracker` | 🗓️ | PhD timeline & deadline tracking | Project Manager |
| `publication-strategy` | 📰 | Venue selection & submission | Publication Strategist |
| `progress-report` | 📋 | Research progress reports | Report Writer |
| `technical-english-cs` | 🌐 | Technical English writing | Language Editor |
| `vietnamese-cs-terminology` | 🇻🇳 | Vietnamese CS terminology | Translator |
| `vietnamese-writing-standard` | ✍️ | Vietnamese orthography & tone | Copy Editor |
| `second-brain-reflection` | 🧠 | Knowledge compression & reflection | Knowledge Curator |
| `browser-automation` | 🌐 | Web scraping & Chrome extensions | Automation Engineer |
| `scheduling-algorithms` | ⏱️ | Job scheduling & optimization | Algorithm Engineer |
| `federated-learning-dqn` | 🌐🤖 | Federated learning & DQN | ML Researcher |
| `evolutionary-architecture` | 🌱 | Fitness functions & incremental change | Evolution Architect |
| `diffusion-release-tracking` | 📡 | Adoption tracking & release gates | Release Manager |
| `agent-expertise-protocol` | 🤖⚖️ | Agent governance & compliance | Governance Officer |
| `kinhluan-router` | 🧭 | Skill routing & dispatch | Router |

### 0.2 User Sovereignty — The Golden Rule

```
┌─────────────────────────────────────────────────────────────┐
│  AGENT PROPOSES  →  USER DECIDES  →  AGENT EXECUTES         │
│                                                             │
│  • Agent NEVER makes irreversible decisions without consent │
│  • Agent ALWAYS presents trade-offs, not ultimatums         │
│  • User can OVERRIDE any recommendation at any time         │
│  • Agent must CONFIRM before: skip steps, change scope,     │
│    deviate from Master Framework                            │
└─────────────────────────────────────────────────────────────┘
```

**Mandatory escalation points:**
- Skip a workflow stage → Ask user: "Bước [X] chưa hoàn thành. Bạn có muốn bỏ qua không?"
- Change JTBD/Value Prop after PMR → Ask user: "PMR kết quả [X]. Có cập nhật JTBD không?"
- Override kill criteria → Ask user: "Kill criteria triggered: [reason]. Proceed anyway?"
- Select tech stack → Ask user: "Recommend [stack]. Approve or choose alternative?"

### 0.3 Master Framework Compliance

**Before ANY recommendation, agent must check:**

```
□ 1. What workflow stage is the user in? (PhD / MVP / Ngũ Sự / Tech)
□ 2. What artifacts already exist in workspace?
□ 3. What is the NEXT required step per Master Framework?
□ 4. Does user's request match the current stage?
□ 5. If NOT match → Escalate: "Bạn đang ở bước [X]. 
    Muốn làm [Y] trước, hay hoàn thành [X] trước?"
```

**Compliance violation examples:**
| User Request | Current Stage | Agent Response |
|---|---|---|
| "Viết code ngay" | Chưa có JTBD | "Cần define JTBD trước. Dùng business-product-leadership?" |
| "Deploy production" | Chưa có CI/CD | "Cần setup pipeline trước. Dùng collaborative-engineering-agent?" |
| "Viết paper" | Chưa có experiment | "Cần chạy experiment trước. Dùng experiment-tracking?" |
| "Refactor architecture" | Chưa có C4 L1 | "Cần vẽ C4 L1 trước. Dùng c4-level1-context?" |

---

## 1. When to Use

- User says: "dùng skill phù hợp", "use right skill", "kinhluan skills", "what should I do next?"
- Multiple skills could apply to a request
- Unclear which workflow stage the user is in
- Need to check artifact existence before routing
- Cross-workflow routing (e.g., "write paper" but experiments not done yet)

---

## 2. Routing Architecture

### 2.1 Three-Layer Detection

```
Layer 1: WORKFLOW DETECTION
    ├─ PhD/Research workflow?
    ├─ MVP/Product workflow?
    ├─ Ngũ Sự/Strategy audit?
    └─ Pure tech/dev task?

Layer 2: STAGE / ARTIFACT DETECTION
    ├─ What files exist in workspace?
    ├─ What was the last completed step?
    └─ What gaps exist in the current workflow?

Layer 3: INTENT CLASSIFICATION
    ├─ Create / Write / Review / Analyze / Fix
    ├─ Specific domain (scheduling, FL, security...)
    └─ Urgency / priority signals
```

### 2.2 Workflow Detection Rules

| User Signal | Likely Workflow | Check For |
|---|---|---|
| "paper", "thesis", "experiment", "baseline", "survey" | **PhD/Research** | `research/` dir, `sota-matrix.md`, `experiments/` |
| "MVP", "product", "feature", "launch", "JTBD", "user" | **MVP/Product** | `docs/why-statement.md`, `c4-diagrams/`, feature flags |
| "should we build", "competitor", "strategy", "timing" | **Ngũ Sự/Strategy** | No specific artifacts — always available |
| "code", "review", "bug", "API", "database", "test" | **Tech/Dev** | Source code files, `package.json`, `go.mod`, etc. |

---

## 3. PhD/Research Workflow Routing

### Stage Map

```
Stage 0: START ──→ sota-survey (if no sota-matrix.md)
   │
Stage 1: SURVEY ──→ research-question (if sota-matrix.md exists, no RQ defined)
   │
Stage 2: RQ ──→ research-design (if RQ exists, no protocol)
   │
Stage 3: DESIGN ──→ experiment-tracking (if protocol exists, no experiments run)
   │
Stage 4: EXPERIMENT ──→ paper-writing (if results exist, no draft)
   │
Stage 5: DRAFT ──→ internal-critique → journal-q1-polish (if draft exists)
   │
Stage 6: POLISH ──→ publication-strategy (if paper ready)
   │
Stage 7: SUBMIT ──→ defense-prep (if paper accepted / thesis compilation)
```

### Artifact-Based Routing

| Artifact Exists? | Missing? | Route To |
|---|---|---|
| No `sota-matrix.md` | — | `sota-survey` |
| `sota-matrix.md` | No clear RQ | `research-question` |
| `sota-matrix.md` + RQ | No experiment protocol | `research-design` |
| Protocol | No `experiments/` dir or logs | `experiment-tracking` |
| Experiment logs | No paper draft | `paper-writing` |
| Paper draft | Not self-reviewed | `internal-critique` |
| Self-reviewed draft | Not polished for Q1 | `journal-q1-polish` |
| Polished paper | No venue selected | `publication-strategy` |
| Accepted papers | No defense prep | `defense-prep` |

### Cross-Stage Routing Examples

**User: "viết paper về federated learning"**
```
1. Detect: PhD workflow
2. Check: Does sota-matrix.md exist? → No
3. Route: "Bạn cần survey SOTA trước. Dùng sota-survey để tìm papers, 
   sau đó mới viết paper."
```

**User: "review my paper"**
```
1. Detect: PhD workflow, Stage 5-6
2. Check: Does draft exist? → Yes
3. Check: Has internal-critique been run? → No
4. Route: internal-critique
5. After critique: "Tiếp theo dùng journal-q1-polish để chuẩn hóa Q1."
```

**User: "so sánh baseline"**
```
1. Detect: PhD workflow, Stage 4
2. Check: experiments/ exists? → Yes
3. Route: experiment-tracking (comparison workflow)
```

---

## 4. MVP/Product Workflow Routing

### Stage Map

```
Stage 0: START ──→ problem-discovery (if no problem statement)
   │
Stage 1: DISCOVERY ──→ why-strategic-rationale (if problem validated)
   │
Stage 2: WHY ──→ business-product-leadership (if WHY statement exists)
   │
Stage 3: WHAT ──→ ddd-core + c4-model (if JTBD defined)
   │
Stage 4: DESIGN ──→ ddd-tactical + c4-level2/3 (if bounded contexts defined)
   │
Stage 5: BUILD ──→ python-dev / js-dev / go-dev (if architecture ready)
   │
Stage 6: SHIP ──→ docker + k8s + dora-core + collaborative-engineering-agent
   │
Stage 7: RELEASE ──→ diffusion-release-tracking
```

### Artifact-Based Routing

| Artifact Exists? | Missing? | Route To |
|---|---|---|
| No problem validation | — | `problem-discovery` |
| Problem statement | No WHY statement | `why-strategic-rationale` |
| WHY statement | No JTBD | `business-product-leadership` |
| JTBD | No architecture | `ddd-core` + `c4-model` |
| C4 L1/L2 | No component design | `ddd-tactical` + `c4-level3-component` |
| Architecture | No code | `python-dev` / `js-dev` / `go-dev` |
| Code | No CI/CD | `collaborative-engineering-agent` + `docker` |
| CI/CD | No release plan | `diffusion-release-tracking` |

### Ngũ Sự Audit Routing

At any stage, user can trigger Ngũ Sự assessment:

```
User: "đánh giá lại chiến lược" / "should we continue?"
→ art-of-war-software-engineering (score all 5 factors)
   ├─ Tao < 5 → why-strategic-rationale
   ├─ Heaven < 5 → problem-discovery + diffusion-release-tracking
   ├─ Earth < 5 → c4-model audit
   ├─ Command < 5 → business-product-leadership (DRI/RACI)
   └─ Method < 5 → dora-core baseline
```

---

## 5. Tech/Dev Task Routing

### Language Detection

| File Pattern | Language | Route To |
|---|---|---|
| `package.json`, `.tsx`, `.ts` | JavaScript/TypeScript | `javascript-typescript` |
| `go.mod`, `.go` | Go | `golang-development` |
| `pyproject.toml`, `requirements.txt`, `.py` | Python | `python-development` |
| `Dockerfile`, `docker-compose.yml` | Docker | `docker-containerization` |
| `*.yaml` in `k8s/`, `deployment.yml` | Kubernetes | `kubernetes-orchestration` |

### Task Type Detection

| User Intent | Route To |
|---|---|
| "review code", "code review", "critique" | `collaborative-engineering-agent` (DRE) |
| "security", "vulnerability", "OWASP" | `security-analysis` |
| "architecture", "design", "refactor" | `c4-model` + `ddd-core` |
| "test", "testing", "bug" | `collaborative-engineering-agent` + language skill |
| "deploy", "CI/CD", "pipeline" | `dora-core` + `collaborative-engineering-agent` |
| "ADR", "decision" | `architecture-decision-records` |

---

## 6. Domain-Specific Routing

These skills are **domain-specific** and only route when the domain is explicitly mentioned:

| Domain Mentioned | Route To |
|---|---|
| "federated learning", "FL", "DQN", "privacy" | `federated-learning-dqn` |
| "scheduling", "HEFT", "GA", "makespan" | `scheduling-algorithms` |

**Rule:** Do NOT route to domain-specific skills unless the user explicitly mentions the domain or the workspace contains domain-specific code (e.g., `federated/`, `scheduling/` directories).

---

## 7. Multi-Skill Scenarios

### Scenario: "Làm MVP app học tiếng Anh"

```
1. Workflow: MVP/Product
2. Check artifacts: None → Stage 0
3. Route sequence:
   a. problem-discovery → validate demand
   b. why-strategic-rationale → WHY statement
   c. business-product-leadership → JTBD + MVP scope
   d. ddd-core + c4-model → architecture
   e. js-dev / python-dev → build
   f. docker + k8s → ship
   g. diffusion-release-tracking → release
```

### Scenario: "Viết luận văn thạc sĩ về optimization"

```
1. Workflow: PhD/Research
2. Check artifacts: None → Stage 0
3. Route sequence:
   a. sota-survey → literature matrix
   b. research-question → RQ + hypothesis
   c. research-design → protocol
   d. experiment-tracking → run experiments
   e. paper-writing → draft
   f. internal-critique → self-review
   g. journal-q1-polish → Q1 polish
   h. publication-strategy → venue + submit
   i. defense-prep → prepare defense
```

### Scenario: "Review code Go microservice"

```
1. Workflow: Tech/Dev
2. Language: Go (go.mod detected)
3. Intent: code review
4. Route:
   a. golang-development (language patterns)
   b. collaborative-engineering-agent (DRE critique)
   c. security-analysis (if auth/API involved)
```

---

## 8. Quick Reference: Skill → Trigger Mapping

| User Says / Context | Primary Skill | Secondary Skills |
|---|---|---|
| "survey", "literature", "papers", "SOTA" | `sota-survey` | `research-question` |
| "research question", "RQ", "hypothesis" | `research-question` | `research-design` |
| "experiment design", "methodology", "baseline" | `research-design` | `experiment-tracking` |
| "run experiment", "compare baseline", "results" | `experiment-tracking` | `paper-writing` |
| "write paper", "thesis chapter", "LaTeX" | `paper-writing` | `technical-english-cs` |
| "polish paper", "Q1", "ISI", "Scopus" | `journal-q1-polish` | `internal-critique` |
| "review my paper", "critique", "fatal flaw" | `internal-critique` | `publication-strategy` |
| "where to submit", "venue", "rebuttal" | `publication-strategy` | `journal-q1-polish` |
| "thesis defense", "committee", "bảo vệ" | `defense-prep` | `milestone-tracker` |
| "should we build", "strategy", "competitor" | `art-of-war` | `problem-discovery` |
| "why build", "value proposition", "PR/FAQ" | `why-strategic-rationale` | `business-product-leadership` |
| "validate problem", "demand", "interview" | `problem-discovery` | `why-strategic-rationale` |
| "JTBD", "product strategy", "MVP" | `business-product-leadership` | `diffusion-release-tracking` |
| "C4 diagram", "architecture" (general) | `c4-model` | `ddd-core` |
| "context diagram", "level 1" | `c4-level1-context` | `c4-model` |
| "container/service diagram", "level 2" | `c4-level2-container` | `c4-model` |
| "component diagram", "level 3" | `c4-level3-component` | `c4-model` |
| "bounded context", "ubiquitous language" | `ddd-core` | `c4-level1-context` |
| "aggregate", "entity", "value object" | `ddd-tactical` | `c4-level4-code` |
| "CQRS", "event sourcing", "saga" | `ddd-patterns` | `ddd-tactical` |
| "docker", "Dockerfile", "container" | `docker-containerization` | `kubernetes-orchestration` |
| "k8s", "kubernetes", "deploy" | `kubernetes-orchestration` | `docker-containerization` |
| "DORA", "deployment frequency", "lead time" | `dora-core` | `collaborative-engineering-agent` |
| "python", "FastAPI", "Pydantic" | `python-development` | `docker-containerization` |
| "go", "golang", "goroutine" | `golang-development` | `docker-containerization` |
| "javascript", "typescript", "react", "nextjs" | `javascript-typescript` | `docker-containerization` |
| "security", "vulnerability", "OWASP" | `security-analysis` | `collaborative-engineering-agent` |
| "review code", "PR", "code review" | `collaborative-engineering-agent` | language skill |
| "federated learning", "FL", "DQN" | `federated-learning-dqn` | `experiment-tracking` |
| "scheduling", "HEFT", "makespan" | `scheduling-algorithms` | `experiment-tracking` |
| "dịch thuật ngữ", "Vietnamese terms" | `vietnamese-cs-terminology` | `paper-writing` |
| "technical English", "IEEE/ACM writing" | `technical-english-cs` | `journal-q1-polish` |

---

## 9. Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| Workflow orchestration | `art-of-war` | Ngũ Sự assessment layer |
| PhD stage routing | `milestone-tracker` | Timeline and deadline management |
| MVP stage routing | `business-product-leadership` | JTBD and product decisions |
| Dev task routing | `collaborative-engineering-agent` | Code review and SDLC |
| Reflection trigger | `second-brain-reflection` | Post-task knowledge capture |
