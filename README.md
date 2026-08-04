# KMUTT Year3 semester1 - Computer Engineering

**A context engineering platform for surviving one semester of Computer Engineering.**

> **TL;DR** — I drop a lecture PDF into a folder. The repo turns it into machine-readable Markdown, writes a summary of it into a map file, and links it into a graph. From then on, any AI agent I open here already knows what the course is, who teaches it, what's been covered, what's due, and how the lecturer wants it. I never explain my semester to a chatbot twice.

---

## The Problem

Every conversation with an AI assistant starts at zero.

You paste a slide deck. You explain that you're in Machine Learning. You explain that the deadline is one week and the lecturer forbids posted solutions. You get an answer. You close the tab. **All of that context evaporates.** Tomorrow you do it again, worse, because you forgot half the details.

Meanwhile the raw material is hostile to machines. A lecture deck is 83 slides of images — reading it burns enormous context, and every equation comes out as `������`.

So you end up paying the same expensive setup cost on every single question, forever.

## The Thesis

> ### Hard compute once. Cheap forever.

Pay the expensive cost **exactly once**, at ingest time, and write the result down in a durable, plain-text form. Every question after that is cheap, because the hard part is already on disk.

| Phase                                                                                        | Cost                                                     | How often               |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ----------------------- |
| **Ingest** — read the PDF, transcribe the math, describe the figures, summarize, index, link | Expensive (a subagent reads every page)                  | **Once per file, ever** |
| **Query** — "explain LDA", "help me plan Lab 1", "what's on the midterm?"                    | Nearly free (reads a 40-line map, then one cached `.md`) | Unlimited               |

The user's entire job is **step one of a two-step pipeline**: put the file in the folder.

---

## How It Works

```mermaid
flowchart TD
    A["📥 I drop a file<br/>lecture.pdf / lab.pdf / slides.pptx"] --> B{"Is there a fresh<br/>.md cache next to it?"}
    B -->|Yes| G
    B -->|No| C{"Prose, or<br/>math &amp; figures?"}
    C -->|"Prose (syllabus)"| D["pdftotext -layout<br/><i>free, no model</i>"]
    C -->|"Formula / figure heavy"| E["Sonnet subagent reads<br/>every page → LaTeX + figure notes<br/><i>heavy reads stay out of main context</i>"]
    D --> F["📄 name.md — the text cache"]
    E --> F
    F --> G["🗺️ INDEX.md updated<br/>annotated entry + wiki-link"]
    G --> H["📋 CLAUDE.md updated<br/>only if course facts changed"]
    H --> I["✅ Permanently cheap to read"]

    I --> Q1["❓ 'Explain Bayes classifier'"]
    I --> Q2["❓ 'Help me start Lab 1'"]
    I --> Q3["❓ 'What did I miss?'"]

    style A fill:#1e40af,stroke:#93c5fd,color:#fff
    style E fill:#7c2d12,stroke:#fdba74,color:#fff
    style I fill:#14532d,stroke:#86efac,color:#fff
```

The whole pipeline is one command: [`/update-index`](.claude/commands/update-index.md).

---

## Quick Start

```bash
git clone https://github.com/jakkarin-promsee/kmutt-y3-s1.git
cd kmutt-y3-s1
claude
```

### Daily use (this is the entire workflow)

**1. Drop the file where it belongs.**

```
CPE342-machine-learning/lecture/Lecture+2+-+Regression.pdf
```

**2. Tell the agent to absorb it.**

```bash
/update-index CPE342-machine-learning
```

**3. There is no step 3.** Ask it anything.

```
> I have Lab 1 due Friday. Walk me through what it's actually asking for.
> Quiz me on Lecture 1 — I have a midterm.
> Brainstorm three approaches for the assignment, then tell me which one is dumb.
```

The agent already read the course policies, the grading breakdown, the instructor's quirks, and every lecture you've ever added. You don't brief it. That's the point.

---

## Repository Layout

