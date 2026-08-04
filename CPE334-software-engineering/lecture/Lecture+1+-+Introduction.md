# Lecture 1 - Introduction — CPE334 Software Engineering (in the Age of AI Coding Agents)

> Text cache of [[Lecture+1+-+Introduction.pdf]]. Auto-generated transcription — layout and some figure detail are lost. Read the PDF directly if visuals matter.

## Slide 1 — Lecture 1 - Introduction

**CPE334 – Software Engineering** (in the Age of AI Coding Agents)

Week#1: 3-7 August 2026

- Dr. Suthep Madarasmi
- Dr. Piyanit Ua-areemitr
- Dr. Santawat Thanyadit

Department of Computer Engineering
King Mongkut's University of Technology Thonburi

*Figure: title slide with KMUTT and CPE department logos.*

## Slide 2 — Today's lecture storyline

From *AI can write code* to *we can engineer a product*.

1. AI coding agents
2. Code vs software product
3. Software Development Life Cycle
4. Process models
5. Responsible AI use
6. Lab preparation

## Slide 3 — AI coding agents

Not just autocomplete: agents can plan steps, call tools, edit files, run commands, and propose changes.

- A basic chatbot - mainly produces a response based on *inputs*
- AI agent – an ***autonomous*** software system that can pursue a *goal*
  - Understanding its **environment** and instructions
  - **Planning** a sequence of actions
  - **Using tools** or external systems
  - Observing the results
  - Adjusting its actions until the task is completed (**feedback loops**)
  - Retain context across interactions (**memory**)
- AI coding agent - performs software-development actions using code, tools, tests, and repositories

*Figure: horizontal pipeline diagram — Understand task → Inspect repo → Plan changes → Edit + run tests → Propose review — showing the five-step loop an AI coding agent follows.*

## Slide 4 — (Discussion question)

**Is knowing how to use AI coding agents enough to develop software?**

## Slide 5 — (Discussion question)

**Which processes are necessary for software development?**

## Slide 6 — Which processes are necessary for software development?

Software development is a sequence of decisions, not only a sequence of prompts.

*Figure: seven-stage horizontal process flow — Discover (problem, users, value) → Decide (scope, priorities, risks) → Design (structure and interfaces) → Build (code and integration) → Verify (tests and review) → Release (deploy and operate) → Learn (feedback and change).*

- AI can assist at every stage, but every stage still needs a human accountable for the decision.
- A good software engineer learns how to convert messy needs into small, verified product increments.

## Slide 7 — Writing code vs engineering a software product

AI lowers the cost of code. It does not remove the cost of building the right thing well.

| Writing code | Engineering a software product |
|---|---|
| Implements an instruction | Solves a user problem |
| Works on a local example | Meets explicit acceptance criteria |
| May ignore future maintainers | Is testable, secure, maintainable |
| Can be generated quickly | Can be operated and evolved |

**Course principle:** Use AI to accelerate implementation, but use software engineering to define, constrain, verify, and evolve the product.

## Slide 8 — Software Development Life Cycle (SDLC)

A repeatable roadmap for moving from a problem to a maintained product.

*Figure: eight-stage horizontal pipeline — Planning (why + feasibility) → Requirements (what users need) → Specification (agreed behavior) → Design (how it works) → Implementation (code changes) → Testing (evidence) → Deployment (release) → Maintenance (learn + evolve), with a dotted feedback arrow looping from Maintenance back to Planning.*

- Feedback loops: requirements change, tests reveal defects, deployment creates new learning.
- Different models arrange these phases differently; the activities never disappear.

## Slide 9 — SDLC phase 1–2: Planning and requirements

Before asking an agent to code, decide the product problem and the expected value.

**Planning**
- Stakeholders and users
- Goals and success measures
- Feasibility, constraints, risk
- Scope and priorities

**Requirements**
- Functional requirements: what the system must do
- Non-functional requirements: quality attributes
- Constraints: laws, platforms, budget, data
- Traceability: where each need came from

**Requirement = a documented need, capability, or constraint that the software must satisfy.**

## Slide 10 — SDLC phase 3: Specification as an engineering contract

