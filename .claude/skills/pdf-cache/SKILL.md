---
name: pdf-cache
description: Read the Markdown cache, never the PDF itself. Load before opening ANY .pdf or .pptx in this coursework vault — lecture slides, syllabi, assignment briefs. Covers the single authoritative cache check — check-pdf-cache.py, the only thing that reads each folder's .pdfignore, and never something to re-derive from a file listing — generating a cache when it's missing or stale (pdftotext for prose, a Sonnet subagent for decks with math or figures), the extra hop for PowerPoint originals (.pptx → reading-copy .pdf → .md), and recording it on the original's INDEX.md entry. Use whenever a task would otherwise mean reading PDF or slide pages directly.
---

# PDF → Markdown caching

PDF pages load as **images**. Reading one is expensive and lossy, and the cost repeats every session.
So every PDF in this vault gets a permanent Markdown twin, generated once and read forever after.

---

## The rule — one question, one authority

**"Does this file have a Markdown cache?" is answered by `check-pdf-cache.py`, and by nothing
else.** Not by an `ls`, not by a `find`, not by a Glob, not by what you remember from earlier in
the session. Run it *before* reading any PDF and *before* generating anything:

```bash
python check-pdf-cache.py "CPE342-machine-learning/lecture/Lecture+1+-+Introduction+to+ML.pdf"
python check-pdf-cache.py CPE342-machine-learning
```

A **file** argument checks that one document; a **folder** argument walks it and lists every source
still uncached (or prints `nothing to do`). `.pptx` + `.pdf` of one basename count as one document,
`temp/` and dot-folders are skipped, and paths come back vault-relative.

| Answer | What it means | What you do |
| --- | --- | --- |
| `CACHED` | the `.md` twin exists and is current | read the `.md`. **Done — do not open the PDF** |
| `MISSING` | no cache yet | generate one, per the sections below |
| `EXPORT` | a `.pptx` whose `.pdf` reading copy is missing | ask the user to export it — see below |
| `IGNORED` | a `.pdfignore` rule matched | **generate nothing.** The user marked this file not worth the tokens; open the PDF directly only if the task genuinely needs its contents, and say that you're doing it |

Flags worth knowing: `--all` prints every source with its status (not just the pending ones),
`--json` for structured output, `--stale` also flags caches older than their source — that last one
reads modification times, which a fresh `git clone` resets, so trust it only on a working copy.

Exit status is 0 whenever the scan ran; pending work is not an error. A `2` means the path was wrong.

**Its answer is final. Act on it and move on** — do not confirm it, do not spot-check one file "to
be safe", do not re-derive it from a listing you happen to already have on screen.

### Why re-checking by hand is *worse*, not safer

This is the part worth internalising: a directory listing cannot answer this question, so a
hand-check doesn't add a safety net — it produces a **less accurate** answer and then overrides a
more accurate one. Four things the script knows and a listing structurally cannot:

1. **`.pdfignore` is invisible in a listing.** The rule that governs a file can live in a parent
   folder you never listed, in any of several `.pdfignore` files across the vault. A PDF that looks
   uncached to you may be deliberately uncached — regenerating it is exactly what the user asked
   nobody to do.
2. **A `.pptx`, its reading-copy `.pdf` and their `.md` are one document, not three files.** A
   listing shows three lines and invites the wrong conclusion — most often "the `.pptx` needs its
   own cache", which ends in `pdftotext` being pointed at a `.pptx`.
3. **Basename pairing has a trap.** `Lecture+2.v2.pdf` pairs with `Lecture+2.v2.md`, not
   `Lecture+2.md`. Eyeballing similar-looking names gets this wrong silently.
4. **`temp/` and dot-folders are excluded**, and staleness needs modification times a listing
   doesn't show you.

The cost argument is real too — one call versus a walk plus a comparison per folder — but accuracy
is the actual reason. **Being thorough here means running the script, not double-checking it.**

### When the answer looks wrong

Say so, out loud, to the user — then stop. Do **not** quietly fall back to checking by hand; that
converts a script bug into a silent wrong answer nobody can see.

- Want more detail first? `--all` shows every source with its status, `--json` is structured. Those
  are the escalation path, not `ls`.
- `IGNORED` on a file you think matters → tell the user it's ignored and why you'd want it. The
  `.pdfignore` is their decision, not yours to route around.

Listing a folder for a *different* question — what files exist, for an `INDEX.md` diff — is fine
and normal. Just never let that listing answer the cache question.

### `.pdfignore` — files the user doesn't want cached

Any folder may hold one, and each class can have its own; the rules cover that folder and everything
beneath it, deeper files layering on top, exactly like `.gitignore`. `#` comments, `!` negation,
`*` `?` `**` globs and a trailing `/` for directory-only all behave the same. Windows separators are
read as separators (`assignment\Lab-1\report.pdf`), because that's how paths get copied out of
Explorer.

It exists because some PDFs are pure cost: a submitted report full of screenshots, a 300-page
interest table. **Never add or edit rules on your own** — the user decides what isn't worth
rendering. If a file looks like a waste of tokens to cache, say so and let them add the line.

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

## Recording a cache in `INDEX.md`

This is the rule any time an `INDEX.md` is written — not only right after generating something, but
equally when diffing a folder where nothing new was cached.

1. **The bullet belongs to the source file; the cache hangs off it** as `*(text cache:
   [[<name>]])*`. A cache never gets a bullet of its own, and neither does a reading-copy `.pdf`
   exported from a `.pptx` — both are derivatives of the entry above them.
2. **A `.md` with no sibling source file** — a real note in `note/` — *is* its own entry.
3. **Never** cache, list, or document anything under `temp/`.

---

## The cache is not the source of truth

When two of them disagree, the ranking is:

> **`.pdf` (or the lecturer's `.pptx`) — the truth**
> **↳ its `.md` cache — a lossy machine translation of the truth**
> **↳ `INDEX.md` — a hand-written summary *of the cache***

Every step down loses something. `pdftotext` mangles layout and drops figures; a subagent
transcribing eighty slides will occasionally emit an equation that looks plausible and is simply
wrong. That is expected, and it's an acceptable trade — the cache exists to make the whole vault
cheap to read, **not to be quoted as evidence**.

So: work from the `.md` by default. That is the entire point of the system and most questions never
need more. But **open the actual PDF page whenever the answer depends on**:

- an exact number, coefficient, or table value,
- a formula you're about to reproduce or compute with,
- a figure or diagram you must reason about, or a table whose *structure* matters,
- the lecturer's precise wording — anything gradable, anything being quoted,
- anything in the cache that looked surprising, garbled, or too convenient.

Say which one you used when it matters. Reading the PDF for these reasons isn't the cache failing —
it's the cache doing its job of telling you *which page* to open.

**One documented inversion exists.** Some PRE380 decks hide their worked solutions in PowerPoint
animation layers, so the text layer holds content the rendered page never shows and the cache is
genuinely *more* complete than the PDF. That class's `CLAUDE.md` says so explicitly. Treat it as the
exception it is — do not generalise it to other classes.

---

## Related

- A cache `.md` is a raw transcription. A study note in `note/` is the user's own authored summary.
  One slide deck can have both: `lecture/<name>.md` (cache) and `note/<lectureN>.md` (summary).
- `check-pdf-cache.py` is documented in the root `CLAUDE.md` too; `python check-pdf-cache.py --help`
  lists every flag.
- `/update-index` runs this whole procedure across an entire class folder at once.
- Writing the `INDEX.md` entry correctly is the `vault-writing` skill.
