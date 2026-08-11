# Lab 1 — คู่มือเดินงานทีละก้าว

แปลง [[Lab1_Labsheet.pdf|labsheet]] ให้เป็นลำดับ action ที่ทำตามได้จริง ตั้งแต่ยังไม่มีอะไรเลยจนถึง
ส่ง PDF · ศัพท์ที่ไม่รู้ดูที่ [[Lab1_Glossary.pdf|glossary]] · เบื้องหลังว่าทำไม Git ถึงทำงานแบบนี้
ดูที่ [[Git_GitHub_Workflow_Playbook]] · เนื้อ Issue พร้อมก๊อปอยู่ที่ [[Lab1_Issue_Drafts]]

**วิธีใช้ไฟล์นี้:** ทำจาก Phase 0 ไล่ลงมา ห้ามข้าม · ทุก Phase มี "หลักฐานที่ต้องเก็บ" ตอนท้าย
แคปไว้ทันที เพราะหลายอย่างย้อนไปถ่ายไม่ได้ · คำสั่งทั้งหมดเขียนสำหรับ **PowerShell**

---

## แผนที่ทั้งหมด — 10 Phase

| Phase | ทำอะไร | ใช้เวลาโดยประมาณ |
| --- | --- | --- |
| 0 | เตรียมเครื่อง เตรียมคน | 1 ชม. |
| 1 | สร้าง repo + branch + collaborator | 20 นาที |
| 2 | สร้าง Project board + Issue 4 อัน | 40 นาที |
| 3 | Issue #1 — วางโครงโปรเจกต์ | 2–3 ชม. |
| 4 | Issue #2 — health check | 1–2 ชม. |
| 5 | Issue #3 — Category + seed | 1–2 ชม. |
| 6 | Issue #4 — แสดงรายการ category | 2 ชม. |
| 7 | เอกสาร 4 ไฟล์ | 1 ชม. |
| 8 | Release เข้า `main` | 20 นาที |
| 9 | เก็บหลักฐาน + ทำ PDF ส่ง | 1–2 ชม. |

**อย่าทำรวดเดียวจบ** — Phase 3–6 แต่ละอันต้องรอเพื่อนรีวิว เผื่อเวลารอไว้ด้วย ไม่งั้นจะไปติดคอขวด
ตอนใกล้ deadline

---

## Phase 0 — เตรียมก่อนแตะอะไรทั้งนั้น

### 0.1 หาคู่ peer reviewer

labsheet §6 ข้อ 1 บอกให้หาก่อนเป็นอย่างแรก เพราะทุก PR ต้องมีคนอนุมัติ ถ้าหาไม่ได้ = ทำ Lab
ไม่จบ ไม่ใช่แค่เสียคะแนน

ตกลงกับเพื่อนให้ชัด 3 เรื่อง:

1. แลก **GitHub username** กัน (ไม่ใช่ชื่อเล่น ไม่ใช่อีเมล — username ที่ใช้ล็อกอิน)
2. แลกรหัสนักศึกษาและชื่อเต็ม (ต้องใส่ใน `docs/lab-01/reviewer.md`)
3. ตกลงเวลาตอบรีวิว เช่น "เปิด PR แล้วรีวิวกลับภายใน 12 ชม." — ในทีมจริงเรียก
   *review SLA* ถ้าไม่ตกลงไว้ งานจะค้างที่คอลัมน์ PR Review เป็นวัน ๆ

### 0.2 ติดตั้งเครื่องมือ

เช็คว่ามีอะไรแล้วบ้าง:

```powershell
git --version
node --version
npm --version
psql --version
gh --version
```

**Node.js** — ต้อง v18 ขึ้นไป (เครื่องมึงมี v24 แล้ว ผ่าน) ถ้าไม่มี: `winget install OpenJS.NodeJS.LTS`

**PostgreSQL** — ยังไม่มีต้องลง เลือกทางใดทางหนึ่ง:

```powershell
winget install PostgreSQL.PostgreSQL.17
```

ตอนติดตั้งมันจะให้ตั้งรหัสผ่านของ user `postgres` — **จดไว้** เดี๋ยวต้องเอาไปใส่ `DATABASE_URL`<br/>
พอลงเสร็จ PostgreSQL จะรันเป็น Windows Service อัตโนมัติที่พอร์ต `5432` และได้ pgAdmin
มาด้วยสำหรับส่องข้อมูลแบบ GUI

**GitHub CLI** (ไม่บังคับ แต่ทำให้เร็วขึ้นเยอะ):

```powershell
winget install GitHub.cli
```

ปิดเปิด terminal ใหม่ แล้ว `gh auth login` → GitHub.com → HTTPS → Login with a web browser

### 0.3 ตั้งค่า Git identity

```powershell
git config --global user.name "ชื่อจริงของกู"
git config --global user.email "อีเมลที่ผูกกับบัญชี GitHub"
```

