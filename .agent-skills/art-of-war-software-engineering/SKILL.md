---
name: art-of-war-software-engineering
description: Use before any major initiative, architecture decision, or competitive strategy choice. Triggers on "should we build this?", "how do we compete?", "is the timing right?", or when evaluating resource allocation. Scores five parallel factors (Tao/Heaven/Earth/Command/Method) → go/caution/stop verdict.
metadata:
  tags: ["strategy", "sun-tzu", "leadership", "planning", "tactics", "product-strategy"]
---

# ⚔️ Art of War for Software Engineering

**"The general who wins a battle makes many calculations in his temple before the battle is fought."** — Sun Tzu

Without this framework, teams commit to initiatives with hidden weaknesses — wrong timing, technical terrain that can't support the feature, no clear ownership, or engineers building without knowing why. The Five Factors surface these risks before resources are spent.

---

## 🏛️ The Five Fundamental Factors (Ngũ Sự)

Five **parallel** evaluation criteria. Score all simultaneously — not a sequential pipeline.

### 1. Tao (道 — The Way)
**Definition:** Shared vision and alignment between stakeholders and the engineering team.
- **Software Mapping:** Does every engineer know why we are building this? → `why-strategic-rationale`
- **Check:** Can any engineer articulate the business value without reading a doc?

| Score | Signal |
|---|---|
| 1–3 | No WHY Statement. Direction changes weekly. Engineers "just completing tickets". |
| 4–6 | Some alignment but different team members give different answers to "why". |
| 7–10 | Clear WHY Statement + JTBD defined. All engineers can articulate business value. |

**If score < 5:** Run `why-strategic-rationale` before proceeding.

---

### 2. Heaven (天 — Timing)
**Definition:** External conditions beyond control — market trends, timing, competition.
- **Software Mapping:** Is the market ready? → `diffusion-release-tracking` Rogers curve
- **Check:** Launching too early (market not ready) or too late (missed window)?

| Score | Signal |
|---|---|
| 1–3 | No market validation. Building on assumption. Competitors dominate with no visible gap. |
| 4–6 | Some demand signals but timing unclear. Problem unvalidated. |
| 7–10 | Problem validated via `problem-discovery`. Target segment identified. Chasm strategy defined. |

**If score < 5:** Run `problem-discovery` + `diffusion-release-tracking` before proceeding.

---

### 3. Earth (地 — Terrain)
**Definition:** Technical landscape, legacy systems, infrastructure — the "ground" you must traverse.
- **Software Mapping:** Tech debt, system boundaries, architecture → `c4-model` + `ddd-core`
- **Check:** Is tech debt too heavy to traverse? Should we buy instead of build?

| Score | Signal |
|---|---|
| 1–3 | Massive tech debt. Monolith. >6 months to change core component. No CI/CD. |
| 4–6 | Some debt, partially modular. Deploy takes days. Inconsistent test coverage. |
| 7–10 | Clean C4/DDD architecture. Loosely coupled. Core Domain isolated. Deploy < 1 hour. |

**If score < 5:** Run `c4-model` audit. Identify debt hotspots. Evaluate SaaS/managed services for Generic Subdomains before committing to build.

---

### 4. Command (將 — Leadership)
**Definition:** Leadership qualities — wisdom, accountability, decision-making clarity.
- **Software Mapping:** Architects, PMs, Senior Engineers → `business-product-leadership`
- **Check:** Is there one DRI (Directly Responsible Individual) for the technical vision?

