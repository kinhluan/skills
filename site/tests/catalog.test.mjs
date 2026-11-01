import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";
import {
  categories,
  getCatalog,
  getManifest,
  getRelatedSkills,
  renderSkill,
  repositoryRoot
} from "../src/lib/catalog.mjs";
import { fiveFactors, learningPaths, pursuits } from "../src/data/editorial.mjs";

const catalog = getCatalog();
const names = new Set(catalog.map((skill) => skill.name));

test("catalog mirrors the generated repository manifest", () => {
  const manifest = getManifest();
  assert.equal(catalog.length, manifest.skills.length);
  assert.equal(catalog.length, 64);
  assert.equal(names.size, catalog.length);

  for (const skill of catalog) {
    assert.ok(skill.description.length > 40, `${skill.name} needs a useful description`);
    assert.ok(skill.category?.id, `${skill.name} needs a category`);
    assert.ok(
      fs.existsSync(path.join(repositoryRoot(), "skills", skill.name, "SKILL.md")),
      `${skill.name} source is missing`
    );
  }
});

test("every editorial category has content", () => {
  for (const category of categories) {
    assert.ok(
      catalog.some((skill) => skill.category.id === category.id),
      `${category.id} has no skills`
    );
  }
});

test("editorial journeys only reference published skills", () => {
  const references = [
    ...fiveFactors.flatMap((factor) => factor.skills),
    ...pursuits.flatMap((pursuit) => pursuit.skills),
    ...learningPaths.flatMap((path) => path.steps)
  ];

  for (const slug of references) {
    assert.ok(names.has(slug), `Editorial content references unknown skill: ${slug}`);
  }
});

test("all skill markdown renders without executable markup", () => {
  for (const skill of catalog) {
    const rendered = renderSkill(skill.name);
    assert.ok(rendered.html.length > 100, `${skill.name} rendered body is unexpectedly short`);
    assert.doesNotMatch(rendered.html, /<script\b/i, `${skill.name} leaked a script tag`);
    assert.doesNotMatch(
      rendered.html,
      /\son[a-z]+\s*=/i,
      `${skill.name} leaked an event handler`
    );
    assert.doesNotMatch(
      rendered.html,
      /javascript:/i,
      `${skill.name} leaked a javascript URL`
    );
  }
});

test("related skills never include the source skill", () => {
  for (const skill of catalog) {
    const related = getRelatedSkills(skill);
    assert.ok(related.length <= 4);
    assert.ok(related.every((candidate) => candidate.name !== skill.name));
  }
});
