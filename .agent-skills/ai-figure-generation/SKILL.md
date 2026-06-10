---
name: ai-figure-generation
description: Generate scientific figures, diagrams, and illustrations using AI image models (DALL-E, Midjourney, Stable Diffusion) from research content. Use when creating visuals for slides, papers, or posters. Converts technical concepts into publication-ready imagery through structured prompts.
metadata:
  tags: ["research", "phd", "visualization", "ai-image", "dalle", "midjourney", "stable-diffusion", "figure", "diagram", "illustration"]
---

# AI Figure Generation

**Turn research concepts into compelling visuals.**

This skill generates scientific figures, diagrams, and illustrations using AI image models. It bridges the gap between technical research content and visual communication — essential for slides, papers, posters, and outreach.

> "A picture is worth a thousand words — but only if it's the right picture." — Unknown

---

## 1. When to Use AI Image Generation

### Use Cases

| Scenario | AI Tool | Output |
|---|---|---|
| **Conceptual diagram** | DALL-E 3 / Midjourney v6 | System architecture, workflow overview |
| **Data visualization style** | Stable Diffusion XL | Stylized charts, infographics |
| **Illustrative figure** | DALL-E 3 | Metaphorical representation of abstract concept |
| **Poster figure** | Midjourney v6 | Eye-catching, high-resolution scientific art |
| **Slide background** | Stable Diffusion | Themed backgrounds for presentation sections |
| **Process flowchart** | DALL-E 3 | Step-by-step methodology illustration |

### When NOT to Use

- **Exact data plots** → Use `slide-automation` (matplotlib/plotly) for accuracy
- **Mathematical notation** → Use LaTeX/TikZ for precision
- **Network topology** → Use draw.io/Gephi for correctness
- **Screenshots of code/results** → Use actual screenshots

---

## 2. Prompt Engineering for Scientific Figures

### 2.1 The Scientific Prompt Formula

```
[Subject] + [Style] + [Context] + [Technical Details] + [Composition] + [Quality]
```

**Example:**
```
Subject: "A federated learning system with 5 edge devices"
Style: "clean vector illustration, flat design, scientific diagram"
Context: "medical AI training on hospital data without sharing patient records"
Technical: "each device labeled 'Hospital A-E', central server labeled 'Aggregator', arrows showing gradient updates"
Composition: "white background, devices arranged in circle around server, color-coded data types"
Quality: "4K, crisp lines, professional publication quality, no text clutter"

Full prompt:
"Clean vector illustration of a federated learning system. Five edge devices 
labeled Hospital A through E arranged in a circle around a central server labeled 
'Aggregator'. Each hospital has a different colored data icon (blue for imaging, 
green for text, orange for genomics). Dashed arrows show encrypted gradient 
updates flowing to the server. Solid arrows show updated model returning to 
hospitals. White background, flat design, scientific diagram style, 4K, 
crisp lines, professional publication quality, minimal text, no clutter"
```

### 2.2 Prompt Templates by Figure Type

#### System Architecture Diagram

```markdown
**Template:**
"[Style: clean technical diagram/vector illustration/3D render] of [System Name]. 
[Component 1] connected to [Component 2] via [Connection Type]. 
[Component 3] labeled '[Label]'. [Color scheme: blue for data, green for 
processing, orange for output]. [Background: white/light gray]. 
[Quality: 4K, crisp, publication-ready]."

**Example (Transformer Architecture):**
"Clean vector illustration of a Transformer neural network architecture. 
Input embedding layer at bottom feeding into multi-head attention block 
with 8 parallel attention heads shown as colored matrices. Residual 
connections with plus signs. Feed-forward network with two dense layers. 
Layer normalization blocks. Output probability distribution at top. 
Labels for each component. White background, blue and orange color scheme, 
scientific diagram style, 4K, crisp lines, minimal text"
```

#### Process / Workflow Diagram

```markdown
**Template:**
"[Style: flat design infographic/step-by-step diagram] showing [N] steps 
of [Process Name]. Step 1: [Description with icon]. Step 2: [Description]. 
... Step N: [Description]. [Arrow style: curved/dashed/colored]. 
[Color coding: green for success, yellow for processing, red for decision]. 
[Background: gradient/white]."

**Example (Research Pipeline):**
"Flat design infographic showing 5 steps of a PhD research pipeline. 
Step 1: Literature review with book icon and magnifying glass. 
Step 2: Experiment design with flask and gears. Step 3: Data collection 
with database icon. Step 4: Analysis with chart and microscope. 
Step 5: Publication with paper and checkmark. Curved arrows connecting 
each step. Green for completed, yellow for in-progress, blue for future. 
White background, clean modern style, 4K"
```

#### Abstract Concept Illustration

```markdown
**Template:**
"[Style: metaphorical illustration/surreal scientific art] representing 
[Abstract Concept]. [Visual metaphor: e.g., 'neural network as a garden 
where each neuron is a flower']. [Color palette: specify]. 
[Mood: inspiring/mysterious/technical]. [Quality: highly detailed, 
8K, artistic yet scientifically grounded]."

**Example (Attention Mechanism):**
"Surreal scientific illustration representing neural network attention 
mechanism. A glowing brain made of interconnected nodes and pathways. 
Bright beams of light connecting important nodes while dimmer connections 
fade to background. Nodes are crystalline structures with mathematical 
symbols inside. Deep blue and gold color palette. Cosmic background with 
subtle grid pattern. Highly detailed, 8K, artistic yet scientifically 
accurate, inspiring mood"
```

