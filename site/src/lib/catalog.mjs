import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "marked";
import sanitizeHtml from "sanitize-html";

const repositoryCandidates = [
  process.cwd(),
  path.resolve(process.cwd(), ".."),
  fileURLToPath(new URL("../../..", import.meta.url))
];
const REPOSITORY_ROOT = repositoryCandidates.find(
  (candidate) =>
    fs.existsSync(path.join(candidate, "skills.json")) &&
    fs.existsSync(path.join(candidate, "skills"))
);

if (!REPOSITORY_ROOT) {
  throw new Error("Unable to locate the repository root containing skills.json and skills/.");
}
const MANIFEST_PATH = path.join(REPOSITORY_ROOT, "skills.json");
const SKILLS_ROOT = path.join(REPOSITORY_ROOT, "skills");
const SOURCE_BASE = "https://github.com/kinhluan/skills/blob/main";

export const categories = [
  {
    id: "research",
    label: "Research & Scholarship",
    shortLabel: "Research",
    description: "From a defensible question to reproducible evidence, publication, and defense."
  },
  {
    id: "architecture",
    label: "Architecture & Domain",
    shortLabel: "Architecture",
    description: "Boundaries, decisions, models, and systems designed to evolve."
  },
  {
    id: "engineering",
    label: "Engineering & Delivery",
    shortLabel: "Engineering",
    description: "Language craft, delivery flow, quality gates, and operational feedback."
  },
  {
    id: "product",
    label: "Product & Strategy",
    shortLabel: "Product",
    description: "Problem evidence, strategic choices, adoption, and measurable outcomes."
  },
  {
    id: "security",
    label: "Security & Resilience",
    shortLabel: "Security",
    description: "Threat-aware design, authorized assessment, hardening, and remediation."
  },
  {
    id: "agents",
    label: "Agents & Automation",
    shortLabel: "Agents",
    description: "Responsible agent orchestration, browser workflows, visuals, and automation."
  },
  {
    id: "language",
    label: "Language & Knowledge",
    shortLabel: "Language",
    description: "Technical expression, Vietnamese terminology, and durable reflection."
  }
];

const categoryById = new Map(categories.map((category) => [category.id, category]));

const securitySignals = new Set([
  "api-security",
  "authorization",
  "cloud-security",
  "container-security",
  "penetration-testing",
  "security-review",
  "threat-modeling"
]);

const securitySkillNames = new Set([
  "api-security",
  "cloud-security",
  "container-security",
  "penetration-testing",
  "security-analysis",
  "threat-modeling"
]);

const architectureSignals = new Set([
  "architecture",
  "c4",
  "c4-model",
  "clean-architecture",
  "ddd",
  "decision-records",
  "evolutionary"
]);

const productSignals = new Set([
  "adoption",
  "decision-making",
  "diffusion-of-innovations",
  "initiative-review",
  "jtbd",
  "product-analytics",
  "product-discovery",
  "product-management",
  "product-strategy",
  "strategy",
  "ux-research"
]);

const agentSignals = new Set([
  "agent-governance",
  "ai-image",
  "automation",
  "browser",
  "routing",
  "skill-selection"
]);

const languageSkillNames = new Set([
  "second-brain-reflection",
  "technical-english-cs",
  "vietnamese-cs-terminology",
  "vietnamese-writing-standard"
]);

const acronymMap = new Map([
  ["adr", "ADR"],
  ["ai", "AI"],
  ["api", "API"],
  ["c4", "C4"],
  ["ci", "CI"],
  ["cs", "CS"],
  ["ddd", "DDD"],
  ["dora", "DORA"],
  ["dqn", "DQN"],
  ["git", "Git"],
  ["golang", "Go"],
  ["javascript", "JavaScript"],
  ["kubernetes", "Kubernetes"],
  ["phd", "PhD"],
  ["q1", "Q1"],
  ["sota", "SOTA"],
  ["typescript", "TypeScript"],
  ["ux", "UX"]
]);

function intersects(tags, signals) {
  return tags.some((tag) => signals.has(tag));
}

function classify(skill) {
  const tags = skill.tags ?? [];
  if (languageSkillNames.has(skill.name)) return categoryById.get("language");
  if (securitySkillNames.has(skill.name) || intersects(tags, securitySignals)) {
    return categoryById.get("security");
  }
  if (intersects(tags, architectureSignals)) return categoryById.get("architecture");
  if (intersects(tags, productSignals)) return categoryById.get("product");
  if (tags.includes("research") || tags.includes("phd")) return categoryById.get("research");
  if (intersects(tags, agentSignals)) return categoryById.get("agents");
  return categoryById.get("engineering");
}

export function formatSkillName(name) {
  return name
    .split("-")
    .map((word) => acronymMap.get(word) ?? `${word.charAt(0).toUpperCase()}${word.slice(1)}`)
    .join(" ");
}

