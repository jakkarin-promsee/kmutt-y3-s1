---
name: vault-writing
description: Link syntax, formatting, and prose-wrap rules for this Obsidian coursework vault. Load before writing or editing ANY markdown here — INDEX.md entries, class notes, CLAUDE.md — and any time you mention a vault file, because every mention must be a [[wiki-link]] with exact syntax (extensions on non-.md files, path-qualified ambiguous basenames, literal heading anchors). Also covers when NOT to link (folders, dot-folders, placeholders), verifying links with check-links.py rather than a hand-rolled checker, the <br/> line-break rule, and the never-reflow rule.
---

# Writing rules — 1_Uni vault

The vault is an Obsidian vault. Two things follow from that, and they're the whole skill: **file
mentions are links**, and **source line breaks are not render line breaks**.

---

## §1 — Linking

Every reference to a **real file inside the vault** is an Obsidian link, not inline code.
`` `Syllabus_CPE333.pdf` `` is dead text; `[[Syllabus_CPE333.pdf]]` is clickable, shows up in
backlinks and the graph, and re-points itself when the file is renamed inside Obsidian.

### Forms

| Target | Write it as | Note |
| --- | --- | --- |
| A note or a text cache (`.md`) | `[[Lecture1_IntroductionToOS]]` | no extension → Obsidian assumes `.md` |
| A PDF / PPTX / any non-`.md` file | `[[Syllabus_CPE333.pdf]]` | **extension required**, or it won't resolve |
| A PDF *and* its cache | `[[Name.pdf]]` = source · `[[Name]]` = cache | the extension is the only difference |
| A heading inside a note | `[[#Formula cheat-sheet]]` · `[[lecture1#Exam focus]]` | see the anchor rule below |
| A nicer label | `[[Lecture+1+-+Introduction.pdf\|Lecture 1 — Introduction]]` | `\|` separates link from display text |
| Show it inline | `![[Syllabus_CPE333.pdf#page=3]]` | leading `!` embeds instead of links |

### The extension has to be one Obsidian *recognizes*

Writing the extension isn't enough on its own. Out of the box Obsidian only indexes `.md`, `.pdf`,
`.canvas`, and common image/audio/video types — **`.pptx`, `.py`, `.docx` and `.xlsx` are invisible
to it**, so `[[Lecture1_IntroductionToOS.pptx]]` and `[[save-checkpoint.py]]` render as links and
resolve to nothing. Exactly the silent failure this skill exists to prevent.

**This vault requires *Settings → Files and links → Detect all file extensions* to be ON.** It
writes `showUnsupportedFiles: true` into `.obsidian/app.json` — and in this repo that file is
**committed, not gitignored**, so it's one click *once* and every clone inherits it. Commit
`app.json` after flipping it, or the fix stays on one machine.

`check-links.py` reads that file, so it reports the real state rather than assuming: with the
setting off, every `[[…py]]` and `[[…pptx]]` link comes back as **DEAD EXTENSION**, because it is
genuinely dead. Two caveats: Obsidian keeps this config in memory and only writes it on exit, so a
just-flipped setting shows up after you close the app — and **never hand-edit `.obsidian/`** for the
same reason, since Obsidian will overwrite whatever you put there.

### Not links — keep these as inline code

- **Folders** — `assignment/`, `lecture/`, `note/`, `temp/`, `format-template/`. Obsidian links
  files, not folders.
- **Dot-folders** — anything under `.claude/` or `.obsidian/`, including this skill and the
  `/update-index` command. Obsidian ignores them, so a link there is permanently unresolved.
- **Anything outside the vault** — `~/.claude/CLAUDE.md`, shell paths. For URLs and email use a
  normal markdown link (`[text](https://…)`, `[addr](mailto:addr)`).
- **Placeholders and patterns** — `<name>.pdf`, `lecture/<name>.md`, `feature/<issue#>-<slug>`, or a
  bare extension like `.md`. They describe a shape, not a file that exists.

### Ambiguous basenames → path-qualify

`CLAUDE.md` and `INDEX.md` exist in *every* class folder, so a bare `[[INDEX]]` silently resolves to
whichever copy is closest to the current note — and re-points somewhere else the moment that note
moves. Write the full vault path with an alias:

- `[[CPE342-machine-learning/INDEX|INDEX.md]]`
- `[[CPE342-machine-learning/CLAUDE|CPE342 CLAUDE.md]]`

Same for any note name that repeats across classes — `lecture1.md`, `lab1.md`, and so on.

### The two exceptions

**The root `CLAUDE.md`** can't be wiki-linked from inside a class folder — there's no folder prefix
to disambiguate it from the class's own `CLAUDE.md`. Use a relative markdown link:

```markdown
For vault-wide rules, see the root [CLAUDE.md](../CLAUDE.md).
```

**`README.md`** uses relative markdown links throughout, because GitHub renders `[[…]]` as literal
dead text. Relative links work in both GitHub and Obsidian.

### Heading links are literal, not slugs

GitHub-style `[Exam focus](#exam-focus)` does **not** resolve in Obsidian. The link must copy the
heading's exact characters, including `§` and em dashes: `## §1 — Linking` → `[[#§1 — Linking]]`.

### After any rename or move, fix the links

Obsidian auto-updates links only for renames done *inside* Obsidian — not for files moved in
Explorer or by a shell command. A wiki-link to a file that no longer exists is worse than no link,
because it still looks valid.

### Verifying links — run the script, don't grep

`check-links.py` at the vault root is the authority on whether a link resolves. **Never hand-roll a
checker** — writing a throwaway script, grepping for `[[`, or spot-checking with `ls` costs more
than the script and gets less:

```bash
python check-links.py                       # whole vault
python check-links.py CPE342-machine-learning
```

Run it after any rename, move, or delete, and before finishing an edit that added links. It reads
both syntaxes (`[[wiki]]` and `[text](relative)`), blanks out code fences and LaTeX first — this
file alone quotes a dozen `[[…]]` examples that are **not** links — skips `format-template/`, whose
placeholder links are fake on purpose, and checks `#Heading` anchors literally, which is the only
way to catch a table of contents broken by a reworded heading.

It separates **broken** (fix these) from **warnings** (advisory: ambiguous basenames, case-only
matches, wiki-links in `README.md`). `DEAD EXTENSION` counts as broken, and the fix is the Obsidian
setting above — **never** by deleting the link or dropping the extension off it.

---

## §2 — Formatting

### A single newline renders as nothing

Markdown joins the lines of a paragraph into one flowing line, so this:

```markdown
**Built by a student at KMUTT**
who decided this beat doing the homework.
```

renders as one run-on line. To force a visible break, end the line with `<br/>`. (Two trailing
spaces also work, but editors and formatters strip trailing whitespace and silently break it again.)
A blank line starts a new paragraph.

### Match the wrap style of the file you're editing

Where a line ends in the *source* is a separate question from how it renders. The renderer doesn't
care; the user does — they read the raw files.

- **`README.md` → one line per paragraph.** No hard wrapping; the editor soft-wraps it. Already
  converted — keep it that way.
- **Every other doc → whatever that file already does.** The class `CLAUDE.md` / `INDEX.md` files
  and this one are wrapped at ~100 columns. That's fine; leave it.
- **Never reflow a whole file as a side effect of an unrelated edit.** It buries the real change in
  diff noise. This outranks any preference about wrap width.

### Never reflow code fences, tables, or mermaid blocks

There a newline *is* structural: one table row per line, one mermaid statement per line. Reflowing
them breaks the render.
