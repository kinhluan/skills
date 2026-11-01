import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { getCatalog } from "../src/lib/catalog.mjs";

const DIST = path.resolve(process.cwd(), "dist");
const BASE_PATH = "/skills";

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const target = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(target) : [target];
  });
}

function outputForUrl(urlPath) {
  const withoutBase = urlPath.slice(BASE_PATH.length) || "/";
  const decoded = decodeURIComponent(withoutBase);
  const relative = decoded.replace(/^\/+/, "");

  if (!relative) return path.join(DIST, "index.html");
  if (decoded.endsWith("/")) return path.join(DIST, relative, "index.html");
  return path.join(DIST, relative);
}

assert.ok(fs.existsSync(DIST), "site/dist does not exist; run the build first");

const htmlFiles = walk(DIST).filter((file) => file.endsWith(".html"));
const expectedRoutes = [
  "index.html",
  "404.html",
  "about/index.html",
  "paths/index.html",
  "principles/index.html",
  "pursuits/index.html",
  "library/index.html",
  ...getCatalog().map((skill) => `library/${skill.name}/index.html`)
];

for (const route of expectedRoutes) {
  assert.ok(fs.existsSync(path.join(DIST, route)), `Missing generated route: ${route}`);
}

for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  assert.doesNotMatch(html, />undefined</, `${file} contains unresolved content`);
  assert.doesNotMatch(html, /(?:href|src)="undefined"/, `${file} contains an undefined URL`);

  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const value = match[1];
    if (
      !value ||
      value.startsWith("#") ||
      value.startsWith("mailto:") ||
      value.startsWith("data:") ||
      /^https?:\/\//.test(value)
    ) {
      continue;
    }

    const url = new URL(value, "https://kinhluan.github.io");
    if (!url.pathname.startsWith(BASE_PATH)) {
      assert.fail(`${file} contains a root URL without the GitHub Pages base: ${value}`);
    }

    const target = outputForUrl(url.pathname);
    assert.ok(fs.existsSync(target), `${file} links to missing output: ${value}`);
  }
}

console.log(`Verified ${expectedRoutes.length} routes and internal links across ${htmlFiles.length} pages.`);