> **สำคัญมาก** GitHub จับคู่ commit กับบัญชีด้วย**อีเมล** ถ้าไม่ตรงกับที่ verify ไว้ commit
> จะขึ้นเป็นคนแปลกหน้าไม่มีรูป แล้วหลักฐาน commit history ใน Part 1 จะดูเหมือนไม่ใช่งานของมึง
> เช็คที่ [github.com/settings/emails](https://github.com/settings/emails)

### 0.4 เลือกที่วางโปรเจกต์

**ห้ามวางในวอลต์ `1_Uni`** เพราะวอลต์เป็น Git repo อยู่แล้ว จะกลายเป็น repo ซ้อน repo
แนะนำ `C:\Users\BTCOM\Desktop\toktickit`

**หลักฐานที่ต้องเก็บ:** ยังไม่มี

---

## Phase 1 — repo, branch, collaborator

### 1.1 สร้าง repo บนเว็บ

github.com → ปุ่ม `+` มุมขวาบน → **New repository**

| ช่อง              | ใส่อะไร                                                |
| ----------------- | ------------------------------------------------------ |
| Repository name   | `toktickit`                                            |
| Visibility        | Private                                                |
| Add a README file | **ติ๊ก**                                               |
| Add .gitignore    | เลือก `Node` (จะได้ไม่ต้องเขียนเอง เดี๋ยวค่อยแก้เพิ่ม) |

ที่ต้องติ๊ก README เพราะถ้า repo ว่างเปล่าจะยังไม่มี branch `main` ให้แตกกิ่ง

### 1.2 clone ลงเครื่อง

```powershell
cd C:\Users\BTCOM\Desktop
git clone https://github.com/<username>/toktickit.git
cd toktickit
```

### 1.3 สร้าง branch `lab1-staging`

```powershell
git switch main
git pull
git switch -c lab1-staging
git push -u origin lab1-staging
```

`-c` = create branch ใหม่ · `-u` = ผูก branch ในเครื่องกับบนเว็บ (ทำครั้งเดียวต่อ branch)

เช็คว่าได้จริง:

```powershell
git branch -a
```

ต้องเห็น `main`, `lab1-staging`, `remotes/origin/main`, `remotes/origin/lab1-staging`

### 1.4 เพิ่มเพื่อนเป็น Collaborator

repo → **Settings** → เมนูซ้าย **Collaborators** → `Add people` → พิมพ์ GitHub username เพื่อน →
เลือก role `Write`

**ถ้าไม่ทำขั้นนี้เพื่อนกด Approve ไม่ได้** — คนนอกคอมเมนต์ได้ แต่ review แบบมีผลไม่ได้ และ Part 1
ให้ 5 คะแนนกับหลักฐาน approve

เพื่อนต้องเข้าอีเมลกดรับคำเชิญด้วย ไม่งั้นยังไม่มีผล · และมึงต้องได้รับเชิญเข้า repo ของเพื่อน
เหมือนกัน

### 1.5 ตั้ง branch protection (ไม่บังคับ แต่ควรทำ)

Settings → **Rules** → Rulesets → New branch ruleset

- Ruleset name: `protect-main-and-staging`
- Enforcement status: **Active**
- Target branches → Add target → Include by pattern → ใส่ `main` แล้วเพิ่มอีกอันใส่ `lab1-staging`
- ติ๊ก **Require a pull request before merging** → Required approvals = `1`

ผลคือ push ตรงเข้า `main` หรือ `lab1-staging` จะถูกปฏิเสธทันที บังคับให้ผ่าน PR อย่างเดียว
นี่คือของจริงที่บริษัทใช้ และเป็นตาข่ายกันมึงเผลอ

> ถ้าตั้งแล้วติดปัญหาตอน merge (เช่นเพื่อนยังไม่ approve) ปิดชั่วคราวได้ที่ Enforcement status →
> Disabled แต่อย่าลืมเปิดกลับ

**หลักฐานที่ต้องเก็บ:**
- [ ] URL ของ repo
- [ ] แคปหน้า Settings → Collaborators ที่มีชื่อเพื่อน

---

## Phase 2 — Project board + Issues

### 2.1 สร้างบอร์ด

repo → แท็บ **Projects** → `New project` → เลือกเทมเพลต **Board** → ตั้งชื่อ
`TokTickIT Individual Sprints` → Create

### 2.2 แก้คอลัมน์ให้เป็น 6 สถานะ

บอร์ดใหม่มาพร้อม `Todo / In Progress / Done` ต้องแก้ให้ตรง labsheet §6 ข้อ 4 เป๊ะ ๆ

ทางที่เร็วที่สุด: `⋯` มุมขวาบนของบอร์ด → **Settings** → เมนูซ้าย `Status` (อยู่ใต้ Fields)

- เปลี่ยนชื่อ option เดิม 3 อัน และเพิ่มอีก 3 อัน ให้ได้ครบ 6
- **ลากเรียงลำดับให้ถูก** ลำดับใน field = ลำดับคอลัมน์บนบอร์ด

```
Backlog · Specified · Started · PR Review · Fixing · Done
```

### 2.3 เปิด automation ตัวเดียวที่คุ้ม

`⋯` มุมขวาบน → **Workflows** → เลือก `Item closed` → set Status = **Done** → Enable

พอ PR ที่เขียน `Closes #2` ถูก merge Issue จะปิดเองแล้วการ์ดเด้งไป Done ให้ ที่เหลือลากเอง

### 2.4 สร้าง Issue 4 อัน

repo → แท็บ **Issues** → `New issue` · ก๊อป title กับ body จาก [[Lab1_Issue_Drafts]]

**สร้างเรียง 1 → 2 → 3 → 4 ห้ามสลับ** เพราะเลข Issue แจกตามเวลาสร้าง แก้ทีหลังไม่ได้ และชื่อ
branch ที่ labsheet บังคับอ้างเลขนี้

ตอนสร้างแต่ละอัน ที่แถบขวา:

- `Projects` → เลือก `TokTickIT Individual Sprints`
- พอเลือกแล้วจะมีช่อง `Status` โผล่มา → ตั้งเป็น **Backlog**
- `Assignees` → ใส่ตัวเอง

**ห้ามเขียนโค้ดก่อนสร้างครบทั้ง 4 อัน** — labsheet §7 เขียนตรง ๆ ว่า *"Create all four Issues
before implementation begins"* เหตุผลจริงคือมันบังคับให้อ่านสเปกทั้งหมดก่อน จะได้เห็นตั้งแต่ต้นว่า
Issue 4 พึ่ง Issue 3

**หลักฐานที่ต้องเก็บ:**
- [ ] URL ของบอร์ด + URL ของ Issue ทั้ง 4
- [ ] **แคปบอร์ดตอนทุกการ์ดอยู่ Backlog** ← ย้อนถ่ายไม่ได้

---

## Phase 3 — Issue #1 วางโครงโปรเจกต์

Issue นี้ใหญ่ที่สุดและทุกอย่างพึ่งมัน ทำให้เสร็จก่อนแตะอันอื่น

### 3.1 เปิดงาน

**เว็บ:** ลากการ์ด #1 → `Specified` → `Started`

**terminal:**

```powershell
cd C:\Users\BTCOM\Desktop\toktickit
git switch lab1-staging
git pull
git switch -c feature/1-project-foundation
```

> แตกจาก `lab1-staging` ไม่ใช่ `main` — cheat sheet ของอาจารย์เขียนว่า `main` แต่ขัดกับ §12
> ของ labsheet ที่กำหนดให้ทุกอย่างเข้า `main` ผ่าน `lab1-staging`

### 3.2 สร้างโครงโฟลเดอร์ตาม labsheet §8

```powershell
mkdir docs/lab-01
mkdir server/tests/lab-01
mkdir client/tests/lab-01
```

> **ข้อสังเกต:** labsheet §8 วาด `tests/lab-01/` ไว้ใต้ `server/` อย่างเดียว แต่ Part 2 ต้องมีเทสต์
> Vitest ฝั่ง UI ด้วย ซึ่งอยู่ฝั่ง `client/` กูเลยแนะนำให้ทำสองที่แบบสมมาตร (`server/tests/lab-01/`
> กับ `client/tests/lab-01/`) แล้วเขียนรวมไว้ใน `docs/lab-01/tests.md` — ตรงเจตนา Part 2 และ
> ไม่ขัด §8 · ถ้าไม่ชอบให้ถาม TA ก่อน

### 3.3 Frontend — React + TypeScript + Vite + Bootstrap

```powershell
npm create vite@latest client -- --template react-ts
cd client
npm install
npm install bootstrap
```

เปิด `client/src/main.tsx` เพิ่มบรรทัด import Bootstrap **ก่อน** import `index.css`:

```tsx
import 'bootstrap/dist/css/bootstrap.min.css'
```

ทำไมต้องก่อน: CSS ที่มาทีหลังทับตัวก่อนหน้า ถ้าอยากเขียน style ทับ Bootstrap ของเราต้องอยู่ล่าง

ลองรัน:

```powershell
npm run dev
```

เปิด http://localhost:5173 ต้องเห็นหน้า Vite ขึ้น · ปิดด้วย `Ctrl+C`

พิสูจน์ว่า Bootstrap ติดจริง (AC บอกว่า *"visible in the frontend"*) — แก้ `client/src/App.tsx`
ให้เหลือแค่นี้ไปก่อน:

```tsx
export default function App() {
  return (
    <div className="container py-5">
      <h1 className="mb-4">TokTickIT IT Service Desk</h1>
      <button className="btn btn-primary">Check System</button>
    </div>
  )
}
```

ถ้าปุ่มขึ้นเป็นสีน้ำเงินมีขอบมน = Bootstrap ทำงาน แคปหน้าจอเก็บไว้เป็นหลักฐาน AC ข้อนี้

### 3.4 ติดตั้ง Vitest ฝั่ง client

```powershell
npm install -D vitest jsdom @testing-library/react @testing-library/jest-dom @testing-library/user-event
```

สร้าง `client/tests/setup.ts`:

```ts
import '@testing-library/jest-dom'
```

แก้ `client/vite.config.ts`:

```ts
/// <reference types="vitest" />
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './tests/setup.ts',
    include: ['tests/**/*.test.{ts,tsx}'],
  },
})
```

`environment: 'jsdom'` = จำลอง DOM ของเบราว์เซอร์ใน Node เพราะ React ต้องมี `document` ให้ render
ลงไป ส่วน `include` บังคับให้หาเทสต์เฉพาะใน `tests/` ตามโครงที่ labsheet กำหนด

เพิ่ม script ใน `client/package.json`:

```json
"scripts": {
  "dev": "vite",
  "build": "tsc -b && vite build",
  "preview": "vite preview",
  "test": "vitest run"
}
```

### 3.5 Backend — Express + TypeScript

```powershell
cd ..\server
npm init -y
npm install express cors
npm install -D typescript tsx @types/node @types/express @types/cors vitest supertest @types/supertest
npx tsc --init
```

`tsx` = ตัวรัน TypeScript ตรง ๆ โดยไม่ต้อง compile ก่อน ทำให้ dev เร็ว

แก้ `server/tsconfig.json` ให้มีอย่างน้อยนี้:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "rootDir": "./src",
    "outDir": "./dist",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true
  }
}
```

สร้าง `server/src/app.ts`:

```ts
import express from 'express'
import cors from 'cors'