A specification turns requirements into testable, reviewable agreement.

| Specification | Acceptance criterion | Engineering contract |
|---|---|---|
| Precise description of expected behavior, interfaces, rules, data, errors, and quality constraints. | A condition that must be true for a feature/user story to be accepted by the product owner or stakeholder. | The shared baseline between stakeholders and engineers: what will be built, what counts as done, and how it will be verified. |

**Example**
- **Requirement**: Students can submit lab work online.
- **Specification**: System accepts .ipynb files ≤ 25 MB before deadline; records timestamp; shows confirmation.
- **Acceptance criteria**: Given a valid file before deadline, when the student clicks Submit, then the submission is stored and a confirmation ID is displayed.

**Key idea: an AI coding agent should receive the specification, not just a vague wish.**

## Slide 11 — SDLC phase 4: Design and architecture

Design decides the structure before code multiplies the cost of a bad decision.

*Figure: four-box horizontal architecture flow — UI → API → Service → Database — representing a typical layered application architecture.*

**Design artifacts:** Architecture diagrams · data models · API/interface contracts · UI flows · security boundaries · error handling

**AI can propose designs. Engineers must check trade-offs, consistency, scalability, security, and maintainability.**

## Slide 12 — SDLC phase 5: Implementation with coding agents

Implementation is where coding agents are strongest — when the task is small and well-specified.

**Good delegation pattern**

1. **Give context** — repo structure, files, constraints, coding standard
2. **Give specification** — inputs, outputs, edge cases, acceptance criteria
3. **Ask for plan first** — let the agent explain intended files and tests
4. **Scope the increment** — one feature, one bug, or one refactor at a time
5. **Review evidence** — diff, commands run, tests, docs, and residual risks

## Slide 13 — SDLC phase 6: Testing and verification

Testing is evidence. It does not prove perfection, but it reduces uncertainty.

*Figure: four-tier testing pyramid (trapezoid stack) from bottom to top — Unit tests (single function/class), Integration / API tests (components together), UI / End-to-end tests (user flows), Acceptance tests (stakeholder value).*

**Also test:**
- **Regression**: old behavior still works
- **Exploratory**: human discovery of unexpected defects
- **Performance**: speed, load, resource use
- **Security**: misuse, secrets, injection, permissions
- **Usability**: can real users complete the task?

**AI-generated tests are useful but not automatically correct; check that tests would fail on a real defect.**

More reading: https://www.geeksforgeeks.org/software-testing/types-software-testing/

## Slide 14 — SDLC phase 7–8: Deployment, operation, and maintenance

Software becomes real when users depend on it.

*Figure: five-step horizontal chain of circles — Release (version, build, environment) → Configure (secrets, variables, data migration) → Monitor (logs, metrics, alerts) → Rollback (safe recovery plan) → Improve (feedback, defects, refactoring).*

## Slide 15 — Role of AI coding agents across the SDLC

"AI Agent Readiness Across the SDLC" — Where agents create leverage, where they assist, and where human judgment stays in control.

*Figure: six-column diagram, each column an SDLC phase icon with "Best agent use" and "Human-owned" lists plus a "Recommended mode" pill, connected left to right by arrows:*

| Phase | Best agent use | Human-owned | Recommended mode |
|---|---|---|---|
| 1. Planning | Ticket drafts; Prior discussion summaries | Architecture decisions | Assist only |
| 2. Coding | Boilerplate & refactors; Context-aware completion | Critical path logic | Draft + review |
| 3. Code Review | Diff summaries; Convention checks | Reviewer of record | First-pass support |
| 4. Testing | Unit test scaffolds; Edge-case suggestions | Regression sign-off | Suggest + validate |
| 5. CI/CD & Deploy | Build failure triage; Release note drafts | Deploy decisions | Triage only |
| 6. On-Call & Operations | Incident summaries; Log triage | Escalation decisions | Briefing support |

**Use agents where context is available. Keep humans accountable where judgment is required.**

Source: https://www.genaiprotos.com/blog/ai-agents-in-the-sdlc/

## Slide 16 — Role of AI coding agents across the SDLC (continued)

Use the right agent behavior at the right phase.

