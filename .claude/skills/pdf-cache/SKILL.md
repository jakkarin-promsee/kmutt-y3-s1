---
name: pdf-cache
description: Read the Markdown cache, never the PDF itself. Load before opening ANY .pdf or .pptx in this coursework vault — lecture slides, syllabi, assignment briefs. Covers checking for an existing <name>.md sibling cache, generating one when it's missing or stale (pdftotext for prose, a Sonnet subagent for decks with math or figures), the extra hop for PowerPoint originals (.pptx → reading-copy .pdf → .md), and recording it on the original's INDEX.md entry. Use whenever a task would otherwise mean reading PDF or slide pages directly.
---

# PDF → Markdown caching

PDF pages load as **images**. Reading one is expensive and lossy, and the cost repeats every session.
So every PDF in this vault gets a permanent Markdown twin, generated once and read forever after.

---

## The rule

**Before reading `<name>.pdf`, look for `<name>.md` in the same folder.** If it exists and is at
least as new as the PDF, read the `.md` — not the PDF. Stop there.

Only if it's **missing or older than the PDF** do you generate it.

---

## When the lecturer's original is a `.pptx`

Some classes (CPE333) hand out **PowerPoint**, not PDF. Obsidian can't render `.pptx` and
`pdftotext` can't read it, so those decks go through one extra hop. The chain is three files sharing
one basename in one folder:

| File | What it is | Who made it |
| --- | --- | --- |
| `<name>.pptx` | the lecturer's original — **keep it, it's the source of truth** | lecturer |
| `<name>.pdf` | a reading copy, so the deck opens inside Obsidian | the user, by hand (PowerPoint → Save as PDF) |
| `<name>.md` | the text cache, generated from the PDF exactly as above | this skill |

**If the `.pdf` is missing:** don't try to parse the `.pptx` with `pdftotext`, and don't convert it
silently — the export is the user's call, and there's no LibreOffice on this machine to do it
headlessly. Ask them to export it. If the text is needed *right now* and no PDF exists, the global
`pptx` skill can read the deck directly; that's a one-off, not a replacement for the chain.

**In `INDEX.md`, the bullet belongs to the `.pptx`** — the original. The PDF and the cache are both
derivatives, so they hang off that one entry and never get bullets of their own:

```markdown
- [[Lecture1_IntroductionToOS.pptx]] — **Week 1**: Introduction to Operating Systems (15 slides). …
  *(reading copy: [[Lecture1_IntroductionToOS.pdf]] — my own PowerPoint→PDF export, because Obsidian
  can't render `.pptx`. Text cache: [[Lecture1_IntroductionToOS]], made from that PDF.)*
```

A `[[…pptx]]` link only resolves with **Detect all file extensions** enabled — see the
`vault-writing` skill.

---

## Generating a cache — cheapest method first

### 1. Try `pdftotext` (free, no model)

```bash
pdftotext -layout -enc UTF-8 "<name>.pdf" "<name>.md"
```

poppler, already installed. Good whenever the PDF is mostly prose — a syllabus, an assignment brief,
a course outline.

### 2. Fall back to a Sonnet subagent (math, figures, scans)

For **formula-heavy, figure-heavy, or scanned** PDFs — lecturer slide decks, mostly — `pdftotext`
mangles the math and drops the figures entirely. Spawn a **Sonnet subagent** (Task tool,
`model: sonnet`) that *reads the pages* and writes a faithful `<name>.md`:

- transcribe the text,
- rewrite every equation as LaTeX (`$…$` inline, `$$…$$` display),
- describe each figure in one italic line.

The point is that the heavy image reads happen **inside the subagent**, so they never enter the main
thread's context.

### Unsure which method?

Sample the `pdftotext` output. If math or figures come out blank or as garbage (e.g. `������`), use
the subagent.

---

## After generating

1. **Record it in `INDEX.md`** on the original's own entry, as `*(text cache: [[<name>]])*`. It
   never gets a bullet of its own — the cache belongs to the file it came from, and so does any
   reading-copy PDF exported from a `.pptx`. A `.md` with **no** sibling source file (a real note in
   `note/`) *is* its own entry.
2. **Never** cache, list, or document anything under `temp/`.

---

## Limits — when to read the PDF anyway

The cache is a **proxy, not a replacement**. Even a good conversion loses layout and figure detail.
If the task genuinely needs the visuals — a diagram you must reason about, a table whose structure
matters — read the PDF page(s) directly. That's the exception, not the fallback.

---

## Related

- A cache `.md` is a raw transcription. A study note in `note/` is the user's own authored summary.
  One slide deck can have both: `lecture/<name>.md` (cache) and `note/<lectureN>.md` (summary).
- `/update-index` runs this whole procedure across an entire class folder at once.
- Writing the `INDEX.md` entry correctly is the `vault-writing` skill.
