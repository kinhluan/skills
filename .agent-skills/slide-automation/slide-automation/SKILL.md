---
name: slide-automation
description: Generate presentation slides from research content (paper, thesis, markdown) using Python (python-pptx), LaTeX Beamer, Marp, or reveal.js. Use when converting written research into presentation decks, automating figure insertion, or creating reproducible slide templates.
metadata:
  tags: ["research", "phd", "presentation", "slides", "powerpoint", "beamer", "marp", "revealjs", "automation", "python-pptx"]
---

# Slide Automation

**From markdown to deck — reproducible, version-controlled presentations.**

This skill automates the creation of research presentations from structured content. It eliminates manual copy-pasting, ensures consistency, and makes slides version-controllable alongside your research.

> "Your slides should be as reproducible as your experiments." — Researcher's Maxim

---

## 1. When to Automate Slides

### Use Cases

| Scenario | Tool | Output |
|---|---|---|
| **Paper → Conference talk** | python-pptx | .pptx with figures auto-inserted |
| **Thesis → Defense slides** | LaTeX Beamer | .pdf with precise typography |
| **Markdown → Quick deck** | Marp | .html or .pdf from markdown |
| **Web-based presentation** | reveal.js | Interactive HTML slides |
| **Recurring reports** | python-pptx | Template-based monthly updates |

### When NOT to Automate

- **One-off, highly designed pitch deck** → Use Keynote/PowerPoint manually
- **Creative storytelling presentation** → Manual design for emotional impact
- **Rapid iteration with designer** → Figma/Sketch collaboration

---

## 2. Tool Comparison

| Tool | Format | Best For | Learning Curve | Collaboration |
|---|---|---|---|---|
| **python-pptx** | .pptx | Data-heavy, figure-rich talks | Low | Git-friendly |
| **LaTeX Beamer** | .pdf | Academic defense, math-heavy | Medium | Git-friendly |
| **Marp** | .md → .pdf/.html | Quick markdown-based decks | Very low | Git-friendly |
| **reveal.js** | .html | Interactive web presentations | Low | Git-friendly |
| **Quarto** | .qmd → multiple | Reproducible research reports | Medium | Git-friendly |

---

## 3. python-pptx: PowerPoint from Python

### 3.1 Basic Structure

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RgbColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# Create presentation
prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9
prs.slide_height = Inches(7.5)

# Add title slide
blank_layout = prs.slide_layouts[6]  # Blank layout
slide = prs.slides.add_slide(blank_layout)

# Add title
title_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(11.333), Inches(1.5))
tf = title_box.text_frame
tf.text = "Federated Learning for Medical AI"
p = tf.paragraphs[0]
p.font.size = Pt(44)
p.font.bold = True
p.font.color.rgb = RgbColor(0x1a, 0x1a, 0x1a)
p.alignment = PP_ALIGN.CENTER

# Add subtitle
sub_box = slide.shapes.add_textbox(Inches(1), Inches(4.2), Inches(11.333), Inches(1))
tf = sub_box.text_frame
tf.text = "Privacy-Preserving Collaborative Training"
p = tf.paragraphs[0]
p.font.size = Pt(24)
p.font.color.rgb = RgbColor(0x66, 0x66, 0x66)
p.alignment = PP_ALIGN.CENTER

