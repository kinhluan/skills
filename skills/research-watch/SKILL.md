---
name: research-watch
description: Design, run, or maintain a recurring watch for new research papers, authors, citations, venues, and topic trends. Use when a user wants literature alerts, a periodic evidence digest, or an update process for a living literature review.
metadata:
  tags: ["research", "monitoring", "alerts", "literature", "trends", "recurring"]
---

# Research Watch

Build a reproducible monitoring specification and separate it from the scheduler that executes it. If the environment has no recurring-task mechanism, produce a runnable one-shot query and setup instructions; do not claim that an ongoing watch was created.

## Define the Watch

Record:

```yaml
name: descriptive-watch-name
question: decision or research question this watch informs
entities:
  topics: []
  authors: []
  venues: []
  seed_papers: []
include_terms: []
exclude_terms: []
sources: []
cadence: weekly
lookback_overlap_days: 3
destination: path, document, feed, or inbox
owner: person responsible for review
```

Use stable identifiers where possible: ORCID for authors, DOI/OpenAlex/Semantic Scholar/arXiv IDs for papers, and canonical venue identifiers. Names alone are ambiguous.

## Build Dynamic Queries

1. At execution time, calculate `window_start` from the previous successful run minus the overlap.
2. Set `window_end` to the current execution date in the user's time zone.
3. URL-encode query parameters.
4. Use HTTPS endpoints, documented authentication, pagination, rate limits, timeouts, and retry/backoff.
5. Persist the query, retrieval timestamp, source identifier, and raw metadata needed to reproduce the result.

Never freeze a date range such as `2024:2025` in a recurring query. Do not use citation count or venue rank as an automatic inclusion rule for new work.

Useful primary services:

- [arXiv API](https://info.arxiv.org/help/api/index.html)
- [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)
- [OpenAlex API](https://docs.openalex.org/)
- [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/api-docs/graph)
- official publisher, conference, journal, or author feeds when available

Check current API documentation before implementing because fields, limits, and authentication can change.

## Retrieve and Deduplicate

1. Fetch every configured source for the same time window.
2. Normalize titles for comparison, but retain original text.
3. Deduplicate first by DOI or stable source ID, then by title/author/year with manual review for uncertain matches.
4. Preserve preprint and published versions as related records rather than silently collapsing materially different versions.
5. Mark retractions, corrections, withdrawn preprints, and version changes.
6. Keep a checkpoint only after the destination write succeeds.

## Relevance Triage

Create a rubric tied to the watch question:

| Dimension | Question |
|---|---|
| directness | Does the work address the defined question or population? |
| contribution | Is the method, dataset, result, or critique new for this watch? |
| evidence | Are claims supported by accessible methods and results? |
| applicability | Does it change a decision, experiment, baseline, or argument? |
| confidence | Is the match based on full text, abstract, or metadata only? |

Calibrate weights with labeled examples. Treat automated relevance as triage, not truth. A paper may be important with zero citations, outside ranked venues, or contrary to the current consensus.

## Recurring Execution

Only create an external alert, scheduled job, message, or document when that action is within the user's request. Report the actual mechanism:

- platform-native recurring task or monitor;
- arXiv/RSS or publisher feed;
- Google Scholar or Semantic Scholar alert configured by the user;
- CI/cron job owned by the repository;
- manual one-shot command and calendar reminder.

For every run, log status, window, sources queried, result count, deduplication count, failures, and next checkpoint. Alert visibly on partial-source failure rather than publishing a silently incomplete digest.

## Digest

```markdown
## Research Watch — [name]

**Window:** [start–end, timezone]
**Sources:** [successful sources]
**Partial failures:** [none or details]
**Retrieved / unique / included:** N / N / N

### Decision-relevant additions
1. **[Title]** — [stable link]
   - Match evidence: [abstract/full text/metadata]
   - Main claim: [paraphrase]
   - Why it matters: [connection to watch question]
   - Confidence/caveat: [limit]
   - Action: read / audit / add baseline / update related work

### Trend update
- Emerging:
- Confirming:
- Contradicting:

### Query changes for next run
- [term/source/rubric change with rationale]
```

Route deep synthesis to `sota-survey`, claim/code verification to `paper-audit`, experiment changes to `research-design`, and manuscript updates to `paper-writing`.
