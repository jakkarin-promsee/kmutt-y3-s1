# INDEX — CPE334 Introduction to Software Engineering in the Age of AI Agents

Annotated map of this class folder, so an agent (and I) can understand the whole folder **without
opening every file**. Keep it current: update a section whenever files are added, renamed, or
removed. **Do not list `temp/`** — it's volatile.

> Format per entry: `[[file]]` — what it is / what it covers (+ due date or status if relevant).
> Links are Obsidian wiki-links (full syntax and edge cases: the `vault-writing` skill):
> `[[Name.pdf]]` is the source file, `[[Name]]` is its Markdown text cache.

## assignment/

### Lab-1/

- [[Lab1_Labsheet.pdf]] — **Lab 1 lab sheet** "TokTickIT Full-Stack Hello World
  Starter", Sprint 1, score /40. Covers the product overview (3-role IT service desk), full ticket
  model (parent + 5 child entities), 4 required GitHub Issues (`feature/1-project-foundation`,
  `feature/2-health-check`, `feature/3-category-seed`, `feature/4-category-list`), acceptance
  criteria + tests for each, Kanban workflow, and the grading rubric. Lab goal: a working vertical
  slice (React/Vite → Express → Prisma → PostgreSQL) showing system status and seeded categories.
  *(text cache: [[Lab1_Labsheet]])*
- [[Lab1_Glossary.pdf]] — **Lab 1 glossary** "Appendix — Glossary of Key Terms".
  Quick-reference table of ~25 terms across product/process (vertical slice, engineering contract,
  acceptance criteria, DoD), web stack (REST, endpoint, CORS, TypeScript, Vite), database
  (PostgreSQL, Prisma, model, migration, seed), testing (Vitest, Supertest, mock, TDD), and
  Git/GitHub (Git flow, feature branch, staging branch, PR, peer review, Issue).
  *(text cache: [[Lab1_Glossary]])*
- [[Lab1_Git_GitHub_CheatSheet.pdf]] — **Lab 1 cheat sheet** for Git & GitHub.
  One-time setup, Lab 1 branch model (`feature/* → lab1-staging → main`), step-by-step
  feature-branch workflow, opening and reviewing PRs, release PR to `main`, merge-conflict
  resolution, and common gotchas (HTTPS tokens, why PRs beat direct pushes).
  *(text cache: [[Lab1_Git_GitHub_CheatSheet]])*
- [[Lab1_Guidance]] — **คู่มือเดินงาน Lab 1 ทีละก้าว** ของกูเอง แปลง labsheet เป็น 10 Phase
  เรียงลำดับทำจริง: เตรียมเครื่อง/หาคู่รีวิว → repo + branch + collaborator → บอร์ด + Issue →
  Issue #1–#4 ทีละอัน (คำสั่งติดตั้ง โค้ด Express/Prisma/React เทสต์ Supertest+Vitest พร้อม
  คำอธิบายว่าทำไมเขียนแบบนั้น) → เอกสาร 4 ไฟล์ → release เข้า `main` → เก็บหลักฐาน + ประกอบ PDF
  ส่ง · มี "หลักฐานที่ต้องเก็บ" ท้ายทุก Phase, Definition of Done ต่อ Issue, และตารางกับดัก
- [[Lab1_Issue_Drafts]] — **ร่างเนื้อ GitHub Issue ทั้ง 4 อัน** ของกูเอง พร้อมก๊อปวางตอนกด New
  issue: title + body (Type, branch, target, dependency, acceptance criteria แบบ checkbox ลอกจาก
  labsheet §7 คำต่อคำ) + label ที่ควรสร้าง + แผนภาพลำดับ dependency ของ Issue 1–4

## lecture/

