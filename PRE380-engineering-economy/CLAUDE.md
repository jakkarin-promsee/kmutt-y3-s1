# PRE380 — Engineering Economy

Per-class instructions for Claude. Read this (then [[PRE380-engineering-economy/INDEX|INDEX.md]])
before working on anything in this class. For vault-wide rules, see the root
[CLAUDE.md](../CLAUDE.md).

## Course info

- **Code:** PRE380
- **Name:** Engineering Economy
- **Instructor:** Dr. Suriyaphong Nilsang ("Chris") — [suriyaphong.nils@mail.kmutt.ac.th](mailto:suriyaphong.nils@mail.kmutt.ac.th)
  / [suriyaphong.nilsang@gmail.com](mailto:suriyaphong.nilsang@gmail.com) · Line ID `suriyaphong.nilsang`
- **Office hours:** 1–4 PM Monday, Tuesday, Friday — or by appointment
- **Semester / Year:** not printed on any handout — see ⚠️ in Class-specific notes
- **Platform (LEB2):** the two reference sheets (factor formulas, compound interest tables) are LEB2
  downloads; there is also a **Line open-chat group** and a **video playlist** for self-study
  (links are QR codes on Introduction slides 11–12, so they don't survive text extraction)
- **Textbook:** slides are "modified and based on" **Blank & Tarquin, _Engineering Economy_, 7th ed.
  (2012)**

## Grading

| Component               | Weight                       |
| ----------------------- | ---------------------------- |
| Midterm examination     | 40% (score 80, halved)       |
| Final examination       | 40% (score 80, halved)       |
| Quiz                    | 20% (4 quizzes, 10/2 each)   |
| Assessments (in-class)  | **+5% extra**                |
| Attendance              | no weight printed            |

**Grading is curved, not absolute.** Introduction slide 9 plots the score distribution of four past
cohorts (66_2, 67_1, 67_2, 68_1 — means 63.15 / 60.88 / 47.83 / 58.01) with cutoffs drawn at
**F < 30 · C+ ≥ 55 · A ≥ 73**, and states *grading depends on the GROUPs, all sections*. So the
cutoffs move year to year — treat 30/55/73 as the historical shape, not a promise.

- **Midterm:** chapters 1–9 · **Final:** chapters 10–16
- Both are **onsite, scheduled by the Registration Office, 13:00–16:00**

## Learning plan (16 weeks)

| Week | Topic                                                        |
| ---- | ------------------------------------------------------------ |
| 1    | Introduction / Foundations of Engineering Economy             |
| 2    | Factors, Effect of Time & Interest on Money                   |
| 3    | Combining Factors, Nominal & Effective Interest Rates         |
| 4    | Present Worth Analysis                                        |
| 5    | Annual Worth Analysis                                         |
| 6    | ROR Analysis for a Single Alternative                         |
| 7    | ROR Analysis for Multiple Alternatives                        |
| 8    | **Midterm Examination**                                       |
| 9    | Benefit & Cost Analysis                                       |
| 10   | Making Choices: Project Financing and Noneconomic Attributes  |
| 11   | Replacement and Retention Decisions                           |
| 12   | Breakeven Analysis                                            |
| 13   | Effects of Inflation, Cost Estimation                         |
| 14   | Depreciation Methods                                          |
| 15   | After-Tax Economic Analysis / Decision Making under Risk      |
| 16   | **Final Examination**                                         |

Learning style, per Introduction slide 6: **in-class assessments + namecheck** → **brief and discuss
in class** → **self-learning via video**. The in-class assessments are the extra-credit component,
so they're worth doing even though they can't hurt the grade.

## The two reference sheets — you need both, every problem

This course runs on **standard factor notation** `(X/Y, i, n)`: the letter left of the slash is what
you're solving for, the letter right of it is what you're given. Two LEB2 downloads support it and
they are not interchangeable:

- [[Chapter+2+-+Engineering+Economy+Factors.pdf]] — the **closed-form formulas** for every factor
  (discrete/continuous compounding, gradients, loan payments). Use when `i` or `n` is untabulated.
- [[Chapter+2+-+COMPOUND+INTEREST+TABLES.pdf]] — the **tabulated factor values**, one page per
  interest rate. Use for exam-style hand calculation. Page map is in
  [[PRE380-engineering-economy/INDEX|INDEX.md]] so you can jump straight to a rate.

Three ways to get a factor for an untabulated `i` or `n` (Chapter 2 deck, slide 2-15): the formula,
a spreadsheet function with P/F/A set to 1, or linear interpolation in the tables — **interpolation
is only approximate and reads high** (the deck's worked example is off by 0.0018).

## How to help me in this class

Engineering economy is graded on *method*, not just the final number. So when helping with a problem:

1. **Draw the cash-flow diagram first** (ASCII or a description) — timeline, arrows up for inflows,
   down for outflows, end-of-period assumption. Most errors here are timing errors, not arithmetic.
2. **Write the factor notation before any numbers** — `P = A(P/A, 10%, 5)`, then substitute. This is
   what the lecturer's own solutions do, and it makes a wrong factor obvious.
3. **Quote the factor value to 4 decimals and say where it came from** — table page or formula. If
   you computed it instead of looking it up, say so.
4. Watch the two placement rules that cause most mistakes: in `P/A` and `A/P`, **P is one period
   ahead of the first A**; in `F/A` and `A/F`, **F lands in the same period as the last A**. For an
   arithmetic gradient, **G starts between periods 1 and 2**, so `P_G` sits *two* periods ahead of
   the first change.
5. Per the root "teach me" rule: for anything gradable, walk me through the method and let me write
   the final answer. Full worked solutions are fine for practice problems.

## Class-specific notes

- ⚠️ **Every printed date on these handouts is from last semester.** The Introduction calendar runs
  **January → May**, midterm *Tue 31 March 2026*, final *Fri 22 May 2026*. That calendar is
  internally *correct* — its weekday grid checks out against 2026 (12 Jan 2026 really is a Monday,
  31 Mar a Tuesday, 22 May a Friday), so only the Thai month labels carrying `-25` are wrong. But a
  Jan→May calendar is **semester 2**, i.e. the term that ended before this one; this vault is
  **semester 1, 2026**. The deck is simply last semester's, reused (the grade-curve slide stops at
  cohort 68_1). **Derive real dates from LEB2, never from the slides.** Same reuse pattern as
  [[CPE342-machine-learning/CLAUDE|CPE342]].
- **Quiz cadence is worth planning around**, even though the dates themselves are stale. Last
  semester ran **4 quizzes at weeks 5, 8, 11 and 15** — roughly every 3–4 weeks, each one landing
  the week *after* a chapter block closes, and week 15's falling in a "Break" week. Together they're
  20% of the grade, the same as half an exam.
- ⚠️ **The Chapter 2 deck in `lecture/` is partial.** It ends at slide **2-26**, but
  [[Assignment-1.jpg]] is slide **2-36** of the same deck. At least ten slides — including whatever
  set up Assessment #1 — aren't in the folder. Worth grabbing the full deck from LEB2.
- ⚠️ **Assessment #1 is missing half its data.** The brief says to decide between building *or*
  renting, then only gives the numbers for building. See the note in
  [[PRE380-engineering-economy/INDEX|INDEX.md]].
- 🔑 **These decks hide content behind PowerPoint animation layers — always prefer the cache.** On
  eight of Chapter 2's worked-example slides, the solution box and cash-flow diagram are *present in
  the file as text objects but never rendered*: display the page and you see only the question and
  its multiple-choice options. So the lecturer's own worked method is invisible in the PDF and
  visible only via the text layer. The caches in `lecture/` merge both, which makes them strictly
  more complete than the source — the opposite of the usual cache/original relationship. Two
  practical consequences: **(1)** never conclude "this slide has no solution" from looking at the
  PDF; check the cache or run `pdftotext` on that page. **(2)** when a cache and a page image
  disagree about whether something *exists*, the text layer is the one telling the truth.
- **The interest tables have no Markdown cache, on purpose.** They're 32 pages of numeric columns;
  `pdftotext -layout` misaligns rows, which would silently produce wrong factor values. Read the
  specific PDF page instead — the page map is in [[PRE380-engineering-economy/INDEX|INDEX.md]].
- Filenames are `+`-encoded LEB2 downloads. "Chapter 0" is the **syllabus / course-overview deck**,
  not a content chapter — every course fact above comes from it.
- Currency mixes: the decks are the US textbook's ($), the assignments are Thai (Baht). Keep them
  straight and don't convert.
