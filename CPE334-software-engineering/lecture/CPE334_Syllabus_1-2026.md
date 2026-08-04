# CPE334 Course Syllabus — Introduction to Software Engineering in the Age of AI Agents

> Text cache of [[CPE334_Syllabus_1-2026.pdf]]. Auto-generated transcription — layout and some figure detail are lost. Read the PDF directly if visuals matter.

## Page 1 — Course Syllabus

**Course Syllabus**

| Field | Value |
| --- | --- |
| Course Code | CPE334 |
| Course Name | Introduction to Software Engineering in the Age of AI Agents |
| Course Credit | 3 (3-0-6) |
| Semester/Year | 1/2026 |
| Prerequisite | - |
| Class Meeting | Lecture & Lab |
| | Sections 1, 2, HDS: Tuesdays 13:30 – 17:20 |
| | Sections 31, 32: Thursdays 08:30 – 12:20 |
| Class Website | https://leb2.kmutt.ac.th |
| Course Instructors | Dr. Suthep Madarasmi. (Jogie) — Email: suthep.mad@kmutt.ac.th |
| | Dr. Piyanit Ua-areemitr (Toey) — Email: piyanit.wep@kmutt.ac.th |
| | Dr. Santawat Thanyadit (Job) — Email: santawat.than@kmutt.ac.th |
| Office Hour | By appointment |
| Teaching Assistant | Rachawipa Katippatee (Bom) — Email: rachawipa.kati@gmail.com |
| | Kantapat Suwannahong (Bump) — Email: kantapat.suwan@kmutt.ac.th |
| | Rattanachote Petpansri (Loogmoo) — Email: Rattanachote.petpa@kmutt.ac.th |
| | Prapatsorn Sangrod (Noon) — Email: prapatsorn.sangr@kmutt.ac.th |
| | Supachok Deetaweesukh (Tik) — Email: jedsadaporn.pann@mail.kmutt.ac.th |

-1-

## Page 2 — Course Description, Learning Outcomes, Teaching Method, Evaluation, Reference

**Course Description:**

This course introduces the core principles and practices of software engineering in a development environment where AI agents and LLMs assist with design specifications, coding, testing, debugging, refactoring, documentation, and deployment. The central message is that AI tools do not replace software engineering discipline: students must still understand requirements, design software, write specifications, create tests, manage code changes, review work, secure applications, deploy systems, and improve their process. The AI coding agent is treated as a fast but accountable junior developer that requires clear instructions, tests, review, and human accountability.

The first half builds individual capability through four structured labs, in which each student develops their own Service Desk / Issue Tracker web application as a platform for practicing the full engineering workflow. The second half is team-based: students build one substantial project from an approved list using Agile project management, code reviews, CI/CD, cloud deployment, testing, documentation, and final delivery.

**Learning Outcome:**

After completing this course, the student should be able to

**CLO1 — Build individually.** Build and demonstrate a working full-stack web application on your own, from an empty Git repository to a tested, running app, using an AI coding agent responsibly.
Evaluated by: the individual labs (TokTickIT) — repo, passing tests, and a working demo.

**CLO2 — Work as a team.** Work in an Agile team to plan, build, and deliver a substantial software product using shared Git workflow, code reviews, and sprints.
Evaluated by: the group project — proposal, Kanban board, reviewed PRs, and final delivery.

**CLO3 — Apply engineering practices.** Apply core software-engineering practices — clear requirements, documentation (Spec DD and Test DD) and tests, basic security, automated testing, and simple CI/CD with cloud deployment.
Evaluated by: exams plus lab and project artifacts (spec/test docs, security, CI/CD, deployment).

**Teaching Method:** Lectures, structured hands-on labs, and team-based project-based learning with AI coding agents

**Student Evaluation:**

| Component | Weight |
| --- | --- |
| Midterm Exam | 20% |
| Final Exam | 20% |
| Labs / Assignments | 35% |
| Group Project | 25% |