- [[CPE334_Syllabus_1-2026.pdf]] — course syllabus, 1/2026. Instructors & TAs, meeting times,
  grading split (Midterm 20 / Final 20 / Labs 35 / Project 25), CLO1–CLO3, and the full 14-week
  schedule with each week's lab.
  *(text cache: [[CPE334_Syllabus_1-2026]] — regenerated 2026-08-04 by a Sonnet subagent reading
  all 4 pages; the instructor/TA list, grading split and the 14-week schedule are proper Markdown
  tables, so the old column-shift caveat no longer applies.)*
- [[Lecture+1+-+Introduction.pdf]] — **Lecture 1, "Software Engineering in the Age of AI Coding
  Agents"** (Week 1, 3–7 Aug). 46 slides. Storyline: AI coding agents → code vs software product →
  SDLC → process models (waterfall/iterative/agile) → responsible AI use → Lab 1 prep. Second half
  is the practical toolkit: React/Vite/Bootstrap + Express + Prisma + PostgreSQL, vertical slice,
  Spec-DD & TDD, and an extended Git/GitHub workflow section (branches, PRs, Issues/Kanban, repo
  setup, merge conflicts, `feature → lab1-staging → main` release path).
  *(text cache: [[Lecture+1+-+Introduction]] — regenerated 2026-08-04 by a Sonnet subagent reading
  all 46 slides; one `## Slide N` heading per slide, slide text and shell/Git snippets verbatim,
  and 29 diagrams captured as one-line descriptions (SDLC phases, process models, branching model,
  merge types). Descriptions, not pictures — read the PDF if a diagram's exact shape matters.)*
- [[Lecture+2+-+Requirement+Engineering.pdf]] — **Lecture 2, "Requirement Engineering"** (Week 2,
  10–14 Aug 2026). 43 slides, continuing straight from Lecture 1. First half is the theory: why
  requirements matter (software's intangibility, project-failure stats, the cost-of-defects curve) →
  stakeholders and what a requirement *is* → user vs. system vs. business requirements → functional
  vs. non-functional vs. domain, with an NFR taxonomy → the quality checklist. Then the **four-phase
  RE process** — Elicitation & Analysis, Specification, Validation, Change Management — each worked
  against the course's running TokTickIT / campus-ticketing example. Closes the theory with
  MVP-style feature scoping, a **traceability matrix** sized for Lab 1, and RE in the AI-agent era
  (weak vs. strong prompts).
  **Slides 34–43 are explicit Lab 1 prep** — project structure, full-stack architecture,
  React/TS/Vite/Bootstrap, Node/Express/TS, REST fundamentals and Express routes,
  PostgreSQL/Prisma schema & seed, React data-fetching states, and Vitest/Supertest patterns. Same
  `/api/health` and `/api/categories` endpoints as [[Lab1_Labsheet.pdf]], so read these slides
  alongside the lab sheet rather than separately.
  *(text cache: [[Lecture+2+-+Requirement+Engineering]] — generated 2026-08-15 by a Sonnet subagent
  reading all 43 slides; one `## Slide N` heading per slide, slide text and code snippets verbatim,
  and 20 diagrams captured as one-line descriptions (cost-of-defects chart, NFR taxonomy tree, RE
  process flow, traceability chain, full-stack architecture, Prisma pipeline). Descriptions, not
  pictures — read the PDF if a diagram's exact shape matters.)*

## note/

- [[Git_GitHub_Workflow_Playbook]] — **คู่มือ Git/GitHub ของกูเอง** เขียนตอนเตรียม Lab 1 แต่ครอบคลุม
  workflow ทั้งคอร์ส: โมเดลความคิด (git vs GitHub, 4 ที่ที่ไฟล์อยู่, branch คืออะไรจริง ๆ), setup
  ครั้งเดียวจบ, สร้าง repo + collaborator + Project board + Issues, ลูปหลักต่อ 1 Issue (terminal
  สลับกับเว็บทีละขั้น), peer review ทั้งสองทาง, release เข้า `main`, เช็คลิสต์หลักฐานส่ง Part 1,
  ตารางแก้ปัญหาที่เจอบ่อย, merge conflict, และโปรเจกต์จริงในบริษัทต่างจากแล็บตรงไหน
