---
name: research-watch
description: Monitor a research topic for new papers, trends, and breakthroughs. Set up recurring watches on arXiv, Semantic Scholar, or specific authors/venues. Use when tracking a fast-moving field, waiting for follow-up work, or maintaining a living literature review. Inspired by Feynman's /watch workflow.
metadata:
  tags: ["research", "phd", "monitoring", "alerts", "literature", "trends"]
---

# Research Watch

**Stay current without drowning in papers.**

Set up intelligent monitoring for research topics, authors, venues, or keywords. Get notified when relevant new work appears, with automatic relevance scoring and synthesis.

> "The literature moves fast. Your knowledge should move faster." — Anonymous Researcher

---

## 1. Watch Types

### 1.1 Topic Watch

Monitor a research topic for new papers:

```
Topic: "mechanistic interpretability"
Keywords: ["mechanistic interpretability", "circuit tracing", "activation patching"]
Venues: [NeurIPS, ICML, ICLR, arXiv cs.LG]
Frequency: weekly
```

**Relevance scoring:**
| Score | Criteria | Action |
|---|---|---|
| 90-100 | Directly addresses your research question | Read immediately |
| 70-89 | Related method or application | Read within 2 days |
| 50-69 | Same field, tangential topic | Skim abstract |
| < 50 | Same broad area | Skip, but log for completeness |

### 1.2 Author Watch

Track specific researchers:

```
Authors: ["Yann LeCun", "Yoshua Bengio", "Geoffrey Hinton"]
Rationale: "Foundational figures in deep learning"
Alert on: new papers, preprints, blog posts
```

### 1.3 Venue Watch

Monitor specific conferences/journals:

```
Venues: ["NeurIPS", "ICML", "ICLR", "JMLR"]
Filter: papers matching [your keywords]
Alert: when proceedings published
```

### 1.4 Citation Watch

Track who cites your work or key papers:

```
Target papers: [your-paper-id, foundational-paper-id]
Alert on: new citations
Include: citation context (how they cite you)
```

---

## 2. Setup Protocol

### Step 1 — Define Watch Scope

```
Watch Name: [descriptive name]
Type: [topic / author / venue / citation]
Query: [keywords, authors, or paper IDs]
Sources: [arXiv / Semantic Scholar / Google Scholar / PubMed]
Frequency: [daily / weekly / monthly]
```

### Step 2 — Configure Filters

**Exclude noise:**
- Negative keywords: ["survey", "review", "tutorial"] (if you want only original research)
- Minimum citations: [0 for new work, 10 for established work]
- Date range: [last 30 days / last 90 days / all time]

**Include priority:**
- CCF-A venues: always alert
- arXiv from known authors: always alert
- Preprints with >50 citations in first month: flag as potentially important

### Step 3 — Set Up Alerts

**arXiv RSS/API:**
```bash
# arXiv API query
http://export.arxiv.org/api/query?search_query=all:mechanistic+interpretability&sortBy=submittedDate&sortOrder=descending&max_results=10
```

**Semantic Scholar Alerts:**
```bash
# Semantic Scholar search with date filter
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=mechanistic+interpretability&fields=title,authors,year,abstract,citationCount&publicationDateOrYear=2024:2025"
```

**Google Scholar Alerts:**
- Create alert at https://scholar.google.com/scholar_alerts
- Use exact phrase matching: `"mechanistic interpretability"`

### Step 4 — Synthesis Template

When new papers arrive, produce a brief synthesis:

```markdown
## Research Watch Report: [Topic] — [Date Range]

### New Papers (N found)

#### 🔴 High Relevance
1. **[Title]** by [Authors] ([Venue], [Year])
   - **Why relevant:** [1 sentence]
   - **Key claim:** [1 sentence]
   - **Relation to your work:** [how it connects]
   - **Action:** [read / skim / save for later]

#### 🟡 Medium Relevance
2. ...

#### 🟢 Low Relevance
3. ...

### Trend Analysis
- **Emerging direction:** [what's new this period]
- **Confirming trend:** [what continues from before]
- **Contradicting result:** [paper that challenges consensus]

### Recommended Actions
1. [Read paper X immediately — directly relevant]
2. [Add paper Y to reading list — related method]
3. [Update SOTA matrix with paper Z — new baseline]
```

