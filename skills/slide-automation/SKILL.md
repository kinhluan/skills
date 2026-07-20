---
name: slide-automation
description: Create or update reproducible presentation decks from papers, theses, reports, Markdown, data, or figures using PowerPoint, Beamer, Marp, reveal.js, or repository tooling. Use when the user needs slide structure, automated deck generation, figure placement, or rendered-deck verification.
metadata:
  tags: ["slides", "presentation", "research", "powerpoint", "beamer", "automation"]
---

# Slide Automation

Design for the audience and speaking situation, then automate repeatable layout and data binding. A generated source file is not finished until the rendered deck has been inspected.

## Workflow

1. Establish audience, purpose, duration, venue/screen, output format, template, and accessibility constraints.
2. Extract one claim or question per slide and build a narrative:
   - context/problem;
   - evidence or method;
   - key result;
   - interpretation and limits;
   - decision or takeaway.
3. Select the tool already used by the project:
   - PowerPoint for broad editing and office workflows;
   - Beamer for LaTeX-heavy academic material;
   - Marp/reveal.js for version-controlled web/Markdown delivery;
   - a supplied presentation skill/tool when the environment provides one.
4. Reuse the user's template, theme, fonts, and assets.
5. Generate charts/figures from source data when possible and preserve provenance.
6. Render every slide and inspect montage plus full-size high-risk slides.
7. Fix overflow, clipping, contrast, legibility, missing fonts/assets, animation dependence, and inconsistent references.

## Content Rules

- Use a declarative title that states the slide's message.
- Prefer one visual argument over paragraphs.
- Keep essential labels readable at presentation distance.
- Show units, uncertainty, sample size, and source for quantitative claims.
- Do not stretch, crop, recolor, or simplify scientific figures in a way that changes meaning.
- Separate results from interpretation and limitations.
- Keep speaker notes distinct from visible slide content.
- Add alt text or an accessible equivalent where the format supports it.

For defenses or technical talks, align slide count to actual rehearsal time rather than a fixed slides-per-minute rule.

## Automation Contract

- deterministic input paths and ordering;
- explicit theme/layout constants;
- no machine-specific absolute paths;
- graceful handling of missing assets;
- pinned dependencies when reproducibility matters;
- generated output plus source and build command;
- no secrets or private speaker notes in public artifacts.

## Verification

Check:

- deck opens in the target application;
- every slide renders at intended aspect ratio;
- text and visuals remain inside safe margins;
- equations, Unicode, fonts, and citations survive export;
- charts match source data;
- links/media work offline if required;
- PDF export matches the editable deck;
- no placeholder or example content remains.

## Output

Report artifact paths, source inputs, tool/build command, slide count/story, visual checks performed, and any fonts/assets or manual steps still required.

Read [references/detailed-guide.md](references/detailed-guide.md) only for the selected output technology. For new scientific diagrams or illustrations, use [`ai-figure-generation`](../ai-figure-generation/SKILL.md) and verify scientific accuracy before insertion.