| Agent type | Role |
|---|---|
| **Specification agent** | clarify requirements, draft user stories, refine acceptance criteria, detect ambiguity |
| **Coding agent** | implement small scoped increments, refactor, update tests, generate docs |
| **Debugging agent** | reproduce defect, inspect logs, isolate root cause, propose fix and regression test |

**Never let the agent choose the product goal, acceptance standard, risk appetite, or final responsibility.**

## Slide 17 — Risk: blindly accepting "works"

An AI agent's claim is not evidence.

- **Wrong target** — implements a different requirement
- **False confidence** — claims tests passed but did not run them
- **Hidden breakage** — passes examples but fails edge cases
- **Security gaps** — leaks secrets, weak permissions, unsafe commands
- **Dependency risk** — adds packages or commands you do not understand
- **Documentation drift** — README/comments no longer match behavior

**Engineers remain responsible for AI-generated code, tests, commands, and documentation submitted under their name.**

## Slide 18 — SDLC models

Models are ways to organize the same core activities.

**Planning style**
- **Predictive** - Plan first, then execute. Change is controlled. *(Figure: person with a boxed product idea flowing through Design → Implementation → Testing to a final boxed product — a linear, plan-driven flow.)*
- **Adaptive** - Learn while building. Change is expected. *(Figure: person with an evolving product idea, adjusted based on feedback through successive wrapped/gift-wrapped box stages — showing iterative refinement of the product concept.)*

**Delivery style**
- **Incremental** - Deliver working slices of the product. *(Figure: a circle growing step by step into a skateboard-like frame, then a partial car, then a full car — each stage adds more value/completeness.)*
- **Iterative** - Refine the same solution through feedback cycles. *(Figure: a row of faces from frowning to smiling above a skateboard → scooter → bicycle → motorbike → car progression — "same feature, better fit" — showing the same transportation need refined repeatedly.)*

## Slide 19 — Examples of SDLC models - Waterfall

*Figure: five-stage horizontal flow with bidirectional arrows — Requirements → Design → Implementation → Verification → Deployment & Maintenance — the classic Waterfall model, Requirements stage highlighted as the starting point.*

**Use**
- Requirements are stable and well understood.
- Team has experience building similar software
- Define change-control rules before implementation begins.

**Pros**
- Clear milestones and responsibilities.
- Strong traceability from requirement to release.
- Easier upfront budgeting and scheduling.

**Cons**
- First release takes a long time.
- Feedback arrives late.
- Changes become expensive (not flexible for changes).

**Waterfall is not bad; it fits low-uncertainty work better than discovery-heavy work.**

## Slide 20 — Examples of SDLC models – Incremental model

*Figure: the same five-stage Waterfall-style pipeline (Requirements → Design → Implementation → Verification → Deployment & Maintenance) branching down into four sequential increment boxes — Increment 1 (MVP / core workflow) → Increment 2 (Add priority feature) → Increment 3 (Integrate & harden) → Increment 4 (Release candidate) — labeled "Working product grows over time."*

**Use**
- If organization may benefit from early delivery of part of product.
- If building one increment will help define future increments.

**Pros**
- Early user feedback & make necessary changes between increments.
- Earlier business value.
- Better risk management than one big release.

**Cons**
- Needs disciplined architecture and integration.
- May result in rework.
- Requires continuous validation.

**Increment ≠ unfinished fragment. Each increment should be coherent enough to evaluate.**

## Slide 21 — Examples of SDLC models – Agile values

Agile emphasizes feedback, adaptation, and working software in increments.

Agile Alliance was officially formed in 2001. Starting with Manifesto to principles.

*Figure: three repeating circular arrow icons labeled "Define, design, build, test," chained left to right along a rightward arrow — representing repeated short Agile cycles.*

- **Individual & interaction** over processes & tools — Effective communication among team members.
- **Working software** over comprehensive documentation — Regular delivery of working software allows early validation and feedback from users.
- **Customer collaboration** over contact negotiation — Customers provide regular feedback, ensuring the product aligns with their expectations.
- **Responding to change** over following a plan — Flexible planning ensures the product remains relevant and up to date.

**People & interaction** — Pros: early detection. Cons: requires participation.

