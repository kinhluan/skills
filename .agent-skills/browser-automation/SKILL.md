---
name: browser-automation
description: Browser automation, web scraping, Chrome Extension development, and UI automation with Playwright/CDP. Use when building Chrome extensions, automating web workflows, scraping data, filling forms, or integrating web content with agent skills.
metadata:
  tags: ["browser", "automation", "chrome-extension", "playwright", "web-scraping", "ui-automation", "cdp", "puppeteer", "form-filling", "content-extraction"]
  triggers: ["chrome extension", "browser automation", "web scraping", "playwright", "puppeteer", "form filling", "ui automation", "crawl web", "extract data from page", "automate browser", "trình duyệt", "tự động hóa web", "mở rộng chrome"]
  version: "1.0.0"
---

# Browser Automation & Chrome Extension Skill

Build browser automation workflows, Chrome Extensions, and web scraping pipelines that integrate with the kinhluan/skills system.

## When to Use

- Building a Chrome Extension or browser extension
- Automating web workflows (form filling, clicking, navigation)
- Scraping data from websites
- Extracting and summarizing web page content
- Connecting browser actions to agent skills
- Using Playwright, Puppeteer, or Chrome DevTools Protocol (CDP)
- "Tự động hóa trình duyệt", "mở rộng Chrome", "cào dữ liệu web"

---

## Chrome Extension Architecture (Manifest V3)

### Core Components

| Component | Runs In | Purpose |
|-----------|---------|---------|
| **Popup** | User click | UI panel — skill browser, search, settings |
| **Content Script** | Page context | DOM access — extract data, inject automation |
| **Service Worker** | Background | Event handling — fetch skills, caching, messaging |
| **Options Page** | Tab | Configuration — API keys, preferences |

### Minimal Manifest V3

```json
{
  "manifest_version": 3,
  "name": "KinhLuan Skills Browser",
  "version": "1.0.0",
  "permissions": ["activeTab", "storage", "scripting"],
  "host_permissions": ["https://raw.githubusercontent.com/*"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": { "16": "icon16.png", "48": "icon48.png", "128": "icon128.png" }
  },
  "background": { "service_worker": "background.js" },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "run_at": "document_idle"
    }
  ]
}
```

### Permission Minimization Rule

> **Start with least privilege.** Only add permissions when a feature genuinely needs them.

| Feature | Minimum Permission |
|---------|-------------------|
| Read current page | `activeTab` |
| Read any page | `host_permissions` (specific domains) |
| Store settings | `storage` |
| Inject scripts | `scripting` |
| Cross-origin fetch | `host_permissions` (target origins) |

---

## Content Extraction Strategies

### 1. Readability-Style Article Extraction

```typescript
// content.ts — Extract main article content
function extractArticle(): { title: string; content: string; url: string } {
  const title = document.title;
  const url = location.href;

  // Heuristic: find the largest text block
  const candidates = Array.from(document.querySelectorAll('article, main, [role="main"], .content, .post, .entry'));
  let best = candidates[0];
  if (!best) {
    // Fallback: score paragraphs by text density
    const paragraphs = Array.from(document.querySelectorAll('p'));
    const scored = paragraphs.map(p => ({
      el: p.parentElement!,
      score: p.innerText.length + (p.querySelectorAll('p').length * 20)
    }));
    scored.sort((a, b) => b.score - a.score);
    best = scored[0]?.el || document.body;
  }

  return { title, content: best.innerText.trim(), url };
}

// Send to background/service worker
chrome.runtime.sendMessage({ type: 'EXTRACTED_CONTENT', payload: extractArticle() });
```

### 2. Structured Data Extraction (JSON-LD / Microdata)