**Reference:** To be announced. Course materials are distributed via LEB2 (https://leb2.kmutt.ac.th) and the class Facebook group "CPE334 Software Engineering in the Age of AI Agents."

-2-

## Page 3 — Class Policy and Course Schedule (Weeks 1–7)

**Class Policy:**

Students are responsible for all announcements and changes made in class.
Academic integrity and the honesty policy will be strictly enforced.
AI coding agents may be used, but students remain fully accountable for all submitted work and must document their AI usage.

**Course Schedule**

The following topics will be covered in our schedule. The instructor may revise parts of the outline to conform to the background, knowledge, and interests of the students.

| Week | Date | Topics | Activities |
| --- | --- | --- | --- |
| 1 | 4,6 Aug | Course Introduction: Software Engineering in the Age of AI Coding Agents (Dr. Piyanit) | Lab: Lab 1 (Week 1 of 2) — Project Foundation & Vertical Slice: GitHub repo, Git Flow, Issues/Kanban, project scaffold (React/Vite/Bootstrap → Express → Prisma/PostgreSQL) |
| 2 | 11,13 Aug | Requirements Engineering, Proposal Thinking, Traceability, and Feature Scoping (Dr. Piyanit) | Lab: Lab 1 (Week 2 of 2) — API health check, category seed & list, automated tests (Vitest/Supertest), peer-reviewed PR → lab1-staging → main |
| 3 | 18,20 Aug | Specification, Architecture, Tech Stack, Data Modeling, and Lightweight UML (Dr. Suthep) | Lab: Lab 2 (Week 1 of 2) — Ticket Creation: engineering contract, Spec DD, Test DD, DB increment & seed, REST API contract |
| 4 | 25,27 Aug | Test Design, TDD, Verification, Automated Testing, and Definition of Done (Dr. Suthep) | Lab: Lab 2 (Week 2 of 2) — Create Ticket / My Tickets / Ticket Detail screens, attachments, Zen Green theme UI, full test suite (unit/API/UI/E2E) |
| 5 | 1,3 Sep | Software Security: Authentication, Passwords, Sessions, User Management; Authorization, Roles, SQL Injection, and Common Vulnerabilities (Dr. Piyanit) | Lab: Lab 3 (Week 1 of 2) — Authentication, mandatory first-login password change, User model, migration from Development Requester |
| 6 | 8,10 Sep | Project Management I: Work Breakdown, Estimation, Scheduling, Resource Constraints, and Definition of Ready (Dr. Santawat) | Lab: Lab 3 (Week 2 of 2) — Role-based authorization (Requester / IT Staff / Administrator), IT Staff ticket queue, Administrator user management, public comments & internal notes |
| 7 | 15,17 Sep | Team Project Kickoff: Proposal, Backlog, Agile Planning, Team Workflow, and Repository Hygiene (Dr. Santawat) | Lab: Lab 4 (Week 1 of 2) — Actions Taken model, Ticket status-transition matrix, cross-record business rules |

-3-

## Page 4 — Course Schedule (Weeks 8–14, Exams, Final Presentation)

| Week | Date | Topics | Activities |
| --- | --- | --- | --- |
| 8 | 22,24 Sep | Architecture, Infrastructure, API Design, UML, and Test Strategy for Team Projects (Dr. Santawat) | Lab: Lab 4 (Week 2 of 2) — IT Staff & Requester dashboards, final regression & product hardening (complete TokTickIT) |
| 9 | 6,8 Oct | CI/CD, Build Automation, Quality Gates, and Release Discipline (Dr. Santawat) | Lab: Team Project Kickoff + CI/CD — set up the team repo, proposal & backlog, branch protection, and a CI pipeline with build and automated-test quality gates on every Pull Request |
| 10 (Holiday) | 13,15 Oct | Midterm Review and Individual Practical Integration (Dr. Suthep) | Lab: Individual Practical Challenge & Demo (midterm integration); begin Team Sprint 1 — working vertical slice |
| | 14–28 Oct | Midterm Exam (covers Weeks 1–7) | |
| 11 | 3,5 Nov | Cloud Deployment and Delivery to Users (Dr. Suthep) | Lab: Cloud Deployment Lab — deploy the team application to the cloud (GCP) and deliver to users; Team Sprint 2 |
| 12 | 10,12 Nov | Quality Assurance, UAT, Defect Management, Maintenance, and Technical Debt (Dr. Piyanit) | Lab: QA & UAT — write UAT scripts, defect triage & fixing, maintenance tickets, and a technical-debt log; Team Sprint 3 |
| 13 | 17,19 Nov | Metrics, Reviews, Retrospectives, Ethics, Responsible AI Use, and AI Usage Report (Dr. Suthep) | Lab: Metrics, code review & retrospective; Responsible-AI reflection and AI Usage Report; final project hardening |
| 14 | 24,26 Nov | Final Delivery, Product Demonstration, and Course Integration | Lab: Final Team Demo & Submission — product demonstration and course integration |
| | 1–11 Dec | Final Exam (covers Weeks 8–14) | |
| | After Finals | Project Demonstration and Presentation | |

*Note: Any additional modifications to the syllabus will be announced in class.*

-4-