export function createApp() {
  const app = express()
  app.use(cors())
  app.use(express.json())

  app.get('/api/health', (_req, res) => {
    res.status(200).json({ status: 'ok', service: 'TokTickIT API' })
  })

  return app
}
```

สร้าง `server/src/server.ts`:

```ts
import { createApp } from './app'

const port = Number(process.env.PORT) || 3000

createApp().listen(port, () => {
  console.log(`TokTickIT API listening on http://localhost:${port}`)
})
```

> **ทำไมต้องแยก `app.ts` กับ `server.ts`** — นี่คือจุดที่กรรมการชอบถาม<br/>
> `app.ts` สร้าง Express app แต่ไม่เปิดพอร์ต · `server.ts` เป็นตัวเปิดพอร์ตจริง<br/>
> ทำแบบนี้เพราะ **Supertest ต้องการ app ที่ยังไม่ listen** มันจะเปิดพอร์ตชั่วคราวให้เอง
> ถ้ารวมไว้ไฟล์เดียว การ import ในเทสต์จะไปเปิดพอร์ตค้างไว้ แล้วเทสต์จะไม่ยอมจบ

เพิ่ม script ใน `server/package.json`:

```json
"scripts": {
  "dev": "tsx watch src/server.ts",
  "test": "vitest run"
}
```

ลองรัน:

```powershell
npm run dev
```

เปิด http://localhost:3000/api/health ต้องเห็น JSON

> Issue #1 แค่ต้องการให้ backend **start ได้** ส่วน health check เป็นงานของ Issue #2 แต่ใส่
> endpoint ว่าง ๆ ไว้ก่อนเพื่อพิสูจน์ว่าเซิร์ฟเวอร์ทำงานก็ไม่ผิด — เดี๋ยว Issue #2 ค่อยเติมเทสต์
> กับการต่อ UI

### 3.6 PostgreSQL + Prisma

```powershell
npm install @prisma/client
npm install -D prisma
npx prisma init --datasource-provider postgresql
```

จะได้ `server/prisma/schema.prisma` กับ `server/.env`

แก้ `server/.env`:

```
DATABASE_URL="postgresql://postgres:<รหัสที่ตั้งตอนลง PostgreSQL>@localhost:5432/toktickit?schema=public"
PORT=3000
```

สร้าง `server/.env.example` — โครงเดียวกันแต่ไม่มีของจริง:

```
DATABASE_URL="postgresql://USER:PASSWORD@localhost:5432/toktickit?schema=public"
PORT=3000
```

> **นี่คือหัวใจของ AC ข้อ "secrets are not committed"** — `.env` มีรหัสผ่านจริง ห้ามขึ้น Git ·
> `.env.example` คือแบบฟอร์มเปล่าให้คนอื่นรู้ว่าต้องตั้งตัวแปรอะไรบ้าง อันนี้ commit ได้

พิสูจน์ว่าต่อ DB ติด:

```powershell
npx prisma db push
```

ถ้าไม่มี error = PostgreSQL เข้าถึงได้และ Prisma ต่อติด (Prisma จะสร้าง database `toktickit`
ให้เองถ้ายังไม่มี) แคปผลลัพธ์เก็บไว้

### 3.7 `.gitignore`

แก้ `.gitignore` ที่ root ให้มีอย่างน้อยนี้:

```gitignore
node_modules/
dist/
build/
coverage/

.env
.env.local
.env.*.local
!.env.example

*.log
npm-debug.log*
.DS_Store
```

บรรทัด `!.env.example` คือ "ยกเว้นไฟล์นี้ ให้ track" — เครื่องหมาย `!` แปลว่ากลับด้านกฎที่อยู่ข้างบน

เช็คว่ากันได้จริงก่อน commit:

```powershell
git status
```

**ต้องไม่เห็น `node_modules` หรือ `.env` ในรายการ** ถ้าเห็นแปลว่า `.gitignore` ยังไม่ครอบ แก้ก่อน
commit เด็ดขาด (ถ้าหลุดขึ้นไปแล้วลบยากกว่าเยอะ)

### 3.8 `README.md`

AC บอกว่า *"Initial README setup instructions are present"* และ Part 1 ขอ rendered README
เขียนให้คนอื่นเอาไปรันได้จริง:

```markdown
# TokTickIT

