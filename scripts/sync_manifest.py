#!/usr/bin/env python3
"""Synchronize skills.json entries from the canonical skills tree."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
IGNORED_RESOURCE_PARTS = {"__pycache__", ".DS_Store"}


def parse_frontmatter(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: missing frontmatter")
    try:
        closing_index = next(
            index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError(f"{path}: missing closing frontmatter delimiter") from exc
    metadata = yaml.safe_load("\n".join(lines[1:closing_index]))
    if not isinstance(metadata, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return metadata


def publishable_files(skill_dir: Path) -> list[str]:
    files: list[str] = []
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(skill_dir)
        if any(part in IGNORED_RESOURCE_PARTS or part.endswith(".pyc") for part in relative.parts):
            continue
        files.append(relative.as_posix())
    return files


def build_manifest(manifest_path: Path, skills_dir: Path) -> dict[str, object]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries: list[dict[str, object]] = []
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        metadata = parse_frontmatter(skill_dir / "SKILL.md")
        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError(f"{skill_dir}: name and description must be strings")

        entry: dict[str, object] = {
            "name": name,
            "path": f"./skills/{skill_dir.name}",
            "files": publishable_files(skill_dir),
            "description": description,
        }
        skill_metadata = metadata.get("metadata")
        if isinstance(skill_metadata, dict):
            tags = skill_metadata.get("tags")
            if isinstance(tags, list) and all(isinstance(tag, str) for tag in tags):
                entry["tags"] = tags
        entries.append(entry)

    manifest["skills"] = entries
    return manifest


def render_manifest(manifest: dict[str, object]) -> str:
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if skills.json is stale")
    args = parser.parse_args()

    manifest_path = ROOT / "skills.json"
    skills_dir = ROOT / "skills"
    rendered = render_manifest(build_manifest(manifest_path, skills_dir))
    current = manifest_path.read_text(encoding="utf-8")
    if args.check:
        if current != rendered:
            print("skills.json is stale; run 'make sync-manifest'")
            return 1
        print("skills.json is synchronized.")
        return 0

    manifest_path.write_text(rendered, encoding="utf-8")
    print(f"Synchronized {len(json.loads(rendered)['skills'])} skills in skills.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
