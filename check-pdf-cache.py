#!/usr/bin/env python3
"""Which PDFs and slide decks in this vault still need a Markdown cache?

The `pdf-cache` rule is "read `<name>.md`, never `<name>.pdf`". Checking that by
hand costs an agent a pile of `find` and `ls` calls per folder -- and a wrong
answer means either a wasted subagent run or an expensive page-by-page PDF read.
This script answers it in one call: it pairs every `.pdf` / `.pptx` with its
`.md` twin and reports only the ones still unpaired.

Two modes, same argument
------------------------
    python check-pdf-cache.py lecture/Week1.pdf      # one file   -> what to do with it
    python check-pdf-cache.py CPE342-machine-learning
                                                     # one folder -> everything uncached

A `.pptx` and a `.pdf` sharing one basename are *one* deck, not two files, so
they collapse into a single result -- that is the chain the `pdf-cache` skill
describes: `.pptx` (lecturer's original) -> `.pdf` (reading copy) -> `.md`.

Statuses
--------
    MISSING   a `.pdf` with no `.md` -- generate the cache
    EXPORT    a `.pptx` with no `.pdf` -- only the user can export that
    STALE     the `.md` is older than its source (needs --stale, see below)
    IGNORED   matched a `.pdfignore` rule -- do not cache it
    CACHED    already paired; read the `.md`

Ignoring
--------
A `.pdfignore` behaves like `.gitignore`: it lives in a folder, covers that
folder and everything beneath it, and there can be one per class. Deeper files
layer on top of shallower ones and the last matching rule wins. `#` comments,
`!` negation, `*` `?` `**` globs and a trailing `/` for directory-only all work
as in git. Windows separators are read as separators, not escapes, so a line
copied out of Explorer (`assignment\\Lab-1\\report.pdf`) just works.

`temp/` and dot-folders are skipped while walking -- the vault never caches or
documents those. Pointing the script straight at one still scans it.

Usage
-----
    python check-pdf-cache.py <path> [<path> ...]
    python check-pdf-cache.py <path> --all      # every source file with its status
    python check-pdf-cache.py <path> --stale    # also flag caches older than their source
    python check-pdf-cache.py <path> --json     # machine-readable

--stale is opt-in on purpose: a fresh `git clone` stamps every file with the
checkout time, so modification dates lie right after one and everything would
look stale. Trust it only on a working copy you have been editing.

Exit status is 0 whenever the scan ran -- "work pending" is not an error -- and
2 if a path does not exist.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# The lecturer's originals worth caching. Everything else is already readable.
SOURCE_SUFFIXES = {".pdf", ".pptx"}
CACHE_SUFFIX = ".md"
IGNORE_FILENAME = ".pdfignore"

# Root CLAUDE.md: temp/ is volatile and never cached, listed, or documented.
SKIP_DIRS = {"temp"}

# The vault root -- this script sits in it, so paths can be printed relative to it.
VAULT_ROOT = Path(__file__).resolve().parent

STATUS_ORDER = ("missing", "export", "stale", "cached", "ignored")
PENDING = ("missing", "export", "stale")

# A Thai Windows console defaults to cp874, which cannot encode a Thai filename
# or even a middle dot -- printing one would crash the run. Force UTF-8 out.
for stream in (sys.stdout, sys.stderr):
    stream.reconfigure(encoding="utf-8", errors="replace")


def die(message: str) -> None:
    """Print to stderr and exit 2 -- a bad argument, not a scan result."""
    print(message, file=sys.stderr)
    raise SystemExit(2)


def show(path: Path) -> str:
    """Vault-relative POSIX path, for output that stays short and copy-pasteable."""
    resolved = path if path.is_absolute() else path.resolve()
    try:
        return resolved.relative_to(VAULT_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


# --------------------------------------------------------------------------- #
# .pdfignore                                                                    #
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Rule:
    """One line of one `.pdfignore`."""

    regex: re.Pattern[str]
    negated: bool
    dir_only: bool
    origin: str  # "CPE334-software-engineering/.pdfignore:2"
    raw: str


def _translate(pattern: str) -> str:
    """Turn a gitignore-style glob into a regex body (no anchors).

    `*` and `?` stop at a path separator, `**` crosses them -- the distinction
    that makes `*.pdf` mean "in this folder" and `**/*.pdf` mean "anywhere".
    """
    out: list[str] = []
    i, n = 0, len(pattern)
    while i < n:
        char = pattern[i]

        if char == "*":
            j = i
            while j < n and pattern[j] == "*":
                j += 1
            double = j - i > 1
            before = pattern[i - 1] if i > 0 else "/"
            after = pattern[j] if j < n else ""
            if double and before == "/" and after == "/":
                out.append("(?:.*/)?")  # a/**/b -> a/, any depth, b
                j += 1  # the trailing slash is part of the wildcard
            elif double and before == "/" and after == "":
                out.append(".*")  # a/** -> everything under a
            else:
                out.append("[^/]*")
            i = j
            continue

        if char == "?":
            out.append("[^/]")
            i += 1
            continue

        if char == "[":
            close = i + 1
            if close < n and pattern[close] in "!^":
                close += 1
            if close < n and pattern[close] == "]":
                close += 1
            while close < n and pattern[close] != "]":
                close += 1
            if close >= n:  # unterminated class -- a literal bracket
                out.append(re.escape("["))
                i += 1
                continue
            body = pattern[i + 1 : close]
            out.append("[" + ("^" + body[1:] if body.startswith("!") else body) + "]")
            i = close + 1
            continue

        out.append(re.escape(char))
        i += 1

    return "".join(out)


def load_rules(directory: Path) -> list[Rule]:
    """Parse `<directory>/.pdfignore`, or return [] when there isn't one."""
    ignore_file = directory / IGNORE_FILENAME
    if not ignore_file.is_file():
        return []

    rules: list[Rule] = []
    text = ignore_file.read_text(encoding="utf-8", errors="replace")
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        negated = line.startswith("!")
        if negated:
            line = line[1:]

        # Windows separators are separators here. git would read `\` as an
        # escape, but every path in this vault gets copied out of Explorer.
        line = line.replace("\\", "/")

        dir_only = line.endswith("/")
        line = line.rstrip("/")
        # A slash anywhere but the end anchors the pattern to this folder;
        # a bare name matches at any depth below it.
        anchored = "/" in line
        line = line.lstrip("/")
        if not line:
            continue

        prefix = "" if anchored else r"(?:.*/)?"
        rules.append(
            Rule(
                regex=re.compile(f"^{prefix}{_translate(line)}$"),
                negated=negated,
                dir_only=dir_only,
                origin=f"{show(ignore_file)}:{lineno}",
                raw=raw.strip(),
            )
        )
    return rules


