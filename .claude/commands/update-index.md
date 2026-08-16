---
description: Sync a class folder's INDEX.md (and CLAUDE.md) with disk — including PDF→Markdown caches
argument-hint: "[folder]  — e.g. CPE342-machine-learning; omit to use the class in context"
allowed-tools: Bash(find:*), Bash(ls:*), Bash(pdftotext:*), Bash(python check-pdf-cache.py:*), Bash(python ../check-pdf-cache.py:*), Bash(python check-links.py:*), Bash(python ../check-links.py:*), Read, Edit, Write, Glob, Task, Agent
---

You are running the **`/update-index`** maintenance command for this Obsidian coursework vault.

**Load the `pdf-cache` and `vault-writing` skills before step 1.** They hold every procedure this
command runs — the cache check and how to generate one, `.pptx` handling, link syntax, `INDEX.md`
entry format. This file is the running order and the scope; it deliberately does **not** restate
them, so if the two ever seem to disagree, the skill is right.

## Target folder

`$1`

- If `$1` is empty, use the class folder currently in context. If ambiguous, ask which class first.
- `$1` is a class folder like `CPE342-machine-learning` (or `.` for the vault root → only sync the
  **Classes** table in the root `CLAUDE.md`).

## Steps

1. **List reality.** Recursively list the target's files, excluding `temp/` and dotfiles/dotdirs:

   ```bash
   find "$1" -not -path '*/temp/*' -not -path '*/.*' -type f | sort
   ```

   This listing feeds the `INDEX.md` diff in step 4 — *which files exist*. **It is not how you decide
   which PDFs need a cache**, however obvious it looks. Step 2 owns that question.

2. **Cache every PDF that needs one (`pdf-cache` skill).** Run the check even though you just listed
   the folder and think you already know:

   ```bash
   python check-pdf-cache.py "$1"
   ```

   (from inside a class folder that's `python ../check-pdf-cache.py .`)

   Act on each line it prints and **only** on those, generating each one the way the skill says.
   Anything it doesn't list is already cached or `.pdfignore`d — leave it alone. Then re-run the
   step-1 listing so the new `.md` caches are included below.

3. **Read the docs.** Read `$1/INDEX.md` and `$1/CLAUDE.md`. If either is missing, create it from
   `format-template/INDEX.md` / `format-template/CLAUDE.md` and fill in what you can.

4. **Diff disk vs. `INDEX.md`.** Entry wording, wiki-link form, and which files get their own bullet
   all follow the `vault-writing` and `pdf-cache` skills:
   - On disk but not in INDEX → add an entry with a short description (skim the file if the purpose
     isn't obvious from the name; decode `+`-encoded names to a readable title).
   - In INDEX but no longer on disk → remove the entry.
   - Moved between `assignment/` `lecture/` `note/` → move its entry to the right section.

5. **Check the links resolve — with the script, not by hand:**

   ```bash
   python check-links.py "$1"
   ```

   Fix everything under **broken** (`UNRESOLVED`, `RELATIVE`, `NOT LINKABLE`, `BAD ANCHOR`).
   Warnings are advisory: `AMBIGUOUS` means path-qualify it, and the `.py` / `.pptx` extension
   warnings are expected and stay.

6. **Update `$1/CLAUDE.md` only if course facts or structure changed** (new grading info, a rename,
   a new subfolder). Smallest correct edit — don't rewrite otherwise.

7. **Update the root `CLAUDE.md` Classes table** if this run created, renamed, or changed a class
   folder's status.

**Never** list, cache, or document anything under `temp/`.

## Report

End with a short summary: PDFs converted (and how), any `EXPORT` deck still waiting on the user,
files added / removed / moved, which docs you edited, and anything that looked off. If nothing
drifted and `check-pdf-cache.py` reported nothing to do, say exactly that.
