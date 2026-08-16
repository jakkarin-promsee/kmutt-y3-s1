# INDEX — PRE380 Engineering Economy

Annotated map of this class folder, so an agent (and I) can understand it **without opening every
file**. Update when files are added/renamed/removed. `temp/` is not listed (volatile).

> Filenames use `+` for spaces (downloaded as-is from LEB2). Readable titles are given below.
> Links are Obsidian wiki-links (full syntax and edge cases: the `vault-writing` skill):
> `[[Name.pdf]]` is the source file, `[[Name]]` is its Markdown text cache.

## assignment/

- **[[Assignment-1.jpg]]** — *Assessments #1: data storage — build vs. rent* (one slide, exported as
  an image). A company wants to expand internal data storage and must choose between **building its
  own server** or **renting from another company**. Given for the build option: purchase
  **7,800,000 ฿**, server room **700,000 ฿**, useful life **10 years**, operating costs **550,000 ฿/yr
  increasing by 35,000 ฿/yr** (an arithmetic gradient), system update **150,000 ฿ first in year 4 and
  every 4 years after**, salvage **10% of purchase price** at end of useful life or **25%** if sold
  early. Project term **15 years**, **MARR 18%/yr**. Required: **show the present worth at t = 0**.
  *(Text transcription: [[Assignment-1]] — the slide is an image, so this is the readable version.
  Verified against the image; it is faithful.)*
  > ⚠️ **The brief is missing Option 2.** It promises the costs of *"both options"* and then lists
  > only Option 1. Nothing about rental rates, term, or escalation appears anywhere on the slide —
  > this is a gap in the handout itself, not in the transcription. Either the rent figures came
  > verbally in class or they're on one of the Chapter 2 slides we don't have (see below). **Ask
  > before attempting a comparison** — as it stands the only answerable question is the build-option
  > present worth, which is exactly what "Required" asks for.
  > **Slide number 2-36 places this in the Chapter 2 deck, which only goes to 2-26 in `lecture/`.**
  > At least ten slides are missing from the folder, probably including the rental data.
  >
  > Solving it needs, from [[Chapter+2+-+Engineering+Economy+Factors.pdf]]: `P/A` and `P/G` for the
  > operating costs, `P/F` for each update and the salvage, and — because the **15-year project
  > outlives the 10-year server** — a decision about what happens in years 10–15 (replacement, or
  > the 25%-early-sale clause). Interest table page for 18%: **p23**.

## lecture/

- **[[Chapter+0+-+Introduction.pdf]]** — *Course overview* (12 slides). **This is the syllabus**,
  despite the name — instructor and contact details, office hours, the 16-week learning plan, the
  learning style (in-class assessment → discuss → self-study video), learning outcomes 1–4, the
  grading policy, the score-distribution curve, the semester calendar with quiz and exam dates, and
  QR codes for the Line group and video playlist. Source of truth for course facts — see
  [[PRE380-engineering-economy/CLAUDE|CLAUDE.md]].
  *(Text cache: [[Chapter+0+-+Introduction]] — full transcription by a Sonnet subagent reading the
  page images, one section per slide. **Read it instead of the PDF**: the slide-10 calendar is
  rebuilt as a correct week-by-week table — `pdftotext` shuffled its columns so weeks no longer
  matched their topics — and the slide-9 histogram is captured with its cutoffs
  **F < 30 · C+ ≥ 55 · A ≥ 73** and the full Group/Mean/StDev/N legend. Only the QR codes on slides
  11–12 can't be carried over; their captions are, so open those two pages in Obsidian to scan them.
  Printed typos kept `[sic]`: "IMPORTENT DATE", "Leaning outcome".)*