class IgnoreIndex:
    """Every `.pdfignore` that applies to a folder, shallowest first.

    Each folder's answer is memoised, so a whole class folder costs one read per
    `.pdfignore` no matter how many PDFs sit under it.
    """

    def __init__(self, ceiling: Path) -> None:
        self._ceiling = ceiling
        self._cache: dict[Path, list[tuple[Path, list[Rule]]]] = {}

    def layers_for(self, directory: Path) -> list[tuple[Path, list[Rule]]]:
        directory = directory.resolve()
        cached = self._cache.get(directory)
        if cached is not None:
            return cached

        # Stop at the vault root, the way git stops at the repo root -- or at the
        # drive root, for the rare check run outside the vault entirely.
        parent = directory.parent
        at_top = parent == directory or directory == self._ceiling
        inherited: list[tuple[Path, list[Rule]]] = [] if at_top else self.layers_for(parent)

        own = load_rules(directory)
        layers = inherited + [(directory, own)] if own else list(inherited)
        self._cache[directory] = layers
        return layers

    def match(self, path: Path) -> Rule | None:
        """The rule that decides `path`, or None if nothing ignores it."""
        verdict: Rule | None = None
        resolved = path.resolve()

        for base, rules in self.layers_for(path.parent):
            try:
                relative = resolved.relative_to(base).as_posix()
            except ValueError:  # pragma: no cover -- layers always contain the path
                continue

            # Test each ancestor folder too, so ignoring a folder ignores what
            # is inside it. Deeper components are checked last, so a rule about
            # the file itself overrides one about its folder.
            parts = relative.split("/")
            for depth in range(1, len(parts) + 1):
                candidate = "/".join(parts[:depth])
                is_dir = depth < len(parts)
                for rule in rules:
                    if rule.dir_only and not is_dir:
                        continue
                    if rule.regex.match(candidate):
                        verdict = rule

        return verdict if verdict is not None and not verdict.negated else None