| Score | Signal |
|---|---|
| 1–3 | No clear owner. Decisions by committee or HIPPO (Highest Paid Person's Opinion). |
| 4–6 | Nominal ownership but unclear accountability. Gut-feel decisions dominant. |
| 7–10 | Clear DRI. Data-driven decisions. WHY understood and owned by leadership. |

**If score < 5:** Establish ownership and define RACI before execution begins.

---

### 5. Method (法 — Discipline)
**Definition:** SDLC discipline, logistics, operational structure.
- **Software Mapping:** CI/CD, testing, DORA metrics → `dora-core`
- **Check:** Are deploy pipelines robust? Is testing/linting consistent?

| Score | Signal |
|---|---|
| 1–3 | Manual deployment. No CI/CD. DORA: Low tier (deployments < monthly). |
| 4–6 | Some automation but inconsistent. DORA: Medium tier. |
| 7–10 | Full CI/CD. Automated testing. DORA: High/Elite tier. Lead time < 1 hour. |

**If score < 5:** Run `dora-core` baseline. Fix CI/CD before adding feature complexity.

---

## ⚖️ Strategic Assessment Matrix

Score all five factors simultaneously before committing to any initiative.

| Factor | Score /10 | If Low → Action |
|:---|:---:|:---|
| **Tao 道** — WHY clear to every engineer? | | Run `why-strategic-rationale` |
| **Heaven 天** — Market timing validated? | | Run `problem-discovery` + `diffusion-release-tracking` |
| **Earth 地** — Tech terrain navigable? | | Run `c4-model` audit, consider SaaS |
| **Command 將** — Single DRI accountable? | | Establish ownership, define RACI |
| **Method 法** — Pipeline automated? | | Run `dora-core` baseline |
| **Total** | **/50** | |

| Score | Decision |
|:---|:---|
| **40–50** | Excellent positioning. Proceed at full speed. |
| **30–39** | Proceed with caution. Fix lowest-scoring factor before sprint planning. |
| **< 30** | **STOP.** Fix the two lowest-scoring factors. Re-assess before committing resources. |

---

## 🎯 Strategic Stratagems

### 1. "Know Yourself, Know Your Enemy"
> "If you know the enemy and know yourself, you need not fear the result of a hundred battles."

**Know yourself:** Audit team capabilities, tech debt (Earth), Core Domain boundaries.
**Know your enemy:** Run `problem-discovery` — customer interviews + LMR (job board scan) + competitor analysis. Competitor analysis reveals the beachhead niche.

**DO:** Complete `problem-discovery` before defining JTBD.
**DON'T:** Substitute SWOT gut-feel for actual market signals. Assumptions are not intelligence.

---

### 2. "Win Without Fighting" (The Sheathed Sword)
> "The supreme art of war is to subdue the enemy without fighting."

For every feature, ask: Core Domain or Generic Subdomain?
- **Generic Subdomain** → buy SaaS (Auth → Auth0, Payments → Stripe, Email → SendGrid)
- **Core Domain** → build with full engineering investment

**DO:** Default to SaaS for anything outside Core Domain.
**DON'T:** Build Generic Subdomains. Every one you build steals engineering energy from your Core Domain — the only place you can actually win.

---

### 3. "Avoid Strength, Attack Weakness"
> "Water runs away from high places and hastens downwards."

**Strength** = dominant competitors with moats, or your own legacy codebase.
**Weakness** = underserved niches competitors ignore, new isolated microservices vs. monolith.

**DO:** Identify underserved segment from `problem-discovery` competitor analysis → use as beachhead. Dominate that niche completely, then cross the Chasm (`diffusion-release-tracking`). Target Early Adopters first.
**DON'T:** Compete head-on with dominant player. Don't refactor a massive monolith when you can build isolated new value instead.

---

### 4. "Binh Như Nước" — Water Strategy (Adaptability)
> "Shape your flow according to the nature of the ground over which it flows."

**DO:** Ship behind feature flags. Maintain high Deployment Frequency (`dora-core`). Keep architecture loosely coupled.
**DON'T:** Build tightly coupled monoliths or plan big-bang releases. Frozen water cannot flow — when Heaven (market) changes, you must be able to pivot.

---

## 🔄 Integrated Workflow

```
1. Ngũ Sự Assessment (score /50)                    [Sun Tzu, ~500 BC]
   ├─ < 30  → Fix 2 lowest factors → re-assess
   └─ ≥ 30  → Proceed

2. "Know Yourself/Enemy" → problem-discovery
   ├─ Customer interviews                            [Blank 2005]
   ├─ Lean validation (landing page, smoke test)    [Ries 2011]
   └─ Output: Problem Statement + beachhead niche

3. "Establish Tao" → why-strategic-rationale
   ├─ VPC (Value Proposition Canvas)                [Osterwalder 2014]
   ├─ PR/FAQ (Working Backwards)                    [Amazon; Bryar & Carr 2021]
   └─ Output: WHY Statement + JTBD                 [Christensen; Moesta]

4. "Map Earth" → c4-model + ddd-core
   ├─ C4 architecture mapping                       [Simon Brown 2011]
   ├─ Domain-Driven Design                          [Evans 2003]
   ├─ Generic Subdomain → "Win without fighting" → buy/SaaS
   └─ Core Domain → build

5. "Water strategy" → ship/release
   ├─ Feature flags (dark launch)                   [Fowler 2010]
   ├─ Early Adopters → Rogers curve → Cross Chasm   [Rogers 1962; Moore 1991]
   └─ DORA metrics = measure adaptability           [Forsgren, Humble, Kim 2018]
```

*Ngũ Sự runs as audit layer at each step — not just at the start.*

---

## 🔗 Connection to Ecosystem

- → `why-strategic-rationale`: Establishes the **Tao** (WHY Statement)
- → `problem-discovery`: Executes "Know Your Enemy" (market + competitor signals)
- → `diffusion-release-tracking`: Navigates the **Heaven** (Rogers curve + Chasm)
- → `c4-model` + `ddd-core`: Maps the **Earth** (architecture + domain)
- → `business-product-leadership`: Exercises the **Command** (JTBD + MVP + DRI)
- → `dora-core`: Refines the **Method** (CI/CD + DORA metrics)

---

## 🚫 Strategic Anti-Patterns

| Anti-pattern | Detection Signal | Consequence | Fix |
|:---|:---|:---|:---|
| **High Method, Zero Tao** | Engineers ship daily but can't explain business value | Efficiently building the wrong thing | WHY Statement before next sprint |
| **Attacking strength** | Competing head-on with dominant player in their core market | Resource drain, no path to win | Beachhead: dominate underserved niche first |
| **Building Generic Subdomains** | Auth, payments, email built in-house | Engineering energy stolen from Core Domain | Replace with SaaS, redirect capacity |
| **Ignoring the Earth** | Adding features to high-debt codebase with no audit | Velocity collapse, production incidents | C4/DDD audit before committing to timeline |
| **Frozen water** | Monolith, big-bang releases, no feature flags | Cannot pivot when market changes | Loosely coupled services + feature flags + high DF |
| **Command without Method** | Strong vision, inconsistent/manual pipelines | Vision never ships reliably | DORA baseline → CI/CD investment |

---

## 📚 Sources

| Concept | Author / Source | Year | Search keywords |
|:---|:---|:---:|:---|
| Five Factors (Ngũ Sự) | Sun Tzu, *The Art of War* | ~500 BC | "Art of War Sun Tzu five factors" |
| Customer Development | Steve Blank, *Four Steps to the Epiphany* | 2005 | "Customer Development Steve Blank" |
| Lean Startup / smoke tests | Eric Ries, *The Lean Startup* | 2011 | "Lean Startup Eric Ries validated learning" |
| Value Proposition Canvas (VPC) | Alex Osterwalder, *Value Proposition Design* | 2014 | "Value Proposition Canvas Osterwalder" |
| Working Backwards / PR/FAQ | Amazon; Colin Bryar & Bill Carr, *Working Backwards* | 2021 | "Amazon Working Backwards PR FAQ" |
| Jobs-To-Be-Done (JTBD) | Christensen; Ulwick; Moesta, *Demand-Side Sales 101* | 2003+ | "Jobs To Be Done theory Christensen" |
| Crossing the Chasm / Beachhead | Geoffrey Moore, *Crossing the Chasm* | 1991 | "Crossing the Chasm Geoffrey Moore beachhead" |
| Diffusion of Innovations | Everett Rogers | 1962 | "Diffusion of Innovations Everett Rogers" |
| Domain-Driven Design (DDD) | Eric Evans, *Domain-Driven Design* | 2003 | "Domain Driven Design Eric Evans" |
| C4 Model | Simon Brown | 2011 | "C4 model Simon Brown architecture" |
| DORA Metrics | Forsgren, Humble, Kim, *Accelerate* | 2018 | "DORA metrics Accelerate book DevOps" |
| Feature Toggles | Martin Fowler | 2010 | "Feature Toggles Martin Fowler" |
