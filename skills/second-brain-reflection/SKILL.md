---
name: second-brain-reflection
description: >
  Systematically extract lessons from tasks, compress them into reusable rules, 
  and store them in the appropriate memory tier (Local, Global, or Private).
  Use this skill at the end of every major mission or experiment to build 
  your 'Second Brain'.
metadata:
  tags: ["knowledge-management", "reflection", "compression", "second-brain", "learning-loop"]
---

# 🧠 Second Brain Reflection & Compression

**"He who learns but does not think is lost! He who thinks but does not learn is in great danger."** — Confucius (adapted for Agents)

This skill transforms raw experience into compressed, actionable tri thức (knowledge). It ensures that every failure is a lesson and every success is a reusable pattern.

---

## 🔄 The Reflection Protocol

Trigger this protocol after completing a Mission, PR, or Experiment.

### 1. The Art of War Audit (Ngũ Sự)
Evaluate the task through the lens of Sun Tzu's Five Factors:
- **Tao (Alignment):** Did our output match the original `why-strategic-rationale`?
- **Heaven (Context):** Did external shifts (market, new library updates) affect us?
- **Earth (Terrain):** What new technical debt or "architectural traps" did we find in the codebase?
- **Command (Leadership):** Were our decisions data-backed? Where did we guess?
- **Method (Discipline):** Which parts of our SDLC (tests, lint, deploy) felt slow or fragile?

### 2. Knowledge Extraction
Identify 1-3 critical insights. Ask:
- "What was the 'Aha!' moment?"
- "If I had to do this again from scratch, what would I do differently in the first 10 minutes?"
- "What is the one rule that would have prevented our biggest hurdle in this task?"

---

## 🗜️ The Compression Engine (Terse Format)

Do NOT save conversational fluff. Use the **Rule/Stratagem Format**:

- **Rule:** `Condition/Context → Action/Constraint. (Reason).`
- **Stratagem:** `Pattern → Optimization. (Impact).`

### Examples:
- **Bad:** "We realized that when we use the standard Python json library it is too slow for 1GB files, so we should use orjson next time to save 5 seconds."
- **Good (Compressed):** `Rule: Large JSON (>500MB) → Use orjson, not stdlib. (5x faster serialization).`

---

## 💾 Memory Tiering (Where to Save)

Agent must determine the scope before saving:

| Scope | Location | Action |
| :--- | :--- | :--- |
| **Project Specific** | `./GEMINI.md` | Add to "Shared Rules" section. |
| **Private/Task Finding** | `~/.gemini/tmp/skills/memory/MEMORY.md` | Add to local project index. |
| **Universal Truth** | `~/.gemini/GEMINI.md` | Add to "Personal Preferences" section. |

---

## 🚦 Output Format

After processing, the agent should present the knowledge in this format:

```markdown
### 🧠 Second Brain Sync — [Task Name]

**1. Strategic Audit (Sun Tzu):**
- [Factor]: [Finding]

**2. Compressed Knowledge:**
- `Rule: [Context] → [Action]. ([Why]).`

**3. Saving Location:**
- [Path to file]
```

---

## 🔄 Workflow Integration — When to Trigger

Second Brain Reflection is a **closing ritual** for every major workflow. Trigger automatically at the end of:

### PhD/Research Workflow Closing Ritual
After completing each stage:
- **Post-survey:** What search strategies worked? Which venues had the best signal?
- **Post-RQ formulation:** What gaps were most fruitful? What RQ patterns to avoid?
- **Post-experiment:** Which hyperparameters mattered most? What debugging sequence saved time?
- **Post-paper submission:** What reviewer feedback was predictable? What writing pattern to repeat?
- **Post-defense:** What committee questions were surprising? What slides worked best?

### MVP/Product Workflow Closing Ritual
After completing each stage:
- **Post-problem-discovery:** Which validation method gave the strongest signal? What interview question was most revealing?
- **Post-WHY statement:** What assumption was most wrong? What stakeholder pushback was most valuable?
- **Post-design (C4/DDD):** What boundary was hardest to draw? What Generic Subdomain should have been SaaS?
- **Post-ship:** What CI/CD step failed most? What test would have caught the production bug?
- **Post-release:** Which Rogers gate had the weakest signal? What feature flag strategy worked best?

### Ngũ Sự Assessment Closing Ritual
After each strategic assessment:
- Which factor was most surprising? (usually Earth or Command)
- What score changed the most from last assessment?
- What action item from last assessment was actually completed?

### Dev/Task Closing Ritual
After major coding tasks:
- What pattern should become a project rule?
- What tool/library saved the most time?
- What anti-pattern appeared that should be banned?

### Reflection Gate
Before marking any task as DONE in `collaborative-engineering-agent` Kanban, ask:
> "What is the one rule from this task that would save time on the next similar task?"

If the answer is non-trivial, run Second Brain Reflection before closing the task.

---

## 🔗 Integration

- → `art-of-war`: Provides the Audit framework.
- → `master-framework`: Lessons feed back into Layer 0 (WHY) and Layer 2 (DESIGN).
- → `collaborative-engineering-agent`: Reflection Gate before marking tasks DONE.
- → `kinhluan-router`: Reflection results update routing heuristics ("last time X happened, Y skill was most useful").