- **[[Chapter+1+-+Foundations+of+Engineering+Economy.pdf]]** — *Chapter 1: Foundations of
  Engineering Economy* (27 slides). **Week 1.** The vocabulary chapter — no factor notation yet.
  *(Text cache: [[Chapter+1+-+Foundations+of+Engineering+Economy]] — full transcription by a Sonnet
  subagent reading the page images, one section per slide, with the diagrams rendered as ASCII
  timelines. **Read it instead of the PDF.**)*
  - Why engineering economy matters; the 7 general steps of decision making; steps in an engineering
    economy study.
  - **Time value of money (TVM)** — the course's central idea; interest `I` and interest rate `i`;
    rate of return; borrower's vs. lender's perspective.
  - **Symbols** `t, P, F, A, n, i` — these carry through every later chapter.
  - **Cash flows** — inflows (revenues, `+`) vs. outflows (disbursements, `−`);
    `NCF = R − D`; the **end-of-period assumption**; point vs. range estimates; **cash-flow
    diagrams** (arrows up for in, down for out, drawn roughly to scale).
  - **Economic equivalence** — different amounts at different times can be equal in value at a rate.
  - **Simple vs. compound interest** — `I = Pni` vs. interest on principal + accrued interest;
    worked side by side on $100,000 over 3 years at 10% ($130,000 vs. $133,100).
  - **MARR** — hurdle/benchmark rate; equity vs. debt financing; `ROR ≥ MARR > WACC`; opportunity
    cost as the ROR of the best project you didn't fund.
  - **Excel functions**: `PV`, `FV`, `PMT`, `NPER`, `RATE`, `IRR`, `NPV`.
  > Two formulas are drawn as images on the slides, so they were blank in the old `pdftotext` cache
  > and are now **recovered** in the current one: the interest-rate definition (1-9)
  > $i\,(\%) = \dfrac{\text{interest accrued per time unit}}{\text{principal}} \times 100\%$, and the
  > compound-interest expression for period `t` (1-20), which the slide states as a summation —
  > $I_t = \left(P + \sum_{j=1}^{t-1} I_j\right)i$, i.e. the rate applied to principal *plus every
  > period's interest so far*.
  > Two figures the transcription flags as not fully legible: the arrow placement on slide 1-15 and
  > the hand-plotted bar heights on 1-16. Open those pages if exact positions matter.
  > The title slide's footer says `1-1`; from slide 2 on it numbers correctly.

- **[[Chapter+2+-+Factors,+Effect+of+Time+&+Interest+on+Money.pdf]]** — *Chapter 2: Factors, Effect
  of Time & Interest on Money* (26 slides). **Week 2.** Where the course gets computational:
  every factor, each with a worked multiple-choice example.
  *(Text cache: [[Chapter+2+-+Factors,+Effect+of+Time+&+Interest+on+Money]] — Sonnet-subagent
  transcription of the page images, **merged with the PDF's hidden text layer**. Cash-flow diagrams
  are rendered as ASCII timelines.)*
  > 🔑 **Read the cache, not the PDF — the PDF hides the answers.** Eight worked example slides
  > (2-8, 2-9, 2-13, 2-14, 2-20, 2-22, 2-24, 2-25) render as *question + multiple-choice options
  > only*. Their solution boxes and cash-flow diagrams are PowerPoint animation reveal-states: real
  > text objects present in the file, but invisible when the page is displayed or rasterized. Open
  > 2-13 in Obsidian and you see four options and blank space; `pdftotext` pulls the whole worked
  > solution off that same page. **The cache is the only place both halves exist together.**
  > Consequence for the diagrams: on 2-13, 2-14, 2-20 and 2-22 the transcription reconstructs them
  > from surviving coordinate-anchored number labels plus the general patterns established on
  > 2-11/2-12/2-18/2-21, and says so inline. Treat those four as *faithful in structure, inferred in
  > layout*. On 2-8 and 2-9 no position data survived, so the cache declines to draw one rather than
  > inventing it.
  - **Single payment** `F/P`, `P/F` (2-4 – 2-10): `F = P(1+i)^n`, `P = F/(1+i)^n`; standard factor
    notation `(F/P, i, n)`; `FV`/`PV` with the double comma; worked $5,000 @ 8% for 10 yr → $10,794.50.
  - **Uniform series** `P/A`, `A/P`, `F/A`, `A/F` (2-11 – 2-14). **P is one period ahead of the
    first A; F falls in the same period as the last A** — the deck flags both explicitly.
  - **Untabulated i or n** (2-15 – 2-16): formula, spreadsheet, or interpolation. Interpolating
    `(F/P, 8.3%, 10)` gives 2.2215 vs. the true 2.2197 — **interpolation reads high**.
  - **Arithmetic gradient** (2-17 – 2-20): `P_G = G(P/G, i, n)`, `A = base ± G(A/G, i, n)`. **G
    starts between periods 1 and 2**, so `P_G` sits two periods ahead of the first change; a
    gradient cash flow always splits into **base amount + gradient**.
  - **Geometric gradient** (2-21 – 2-23): `P_g = A₁{1 − [(1+g)/(1+i)]^n}/(i − g)`, and `P_g = A₁n/(1+i)`
    when `g = i`. **No tables exist for geometric factors** — you must use the formula.
  - **Unknown i or n** (2-24 – 2-25): set up the equation, solve the factor, then read *along* the
    A/P column of the tables to bracket the answer. Trial and error or interpolation.
  - **Summary** (2-26) — the eight placement rules worth memorising for the exam.
  > Deck stops at **2-26**, but [[Assignment-1.jpg]] is slide **2-36** of it. The folder has a
  > partial copy. Slide 2-23 (geometric gradient, $16,000 instrument) and 2-10 (three past deposits)
  > are posed with no worked solution — they're the in-class assessment problems.

