---
name: pdf-cache
description: Read the Markdown cache, never the PDF itself. Load before opening ANY .pdf in this coursework vault — lecture slides, syllabi, assignment briefs. Covers checking for an existing <name>.md sibling cache, generating one when it's missing or stale (pdftotext for prose, a Sonnet subagent for decks with math or figures), and recording it on the source file's INDEX.md entry. Use whenever a task would otherwise mean reading PDF pages directly.
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

1. **Record it in `INDEX.md`** on the source file's own entry, as `*(text cache: [[<name>]])*`. It
   never gets a bullet of its own — the cache belongs to the PDF. A `.md` with **no** sibling PDF
   (a real note in `note/`) *is* its own entry.
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