#### Comparison / Before-After

```markdown
**Template:**
"Split-screen comparison. Left side: [Before state] labeled 'Before' 
with [visual characteristics]. Right side: [After state] labeled 'After' 
with [visual characteristics]. [Differences highlighted: arrows, color 
changes, annotations]. [Style: scientific visualization]."

**Example (Model Improvement):**
"Split-screen scientific visualization comparing two machine learning 
models. Left side labeled 'Baseline': scattered points with high variance, 
fuzzy decision boundary, red error regions. Right side labeled 'Our Method': 
tight clusters, clear decision boundary, minimal error regions in green. 
Central arrow with '32% improvement' label. White background, clean 
diagram style, publication quality, 4K"
```

### 2.3 Tool-Specific Prompt Adjustments

| Tool | Strengths | Prompt Adjustments |
|---|---|---|
| **DALL-E 3** | Text accuracy, follows instructions precisely | Be explicit about labels and text. DALL-E reads text well. |
| **Midjourney v6** | Artistic quality, aesthetics | Add `--ar 16:9` for slides, `--style raw` for technical accuracy |
| **Stable Diffusion XL** | Customizable, local running | Use ControlNet for precise layout control. Add LoRA for scientific style. |
| **Ideogram** | Best text rendering | Use for figures requiring precise labels and annotations |

**Midjourney parameters:**
```
--ar 16:9      # Slide aspect ratio
--ar 4:3       # Standard presentation
--ar 3:2       # Poster
--style raw    # Less artistic, more literal
--v 6          # Version 6 (latest)
--q 2          # Higher quality
```

---

## 3. Figure Types for Research

### 3.1 For Papers

| Figure Type | Prompt Focus | Example |
|---|---|---|
| **Method overview** | Clean diagram, labeled components | "Vector diagram of proposed method with 3 modules..." |
| **Data pipeline** | Flowchart style, step-by-step | "Infographic showing data preprocessing pipeline..." |
| **Conceptual model** | Abstract but grounded | "Illustration of attention flow in transformer..." |
| **Qualitative results** | Side-by-side comparisons | "Comparison grid showing 4 input-output pairs..." |

### 3.2 For Slides

| Figure Type | Prompt Focus | Example |
|---|---|---|
| **Title slide background** | Thematic, not distracting | "Abstract geometric pattern in blue tones, subtle, professional..." |
| **Section divider** | Visual metaphor | "Bridge connecting two cliffs, symbolizing methodology to results..." |
| **Key concept** | Single idea, bold | "Giant magnifying glass over a neural network, highlighting one node..." |
| **Takeaway figure** | Memorable, simple | "Single powerful image summarizing main result..." |

### 3.3 For Posters

| Figure Type | Prompt Focus | Example |
|---|---|---|
| **Eye-catching header** | Bold, colorful, readable from distance | "Stylized scientific illustration of [topic], vibrant colors..." |
| **Method figure** | Detailed but clear | "Detailed technical diagram with callouts and annotations..." |
| **Results highlight** | Data-driven visual | "Artistic representation of performance improvement..." |

---

## 4. Post-Processing

### 4.1 From AI Output to Publication

```
AI Generated Image
    ↓
[1] Upscale (if needed) — Topaz Gigapixel AI, Real-ESRGAN
[2] Clean up text/labels — Photoshop, GIMP, or regenerate with better prompt
[3] Add precise annotations — PowerPoint, Keynote, draw.io
[4] Export final — PNG for slides, PDF for papers, TIFF for print
```

### 4.2 Adding Annotations

AI-generated images often need precise labels added manually:

```python
# Python: Add annotations with PIL
from PIL import Image, ImageDraw, ImageFont

img = Image.open("ai_generated.png")
draw = ImageDraw.Draw(img)

# Add label
font = ImageFont.truetype("Arial.ttf", 24)
draw.text((100, 50), "Encoder", fill="black", font=font)

# Add arrow
draw.line([(200, 100), (300, 100)], fill="red", width=3)

img.save("figure_with_annotations.png")
```

---

## 5. Ethics and Best Practices

### 5.1 Disclosure

**Always disclose AI-generated figures:**
- Paper caption: "Figure generated using DALL-E 3 and manually annotated"
- Slide footnote: "AI-assisted visualization"
- Poster: Small note indicating AI generation

### 5.2 Accuracy

**AI-generated figures are illustrative, not data:**
- ✅ Use for: Conceptual diagrams, process flows, metaphors
- ❌ Never use for: Exact data plots, experimental results, quantitative comparisons

### 5.3 Copyright

- DALL-E 3: You own the output (OpenAI terms)
- Midjourney: Commercial use allowed with subscription
- Stable Diffusion: Open source, check model license

---

## 6. Integration with Slide Automation

```
Research Content
    ↓
ai-figure-generation → Creates conceptual figures, backgrounds, illustrations
    ↓
slide-automation → Inserts figures into slides, adds data plots, exports deck
    ↓
Final Presentation
```

**Workflow:**
1. Use `ai-figure-generation` for conceptual/metaphorical visuals
2. Use `slide-automation` for data plots and slide structure
3. Combine in final presentation tool

---

## References

- [DALL-E 3](https://openai.com/dall-e-3) — OpenAI image generation
- [Midjourney](https://www.midjourney.com/) — Artistic AI images
- [Stable Diffusion](https://stability.ai/) — Open-source image generation
- [Ideogram](https://ideogram.ai/) — Text-accurate image generation
- [slide-automation](./slide-automation/SKILL.md) — Automated slide creation
