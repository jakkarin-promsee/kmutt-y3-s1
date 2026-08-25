# INDEX — CPE333 Operating Systems

Annotated map of this class folder, so an agent (and I) can understand it **without opening every
file**. Update when files are added/renamed/removed. `temp/` is not listed (volatile), and
`workspace/` lists sources only — never the compiled binaries beside them.

> Format per entry: `[[file]]` — what it is / what it covers (+ due date or status if relevant).
> Links are Obsidian wiki-links (full syntax and edge cases: the `vault-writing` skill):
> `[[Name.pdf]]` is the source file, `[[Name]]` is its Markdown text cache.

## assignment/

- [[PS2_2026.pdf]] — **Problem Session 2: Process Creation & Pipes** — group work (up to 3–4
  students), Linux/Unix environment required. Five tasks: (1) the `fork()` hello-world from
  [[Lecture2_ProcessAndProcessAPIs.pptx]] plus a `wait()` variant, (2) `sleep()` + `ps -ef` to
  observe orphan vs. zombie (`<defunct>`) processes, (3) fork until failure to find the process
  limit, (4) `pipe()` + `fork()` child→parent message passing, (5) three pipe edge cases (read own
  message, read before write, several writes before a read). Deliverable is a **PDF report** to LEB2
  — source code + explanation, results, discussion. No C files submitted.
  *(text cache: [[PS2_2026]])*

## lecture/

- [[Syllabus_CPE333.pdf]] — course syllabus: instructor + TA contacts, schedule (Tue 13:30–16:20,
  LIB108), grading split, textbooks, and the full 14-week topic table with module A/B/C mapping.
  *(text cache: [[Syllabus_CPE333]])*
- [[Lecture1_IntroductionToOS.pptx]] — **Week 1**: Introduction to Operating Systems (15 slides).
  Course opener, no problem session. Covers: what an OS is (resource manager / virtual machine);
  the three parts — virtualization (CPU + memory), concurrency, persistence; the three mini-projects;
  OS design goals (abstraction, performance, isolation, reliability, energy, security, mobility);
  and a history run — mainframe libraries → user/kernel mode + system calls → multiprogramming on
  minicomputers → UNIX & C → DOS/Mac OS/Windows NT/Mac OS X.
  *(reading copy: [[Lecture1_IntroductionToOS.pdf]] — my own PowerPoint→PDF export, because Obsidian
  can't render `.pptx`. Text cache: [[Lecture1_IntroductionToOS]], made from that PDF.)*
- [[Lecture2_ProcessAndProcessAPIs.pptx]] — **Week 2**: Process and Process APIs (45 slides).
  Slides 1–33 are the concept half — the process abstraction `Process = (P, D, C, S)`, address
  space, the ready/running/blocked state machine, process creation and the Process Control Block,
  then Limited Direct Execution: user vs. kernel mode, system calls and the trap table, context
  switching, cooperative vs. timer-interrupt scheduling. Slides 34–45 are the UNIX process API half
  that [[PS2_2026.pdf]] builds on — `fork()`, `wait()`/`waitpid()`, the `exec()` family, `exit()`
  and `kill()`, why the shell needs `fork()` and `exec()` separated, and `pipe()`.
  *(reading copy: [[Lecture2_ProcessAndProcessAPIs.pdf]] — PowerPoint→PDF export. Text cache:
  [[Lecture2_ProcessAndProcessAPIs]], from `pdftotext`; ⚠️ the C code listings on slides 35 and 45
  are **images**, so they are blank in the cache — read those PDF pages directly.)*

## note/

- _none yet_

## workspace/

Where C gets compiled, so build output stays out of `assignment/` — see
[[CPE333-operating-systems/CLAUDE|CPE333 CLAUDE.md]]. Each `.c` here builds to an extension-less
binary of the same name (`q3.c` → `q3`); those are gitignored and not listed below.

**PS2 — [[PS2_2026.pdf]] solutions**, one file per numbered task:

- [[q1.1.c]] / [[q1.2.c]] — Q1: the `fork()` hello-world from slide 35, and the `wait()` variant.
  Run either one 20–30× in a loop: the first has non-deterministic output ordering, the second
  always prints the child first.
- [[q2.1.c]] — Q2.1: parent forks, never calls `wait()`, sleeps 30s → child shows as `<defunct>`
  in `ps`. Reaps it at the very end so the zombie is seen disappearing.
- [[q2.2.c]] — Q2.2: parent exits first → child prints `getppid()` before *and* after, so the
  re-parenting is visible without `ps`. ⚠️ On WSL the new parent is the `/init` relay, **not**
  PID 1, because the relay registers itself as a child subreaper.
- [[q3.c]] — Q3: recursive fork chain (parent waits, child forks) so the process count grows
  linearly instead of 2ⁿ. ⚠️ **Always cap it first:** `ulimit -u 500 && ./q3`.
- [[q4.c]] — Q4: `pipe()` then `fork()`, child sends, parent receives. The first two output lines
  race, so they can print in either order — the brief's sample output is one outcome, not a spec.
- [[q5.1.c]] / [[q5.2.c]] / [[q5.3.c]] — Q5: sender reading its own message (`EBADF` vs. success),
  read-before-write (blocks vs. EOF), and several writes before one read (66 bytes in one `read()`
  → a pipe is a byte stream, not a message queue). Each runs two labelled experiments.
- [[build-gcc.py]] — compiles every `q*.c` through WSL with `-Wall`. Compile-only by default;
  `--run` also executes the ones that terminate on their own (never `q2.*` or `q3`).
- [[build-gcc-log.py]] — scratch, prints the commands without running them.
