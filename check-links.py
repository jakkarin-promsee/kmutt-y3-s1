#!/usr/bin/env python3
"""Do the [[wiki-links]] in this vault still point at something real?

A dead wiki-link is worse than no link: Obsidian renders it exactly like a live
one, so nothing looks wrong until you click it. Renames done outside Obsidian --
in Explorer, by a shell command, by an agent -- break links silently and in bulk.

    python check-links.py                      # the whole vault
    python check-links.py CPE342-machine-learning
    python check-links.py CPE342-machine-learning/note/lecture-1.md

The file index is always the **whole vault**, whatever you point at, because a
link in one class routinely targets a file in another. Narrowing the argument
narrows which documents get *read*, never which files count as link targets.

Both link syntaxes are checked: `[[wiki-links]]` everywhere, and `[text](path)`
relative links -- README.md is written entirely in those, and every class
CLAUDE.md needs one for `[CLAUDE.md](../CLAUDE.md)`, which has no wiki form.

What counts as broken
---------------------
    UNRESOLVED     nothing on disk matches the target
    RELATIVE       a `[text](path)` pointing at nothing, resolved from the
                   folder the file sits in -- the links GitHub follows
    NOT LINKABLE   the file exists, but somewhere Obsidian won't index -- a
                   dot-folder like `.claude/`, or `temp/`
    BAD ANCHOR     the file resolves but `#Heading` names no heading in it.
                   Obsidian anchors are literal text, not GitHub-style slugs, so
                   rewording a heading breaks every link into it
    DEAD EXTENSION `[[x.py]]` / `[[x.pptx]]` while *Detect all file extensions*
                   is off, which `.obsidian/app.json` is asked about directly.
                   Off means the link really is dead, so it is not a warning

And as warnings, three ways a link can resolve today and still be a trap:
ambiguous bare basenames (`[[INDEX]]` when five exist), a target that matches
only case-insensitively, and wiki-links in `README.md`, which GitHub renders as
dead text.

What is skipped, and why
------------------------
- **Code and math.** Fenced blocks, `inline code`, `$…$` and `$$…$$` are blanked
  out first. This vault's docs quote `[[Name.pdf]]` as an *example of the
  syntax* constantly, and LaTeX like `\\left[…\\right](2)` is indistinguishable
  from a Markdown link to any regex. (Line numbers survive the blanking.)
- **`format-template/`.** Its `[[Name.pdf]]`, `[[file]]` and
  `[[CPE999-example/INDEX]]` are deliberate placeholders for a class that does
  not exist yet -- the whole point of a template. Pass `--include-template` to
  check it anyway, or name one of its files directly.
- **`temp/` and dot-folders** as *targets*: they are still walked, so a link
  into one gets `NOT LINKABLE` rather than a confusing `UNRESOLVED`.

Usage
-----
    python check-links.py [<path> ...] [--json] [--strict] [--include-template]

Exit status is 0 whenever the scan ran, so a report of broken links does not
look like a crashed command. `--strict` makes broken links exit 1 (for a hook or
a CI step); a bad argument is always 2.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

VAULT_ROOT = Path(__file__).resolve().parent

# Never walked: huge, machine-owned, and never a link target.
HARD_SKIP = {".git", ".obsidian", "node_modules", "__pycache__", ".venv", "venv"}

# Walked and remembered, but not valid link targets. Obsidian does not index
# dot-folders at all, and `temp/` is volatile by vault rule.
UNLINKABLE_DIRS = {"temp"}

# Placeholder links by design -- see the module docstring.
TEMPLATE_DIR = "format-template"

# Extensions Obsidian indexes out of the box. Everything else resolves only with
# *Settings -> Files and links -> Detect all file extensions* turned on.
OBSIDIAN_NATIVE = {
    ".md", ".pdf", ".canvas",
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".avif",
    ".mp3", ".wav", ".m4a", ".ogg", ".3gp", ".flac",
    ".mp4", ".webm", ".ogv", ".mov", ".mkv",
}

# `[[target]]`, `[[target|alias]]`, `[[target#anchor|alias]]`, `![[embed]]`.
# Deliberately loose: the pieces are split by hand below, so a heading with a
# `#` in the alias or an empty target (`[[#Heading]]`) still parses.
LINK_RE = re.compile(r"!?\[\[([^\]\n]+?)\]\]")

# `[text](target)` -- the vault's other link syntax. README.md uses it
# throughout, and every class CLAUDE.md uses it for `[CLAUDE.md](../CLAUDE.md)`,
# which has no wiki-link form. Resolved relative to the file it appears in.
MD_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(\s*<?([^)>\s]+)>?(?:\s+\"[^\"\n]*\")?\s*\)")
EXTERNAL_RE = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", re.I)

FENCE_RE = re.compile(r"^```.*?^```", re.S | re.M)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

# LaTeX, which the study notes are full of. `\left[ … \right](2)` is a markdown
# link as far as any regex is concerned, so math has to go the same way code
# does. Inline math requires a non-space just inside each `$` -- that is what
# keeps "$100,000 vs $133,100" in prose from being read as a formula.
MATH_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.S)
MATH_INLINE_RE = re.compile(r"\$(?!\s)[^$\n]+?(?<!\s)\$")
HEADING_RE = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
EMPHASIS_RE = re.compile(r"[*_`~]")


def show(path: Path) -> str:
    """Vault-relative POSIX path -- short, and clickable as `file:line`."""
    resolved = path if path.is_absolute() else path.resolve()
    try:
        return resolved.relative_to(VAULT_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def die(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(2)


def detect_all_extensions(root: Path) -> bool | None:
    """Is Obsidian's *Detect all file extensions* on? None if there's no config.

    Without it Obsidian indexes only `.md`, `.pdf`, `.canvas` and media, so a
    `[[save-checkpoint.py]]` renders as a link and resolves to nothing. The
    answer lives in `.obsidian/app.json`, which **is committed in this repo** --
    so this is one setting for every clone, not one per machine.

    Read only, never written: Obsidian keeps this config in memory and rewrites
    the file when it exits, which also means a freshly-flipped setting shows up
    here only after the app closes.
    """
    try:
        config = json.loads((root / ".obsidian" / "app.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return bool(config.get("showUnsupportedFiles", False))


def strip_code_and_math(text: str) -> str:
    """Blank out code and LaTeX, preserving every offset.

    Both are full of bracket syntax that looks exactly like a link, and this
    vault's docs quote `[[Name.pdf]]` as an *example* constantly. Newlines are
    kept and everything else becomes a space, so `str.count("\\n")` still
    reports the true line number of whatever survives.
    """

    def blank(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group(0))

    for pattern in (FENCE_RE, MATH_BLOCK_RE, INLINE_CODE_RE, MATH_INLINE_RE):
        text = pattern.sub(blank, text)
    return text


# --------------------------------------------------------------------------- #
# The vault, as Obsidian sees it                                                #
# --------------------------------------------------------------------------- #


class VaultIndex:
    """Every file in the vault, split into what Obsidian can link and what it can't."""

    def __init__(self, root: Path, include_template: bool) -> None:
        self.root = root
        self.files: set[str] = set()
        self.by_base: dict[str, list[str]] = defaultdict(list)
        self.unlinkable: dict[str, str] = {}  # path -> why Obsidian ignores it
        self._headings: dict[str, set[str]] = {}
        self._include_template = include_template
        self.all_extensions = detect_all_extensions(root)
        self._walk()

    def _walk(self) -> None:
        for dirpath, dirnames, filenames in os.walk(self.root):
            dirnames[:] = sorted(d for d in dirnames if d not in HARD_SKIP)
            for name in sorted(filenames):
                path = Path(dirpath) / name
                rel = show(path)
                reason = self._unlinkable_reason(rel)
                if reason:
                    self.unlinkable[rel] = reason
                    continue
                self.files.add(rel)
                # `[[Name]]` means Name.md; every other type needs its extension
                # written out, so it is indexed under its full filename only.
                self.by_base[name].append(rel)
                if name.endswith(".md"):
                    self.by_base[name[:-3]].append(rel)

    def _unlinkable_reason(self, rel: str) -> str | None:
        parts = rel.split("/")[:-1]
        for part in parts:
            if part.startswith("."):
                return f"inside `{part}/`, and Obsidian does not index dot-folders"
            if part in UNLINKABLE_DIRS:
                return f"inside `{part}/`, which this vault never links or documents"
            if part == TEMPLATE_DIR and not self._include_template:
                return f"inside `{TEMPLATE_DIR}/`, a template of placeholders"
        return None

    def lookup(self, target: str) -> list[str]:
        """Files a `[[target]]` could resolve to. Several means ambiguous."""
        if "/" in target:
            return [p for p in (target, target + ".md") if p in self.files]
        return list(self.by_base.get(target, ()))

    def lookup_folded(self, target: str) -> list[str]:
        """Same, ignoring case -- Windows and Obsidian both do."""
        key = target.casefold()
        if "/" in target:
            wanted = {key, key + ".md"}
            return sorted(p for p in self.files if p.casefold() in wanted)
        return sorted(
            p for base, paths in self.by_base.items() if base.casefold() == key for p in paths
        )

    def lookup_unlinkable(self, target: str) -> list[str]:
        """Where a target *would* have matched, had Obsidian been willing to look."""
        key = target.casefold()
        hits = []
        for path in self.unlinkable:
            name = path.rsplit("/", 1)[-1]
            stem = name[:-3] if name.endswith(".md") else None
            if key in (path.casefold(), (path + ".md").casefold(), name.casefold()):
                hits.append(path)
            elif stem and key == stem.casefold():
                hits.append(path)
        return sorted(hits)

    def headings(self, rel: str) -> set[str]:
        """Normalised heading texts of a Markdown file, for anchor checking."""
        cached = self._headings.get(rel)
        if cached is not None:
            return cached
        found: set[str] = set()
        path = self.root / rel
        if path.is_file():
            text = strip_code_and_math(path.read_text(encoding="utf-8", errors="replace"))
            for match in HEADING_RE.finditer(text):
                found.add(normalise_anchor(match.group(1)))
        self._headings[rel] = found
        return found