# Save
prs.save('presentation.pptx')
```

### 3.2 Research Slide Template

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RgbColor

class ResearchSlideDeck:
    """Template for academic/research presentations."""
    
    # Color scheme
    PRIMARY = RgbColor(0x1a, 0x5f, 0x9e)      # Dark blue
    SECONDARY = RgbColor(0x2e, 0x8b, 0x57)    # Green
    ACCENT = RgbColor(0xe6, 0x8a, 0x00)       # Orange
    DARK = RgbColor(0x1a, 0x1a, 0x1a)         # Near black
    LIGHT = RgbColor(0xf5, 0xf5, 0xf5)        # Light gray
    
    def __init__(self, title: str, author: str, date: str):
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.title = title
        self.author = author
        self.date = date
        self._add_title_slide()
    
    def _add_title_slide(self):
        """Add title slide with research branding."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        
        # Background accent bar
        shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
            Inches(0.3), Inches(7.5)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = self.PRIMARY
        shape.line.fill.background()
        
        # Title
        title_box = slide.shapes.add_textbox(
            Inches(1), Inches(2.5), Inches(11), Inches(1.5)
        )
        tf = title_box.text_frame
        tf.text = self.title
        p = tf.paragraphs[0]
        p.font.size = Pt(40)
        p.font.bold = True
        p.font.color.rgb = self.DARK
        
        # Author and date
        info_box = slide.shapes.add_textbox(
            Inches(1), Inches(4.3), Inches(11), Inches(1)
        )
        tf = info_box.text_frame
        tf.text = f"{self.author}\n{self.date}"
        p = tf.paragraphs[0]
        p.font.size = Pt(20)
        p.font.color.rgb = RgbColor(0x66, 0x66, 0x66)
    
    def add_content_slide(self, title: str, bullets: list[str], 
                          figure_path: str = None):
        """Add a content slide with bullets and optional figure."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        
        # Title bar
        title_shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
            Inches(13.333), Inches(1)
        )
        title_shape.fill.solid()
        title_shape.fill.fore_color.rgb = self.PRIMARY
        title_shape.line.fill.background()
        
        # Title text
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.2), Inches(12), Inches(0.6)
        )
        tf = title_box.text_frame
        tf.text = title
        p = tf.paragraphs[0]
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = RgbColor(0xFF, 0xFF, 0xFF)
        
        # Content area
        if figure_path:
            # Two-column: bullets left, figure right
            # Bullets
            content_box = slide.shapes.add_textbox(
                Inches(0.5), Inches(1.3), Inches(6), Inches(5.5)
            )
            tf = content_box.text_frame
            tf.word_wrap = True
            
            for i, bullet in enumerate(bullets):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = f"• {bullet}"
                p.font.size = Pt(18)
                p.font.color.rgb = self.DARK
                p.space_after = Pt(12)
            
            # Figure
            slide.shapes.add_picture(
                figure_path, Inches(7), Inches(1.3), 
                width=Inches(5.5)
            )
        else:
            # Full-width bullets
            content_box = slide.shapes.add_textbox(
                Inches(0.5), Inches(1.3), Inches(12.333), Inches(5.5)
            )
            tf = content_box.text_frame
            tf.word_wrap = True
            
            for i, bullet in enumerate(bullets):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = f"• {bullet}"
                p.font.size = Pt(20)
                p.font.color.rgb = self.DARK
                p.space_after = Pt(14)
        
        return slide
    
    def add_figure_slide(self, title: str, figure_path: str, 
                         caption: str = None):
        """Add a full-slide figure with caption."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        
        # Title
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.3), Inches(12), Inches(0.6)
        )
        tf = title_box.text_frame
        tf.text = title
        p = tf.paragraphs[0]
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = self.DARK
        
        # Figure (centered, large)
        slide.shapes.add_picture(
            figure_path, Inches(1.5), Inches(1.2),
            width=Inches(10.333)
        )
        
        # Caption
        if caption:
            cap_box = slide.shapes.add_textbox(
                Inches(1), Inches(6.5), Inches(11.333), Inches(0.6)
            )
            tf = cap_box.text_frame
            tf.text = caption
            p = tf.paragraphs[0]
            p.font.size = Pt(14)
            p.font.italic = True
            p.font.color.rgb = RgbColor(0x66, 0x66, 0x66)
            p.alignment = PP_ALIGN.CENTER
        
        return slide
    
    def save(self, filename: str):
        """Save the presentation."""
        self.prs.save(filename)
        print(f"Saved: {filename}")


# Usage example
deck = ResearchSlideDeck(
    title="Federated Learning for Medical AI",
    author="Nguyen Van A",
    date="June 2026"
)

deck.add_content_slide(
    title="Research Motivation",
    bullets=[
        "Medical data is siloed across hospitals due to privacy regulations",
        "Centralized training requires data sharing — prohibited by HIPAA/GDPR",
        "Federated Learning enables collaborative training without data sharing",
        "Challenge: Statistical heterogeneity across medical institutions"
    ]
)

deck.add_figure_slide(
    title="Proposed Architecture",
    figure_path="figures/fl_architecture.png",
    caption="Figure 1: Heterogeneous federated learning with personalized aggregation"
)

deck.save("defense_presentation.pptx")
```