**Adaptive** — Pros: early detection. Cons: System modelling is challenging; Lack of control.

More reading: https://agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/

## Slide 22 — Examples of SDLC models – Agile frameworks (Scrum)

**Scrum** — Choose Scrum when product discovery benefits from sprint goals and regular ceremonies.

*Figure: Scrum cycle diagram. Roles shown: Product Owner (value & priorities), Team (design, build, test, & deliver), Scrum Master (process & impediments). Flow: Product Backlog (ordered work items) → Sprint Planning Meeting (select goal & work) → Sprint Backlog → Sprint (1-4 Weeks, short time-boxed development cycle) with a 24H inner loop to Daily Stand Up (inspects progress and adapt) → Sprint Review + Sprint Retrospective (show increment / improve the process) → Finished Work (Done means integrated, tested, and reviewable).*

Source: https://www.pm-partners.com.au/insights/the-agile-journey-a-scrum-overview/

## Slide 23 — Examples of SDLC models – Agile frameworks (Kanban)

**Kanban** — Choose Kanban when work arrives continuously and controlling flow is the main problem.

**Flow-management system**
- Visualize workflow
- Limit work in progress
- Manage flow
- Make policies explicit
- Improve collaboratively

*Figure: Kanban board table with columns labeled Backlog, Acknowledged, Development (In progress / Ready), Testing (In progress / Ready), Deployment, Done, and a "Status" row. Colored square job cards (two work-item types) populate cells, illustrating cards moving left to right across workstage columns and status sub-lanes; annotations point out "Column" and "Lane (across columns)."*

Legend: dark green square = Work Item (Type 1); light green square = Work Item (Type 2).

**Notes**
- Cycle time: start to finish
- Throughput: completed items per period
- Blocked work: visible delays

Source: https://www.geeksforgeeks.org/software-engineering/kanban-agile-methodology/

## Slide 24 — Definition of Done: the completion gate

Done is not a feeling. It is an agreed quality checklist.

**Definition of Done (DoD) = team-level conditions that every completed increment must satisfy.**

- Acceptance criteria satisfied
- Code reviewed
- Tested (are written and passed)
- No critical defects/security issues
- Docs / comments updated
- Merged/deployed according to policy

**The DoD is used as a gate at the end of a story/increment/sprint or release after implementation and verification, before calling work complete.**

More reading: https://saat-network.ch/2023/06/working-reliable-valuable-a-definition-of-done-checklist/

## Slide 25 — Lecture takeaway: AI-native, engineering-first

The goal is not to avoid AI. The goal is to use AI inside a reliable engineering process.

- **Product thinking** — users, value, scope, acceptance
- **Engineering process** — SDLC, design, tests, DoD
- **AI agent skill** — delegation, review, debugging

**Good software engineers in the age of agents can define the work, constrain the agent, verify the result, and explain the trade-offs.**

## Slide 26 — (Section transition)

**Let's prepare for our lab session.**

## Slide 27 — Full-stack web app: from UI to database

A full-stack app is a set of layers that work together: the user interface, server logic, data access layer, and persistent storage.

*Figure: "Typical Lab Architecture" — vertical stack of four boxes connected top to bottom: React UI ("Frontend running in the browser. Displays screens and sends requests when users act.") --HTTP request/response--> Express REST API ("Backend endpoints such as GET /api/categories. Handles validation and application logic.") --Prisma Client method call--> Prisma ORM (Object-Relational Mapping) ("Object–Relational Mapper. Let code query database tables using JS/TS objects.") --SQL over DB connection--> PostgreSQL ("Relational database").*

| Term | Definition |
|---|---|
| Frontend | User-facing code in the browser: screens, forms, interaction, client-side state. |
| Backend | Server-side code: business rules, authentication checks, validation, data access. |
| API | The contract between frontend and backend: endpoint, method, input, output, status codes. |
| ORM | A programming layer that maps objects/classes to database tables and creates SQL queries. |
| Database | The persistent source of truth for structured data and relationships. |

## Slide 28 — ORM idea

The developer writes object-style code; the ORM generates database queries and maps results back into objects.