# --------------------------------------------------------------------------- #
# Scanning                                                                      #
# --------------------------------------------------------------------------- #


@dataclass
class Entry:
    """One source document -- a `.pdf`, a `.pptx`, or both -- and its cache."""

    status: str
    source: Path  # the file to act on
    cache: Path
    pdf: Path | None
    pptx: Path | None
    rule: Rule | None

    def detail(self) -> str:
        """The one-line instruction that goes with this status."""
        if self.status == "cached":
            return f"read {show(self.cache)} instead of the PDF"
        if self.status == "missing":
            return f"no cache yet -> generate {show(self.cache)} (pdf-cache skill)"
        if self.status == "export":
            return (
                "no .pdf reading copy -> ask the user to export it "
                "(PowerPoint -> Save as PDF); never run pdftotext on a .pptx"
            )
        if self.status == "stale":
            return f"{show(self.cache)} is older than its source -> regenerate it"
        if self.status == "ignored" and self.rule is not None:
            return (
                f'ignored by {self.rule.origin} ("{self.rule.raw}") -> do not cache it; '
                "open the PDF directly only if the task truly needs it"
            )
        return ""

    def as_dict(self) -> dict[str, object]:
        return {
            "status": self.status,
            "source": show(self.source),
            "cache": show(self.cache),
            "pdf": show(self.pdf) if self.pdf else None,
            "pptx": show(self.pptx) if self.pptx else None,
            "ignored_by": self.rule.origin if self.rule else None,
            "detail": self.detail(),
        }