### 3.3 Auto-Generate from Markdown

```python
import re
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt

def markdown_to_pptx(md_path: str, output_path: str):
    """Convert markdown research outline to PowerPoint."""
    
    with open(md_path) as f:
        content = f.read()
    
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Parse markdown sections
    sections = re.split(r'\n## ', content)
    
    for section in sections[1:]:  # Skip title
        lines = section.strip().split('\n')
        title = lines[0].strip()
        
        # Extract bullets
        bullets = []
        for line in lines[1:]:
            if line.strip().startswith('- ') or line.strip().startswith('* '):
                bullets.append(line.strip()[2:])
        
        # Create slide
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        
        # Add title
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.5), Inches(12), Inches(0.8)
        )
        tf = title_box.text_frame
        tf.text = title
        p = tf.paragraphs[0]
        p.font.size = Pt(32)
        p.font.bold = True
        
        # Add bullets
        if bullets:
            content_box = slide.shapes.add_textbox(
                Inches(0.5), Inches(1.5), Inches(12), Inches(5)
            )
            tf = content_box.text_frame
            tf.word_wrap = True
            
            for i, bullet in enumerate(bullets[:6]):  # Max 6 bullets
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = f"• {bullet}"
                p.font.size = Pt(20)
                p.space_after = Pt(10)
    
    prs.save(output_path)
    print(f"Generated {output_path} with {len(sections)-1} slides")


# Usage
markdown_to_pptx("research_outline.md", "auto_presentation.pptx")
```

---

## 4. LaTeX Beamer: Academic Defense

### 4.1 Basic Template

```latex
\documentclass[aspectratio=169]{beamer}

% Theme
\usetheme{Madrid}
\usecolortheme{seahorse}
\setbeamertemplate{navigation symbols}{}

% Colors
\definecolor{primary}{RGB}{26, 95, 158}
\definecolor{accent}{RGB}{230, 138, 0}
\setbeamercolor{title}{fg=primary}
\setbeamercolor{frametitle}{fg=primary,bg=white}
\setbeamercolor{structure}{fg=primary}

% Information
\title[Federated Learning]{Federated Learning for Medical AI}
\subtitle{Privacy-Preserving Collaborative Training}
\author{Nguyen Van A}
\institute{Hanoi University of Science and Technology}
\date{June 2026}

\begin{document}

% Title slide
\begin{frame}
\titlepage
\end{frame}

% Outline
\begin{frame}{Outline}
\tableofcontents
\end{frame}

% Content
\section{Introduction}
\begin{frame}{Research Motivation}
\begin{itemize}
    \item Medical data is siloed across hospitals
    \item Privacy regulations prohibit data sharing
    \item Federated Learning enables collaborative training
    \item Challenge: Statistical heterogeneity
\end{itemize}
\end{frame}

\section{Methodology}
\begin{frame}{Proposed Approach}
\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
    \item Personalized aggregation
    \item Adaptive learning rates
    \item Differential privacy guarantees
\end{itemize}
\column{0.5\textwidth}
\includegraphics[width=\linewidth]{figures/architecture.pdf}
\end{columns}
\end{frame}

\section{Results}
\begin{frame}{Experimental Results}
\begin{table}
\centering
\begin{tabular}{lccc}
\toprule
Method & Accuracy & Rounds & Privacy \\
\midrule
FedAvg & 92.1\% & 134 & $\epsilon=8$ \\
FedProx & 93.0\% & 118 & $\epsilon=8$ \\
\textbf{Ours} & \textbf{94.3\%} & \textbf{87} & $\epsilon=4$ \\
\bottomrule
\end{tabular}
\end{table}
\end{frame}

\section{Conclusion}
\begin{frame}{Conclusion}
\begin{block}{Key Contributions}
\begin{enumerate}
    \item Novel aggregation mechanism for heterogeneous data
    \item Improved convergence with fewer communication rounds
    \item Stronger privacy guarantees
\end{enumerate}
\end{block}
\end{frame}

\begin{frame}
\centering
\Huge Thank You
\vspace{1cm}

\normalsize Questions?
\end{frame}

\end{document}
```