def normalise_anchor(text: str) -> str:
    """Obsidian matches heading text literally; only case and spacing are loose."""
    return " ".join(EMPHASIS_RE.sub("", text).split()).casefold()


# --------------------------------------------------------------------------- #
# Reading the documents                                                         #
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Link:
    doc: str
    line: int
    target: str  # before the `#`, may be "" for a same-file anchor
    anchor: str  # after the `#`, may be ""
    raw: str

    def where(self) -> str:
        return f"{self.doc}:{self.line}"


@dataclass
class Finding:
    kind: str
    link: Link
    detail: str
    candidates: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, object]:
        return {
            "kind": self.kind,
            "doc": self.link.doc,
            "line": self.link.line,
            "link": self.link.raw,
            "detail": self.detail,
            "candidates": self.candidates,
        }


def iter_links(doc: str, text: str):
    """Every wiki-link in `text`, code already blanked out by the caller."""
    for match in LINK_RE.finditer(text):
        # Inside a Markdown table the alias separator must be written `\|`, or
        # the pipe would end the cell. Obsidian reads both forms.
        inside = match.group(1).replace("\\|", "|")
        inside = inside.split("|", 1)[0]  # drop the display alias
        target, _, anchor = inside.partition("#")
        target, anchor = target.strip(), anchor.strip()
        if not target and not anchor:
            continue
        line = text.count("\n", 0, match.start()) + 1
        yield Link(doc=doc, line=line, target=target, anchor=anchor, raw=match.group(0))