```typescript
function extractStructuredData(): Record<string, unknown>[] {
  const jsonLd = Array.from(document.querySelectorAll('script[type="application/ld+json"]'))
    .map(s => {
      try { return JSON.parse(s.textContent || '{}'); } catch { return null; }
    })
    .filter(Boolean);

  const microdata = Array.from(document.querySelectorAll('[itemscope]'))
    .map(el => {
      const props: Record<string, string> = {};
      el.querySelectorAll('[itemprop]').forEach(p => {
        props[p.getAttribute('itemprop')!] = p.textContent || '';
      });
      return { type: el.getAttribute('itemtype'), ...props };
    });

  return [...jsonLd, ...microdata];
}
```

### 3. Table & List Scraping

```typescript
function extractTables(): Array<{ headers: string[]; rows: string[][] }> {
  return Array.from(document.querySelectorAll('table')).map(table => {
    const headers = Array.from(table.querySelectorAll('th')).map(th => th.innerText.trim());
    const rows = Array.from(table.querySelectorAll('tr')).slice(headers.length ? 0 : 1).map(tr =>
      Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim())
    ).filter(r => r.length > 0);
    return { headers: headers.length ? headers : rows.shift() || [], rows };
  });
}
```

---

## UI Automation Patterns

### Playwright Integration (Local Agent → Browser)

```typescript
// Agent-side: Control browser via Playwright
import { chromium, Page } from 'playwright';

async function runAutomation(skillPrompt: string, url: string) {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(url);

  // Parse skill instructions into actions
  const actions = parseSkillActions(skillPrompt); // [{ type: 'click', selector: '...' }, ...]

  for (const action of actions) {
    switch (action.type) {
      case 'click':
        await page.click(action.selector);
        break;
      case 'type':
        await page.fill(action.selector, action.value);
        break;
      case 'wait':
        await page.waitForSelector(action.selector, { timeout: action.timeout || 5000 });
        break;
      case 'scroll':
        await page.evaluate(() => window.scrollBy(0, window.innerHeight));
        break;
      case 'extract':
        return await page.evaluate(extractArticle);
    }
  }

  await browser.close();
}
```

### Chrome DevTools Protocol (CDP) — Direct Browser Control

```typescript
// Connect to existing Chrome instance via CDP
import CDP from 'chrome-remote-interface';

async function cdpExtract(url: string) {
  const client = await CDP({ port: 9222 });
  const { Page, Runtime } = client;

  await Page.enable();
  await Page.navigate({ url });
  await Page.loadEventFired();

  // Execute extraction function in browser context
  const { result } = await Runtime.evaluate({
    expression: `(${extractArticle.toString()})()`,
    returnByValue: true
  });

  await client.close();
  return result.value;
}
```

### Element Selection Strategy

| Strategy | Selector | Best For |
|----------|----------|----------|
| **Test ID** | `[data-testid="submit-btn"]` | Stable, semantic |
| **ARIA** | `[aria-label="Search"]` | Accessible, reliable |
| **Role** | `[role="button"]` | Semantic markup |
| **Text** | `text="Submit"` | User-visible labels |
| **CSS** | `.btn-primary` | Visual styling |
| **XPath** | `//button[contains(.,"Submit")]` | Complex matching |

> **Priority**: `data-testid` > `aria-label` > `role` > `text` > `CSS class` > `XPath`

---

## Form Filling Patterns

### Auto-Detect & Fill