### 4.2 Compile

```bash
# Compile Beamer to PDF
pdflatex defense.tex
pdflatex defense.tex  # Run twice for TOC

# Or use latexmk
latexmk -pdf defense.tex
```

---

## 5. Marp: Markdown to Slides

### 5.1 Basic Usage

```markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

# Federated Learning for Medical AI

## Privacy-Preserving Collaborative Training

**Nguyen Van A**
Hanoi University of Science and Technology
June 2026

---

## Research Motivation

- Medical data is siloed across hospitals
- Privacy regulations prohibit data sharing
- Federated Learning enables collaborative training
- **Challenge**: Statistical heterogeneity

---

## Proposed Architecture

![width:800px](figures/architecture.png)

*Figure 1: Heterogeneous federated learning system*

---

## Results

| Method | Accuracy | Rounds |
|--------|----------|--------|
| FedAvg | 92.1% | 134 |
| FedProx | 93.0% | 118 |
| **Ours** | **94.3%** | **87** |

---

## Conclusion

1. Novel aggregation mechanism
2. Improved convergence
3. Stronger privacy guarantees

---

# Thank You

Questions?
```

### 5.2 Compile

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Convert to PDF
marp slides.md -o presentation.pdf

# Convert to HTML
marp slides.md -o presentation.html

# Watch mode (auto-rebuild)
marp slides.md --watch
```

---

## 6. reveal.js: Web Presentations

### 6.1 Basic Structure

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/white.css">
    <style>
        .reveal h1, .reveal h2 { color: #1a5f9e; }
        .reveal .highlight { color: #e68a00; font-weight: bold; }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            
            <section>
                <h1>Federated Learning for Medical AI</h1>
                <p>Privacy-Preserving Collaborative Training</p>
                <p><small>Nguyen Van A | HUST | June 2026</small></p>
            </section>
            
            <section>
                <h2>Research Motivation</h2>
                <ul>
                    <li>Medical data is siloed across hospitals</li>
                    <li>Privacy regulations prohibit data sharing</li>
                    <li class="highlight">Federated Learning enables collaborative training</li>
                </ul>
            </section>
            
            <section>
                <h2>Results</h2>
                <table>
                    <tr><th>Method</th><th>Accuracy</th><th>Rounds</th></tr>
                    <tr><td>FedAvg</td><td>92.1%</td><td>134</td></tr>
                    <tr><td class="highlight">Ours</td><td class="highlight">94.3%</td><td class="highlight">87</td></tr>
                </table>
            </section>
            
            <section>
                <h1>Thank You</h1>
                <p>Questions?</p>
            </section>
            
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
    <script>Reveal.initialize();</script>
</body>
</html>
```

---

## 7. Integration with AI Figure Generation

