# Git & GitHub Workflow Playbook

คู่มือของกู เขียนไว้ใช้ตอนทำ [[Lab1_Labsheet.pdf|Lab 1]] แต่ workflow ทั้งหมดนี้คือของจริงที่ทีม
ซอฟต์แวร์ใช้กัน ไม่ใช่ของปลอมสำหรับนักเรียน — เลยเก็บไว้ที่ `note/` ไม่ใช่ `assignment/`

ตารางคำสั่งย่อ ๆ ดูที่ [[Lab1_Git_GitHub_CheatSheet.pdf|cheat sheet ของอาจารย์]] ได้เลย<br/>
ไฟล์นี้เน้น **ลำดับขั้นตอน + ทำตรงไหน (terminal / เว็บ) + ทำไม**

---

## §0 — โมเดลความคิดที่ต้องมีก่อน

### Git ≠ GitHub

| | Git | GitHub |
| --- | --- | --- |
| คืออะไร | โปรแกรมบันทึกประวัติไฟล์ ทำงานในเครื่อง | เว็บที่เก็บสำเนา repo + เครื่องมือทำงานร่วมกัน |
| ใช้ยังไง | คำสั่งใน terminal (`git ...`) | คลิกในเว็บ (หรือ `gh ...`) |
| ทำงานตอนออฟไลน์ | ได้ | ไม่ได้ |
| มีอะไร | commit, branch, merge | Issues, Pull Request, Review, Projects, Actions |

**Pull Request ไม่ใช่คำสั่งของ Git** — มันเป็นฟีเจอร์ของ GitHub ล้วน ๆ ในเครื่องมึงมีแค่ branch กับ
merge เท่านั้น ส่วน PR คือ "ใบคำร้องขอ merge + กระทู้คุยกัน + ประตูให้คนอื่นอนุมัติ" ที่ GitHub
สร้างครอบไว้ข้างบน

### ไฟล์หนึ่งไฟล์อยู่ได้ 4 ที่

```
[1] Working Directory  ไฟล์จริงที่มึงแก้อยู่ในเครื่อง
      │  git add
      ▼
[2] Staging Area       ตะกร้าที่เลือกไว้ว่า "commit หน้าจะเอาอันนี้"
      │  git commit
      ▼
[3] Local Repository   ประวัติในเครื่อง (.git) — ยังไม่มีใครเห็น
      │  git push          ▲
      ▼                    │ git pull
[4] Remote (GitHub)    ประวัติบนเว็บ — คนอื่นเห็นตรงนี้
```

ทุกคำสั่งที่งงกันบ่อยคือแค่ "ย้ายของระหว่าง 4 ช่องนี้" เช่น `git restore --staged <file>` = เอาออก
จากช่อง 2 กลับไปช่อง 1 — ไม่ได้ลบงาน

**สำคัญ:** commit แล้วยัง**ไม่**ขึ้นเว็บ ต้อง `push` ก่อน หลายคนงงตรงนี้

### Branch คืออะไรจริง ๆ

Branch **ไม่ใช่** สำเนาโฟลเดอร์ มันคือ **ป้ายชื่อที่ชี้ไปที่ commit หนึ่งอัน** และเลื่อนตามเมื่อ
commit ใหม่ ทำให้สร้าง branch แทบไม่กินอะไรเลย — สร้างทิ้งสร้างขว้างได้

`git switch <branch>` = สั่งให้ Git เปลี่ยนไฟล์ในโฟลเดอร์ให้ตรงกับสภาพของ branch นั้น ไฟล์
ในโฟลเดอร์เดียวกันเป๊ะ ๆ เลย ไม่ได้แยกโฟลเดอร์

### ทำไมต้องมี branch (เหตุผลจริงในอุตสาหกรรม)

1. **`main` ต้องพังไม่ได้** — เป็นตัวที่ deploy ขึ้น production คนแก้ของพังใส่ตรง ๆ ไม่ได้
2. **ทำงานขนานกันได้** — 5 คนทำ 5 ฟีเจอร์พร้อมกันโดยไม่เหยียบกัน
3. **มีประตูให้ตรวจ** — โค้ดจะเข้า `main` ได้ต้องผ่านสายตาคนอื่นก่อน (นี่คือหัวใจของ PR)
4. **ย้อนได้เป็นก้อน** — ฟีเจอร์พัง ก็ย้อน merge commit อันเดียว ไม่ต้องไล่แกะทีละบรรทัด

