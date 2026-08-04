---
course: CPE342 Machine Learning
lecture: 1
title: Introduction to ML & Statistical Learning
source: lecture/Lecture+1+-+Introduction+to+ML.pdf (83 slides)
topics: [statistical-learning, bayes-classifier, LDA, QDA, evaluation-metrics]
tags: [cpe342, machine-learning, note]
---

# Lecture 1 — Introduction to ML & Statistical Learning

> [!abstract] What this lecture does
> It runs on **two levels at once**: (1) a tour of the whole ML landscape, and (2) the first three
> real ISLP topics — **statistical learning**, the **Bayes classifier**, and **discriminant
> analysis (LDA/QDA)**. The glue holding it together is Mitchell's **Task / Performance / Experience
> (T–P–E)** definition of learning. Keep that lens in mind and the 83 slides fall into place.

**Sections:** [§1 Statistical Learning](#1--statistical-learning) ·
[§2 Bayes' Classifier](#2--bayes-classifier) ·
[§3 Discriminant Analysis (LDA/QDA)](#3--discriminant-analysis-ldaqda) ·
[Evaluation metrics](#evaluation-metrics-classification) ·
[Formula cheat-sheet](#formula-cheat-sheet) · [Exam focus](#exam-focus) · [Errata](#errata-in-the-slides)

---

## §1 — Statistical Learning

### What ML is (and where it sits)
- **Machine learning** = a method of data analysis that **automates model building**: algorithms
  *learn from data* to find patterns **without being explicitly programmed** where to look.
- Nesting: **AI ⊃ ML ⊃ Deep Learning.** DL is a specific kind of ML (multi-layer neural nets);
  understanding DL requires solid ML basics first.
- **Why it matters:** *automatic* (train once, run repeatedly), *fast*, *accurate*, and *scales* to
  big data.

### The core model
$$Y = f(X) + \epsilon$$
- `X` = predictors (features), `Y` = response, `f` = the true but **unknown** relationship,
  `ε` = random noise (mean ≈ 0), independent of `X`.
- ML = producing an estimate **`f̂`** of `f`.
- **Two kinds of error:**
  - **Reducible** — the gap between `f̂` and `f`; we shrink it with better models/data.
  - **Irreducible** — the `ε` term; no model can beat it (it's the ceiling on accuracy).

### Why estimate `f`? Prediction vs. Inference
| Goal | You care about… | Model can be… |
|------|-----------------|---------------|
| **Prediction** | accuracy of `Ŷ = f̂(X)` | a black box |
| **Inference** | *which* predictors matter, and *how* | must be interpretable |

> [!tip] The explainability ↔ accuracy trade-off
> Simple models (linear/logistic regression) are **easy to explain but less accurate**; complex
> models (SVM, boosting, neural nets) are **more accurate but harder to explain**. Choosing a model
> = choosing where you sit on this line.

### Types of learning
- **Supervised** — data has known labels/outputs. (e.g. insurance underwriting, fraud detection)
- **Unsupervised** — no labels; find patterns/structure. (e.g. customer clustering, association rules)
- **Semi-supervised** — labels known for only a *subset*; blend of the two. (e.g. medical prediction
  where labelling is expensive)
- **Reinforcement** — learn by **making decisions and getting feedback/reward**. (e.g. game AI)

Within supervised learning:
- **Regression** → predict a **numeric value**  `f : ℝⁿ → ℝ`
- **Classification** → predict a **category** (1 of *k*)  `f : ℝⁿ → {1,…,k}`

### Mitchell's definition — the backbone (T / P / E)
> "A computer program learns from experience **E** w.r.t. tasks **T** and performance measure **P**,
> if its performance at T (as measured by P) improves with E." — *Mitchell, 1997*

- **Tasks (T):** classification, regression, **clustering** (`ℝⁿ→{1..k}` *without* labels),
  transcription (speech→text), machine translation, **anomaly detection**, synthesis & sampling.
- **Performance (P):** *classification* → accuracy / precision / recall; *regression* → R², MAE, MSE.
- **Experience (E):** the data — split into **training** vs **test** sets.
  - Train/tune on the **training set** (using **cross-validation**); **don't touch the test set**
    until the very end.
  - **k-fold cross-validation:** split training data into *k* folds; each round, one fold validates
    and the rest train; average the *k* scores. Gives a more stable performance estimate.

### Worked example — Linear Regression (a full T–P–E instance)
- **Task:** predict `ŷ = wᵀx`.
- **Performance:** Mean Squared Error, $\text{MSE} = \frac{1}{m}\sum_i (\hat y_i - y_i)^2$.
- **Experience:** choose `w` to minimize training MSE. Setting `∇_w MSE = 0` gives the closed-form
  **normal equation**:
$$w = (X^\top X)^{-1} X^\top y$$

### Under-fitting vs. Over-fitting
- **Under-fit** — model too simple, misses the real pattern (high bias). *e.g.* a straight line
  through curved data.
- **Appropriate capacity** — captures the signal, ignores the noise. ✅
- **Over-fit** — model too complex, memorizes noise / "too good to be true" (high variance); great on
  training data, bad on new data.
- This is exactly what the **train/test split + cross-validation** protects against.

---

## §2 — Bayes' Classifier

### The ideal classifier
Assign a test point `x₀` to the class **j** with the highest conditional probability:
$$\arg\max_j \; \Pr(Y = j \mid X = x_0)$$
- The set of points where classes tie forms the **Bayes decision boundary**.
- This is the **theoretically best possible** classifier — but we can't compute it directly (the
  true probabilities are unknown). Everything else *approximates* it.

### Bayes' Theorem
$$p(F\mid E) = \frac{p(E\mid F)\,p(F)}{p(E)}, \qquad p(E) = p(E\mid F)p(F) + p(E\mid \bar F)p(\bar F)$$
- **Posterior** `p(F|E)` = **likelihood** `p(E|F)` × **prior** `p(F)` ÷ **evidence** `p(E)`.
- Derived from the definition of conditional probability `p(E|F) = p(E∩F)/p(F)`.

> [!example] Base-rate trap (disease test) — the intuition to remember
> Disease in **1 / 100,000**. Test: 99% true-positive, 99.5% true-negative. If you test **positive**:
> $$p(D\mid E)=\frac{(0.99)(0.00001)}{(0.99)(0.00001)+(0.005)(0.99999)}\approx 0.002$$
> Only ~**0.2%** chance you're actually sick! Because the disease is so rare, false positives vastly
> outnumber true positives. **Priors dominate when an event is rare.** (Test negative → ~99.99999%
> chance you're fine.)

### Bayesian spam filter (applied Naïve Bayes)
For a word `w`: estimate `p(w) = n_B(w)/|B|` (spam) and `q(w) = n_G(w)/|G|` (ham). Assuming a message
is equally likely spam/ham a priori:
$$r(w) = \frac{p(w)}{p(w) + q(w)}$$
Flag as spam if `r(w)` > **threshold** (e.g. 0.9).
- **Multiple words** (assume independence — the "naïve" bit):
  $$r(w_1,\dots,w_k)=\frac{\prod p(w_i)}{\prod p(w_i)+\prod q(w_i)}$$
- *e.g.* "Rolex" (250/2000 spam, 5/1000 ham) → `r ≈ 0.962` → spam. More words ⇒ better accuracy.

---

## §3 — Discriminant Analysis (LDA/QDA)

**The move:** we can't compute the ideal Bayes classifier, so we **model each class's feature
distribution as Gaussian**, estimate its parameters from data, and plug into Bayes' theorem.

### Bayes' theorem for classification
$$\Pr(Y=k\mid X=x) = \frac{\pi_k\,f_k(x)}{\sum_{l=1}^K \pi_l\,f_l(x)}$$
- `π_k` = **prior** of class *k* (how common it is).
- `f_k(x)` = **class-conditional density** `Pr(X=x | Y=k)`, assumed **Gaussian**.

### LDA — Linear Discriminant Analysis
- **Assumption:** all classes are Gaussian **and share one common variance** `σ²` → boundaries are
  **straight lines**. Idea: project data to **maximize between-class separation** while
  **minimizing within-class spread**.
- Taking `log` of the Gaussian posterior kills the exponential and leaves a **linear** discriminant:
$$\delta_k(x) = x\cdot\frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \log(\pi_k)$$
  → assign `x` to the class with the **largest** `δ_k(x)`.
- **Estimate parameters from the training data:**
$$\hat\mu_k=\frac{1}{n_k}\!\!\sum_{i:y_i=k}\!\!x_i,\quad
\hat\sigma^2=\frac{1}{n-K}\sum_{k=1}^{K}\sum_{i:y_i=k}(x_i-\hat\mu_k)^2,\quad
\hat\pi_k=\frac{n_k}{n}$$

### QDA — Quadratic Discriminant Analysis
- **Relax** the shared-covariance assumption: each class gets its **own** covariance `Σ_k`.
- The log-posterior keeps a quadratic term → boundaries are **curved**:
$$\log P(y=k\mid x) = -\tfrac12\log|\Sigma_k| - \tfrac12 (x-\mu_k)^\top \Sigma_k^{-1}(x-\mu_k) + \log P(y=k) + \text{Cst}$$

> [!warning] LDA vs QDA — the key relationship (slide typo corrected)
> **LDA is a special case of QDA** where every class is forced to **share the same covariance
> matrix**. (Slide 71 misprints this as "LDA is a special case of LDA" — remember it as **QDA**.)
> - **LDA:** fewer parameters, straight boundaries, safer with little data (higher bias).
> - **QDA:** more flexible, curved boundaries, needs more data (higher variance).

---

## Evaluation metrics (classification)

From the **confusion matrix** (TP, FP, FN, TN):

| Metric | Formula | Meaning |
|--------|---------|---------|
| **Accuracy** | `(TP+TN)/(TP+FP+TN+FN)` | overall correctness |
| **Recall** (TPR, completeness) | `TP/(TP+FN)` | of the actual positives, how many did we catch? |
| **Precision** (exactness) | `TP/(TP+FP)` | of the predicted positives, how many were right? |
| **F-measure (F1)** | `2·(P·R)/(P+R)` | harmonic mean — balances precision & recall |
| **FPR** | `FP/(FP+TN)` | false-alarm rate |

**ROC curve** = TPR vs FPR as you sweep the decision threshold. **AUC** = area under it:

| AUC | Quality |
|-----|---------|
| 0.9–1.0 | Excellent |
| 0.8–0.9 | Very good |
| 0.7–0.8 | Good |
| 0.6–0.7 | Satisfactory |
| 0.5–0.6 | Unsatisfactory (≈ random = 0.5) |

*(Regression metrics from §1: R², MAE `= (1/n)Σ|ŷ_i − y_i|`, MSE `= (1/m)Σ(ŷ−y)²`.)*

---

## Formula cheat-sheet

| Concept | Formula |
|---------|---------|
| Statistical learning model | `Y = f(X) + ε` |
| Linear regression (normal eq.) | `w = (XᵀX)⁻¹Xᵀy` |
| Bayes' theorem | `p(F│E) = p(E│F)p(F) / p(E)` |
| Bayes classifier rule | assign `argmax_j Pr(Y=j│X=x₀)` |
| Bayes for classification | `Pr(Y=k│X=x) = π_k f_k(x) / Σ_l π_l f_l(x)` |
| LDA discriminant | `δ_k(x) = x·μ_k/σ² − μ_k²/2σ² + log π_k` |
| F1 | `2·(P·R)/(P+R)` |

---

## Exam focus

1. **`Y = f(X) + ε`** + reducible vs irreducible error + prediction vs inference.
2. **T–P–E** framing — be able to slot any algorithm into task / performance / experience.
3. **Bias–variance** intuition via under/over-fitting; why we need **test set + CV**.
4. **Bayes' theorem** numerically — the base-rate example is prime exam material.
5. **LDA vs QDA** — the shared-vs-per-class-covariance distinction, and that LDA ⊂ QDA.
6. **Precision / recall / F1 / ROC-AUC** — definitions and when each matters.

---

## Errata in the slides
- **Slide 71 (QDA):** "LDA is a special case of **LDA**" → should be "**QDA**".
- **MAE slide:** written `(1/n)Σ|xᵢ − x|`; means `(1/n)Σ|ŷᵢ − yᵢ|` (predicted − actual).
- **ROC slide:** lower triangle labelled "AOC" — not a real term; only **AUC** (area under curve) matters.

## References
- **ISLP** — G. James et al., *An Introduction to Statistical Learning with Applications in Python*
  (2023). This lecture ≈ **Ch. 2** (statistical learning) + **Ch. 4** (classification, LDA/QDA).
- **Géron** — *Hands-On Machine Learning with Scikit-Learn & TensorFlow* (O'Reilly, 2019).

> [!note] Source
> Summarized from `lecture/Lecture+1+-+Introduction+to+ML.pdf` (83 slides). See
> [[CLAUDE]] for course info and the instructor/semester flags.