def iter_relative_links(doc: str, text: str):
    """Every `[text](path)` that points inside the repo, code already blanked."""
    for match in MD_LINK_RE.finditer(text):
        target = match.group(1)
        if EXTERNAL_RE.match(target):  # http:, mailto:, //cdn, #anchor
            continue
        path = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not path:
            continue
        line = text.count("\n", 0, match.start()) + 1
        yield Link(doc=doc, line=line, target=path, anchor="", raw=match.group(0))


def in_template(path: Path) -> bool:
    return TEMPLATE_DIR in show(path).split("/")


def iter_docs(targets: list[Path], include_template: bool, notes: list[str]):
    """Markdown files to read.

    `format-template/` is the one folder whose links are fake on purpose, so
    `--include-template` decides it however you point at it -- otherwise a
    direct `check-links.py format-template` would contradict the flag. `temp/`
    and dot-folders have no such flag, so naming one explicitly still scans it.
    """
    for target in targets:
        if in_template(target) and not include_template:
            notes.append(
                f"skipped `{show(target)}` -- {TEMPLATE_DIR}/ is placeholder links by design; "
                "pass --include-template to check it anyway"
            )
            continue

        if target.is_file():
            if target.suffix.lower() != ".md":
                die(f"error: {show(target)} is not a Markdown file")
            yield target
            continue
        for dirpath, dirnames, filenames in os.walk(target):
            dirnames[:] = sorted(
                d
                for d in dirnames
                if d not in HARD_SKIP
                and not d.startswith(".")
                and d not in UNLINKABLE_DIRS
                and (include_template or d != TEMPLATE_DIR)
            )
            for name in sorted(filenames):
                if name.endswith(".md"):
                    yield Path(dirpath) / name


