# 1_Uni — Semester Coursework Vault

Root instructions for Claude. One workspace for **all my classes this semester**. It is an
**Obsidian vault**, so every reference to a vault file is a `[[wiki-link]]`, and each `INDEX.md` is
the Map of Content for its class.

**Read order:** this file → the target class's `CLAUDE.md` → its `INDEX.md` → the actual files.
Never skip the class-level `CLAUDE.md`.

**Two skills hold the detail** — `vault-writing` (link syntax, formatting, prose wrap) and
`pdf-cache` (PDF → Markdown). They are the source of truth for their procedures; what this file says
about them is a trigger, not the rule. Load the skill before writing links, reflowing prose, or
opening a PDF.

---

## Classes — this semester

Folder name = `<CODE>-<kebab-case-name>`. The names below are the intended convention — create them
exactly like this, and keep the Status column in sync.

| Code   | Course               | Folder                        | Status      |
| ------ | -------------------- | ----------------------------- | ----------- |
| CPE333 | Operating Systems    | `CPE333-operating-systems`    | **active**  |
| CPE334 | Software Engineering | `CPE334-software-engineering` | **active**  |
| CPE342 | Machine Learning     | `CPE342-machine-learning`     | **active**  |
| GEN101 | Physical Education   | `GEN101-physical-education`   | not created |
| GEN241 | Beauty of Life       | `GEN241-beauty-of-life`       | not created |
| PRE380 | Engineering Economy  | `PRE380-engineering-economy`  | **active**  |

---

## Folder layout — identical for every class

```
<CODE>-<name>/
├── assignment/   Assignment briefs, my working files, and submissions
├── lecture/      Slides / PDFs / readings handed out by the lecturer
├── note/         My own notes worth keeping (from lecture or while doing assignments)
├── temp/         Scratch. Messy, short-lived, "some shit". Never documented.
├── CLAUDE.md     Per-class instructions: course info + class-specific rules
└── INDEX.md      Annotated map of the folder, so an agent gets it without opening every file
```

Where a file goes: from the lecturer → `lecture/` · about one assignment → `assignment/` · my own
keepable writing not tied to an assignment → `note/` · throwaway or half-baked → `temp/`.

New class: copy `format-template/` to `<CODE>-<name>/`, fill in its two files, add the table row.

---

## Navigation

1. **Go straight to the class folder.** Don't `ls`/read the root each session — it holds only this
   file, shared config, and the class folders. (Exception: the task is about the vault itself.)
2. **Class `CLAUDE.md` first, then its `INDEX.md`**, before touching any of its files.
3. **Stay in the active class.** Working on CPE342 → don't `ls` or read CPE334, unless I ask.
4. **`temp/` is volatile.** Always `ls temp/` fresh; never document its contents anywhere.

---

## Maintenance

I dump downloaded lectures and assignments in without updating anything. If you notice drift while
working, fix it:

1. Files added / renamed / removed in a class → update that class's `INDEX.md`, and its `CLAUDE.md`
   if course facts or structure changed. **Never track `temp/`.**
2. New or renamed class folder → update the **Classes** table above.
3. **Smallest correct edit.** Don't rewrite a doc to fix one stale line, and never reflow a file as
   a side effect of an unrelated change.
4. **Every vault file you mention gets a `[[link]]`.** After a rename or move done outside Obsidian,
   fix the links pointing at it — a dead wiki-link still looks valid, which is worse than no link.
   Syntax, edge cases and verification are the `vault-writing` skill; whether a link still resolves
   is [[check-links.py]]'s job, never a hand-written checker:

   ```bash
   python check-links.py <path>
   ```

5. `+`-encoded download names (`Lecture+1+-+Intro.pdf`) can stay; note the readable title in
   `INDEX.md`. Renaming the actual file is my call.

---

## Reading PDFs — read the cache, not the PDF

PDF pages load as images and burn context, so every `.pdf` / `.pptx` here gets a `<name>.md` twin,
generated once and read forever after. **Which files have one is decided by [[check-pdf-cache.py]]
and by nothing else** — not `ls`, not `find`, not Glob, which can't see `.pdfignore` and pair
basenames wrong:

```bash
python check-pdf-cache.py <path>
```

**Take its answer and act on it — don't verify it.** Listing a folder to see what files exist (for
an `INDEX.md` diff) is fine; just never let that listing decide the cache question. If a result
looks wrong, tell me.

The four statuses, generating a missing cache, the `.pptx` hop, `.pdfignore` semantics and the
`INDEX.md` bookkeeping are all in the `pdf-cache` skill — load it before opening any PDF.
`/update-index` runs the whole procedure across a class folder at once.

---

## How to work with me (this matters as much as the rules)

I'm a KMUTT Computer Engineering undergrad doing this workflow for the first time. Treat every task
as collaborative, not order-taking:

- **Teach and lecture me** as you go. Explain the _why_, not just the _what_.
- **Brainstorm** — if you see a better approach than what I asked for, say so, and when it's clearly
  right just do it (then tell me what you changed and why).
- **Catch my mistakes.** My instructions may be wrong or miss something even when they sound
  confident. You often have the whole picture I don't — if I'm wrong, tell me I'm wrong.
- Bias toward being genuinely useful over being agreeable. I'd rather be corrected than flattered.

---

## Root files

- `README.md` — public GitHub-facing pitch (repo: `kmutt-y3-s1`). Uses relative markdown links, not
  wiki-links, because GitHub renders `[[…]]` as dead text.
- `prompts ` — my reusable prompts set. Ignore unless I ask.
- `PROBLEM.md` — my pain-point / roadmap list for the vault itself. Ignore unless I ask.
- [[check-pdf-cache.py]] — `python check-pdf-cache.py <path>` answers "does this PDF already have a
  Markdown cache?" for one file or a whole folder, `.pdfignore` included. See **Reading PDFs**
  above; `--all`, `--stale` and `--json` are in `--help`.
- [[check-links.py]] — `python check-links.py <path>` verifies every `[[wiki-link]]` and
  `[text](relative)` link, including `#heading` anchors. Ignores code, LaTeX and
  `format-template/`. `--strict` exits 1 on breakage; `--json` for structured output.
- [[save-checkpoint.py]] — `python save-checkpoint.py` stages the whole vault and commits as
  `<dd>/<mm>/<BE year>-<n>`, whichever folder it's run from — though Python still needs the path, so
  from inside a class folder that's `python ../save-checkpoint.py`. Add `--push` to also push. Run
  `--help` for flags.
- `format-template/` — copy-me starting point for a new class.
- `.obsidian/` — vault config, don't hand-edit. `.claude/` — settings, slash commands and skills.
