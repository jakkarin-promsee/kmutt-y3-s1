# Lab 1 — ร่างเนื้อ GitHub Issue ทั้ง 4 อัน

ก๊อปวางตอนกด **New issue** ใน repo `toktickit` · เนื้อหา acceptance criteria ลอกจาก
[[Lab1_Labsheet.pdf|labsheet]] §7 แบบคำต่อคำ เพราะกรรมการเทียบกับ labsheet ตอนตรวจ

ทุกอันตอนสร้าง: แถบขวา → `Projects` → เลือก `TokTickIT Individual Sprints` → `Status` = **Backlog**<br/>
ขั้นตอนที่เหลือดูที่ [[Git_GitHub_Workflow_Playbook]]

> ต้องสร้างครบทั้ง 4 อัน **ก่อน** เริ่มเขียนโค้ด (labsheet §7) และเลข `#1`–`#4` ที่ได้ต้องเรียงตามนี้
> เพราะชื่อ branch ที่ labsheet บังคับอ้างอิงเลขนี้ — สร้างสลับลำดับแล้วเลขจะเพี้ยน

---

## Issue 1

**Title**

```
Set up the TokTickIT project foundation
```

**Body**

```markdown
Type: Technical setup
Branch: `feature/1-project-foundation`
Target: `lab1-staging`

## Acceptance criteria
- [ ] React + TypeScript + Vite frontend starts successfully
- [ ] Bootstrap is installed and visible in the frontend
- [ ] Node.js + Express + TypeScript backend starts successfully
- [ ] PostgreSQL is reachable and Prisma is initialized
- [ ] Vitest and Supertest commands are configured
- [ ] `.gitignore` and `.env.example` exist; secrets and `node_modules` are not committed
- [ ] Initial README setup instructions are present

## Notes
Blocks every other issue — must be merged into `lab1-staging` first.
```

---

## Issue 2

**Title**

```
Implement the API health check
```

**Body**

```markdown
Type: Feature
Branch: `feature/2-health-check`
Target: `lab1-staging`
Depends on: #1

## Acceptance criteria
- [ ] `GET /api/health` returns HTTP 200
- [ ] The JSON response contains `status = ok` and `service = TokTickIT API`
- [ ] A Supertest test verifies the endpoint
- [ ] The React page displays the backend status based on a real API call
- [ ] A useful error message appears when the backend is unavailable

## Expected response
GET /api/health → 200 OK
{ "status": "ok", "service": "TokTickIT API" }
```

---

## Issue 3

**Title**

```
Create and seed IT request categories
```

**Body**

```markdown
Type: Database preparation
Branch: `feature/3-category-seed`
Target: `lab1-staging`
Depends on: #1

## Acceptance criteria
- [ ] A Prisma `Category` model exists with `id`, unique `name`, and `createdAt`
- [ ] A migration creates the `Category` table
- [ ] The seed inserts Account and Access, Hardware, Software, and Network
- [ ] The seed is safe to run more than once without duplicates
- [ ] Database credentials are not committed

## Model
model Category {
  id        Int      @id @default(autoincrement())
  name      String   @unique
  createdAt DateTime @default(now())
}
```

---

## Issue 4

**Title**

```
Display the IT request category list
```

**Body**

```markdown
Type: Feature
Branch: `feature/4-category-list`
Target: `lab1-staging`
Depends on: #3 (must already be merged into `lab1-staging`)

## Acceptance criteria
- [ ] `GET /api/categories` retrieves categories from PostgreSQL through Prisma
- [ ] The API returns each category ID and name in a predictable order
- [ ] A Supertest test verifies the response
- [ ] React displays the categories returned by the API, not hard-coded values
- [ ] Loading and error states are shown
- [ ] A Vitest test verifies the category-list UI behavior

## Expected response
GET /api/categories → 200 OK
[
  { "id": 1, "name": "Account and Access" },
  { "id": 2, "name": "Hardware" },
  { "id": 3, "name": "Software" },
  { "id": 4, "name": "Network" }
]
```

---

## Label ที่ควรสร้าง (ไม่บังคับ แต่ทำให้บอร์ดอ่านง่าย)

repo → Issues → เมนูซ้าย `Labels` → New label

| Label | สี | ใช้กับ |
| --- | --- | --- |
| `setup` | เทา | Issue 1 |
| `feature` | ฟ้า | Issue 2, 4 |
| `database` | ม่วง | Issue 3 |

---

## ลำดับที่ทำได้ (labsheet §7)

```
#1 foundation
   ├── #2 health check      ← ทำพร้อม #3 ได้
   └── #3 category seed
          └── #4 category list   ← เริ่มได้ต่อเมื่อ #3 merge เข้า lab1-staging แล้ว
```

labsheet เขียนว่า "Issue 4 starts only after Issue 3 is available in **dev**" — คำว่า `dev` ตรงนั้น
หมายถึง `lab1-staging` (ตาราง §12 ระบุ target ของทุก PR เป็น `lab1-staging`) เป็นชื่อที่หลุดมาจาก
Git Flow มาตรฐาน
