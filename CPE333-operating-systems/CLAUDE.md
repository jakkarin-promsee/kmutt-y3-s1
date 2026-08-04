# CPE333 — Operating Systems

Per-class instructions for Claude. Read this file (then [[CPE333-operating-systems/INDEX|INDEX.md]])
before working on anything in this class. For vault-wide rules, see the root
[CLAUDE.md](../CLAUDE.md).

## Course info

- **Code:** CPE333 — (TH) ระบบปฏิบัติการ
- **Name:** Operating Systems
- **Instructor:** Asst.Prof. Rajchawit Sarochawikasit — rajchawit.sar@mail.kmutt.ac.th
  (TA: Omar Yusoh)
- **Semester:** Semester 1, 2026
- **Credits / schedule:** 3 (3-0-6) — Tue 13:30–16:20, LIB108, lecture-based
- **Grading:** Midterm 30% / Final 30% / Mini-project 20% / Lab + Assignment + Quiz 20%
  - Graded **relative to class peers**; a total below ~35% is usually an F.

## Folder layout

Same as every class (see root [CLAUDE.md](../CLAUDE.md)):

- `assignment/` — assignment briefs, my working files, submissions
- `lecture/` — slides / PDFs / readings from the lecturer
- `note/` — my own notes worth keeping
- `temp/` — scratch; volatile, **never documented**
- [[CPE333-operating-systems/INDEX|INDEX.md]] — annotated map of this folder

## Class-specific notes

**Goal of the course:** understand OS concepts well enough to read small, basic **Linux kernel
code**. Expect C, system calls, and real kernel/POSIX APIs — not pseudocode. When writing example
code for this class, default to **C** (POSIX), not Python.

**Textbooks:**

1. *Operating Systems: Three Easy Pieces* — Arpaci-Dusseau (the primary one; free online, OSTEP)
2. *Operating System Concepts*, 8th ed. — Silberschatz, Galvin, Gagne (Wiley, 2008)

**Course arc — three modules, and this is what the exams cover:**

| Module | Part (lecturer's name) | Weeks | Topics | Examined in |
| --- | --- | --- | --- | --- |
| **A** | Part I — **Virtualization** | 2–6 | Processes & process APIs, scheduling, contiguous memory allocation, segmentation & paging, virtual memory | **Midterm** |
| **B** | Part II — **Concurrency** | 8–11 | Threads & thread API, locks, condition variables & semaphores, resource allocation & deadlock | **Final** |
| **C** | Part III — **Persistence** | 12–13 | I/O devices & mass storage, file systems & implementation | **Final** |

Week 1 is the intro (no module). Full week-by-week table lives in
[[Syllabus_CPE333]] — read that cache rather than the PDF.

> The three parts are literally the *three easy pieces* of the OSTEP textbook — virtualization,
> concurrency, persistence. So the course follows OSTEP's structure directly: when I'm stuck on a
> week's topic, point me at the matching OSTEP part rather than the Silberschatz book.

**Mini-project (20%)** runs across the whole semester: proposal presentation in **week 7**, final
defence in **week 14**. ⚠️ The syllabus calls it *one* mini-project, but Lecture 1 (slide 3) lists
**three**: (1) compile and build an OS, (2) study and present key OS components in detail,
(3) modify some kernel modules. **Unresolved — ask the lecturer** whether that's three graded
deliverables or three stages of one project. It changes the workload a lot.

**Problem sessions** are held in weeks 2, 3, 4, 6, 8, 9, 11, 13 — those weeks have in-class problem
work, so notes from them are worth keeping in `note/`.
