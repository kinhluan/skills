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

## 🔗 Integration

- → `art-of-war`: Provides the Audit framework.
- → `master-framework`: Lessons feed back into Layer 0 (WHY) and Layer 2 (DESIGN).
- → `antigravity-workflow`: Captures "Human-in-the-Loop" corrections for future automation.