```typescript
interface FieldMapping {
  label: string;
  selector: string;
  type: 'text' | 'email' | 'select' | 'checkbox' | 'radio';
  value: string;
}

function detectFormFields(): FieldMapping[] {
  const fields: FieldMapping[] = [];

  document.querySelectorAll('input, select, textarea').forEach(el => {
    const input = el as HTMLInputElement;
    const label = findLabel(input);
    const type = input.type === 'select-one' ? 'select' : (input.type as FieldMapping['type']);
    fields.push({ label, selector: getSelector(input), type, value: '' });
  });

  return fields;
}

function findLabel(input: HTMLElement): string {
  const id = input.id;
  if (id) {
    const label = document.querySelector(`label[for="${id}"]`);
    if (label) return label.textContent?.trim() || '';
  }
  const parent = input.closest('label');
  if (parent) return parent.textContent?.trim() || '';
  return input.placeholder || input.name || input.getAttribute('aria-label') || '';
}

function getSelector(el: HTMLElement): string {
  if (el.id) return `#${el.id}`;
  if (el.getAttribute('data-testid')) return `[data-testid="${el.getAttribute('data-testid')}"]`;
  const tag = el.tagName.toLowerCase();
  const classes = Array.from(el.classList).join('.');
  return classes ? `${tag}.${classes}` : tag;
}
```

### Batch Fill from Skill Data

```typescript
async function fillForm(data: Record<string, string>) {
  const fields = detectFormFields();

  for (const [key, value] of Object.entries(data)) {
    const field = fields.find(f =>
      f.label.toLowerCase().includes(key.toLowerCase()) ||
      f.selector.includes(key.toLowerCase())
    );
    if (!field) continue;

    const el = document.querySelector(field.selector) as HTMLInputElement;
    if (!el) continue;

    if (field.type === 'select') {
      const option = Array.from(el.querySelectorAll('option')).find(o =>
        o.textContent?.toLowerCase().includes(value.toLowerCase())
      );
      if (option) (el as HTMLSelectElement).value = option.value;
    } else if (field.type === 'checkbox') {
      el.checked = value.toLowerCase() === 'true' || value === 'yes';
    } else {
      el.value = value;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }
}
```

---

## Skill Routing from Web Content

### Intent Matching on Extracted Content

```typescript
// Lightweight client-side routing (mirrors router skill)
const WEB_ROUTES = [
  { skill: 'sota-survey', keywords: ['survey', 'literature', 'review', 'papers', 'state of the art', 'related work'] },
  { skill: 'research-question', keywords: ['research question', 'hypothesis', 'contribution', 'novelty'] },
  { skill: 'c4-model', keywords: ['architecture', 'system diagram', 'c4 model', 'container', 'component'] },
  { skill: 'ddd-core', keywords: ['domain driven', 'bounded context', 'ubiquitous language', 'ddd'] },
  { skill: 'python-development', keywords: ['python', 'fastapi', 'pydantic', 'django', 'flask'] },
  { skill: 'javascript-typescript', keywords: ['javascript', 'typescript', 'react', 'node.js', 'frontend'] },
  { skill: 'security-analysis', keywords: ['security', 'vulnerability', 'owasp', 'pentest', 'xss', 'sql injection'] },
  { skill: 'docker-containerization', keywords: ['docker', 'container', 'dockerfile', 'docker-compose'] },
  { skill: 'kubernetes-orchestration', keywords: ['kubernetes', 'k8s', 'pod', 'deployment', 'helm'] },
  { skill: 'business-product-leadership', keywords: ['product strategy', 'jtbd', 'mvp', 'product market'] },
];

function routeFromContent(text: string): string[] {
  const lower = text.toLowerCase();
  const matched = new Set<string>();
  for (const route of WEB_ROUTES) {
    if (route.keywords.some(kw => lower.includes(kw))) matched.add(route.skill);
  }
  return Array.from(matched).slice(0, 3);
}
```

### Full Workflow: Page → Skill → Agent

```
1. User clicks extension on any page
2. Content script extracts article text
3. Extension runs routeFromContent(text)
4. Suggests top 3 matching kinhluan skills
5. User selects a skill
6. Extension fetches SKILL.md from raw GitHub
7. Formats prompt: [SKILL instructions] + [page context]
8. Copies to clipboard OR opens agent chat with pre-filled prompt
```

---

## Security & Privacy

### CSP Compliance

```json
{
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'; connect-src 'self' https://raw.githubusercontent.com"
  }
}
```

### CORS Handling

```typescript
// Fetch skills.json from raw GitHub (CORS-enabled)
const SKILLS_JSON_URL = 'https://raw.githubusercontent.com/kinhluan/skills/main/skills.json';

async function fetchSkills(): Promise<SkillsManifest> {
  const res = await fetch(SKILLS_JSON_URL);
  if (!res.ok) throw new Error(`Failed to fetch skills: ${res.status}`);
  return res.json();
}