---

## 3. Watch Management

### Active Watches Log

Keep a log of all active watches:

```markdown
## Active Research Watches

| Watch Name | Type | Query | Frequency | Last Check | Papers Found |
|---|---|---|---|---|---|
| MechInterp-2024 | Topic | "mechanistic interpretability" | Weekly | 2024-01-15 | 12 |
| Transformer-Scaling | Topic | "scaling laws" + "transformer" | Weekly | 2024-01-15 | 8 |
| LeCun-Papers | Author | "Yann LeCun" | Daily | 2024-01-15 | 1 |
| NeurIPS-2024 | Venue | NeurIPS 2024 proceedings | Monthly | 2024-01-15 | 0 |
```

### Watch Review Cycle

**Monthly:**
- Review all active watches
- Deactivate watches that are no longer relevant
- Merge overlapping watches
- Update keywords based on evolving research focus

**Quarterly:**
- Assess watch effectiveness (signal-to-noise ratio)
- Adjust relevance thresholds
- Add new watches for emerging sub-topics

---

## 4. Integration with Research Workflow

### Watch → SOTA Survey

```
Research Watch (ongoing)
    ↓ (monthly synthesis)
SOTA Survey Update (sota-survey)
    ↓
Updated Literature Matrix
    ↓
Research Question Refinement (research-question)
```

### Watch → Experiment

```
Research Watch detects new baseline
    ↓
Paper Audit (paper-audit) — verify claims
    ↓
Add to experiment tracking (experiment-tracking)
    ↓
Run comparison experiment
```

### Watch → Paper

```
Research Watch detects related work published
    ↓
Update Related Work section (paper-writing)
    ↓
Add citation + differentiate your work
```

---

## 5. Tools for Research Watching

### Manual (Free)
- **arXiv RSS:** Subscribe to category feeds
- **Google Scholar Alerts:** Email alerts for queries
- **Semantic Scholar:** Weekly digest for followed authors
- **Twitter/X:** Follow researchers (noisy but fast)

### Semi-Automated
- **Zotero + RSS:** Auto-import papers from feeds
- **Notion/Airtable:** Track papers with custom views
- **Obsidian:** Link papers in knowledge graph

### Automated (Future)
- **LLM-powered filtering:** Auto-score relevance, generate summaries
- **Slack/Discord bots:** Push alerts to team channels
- **Auto-synthesis:** Generate weekly reports automatically

---

## 6. Anti-Patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| **Too many watches** | Information overload | Limit to 3-5 active watches |
| **Too broad queries** | 90% irrelevant papers | Use exact phrases, add negative keywords |
| **Set-and-forget** | Watches become stale | Monthly review and cleanup |
| **No synthesis** | Papers accumulate unread | Weekly synthesis, not just alerts |
| **Ignoring low-relevance** | Miss paradigm shifts | Monthly review of "skipped" papers |

---

## Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| New paper discovery | `sota-survey` | Deep analysis of discovered papers |
| Paper verification | `paper-audit` | Check if new papers are trustworthy |
| Literature update | `paper-writing` | Update Related Work sections |
| Trend detection | `research-question` | Identify new research directions |

---

## References

- [Feynman /watch](https://github.com/companion-inc/feynman) — Recurring research watch
- [arXiv API](https://arxiv.org/help/api) — Programmatic paper access
- [Semantic Scholar API](https://api.semanticscholar.org/corpus/) — Academic graph API
- [Google Scholar Alerts](https://scholar.google.com/scholar_alerts) — Email alerts