---

## §1 — โมเดล branch ของ Lab 1

```
main                        ← ตัวจริง เสถียร ห้าม commit ตรง
└── lab1-staging            ← ที่รวมงานของ Lab 1 ห้าม commit ตรงเหมือนกัน
      ├── feature/1-project-foundation
      ├── feature/2-health-check
      ├── feature/3-category-seed
      └── feature/4-category-list
```

กติกา: งานทั้งหมดเกิดบน `feature/*` → PR เข้า `lab1-staging` → ครบ 4 อันแล้วเปิด PR ใหญ่
อันเดียวจาก `lab1-staging` → `main`

**ลำดับที่ทำได้** (labsheet §7): Issue 1 ต้องเสร็จก่อน → แล้ว Issue 2 กับ 3 ทำพร้อมกันได้ →
Issue 4 เริ่มได้ต่อเมื่อ Issue 3 merge เข้า staging แล้ว

---

## §2 — Setup ครั้งเดียวจบ (terminal)

```bash
git --version
git config --global user.name "ชื่อจริงของกู"
git config --global user.email "อีเมลที่ผูกกับบัญชี GitHub"
```

> **จุดพลาดที่กัดตอนส่งงาน:** GitHub จับคู่ commit กับบัญชีด้วย **อีเมล** ถ้าอีเมลใน `git config`
> ไม่ตรงกับที่ verify ไว้ในบัญชี GitHub commit จะขึ้นเป็นคนแปลกหน้าไม่มีรูปโปรไฟล์ — แล้ว
> "หลักฐาน commit history" ใน Part 1 จะดูเหมือนไม่ใช่งานของกู เช็คที่
> [github.com/settings/emails](https://github.com/settings/emails)

**GitHub CLI (`gh`)** — cheat sheet ใช้ `gh` เยอะ แต่มันไม่ได้ติดมากับ Git ต้องลงเอง:

```bash
winget install --id GitHub.cli
```

ปิดเปิด terminal ใหม่ แล้ว `gh auth login` → เลือก GitHub.com → HTTPS → Login with a web browser<br/>
ไม่อยากลงก็ได้ ทุกอย่างทำผ่านเว็บได้หมด แค่ช้ากว่า

**รหัสผ่าน GitHub ใช้ push ไม่ได้แล้ว** ตั้งแต่ปี 2021 ต้องใช้ `gh auth login` หรือ Personal Access
Token (Settings → Developer settings → Personal access tokens) เอา token มาวางตอนที่มันถามหา
password

---

## §3 — สร้าง repo + branch โครง

> **อย่าสร้างโปรเจกต์ไว้ในวอลต์นี้** — `1_Uni` เป็น Git repo อยู่แล้ว ถ้าเอา `toktickit/`
> ไปวางข้างในจะกลายเป็น repo ซ้อน repo แล้ว [[save-checkpoint.py]] จะไปยุ่งกับมัน<br/>
> วางไว้นอกวอลต์ เช่น `C:\Users\BTCOM\Desktop\toktickit`

**บนเว็บ:** github.com → ปุ่ม `+` มุมขวาบน → New repository<br/>
ชื่อ `toktickit` · Private · **ติ๊ก Add a README file** (ถ้าไม่ติ๊ก repo จะว่างเปล่าและยังไม่มี
branch `main` ให้แตกกิ่ง) → Create repository

**ใน terminal:**

```bash
cd C:\Users\BTCOM\Desktop
git clone https://github.com/<username>/toktickit.git
cd toktickit
git switch main
git pull
git switch -c lab1-staging
git push -u origin lab1-staging
```

`-c` = create · `-u` = ผูก branch ในเครื่องเข้ากับ branch บนเว็บ ทำครั้งเดียวต่อ branch หลังจากนั้น
`git push` เฉย ๆ พอ

**บนเว็บ — เพิ่มเพื่อนเป็น Collaborator:** repo → Settings → Collaborators → Add people →
ใส่ username เพื่อน<br/>
ถ้าไม่ทำขั้นนี้ เพื่อนกด **Approve** ไม่ได้ (คนนอกรีวิวได้แต่ approve แบบมีผลไม่ได้) — และ Part 1
ให้คะแนน 5 คะแนนกับหลักฐานว่าเพื่อน approve

**บนเว็บ — กันตัวเองพลาด (ไม่บังคับ แต่ควรทำ):** Settings → Rules → Rulesets → New branch ruleset
→ ใส่ `main` และ `lab1-staging` → เปิด *Require a pull request before merging*<br/>
นี่คือของจริงที่บริษัทใช้ ทำให้ push ตรงเข้า `main` ไม่ได้เลยแม้จะอยากทำ

---

## §4 — Issues + Project board (บนเว็บทั้งหมด)

### Issue มีไว้ทำอะไร

Issue = **หน่วยงาน 1 ชิ้น** ที่มีเลขถาวรและ URL ถาวร เป็นใบสั่งงานที่มีกระทู้คุยกันในตัว หน้าที่จริง
ของมันคือเป็น **หมุดที่ทุกอย่างผูกเข้าหา**:

```
Issue #2 "Implement the API health check"
   ├── acceptance criteria อยู่ในตัว Issue   ← สเปกว่า "เสร็จ" แปลว่าอะไร
   ├── branch  feature/2-health-check        ← เลข 2 มาจาก Issue
   ├── PR เขียน "Closes #2"                  ← merge แล้ว Issue ปิดเอง
   ├── การ์ดบนบอร์ด                          ← บอกว่าตอนนี้งานอยู่สเตจไหน
   └── commit ที่ push ขึ้น branch นั้น
```

เหตุผลที่วงการทำแบบนี้: อีก 8 เดือนถ้ามีคนถามว่า "โค้ดบรรทัดนี้มีไว้ทำไม" เขาไล่ย้อนได้
`git blame` → commit → PR → Issue → เจอเหตุผลและบทสนทนาตอนตัดสินใจ **โค้ดทุกบรรทัดต้องสาวกลับไป
หาเหตุผลได้** บริษัทใช้ Jira ticket, GitHub ใช้ Issue — แนวคิดเดียวกัน

> **กับดักเรื่องเลข:** Issue กับ PR ใช้เลขชุดเดียวกันใน repo เดียว สร้าง Issue 4 อันได้ `#1`–`#4`
> แล้ว **PR อันแรกจะเป็น `#5`** ไม่ใช่ `#1`

### สร้าง Issue 4 อัน

repo → แท็บ Issues → New issue · ทำครบ 4 อันตาม labsheet §7 **ก่อนเริ่มเขียนโค้ด**

Title ตั้งตามนี้ แล้วในช่อง body วาง acceptance criteria จาก labsheet เป็น checkbox:

```markdown
Type: Feature
Branch: feature/2-health-check

## Acceptance criteria
- [ ] GET /api/health returns HTTP 200
- [ ] JSON response contains status = ok and service = TokTickIT API
- [ ] A Supertest test verifies the endpoint
- [ ] The React page displays backend status from a real API call
- [ ] A useful error message appears when the backend is unavailable
```

Issue จะได้เลข `#1 #2 #3 #4` อัตโนมัติ — เลขนี้เอาไปตั้งชื่อ branch และอ้างใน PR

### บอร์ดอยู่ตรงไหนบนเว็บ

จุดที่ GitHub ออกแบบสับสน — **Project board ไม่ได้อยู่ในหน้า repo** มันอยู่ระดับ**บัญชี** แล้วค่อย
"ผูก" เข้ากับ repo ทีหลัง

| ของ | อยู่ที่ไหน | URL |
| --- | --- | --- |
| Issue | หน้า repo แท็บ `Issues` | `github.com/<user>/toktickit/issues` |
| Project board (การ์ด) | หน้าโปรไฟล์ แท็บ `Projects` | `github.com/users/<user>/projects/1` |
| ทางลัดจาก repo | หน้า repo แท็บ `Projects` | เห็นก็ต่อเมื่อผูกบอร์ดกับ repo แล้ว |

เข้าไปหาบอร์ด: รูปโปรไฟล์มุมขวาบน → `Your profile` → แท็บบนสุด (Overview · Repositories ·
**Projects** · Packages · Stars)

**การ์ด = Issue ตัวเดิม ไม่ใช่สำเนา** ลากการ์ดจาก Started → PR Review คือการไปแก้ฟิลด์ `Status`
ของ Issue นั้น เปิดหน้า Issue ดูตอนนั้นจะเห็น Status เปลี่ยนตาม และคอลัมน์บนบอร์ดก็คือ
"ตัวเลือกของฟิลด์ Status" ที่เอามาเรียงเป็นแถว — เลยเป็นเหตุผลว่าทำไมเพิ่มคอลัมน์ = เพิ่ม option
ของฟิลด์ Status<br/>
บอร์ดไม่ใช่ที่เก็บงาน มันคือ **แว่นมองงาน** ลบบอร์ดทิ้ง Issue ทั้ง 4 ยังอยู่ครบ

เอา Issue ขึ้นบอร์ดได้ 2 ทาง ผลเหมือนกัน:

- **จากบอร์ด** → `+ Add item` ล่างสุดของคอลัมน์ → พิมพ์ `#` → เลือก Issue
- **จากหน้า Issue** → แถบขวามือหัวข้อ `Projects` → ⚙ → เลือกบอร์ด · จากนั้นช่อง `Status`
  จะโผล่ให้ตั้งค่าได้จากหน้า Issue เลย ไม่ต้องเปิดบอร์ด

### สร้าง Project board

`github.com/<user>` → แท็บ Projects → New project → **Board** → ตั้งชื่อ
`TokTickIT Individual Sprints`

Board มาพร้อม Todo / In Progress / Done ต้องแก้ให้เป็น 6 สถานะตาม labsheet เป๊ะ ๆ:
คลิก `⋯` ข้างชื่อคอลัมน์ → Edit details เพื่อเปลี่ยนชื่อ, หรือ `+` ท้ายสุดเพื่อเพิ่มคอลัมน์

```
Backlog · Specified · Started · PR Review · Fixing · Done
```

จากนั้น `+ Add item` → พิมพ์ `#` → เลือก Issue ทั้ง 4 เข้ามา เริ่มที่ **Backlog** ทุกอัน

| สถานะ | ย้ายมาเมื่อไหร่ |
| --- | --- |
| Backlog | เพิ่ง create Issue ยังไม่ได้อ่านละเอียด |
| Specified | อ่านเข้าใจแล้ว พร้อมลงมือ |
| Started | สร้าง feature branch แล้ว กำลังเขียน |
| PR Review | เปิด PR แล้ว เพื่อนกำลังตรวจ |
| Fixing | เพื่อนขอให้แก้ / test ไม่ผ่าน |
| Done | approve + test ผ่าน + merge เข้า staging แล้ว |

**ต้องลากการ์ดเองทุกครั้ง** — GitHub ไม่ย้ายให้อัตโนมัติ (ยกเว้น Done ถ้าตั้ง workflow ไว้) และ
Part 1 ให้คะแนนหลักฐานว่าใช้บอร์ดจริง เลยควรแคปหน้าจอบอร์ดตอนที่การ์ดกระจายอยู่หลายคอลัมน์
เก็บไว้ระหว่างทาง ไม่ใช่แคปตอนจบอย่างเดียว

### การเลื่อนการ์ด = แก้ฟิลด์ Status เฉย ๆ จริงไหม

จริง กลไกมีแค่นั้น ลากการ์ด = เซ็ตค่าฟิลด์ `Status` ไม่มีอะไรวิ่งไปแตะ branch หรือโค้ดเลย —
**และนั่นคือจุดที่คนทำพัง** เพราะมันง่ายจนกลายเป็นของประดับ

กติกาคือ **ห้ามเลื่อนถ้าไม่มีเหตุการณ์จริงรองรับ** (ดูตารางด้านบน) ถ้าการ์ดขึ้น Started แต่ยังไม่มี
branch อยู่จริง บอร์ดก็โกหก แล้วตอนกรรมการเทียบ screenshot บอร์ดกับ commit history มันจะไม่ตรงกัน

เหตุผลที่คอลัมน์ `Fixing` แยกจาก `PR Review`: มันบอกว่า **ลูกบอลอยู่ที่ใคร**<br/>
`PR Review` = อยู่ที่ reviewer · `Fixing` = กลับมาที่ author — ในทีมจริงนี่คือวิธีที่คนรู้ว่าใครต้อง
ขยับต่อโดยไม่ต้องเดินไปถาม

ควรทำควบคู่ ไม่ใช่ลากเฉย ๆ:

- เลื่อนไป **Fixing** → คอมเมนต์ตอบ reviewer ใน PR ด้วย อย่าลากแล้วเงียบ
- เลื่อนไป **Started** → ใส่ตัวเองใน `Assignees` (ในทีมจริง = ประกาศว่าจองงานนี้แล้ว)
- ติ๊ก checkbox acceptance criteria ระหว่างทำ ไม่ใช่ติ๊กรวดเดียวตอนจบ

**Automation ที่เปิดได้:** `⋯` มุมขวาบนของบอร์ด → Workflows → เปิด **Item closed → Done**<br/>
พอ PR ที่เขียน `Closes #2` ถูก merge Issue จะปิดเองและการ์ดเด้งไป Done ให้ · ส่วนสถานะกลาง
(Specified / Started / PR Review / Fixing) ไม่มี automation ที่เชื่อถือได้สำหรับการ์ด Issue
ต้องลากเอง

---

## §5 — ลูปหลัก: ทำ 1 Issue (วนซ้ำ 4 รอบ)

ตัวอย่างนี้ใช้ Issue 2 · ทำเหมือนกันทุกอัน เปลี่ยนแค่เลขกับชื่อ

**1 · เว็บ** — ลากการ์ด Issue 2 จาก Backlog → Specified → Started

**2 · terminal** — แตก branch จากฐานที่ถูกต้อง:

```bash
git switch lab1-staging
git pull
git switch -c feature/2-health-check
```

> cheat sheet ของอาจารย์เขียนว่าให้แตกจาก `main` — ตรงนั้นขัดกับ §12 ของ labsheet ที่บอกว่างาน
> ทุกอย่างเข้า `main` ผ่าน `lab1-staging` **แตกจาก `lab1-staging`** ปลอดภัยกว่า เพราะจะได้ของที่
> merge ไปแล้วติดมาด้วย (เช่น Issue 4 ต้องมี Issue 3 อยู่ก่อน) และลด conflict

**3 · เขียนโค้ด** แล้วดูว่าอะไรเปลี่ยนบ้าง:

```bash
git status
git diff
```

**4 · commit ทีละก้อนที่มีความหมาย** — อย่ารอเขียนเสร็จหมดแล้ว commit ทีเดียว:

```bash
git add .
git commit -m "feat: add GET /api/health endpoint returning service status"
```

รูปแบบ Conventional Commits ที่ใช้กันทั้งวงการ:
`feat:` ฟีเจอร์ใหม่ · `fix:` แก้บั๊ก · `test:` เพิ่ม/แก้เทสต์ · `docs:` เอกสาร ·
`chore:` งานจิปาถะ (ลง dependency, ตั้ง config) · `refactor:` รื้อโค้ดโดยพฤติกรรมเหมือนเดิม

เขียนให้บอก **เหตุผลเชิงวิศวกรรม** ไม่ใช่ `update files` — CLAUDE.md ของวิชานี้ระบุไว้ และมันคือ
สิ่งที่กรรมการ/หัวหน้าทีมอ่านตอนไล่ประวัติ

**5 · push:**

```bash
git push -u origin feature/2-health-check
```

**6 · เปิด PR** — หลัง push GitHub จะขึ้นแถบเหลือง "Compare & pull request" ในหน้า repo กดได้เลย
หรือไปที่แท็บ Pull requests → New pull request

> **จุดพลาดที่คนทำผิดกันเยอะที่สุด:** ช่อง `base:` GitHub ตั้ง `main` ให้เป็นค่าเริ่มต้น
> **ต้องเปลี่ยนเป็น `lab1-staging`** ไม่งั้นฟีเจอร์วิ่งเข้า `main` ตรง ๆ ผิดกติกาข้อใหญ่ที่สุดของแล็บ

หน้าตา PR ที่ควรเขียน:

```markdown
Closes #2

## What
เพิ่ม GET /api/health ที่ Express และต่อหน้า React ให้แสดงสถานะ backend จาก API จริง

## Acceptance criteria
- [x] GET /api/health returns HTTP 200
- [x] JSON contains status = ok, service = TokTickIT API
- [x] Supertest test verifies the endpoint
- [x] React page shows backend status from a real API call
- [x] Useful error message when backend is unavailable

## How to test
cd server && npm test
```

`Closes #2` เป็นคำสั่งพิเศษของ GitHub — พอ PR ถูก merge Issue 2 จะปิดเองและการ์ดเด้งไป Done<br/>
คำที่ใช้ได้: `Closes` `Fixes` `Resolves` + `#เลข`

**7 · ขอให้เพื่อนรีวิว** — ในหน้า PR แถบขวา `Reviewers` → `⚙` → เลือก username เพื่อน<br/>
**เว็บ:** ลากการ์ด Started → **PR Review**

**8 · รอ แล้วแก้ตามที่เพื่อนบอก** (ดู §6)<br/>
ถ้าเพื่อนขอแก้ → **เว็บ:** ลากการ์ดไป **Fixing** → แก้ในเครื่อง → `git add . && git commit && git push`
**บน branch เดิม** commit ใหม่จะโผล่ใน PR เดิมเองอัตโนมัติ ไม่ต้องเปิด PR ใหม่ → กด
`Re-request review` (ไอคอนวงกลมลูกศรข้างชื่อเพื่อน) → ลากการ์ดกลับไป **PR Review**

**9 · merge** (หลัง approve แล้วเท่านั้น) — ปุ่ม `Merge pull request` → `Confirm merge` →
`Delete branch`<br/>
ลบ branch ปลอดภัย ประวัติ commit ยังอยู่ครบใน `lab1-staging`

**10 · เว็บ:** ลากการ์ดไป **Done** (ถ้าใส่ `Closes #2` มันอาจย้ายให้เอง)

**11 · terminal** — เก็บกวาดก่อนขึ้นรอบถัดไป:

```bash
git switch lab1-staging
git pull                                    # ดึงงานที่เพิ่ง merge ลงมา
git branch -d feature/2-health-check        # ลบ branch ในเครื่อง
```

---

## §6 — Peer review ต้องทำทั้งสองทาง

Part 1 ให้ 5 คะแนนกับตรงนี้ ต้องมีหลักฐาน **ทั้งฝั่งที่เพื่อนตรวจกู และฝั่งที่กูตรวจเพื่อน**

### ฝั่งกูเป็นคนตรวจ (reviewer)

1. เพื่อน add กูเป็น Collaborator ใน repo ของเขา
2. ไปหน้า PR ของเพื่อน → แท็บ **Files changed**
3. อ่านโค้ด ชี้จุดที่จะคอมเมนต์: hover ที่เลขบรรทัด → กดไอคอน `+` สีน้ำเงิน → พิมพ์คอมเมนต์ →
   `Start a review` (ไม่ใช่ Add single comment — เพราะ Start a review จะรวบส่งทีเดียว)
4. คอมเมนต์ครบแล้วกด **Review changes** มุมขวาบน → เลือกอย่างใดอย่างหนึ่ง:
   - **Comment** — ความเห็นเฉย ๆ ไม่ตัดสิน
   - **Approve** — ผ่าน merge ได้
   - **Request changes** — ต้องแก้ก่อน (บล็อกการ merge ถ้าตั้ง rule ไว้)
5. → Submit review

**คอมเมนต์ที่ดีเป็นยังไง** — อย่าเขียน `ok` หรือ `lgtm` เปล่า ๆ เพราะกรรมการขอดู "review comment
ที่ให้ไปและเพื่อนตอบว่าอะไร" คอมเมนต์ที่มีน้ำหนักคือชี้ที่โค้ดจริง เช่น:

> `server/src/routes/health.ts:12` — endpoint ตอบ 200 ตลอดแม้ DB ล่ม ถ้า acceptance criteria
> ต้องการให้ UI แสดง error ตอน backend มีปัญหา ตรงนี้ควรลอง query DB แล้วตอบ 503 ไหม

> `client/src/App.tsx:28` — ตอนนี้ error state ใช้ข้อความเดียวกับ loading ทำให้แยกไม่ออกว่า
> ช้าอยู่หรือพังแล้ว

### ฝั่งกูเป็นคนถูกตรวจ (author)

- อ่านทุกคอมเมนต์ **ตอบทุกอัน** ในกล่องใต้คอมเมนต์นั้น ไม่ใช่แค่แก้เงียบ ๆ
- ไม่เห็นด้วยก็เถียงได้ นี่คือส่วนหนึ่งของงาน — แต่ให้เหตุผล
- แก้แล้วตอบว่า "แก้แล้วใน commit `abc1234`" → กด `Resolve conversation`
- push ขึ้น branch เดิม → `Re-request review`

### `docs/lab-01/reviewer.md`

ต้องมีตามที่ labsheet §12 + Part 1 กำหนด:

```markdown
# Peer Reviewer — Lab 1

| | |
| --- | --- |
| Reviewer name | ... |
| Student ID | ... |
| GitHub username | @... |

## PRs my reviewer reviewed for me
- https://github.com/<me>/toktickit/pull/1
- ...

## PRs I reviewed for my reviewer
- https://github.com/<partner>/toktickit/pull/1
- ...
```

---

## §7 — Release เข้า main

พอ 4 ฟีเจอร์ merge เข้า `lab1-staging` ครบ และเทสต์ผ่านหมด:

```bash
git switch lab1-staging
git pull
cd server && npm test        # ต้องผ่านก่อนเปิด PR
```

**เว็บ:** Pull requests → New pull request → `base: main` ← `compare: lab1-staging` → ตั้งชื่อ
`Lab 1 release` → ให้เพื่อน approve → Merge<br/>
PR อันนี้ **อย่าลบ branch `lab1-staging`** ทิ้งหลัง merge เพราะจะใช้เป็นหลักฐานและอ้างอิงต่อ

จบแล้ว `main` มีของครบ ดูประวัติเป็นกราฟ:

```bash
git switch main
git pull
git log --oneline --graph --all
```

ภาพที่ควรเห็นคือเส้นแตกออกเป็น 4 กิ่งแล้วบรรจบกลับ — นั่นคือ "screenshot commit history" ที่
Part 1 ขอ

---

## §8 — เช็คลิสต์หลักฐานที่ต้องเก็บ (Part 1 = 15 คะแนน)

เก็บระหว่างทาง อย่ารอเก็บตอนจบ เพราะบางอย่างย้อนไปแคปไม่ได้แล้ว

- [ ] URL: repo, Project, Issue ทั้ง 4, PR ทั้งหมด (4 feature PR + 1 release PR)
- [ ] แคปบอร์ด Kanban ระหว่างทาง (การ์ดกระจายหลายคอลัมน์) — **ย้อนหลังไม่ได้**
- [ ] แคปบอร์ดตอนจบ ทั้ง 4 การ์ดอยู่ Done
- [ ] แคป `git log --oneline --graph --all` บน `main` เห็นกิ่งรวมกลับ
- [ ] แคปโครงสร้างโฟลเดอร์ใน IDE ให้ตรงกับ labsheet §8
- [ ] `README.md` แบบ rendered + เนื้อหา `.gitignore`
- [ ] แคปคอมเมนต์รีวิวของเพื่อน + คำตอบของกู
- [ ] แคปคอมเมนต์รีวิวที่กูให้เพื่อน + คำตอบของเพื่อน
- [ ] แคปหน้า PR ที่มีป้ายเขียว "approved"
- [ ] `docs/lab-01/reviewer.md` rendered

---

## §9 — พังบ่อย แก้ยังไง

| อาการ | สาเหตุ | ทางแก้ |
| --- | --- | --- |
| เผลอ commit ใส่ `main`/`lab1-staging` | ลืม `git switch -c` | `git switch -c feature/x` (commit ติดมาด้วย) แล้ว `git switch main && git reset --hard origin/main` |
| PR ตั้ง base เป็น `main` ไปแล้ว | ค่า default ของ GitHub | ในหน้า PR กด `Edit` ข้างหัวข้อ → เปลี่ยน base เป็น `lab1-staging` |
| เผลอ push `node_modules/` หรือ `.env` | ไม่มี `.gitignore` ตั้งแต่แรก | เพิ่มใน `.gitignore` แล้ว `git rm -r --cached node_modules .env` → commit → push |
| `Updates were rejected` ตอน push | บน GitHub มี commit ที่เครื่องยังไม่มี | `git pull` แล้ว push ใหม่ |
| merge conflict | สองกิ่งแก้ไฟล์บรรทัดเดียวกัน | ดู §10 |
| เพื่อนกด Approve ไม่ได้ | ยังไม่ได้เป็น Collaborator | Settings → Collaborators → Add people |
| commit ขึ้นชื่อคนอื่น/ไม่มีรูป | อีเมลใน `git config` ไม่ตรงกับบัญชี GitHub | แก้ `git config --global user.email` แล้ว commit ใหม่ |
| แก้ commit message ล่าสุด | | `git commit --amend -m "ข้อความใหม่"` (ถ้า push ไปแล้วต้อง `git push --force-with-lease`) |
| อยากทิ้งงานที่แก้ในไฟล์ | | `git restore <file>` |
| เอาไฟล์ออกจาก staging | | `git restore --staged <file>` |

---

## §10 — Merge conflict

เกิดตอนที่ branch ของกูกับ `lab1-staging` แก้ไฟล์เดียวกันบรรทัดเดียวกัน Git ตัดสินใจแทนไม่ได้
เลยโยนให้คนตัดสิน — **ไม่ใช่ error ไม่ใช่ความผิดพลาด** เป็นเรื่องปกติมาก

```bash
git switch feature/4-category-list
git pull origin lab1-staging
```

Git จะใส่เครื่องหมายลงไปในไฟล์:

```
<<<<<<< HEAD
โค้ดฝั่งกู (branch ปัจจุบัน)
=======
โค้ดจาก lab1-staging
>>>>>>> lab1-staging
```

แก้ไฟล์ให้เหลือโค้ดที่ถูกต้อง — ลบบรรทัด `<<<<<<<` `=======` `>>>>>>>` ออกให้หมด บางทีคำตอบคือ
เอาทั้งสองฝั่ง ไม่ใช่เลือกข้างเดียว จากนั้น:

```bash
git add .
git commit -m "merge: resolve conflicts with lab1-staging"
git push
```

VS Code มีปุ่ม Accept Current / Accept Incoming / Accept Both ให้กดแทนการลบมือได้ แต่ต้องอ่านก่อนกด

---

## §11 — โปรเจกต์จริงต่างจากแล็บตรงไหน

แล็บนี้คือของจริงแบบย่อ ของที่เพิ่มเข้ามาในบริษัท:

| เพิ่มมา | คืออะไร |
| --- | --- |
| `develop` แทน `lab<N>-staging` | ชื่อต่างกัน หน้าที่เหมือนกันเป๊ะ (Git Flow) · บางทีมีข้าม staging ไปเลย ใช้ trunk-based |
| Branch protection | บังคับด้วยระบบว่าต้องมี PR + approve กี่คน + CI เขียวก่อน merge |
| CI (GitHub Actions) | เปิด PR ปุ๊บ รันเทสต์ + lint + build อัตโนมัติ ไม่ต้องเชื่อคำว่า "เครื่องผมรันผ่าน" |
| CODEOWNERS | ไฟล์กำหนดว่าโฟลเดอร์ไหนใครต้องรีวิว GitHub ใส่ reviewer ให้เอง |
| Squash merge | ยุบ commit ยิบย่อยของ branch ให้เหลืออันเดียวตอน merge ประวัติ `main` สะอาด |
| Release tag | `git tag v1.0.0` ปักหมุดว่าเวอร์ชันไหน deploy ตอนไหน |
| Draft PR | เปิด PR ตั้งแต่ยังทำไม่เสร็จ เพื่อให้ทีมเห็นทิศทางก่อน |
| Environment / secrets | ค่า config ต่อ environment เก็บใน GitHub ไม่ใช่ในโค้ด |

สิ่งที่**เหมือนกันทุกที่** และคือเหตุผลที่วิชานี้บังคับ: ไม่มีใครแตะ `main` ตรง ๆ · งานทุกชิ้นผูกกับ
ticket · โค้ดทุกบรรทัดมีคนที่ไม่ใช่คนเขียนอ่านก่อนเข้า · Definition of Done ไม่ใช่ "โค้ดรันได้"
แต่คือ "รีวิวผ่าน เทสต์ผ่าน merge แล้ว มีหลักฐาน"
