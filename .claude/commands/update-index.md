---
description: Sync a class folder's INDEX.md (and CLAUDE.md) with disk — including PDF→Markdown caches
argument-hint: "[folder]  — e.g. CPE342-machine-learning; omit to use the class in context"
allowed-tools: Bash(find:*), Bash(ls:*), Bash(pdftotext:*), Bash(python check-pdf-cache.py:*), Bash(python check-links.py:*), Read, Edit, Write, Glob, Task
---

You are running the **`/update-index`** maintenance command for this Obsidian coursework vault.
Read the root `CLAUDE.md` first (folder layout, naming, "never document `temp/`", read order), then
load the `pdf-cache` and `vault-writing` skills — they hold the procedures this command runs.

## Target folder

`$1`

- If `$1` is empty, use the class folder currently in context. If ambiguous, ask which class first.
- `$1` is a class folder like `CPE342-machine-learning` (or `.` for the vault root → only sync the
  **Classes** table in `CLAUDE.md`).

## Steps

1. **List reality.** Recursively list the target's files, excluding `temp/` and dotfiles/dotdirs:
   `find "$1" -not -path '*/temp/*' -not -path '*/.*' -type f | sort`

   This listing is for the `INDEX.md` diff in step 4 — *which files exist*. **It is not how you
   decide which PDFs need a cache**, however obvious it looks: it can't see `.pdfignore` (the rules
   may live in a parent folder), and it shows a `.pptx` chain as three separate files. Step 2 owns
   that question.

2. **Ensure every PDF has a Markdown cache (`pdf-cache` skill).** The script is the authority on
   what's missing. Run it even when you just listed the folder and think you already know:

   ```bash
   python check-pdf-cache.py "$1"
   ```

   (from inside a class folder it's `python ../check-pdf-cache.py .`)

   Then act on each line it prints, and **only** on those:
   - `MISSING` → generate the cache:
     - `pdftotext -layout -enc UTF-8 "<name>.pdf" "<name>.md"` for text/prose PDFs (e.g. a syllabus).
     - If the PDF is **formula-heavy / figure-heavy / scanned** (lecturer slide decks), pdftotext
       mangles it — instead spawn a **Sonnet subagent** (Task tool, `model: sonnet`) that reads the
       pages and writes a faithful `<name>.md`: text transcribed, every equation as LaTeX
       (`$…$` / `$$…$$`), each figure in one italic line.
     - Unsure which? Sample the pdftotext output — if math/figures come out as blank or garbage
       (e.g. `������`), use the subagent.
   - `EXPORT` → a `.pptx` with no `.pdf` reading copy. Don't convert it; note it for the report and
     ask the user to export it.
   - Anything it doesn't list is already cached or `.pdfignore`d — **leave it alone**. A file the
     user ignored still gets its `INDEX.md` entry, just without a text-cache note.
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
   - **Every entry is a wiki-link, per the `vault-writing` skill** — `[[Name.pdf]]` for the source file,
     `[[Name]]` for its `.md` cache, path-qualified (`[[<CODE>-<name>/INDEX|INDEX.md]]`) for any
     basename that repeats across classes. Never a bare `` `path` `` in backticks.

4b. **Check the links resolve — with the script, not by hand.** Don't write your own checker and
   don't grep for `[[`; `check-links.py` already handles code fences, LaTeX, anchors, and
   `format-template/`:

   ```bash
   python check-links.py "$1"
   ```

   Fix everything under **broken** (`UNRESOLVED`, `RELATIVE`, `NOT LINKABLE`, `BAD ANCHOR`) — those
   are links left dangling by a rename or deletion, or pointed at `.claude/` / `.obsidian/` /
   a folder, none of which Obsidian resolves. Warnings are advisory: `AMBIGUOUS` means path-qualify
   it, and the `.py` / `.pptx` extension warnings are expected and stay.

5. **Update `$1/CLAUDE.md` only if course facts or structure changed** (new grading info, a rename,
   a new subfolder). Smallest correct edit — don't rewrite otherwise.

6. **Update the root `CLAUDE.md` Classes table** if this run created, renamed, or changed a class
   folder's status.

7. **Never** list, cache, or document anything under `temp/`.

## Report

End with a short summary: PDFs converted (and how), any `EXPORT` deck still waiting on the user,
files added / removed / moved, which docs you edited, and anything that looked off. If nothing
drifted and `check-pdf-cache.py` reported nothing to do, say exactly that.
