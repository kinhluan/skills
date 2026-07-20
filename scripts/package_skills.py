#!/usr/bin/env python3
"""Build deterministic .skill archives from canonical skill sources."""

from __future__ import annotations

import argparse
import io
import os
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
IGNORED_PARTS = {"__pycache__", ".DS_Store"}
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def source_files(skill_dir: Path) -> list[Path]:
    return [
        path
        for path in sorted(skill_dir.rglob("*"))
        if path.is_file()
        and not any(
            part in IGNORED_PARTS or part.endswith(".pyc")
            for part in path.relative_to(skill_dir).parts
        )
    ]


def archive_bytes(skill_dir: Path) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(
        output, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in source_files(skill_dir):
            relative = path.relative_to(skill_dir).as_posix()
            info = zipfile.ZipInfo(
                filename=f"{skill_dir.name}/{relative}",
                date_time=ZIP_TIMESTAMP,
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (0o100644 & 0xFFFF) << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    return output.getvalue()


def skill_dirs() -> list[Path]:
    return sorted(
        path
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )


def clean() -> int:
    if not DIST_DIR.exists():
        return 0
    removed = 0
    for archive in DIST_DIR.glob("*.skill"):
        archive.unlink()
        removed += 1
    print(f"Removed {removed} generated package(s).")
    return 0


def check() -> int:
    expected = {f"{skill.name}.skill": archive_bytes(skill) for skill in skill_dirs()}
    actual_paths = {path.name: path for path in DIST_DIR.glob("*.skill")}
    missing = sorted(set(expected) - set(actual_paths))
    stale = sorted(
        name
        for name in set(expected) & set(actual_paths)
        if actual_paths[name].read_bytes() != expected[name]
    )
    extra = sorted(set(actual_paths) - set(expected))
    if missing or stale or extra:
        if missing:
            print(f"Missing packages: {', '.join(missing)}")
        if stale:
            print(f"Stale packages: {', '.join(stale)}")
        if extra:
            print(f"Unexpected packages: {', '.join(extra)}")
        print("Run 'make package' and commit the resulting dist changes.")
        return 1
    print(f"Verified {len(expected)} deterministic package(s).")
    return 0


def build() -> int:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    expected_names: set[str] = set()
    for skill_dir in skill_dirs():
        name = f"{skill_dir.name}.skill"
        expected_names.add(name)
        destination = DIST_DIR / name
        data = archive_bytes(skill_dir)
        file_descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{name}.", dir=DIST_DIR
        )
        try:
            with os.fdopen(file_descriptor, "wb") as temporary_file:
                temporary_file.write(data)
            os.replace(temporary_name, destination)
        finally:
            if os.path.exists(temporary_name):
                os.unlink(temporary_name)

    for archive in DIST_DIR.glob("*.skill"):
        if archive.name not in expected_names:
            archive.unlink()
    print(f"Built {len(expected_names)} deterministic package(s) in dist/.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--clean", action="store_true")
    args = parser.parse_args()
    if args.check:
        return check()
    if args.clean:
        return clean()
    return build()


if __name__ == "__main__":
    raise SystemExit(main())