- **[[Chapter+2+-+Engineering+Economy+Factors.pdf]]** — *Engineering Economy Factors* (3 pp). The
  **formula sheet** — a textbook reference downloaded from LEB2, not a lecture. Every factor in
  closed form: discrete/discrete (single payment, equal-payment series, uniform and geometric
  gradient, infinite series/perpetuity), discrete/continuous and continuous/continuous compounding
  (`e^{rn}` forms), and conventional loan payment formulas (`R_t`, `I_t`, `B_t`, equity). **The
  reference to reach for whenever `i` or `n` isn't in the tables.**
  *(Text cache: [[Chapter+2+-+Engineering+Economy+Factors]] — transcribed to LaTeX by reading the
  pages. `pdftotext` returns pure mojibake here: the PDF is Ghostscript 5.50 output with
  non-standard font encoding, so the cache is the **only** readable text.)*

- **[[Chapter+2+-+COMPOUND+INTEREST+TABLES.pdf]]** — *Appendix C: Compound Interest Tables* (32 pp,
  textbook pages 594–625). Tabulated values of all eight factors — `F/P`, `P/F`, `A/F`, `A/P`,
  `F/A`, `P/A`, `A/G`, `P/G` — one page per interest rate, plus the `n → ∞` values on p1 and
  continuous-compounding single-payment factors on p32. **The lookup table for hand calculation.**
  > 🚫 **No Markdown cache, deliberately.** `pdftotext -layout` misaligns the numeric columns —
  > values land under the wrong `n` — and a silently wrong factor value is worse than no cache.
  > **Read the specific PDF page instead**, or pull one page as text with
  > `pdftotext -f <page> -l <page> -layout` and check the alignment before trusting it.
  > The decision is recorded in this folder's `.pdfignore`, so `check-pdf-cache.py` answers
  > `IGNORED` for it instead of reporting a missing cache every time.

  **Page map** (PDF page → interest rate):

  | Page | Rate | Page | Rate | Page | Rate | Page | Rate |
  | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | 1 | `n = ∞` values | 9 | 2% | 17 | 7% | 25 | 25% |
  | 2 | ¼% | 10 | 2½% | 18 | 8% | 26 | 30% |
  | 3 | ½% | 11 | 3% | 19 | 9% | 27 | 35% |
  | 4 | ¾% | 12 | 3½% | 20 | 10% | 28 | 40% |
  | 5 | 1% | 13 | 4% | 21 | 12% | 29 | 45% |
  | 6 | 1¼% | 14 | 4½% | 22 | 15% | 30 | 50% |
  | 7 | 1½% | 15 | 5% | 23 | **18%** | 31 | 60% |
  | 8 | 1¾% | 16 | 6% | 24 | 20% | 32 | continuous |

  Note the gaps: **no 11%, 13%, 14%, 16%, 17%, or 19%** — those need the formula sheet.

