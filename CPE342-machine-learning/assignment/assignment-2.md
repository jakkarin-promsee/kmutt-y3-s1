# Assignment 2 — Training models via iterative approach

> **Auto-generated transcription notice.** Base text extracted with `pdftotext -layout` on
> 2026-08-24, then hand-repaired: the model equation is written in Cambria Math private-use
> codepoints and comes out of `pdftotext` as `������`, and the data figure is an embedded image
> that text extraction drops entirely. Both were read off the PDF page directly and are transcribed
> below. **The dataset itself is not in the PDF** — it lives behind the Google Drive link.

---

King Mongkut's University of Technology Thonburi<br/>
Faculty of Engineering, Department of Computer Engineering

**CPE 342 Machine Learning, 1/2024**

## Assignment 2: Training models via iterative approach (10 points)

**Due: 4 Sep 2024. Please submit your report in PDF to LEB2**

> ⚠️ Printed header and due date are **stale** (reused 1/2024 brief — same pattern as
> [[Assighment-1.pdf]] and the syllabus). Derive the real deadline from the lecture date and
> confirm on LEB2.

### Gradient Descent

The data below can be downloaded from
[this link](https://drive.google.com/open?id=13k4WwdwKGBtaCsqSStr3rWxe2pfpTvbk&usp=drive_fs).

*Figure (embedded image, 567×432 px): a matplotlib scatter plot, x-axis labelled `x` spanning
0 to 5, y-axis labelled `y` spanning about 0.95 to 2.0. Roughly 100 points tracing a decaying
exponential — y starts near 1.97 at x≈0, falls steeply through ≈1.6 at x≈0.4 and ≈1.2 at x≈1.7,
then flattens onto a noisy plateau at y≈1.0 from about x≈2.6 onward. Scatter is tight at small x
and visibly noisier on the plateau.*

Fit the data to the following model,

$$\hat{y} = c_0 + c_1 e^{c_2 x}$$

Perform the following tasks.

**Tasks:**

1. Write the error/loss function. (1 points)
2. Write the gradient of each coefficients. (3 points)
3. Write the update rules. (1 points)
4. Implement the gradient descent using the given data. (4 points)
5. Show the loss value over iterations and the resulting coefficients. (1 points)

---

*PDF metadata: 1 page, A4, author Santitham Prom-on, created 21 Aug 2024 via Acrobat PDFMaker for
Word.*