IT service desk application — CPE334 Lab 1 vertical slice.
React + TypeScript + Vite + Bootstrap → Express + TypeScript → Prisma → PostgreSQL

## Prerequisites

- Node.js 18+
- PostgreSQL 16+ running on localhost:5432

## Setup

1. Clone and install

   git clone https://github.com/<username>/toktickit.git
   cd toktickit
   cd server && npm install
   cd ../client && npm install

2. Configure the database

   cd server
   cp .env.example .env      # then edit DATABASE_URL with your password
   npx prisma migrate dev
   npx prisma db seed

3. Run both sides in two terminals

   cd server && npm run dev   # http://localhost:3000
   cd client && npm run dev   # http://localhost:5173

## Tests

   cd server && npm test
   cd client && npm test

## API

| Method | Endpoint | Response |
| --- | --- | --- |
| GET | /api/health | { "status": "ok", "service": "TokTickIT API" } |
| GET | /api/categories | [ { "id": 1, "name": "Account and Access" }, ... ] |

## Project structure

Described in the Lab 1 labsheet section 8.
```

### 3.9 commit + push

commit เป็นก้อน ๆ ที่มีความหมาย ไม่ใช่ก้อนเดียวจบ:

```powershell
cd C:\Users\BTCOM\Desktop\toktickit
git add .gitignore
git commit -m "chore: ignore node_modules, build output, and env files"

git add client
git commit -m "chore: scaffold React + TypeScript + Vite client with Bootstrap"

git add server
git commit -m "chore: scaffold Express + TypeScript server with Prisma and PostgreSQL"

git add docs README.md
git commit -m "docs: add README setup instructions and lab-01 docs folder"

git push -u origin feature/1-project-foundation
```

### 3.10 เปิด PR

หลัง push GitHub จะขึ้นแถบเหลือง **Compare & pull request** ในหน้า repo — กดเลย

> **ตรวจช่อง `base:` ให้เป็น `lab1-staging`** GitHub ตั้ง default เป็น `main` ให้เสมอ
> นี่คือจุดที่คนพลาดกันมากที่สุดในแล็บนี้

เขียน body:

```markdown
Closes #1

## What
วางโครงโปรเจกต์ทั้งหมดตาม labsheet §8 · ยังไม่มี business logic

## Acceptance criteria
- [x] React + TypeScript + Vite frontend starts successfully
- [x] Bootstrap is installed and visible in the frontend
- [x] Node.js + Express + TypeScript backend starts successfully
- [x] PostgreSQL is reachable and Prisma is initialized
- [x] Vitest and Supertest commands are configured
- [x] .gitignore and .env.example exist; secrets and node_modules are not committed
- [x] Initial README setup instructions are present

## How to verify
cd server && npm run dev   → http://localhost:3000/api/health
cd client && npm run dev   → http://localhost:5173
```

แถบขวา → `Reviewers` → เลือกเพื่อน<br/>
**เว็บ:** ลากการ์ด → `PR Review`

### 3.11 วนรอบรีวิว

ดูรายละเอียดที่ Phase 4.6 (เหมือนกันทุก Issue) · approve แล้ว → `Merge pull request` →
`Confirm merge` → `Delete branch`<br/>
**เว็บ:** ลากการ์ด → `Done`

```powershell
git switch lab1-staging
git pull
git branch -d feature/1-project-foundation
```

**หลักฐานที่ต้องเก็บ:**
- [ ] URL ของ PR #1
- [ ] แคปหน้าเว็บที่เห็นปุ่ม Bootstrap
- [ ] แคปผล `npx prisma db push` สำเร็จ
- [ ] แคป `git status` ที่ไม่มี `.env` / `node_modules`

---

## Phase 4 — Issue #2 health check

### 4.1 เปิดงาน

**เว็บ:** ลากการ์ด #2 → `Specified` → `Started`

```powershell
git switch lab1-staging
git pull
git switch -c feature/2-health-check
```

### 4.2 ยืนยัน endpoint

`server/src/app.ts` มี `/api/health` อยู่แล้วจาก Phase 3 · เช็คว่าตรงสเปก §10.1 เป๊ะ:

```ts
app.get('/api/health', (_req, res) => {
  res.status(200).json({ status: 'ok', service: 'TokTickIT API' })
})
```

ชื่อ field ต้องเป็น `status` กับ `service` เป๊ะ ๆ ค่าต้องเป็น `ok` กับ `TokTickIT API` เป๊ะ ๆ
เพราะ AC เขียนไว้แบบนั้นและเทสต์จะเช็คตรงตัว

### 4.3 เทสต์ Supertest

สร้าง `server/tests/lab-01/health.test.ts`:

```ts
import { describe, it, expect } from 'vitest'
import request from 'supertest'
import { createApp } from '../../src/app'

describe('API-01 GET /api/health', () => {
  it('returns 200 with the expected service payload', async () => {
    const res = await request(createApp()).get('/api/health')

    expect(res.status).toBe(200)
    expect(res.body).toEqual({ status: 'ok', service: 'TokTickIT API' })
  })
})
```

`request(createApp())` = Supertest รับ Express app เข้าไป เปิดพอร์ตชั่วคราวเอง ยิง request
แล้วปิดให้ — ไม่ต้องรัน `npm run dev` ค้างไว้ตอนเทสต์

รัน:

```powershell
cd server
npm test
```

ต้องเขียว **แคปผลลัพธ์ terminal เก็บไว้** Part 2 ขอหลักฐานนี้

### 4.4 ต่อ UI ให้เรียก API จริง

แก้ `client/src/App.tsx`:

```tsx
import { useState } from 'react'

const API = import.meta.env.VITE_API_URL ?? 'http://localhost:3000'

type SystemState = 'idle' | 'loading' | 'online' | 'offline'

