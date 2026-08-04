# 1_Uni — Semester Coursework Vault

Root instructions for Claude. This folder is my (single) workspace for **all classes this
semester**. It is an **Obsidian vault** (`.obsidian/`), so every reference to a file in the vault is
an Obsidian `[[wiki-link]]` — see the **Linking Rule** below — and each `INDEX.md` acts as a Map of
Content.

**Read order when working:** this file → the target class's own `CLAUDE.md` → that class's
`INDEX.md` → the actual files. Do not skip the class-level `CLAUDE.md`.

---

## Classes — this semester

One folder per class. Folder name = `<CODE>-<kebab-case-name>` (e.g. `CPE342-machine-learning`).

| Code   | Course               | Folder                        | Status      |
| ------ | -------------------- | ----------------------------- | ----------- |
| CPE333 | Operating Systems    | `CPE333-operating-systems`    | **active**  |
| CPE334 | Software Engineering | `CPE334-software-engineering` | **active**  |
| CPE342 | Machine Learning     | `CPE342-machine-learning`     | **active**  |
| GEN101 | Physical Education   | `GEN101-physical-education`   | not created |
| GEN241 | Beauty of Life       | `GEN241-beauty-of-life`       | not created |
| PRE380 | Engineering Economy  | `PRE380-engineering-economy`  | not created |

> Keep this table in sync. When a class folder is created/renamed, update the row's Status.
> Folder names above are the intended convention — create them exactly like this so navigation
> is predictable. (`CPE333`, `CPE334`, and `CPE342` exist so far.)

---

## Folder layout — every class

All classes use the **same** layout:

```
<CODE>-<name>/
├── assignment/   Assignment briefs, my working files, and submissions
├── lecture/      Slides / PDFs / readings handed out by the lecturer
├── note/         My own notes worth keeping (from lecture or while doing assignments)
├── temp/         Scratch — messy, short-lived, "some shit". Never documented.
├── CLAUDE.md     Per-class instructions: course info + class-specific rules
└── INDEX.md      Annotated map of the folder so an agent understands it without opening every file
```

Rules of thumb for where a file goes:

- From the lecturer → `lecture/`.
- About a specific assignment → `assignment/`.
- My own writing worth keeping that isn't tied to one assignment → `note/`.
- Anything throwaway or half-baked → `temp/`.

A blank, ready-to-copy version of `CLAUDE.md` + `INDEX.md` lives in `format-template/`. To start a
new class: copy `format-template/` to `<CODE>-<name>/` and fill in the two files.

---

## Navigation rules (for Claude)

1. **Go straight to the class folder.** Don't `ls`/read the root each session — the root holds only
   this file, the template, shared config, and the class folders. (Exception: a task explicitly
   about the vault structure, like updating this file.)
2. **Read the class's `CLAUDE.md` first**, then its `INDEX.md`, before touching its files.
3. **Stay in the active class.** If I'm working on CPE342, don't `ls` or read CPE334, etc. — unless
   I ask you to.
4. **`temp/` is volatile.** Always `ls temp/` fresh when you need it; never rely on it being
   documented, and never record its contents in any `CLAUDE.md` or `INDEX.md`.

---

## Maintenance rules

1. **Keep the docs matching disk.** I often dump downloaded lectures / notes / assignments without
   updating anything. If you notice drift while working, fix it:
   - New/renamed/removed files in a class → update that class's `INDEX.md` (and its `CLAUDE.md` if
     structure or course facts changed).
   - New/renamed class folder → update the **Classes** table above.
   - **Do not** track `temp/` in any doc.
2. Prefer the smallest correct edit. Don't rewrite a whole doc to fix one stale line.
3. Downloaded files often arrive with `+`-encoded names (e.g. `Lecture+1+-+Intro.pdf`). You may
   note the human-readable title in `INDEX.md`; renaming the actual file is optional and my call.
4. **Every file you mention gets a link**, per the **Linking Rule** below. When you add, rename, or
   move a file, update the links pointing at it — a wiki-link to a file that no longer exists is
   worse than no link, because Obsidian shows it as valid-looking but dead.

---

## Reading Rule — cache PDFs as Markdown

PDFs (especially slide decks) are heavy: pages load as images, so reading them burns a lot of
context. Cache a lightweight text version next to each PDF and read that instead.