// Cache in chrome.storage
async function cacheSkills(skills: SkillsManifest) {
  await chrome.storage.local.set({ skillsCache: skills, skillsCacheTime: Date.now() });
}
```

### Data Sanitization

```typescript
function sanitizeForPrompt(text: string, maxLength = 8000): string {
  return text
    .replace(/[<>]/g, '')           // Strip HTML-like chars
    .replace(/\s+/g, ' ')           // Collapse whitespace
    .trim()
    .slice(0, maxLength);
}
```

### Permission Checklist

- [ ] Use `activeTab` instead of broad host permissions where possible
- [ ] Never inject scripts from remote URLs
- [ ] Sanitize all DOM-extracted data before sending to APIs
- [ ] Store sensitive data in `chrome.storage.local` (encrypted at rest by OS)
- [ ] Declare minimum permissions in manifest
- [ ] Use `chrome.scripting.executeScript` with function injection (not string eval)

---

## Integration with kinhluan/skills

### Fetch Skill from GitHub Raw

```typescript
const RAW_BASE = 'https://raw.githubusercontent.com/kinhluan/skills/main/.agent-skills';

async function fetchSkill(skillName: string): Promise<{ md: string; toon: string }> {
  const [mdRes, toonRes] = await Promise.all([
    fetch(`${RAW_BASE}/${skillName}/SKILL.md`),
    fetch(`${RAW_BASE}/${skillName}/SKILL.toon`).catch(() => null)
  ]);

  const md = await mdRes.text();
  const toon = toonRes ? await toonRes.text() : '';
  return { md, toon };
}
```

### Parse SKILL.md Frontmatter

```typescript
interface SkillFrontmatter {
  name: string;
  description: string;
  metadata: { tags: string[]; triggers?: string[]; version?: string };
}

function parseFrontmatter(md: string): { frontmatter: SkillFrontmatter; body: string } {
  const match = md.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) throw new Error('Invalid SKILL.md: missing frontmatter');

  // Simple YAML parser (sufficient for skill frontmatter)
  const yaml = match[1];
  const body = match[2].trim();

  const frontmatter: any = {};
  let currentKey = '';
  for (const line of yaml.split('\n')) {
    const keyMatch = line.match(/^(\w+):\s*(.*)$/);
    if (keyMatch) {
      currentKey = keyMatch[1];
      frontmatter[currentKey] = keyMatch[2].replace(/^["']|["']$/g, '');
    } else if (line.trim().startsWith('- ')) {
      const val = line.trim().slice(2).replace(/^["']|["']$/g, '');
      if (!frontmatter[currentKey]) frontmatter[currentKey] = [];
      (frontmatter[currentKey] as string[]).push(val);
    }
  }

  return { frontmatter, body };
}
```

---

## Quick Reference

### Chrome Extension Message Passing

```typescript
// Content → Background
chrome.runtime.sendMessage({ type: 'ACTION', payload: data });

// Background → Content (specific tab)
chrome.tabs.sendMessage(tabId, { type: 'ACTION', payload: data });

// Background → Popup (via storage or direct messaging)
chrome.storage.local.set({ key: value });
```

### Playwright Quick Start

```bash
npm init -y
npm install playwright
npx playwright install chromium
```

```typescript
import { chromium } from 'playwright';
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
const text = await page.innerText('article');
await browser.close();
```

### CDP Quick Start

```bash
# Launch Chrome with remote debugging
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
```

```typescript
import CDP from 'chrome-remote-interface';
const client = await CDP({ port: 9222 });
```

---

## Resources

- [Chrome Extension Docs](https://developer.chrome.com/docs/extensions/)
- [Manifest V3 Migration](https://developer.chrome.com/docs/extensions/develop/migrate)
- [Playwright Docs](https://playwright.dev/)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
- [kinhluan/skills Repo](https://github.com/kinhluan/skills)