# --------------------------------------------------------------------------- #
# Checking                                                                      #
# --------------------------------------------------------------------------- #


def check_link(link: Link, index: VaultIndex) -> list[Finding]:
    """Everything wrong with one link. Usually nothing."""
    findings: list[Finding] = []

    if link.target:
        matches = index.lookup(link.target)

        if not matches:
            folded = index.lookup_folded(link.target)
            if folded:
                findings.append(
                    Finding(
                        "case",
                        link,
                        f"resolves only because Windows ignores case -- the file is `{folded[0]}`",
                        folded,
                    )
                )
                matches = folded
            else:
                blocked = index.lookup_unlinkable(link.target)
                if blocked:
                    reason = index.unlinkable[blocked[0]]
                    return [
                        Finding("unlinkable", link, f"`{blocked[0]}` is {reason}", blocked)
                    ]
                return [Finding("unresolved", link, "")]

        if len(matches) > 1:
            findings.append(Finding("ambiguous", link, "", matches))

        # A non-native extension is only a problem while the setting is off --
        # and then it is a real dead link, not a stylistic warning.
        suffix = Path(matches[0]).suffix.lower()
        if suffix and suffix not in OBSIDIAN_NATIVE and index.all_extensions is not True:
            findings.append(Finding("extension", link, "", matches[:1]))
        resolved = matches[0]
    else:
        resolved = link.doc  # `[[#Heading]]` -- an anchor into this same file

    # Anchors: `^abc` is a block reference and `page=3` is a PDF page, neither
    # of which is a heading.
    if link.anchor and not link.anchor.startswith("^") and resolved.endswith(".md"):
        if "=" not in link.anchor:
            wanted = normalise_anchor(link.anchor)
            headings = index.headings(resolved)
            if wanted not in headings:
                where = "" if not link.target else f"looked in `{resolved}`"
                findings.append(Finding("anchor", link, where))

    return findings


def check(targets: list[Path], index: VaultIndex, include_template: bool):
    findings: list[Finding] = []
    notes: list[str] = []
    docs = 0
    links = 0

    for path in iter_docs(targets, include_template, notes):
        rel = show(path)
        docs += 1
        text = strip_code_and_math(path.read_text(encoding="utf-8", errors="replace"))

        for link in iter_links(rel, text):
            links += 1
            # In README.md a wiki-link is wrong whether or not it resolves, so
            # that one finding replaces the resolution check rather than joining it.
            if rel == "README.md":
                findings.append(Finding("readme", link, ""))
                continue
            findings.extend(check_link(link, index))

        for link in iter_relative_links(rel, text):
            links += 1
            if not (path.parent / link.target).exists():
                findings.append(Finding("relative", link, ""))

    return findings, docs, links, notes


# --------------------------------------------------------------------------- #
# Reporting                                                                     #
# --------------------------------------------------------------------------- #

BROKEN = ("unresolved", "unlinkable", "anchor", "relative", "extension")