def iter_sources(root: Path):
    """Every `.pdf` / `.pptx` under `root`, skipping `temp/` and dot-folders."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            d for d in dirnames if not d.startswith(".") and d.lower() not in SKIP_DIRS
        )
        for name in sorted(filenames):
            if Path(name).suffix.lower() in SOURCE_SUFFIXES:
                yield Path(dirpath) / name


def classify(stem: Path, members: dict[str, Path], index: IgnoreIndex, stale: bool) -> Entry:
    """Decide what, if anything, has to happen to one source document."""
    pdf = members.get(".pdf")
    pptx = members.get(".pptx")
    # `<stem>.md`, built by concatenation -- with_suffix() would eat a real dot
    # in names like "Lecture+2.v2.pdf".
    cache = stem.parent / (stem.name + CACHE_SUFFIX)

    rule = next((hit for member in members.values() if (hit := index.match(member))), None)

    if rule is not None:
        status = "ignored"
    elif not cache.is_file():
        status = "missing" if pdf else "export"
    elif stale and cache.stat().st_mtime < max(m.stat().st_mtime for m in members.values()):
        status = "stale"
    else:
        status = "cached"

    return Entry(
        status=status,
        # Act on the PDF when there is one; a lone .pptx is the user's problem.
        source=pdf or pptx or stem,
        cache=cache,
        pdf=pdf,
        pptx=pptx,
        rule=rule,
    )


def group(sources, index: IgnoreIndex, stale: bool) -> list[Entry]:
    """Collapse `<name>.pptx` + `<name>.pdf` into one entry, then classify each."""
    groups: dict[Path, dict[str, Path]] = {}
    for path in sources:
        stem = path.parent / path.name[: -len(path.suffix)]
        groups.setdefault(stem, {})[path.suffix.lower()] = path
    return [classify(stem, members, index, stale) for stem, members in sorted(groups.items())]


def collect(targets: list[Path], index: IgnoreIndex, stale: bool) -> list[Entry]:
    """Classify every source document reachable from the given paths."""
    files: list[Path] = []
    for target in targets:
        if target.is_dir():
            files.extend(iter_sources(target))
        elif target.suffix.lower() in SOURCE_SUFFIXES:
            # A single file still needs its siblings, or a .pptx would look
            # like it has no reading copy when the .pdf is right there.
            stem = target.parent / target.name[: -len(target.suffix)]
            files.extend(
                sibling
                for suffix in sorted(SOURCE_SUFFIXES)
                if (sibling := stem.parent / (stem.name + suffix)).is_file()
            )
        else:
            die(
                f"error: {show(target)} is not a folder, a .pdf, or a .pptx\n"
                "       (only those have Markdown caches -- read any other file directly)"
            )

    seen: set[Path] = set()
    unique = [f for f in files if not (f.resolve() in seen or seen.add(f.resolve()))]
    return group(unique, index, stale)


# --------------------------------------------------------------------------- #
# Reporting                                                                     #
# --------------------------------------------------------------------------- #


def summary(entries: list[Entry]) -> str:
    counts = {status: sum(e.status == status for e in entries) for status in STATUS_ORDER}
    parts = [f"{len(entries)} source(s)"]
    parts += [f"{counts[status]} {status}" for status in STATUS_ORDER if counts[status]]
    return "scanned " + ", ".join(parts)


def report(entries: list[Entry], targets: list[Path], show_all: bool) -> None:
    """Print the human-readable result: what still needs doing, and nothing else."""
    label_width = max(len(s) for s in STATUS_ORDER) + 2

    if len(entries) == 1 and not targets[0].is_dir():
        entry = entries[0]
        print(f"{entry.status.upper():<{label_width}}{show(entry.source)}")
        print(f"{'':<{label_width}}{entry.detail()}")
        return

    shown = entries if show_all else [e for e in entries if e.status in PENDING]
    if not shown:
        where = ", ".join(show(t) for t in targets)
        print(f"nothing to do -- no source under {where} is waiting on a Markdown cache")
    else:
        header = "status" if show_all else f"{len(shown)} source(s) need a Markdown cache"
        print(f"{header}:\n")
        for entry in shown:
            print(f"  {entry.status.upper():<{label_width}}{show(entry.source)}")
            if entry.status in ("export", "ignored"):
                print(f"  {'':<{label_width}}{entry.detail()}")
        print()

    print(summary(entries))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List the .pdf / .pptx files in this vault that still have no .md cache.",
        epilog="A path may be a folder (scan it) or a single .pdf / .pptx (check just that one).",
    )
    parser.add_argument("paths", nargs="*", default=["."], help="folders or files to check")
    parser.add_argument(
        "--all", action="store_true", help="list every source file with its status, not just pending ones"
    )
    parser.add_argument(
        "--stale",
        action="store_true",
        help="also flag caches older than their source (unreliable right after a git clone)",
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    targets = [Path(p) for p in (args.paths or ["."])]
    for target in targets:
        if not target.exists():
            die(f"error: no such file or folder: {target}")

    index = IgnoreIndex(VAULT_ROOT)
    entries = collect(targets, index, args.stale)

    if args.json:
        chosen = entries if args.all else [e for e in entries if e.status in PENDING]
        print(
            json.dumps(
                {
                    "targets": [show(t) for t in targets],
                    "entries": [e.as_dict() for e in chosen],
                    "counts": {s: sum(e.status == s for e in entries) for s in STATUS_ORDER},
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return 0

    report(entries, targets, args.all)
    return 0


if __name__ == "__main__":
    sys.exit(main())