*Figure: three-box flow — Object (`data class User (val name: String, val email: String, val age: Int)`) → Relational (table with columns name, email, age) → Mapping (matching object fields to database columns) — with both Object and Relational boxes feeding down into a "Matching object fields to database columns" box.*

```
// prisma
model User {
  name   String
  email  String   @Id
  age    Int
  @@map("user")
}

// Typescript
const users = await prisma.user.findMany();
//SELECT * FROM user;
```

Source: https://medium.com/@lordpacific/what-is-orm-a-beginners-guide-to-object-relational-mapping-0a20707fcdd1

## Slide 29 — Vertical slice

*Figure: four stacked horizontal layer bars (UI, Application, Domain, Database) with a single vertical bar labeled "Vertical Slice" cutting through all four layers, showing that one slice touches every layer of the stack.*

- A project management technique
- Emphasizes delivering a fully functional piece of a project, encompassing all layers of the application stack.
- Ensures that each feature or functionality is developed and delivered end-to-end in a single iteration.

Source: https://www.gianty.com/vertical-slice-game-development/

## Slide 30 — Specification-Driven and Test-Driven Development

Two disciplines that make AI-assisted coding safer.

**Specification-Driven Development**
Start by writing the expected behavior clearly enough that implementation choices can be judged.
Typical artifacts: user story, specification, API contract, examples, acceptance criteria.

**Test-Driven Development**

*Figure: three-circle cycle — Red (write failing test) → Green (write just enough code) → Refactor (improve design safely).*

**With agents: write the spec → ask the agent to derive tests → review tests → implement → verify against the spec.**

## Slide 31 — Version control

**Version control system (VCS)** - a software tool to track & manage changes to source code & digital files

- **Track changes to source code** — who, what, when, why
- **Recovers older version** — before experiments and agent edits
- **Facilitate collaboration** — avoid code conflicts & overwriting work

*Figure: three "Developer" nodes, each with a Local Repository and Working Files box connected by commit/update arrows, all pushing to and pulling from a shared central "Main Repository" box — illustrating a distributed version control topology.*

**Distributed VCS:** Git (command line) and GitHub (web-hosted service).

Source: https://www.researchgate.net/publication/371671830_The_five_pillars_of_computational_reproducibility_Bioinformatics_and_beyond

## Slide 32 — Git workflow

**Repositories** — Upload: `git push` (Local repository → Remote repository); Download: `git pull` (Remote repository → Local repository).

**Reviewing code (Github)** — Checking that it all makes sense & follows the expected patterns.

*Figure: flow from Pull request → Code review (project maintainer) → accept => Merge → Main branch in the remote repository; a reject path loops back as "comments & revision" to the Pull request stage.*

## Slide 33 — Git workflow (branching)

*Figure: Git commit-graph diagram. A "Master" line runs left to right through green commit dots. A blue "Your Work" branch (`git branch your-work`) diverges upward with three blue commits, then rejoins Master via `git merge your-work`. An orange "Someone Else's Work" commit branches below and also merges back into Master.*

- **Main (master):** stable release branch. Code should represent accepted output.
- **Feature branches**: short-lived branches for one small feature.

Source: https://novatorsoft.com/en/blog/what-is-branch-how-to-use

## Slide 34 — Git workflow (course branch structure)

*Figure: tree diagram — `main` at top, pointing down to `lab1-staging` ("Integration branch where completed Lab 1" work accumulates), which fans out to four feature branches: `feature/1-project-foundation`, `feature/2-health-check`, `feature/3-category-seed`, `feature/4-category-list`.*

**Feature branches do not merge directly to main. They merge to lab1-staging first through Pull Requests.**

**Release path: feature → lab1-staging → main**

## Slide 35 — Git workflow (scenario walkthrough)

**Scenario: web app development**

Legend: person icon = Lead developer; group icon = Team.

*Figure: multi-step icon sequence across "Local" and "Remote" panels illustrating a full workflow:*
1. Lead developer initializes a Git repository (local)
2. Moves files to the staging area (local)
3. Performs initial commit (local)
4. Pushes commit to blank repository (remote)
5. Team clones remote repository (local)
6. Team creates branch (Feature_branch, local)

