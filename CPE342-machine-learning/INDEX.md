# INDEX — CPE342 Machine Learning

Annotated map of this class folder, so an agent (and I) can understand it **without opening every
file**. Update when files are added/renamed/removed. `temp/` is not listed (volatile).

> Filenames use `+` for spaces (downloaded as-is from LEB2). Readable titles are given below.

## assignment/

- _none yet_

## lecture/

- **`CPE342+Syllabus.pdf`** — *Course syllabus* (2 pp). Course info (Fri 13:30–17:30, CB2506, 3
  credits), instructor Dr. Boonyarit Changaival, CLOs, grading (Midterm 30 / Final 35 / HW 35),
  grade scale, key references (ISLP 2023; Géron 2019), and class policies (1-week deadlines on
  LEB2, academic integrity). Source of truth for course facts — see `CLAUDE.md`.
  *(Text cache: `CPE342+Syllabus.md` — regenerated 2026-08-04 by a Sonnet subagent reading the
  pages; grading and grade-scale tables come through as real Markdown tables.)*

- **`Lecture+1+-+Introduction+to+ML.pdf`** — *Lecture 1: Introduction to ML; Statistical Learning
  concepts; Bayes' Classifier; LDA & QDA* (83 slides, by Asst. Prof. Dr. Santitham Prom-on).
  *(Text cache: `Lecture+1+-+Introduction+to+ML.md` — full LaTeX transcription via a Sonnet
  subagent, because `pdftotext` can't handle the formulas.)*
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

## note/

- **`lecture1.md`** — *My study note for Lecture 1* (Introduction to ML & Statistical Learning).
  Exam-ready summary of all 83 slides: §1 statistical learning (T–P–E, `Y=f(X)+ε`, linear
  regression, under/overfitting), §2 Bayes' classifier & spam filter, §3 LDA/QDA, evaluation
  metrics, a formula cheat-sheet, exam-focus list, and slide errata. Obsidian-formatted (math +
  callouts).
