# Lecture 2 — ML (Handwritten Notes, Scanned)

> **Auto-generated transcription notice.** This file is an auto-generated transcription of a
> **scanned, handwritten** document, produced 2026-08-15 by a Sonnet subagent reading the PDF page
> images directly (standard text extraction returns garbage on this file because the pages are
> images, not text). Handwriting is inherently ambiguous — treat this as a best-effort reading, not
> a verified source. **Check the original PDF for anything that matters** (exam prep, submitted
> homework, exact coefficients). Unclear symbols are marked inline with `⟨?⟩` or a bracketed note.

**What this document is:** handwritten derivation notes (not typed slides) working through
**nonlinear least-squares regression** — fitting the exponential model $f(x) = c_0 + c_1 e^{c_2 x}$
by minimizing sum-of-squared-error $S$ via partial derivatives with respect to each parameter — and
then a **gradient-descent training loop** flowchart that operationalizes those derivatives
(randomize parameters → compute $f(x)$ → compute gradient → update parameters by a step-size ×
gradient → repeat until stop). This is consistent with the companion typed deck
[[Lecture+2+-+Training+Models.pdf]] in the same folder (gradient descent / OLS training), and reads
like a lecturer's or student's worked derivation to accompany that deck, rather than a separate
topic.

---

## Page 1

*Layout: a solid red/pink field filling the page, with a single darker-red vertical stripe running
top-to-bottom about four-fifths of the way across. No text, numerals, or diagram lines are visible
anywhere on the page.*

No transcribable content. This does not look like a page of notes at all — it is most likely a
scanning artifact: a colored divider/cover sheet, the underside of a notebook cover, or a colored
plastic sleeve that got scanned along with the real pages. ⟨?⟩ If this recurs across other lecture
PDFs in this folder, it may be worth flagging to the instructor/LEB2 upload rather than treating it
as content.

---

## Page 2

Derivation of the least-squares cost function for the model $f(x) = c_0 + c_1 e^{c_2 x}$ and its
partial derivatives with respect to each of the three parameters $c_0, c_1, c_2$.

*Margin sketch, top right: a small hand-drawn graph with axes labeled $y$ (vertical) and $x$
(horizontal), showing a curve that starts flat near the origin and sweeps upward to the right —
one curve traced in red, a second, similarly-shaped curve dashed alongside it. Read as an
illustration of the exponential curve $f(x) = c_0 + c_1e^{c_2x}$ fit against the data trend (the
dashed curve possibly representing the target/data curve vs. the red fitted curve, or two candidate
fits at different iterations).*

*Margin sketch, right side (next to the $c_0$ derivative line): a small 3-D box/stool-like sketch
with a label that reads like "$x -$" or "$x =$" near it. ⟨?⟩ Too small/ambiguous to confidently
identify — possibly a rough 3-D coordinate box or an unrelated doodle. Not transcribed as math.*

Cost function:

$$f(x) = c_0 + c_1 e^{c_2 x}$$

$$S = \sum (y - f(x))^2$$

$$S = \sum \left(y - c_0 - c_1 e^{c_2 x}\right)^2 \quad \text{[the bracketed term } (y-c_0-c_1e^{c_2x}) \text{ is annotated as } f(x)\text{ underneath — likely marking where } f(x) \text{ substitutes in, or a labeling shorthand]}$$

**Partial derivative w.r.t. $c_0$:**

$$c_0: \quad \frac{\partial S}{\partial c_0} = 2\sum\left(y - c_0 - c_1 e^{c_2 x}\right)(-1)$$

$$= -2\sum\left(y - c_0 - c_1 e^{c_2 x}\right) \quad \text{...(1)}$$

*(the term $(y - c_0 - c_1 e^{c_2x})$ is again labeled $f(x)$ underneath, i.e. this is $-2\sum(y-f(x))$)*

**Partial derivative w.r.t. $c_1$:**

$$c_1: \quad \frac{\partial S}{\partial c_1} = 2\sum\left(y - c_0 - c_1 e^{c_2 x}\right)\left(-e^{c_2 x}\right)$$

$$= -2\sum_i e^{c_2 x_i}\left(y_i - c_0 - c_1 e^{c_2 x_i}\right) \quad \text{...(2)}$$

⟨?⟩ The subscript-$i$ notation in this line is written compactly/ambiguously in the original
(summation with an $i$ subscript threaded through $e^{c_2x}$ and the $y, c_0, c_1e^{c_2x}$ terms
inside the parenthesis). The reading above is the standard form consistent with differentiating
$S=\sum(y_i-c_0-c_1e^{c_2x_i})^2$ term-by-term, but the exact handwritten subscript placement should
be checked against the PDF directly.

**Partial derivative w.r.t. $c_2$:**

