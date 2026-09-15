# INDEX — CPE342 Machine Learning

Annotated map of this class folder, so an agent (and I) can understand it **without opening every
file**. Update when files are added/renamed/removed. `temp/` is not listed (volatile).

> Format per entry: `[[file]]` — what it is / what it covers (+ due date or status if relevant).
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

- **[[assignment-1-ols.ipynb]]** — _my working notebook for Assignment 1_ (19 cells). A report
  skeleton following the brief's three tasks, **scaffold only — the numbers aren't filled in.** Fits
  the OLS coefficients two independent ways so they cross-check: the deviation-score formula
  $\hat\beta = S_{xy}/S_{xx}$, and the slide-14 pseudoinverse
  $\mathbf{B} = (\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top\mathbf{y}$ — because the brief says
  *"Implement"*, not *"Calculate"*, so the formula gets coded rather than delegated to
  `sklearn.LinearRegression()`. Also carries the by-hand working table, the $R^2$ cell, a
  scatter-plus-fitted-line plot, and a self-check cell that `assert`s against `np.polyfit` so it
  reports right/wrong without printing the answer. Conventions: `...  # TODO` = a code blank,
  `_____` = a prose blank, and every Thai cell or 📝 blockquote is a note to myself to **delete
  before exporting the PDF**.
  > Left unsolved on purpose — the numbers are my gradable deliverable (class policy — see
  > [[CPE342-machine-learning/CLAUDE|CLAUDE.md]]). Export to PDF, submit on LEB2.

- **[[assignment-2.pdf]]** — _Assignment 2: Training models via iterative approach_ (1 p, 10 pts).
  **Gradient descent**, the iterative counterpart to Assignment 1's closed-form OLS. Fit the
  nonlinear model $\hat{y} = c_0 + c_1e^{c_2x}$ to a ~100-point dataset by GD. Five tasks:
  (1) write the error/loss function (1 pt); (2) write the gradient of each coefficient (3 pts);
  (3) write the update rules (1 pt); (4) implement GD on the given data (4 pts); (5) show the loss
  over iterations and the resulting coefficients (1 pt). Submit as a **PDF report on LEB2**. This is
  exactly the model derived by hand in [[Lecture+2+-+ML.pdf]] — equations (1)–(3) on its page 2 are
  task 2, and its page-3 flowchart is tasks 3–4.
  _(Text cache: [[assignment-2]] — `pdftotext` base, hand-repaired: the model equation uses Cambria
  Math private-use codepoints that extract as `������`, and the data scatter plot is an embedded
  image that text extraction drops. Both transcribed into the cache from the page.)_
  > ⚠️ **Due date is stale**, same reused-brief pattern as [[Assighment-1.pdf]]: the header prints
  > _"1/2024"_ and _"Due: 4 Sep 2024"_ (a **two**-week window from its 21 Aug 2024 creation date,
  > not the syllabus's one week). Lecture 3 was handed out **Fri 21 Aug 2026**, so the real due date
  > is **Fri 28 Aug** or **Fri 4 Sep 2026**. Confirm on LEB2.
  > **The dataset is not in the PDF** — it sits behind a Google Drive link on the page (see the
  > cache); the figure on the page is only a picture of it. Downloaded as [[A2.csv]].

- **[[A2.csv]]** — the Assignment 2 dataset, pulled from the Drive link in [[assignment-2]].
  100 rows × 2 columns, `X` and `Y`: `X` spans 0.011–4.978, `Y` decays from 1.971 down to a noisy
  plateau at ≈0.95 — matches the scatter printed in the brief. Fitted by
  [[assignment-2-gd.ipynb]].

- **[[assignment-2-gd.ipynb]]** — _my working notebook for Assignment 2_ (13 cells), the gradient
  descent counterpart to [[assignment-1-ols.ipynb]]. Laid out as the brief's five tasks: tasks 1–2
  (loss + gradients) and task 3 (update rules) are **handwritten on GoodNotes** and slot in as
  [[a2-proff.jpg]] and [[a2-proff3.jpg]]; task 4 is a hand-written batch-GD loop on
  [[A2.csv]] — MSE loss, all three gradients computed from the old coefficients then updated
  simultaneously; task 5 prints the coefficients and draws loss-vs-iteration beside the fitted
  curve over the scatter. Conventions carried over from Assignment 1: `_____` = a blank to fill,
  and every 📝 blockquote is a note to myself to **delete before exporting the PDF**.
  _(PDF export: [[assignment-2-gd.pdf]] — 4 pp, generated from the notebook for LEB2 submission.)_
  > Run at $lpha = 0.01$, 5000 epochs, init $(1, 1, -1)$ it lands on
  > $(0.987,\ 0.941,\ -1.247)$ with MSE $0.001156$ — the optimum is $(1.003,\ 0.999,\ -1.530)$ at
  > MSE $0.000755$, so **that setting stops short**; the loss curve is still visibly falling at the
  > last iteration. $lpha = 0.05$ reaches it in the same 5000 epochs, $lpha = 1.0$ diverges.

- **`assignment/a3/`** — Assignment 3 sits in its own subfolder (the first one here; A1 and A2 are
  flat in `assignment/`), because the activity ships with both its dataset and the in-class
  notebook. **There is no PDF brief** — the task is the last cell of the lecturer's notebook:
  _"Use Telco Churn dataset and build a Kaplan Meier survival analysis. Compare lifetime between
  different payment methods."_

  - **[[6_regression.ipynb]]** — the **lecturer's** Module 6 notebook, handed out in class (98
    cells, outputs kept). `mtcars` correlation heatmap → `statsmodels` OLS → scikit-learn multiple
    regression → **Poisson regression / GLM** on mine-injury data with a `cancer.xls` activity →
    **§8 survival analysis** with `lifelines` (Kaplan-Meier on the `load_dd` political-regimes data,
    segmented democratic vs non-democratic) → **§9 Cox proportional hazards** on `load_rossi`. Its
    §8 is the template the activity is modelled on.

  - **[[Telco+Churn.csv]]** — the activity's dataset. 7043 rows × 21 cols, one row per customer:
    `tenure` (months in service, 0–72) is the duration, `Churn` (Yes/No) is the event, and
    `PaymentMethod` is the grouping variable — Electronic check 2365 · Mailed check 1612 · Bank
    transfer (automatic) 1544 · Credit card (automatic) 1522. Overall churn 1869 / 7043 ≈ 26.5%, so
    **~73% of rows are censored**. 11 rows have `tenure = 0` and a blank `TotalCharges` (brand-new
    customers, all `Churn = No`) — they carry no information for KM.

  - **[[assignment-3.ipynb]]** — _my working notebook for the activity_ (29 cells). Built as small
    step-by-step cells that each `print` a check rather than long prose: load → map `Churn` to a
    0/1 `event` (verified with a `crosstab`) → drop the 11 `tenure = 0` rows → baseline KM over all
    customers → raw churn rate per payment method as a sanity check → four KM curves overlaid with
    confidence intervals → a summary table → `multivariate_logrank_test` and
    `pairwise_logrank_test`. Section 8 is the conclusion, filled from the output.
    _(PDF export: [[assignment-3.pdf]] — 7 pp, generated from the notebook for LEB2 submission.)_
    > **Median survival is `inf` for three of the four groups** — S(t) never falls to 0.5 inside 72
    > months, so medians can't rank them. The notebook compares S(12)/S(24)/S(48) and **RMST at
    > t = 72** instead. Result: Credit card ≈ Bank transfer (log-rank p = 0.35, the only
    > non-significant pair) ≫ Mailed check ≫ Electronic check, whose RMST is 41.2 vs 63.8 months.

- **`assignment/a4/`** — Assignment 4, its own subfolder like `a3/`, and for the same reason: the
  lecturer's notebook ships with the dataset. **No PDF brief** — the task is the whole of
  [[detail]], written down in class: *"ใช้ Decision tree / Random forest / Gradient boosting
  ทำนายผลการรับนักศึกษา (admission) ว่าได้รับ admit หรือไม่"*. Pairs with
  [[Lecture+5+-+Tree-based+and+Ensemble+Models.pdf]], handed out **Fri 4 Sep 2026** → due **Fri 11
  Sep 2026** under the one-week policy. Confirm on LEB2.

  - **[[5(1)_classification_tree-based.ipynb]]** — the **lecturer's** Module 5(1) notebook (57
    cells, outputs stripped). Worked on `hr_attrition.csv` (not included): numeric/categorical
    split → `get_dummies(drop_first=True)` → `train_test_split` → `DecisionTreeClassifier` →
    graphviz tree plot → `feature_importances_` → `predict` / `predict_proba` → confusion matrix,
    `classification_report`, ROC/AUC. **Decision tree only** — the random-forest and
    gradient-boosting half of Lecture 5 is in a Module 5(2) notebook that wasn't handed out, so the
    ensemble code comes from the deck, not from here. Two cells are Colab-only
    (`google.colab.drive`, pickling to Drive) and one needs `pydotplus` + graphviz.

  - **[[MBA.csv]]** — the assignment's dataset. 6194 rows × 10 cols, one row per MBA applicant:
    `gpa` (2.65–3.77), `gmat` (570–780), `work_exp` (1–9 yrs), plus `gender`, `international`,
    `major`, `race`, `work_industry`, and the target `admission`. **Two traps worth knowing before
    modelling.** (1) `admission` is blank on 5194 rows — those are **Deny**, not missing data; only
    `Admit` (900) and `Waitlist` (100) are spelled out, so the positive class is 900/6194 ≈ 14.5%
    and the data is imbalanced. (2) `race` is blank on exactly the 1842 rows where
    `international == True` — the column is only recorded for domestic applicants, so it's a
    category ("International"), not a hole to drop or impute.

  - **[[assignment-4.ipynb]]** — _my working notebook for the assignment_ (46 cells), same
    small-cells-that-print-a-check shape as [[assignment-3.ipynb]]: load → `admission` → 0/1
    `admit` target (crosstab-verified, `NaN` folded into 0) → drop `application_id` → the
    `race`/`international` crosstab and the `International` fill → `get_dummies` → stratified
    70/30 holdout → one `evaluate()` helper reused by all three models → **decision tree**
    (`class_weight='balanced'`, `plot_tree` at depth 2) → **random forest** (300 trees,
    `balanced_subsample`, `oob_score`) → **gradient boosting** (300 rounds, `learning_rate=0.05`,
    balanced `sample_weight` — the class has no `class_weight` argument) → a comparison table and
    three ROC curves on one axis. Section 12 is the conclusion, filled from the output.
    _(PDF export: [[assignment-4.pdf]] — 10 pp, generated from the notebook for LEB2 submission.)_

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