SECTIONS = [
    ("unresolved", "UNRESOLVED -- nothing on disk matches", ""),
    (
        "relative",
        "BROKEN RELATIVE LINK -- [text](path) points at nothing",
        "Resolved from the folder the file sits in. These are the links GitHub follows.",
    ),
    ("unlinkable", "NOT LINKABLE -- the file exists, but not where Obsidian looks", ""),
    (
        "anchor",
        "BAD ANCHOR -- the file resolves, the heading does not",
        "Obsidian matches heading text literally, not as a GitHub-style slug.",
    ),
    (
        "ambiguous",
        "AMBIGUOUS -- bare basename with more than one match",
        "Obsidian silently picks the nearest copy, and that changes when either file moves. "
        "Path-qualify: [[CPE342-machine-learning/INDEX|INDEX.md]].",
    ),
    (
        "extension",
        "DEAD EXTENSION -- Obsidian is not indexing this file type",
        "",  # filled in from .obsidian/app.json, see extension_note()
    ),
    (
        "case",
        "CASE MISMATCH -- works on Windows, breaks on a case-sensitive filesystem",
        "",
    ),
    (
        "readme",
        "WIKI-LINK IN README.md -- GitHub renders it as dead text",
        "Use a relative Markdown link there instead.",
    ),
]


def extension_note(all_extensions: bool | None) -> str:
    """Why these links are dead, and the one action that fixes all of them."""
    cause = (
        "`.obsidian/app.json` has `showUnsupportedFiles` off"
        if all_extensions is False
        else "there is no readable `.obsidian/app.json`, so it is off"
    )
    return (
        f"{cause}. Turn on *Settings -> Files and links -> Detect all file extensions* in "
        "Obsidian, close the app so the setting is written to disk, then commit app.json -- "
        "it is tracked in this repo, so one flip fixes every clone. (If Obsidian is open right "
        "now with it already on, app.json is just stale until the app exits.)"
    )


def report(
    findings: list[Finding], docs: int, links: int, notes: list[str], all_extensions: bool | None
) -> None:
    for note in notes:
        print(f"note: {note}")
    if notes:
        print()
    print(f"checked {links} link(s) in {docs} document(s)\n")

    grouped: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[finding.kind].append(finding)

    if not findings:
        print("nothing to check" if not links else "all links resolve")
        return

    for kind, title, note in SECTIONS:
        group = grouped.get(kind)
        if not group:
            continue
        print(f"{title}  ({len(group)})")
        if kind == "extension":
            note = extension_note(all_extensions)
        if note:
            print(f"  {note}")
        for finding in group:
            print(f"  {finding.link.where()}  {finding.link.raw}")
            if finding.detail:
                print(f"      {finding.detail}")
            if len(finding.candidates) > 1:
                for candidate in finding.candidates:
                    print(f"        - {candidate}")
        print()

    broken = sum(len(grouped.get(kind, ())) for kind in BROKEN)
    warnings = len(findings) - broken
    print(f"{broken} broken, {warnings} warning(s)")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="Check that every [[wiki-link]] in this vault resolves to a real file.",
        epilog="Paths narrow which documents are read; link targets are always "
        "matched against the whole vault.",
    )
    parser.add_argument("paths", nargs="*", default=["."], help="folders or .md files to check")
    parser.add_argument(
        "--include-template",
        action="store_true",
        help=f"also check {TEMPLATE_DIR}/, whose links are placeholders on purpose",
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--strict", action="store_true", help="exit 1 if any link is broken (for hooks and CI)"
    )
    args = parser.parse_args()

    targets = [Path(p) for p in (args.paths or ["."])]
    for target in targets:
        if not target.exists():
            die(f"error: no such file or folder: {target}")

    index = VaultIndex(VAULT_ROOT, args.include_template)
    findings, docs, links, notes = check(targets, index, args.include_template)

    if args.json:
        print(
            json.dumps(
                {
                    "targets": [show(t) for t in targets],
                    "documents": docs,
                    "links": links,
                    "detect_all_extensions": index.all_extensions,
                    "notes": notes,
                    "findings": [f.as_dict() for f in findings],
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        report(findings, docs, links, notes, index.all_extensions)

    if args.strict and any(f.kind in BROKEN for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