$$c_2: \quad \frac{\partial S}{\partial c_2} = 2\sum\left(y - c_0 - c_1 e^{c_2 x}\right)\left(-c_1 x e^{c_2 x}\right) \quad \text{...(3)}$$

*(equations (1)–(3) are underlined together at the bottom of this block, then the page restates the
model once more below the underline:)*

$$f(x) = c_0 + c_1 e^{c_2 x}$$

---

## Page 3

A flowchart of the gradient-descent training loop that uses equations (1)–(3) from Page 2 to
iteratively fit $c_0, c_1, c_2$.

*Original layout: an oval start node at the top, feeding down into a two-part rectangle (upper half
"calculate f(x)", lower half "calculate gradient of current iteration"), feeding down into a large
rectangle labeled "Update" containing the three parameter-update equations, feeding down into a
"Stop?" node that either loops back up to the "calculate f(x)" box (via a line running down the left
side of the diagram) or exits to "End". A separate rounded box sits off to the left, unconnected by
an arrow, defining $\alpha$ = step-size / learning rate. To the right of the gradient box, the partial
derivatives and their short-hand names are noted; a small red mark/arrow (unclear — see note below)
points at the word "Update".*

```
                 ┌────────────────────────────┐
                 │  randomize c0, c1, c2       │   <-- also written beside this node:
                 │      (oval / start node)    │       c0^(0), c1^(0), c2^(0)
                 └──────────────┬─────────────┘
                                │
                                ▼
                 ┌────────────────────────────┐
                 │      calculate f(x)         │◄─────────────────┐
                 ├────────────────────────────┤                   │
                 │  calculate gradient of      │   ✓  ∂S/∂c0, ∂S/∂c1, ∂S/∂c2
                 │     current iteration       │      grad_c0 / grad_c1,
                 └──────────────┬─────────────┘      grad_c2
                                │
                                ▼
                 ┌────────────────────────────┐
                 │           Update            │   <-- small red mark/arrow here, unclear (see note)
                 │                              │
                 │ c0^(t+1) = c0^(t) - step_size × grad_c0
                 │ c1^(t+1) = c1^(t) - step_size × grad_c1
                 │ c2^(t+1) = c2^(t) - step_size × grad_c2
                 └──────────────┬─────────────┘
                                │
                                ▼
                          ┌───────────┐
                          │   Stop?   ├──────────► End
                          └─────┬─────┘
                                │
                                └───────────────────┘  (loop back up to "calculate f(x)")

   ┌───────────────────────────┐
   │  α                        │   (this box floats to the left of the loop,
   │  step-size / learning rate│    not connected to the flow by an arrow —
   └───────────────────────────┘    it just defines the symbol α used above)
```

Node/step list (in flow order):

1. **Randomize $c_0, c_1, c_2$** — initialize parameters, labeled $c_0^{(0)}, c_1^{(0)}, c_2^{(0)}$.
2. **Calculate $f(x)$** — evaluate the model at the current parameter values.
3. **Calculate gradient of current iteration** — compute $\partial S/\partial c_0$,
   $\partial S/\partial c_1$, $\partial S/\partial c_2$ (checked off with a ✓), abbreviated
   `grad_c0`, `grad_c1`, `grad_c2`.
4. **Update** — apply gradient descent:
   - $c_0^{(t+1)} = c_0^{(t)} - \text{step\_size} \times \text{grad\_c0}$
   - $c_1^{(t+1)} = c_1^{(t)} - \text{step\_size} \times \text{grad\_c1}$
   - $c_2^{(t+1)} = c_2^{(t)} - \text{step\_size} \times \text{grad\_c2}$
5. **Stop?** — if not satisfied, loop back to step 2 ("calculate f(x)"); if satisfied, proceed to
   **End**.

Side annotation: $\alpha$ = **step-size / learning rate** (the scalar multiplying the gradient in
the update step).

⟨?⟩ The small red mark next to the word "Update" (transcribed above as "small red mark/arrow") is
too small/ambiguous to read confidently — it may be a grading tick, an emphasis arrow, or a stray
mark, not obviously part of the mathematical content. Everything else on this page — the flowchart
structure, the three update equations, and the $\alpha$ definition — is legible with high
confidence.

---

## Overall notes

- **Pages 2 and 3 together form one coherent derivation**: Page 2 derives the three partial
  derivatives of the SSE cost function for the exponential model $f(x)=c_0+c_1e^{c_2x}$; Page 3
  turns those derivatives directly into a gradient-descent training-loop flowchart (`grad_c0`,
  `grad_c1`, `grad_c2` in the flowchart correspond exactly to equations (1), (2), (3) on Page 2).
- **Page 1 has no mathematical content** — treat it as a blank/artifact page, not a missing
  derivation.