**Feature development** panel: Cloned repository → Creates user_auth branch → Commits to the branch (local, by team) → Pushes the branch to remote and creates a pull request (remote) → Lead developer approves pull request and merges changes (remote).

**Project release** panel: Team pulls changes (local) → Performs testing and updates (local) → creates a release branch (remote, by lead) → pushes commits to remote and creates a pull request (remote, by team) → Lead developer approves pull requests and merges changes (remote).

## Slide 36 — Git workflow (commands)

*Figure: four-stage horizontal pipeline — Working tree (edited files) --`git add .`--> Staging area (selected changes) --`git commit`--> Local repository (commits + history) --`git push`/`git pull`--> Remote repository (GitHub / origin). Below, two small illustrated icons: a workbench labeled "Working tree" and filing cabinets labeled "Staging area" / "Repository."*

```bash
# Select changes to include in the next checkpoint
git add README.md src/app.js

# Save the checkpoint in local commit history
git commit -m "Add project foundation"

# Share local commits with GitHub
git push origin feature/1-project-foundation
```

```bash
# Update the current local branch from its remote branch
git pull origin lab1-staging

# Inspect history
git log --oneline --graph --decorate

# Show the current state of working directory & staging area
git status
```

## Slide 37 — Quick recap

| Term | Definition |
|---|---|
| Repository | A project folder tracked by Git. |
| Remote repository | The repo hosted on GitHub. |
| Local repository | The repo on your computer. |
| Origin | The usual remote name for GitHub. |
| Clone | Local copy of the remote Git repository |
| Merge | Combine changes from one branch to another. |
| Working tree | Files you are currently editing. |
| Staging area | Changes selected for the next commit. |
| Commit | A saved snapshot of the project's current state. |
| Commit history | The ordered record of snapshots. |
| Branch | A named, separate line of development. |

## Slide 38 — Github overview

Online hosting service for Git repositories

*Figure: screenshot of a GitHub repository page ("piyanitwep-sys / se-demo") showing the Code tab, branch selector (main, 2 Branches), a recent merged pull request commit, the README content ("se-demo — For simple demo how to use Github Edit message"), and a right-hand "About" sidebar with Readme, Activity, stars/watchers/forks counts, Releases, Packages, and Contributors sections.*

## Slide 39 — Github code review

*Figure: screenshot of a GitHub pull request titled "Landing Page Improvements #1," merged, showing 27 commits merged into main from a dated branch, with tabs for Conversation, Commits, Checks, Files changed (98). A diff view for `src/components/Navigation.js` shows removed lines (red, e.g. old React/Gatsby imports and a `header` variable pattern) and added lines (green, e.g. new imports and a `return (` JSX pattern) — illustrating a side-by-side code review diff.*

Source: https://www.awesomecodereviews.com/tools/best-code-review-tools/

## Slide 40 — Github issue & kanban

*Figure: five-stage horizontal flow — Issue → Branch → Commit → Pull Request → Merge — showing the standard GitHub contribution lifecycle.*

**Issues** panel: screenshot of a GitHub Issues list (2,798 open issues) with filters, labels, milestones, and example issue titles (e.g. "Testing: Travis Integration out-of-date," "Components are not removed from DOM when calling NgModuleRef.destroy()").

**Kanban** panel: screenshot of a GitHub Projects Kanban board with columns Backlog, Planned, In Progress, Done, populated with example cards (e.g. "Fullscreen mode refactoring," "Stop timer from team dashboard," "Summary emails").

**Note:**
- **Issue**: describes work, acceptance criteria, dependencies & evidence needed.
- **Branch**: isolates code changes that implement one Issue.

Sources: https://www.geeksforgeeks.org/git/issues-in-github/ ; https://everhour.com/blog/tracking-time-github-boards/

## Slide 41 — Repository setup

**Case 1 – clone from Github**

```bash
# 1) Copy the repository URL from GitHub
# Example: https://github.com/org/se-ai-lab1.git

git clone https://github.com/org/se-ai-lab1.git
cd se-ai-lab1

# 2) Check where you are and what branch is active + change branch
git status
git branch
git checkout -b new-branch

# 3) Inspect the latest commits
git log --oneline --decorate -5
```