export default function App() {
  const [state, setState] = useState<SystemState>('idle')

  async function checkSystem() {
    setState('loading')
    try {
      const res = await fetch(`${API}/api/health`)
      if (!res.ok) throw new Error(`health returned ${res.status}`)
      const body = await res.json()
      setState(body.status === 'ok' ? 'online' : 'offline')
    } catch {
      setState('offline')
    }
  }

  return (
    <div className="container py-5">
      <h1 className="mb-4">TokTickIT IT Service Desk</h1>

      <button className="btn btn-primary" onClick={checkSystem} disabled={state === 'loading'}>
        Check System
      </button>

      {state === 'loading' && (
        <p className="mt-4" role="status">⏳ Loading…</p>
      )}

      {state === 'online' && (
        <p className="mt-4">System Status: <span className="badge bg-success">Online</span></p>
      )}

      {state === 'offline' && (
        <div className="alert alert-danger mt-4" role="alert">
          System Status: Offline<br />
          Unable to connect to TokTickIT API
        </div>
      )}
    </div>
  )
}
```

สร้าง `client/.env`:

```
VITE_API_URL=http://localhost:3000
```

และ `client/.env.example` เนื้อเดียวกัน · Vite บังคับว่าตัวแปรที่ frontend อ่านได้ต้องขึ้นต้นด้วย
`VITE_` เพื่อกันคนเผลอเอา secret ฝั่งเซิร์ฟเวอร์ไปฝังในไฟล์ JS ที่ส่งให้เบราว์เซอร์

> **ทำไมต้องมี state 4 ค่า** — `idle` คือยังไม่กด, `loading` คือกำลังรอ, อีกสองคือผลลัพธ์<br/>
> ถ้าใช้แค่ boolean `isOnline` มึงจะแยกไม่ออกระหว่าง "ยังไม่ได้เช็ค" กับ "เช็คแล้วพัง" ซึ่ง
> AC บังคับให้มี loading state แยกชัดเจน

### 4.5 ทดสอบด้วยตาก่อนเปิด PR

เปิดสอง terminal:

```powershell
cd server; npm run dev
```

```powershell
cd client; npm run dev
```

กด Check System → ต้องขึ้น Online · จากนั้น **ปิด backend ด้วย `Ctrl+C`** แล้วกดใหม่ →
ต้องขึ้นกล่องแดง Offline · **แคปทั้งสองภาพ** Part 4 ขอทั้ง success case และ failure case

### 4.6 PR + รอบรีวิว (ทำเหมือนกันทุก Issue ตั้งแต่นี้ไป)

```powershell
git add .
git commit -m "feat: add /api/health endpoint with Supertest coverage"
git commit -m "feat: show backend status on the client from a real API call"
git push -u origin feature/2-health-check
```

เปิด PR → **base = `lab1-staging`** → body มี `Closes #2` + acceptance criteria ติ๊กครบ +
วิธี verify → ใส่เพื่อนใน Reviewers<br/>
**เว็บ:** ลากการ์ด → `PR Review`

**ฝั่งเพื่อนรีวิวมึง:**<br/>
เพื่อนเปิด PR → แท็บ `Files changed` → hover เลขบรรทัด → กด `+` สีน้ำเงิน → พิมพ์คอมเมนต์ →
`Start a review` → คอมเมนต์ครบแล้ว `Review changes` มุมขวาบน → `Approve` หรือ `Request changes`
→ Submit

**ถ้าโดน Request changes:**<br/>
**เว็บ:** ลากการ์ด → `Fixing` → ตอบคอมเมนต์ทุกอันในกล่องใต้มัน → แก้โค้ด →

```powershell
git add .
git commit -m "fix: return 503 when the database ping fails"
git push
```

commit ใหม่จะโผล่ใน PR เดิมเองอัตโนมัติ **ห้ามเปิด PR ใหม่** → กด `Re-request review`
(ไอคอนวงกลมลูกศรข้างชื่อเพื่อน) → กด `Resolve conversation` ในคอมเมนต์ที่แก้แล้ว →
**เว็บ:** ลากการ์ดกลับ `PR Review`

**พอ approve:** `Merge pull request` → `Confirm merge` → `Delete branch` →
**เว็บ:** ลากการ์ด → `Done`

```powershell
git switch lab1-staging
git pull
git branch -d feature/2-health-check
```

**หลักฐานที่ต้องเก็บ:**
- [ ] URL PR #2 · แคปคอมเมนต์รีวิวของเพื่อน + คำตอบของมึง
- [ ] แคปผล `npm test` ฝั่ง server
- [ ] แคปหน้าเว็บ Online และ Offline

---

## Phase 5 — Issue #3 Category + seed

### 5.1 เปิดงาน

**เว็บ:** ลากการ์ด #3 → `Specified` → `Started`

```powershell
git switch lab1-staging
git pull
git switch -c feature/3-category-seed
```

### 5.2 เขียน model

แก้ `server/prisma/schema.prisma` เติมท้ายไฟล์:

```prisma
model Category {
  id        Int      @id @default(autoincrement())
  name      String   @unique
  createdAt DateTime @default(now())
}
```

`@unique` ไม่ใช่แค่ของตกแต่ง — มันคือสิ่งที่ทำให้ seed ซ้ำแล้วไม่เกิดข้อมูลซ้ำได้ (AC ข้อ 4)
เพราะฐานข้อมูลจะปฏิเสธชื่อซ้ำเอง และเป็น key ที่ `upsert` ใช้หา record เดิม

### 5.3 สร้าง migration

```powershell
cd server
npx prisma migrate dev --name add_category_model
```

จะได้โฟลเดอร์ `server/prisma/migrations/<timestamp>_add_category_model/migration.sql`
**ต้อง commit ขึ้น Git ด้วย** เพราะ migration คือประวัติการเปลี่ยนโครงสร้าง DB ที่คนอื่นต้องรันตาม
ให้ได้โครงเดียวกัน — AC ข้อ 2 บังคับ

> ต่างจาก `prisma db push` ที่ใช้ตอน Phase 3: `db push` แค่ยัดโครงเข้า DB โดยไม่จดประวัติ
> เหมาะกับตอนลองเล่น · `migrate dev` จดเป็นไฟล์ SQL ให้ตามรอยได้ เหมาะกับของจริง

### 5.4 เขียน seed

สร้าง `server/prisma/seed.ts`:

```ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

const CATEGORIES = ['Account and Access', 'Hardware', 'Software', 'Network']

async function main() {
  for (const name of CATEGORIES) {
    await prisma.category.upsert({
      where: { name },
      update: {},
      create: { name },
    })
  }
  console.log(`Seeded ${CATEGORIES.length} categories`)
}

main()
  .catch((e) => {
    console.error(e)
    process.exit(1)
  })
  .finally(() => prisma.$disconnect())
```

> **ทำไมใช้ `upsert` ไม่ใช่ `create`** — นี่คือ AC ข้อ *"safe to run more than once"*<br/>
> `create` รันซ้ำจะพังเพราะชื่อซ้ำติด `@unique` · `upsert` แปลว่า "ถ้ามีอยู่แล้วไม่ต้องทำอะไร
> (`update: {}`) ถ้าไม่มีค่อยสร้าง" รันกี่รอบก็ได้ผลเหมือนเดิม ศัพท์เรียกว่า **idempotent**
> ซึ่งเป็นคุณสมบัติที่ script ทุกตัวใน production ต้องมี

บอก Prisma ว่าจะรัน seed ยังไง — เพิ่มใน `server/package.json` (นอก `scripts`):

```json
"prisma": {
  "seed": "tsx prisma/seed.ts"
}
```

รัน:

```powershell
npx prisma db seed
npx prisma db seed
```

**รันสองรอบตั้งใจ** เพื่อพิสูจน์ AC ข้อ idempotent · เช็คข้อมูลด้วย GUI:

```powershell
npx prisma studio
```

เปิด http://localhost:5555 → ตาราง Category ต้องมี **4 แถวเท่านั้น** ไม่ใช่ 8 · แคปเก็บไว้

