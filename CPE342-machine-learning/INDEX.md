# INDEX — CPE342 Machine Learning

Annotated map of this class folder, so an agent (and I) can understand it **without opening every
file**. Update when files are added/renamed/removed. `temp/` is not listed (volatile).

> Filenames use `+` for spaces (downloaded as-is from LEB2). Readable titles are given below.
> Links are Obsidian wiki-links (full syntax and edge cases: the `vault-writing` skill):
> `[[Name.pdf]]` is the source file, `[[Name]]` is its Markdown text cache.

## assignment/

- **[[Assighment-1.pdf]]** — _Assignment 1: Training models_ (1 p). OLS regression on a 10-month
  advertising-budget (X, $thousands) vs. sales (Y, thousands of units) dataset. Three tasks:
  (1) fit a simple linear regression by OLS — intercept, slope, equation of the fitted line;
  (2) interpret slope & intercept in context, and predict sales at a $12,000 budget;
  (3) compute $R^2$ and interpret the goodness of fit. Submit as a **PDF report on LEB2**. Pairs
  directly with [[Lecture+2+-+Training+Models.pdf]].
  _(Text cache: [[Assighment-1]] — plain `pdftotext`; a one-page prose brief with no math to
  mangle.)_
  > ⚠️ **Due date is stale on the handout.** It prints _"CPE 342 … 1/2024"_ and _"Due: 21 August
  > 2024"_ — a reused brief, same pattern as the 1/2025 syllabus. Class meets Friday, Lecture 2 was
  > handed out **Fri 14 Aug 2026**, and the syllabus sets **one-week deadlines** — so the real due
  > date is almost certainly **Fri 21 Aug 2026**. Confirm on LEB2 before relying on it.
  > _(The filename typo "Assighment" is the download's own — renaming it is my call.)_

## lecture/

- **[[CPE342+Syllabus.pdf]]** — _Course syllabus_ (2 pp). Course info (Fri 13:30–17:30, CB2506, 3
  credits), instructor Dr. Boonyarit Changaival, CLOs, grading (Midterm 30 / Final 35 / HW 35),
  grade scale, key references (ISLP 2023; Géron 2019), and class policies (1-week deadlines on
  LEB2, academic integrity). Source of truth for course facts — see
  [[CPE342-machine-learning/CLAUDE|CLAUDE.md]].
  _(Text cache: [[CPE342+Syllabus]] — regenerated 2026-08-04 by a Sonnet subagent reading the
  pages; grading and grade-scale tables come through as real Markdown tables.)_

- **[[Lecture+1+-+Introduction+to+ML.pdf]]** — _Lecture 1: Introduction to ML; Statistical Learning
  concepts; Bayes' Classifier; LDA & QDA_ (83 slides, by Asst. Prof. Dr. Santitham Prom-on).
  _(Text cache: [[Lecture+1+-+Introduction+to+ML]] — full LaTeX transcription via a Sonnet
  subagent, because `pdftotext` can't handle the formulas.)_
  Three sections:
  - **§1 Intro & Statistical Learning** — what ML is / why it matters; AI⊃ML⊃DL; ML timeline;
    supervised vs. unsupervised vs. semi-supervised vs. reinforcement; regression vs.
    classification; `Y = f(X) + ε`, prediction vs. inference; parametric vs. non-parametric;
    explainability–accuracy trade-off; Mitchell's **T / P / E** framing (tasks: classification,
    regression, clustering, transcription, translation, anomaly detection, synthesis); metrics
    (accuracy/precision/recall, R², MAE, MSE); train/test split & **k-fold cross-validation**;
    worked **linear regression** (normal equation `w = (XᵀX)⁻¹Xᵀy`); under/overfitting.
  - **§2 Bayes' Classifier** — assign to most-likely class `argmaxⱼ Pr(Y=j|X=x₀)`; Bayes decision
    boundary; **Bayes' theorem** (derivation, prior/likelihood/posterior); disease-test example
    (base-rate effect); **Bayesian spam filters** (single word, multiple words, k words).
  - **§3 Discriminant Analysis** — linear classification as projection; **LDA** (Gaussian
    class-conditionals, discriminant `δ_k(x)`, parameter estimates `μ̂_k, σ̂², π̂_k`); **QDA**
    (per-class covariance); evaluation recap (confusion matrix, F-measure, **ROC / AUC** with the
    AUC quality table); LDA-in-Python coding-practice links.

- **[[Lecture+2+-+Training+Models.pdf]]** — _Lecture 2: Training Models_ (38 slides, by Asst. Prof.
  Dr. Santitham Prom-on). How parameters actually get fitted — the closed-form route and the
  iterative one. Colab notebook linked on slide 2.
  _(Text cache: [[Lecture+2+-+Training+Models]] — full LaTeX transcription via a Sonnet subagent;
  `pdftotext` renders every formula as `������`, so the cache is the only readable text.)_
  Four sections:
  - **§1 Direct approach — OLS** (slides 3–14): $\hat{y}=\theta_0+\theta_1x_1+\dots+\theta_nx_n$;
    least-squares objective $S=\sum(y_i-\alpha-\beta x_i)^2$, partials set to zero → normal
    equations → Cramer's-rule closed forms; a worked multiple-regression example generalized to the
    pseudoinverse $\mathbf{B}=(\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T\mathbf{Y}$, with a numpy
    `pinv` demo (slide 14 — the deck's only code).
  - **§2 Gradient descent** (slides 15–28): mountain-in-fog intuition (Géron Fig 4-3); why nonlinear
    least squares $S(\boldsymbol\beta)=\sum[y_i-f(\mathbf{x}_i,\boldsymbol\beta)]^2$ has no solvable
    closed form; a five-slide visual walkthrough of one descent step; update rule
    $\beta^{t+1}=\beta^t-\text{step}\cdot dS(\beta)/d\beta$. Slides 23–27 are PowerPoint animation
    builds of one bullet list — the cache keeps all five so slide numbers stay honest.
  - **§3 Batch / stochastic / mini-batch GD** (slides 29–31):
    $\partial\text{MSE}/\partial\theta_j=\frac{2}{m}\sum(\boldsymbol\theta^T\mathbf{x}^{(i)}-y^{(i)})x_j^{(i)}$,
    $\boldsymbol\theta\leftarrow\boldsymbol\theta-\eta\nabla_{\boldsymbol\theta}\text{MSE}$, SGD
    contour plot (Géron Fig 4-9), and Goodfellow's Algorithm 8.1 pseudocode.
  - **§4 Logistic regression** (slides 32–37): logit link
    $\log(H_\theta/(1-H_\theta))=\theta_0+\sum\theta_ix_i$, $H_\theta=1/(1+e^{-f(x)})$, the identity
    $\partial H_\theta/\partial\theta=H_\theta(1-H_\theta)x_i$, cross-entropy loss $J(\theta)$, and
    an 8-line gradient derivation collapsing to
    $\partial J/\partial\theta=\frac{1}{n}\sum(H_\theta(x_i)-y_i)x_i$.

  ⚠️ Slide 38 closes with **"End of Lecture 3"** and the PDF's metadata title is _"Data Science and
  Data Scientists"_ — more reused-material drift (see the ⚠️ in
  [[CPE342-machine-learning/CLAUDE|CLAUDE.md]]). The content really is Lecture 2.

- **[[Lecture+2+-+ML.pdf]]** — _Handwritten companion to the Lecture 2 deck_ (3 scanned pages,
  image-only). **Not a second deck.** A worked derivation of **nonlinear least squares** for the
  exponential model $f(x)=c_0+c_1e^{c_2x}$: the SSE $S=\sum(y-f(x))^2$ and its three partials
  $\partial S/\partial c_0$, $\partial S/\partial c_1$, $\partial S/\partial c_2$ (eq. 1–3), then a
  gradient-descent flowchart — randomize $c_0,c_1,c_2$ → compute $f(x)$ → compute gradient → update
  $c_i^{(t+1)}=c_i^{(t)}-\alpha\,\text{grad}_{c_i}$ → stop? — driven by exactly those three
  gradients. It fills in the concrete derivation that
  [[Lecture+2+-+Training+Models.pdf]] motivates on slides 16–17 but never works through.
  _(Text cache: [[Lecture+2+-+ML]] — best-effort transcription by a Sonnet subagent reading the page
  images; `pdftotext` returns pure garbage because the pages are scans. Handwriting is ambiguous —
  unclear symbols are marked `⟨?⟩` inline, so verify against the PDF before trusting a formula in
  an exam or a submission. **Page 1 is a blank red scanning artifact, not a missing page.**)_

## note/

My own study notes — written in Thai, casual register, built to be read instead of the slides.
Both follow the same shape: a label key (**(จาก slide N)** = on the real slide, **(เสริม)** = added
context, ⚠️ = slide typo or common trap, 🧮 = worked numeric example), a numbered สารบัญ of
`ตอนที่ N` sections, then a cheat sheet / errata / practice-problem / exam-checklist tail.

- **[[CPE342-machine-learning/note/lecture-1|lecture-1.md]]** — study guide for
  [[Lecture+1+-+Introduction+to+ML.pdf]], covering all 83 slides. Opens with a table folding the
  course-admin slides 1–7 (CLOs, grading, references, policies) and the section dividers into one
  row each, so nothing is silently dropped. Sections 0–16: foundations (notation, dot product,
  inverse, derivatives, logs) → what ML is → learning types → `Y=f(X)+ε`, prediction vs inference,
  reducible vs irreducible error → Mitchell's T/P/E with all 7 tasks and full metric formulas,
  plus the accuracy trap shown numerically → linear regression derived line by line from slide 39
  and worked by hand to $\hat{y}=0.5+1.4x$ with $R^2=0.98$ → under/overfitting with a
  train-vs-test diagnosis table → Bayes' classifier and Bayes error rate → Bayes' theorem
  (disease test solved twice, by formula and by natural frequencies) → Bayesian spam filter
  including Laplace smoothing and the log-form sigmoid that links it to logistic regression →
  LDA/QDA computed by hand end-to-end, including how an unequal prior flips the same test point →
  confusion matrix, F-measure, ROC/AUC by hand (trapezoid **and** pair-counting) → coding practice
  → cheat sheet → **slide errata table** → 7 practice problems with collapsible worked solutions →
  tiered exam checklist.
  > Worked examples deliberately avoid [[Assighment-1.pdf]]'s own dataset, same as
  > [[CPE342-machine-learning/note/lecture-2|lecture-2.md]] (class policy — see
  > [[CPE342-machine-learning/CLAUDE|CLAUDE.md]]).

- **[[CPE342-machine-learning/note/lecture-2|lecture-2.md]]** — study guide for
  [[Lecture+2+-+Training+Models.pdf]] **and** the handwritten companion [[Lecture+2+-+ML.pdf]],
  covering all 38 slides. Sections 0–15: foundations (chain rule, gradient, determinant, Cramer's
  rule) → closed-form vs iterative → the two model equations and what `ε` means → why least squares
  squares → OLS derived line by line from slide 8 through the Cramer's-rule closed forms, then
  computed by hand with $R^2$ → the slide-12 pseudoinverse example solved by hand to
  $[3, 5.5, -1.5]$, plus the geometric (orthogonal-projection) reason $\mathbf{A}^\top$ is
  multiplied in → gradient descent intuition and why nonlinear least squares has no closed form →
  GD walked by hand with a learning-rate table showing convergence, one-step convergence, and
  divergence → the handwritten deck's exponential model $c_0+c_1e^{c_2x}$ with all three partials
  and one full numeric iteration → batch/SGD/mini-batch with epoch-vs-iteration arithmetic →
  logistic regression from odds through the 8-line slide-35 gradient derivation, trained by hand →
  runnable code → cheat sheet → **slide errata table** → 7 practice problems with worked solutions →
  tiered exam checklist.
  > Worked examples deliberately use datasets **different from [[Assighment-1.pdf]]**, so the
  > assignment's own numbers stay ungraded work (class policy — see
  > [[CPE342-machine-learning/CLAUDE|CLAUDE.md]]).