```bash
# Verify remote location
git remote -v

# Clean start should show:
# nothing to commit, working tree clean
git status
```

**Case 2 – initialize a safe new one**

```bash
mkdir se-ai-lab1
cd se-ai-lab1

git init

# Create basic project files
echo "# SE AI Lab 1" > README.md
echo "node_modules/" > .gitignore
echo ".env" >> .gitignore
echo "DATABASE_URL=" > .env.example

# First local commit
git add README.md .gitignore .env.example
git commit -m "Initial project setup"
```

```bash
# Connect to GitHub and push main
git branch -M main
git remote add origin https://github.com/org/se-ai-lab1.git
git push -u origin main
```

**The commit message explains the engineering purpose, not just say "update files".**

## Slide 42 — Repository setup (hygiene)

**Never commit**
- .env files
- passwords or API keys
- database credentials
- node_modules/
- generated build files
- large temporary outputs

**README should state**
- What the project is
- How to install and run
- Required environment variables
- How to run tests
- Branch and Pull Request (PR) rules for the lab

## Slide 43 — Create a feature branch – push – open PR

**Example Issue: #1 Project foundation**

```bash
# 0) Get a list of branch
git branch

# 1) Start from the integration branch
git switch lab1-staging

# 2) Get the latest staging work from GitHub
git pull origin lab1-staging

# 3) Create a feature branch for one Issue
git switch -c feature/1-project-foundation

# 4) Work, inspect, stage, and commit
git status
git add .
git commit -m "Set up project foundation"

# 5) Publish the branch to GitHub for the first time
git push -u origin feature/1-project-foundation
```

**Note**
- Starting from lab1-staging avoids building on outdated code.
- The branch name connects the code change to a specific Issue.
- Small commits make review and debugging easier.

**Then in GitHub**
- Create PR from feature/1-project-foundation into lab1-staging.
- Link the Issue in the PR description, for example: "Closes #1".
- Paste acceptance criteria and mark what is satisfied.
- Request peer review before merging.

**Before asking an AI agent to implement, create the branch first so its changes are isolated.**

## Slide 44 — Keep your feature branch current before merge

**Merge another feature into lab1-staging first**

```bash
# 1) Download latest remote information
git fetch origin

# 2) Stay on your feature branch
git switch feature/2-health-check

# 3) Merge the latest staging branch into your feature branch
git merge origin/lab1-staging

# 4) If conflicts happen: edit files, then
git status
git add <resolved-files>
git commit

# 5) Update the Pull Request
git push
```

```bash
# Optional local cleanup after merge
git switch lab1-staging
git pull origin lab1-staging
git branch -d feature/2-health-check
```

**After PR approval**
- Merge into lab1-staging, not directly into main.
- Delete completed remote feature branches after merge.
- Keep local branches tidy after they are finished.

*Figure: two small icons labeled "Local repository" and "Remote repository."*

## Slide 45 — Fast-forward merge vs 3-way merge

*Figure: four commit-graph diagrams. Top pair: "Before Merging" shows Main behind a "Some Feature" branch on a single line; "After a Fast-Forward Merge" shows Main's pointer simply moved forward to the tip of Some Feature (no new merge commit, since Main had no divergent commits). Bottom pair: "Before Merging" shows Main and Some Feature diverging from a common point with commits on both sides; "After a 3-way Merge" shows a new merge commit created on Main that combines both histories, since the branches diverged.*

Source: https://www.linkedin.com/posts/aftabnajib_git-branching-mergeconflicts-activity-7359217391152603138-L5lt/

## Slide 46 — Release Lab 1 from staging to main

*Figure: simple three-box horizontal flow — feature branches → lab1-staging → main.*

- Confirm all Lab 1 feature PRs are merged into lab1-staging.
- Run required checks or demonstrations from lab1-staging.
- Create a PR from lab1-staging into main.
- Merge with a merge commit after approval.

**Release means the integrated lab work is accepted on main, not merely that individual features were pushed.**

**Done** = accepted by review + satisfies criteria + merged + evidence documented
≠ the AI agent said it works