### 5.5 PR + รีวิว

```powershell
git add .
git commit -m "feat: add Category model with unique name and migration"
git commit -m "feat: add idempotent seed for the four IT request categories"
git push -u origin feature/3-category-seed
```

เปิด PR base `lab1-staging` · body `Closes #3` · ทำตามรอบใน Phase 4.6

**หลักฐานที่ต้องเก็บ:**
- [ ] URL PR #3 · คอมเมนต์รีวิว
- [ ] แคป Prisma Studio ที่มี 4 แถว หลังรัน seed สองรอบ

---

## Phase 6 — Issue #4 แสดงรายการ category

> เริ่มได้ต่อเมื่อ #3 merge เข้า `lab1-staging` แล้ว (labsheet §7 ระบุ dependency ไว้)

### 6.1 เปิดงาน

**เว็บ:** ลากการ์ด #4 → `Specified` → `Started`

```powershell
git switch lab1-staging
git pull
git switch -c feature/4-category-list
```

`git pull` ตรงนี้สำคัญมาก ถ้าไม่ดึงจะไม่มี model กับ migration ของ #3 ติดมา แล้วโค้ดจะพัง

### 6.2 เพิ่ม endpoint

แก้ `server/src/app.ts`:

```ts
import express from 'express'
import cors from 'cors'
import { PrismaClient } from '@prisma/client'

export const prisma = new PrismaClient()

export function createApp() {
  const app = express()
  app.use(cors())
  app.use(express.json())

  app.get('/api/health', (_req, res) => {
    res.status(200).json({ status: 'ok', service: 'TokTickIT API' })
  })

  app.get('/api/categories', async (_req, res) => {
    try {
      const categories = await prisma.category.findMany({
        orderBy: { id: 'asc' },
        select: { id: true, name: true },
      })
      res.status(200).json(categories)
    } catch (err) {
      console.error(err)
      res.status(503).json({ error: 'Database unavailable' })
    }
  })

  return app
}
```

- `orderBy: { id: 'asc' }` — AC ข้อ *"predictable order"* ถ้าไม่สั่ง PostgreSQL ไม่รับประกันลำดับ
- `select: { id, name }` — ไม่ส่ง `createdAt` ออกไป เพราะ §10.2 ระบุรูปแบบ response ไว้แค่สอง field
  หลักการคือ **ส่งเท่าที่สัญญาไว้** ไม่ใช่โยน object ทั้งก้อนออกไป
- `try/catch` → 503 — AC ต้องมี error state ที่ใช้งานได้ตอน DB ล่ม

### 6.3 เทสต์ Supertest

สร้าง `server/tests/lab-01/categories.test.ts`:

```ts
import { describe, it, expect } from 'vitest'
import request from 'supertest'
import { createApp } from '../../src/app'

describe('API-02 GET /api/categories', () => {
  it('returns the four seeded categories in id order', async () => {
    const res = await request(createApp()).get('/api/categories')

    expect(res.status).toBe(200)
    expect(res.body).toHaveLength(4)
    expect(res.body.map((c: { name: string }) => c.name)).toEqual([
      'Account and Access',
      'Hardware',
      'Software',
      'Network',
    ])
    expect(res.body[0]).toHaveProperty('id')
  })
})
```

เทสต์นี้ยิง DB จริง เลยต้องรัน seed ก่อน ไม่งั้นแดง

### 6.4 ต่อ UI

แก้ `client/src/App.tsx` ให้เรียกทั้งสอง endpoint:

```tsx
import { useState } from 'react'

const API = import.meta.env.VITE_API_URL ?? 'http://localhost:3000'

type Category = { id: number; name: string }
type SystemState = 'idle' | 'loading' | 'online' | 'offline'

export default function App() {
  const [state, setState] = useState<SystemState>('idle')
  const [categories, setCategories] = useState<Category[]>([])

  async function checkSystem() {
    setState('loading')
    try {
      const health = await fetch(`${API}/api/health`)
      if (!health.ok) throw new Error(`health returned ${health.status}`)

      const list = await fetch(`${API}/api/categories`)
      if (!list.ok) throw new Error(`categories returned ${list.status}`)

      setCategories(await list.json())
      setState('online')
    } catch {
      setCategories([])
      setState('offline')
    }
  }

  return (
    <div className="container py-5">
      <h1 className="mb-4">TokTickIT IT Service Desk</h1>

      <button className="btn btn-primary" onClick={checkSystem} disabled={state === 'loading'}>
        Check System
      </button>

      {state === 'loading' && <p className="mt-4" role="status">⏳ Loading…</p>}

      {state === 'offline' && (
        <div className="alert alert-danger mt-4" role="alert">
          System Status: Offline<br />
          Unable to connect to TokTickIT API
        </div>
      )}

      {state === 'online' && (
        <>
          <p className="mt-4">System Status: <span className="badge bg-success">Online</span></p>
          <h2 className="h5 mt-4">Supported Request Categories</h2>
          <ul className="list-group">
            {categories.map((c) => (
              <li key={c.id} className="list-group-item">{c.name}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  )
}
```

> **จุดที่ต้องอธิบายได้ตอนรีวิว:** ทำไมกดปุ่มแล้วขึ้น Offline ตอน DB ล่ม ทั้งที่ `/api/health`
> ยังตอบ 200 อยู่?<br/>
> เพราะ `checkSystem` เรียกสองเส้นต่อกันใน `try` เดียว พอ `/api/categories` ตอบ 503 มันโยน error
> ลง `catch` → ทั้งหน้าจอกลายเป็น Offline ตรงกับภาพ failure case ใน labsheet Part 4 พอดี<br/>
> ทางเลือกอีกแบบคือให้ `/api/health` ping DB ด้วยแล้วตอบ 503 เอง — ก็ถูกเหมือนกัน แต่ทำให้
> health check ผูกกับ DB ซึ่งขัดหลัก *liveness vs readiness* กูเลยเลือกแบบแรก **เตรียมเหตุผลนี้
> ไว้ตอบถ้าเพื่อนหรืออาจารย์ถาม**

### 6.5 เทสต์ Vitest ฝั่ง UI (3 ตัว)

สร้าง `client/tests/lab-01/App.test.tsx`:

```tsx
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from '../../src/App'

const HEALTH_OK = { status: 'ok', service: 'TokTickIT API' }
const CATEGORIES = [
  { id: 1, name: 'Account and Access' },
  { id: 2, name: 'Hardware' },
  { id: 3, name: 'Software' },
  { id: 4, name: 'Network' },
]

function mockFetch(handler: (url: string) => unknown) {
  vi.stubGlobal('fetch', vi.fn(async (url: string) => {
    const body = handler(url)
    if (body === null) throw new Error('network down')
    return { ok: true, status: 200, json: async () => body }
  }))
}

beforeEach(() => vi.restoreAllMocks())
afterEach(() => vi.unstubAllGlobals())

describe('UI-01 heading', () => {
  it('renders the TokTickIT heading', () => {
    render(<App />)
    expect(screen.getByRole('heading', { name: /TokTickIT IT Service Desk/i })).toBeInTheDocument()
  })
})

describe('UI-02 loading to list', () => {
  it('shows loading then the four categories', async () => {
    mockFetch((url) => (url.includes('health') ? HEALTH_OK : CATEGORIES))
    render(<App />)

    await userEvent.click(screen.getByRole('button', { name: /check system/i }))

    await waitFor(() => expect(screen.getByText('Hardware')).toBeInTheDocument())
    expect(screen.getByText('Account and Access')).toBeInTheDocument()
    expect(screen.getByText('Network')).toBeInTheDocument()
  })
})

describe('UI-03 error state', () => {
  it('shows a useful error message when the API fails', async () => {
    mockFetch(() => null)
    render(<App />)

    await userEvent.click(screen.getByRole('button', { name: /check system/i }))

    await waitFor(() =>
      expect(screen.getByText(/Unable to connect to TokTickIT API/i)).toBeInTheDocument()
    )
  })
})
```

> **ทำไมต้อง mock `fetch`** — เทสต์ UI ต้องรันได้โดยไม่ต้องเปิด backend และไม่ต้องมี DB<br/>
> `vi.stubGlobal('fetch', ...)` = เอาของปลอมไปสวมแทน `fetch` ตัวจริง ทำให้กูควบคุมได้ว่า
> API จะตอบอะไร รวมถึงสั่งให้มัน "พัง" เพื่อเทสต์ error state ซึ่งของจริงทำยากมาก

รัน:

```powershell
cd client
npm test
```

ต้องเขียวทั้ง 3 · แคปเก็บ

### 6.6 PR + รีวิว

```powershell
git add .
git commit -m "feat: add GET /api/categories with Prisma and Supertest coverage"
git commit -m "feat: render the category list with loading and error states"
git commit -m "test: cover heading, loading-to-list, and API failure in the UI"
git push -u origin feature/4-category-list
```

เปิด PR base `lab1-staging` · `Closes #4` · ทำตามรอบใน Phase 4.6

**หลักฐานที่ต้องเก็บ:**
- [ ] URL PR #4 · คอมเมนต์รีวิว
- [ ] แคป `npm test` ทั้งฝั่ง server และ client
- [ ] แคปหน้าเว็บสำเร็จ (มี 4 category) และหน้าเว็บ error

---

## Phase 7 — เอกสาร 4 ไฟล์

เอกสารพวกนี้ต้องทำ**ท้ายสุด**เพราะมันอ้างถึง PR ที่เพิ่งเกิด · เปิดอีก branch หนึ่ง

```powershell
git switch lab1-staging
git pull
git switch -c feature/5-lab1-docs
```

> labsheet บังคับ 4 feature branch สำหรับ 4 Issue แต่ไม่ได้ห้ามมีเพิ่ม การเปิด branch ที่ 5
> สำหรับเอกสารดีกว่าการ commit ตรงเข้า `lab1-staging` ซึ่งผิดกฎ §12 ชัด ๆ

### 7.1 `docs/lab-01/tests.md`

Part 2 ขอตารางนี้แบบ rendered:

```markdown
# Lab 1 — Test Inventory

รันทั้งหมด: `cd server && npm test` และ `cd client && npm test`

| Test ID | Test File | Tool | Test Description |
| --- | --- | --- | --- |
| API-01 | server/tests/lab-01/health.test.ts | Supertest | Health endpoint returns 200 and expected JSON |
| API-02 | server/tests/lab-01/categories.test.ts | Supertest | Categories endpoint returns the four seeded categories |
| UI-01 | client/tests/lab-01/App.test.tsx | Vitest | TokTickIT heading renders |
| UI-02 | client/tests/lab-01/App.test.tsx | Vitest | Loading state changes to category list |
| UI-03 | client/tests/lab-01/App.test.tsx | Vitest | API failure displays a useful error message |

## Result

<วางผล terminal ที่เขียวทั้งหมดตรงนี้>
```

### 7.2 `docs/lab-01/reviewer.md`

```markdown
# Lab 1 — Peer Review

## My reviewer

| Field | Value |
| --- | --- |
| Name | ... |
| Student ID | ... |
| GitHub username | @... |

## PRs my reviewer reviewed and approved for me

| PR | Title | Link |
| --- | --- | --- |
| #5 | Set up the TokTickIT project foundation | https://github.com/.../pull/5 |
| #6 | Implement the API health check | ... |
| #7 | Create and seed IT request categories | ... |
| #8 | Display the IT request category list | ... |

### Review comment I received and how I responded

> **Reviewer:** <ก๊อปคอมเมนต์จริงของเพื่อนมาวาง>

**My response:** <ก๊อปคำตอบจริงของมึงมาวาง> แก้ใน commit `abc1234`

## PRs I reviewed for my partner

| PR | Title | Link | Verdict |
| --- | --- | --- | --- |
| ... | ... | ... | Approved |

### Review comment I gave and how my partner responded

> **Me:** <คอมเมนต์จริงที่มึงให้>

**Partner's response:** <คำตอบจริงของเพื่อน>
```

> สังเกตเลข PR เริ่มที่ `#5` เพราะ Issue กินเลข `#1`–`#4` ไปแล้ว — เลขชุดเดียวกัน

### 7.3 `docs/lab-01/ai_use.md`

Part 3 ขอ 6–10 prompt พร้อม reflection · **เขียนจาก prompt ที่ใช้จริง** ไม่ใช่แต่งขึ้น

```markdown
# Lab 1 — AI Use and Reflection

I used <ชื่อ IDE / agent> with <ชื่อโมเดล> at thinking level <...>.

## Selected key prompts

| Prompt Name | Actual Prompt Text | My Reflection |
| --- | --- | --- |
| Plan Lab 1 | ... | ... |
| Set up full-stack project | ... | ... |
| Implement health check | ... | ... |
| Create category model and seed | ... | ... |
| Build category list UI | ... | ... |
| Write Vitest UI tests | ... | ... |
| Review final work against acceptance criteria | ... | ... |

## Reflection on improving my prompts

<2–3 ย่อหน้า: prompt ไหนได้ผลรอบเดียว อันไหนต้องตามแก้ อะไรที่ทำให้ prompt ดีขึ้น
เช่น ใส่ constraint ชัด ๆ / แปะ acceptance criteria ไปด้วย / สั่งทีละงานเล็ก>
```

**เก็บ prompt ตั้งแต่ Phase 3** อย่ามานั่งนึกย้อนตอนนี้ — เปิดไฟล์นี้ทิ้งไว้แล้วก๊อป prompt
ใส่ทันทีที่ใช้

### 7.4 เช็ค `README.md` อีกรอบ