let catalogCache;

export function getManifest() {
  return JSON.parse(fs.readFileSync(MANIFEST_PATH, "utf8"));
}

export function getCatalog() {
  if (catalogCache) return catalogCache;

  const manifest = getManifest();
  catalogCache = manifest.skills
    .map((skill) => {
      const category = classify(skill);
      return {
        ...skill,
        title: formatSkillName(skill.name),
        category,
        sourceUrl: `${SOURCE_BASE}/skills/${skill.name}/SKILL.md`
      };
    })
    .sort((left, right) => left.title.localeCompare(right.title));

  return catalogCache;
}

export function getSkill(slug) {
  return getCatalog().find((skill) => skill.name === slug);
}

function stripFrontmatter(markdown) {
  return markdown.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "");
}

function stripFirstHeading(markdown) {
  return markdown.replace(/^#\s+.+\r?\n+/, "");
}

function relativeSourceUrl(slug, href) {
  if (
    !href ||
    href.startsWith("#") ||
    href.startsWith("/") ||
    /^[a-z][a-z\d+.-]*:/i.test(href)
  ) {
    return href;
  }

  const relativePath = path.posix.normalize(path.posix.join("skills", slug, href));
  return `${SOURCE_BASE}/${relativePath}`;
}

function headingSlug(text, used) {
  const base = text
    .replace(/<[^>]+>/g, "")
    .replace(/&[a-z\d#]+;/gi, " ")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9\u4e00-\u9fff]+/g, "-")
    .replace(/^-|-$/g, "") || "section";

  const count = used.get(base) ?? 0;
  used.set(base, count + 1);
  return count === 0 ? base : `${base}-${count + 1}`;
}

function addHeadingIds(html) {
  const used = new Map();
  const toc = [];
  const output = html.replace(/<h([23])>([\s\S]*?)<\/h\1>/g, (match, level, content) => {
    const id = headingSlug(content, used);
    const label = content.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&");
    toc.push({ level: Number(level), id, label });
    return `<h${level} id="${id}">${content}</h${level}>`;
  });

  return { html: output, toc };
}

function markdownWordCount(markdown) {
  return markdown
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/`[^`]+`/g, " ")
    .replace(/[#>*_[\]()|-]/g, " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean).length;
}

export function renderSkill(slug) {
  const skillPath = path.join(SKILLS_ROOT, slug, "SKILL.md");
  const original = fs.readFileSync(skillPath, "utf8");
  const markdown = stripFirstHeading(stripFrontmatter(original));
  const rendered = marked.parse(markdown, { gfm: true });
  const clean = sanitizeHtml(rendered, {
    allowedTags: [
      ...sanitizeHtml.defaults.allowedTags,
      "details",
      "summary",
      "figure",
      "figcaption"
    ],
    allowedAttributes: {
      a: ["href", "title", "target", "rel"],
      code: ["class"],
      h2: ["id"],
      h3: ["id"],
      img: ["src", "alt", "title", "loading"],
      th: ["align"],
      td: ["align"]
    },
    allowedSchemes: ["http", "https", "mailto"],
    transformTags: {
      a: (tagName, attributes) => {
        const href = relativeSourceUrl(slug, attributes.href);
        const external = /^https?:/i.test(href);
        return {
          tagName,
          attribs: {
            ...attributes,
            href,
            ...(external ? { target: "_blank", rel: "noreferrer" } : {})
          }
        };
      },
      img: (tagName, attributes) => ({
        tagName,
        attribs: {
          ...attributes,
          src: relativeSourceUrl(slug, attributes.src),
          loading: "lazy"
        }
      })
    }
  });
  const withHeadings = addHeadingIds(clean);

  return {
    ...withHeadings,
    readingMinutes: Math.max(2, Math.ceil(markdownWordCount(markdown) / 220))
  };
}

export function getRelatedSkills(skill, limit = 4) {
  const genericTags = new Set(["research", "phd", "architecture", "security"]);
  const sourceTags = new Set((skill.tags ?? []).filter((tag) => !genericTags.has(tag)));

  return getCatalog()
    .filter((candidate) => candidate.name !== skill.name)
    .map((candidate) => {
      const shared = (candidate.tags ?? []).filter((tag) => sourceTags.has(tag)).length;
      const sameCategory = candidate.category.id === skill.category.id ? 1 : 0;
      return { candidate, score: shared * 3 + sameCategory };
    })
    .filter(({ score }) => score > 0)
    .sort((left, right) => right.score - left.score || left.candidate.title.localeCompare(right.candidate.title))
    .slice(0, limit)
    .map(({ candidate }) => candidate);
}

export function repositoryRoot() {
  return REPOSITORY_ROOT;
}
