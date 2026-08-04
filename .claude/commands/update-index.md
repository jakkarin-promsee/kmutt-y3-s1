---
description: Sync a class folder's INDEX.md (and CLAUDE.md) with disk — including PDF→Markdown caches
argument-hint: "[folder]  — e.g. CPE342-machine-learning; omit to use the class in context"
allowed-tools: Bash(find:*), Bash(ls:*), Bash(pdftotext:*), Read, Edit, Write, Glob, Task
---

You are running the **`/update-index`** maintenance command for this Obsidian coursework vault.
Read the root `CLAUDE.md` first for the conventions (folder layout, naming, the **Reading Rule**,
the **Linking Rule**, "never document `temp/`", read order).

## Target folder

`$1`

- If `$1` is empty, use the class folder currently in context. If ambiguous, ask which class first.
- `$1` is a class folder like `CPE342-machine-learning` (or `.` for the vault root → only sync the
  **Classes** table in `CLAUDE.md`).

## Steps

1. **List reality.** Recursively list the target's files, excluding `temp/` and dotfiles/dotdirs:
   `find "$1" -not -path '*/temp/*' -not -path '*/.*' -type f | sort`

2. **Ensure every PDF has a fresh Markdown cache (Reading Rule).** For each `<name>.pdf` found
   (outside `temp/`):
   - If `<name>.md` is **missing or older** than the PDF → (re)generate it:
     - `pdftotext -layout -enc UTF-8 "<name>.pdf" "<name>.md"` for text/prose PDFs (e.g. a syllabus).
     - If the PDF is **formula-heavy / figure-heavy / scanned** (lecturer slide decks), pdftotext
       mangles it — instead spawn a **Sonnet subagent** (Task tool, `model: sonnet`) that reads the
       pages and writes a faithful `<name>.md`: text transcribed, every equation as LaTeX
       (`$…$` / `$$…$$`), each figure in one italic line.
     - Unsure which? Sample the pdftotext output — if math/figures come out as blank or garbage
       (e.g. `������`), use the subagent.
   - If `<name>.md` already exists and is **at least as new** as the PDF → leave it.
   - After converting, re-run the step-1 listing so the new `.md` caches are included below.

3. **Read the docs.** Read `$1/INDEX.md` and `$1/CLAUDE.md`. If either is missing, create it from
   `format-template/INDEX.md` / `format-template/CLAUDE.md` and fill what you can.

4. **Diff disk vs. `INDEX.md`:**
   - On disk but not in INDEX → add an entry with a short description (skim the file if the purpose
     isn't obvious from the name; decode `+`-encoded names to a readable title).
   - In INDEX but no longer on disk → remove the entry.
   - Moved between `assignment/` `lecture/` `note/` → move its entry to the right section.
   - **A PDF's cache is not its own entry.** A `<name>.md` sitting next to a `<name>.pdf` of the same
     basename is that PDF's text cache: note it on the PDF's entry as "*(text cache: `[[<name>]]`)*",
     don't give it a separate bullet. A `.md` with **no** sibling PDF (e.g. a note in `note/`) *is*
     its own entry.
   - **Every entry is a wiki-link, per the Linking Rule** — `[[Name.pdf]]` for the source file,
     `[[Name]]` for its `.md` cache, path-qualified (`[[<CODE>-<name>/INDEX|INDEX.md]]`) for any
     basename that repeats across classes. Never a bare `` `path` `` in backticks.

4b. **Check the links resolve.** Every `[[target]]` you write or leave in `$1/INDEX.md` and
   `$1/CLAUDE.md` must match a real file: `[[Name]]` needs `Name.md` on disk, `[[Name.pdf]]` needs
   `Name.pdf`. Fix any link left dangling by a rename or deletion. Links into `.claude/` or
   `.obsidian/`, to folders, or to `<placeholder>` patterns are wrong — those stay inline code.

5. **Update `$1/CLAUDE.md` only if course facts or structure changed** (new grading info, a rename,
   a new subfolder). Smallest correct edit — don't rewrite otherwise.

6. **Update the root `CLAUDE.md` Classes table** if this run created, renamed, or changed a class
   folder's status.

7. **Never** list, cache, or document anything under `temp/`.

## Report

End with a short summary: PDFs converted (and how), files added / removed / moved, which docs you
edited, and anything that looked off. If nothing drifted and every PDF already had a fresh cache,
say exactly that.