## note/

- **[[PRE380-engineering-economy/note/lecture-1|lecture-1.md]]** — *เอกสารติว Chapter 1
  (ภาษาไทย)*. Study guide built from
  [[Chapter+1+-+Foundations+of+Engineering+Economy|the Chapter 1 cache]], covering all 27 slides
  from zero with worked numbers. 17 sections: pre-requisites → EE definition → the two 7-step lists
  → TVM → interest/ROR → symbols → cash flow → diagrams → equivalence → simple vs. compound → MARR
  and WACC → opportunity cost → ethics → Excel functions → cheat sheet → errata and traps →
  12 practice problems with full solutions → pre-exam checklist.
  Headings are tagged **(จาก slide 1-N)** where the content is on a slide and **(เสริม)** where it
  is added context, so exam-relevant material is separable from background.
  > Records three things the deck itself doesn't: outcome #3 **"Ethics and economics"** is declared
  > on slide 1-2 but **has no content slide anywhere in the deck** (nor in the 1-27 summary), so the
  > note supplies that section; slide 1-26's `NPER` entry has **an extra opening parenthesis**; and
  > `PMT(5%,5,5000)` actually returns **−1154.87** in Excel, not the `$1154.87` the slide prints —
  > a sign-convention point the slide leaves out. All arithmetic in the note was machine-verified.

- **[[PRE380-engineering-economy/note/lecture-2|lecture-2.md]]** — *เอกสารติว Chapter 2
  (ภาษาไทย)*. Study guide built from
  [[Chapter+2+-+Factors,+Effect+of+Time+&+Interest+on+Money|the Chapter 2 cache]], covering all 26
  slides from zero. 22 sections: pre-requisites → chapter map → symbols → factor notation → single
  payment `F/P`,`P/F` → reading the interest tables → spreadsheets → uniform series `P/A`,`A/P` →
  `F/A`,`A/F` → **placement rules** → untabulated `i`/`n` → arithmetic gradient → worked gradient
  example → geometric gradient → unknown `i` → unknown `n` → factor relationships → the slide-2-26
  summary → cheat sheet → 18 traps → 15 practice problems with full solutions → pre-exam checklist.
  Same labelling scheme as [[PRE380-engineering-economy/note/lecture-1|lecture-1.md]]: headings
  tagged **(จาก slide 2-N)** where the content is on a slide, **(เสริม)** where it is added context.
  > Derives every factor rather than asserting it, so the placement rules fall out of the algebra:
  > `P/A` is built by summing `P/F` term by term (which is *why* P lands one period early), and
  > `F/A` by summing `F/P` (the last A carries $(1+i)^0$, which is *why* F is coincident).
  > Both in-class assessment problems the deck poses without answers — **2-10** (Mr. Sompong's three
  > past deposits, \$47,087.50) and **2-23** (the \$16,000 instrument, PW \$22,974.26) — are worked
  > in full; 2-23 is the chapter's hardest, combining a `g > i` geometric gradient with a salvage
  > sign flip.
  > Records four things the deck doesn't: **(1)** slide 2-24's "i is between 22% and 24%" **cannot
  > be done with this course's tables** — [[Chapter+2+-+COMPOUND+INTEREST+TABLES.pdf]] jumps 20% →
  > 25%, so the note redoes the bracket with the pages that exist. **(2)** the formula sheet
  > [[Chapter+2+-+Engineering+Economy+Factors]] has **no finite-`n` `P/G`** (only `A/G` and the
  > `n → ∞` form), so `(P/G) = (A/G)(P/A)` is given as the workaround. **(3)** slide 2-5's `P/A`
  > column header reads *"Find A Given A"* where *"Find P Given A"* is meant. **(4)** interpolation
  > reads high **because the factor curves are convex**, demonstrated across four factors — the
  > deck states the symptom without the cause. All arithmetic machine-verified.
