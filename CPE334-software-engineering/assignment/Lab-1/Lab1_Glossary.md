Appendix — Glossary of Key Terms

New vocabulary appears fast in Lab 1. Use this table as a quick reference while you work; each term is also
explained in context in the Guided Walkthrough.

Area       Term                 What it means
Product &  Vertical slice       A thin feature that runs through every layer (UI → API → database) to prove the
process    Engineering          whole stack works together.
           contract             The specification PLUS the evidence (tests, acceptance criteria) required to prove
Web stack  Acceptance criteria  it is complete.
                                The specific, checkable conditions an Issue must meet before it is accepted as
Database   Definition of Done   done.
           Frontend /           The checklist that marks work truly finished: merged via PR, tests passing,
Testing    Backend              documented.
           REST API             The browser-side app (React) versus the server program (Express) it talks to over
Git &                           HTTP.
GitHub
                                A style where the backend answers HTTP requests sent to URLs called endpoints.

           Endpoint             One URL + method the API answers, e.g. GET /api/health.

           JSON                 The plain-text format used to exchange data between the frontend and backend.

           HTTP status          The numeric result of a request: 200 OK, 500 server error, 501 not implemented.

           TypeScript           JavaScript with type checking, so many mistakes are caught before the code runs.

           Vite                 The dev server / build tool that runs the React frontend (http://localhost:5173).
           CORS
           PostgreSQL           A browser security rule: the API must allow the frontend's origin, or the call is
           Prisma (ORM)         blocked.
           Model                The relational database that stores the application's data.
                                A library that reads and writes the database from your code, without hand-writing
                                SQL.

                                The shape of a database table, declared once in the Prisma schema.

           Migration            A recorded change that creates or alters database tables.

           Seed                 Code that inserts starter rows — here, the four request categories.
           Idempotent
           Vitest               Safe to run again with no extra effect; use upsert so re-running the seed makes no
           Supertest            duplicates.
           Mock                 The test runner for the frontend and unit tests.
                                A library that tests API endpoints by importing the app directly (no running server
           TDD                  needed).
                                A fake stand-in for a real dependency in a test, e.g. pretending the API call
                                succeeded or failed.
                                Test-Driven Development: write the test first, then write code until it passes (red
                                → green).

           Git flow             The branch discipline used here: feature branch → lab1-staging → main.

           Feature branch       A short-lived branch holding the work for one Issue.
           Staging branch       lab1-staging — the integration branch where features merge and are tested before
                                main.
Pull Request (PR)  A request to merge a branch; it is reviewed before it can be merged.
Peer review        Your partner reviews your PR and approves it or requests changes.
Issue              A tracked unit of work on GitHub (one per task).
GitHub Project /
Kanban             A board with status columns (Backlog … Done) that tracks each Issue's progress.
