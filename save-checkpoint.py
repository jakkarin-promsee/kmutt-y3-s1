#!/usr/bin/env python3
"""Checkpoint commit helper for the 1_Uni vault.

Stages everything and commits with the vault's checkpoint format:

    <dd>/<mm>/<BE year>-<n>        e.g.  04/08/2569-3

`n` restarts at 1 each day and auto-increments by reading git log, so the
script is stateless -- no counter file to lose or desync.

Usage
-----
    python checkpoint.py                 # stage all + commit
    python checkpoint.py -n "did lab 1"  # same, with a note in the commit body
    python checkpoint.py --push          # commit, then push to origin
    python checkpoint.py --dry-run       # show what would happen, change nothing
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date

# Thai Buddhist Era = Gregorian + 543.
BE_OFFSET = 543

# Matches a checkpoint subject line: 04/08/2569-12
SUBJECT_RE = re.compile(r"^(\d{2}/\d{2}/\d{4})-(\d+)$")


def git(*args: str, root: str | None = None, check: bool = True) -> str:
    """Run a git command and return its stdout, stripped."""
    cmd = ["git"]
    if root:
        cmd += ["-C", root]
    cmd += list(args)
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and result.returncode != 0:
        sys.exit(f"error: {' '.join(cmd)}\n{result.stderr.strip()}")
    return result.stdout.strip()


def repo_root() -> str:
    """Absolute path of the repo top level.

    Resolved explicitly so `git add` always means "the whole vault", even when
    the script is run from inside a class folder -- a bare `git add .` would
    only stage the current directory.
    """
    root = git("rev-parse", "--show-toplevel", check=False)
    if not root:
        sys.exit("error: not inside a git repository")
    return root


def today_prefix(today: date) -> str:
    """`dd/mm/BE` for the given date."""
    return f"{today.day:02d}/{today.month:02d}/{today.year + BE_OFFSET}"


def next_number(root: str, prefix: str) -> int:
    """Highest checkpoint number already used today, plus one."""
    log = git("log", "--pretty=format:%s", root=root, check=False)
    highest = 0
    for line in log.splitlines():
        match = SUBJECT_RE.match(line.strip())
        if match and match.group(1) == prefix:
            highest = max(highest, int(match.group(2)))
    return highest + 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Commit the vault with a dd/mm/BE-n checkpoint message."
    )
    parser.add_argument(
        "-n",
        "--note",
        default="",
        help="optional free-text note; goes in the commit body, "
        "keeping the subject line in pure checkpoint format",
    )
    parser.add_argument(
        "--push", action="store_true", help="push to the current branch's remote after committing"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="print the plan without staging or committing"
    )
    args = parser.parse_args()

    root = repo_root()
    message = f"{today_prefix(date.today())}-{next_number(root, today_prefix(date.today()))}"

    # Stage first, then ask git what is actually staged. Doing it in this order
    # catches untracked files too -- `status` before `add` would not.
    if args.dry_run:
        pending = git("status", "--porcelain", root=root)
        if not pending:
            print("nothing to commit -- working tree is clean")
            return 0
        print(f"would commit as: {message}")
        print(pending)
        return 0

    git("add", "-A", "--", root, root=root)

    staged = git("diff", "--cached", "--name-status", root=root)
    if not staged:
        print("nothing to commit -- working tree is clean")
        return 0

    commit_args = ["commit", "-m", message]
    if args.note:
        commit_args += ["-m", args.note]
    git(*commit_args, root=root)

    print(f"committed: {message}")
    for line in staged.splitlines():
        print(f"  {line}")

    if args.push:
        branch = git("rev-parse", "--abbrev-ref", "HEAD", root=root)
        print(f"pushing {branch} -> origin ...")
        git("push", "origin", branch, root=root)
        print("pushed")

    return 0


if __name__ == "__main__":
    sys.exit(main())