อ่านทวนว่าคนที่ไม่เคยเห็นโปรเจกต์นี้ทำตามแล้วรันได้จริงไหม — ลองทำตามเองแบบสมมติว่าเป็นคนอื่น

### 7.5 PR

```powershell
git add docs README.md
git commit -m "docs: add lab-01 test inventory, reviewer record, and AI use report"
git push -u origin feature/5-lab1-docs
```

เปิด PR base `lab1-staging` → ให้เพื่อน approve → merge

---

## Phase 8 — Release เข้า main

### 8.1 ตรวจก่อนปล่อย

```powershell
git switch lab1-staging
git pull

cd server
npm test
cd ..\client
npm test
```

**ทุกอย่างต้องเขียวก่อน** ถ้าแดงห้ามเปิด release PR — กลับไปเปิด branch แก้ก่อน

### 8.2 เปิด release PR

**เว็บ:** แท็บ Pull requests → `New pull request`

- `base:` **`main`**
- `compare:` **`lab1-staging`**
- Title: `Lab 1 release`
- Body: สรุปว่ามีอะไรบ้าง + ลิงก์ Issue ทั้ง 4

ให้เพื่อน approve → `Merge pull request` → **ห้ามกด Delete branch** เพราะ `lab1-staging`
ต้องเก็บไว้เป็นหลักฐานและใช้ต่อ

### 8.3 ดูกราฟประวัติ

```powershell
git switch main
git pull
git log --oneline --graph --all
```

ต้องเห็นเส้นแตกเป็นกิ่ง ๆ แล้วบรรจบกลับ — นี่คือภาพที่ Part 1 ขอ<br/>
ดูบนเว็บสวยกว่า: repo → `Insights` → `Network`

**หลักฐานที่ต้องเก็บ:**
- [ ] URL release PR
- [ ] แคป `git log --oneline --graph --all` หรือหน้า Insights → Network
- [ ] แคปผลเทสต์เขียวทั้งหมดบน `main`

---

## Phase 9 — ทำ PDF ส่ง

### 9.1 เก็บหลักฐานที่เหลือ

- [ ] แคปบอร์ด Kanban ตอนการ์ดกระจายหลายคอลัมน์ (ควรมีจาก Phase 4–6)
- [ ] แคปบอร์ดตอนจบ 4 การ์ดอยู่ `Done` ครบ
- [ ] แคปโครงสร้างโฟลเดอร์ใน IDE — ต้องเห็น `docs/lab-01/tests.md`, `reviewer.md`, `ai_use.md`,
      `README.md`, และไฟล์เทสต์ใน `tests/lab-01/`
- [ ] `README.md` แบบ rendered (เปิดบน GitHub แล้วแคป)
- [ ] เนื้อ `.gitignore`
- [ ] หน้า PR ที่มีป้ายเขียว *"approved"*

### 9.2 ประกอบ PDF ตามฟอร์มบังคับ

labsheet §14 บังคับหัวข้อ 4 อันนี้เป๊ะ ๆ **ห้ามเปลี่ยน**

```
Answer Part 1:
Answer Part 2:
Answer Part 3:
Answer Part 4:
```

| Part | คะแนน | ใส่อะไร |
| --- | --- | --- |
| 1 | 15 | ลิสต์ URL ทั้งหมด · แคปบอร์ด · แคปกราฟ commit · แคปโครงสร้าง · README + .gitignore · หลักฐานรีวิวสองทาง + reviewer.md |
| 2 | 10 | แคปผลเทสต์เขียวบน `main` · `tests.md` แบบ rendered |
| 3 | 5 | `ai_use.md` แบบ rendered — โมเดลที่ใช้ + ตาราง prompt 6–10 อัน + reflection |
| 4 | 10 | แคปหน้าเว็บ 3 ภาพ: ก่อนกดปุ่ม / success มี 4 category / failure ตอน DB ปิด |

> **เขียนให้สั้นและตรง** labsheet เตือนไว้ว่า *"Unnecessarily long responses may receive a penalty"*
> ให้ภาพหลักฐานพูดแทน อย่าเขียนบรรยายยืดยาว

### 9.3 เช็คก่อนส่ง

- [ ] ส่ง PDF **ไฟล์เดียว** เท่านั้น
- [ ] หัวข้อ Part 1–4 ครบและสะกดตามฟอร์ม
- [ ] ลิงก์ทุกอันกดได้จริง — ลองกดเองทุกลิงก์
- [ ] repo เป็น Private แต่ **อาจารย์กับ TA เข้าได้ไหม** ถ้าไม่แน่ใจให้เพิ่มเป็น Collaborator
      หรือถาม TA ว่าต้องการให้เปิด Public
- [ ] `.env` **ไม่**อยู่ใน repo — เช็คซ้ำที่ github ว่ามองไม่เห็นไฟล์นี้

---

## Definition of Done ต่อ 1 Issue (ใช้เช็คทุกรอบ)

- [ ] acceptance criteria ครบทุกข้อ ติ๊กแล้วใน Issue
- [ ] เทสต์ที่เกี่ยวข้องเขียว
- [ ] PR base เป็น `lab1-staging` และมี `Closes #N`
- [ ] เพื่อน approve แล้ว **จริง ๆ** ไม่ใช่แค่คอมเมนต์
- [ ] merge เข้า `lab1-staging` แล้ว
- [ ] การ์ดอยู่ `Done`
- [ ] แคปหลักฐานเก็บแล้ว
- [ ] **อธิบายโค้ดทุกบรรทัดที่ส่งได้** — labsheet §13: *"Do not submit code you cannot explain"*

---

## กับดักที่ทำให้เสียคะแนนบ่อยที่สุด

| กับดัก | ป้องกันยังไง |
| --- | --- |
| PR base เป็น `main` | ตรวจช่อง base ทุกครั้งก่อนกด Create |
| ลืมแคปบอร์ดระหว่างทาง | แคปทุกครั้งที่ลากการ์ด ใช้เวลา 2 วินาที |
| `.env` หลุดขึ้น Git | `git status` ก่อน commit ทุกครั้ง |
| เพื่อนคอมเมนต์ว่า `lgtm` เฉย ๆ | ตกลงกันตั้งแต่ Phase 0 ว่าต้องคอมเมนต์ที่โค้ดจริงอย่างน้อย 1 จุดต่อ PR |
| commit ก้อนเดียว "update files" | commit ทีละงาน ใช้ prefix `feat:` `fix:` `test:` `docs:` `chore:` |
| สร้าง Issue สลับลำดับ | สร้าง 1→2→3→4 รวดเดียว |
| ทำเสร็จแล้วค่อยมาจัดบอร์ดให้สวย | ลากการ์ดทันทีที่เกิดเหตุการณ์จริง |
| นึก prompt ย้อนหลังไม่ออก | เปิด `ai_use.md` ทิ้งไว้ ก๊อป prompt ใส่ทันที |