- **[[Lecture+3+-+Support+Vector+Machine.pdf]]** — _Lecture 3: Support Vector Machine_ (taught
  **Fri 21 Aug 2026**). Not yet summarised — added to the vault 24 Aug 2026 and not opened.
  _(Text cache: **missing.** Run `/update-index` or the `pdf-cache` skill to generate it — it is a
  slide deck with math, so it needs a Sonnet subagent, not `pdftotext`.)_

- **[[Lecture+4+-+Regression.pdf]]** — _Lecture 4: Regression_. Not yet summarised — added to the
  vault 31 Aug 2026 and not opened. Almost certainly the deck behind the lecturer's
  [[6_regression.ipynb]] in `assignment/a3/`, which is the coding half of the same material
  (regression → GLM/Poisson → survival analysis → Cox PH).
  _(Text cache: **missing.** Run `/update-index` or the `pdf-cache` skill to generate it — a slide
  deck with math, so it needs a Sonnet subagent, not `pdftotext`.)_

- **[[Lecture+5+-+Tree-based+and+Ensemble+Models.pdf]]** — _Lecture 5: Tree-Based and Ensemble
  Models_ (taught **Fri 4 Sep 2026**, downloaded 7 Sep). Three topics per its own agenda slide:
  **decision trees** (supervised segmentation, purity, entropy, information gain worked on the
  write-off example, Gini as the alternative split criterion, then accuracy/precision/recall/
  F-measure and ROC–AUC), **bagging** (bootstrap samples → vote/average, out-of-bag error, variance
  reduction, → random forests: 100–500 trees, `m` random variables per node, grown to full depth),
  and **boosting** (AdaBoost → gradient boosting = gradient descent + boosting, fitting each new
  weak learner to the residual → xgboost's regularization / sparsity awareness / parallelization /
  cache-aware access). Closes on bagging-is-robust-to-noise vs boosting-squeezes-performance. Two
  Google Drive links on the section-divider slides. The coding half is
  [[5(1)_classification_tree-based.ipynb]] in `assignment/a4/`.
  _(Text cache: **missing.** Run `/update-index` or the `pdf-cache` skill to generate it — a slide
  deck with math and figures, so it needs a Sonnet subagent, not `pdftotext`.)_

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
