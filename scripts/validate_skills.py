#!/usr/bin/env python3
"""Validate source skills and every release surface in this repository."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

import yaml

from sync_manifest import build_manifest


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MANIFEST_PATH = ROOT / "skills.json"
MAX_SKILL_LINES = 500
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "metadata",
    "license",
    "compatibility",
    "allowed-tools",
}
IGNORED_RESOURCE_PARTS = {"__pycache__", ".DS_Store"}


@dataclass(frozen=True)
class Issue:
    path: Path
    message: str

    def render(self) -> str:
        try:
            display_path = self.path.relative_to(ROOT)
        except ValueError:
            display_path = self.path
        return f"{display_path}: {self.message}"


def parse_frontmatter(path: Path) -> tuple[dict[str, object] | None, str, list[Issue]]:
    issues: list[Issue] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text, [Issue(path, "missing opening YAML frontmatter delimiter")]

    try:
        closing_index = next(
            index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"
        )
    except StopIteration:
        return None, text, [Issue(path, "missing closing YAML frontmatter delimiter")]

    try:
        metadata = yaml.safe_load("\n".join(lines[1:closing_index]))
    except yaml.YAMLError as exc:
        return None, text, [Issue(path, f"invalid YAML frontmatter: {exc}")]

    if not isinstance(metadata, dict):
        issues.append(Issue(path, "frontmatter must be a YAML mapping"))
        return None, text, issues

    return metadata, text, issues


def source_skill_dirs() -> list[Path]:
    return sorted(
        path
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )


def validate_skill(skill_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [Issue(skill_dir, "missing required SKILL.md")]

    metadata, text, parse_issues = parse_frontmatter(skill_md)
    issues.extend(parse_issues)
    if metadata is None:
        return issues

    unknown_keys = sorted(set(metadata) - ALLOWED_FRONTMATTER_KEYS)
    if unknown_keys:
        issues.append(
            Issue(skill_md, f"unsupported frontmatter keys: {', '.join(unknown_keys)}")
        )

    name = metadata.get("name")
    if not isinstance(name, str) or not name:
        issues.append(Issue(skill_md, "frontmatter 'name' must be a non-empty string"))
    else:
        if name != skill_dir.name:
            issues.append(
                Issue(skill_md, f"name '{name}' does not match directory '{skill_dir.name}'")
            )
        if len(name) > MAX_NAME_LENGTH or not NAME_PATTERN.fullmatch(name):
            issues.append(
                Issue(
                    skill_md,
                    "name must be <=64 characters of lowercase letters, digits, and hyphens",
                )
            )

    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        issues.append(
            Issue(skill_md, "frontmatter 'description' must be a non-empty string")
        )
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        issues.append(
            Issue(
                skill_md,
                f"description is {len(description)} characters; maximum is "
                f"{MAX_DESCRIPTION_LENGTH}",
            )
        )

    line_count = len(text.splitlines())
    if line_count > MAX_SKILL_LINES:
        issues.append(
            Issue(
                skill_md,
                f"{line_count} lines exceeds the {MAX_SKILL_LINES}-line "
                "progressive-disclosure limit",
            )
        )

    if (skill_dir / "README.md").exists():
        issues.append(
            Issue(
                skill_dir / "README.md",
                "skill-local README is not a runtime resource; move essential guidance "
                "to SKILL.md or references/",
            )
        )

    for nested_skill in skill_dir.glob("*/SKILL.md"):
        issues.append(
            Issue(nested_skill, "nested skill duplicates are not allowed inside a skill")
        )

    references_dir = skill_dir / "references"
    if references_dir.is_dir():
        for reference in sorted(references_dir.rglob("*")):
            if not reference.is_file():
                continue
            relative_reference = reference.relative_to(skill_dir).as_posix()
            if relative_reference not in text:
                issues.append(
                    Issue(
                        reference,
                        f"orphan reference; link '{relative_reference}' directly from SKILL.md",
                    )
                )

    return issues


def without_fenced_code(text: str) -> str:
    visible_lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        marker = "```" if stripped.startswith("```") else "~~~" if stripped.startswith("~~~") else None
        if marker:
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is None:
            visible_lines.append(line)
    return "\n".join(visible_lines)


def validate_markdown_links() -> list[Issue]:
    issues: list[Issue] = []
    for markdown_file in sorted(SKILLS_DIR.rglob("*.md")):
        text = without_fenced_code(markdown_file.read_text(encoding="utf-8"))
        for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
            target = raw_target.strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split(maxsplit=1)[0]
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
                or "{" in target
                or "}" in target
            ):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            resolved = (markdown_file.parent / path_part).resolve()
            if not resolved.exists():
                issues.append(Issue(markdown_file, f"broken relative link: {target}"))
    return issues


def validate_manifest() -> list[Issue]:
    issues: list[Issue] = []
    try:
        current = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [Issue(MANIFEST_PATH, f"cannot load manifest: {exc}")]

    expected = build_manifest(MANIFEST_PATH, SKILLS_DIR)
    if current != expected:
        issues.append(
            Issue(
                MANIFEST_PATH,
                "manifest is stale; run 'make sync-manifest' and commit the result",
            )
        )
    return issues


def load_router_module():
    router_path = ROOT / "scripts" / "skill_router.py"
    spec = importlib.util.spec_from_file_location("skill_router", router_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load skill router")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(spec.name, None)
    return module


def validate_router() -> list[Issue]:
    router_path = ROOT / "scripts" / "skill_router.py"
    try:
        module = load_router_module()
        routed_names = module.route_names()
    except Exception as exc:  # noqa: BLE001 - validator must report load failures
        return [Issue(router_path, f"cannot load routes: {exc}")]

    issues: list[Issue] = []
    if len(routed_names) != len(set(routed_names)):
        duplicates = sorted(
            name for name in set(routed_names) if routed_names.count(name) > 1
        )
        issues.append(Issue(router_path, f"duplicate routes: {', '.join(duplicates)}"))

    source_names = {path.name for path in source_skill_dirs()}
    route_names = set(routed_names)
    missing = sorted(source_names - route_names)
    unknown = sorted(route_names - source_names)
    if missing:
        issues.append(Issue(router_path, f"skills without routes: {', '.join(missing)}"))
    if unknown:
        issues.append(Issue(router_path, f"routes for unknown skills: {', '.join(unknown)}"))
    return issues


def validate_release_config() -> list[Issue]:
    issues: list[Issue] = []
    version_paths = [
        (MANIFEST_PATH, ("version",)),
        (ROOT / ".claude-plugin" / "plugin.json", ("version",)),
        (
            ROOT / ".claude-plugin" / "marketplace.json",
            ("plugins", 0, "version"),
        ),
        (ROOT / "gemini-extension.json", ("version",)),
    ]
    versions: dict[Path, object] = {}
    for path, keys in version_paths:
        try:
            value: object = json.loads(path.read_text(encoding="utf-8"))
            for key in keys:
                value = value[key]  # type: ignore[index]
            versions[path] = value
        except (OSError, json.JSONDecodeError, KeyError, IndexError, TypeError) as exc:
            issues.append(Issue(path, f"cannot read release version: {exc}"))
    if len(set(versions.values())) > 1:
        rendered = ", ".join(
            f"{path.relative_to(ROOT)}={version}" for path, version in versions.items()
        )
        issues.append(Issue(ROOT, f"release versions differ: {rendered}"))

    skills_root = ROOT / "skills"
    if not skills_root.is_dir() or skills_root.is_symlink():
        issues.append(
            Issue(skills_root, "must be the real canonical skills directory, not a symlink")
        )
    legacy_root = ROOT / ".agent-skills"
    if legacy_root.exists() or legacy_root.is_symlink():
        issues.append(Issue(legacy_root, "legacy duplicate source must not exist"))

    hooks_path = ROOT / "hooks" / "hooks.json"
    try:
        hooks = json.loads(hooks_path.read_text(encoding="utf-8"))
        handlers = hooks["hooks"]["UserPromptSubmit"][0]["hooks"]
        command = handlers[0]
        if command.get("command") != "python3" or command.get("args") != [
            "${CLAUDE_PLUGIN_ROOT}/scripts/skill_router.py"
        ]:
            issues.append(
                Issue(hooks_path, "router hook must use portable Claude plugin exec form")
            )
    except (OSError, json.JSONDecodeError, KeyError, IndexError, TypeError) as exc:
        issues.append(Issue(hooks_path, f"invalid Claude plugin hook config: {exc}"))

    for path in [
        ROOT / "Makefile",
        ROOT / "CLAUDE.md",
        ROOT / "GEMINI.md",
        ROOT / "scripts" / "skill_router.py",
    ]:
        if path.exists() and re.search(r"/Users/[^/\s]+/", path.read_text(encoding="utf-8")):
            issues.append(Issue(path, "contains a machine-specific absolute user path"))
    return issues


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("ERROR: canonical skills directory is missing", file=sys.stderr)
        return 1

    issues: list[Issue] = []
    for skill_dir in source_skill_dirs():
        issues.extend(validate_skill(skill_dir))
    issues.extend(validate_markdown_links())
    issues.extend(validate_manifest())
    issues.extend(validate_router())
    issues.extend(validate_release_config())

    if issues:
        print(f"Validation failed with {len(issues)} error(s):")
        for issue in sorted(issues, key=lambda item: item.render()):
            print(f"  - {issue.render()}")
        return 1

    print(f"Validated {len(source_skill_dirs())} skills and all release surfaces.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