```
Research Content (markdown/paper)
    ↓
[1] Extract figures and concepts
    ↓
[2] ai-figure-generation → Create conceptual visuals
    │   • Architecture diagrams
    │   • Process flows
    │   • Abstract illustrations
    ↓
[3] slide-automation → Build slide structure
    │   • Insert AI-generated figures
    │   • Add data plots (matplotlib)
    │   • Format text and layout
    ↓
[4] Export final deck
    │   • .pptx for conference
    │   • .pdf for defense
    │   • .html for web
    ↓
Final Presentation
```

### Combined Workflow Example

```python
from ai_figure_generation import generate_diagram_prompt
from slide_automation import ResearchSlideDeck
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Generate AI figure
prompt = generate_diagram_prompt(
    concept="federated learning architecture",
    style="clean vector diagram",
    components=["5 hospitals", "aggregator", "encrypted gradients"]
)
# → Send to DALL-E/Midjourney → Save as 'fl_architecture.png'

# Step 2: Create data plot
fig, ax = plt.subplots(figsize=(8, 5))
rounds = np.arange(1, 101)
ax.plot(rounds, 1 - np.exp(-rounds/30), label='FedAvg', color='gray')
ax.plot(rounds, 1 - np.exp(-rounds/20), label='Ours', color='#1a5f9e')
ax.set_xlabel('Communication Rounds')
ax.set_ylabel('Accuracy')
ax.legend()
ax.set_title('Convergence Comparison')
plt.savefig('convergence_plot.png', dpi=150, bbox_inches='tight')

# Step 3: Build presentation
deck = ResearchSlideDeck("Federated Learning", "Nguyen Van A", "2026")
deck.add_figure_slide("Architecture", "fl_architecture.png")
deck.add_figure_slide("Results", "convergence_plot.png", 
                       "Faster convergence with proposed method")
deck.save("presentation.pptx")
```

---

## 8. Best Practices

### 8.1 Slide Design Rules

| Rule | Why | Implementation |
|---|---|---|
| **1 idea per slide** | Cognitive load | One title = one takeaway |
| **6×6 rule** | Readability | Max 6 bullets, max 6 words each |
| **Figure > Table > Text** | Visual processing | Convert tables to charts when possible |
| **Consistent branding** | Professionalism | Same colors, fonts, layout throughout |
| **Backup slides** | Q&A preparation | 5-10 extra slides after "Thank You" |

### 8.2 Version Control

```bash
# Store slides alongside research
git add slides/
git commit -m "slides: update results with experiment 042"

# Tag versions
git tag v1.0-defense
git tag v1.1-conference
```

### 8.3 Reusable Templates

```python
# Save template for future use
import json

template = {
    "colors": {
        "primary": "#1a5f9e",
        "secondary": "#2e8b57",
        "accent": "#e68a00"
    },
    "fonts": {
        "title": "Arial Bold",
        "body": "Arial"
    },
    "layout": {
        "title_height": 0.8,
        "content_top": 1.5,
        "margin": 0.5
    }
}

with open("slide_template.json", "w") as f:
    json.dump(template, f, indent=2)
```

---

## Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| Slide structure | `defense-prep` | Defense-specific slide organization |
| Figure insertion | `ai-figure-generation` | AI-generated conceptual visuals |
| Data plots | `experiment-tracking` | Publication-ready result figures |
| Academic tone | `technical-english-cs` | Slide text refinement |
| Presentation delivery | `defense-prep` | Q&A preparation, timing |

---

## References

- [python-pptx](https://python-pptx.readthedocs.io/) — Python library for PowerPoint
- [LaTeX Beamer](https://ctan.org/pkg/beamer) — LaTeX presentation class
- [Marp](https://marp.app/) — Markdown presentation ecosystem
- [reveal.js](https://revealjs.com/) — HTML presentation framework
- [Quarto](https://quarto.org/) — Reproducible research publishing
- [ai-figure-generation](./ai-figure-generation/SKILL.md) — AI-generated figures
