# CPE334 — Introduction to Software Engineering in the Age of AI Agents

Per-class instructions for Claude. Read this file (then
[[CPE334-software-engineering/INDEX|INDEX.md]]) before working on anything in this class. For
vault-wide rules, see the root [CLAUDE.md](../CLAUDE.md).

## Course info

- **Code:** CPE334
- **Name:** Introduction to Software Engineering in the Age of AI Agents
- **Instructors:** Dr. Suthep Madarasmi (Jogie) · Dr. Piyanit Ua-areemitr (Toey) ·
  Dr. Santawat Thanyadit (Job). Office hour: by appointment.
- **Semester:** 1/2026
- **Credits / schedule:** 3 (3-0-6). Lecture & Lab —
  Sections 1, 2, HDS: **Tue 13:30–17:20** · Sections 31, 32: **Thu 08:30–12:20**.
  _(Which section I'm in: unknown — fill this in.)_
- **Grading:** Midterm 20% / Final 20% / Labs & Assignments 35% / Group Project 25%
- **Course site:** https://leb2.kmutt.ac.th (materials distributed here, plus the Facebook group
  "CPE334 Software Engineering in the Age of AI Agents"). Textbook: TBA.

## Class-specific notes

**The course's premise:** AI coding agents are allowed and encouraged, but they don't replace
engineering discipline. The agent is framed as "a fast but accountable junior developer." I remain
accountable for everything submitted and **must document my AI usage** (there's an AI Usage Report
in Week 13). Keep that in mind when helping me — the graded artifact is usually the *process*
(spec, tests, PR, review), not just working code.

**Course shape:**

- **First half — individual.** Four labs building my own Service Desk / Issue Tracker web app
  ("TokTickIT"), from an empty Git repo to a tested, running app.
- **Second half — team.** One substantial project from an approved list, using Agile, code reviews,
  CI/CD, cloud deployment (GCP), testing, documentation, final delivery.

**Tech stack (from Lab 1):** React + Vite + Bootstrap → Express → Prisma ORM → PostgreSQL.
Tests with Vitest + Supertest. UI theme for Lab 2 is "Zen Green."

**Git workflow the course enforces** — this is graded, so follow it exactly:

- Branches: `feature/<issue#>-<slug>` → `lab<N>-staging` → `main`. Feature branches **never** merge
  directly to `main`.
- One Issue per feature branch; link it in the PR (`Closes #1`); paste acceptance criteria; request
  peer review before merging.
- Never commit `.env`, credentials/API keys, `node_modules/`, build output, or large temp files.
- Commit messages state engineering purpose, not "update files."
- **Definition of Done** = reviewed + accepted, satisfies acceptance criteria, merged, evidence
  documented. *Not* "the AI agent said it works."

**Required documents per feature:** Spec DD (specification-driven design doc) and Test DD. The
course teaches spec-first → derive tests → review tests → implement → verify.