```
kmutt-y3-s1/
├── CLAUDE.md                    # 🧠 THE CONSTITUTION — vault-wide rules, read first, always
├── README.md                    # 📖 you are here
├── PROBLEM.md                   # 🐛 my running pain-point log for the system itself
│
├── format-template/             # 🧬 the seed — copy this to create a new class
│   ├── CLAUDE.md                #    blank per-class instruction file
│   └── INDEX.md                 #    blank map file
│
├── CPE333-operating-systems/    # 🟢 one folder per class, identical shape (see below)
├── CPE334-software-engineering/ # 🟢
├── CPE342-machine-learning/     # 🟢
│
├── .claude/                     # ⚙️  agent config
│   ├── commands/update-index.md #    the ingest command
│   └── settings.local.json      #    permissions
└── .obsidian/                   # 🔗 vault config (gitignored — machine-local)
```

### Every class folder is the same shape

Identical layout across all classes is not aesthetics — it's what lets an agent navigate a course it has never seen before without being told anything.

```
<CODE>-<kebab-case-name>/
├── CLAUDE.md      # 📋 course facts + class-specific rules (instructor, grading, policies)
├── INDEX.md       # 🗺️ annotated map of every file — the agent's entry point
├── lecture/       # 📚 from the lecturer: slides, PDFs, readings (+ their .md caches)
├── assignment/    # ✏️  briefs, my working files, submissions
├── note/          # 🖊️  my own writing worth keeping
└── temp/          # 🗑️  scratch. volatile. never documented. here be dragons.
```

**Where does a file go?** From the lecturer → `lecture/`. About one assignment → `assignment/`. My own keeper writing → `note/`. Half-baked garbage → `temp/`.

---

## The Three-Layer Context Protocol

The core design. An agent entering this repo reads **top-down, narrowing**, and is oriented before it opens a single real file:

```mermaid
flowchart LR
    R["<b>1. Root CLAUDE.md</b><br/>How this vault works<br/><i>rules, layout, conventions</i>"] --> C["<b>2. Class CLAUDE.md</b><br/>What this course is<br/><i>instructor, grading, policies</i>"]
    C --> I["<b>3. Class INDEX.md</b><br/>What exists in here<br/><i>annotated map of every file</i>"]
    I --> F["<b>4. The actual file</b><br/>Only the one that's needed"]

    style R fill:#1e3a5f,stroke:#7dd3fc,color:#fff
    style C fill:#3b2f63,stroke:#c4b5fd,color:#fff
    style I fill:#134e4a,stroke:#5eead4,color:#fff
    style F fill:#422006,stroke:#fcd34d,color:#fff
```

| Layer | File                          | Answers                                        | Analogy              |
| ----- | ----------------------------- | ---------------------------------------------- | -------------------- |
| 1     | Root [`CLAUDE.md`](CLAUDE.md) | _How does this system work?_                   | The OS               |
| 2     | `<class>/CLAUDE.md`           | _What is this course, and how do I help here?_ | Per-app config       |
| 3     | `<class>/INDEX.md`            | _What's in this folder, and what's it about?_  | The filesystem index |
| 4     | The file itself               | _The actual content_                           | The data             |

**Why `INDEX.md` matters more than it looks.** It isn't a file listing — it's a _summary layer_. Each entry says what the file covers, in enough detail that the agent can answer many questions **without opening the file at all**, and knows exactly which file to open when it can't. It's a hand-maintained cache of "what do I know about this course." That's the whole trick.

> **Real example** — the Lecture 1 entry in [`CPE342-machine-learning/INDEX.md`](CPE342-machine-learning/INDEX.md) breaks 83 slides into three sections with every topic named: statistical learning, Bayes' classifier, LDA/QDA, ROC/AUC. An agent asked "where do I learn about the Bayes decision boundary?" answers correctly having read ~40 lines.

---

## The Two Laws

Two rules do most of the heavy lifting. Both are enforced by [`CLAUDE.md`](CLAUDE.md) and applied automatically by [`/update-index`](.claude/commands/update-index.md).

### 📜 Law I — The Reading Rule (never read a PDF twice)

PDFs load as **images**. Reading one is expensive and lossy. So every PDF gets a permanent Markdown twin, generated once:

1. **Is there a `<name>.md` next to `<name>.pdf`, at least as new?** → read that. Done. Free.
2. **No?** Generate it, cheapest method first:
   - `pdftotext -layout -enc UTF-8` — free, no model. Correct choice for prose (syllabi).
   - **Formula-heavy, figure-heavy, or scanned?** `pdftotext` mangles the math and drops the figures. Dispatch a **Sonnet subagent** that reads the pages and writes a faithful transcript: every equation as LaTeX (`$…$` / `$$…$$`), every figure as one italic line. The expensive page reads happen _inside the subagent_ and never touch the main thread's context.
3. **Record it in `INDEX.md`** on the source file's entry as `*(text cache: [[<name>]])*`.

The cache is a **proxy, not a replacement** — if a task genuinely needs the visuals, read the PDF page directly.

> A `lecture/name.md` (machine transcript) and a `note/lecture1.md` (my own study note) are different artifacts and can both exist for the same deck. One is a photocopy, one is understanding.

### 🔗 Law II — The Linking Rule (build a graph, not a pile)

This is an [Obsidian](https://obsidian.md) vault, so every reference to a real file is a `[[wiki-link]]` — never dead text in backticks. Links survive renames, show up in backlinks, and turn the vault into a navigable graph instead of a folder of orphans.

| Target                       | Written as                                                                                   |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| A note or text cache (`.md`) | `[[Lecture1_IntroductionToOS]]` _(no extension)_                                             |
| A PDF / PPTX / anything else | `[[Syllabus_CPE333.pdf]]` _(extension **required**)_                                         |
| A PDF **and** its cache      | `[[Name.pdf]]` = source · `[[Name]]` = cache                                                 |
| A heading inside a note      | `[[lecture1#Exam focus]]` _(literal heading text, not a slug)_                               |
| A repeated basename          | `[[CPE342-machine-learning/INDEX\|INDEX.md]]` _(path-qualify or it silently resolves wrong)_ |

**Not links:** folders, anything in `.claude/` or `.obsidian/`, paths outside the vault, and `<placeholder>` patterns. Those stay inline code.

> **This README is the one deliberate exception.** It uses relative Markdown links, because GitHub renders `[[…]]` as literal dead text. Relative links work in both GitHub _and_ Obsidian.

---

## Commands & Skills

|     | Name                         | Scope                                                                                    | What it does                                                                                                                                                                                                                                         |
| --- | ---------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **`/update-index [folder]`** | 📦 in this repo — [`.claude/commands/update-index.md`](.claude/commands/update-index.md) | The ingest pipeline. Lists the folder, converts every un-cached PDF to Markdown (Law I), diffs disk against `INDEX.md`, rewrites both docs to match reality, verifies every wiki-link resolves, and updates the class table. Skips `temp/` entirely. |
| 🕸️  | **`/graphify`**              | 🌐 global — `~/.claude/skills/graphify/`                                                 | Turns any input into a persistent knowledge graph with god nodes, community detection, and query/path/explain tools. Configured on my machine, **not shipped in this repo** — clone this and you won't have it.                                      |

### Starting a new class

```bash
cp -r format-template/ CPE999-example-class/
```

Fill in the two files, then run `/update-index CPE999-example-class` and let the agent sync the root class table for you.

---

## Class Roster — Semester 1 / 2026

| Code       | Course               | Folder                                                       | Status         |
| ---------- | -------------------- | ------------------------------------------------------------ | -------------- |
| **CPE333** | Operating Systems    | [`CPE333-operating-systems`](CPE333-operating-systems)       | 🟢 active      |
| **CPE334** | Software Engineering | [`CPE334-software-engineering`](CPE334-software-engineering) | 🟢 active      |
| **CPE342** | Machine Learning     | [`CPE342-machine-learning`](CPE342-machine-learning)         | 🟢 active      |
| GEN101     | Physical Education   | `GEN101-physical-education`                                  | ⚪ not created |
| GEN241     | Beauty of Life       | `GEN241-beauty-of-life`                                      | ⚪ not created |
| PRE380     | Engineering Economy  | `PRE380-engineering-economy`                                 | ⚪ not created |

_Ingest coverage: **9 / 9** source PDFs have a current Markdown cache._

---

## Design Principles

**1. Plain text or it didn't happen.** Everything is Markdown. Readable by me, by Obsidian, by GitHub, by any model, by `grep`, and by whatever tool replaces all of them in two years. No database, no lock-in, no proprietary format that dies when a startup does.

**2. The map is the product.** `INDEX.md` and `CLAUDE.md` are not documentation _about_ the system — they _are_ the system. The folders are just storage.

**3. Documentation drifts, so make fixing it a command.** I dump files without updating anything. That's a fact about me, not a bug to nag about. So drift-correction is automated and one keystroke away instead of relying on discipline I demonstrably don't have.

**4. Push expensive work down.** Heavy page-by-page reads happen in a throwaway subagent whose context dies with it. The main thread stays clean and cheap.

**5. Every class is identical.** Uniform structure is what makes a new course zero-cost to onboard — for me _and_ for the agent.

**6. Teach, don't just answer.** Encoded directly into the instruction files: the agent is told to explain the _why_, to push back when I'm wrong, and — for graded work — to help me learn rather than hand me something to submit. Academic integrity is a config value here, not a vibe.

## Non-Goals

- ❌ **Not a cheating machine.** Class policies (deadlines, posted-solution rules, academic integrity) are written into each class's `CLAUDE.md`, and the agent is instructed to walk me through gradable work instead of doing it. That constraint is deliberate and load-bearing.
- ❌ **Not a general note-taking app.** It's an agent context substrate that happens to be readable by humans.
- ❌ **Not portable to your semester without edits.** Fork it, gut the class folders, keep the two Laws. That's the transferable part.

---

## FAQ

<details>
<summary><b>Is this over-engineered for university homework?</b></summary>
<br>

Yes.

</details>

<details>
<summary><b>How long did building this take versus just doing the homework?</b></summary>
<br>

Next question.

</details>

<details>
<summary><b>Why not just paste the PDF into the chat every time?</b></summary>
<br>

That is the exact cost this repo exists to eliminate. Pasting is `O(n)` in questions asked. This is `O(1)` — you pay once at ingest and the marginal cost of question #200 is reading a 40-line map. Also, pasting loses every equation, and you'd have to re-explain the grading policy each time. I did the math. Then I built a repo so an agent could check my math.

</details>

<details>
<summary><b>What happens if I just... don't update the index?</b></summary>
<br>

The system degrades exactly as gracefully as any other cache: files still exist and are still readable, the agent just doesn't know they're there until it looks. Then you run `/update-index` and it self-heals. Correctness is never at risk — only cost.

</details>

<details>
<summary><b>Why is there a `temp/` folder that's banned from all documentation?</b></summary>
<br>

Because a system that demands every scratch file be catalogued is a system I will abandon in nine days. `temp/` is the pressure-release valve: a designated place for garbage, explicitly excluded from `INDEX.md`, `CLAUDE.md`, and every agent listing. Half-baked ideas need somewhere to live where they can't pollute the graph.

</details>

<details>
<summary><b>Can I use this for my own semester?</b></summary>
<br>

Fork it, delete my classes, copy `format-template/` per course. The two Laws and the three-layer protocol are the actual portable IP. Note that `/graphify` lives in my global config and won't come with the clone.

</details>

<details>
<summary><b>Does this make you smarter?</b></summary>
<br>

It makes my _questions_ cheaper, which means I ask more of them, which is probably the same thing if you don't look too closely.

</details>

---

## Roadmap

- [x] Three-layer context protocol (root → class → index → file)
- [x] Reading Rule — automatic PDF → Markdown caching, with subagent fallback for math
- [x] Linking Rule — full wiki-link graph with dangling-link validation
- [x] `format-template/` for zero-friction class creation
- [x] `/update-index` — one-command drift correction
- [ ] Better PDF conversion — library-assisted rather than everything on the subagent _(tracked in [`PROBLEM.md`](PROBLEM.md))_
- [ ] Remaining three classes (GEN101, GEN241, PRE380)
- [ ] Assignment-tracking layer — deadlines and status surfaced without opening each brief
- [ ] Custom skills, once I've used this long enough to know which pain points are real

---

<div align="center">

**Built by a third-year Computer Engineering student at KMUTT**<br/>
who decided that explaining the same syllabus to an AI four hundred times<br/>
was a worse use of a semester than building this.

<sub><b>Hard compute once. Cheap forever.</b></sub>

</div>
