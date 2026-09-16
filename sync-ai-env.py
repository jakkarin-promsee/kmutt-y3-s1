#!/usr/bin/env python3
"""Sync Claude project guidance into Codex-compatible locations.

CLAUDE.md and .claude/skills remain the source of truth. This script mirrors:

    **/CLAUDE.md          -> **/AGENTS.md
    **/.claude/skills/**  -> **/.agents/skills/**

In mirrored UTF-8 text files, references to ``CLAUDE.md`` are rewritten as
``AGENTS.md``. Only files recorded in the generated manifest are eligible for
stale-file cleanup, so unrelated files under .agents are left alone.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


MANIFEST_PATH = Path(".agents/.sync-ai-env-manifest.json")
TEXT_REPLACEMENTS = (("CLAUDE.md", "AGENTS.md"),)
IGNORED_DIRECTORIES = {
    ".agents",
    ".claude",
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}


@dataclass(frozen=True)
class Mapping:
    source: Path
    target: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Mirror CLAUDE.md files and .claude/skills into the names and "
            "locations used by Codex."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="repository root (default: the directory containing this script)",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--check",
        action="store_true",
        help="report drift without writing; exit 1 when a sync is needed",
    )
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="show what a sync would change without writing",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite conflicting targets not previously managed by this script",
    )
    return parser.parse_args()


def is_ignored(relative_path: Path) -> bool:
    return any(part in IGNORED_DIRECTORIES for part in relative_path.parts)


def discover_mappings(root: Path) -> list[Mapping]:
    mappings: list[Mapping] = []

    for current_dir, directory_names, file_names in os.walk(root):
        current = Path(current_dir)
        relative_dir = current.relative_to(root)

        directory_names[:] = sorted(
            name
            for name in directory_names
            if name not in IGNORED_DIRECTORIES
        )

        if "CLAUDE.md" in file_names and not is_ignored(relative_dir):
            mappings.append(
                Mapping(current / "CLAUDE.md", current / "AGENTS.md")
            )

        claude_skills = current / ".claude" / "skills"
        if claude_skills.is_dir():
            for source in sorted(claude_skills.rglob("*")):
                if source.is_file():
                    skill_relative = source.relative_to(claude_skills)
                    mappings.append(
                        Mapping(
                            source,
                            current / ".agents" / "skills" / skill_relative,
                        )
                    )

    return sorted(mappings, key=lambda item: item.target.as_posix())


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def load_manifest(root: Path) -> set[str]:
    path = root / MANIFEST_PATH
    if not path.exists():
        return set()

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        managed = payload["managed_files"]
        if payload.get("version") != 1 or not isinstance(managed, list):
            raise ValueError("unsupported manifest format")
        managed_files = {str(item) for item in managed}
        for item in managed_files:
            relative = Path(item)
            is_agents_file = relative.name == "AGENTS.md"
            is_skill_file = (
                len(relative.parts) >= 3
                and ".agents" in relative.parts
                and "skills" in relative.parts
                and relative.parts.index("skills")
                == relative.parts.index(".agents") + 1
            )
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError(f"unsafe managed path: {item}")
            if not (is_agents_file or is_skill_file):
                raise ValueError(f"unexpected managed path: {item}")
        return managed_files
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Cannot read {path}: {error}") from error


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rendered_content(source: Path) -> bytes:
    content = source.read_bytes()
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        return content

    for old, new in TEXT_REPLACEMENTS:
        text = text.replace(old, new)
    return text.encode("utf-8")


def files_match(content: bytes, target: Path) -> bool:
    return (
        target.is_file()
        and len(content) == target.stat().st_size
        and hashlib.sha256(content).hexdigest() == file_digest(target)
    )


def remove_empty_parents(path: Path, root: Path) -> None:
    boundary = (root / ".agents").resolve()
    current = path.parent
    while current.resolve() != boundary and boundary in current.resolve().parents:
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def write_manifest(root: Path, managed_files: set[str]) -> None:
    path = root / MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "source_of_truth": ["CLAUDE.md", ".claude/skills"],
        "managed_files": sorted(managed_files),
    }
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def sync(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: root directory does not exist: {root}", file=sys.stderr)
        return 2

    try:
        previously_managed = load_manifest(root)
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    mappings = discover_mappings(root)
    managed_now = {relative_posix(item.target, root) for item in mappings}
    stale = sorted(previously_managed - managed_now)
    changed = False
    conflicts: list[str] = []
    operations: list[tuple[str, Mapping, bytes]] = []

    for item in mappings:
        target_relative = relative_posix(item.target, root)
        content = rendered_content(item.source)
        if files_match(content, item.target):
            continue

        changed = True
        action = "update" if item.target.exists() else "create"
        if (
            item.target.exists()
            and target_relative not in previously_managed
            and not args.force
        ):
            conflicts.append(target_relative)
            print(f"[conflict] {target_relative}")
            continue

        if item.target.exists() and not item.target.is_file():
            conflicts.append(target_relative)
            print(f"[conflict] {target_relative} (target is not a file)")
            continue
        operations.append((action, item, content))

    stale_files: list[tuple[str, Path]] = []
    for target_relative in stale:
        target = root / Path(target_relative)
        if target.exists():
            changed = True
            if not target.is_file() and not target.is_symlink():
                conflicts.append(target_relative)
                print(f"[conflict] {target_relative} (stale target is not a file)")
                continue
            stale_files.append((target_relative, target))

    manifest_is_current = previously_managed == managed_now
    if not manifest_is_current:
        changed = True

    if conflicts:
        print(
            "error: conflicting generated targets were not overwritten; "
            "review them or rerun with --force",
            file=sys.stderr,
        )
        return 1 if args.check else 2

    for action, item, content in operations:
        target_relative = relative_posix(item.target, root)
        print(f"[{action}] {target_relative}")
        if not args.check and not args.dry_run:
            item.target.parent.mkdir(parents=True, exist_ok=True)
            item.target.write_bytes(content)
            shutil.copystat(item.source, item.target)

    for target_relative, target in stale_files:
        print(f"[delete] {target_relative}")
        if not args.check and not args.dry_run:
            target.unlink()
            remove_empty_parents(target, root)

    if not manifest_is_current and not args.check and not args.dry_run:
        write_manifest(root, managed_now)

    if args.check:
        if changed:
            print("AI environment is out of sync.")
            return 1
        print("AI environment is in sync.")
        return 0

    if args.dry_run:
        print("Dry run complete; no files were changed.")
        return 0

    if changed:
        print(
            f"Sync complete: {len(mappings)} file(s) managed from Claude sources."
        )
    else:
        print(f"Already in sync: {len(mappings)} file(s) managed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(sync(parse_args()))