1. **Before reading `<name>.pdf`, look for `<name>.md` in the same folder.** If it exists and is at
   least as new as the PDF, read the `.md` — not the PDF.
2. **No `.md` yet (or it's older than the PDF)? Create it, cheapest way first:**
   1. `pdftotext -layout -enc UTF-8 "<name>.pdf" "<name>.md"` — poppler, already installed. Free, no
      model. Good whenever the PDF is mostly prose (e.g. a syllabus).
   2. **If the PDF is formula-heavy, figure-heavy, or scanned** (lecturer slide decks), `pdftotext`
      mangles the math and drops the figures. Fall back to a **Sonnet subagent** that _reads the
      pages_ and writes a faithful `<name>.md`: transcribe the text, rewrite every equation as LaTeX
      (`$…$` / `$$…$$`), and describe each figure in one italic line. This keeps the heavy image
      reads inside the subagent, out of the main thread's context.
3. **The `.md` is a proxy, not a replacement.** Even the best conversion loses layout and some
   figure detail. If the task truly needs the visuals, read the PDF page(s) directly.
4. **Record every generated `.md` in `INDEX.md`** on the source file's own entry, as
   `*(text cache: [[<name>]])*` — per the **Linking Rule** below. Never for `temp/`.

> This cache `.md` is a raw transcription — different from a study note in `note/`, which is my own
> authored summary. So one slide deck can have both: `lecture/<name>.md` (cache) and
> `note/<lectureN>.md` (my summary).

---

## Linking Rule — Obsidian links, not bare paths

This is an Obsidian vault, so **every reference to a real file in the vault must be a link**, not
inline code. `` `Syllabus_CPE333.pdf` `` is dead text; `[[Syllabus_CPE333.pdf]]` is clickable, shows
up in backlinks and the graph, and Obsidian re-points it automatically if the file is renamed.

**Write a link when the target is a real file inside the vault:**

| Target | Write it as | Note |
| --- | --- | --- |
| A note or a text cache (`.md`) | `[[Lecture1_IntroductionToOS]]` | no extension → Obsidian assumes `.md` |
| A PDF / PPTX / any non-`.md` file | `[[Syllabus_CPE333.pdf]]` | **extension required**, or it won't resolve |
| A PDF *and* its cache | `[[Name.pdf]]` = source · `[[Name]]` = cache | the extension is the only difference |
| A heading inside a note | `[[#Formula cheat-sheet]]` · `[[lecture1#Exam focus]]` | see the anchor warning below |
| A nicer label | `[[Lecture+1+-+Introduction.pdf\|Lecture 1 — Introduction]]` | `\|` separates link from display text |
| Show it inline | `![[Syllabus_CPE333.pdf#page=3]]` | leading `!` embeds instead of links |

**Keep these as inline code — they are NOT links:**

- **Folders** — `assignment/`, `lecture/`, `note/`, `temp/`, `format-template/`. Obsidian links
  files, not folders.
- **Dot-folders** — anything under `.claude/` or `.obsidian/`. Obsidian ignores them, so a link
  there is permanently unresolved.
- **Anything outside the vault** — `~/.claude/CLAUDE.md`, shell paths. For URLs and email use a
  normal markdown link (`[text](https://…)`, `[addr](mailto:addr)`).
- **Placeholders and patterns** — `<name>.pdf`, `lecture/<name>.md`, `feature/<issue#>-<slug>`, or a
  bare extension like `.md`. They describe a shape, not a file that exists.

**Ambiguous basenames → path-qualify.** `CLAUDE.md` and `INDEX.md` exist in *every* class folder, so
a bare `[[INDEX]]` silently resolves to whichever copy is closest to the current note — and
re-points somewhere else the moment that note moves. Always write the full vault path with an alias:

- `[[CPE342-machine-learning/INDEX|INDEX.md]]`
- `[[CPE342-machine-learning/CLAUDE|CPE342 CLAUDE.md]]`

Same for any note name that will repeat across classes — `lecture1.md`, `lab1.md`, and so on.

**The root `CLAUDE.md` is the one exception — use a relative markdown link.** A wiki-link cannot
distinguish the vault-root `CLAUDE.md` from the same-named file in a class folder (there is no
folder prefix to qualify it with), so from inside a class folder write:

```markdown
For vault-wide rules, see the root [CLAUDE.md](../CLAUDE.md).
```

**Heading links match the literal heading text, not a GitHub slug.** GitHub-style
`[Exam focus](#exam-focus)` does **not** resolve in Obsidian. The heading is `## Exam focus`, so the
link is `[[#Exam focus]]` — copy the exact characters, including `§` and em dashes:
`[[#§1 — Statistical Learning]]`.

**After any rename or move, fix the links.** Obsidian only auto-updates links for renames done
*inside* Obsidian — not for files moved in Explorer or by a shell command.

---

## Formatting Rule — line breaks and prose wrap

**A single newline renders as nothing.** Markdown joins the lines of a paragraph into one flowing
line, so this:

```markdown
**Built by a student at KMUTT**
who decided this beat doing the homework.
```

renders as one run-on line, not two. To force a visible break, end the line with `<br/>`. (Two
trailing spaces also work, but editors and formatters strip trailing whitespace and silently break
it again — use `<br/>`.) A blank line starts a new paragraph.

**Don't hard-wrap prose mid-sentence.** Where a line ends in the *source* is a separate question
from how it renders. The renderer doesn't care; I do — I read the raw file, and a sentence chopped
across two lines is annoying to read.

- **`README.md` → one line per paragraph.** No hard wrapping; the editor soft-wraps it. Already
  converted — keep it that way.
- **Every other doc → match the file you're editing.** The class `CLAUDE.md` / `INDEX.md` files are
  still wrapped at ~100 columns, and that's fine. Never reflow a whole file as a side effect of an
  unrelated edit — it buries the real change in diff noise.

**Never reflow code fences, tables, or mermaid blocks.** There a newline *is* structural: one table
row per line, one mermaid statement per line. Reflowing them breaks the render.

---

## How to work with me (this matters as much as the commands)

I'm a first-time student at this — a KMUTT Computer Engineering undergrad doing this workflow for
the first time. Treat every task as collaborative, not just order-taking:

- **Teach and lecture me** as you go. Explain the _why_, not just the _what_.
- **Brainstorm** — if you see a better approach than what I asked for, say so and, when it's clearly
  right, just do it (then tell me what you changed and why).
- **Catch my mistakes.** My instructions may be wrong or miss something even when they sound
  confident. You often have the whole picture I don't — if I'm wrong, tell me I'm wrong.
- Bias toward being genuinely useful over being agreeable. I'd rather be corrected than flattered.

---

## Root contents (map)

- `CLAUDE.md` — this file. Universal vault rules; read first.
- `README.md` — the public, GitHub-facing pitch for the vault (repo: `kmutt-y3-s1`). Explains the
  ingest pipeline and the "hard compute once, cheap forever" idea. **Exception to the Linking
  Rule:** it uses relative markdown links (`[CLAUDE.md](CLAUDE.md)`), not `[[wiki-links]]`, because
  GitHub renders `[[…]]` as literal dead text. Relative links work in both GitHub and Obsidian.
- `PROBLEM.md` — my running pain-point / issue list for the vault itself. Agents ignore it unless
  I ask for help with it.
- `format-template/` — the copy-me starting point for a new class (contains blank `CLAUDE.md` +
  `INDEX.md`).
- `<CODE>-<name>/` — one folder per class (see table).
- `.obsidian/` — Obsidian vault config. Don't hand-edit unless asked.
- `.claude/` — Claude Code settings for this project (`settings.local.json`).

Shared tooling / skills (e.g. `graphify`) is configured in the global `~/.claude/CLAUDE.md`; if any
vault-level tool or agent config is added here later, document its path and purpose in this section.

---

## Tooling & roadmap

**Built:**

- **`/update-index [folder]`** — slash command at `.claude/commands/update-index.md`. `ls` a
  class folder, **convert any un-cached PDF to Markdown** (per the Reading Rule), diff the folder
  against its `INDEX.md` + `CLAUDE.md`, and update both to match reality (plus the Classes table for
  a new/renamed folder). The **Maintenance rules** + **Reading Rule** above are the manual version.

**Ideas — not built yet:**

- **Skills** — none decided yet. I'll add them once I've used this template enough to feel the pain
  points.
