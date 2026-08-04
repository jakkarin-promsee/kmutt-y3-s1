# Lecture 1 — Introduction to ML (text cache)

> Auto-generated Markdown cache of `Lecture+1+-+Introduction+to+ML.pdf` (83 slides). Formulas transcribed as LaTeX; figures described in italics. This is a lossy proxy — open the PDF for exact figures and layout.

## Slide 1 — Machine Learning

- **Machine Learning**
- Lecture 1: Introduction to ML, Statistical learning: concepts, Bayes classifier, LDA, QDA
- **Asst. Prof. Dr. Santitham Prom-on**
- Department of Computer Engineering, Faculty of Engineering
- King Mongkut's University of Technology Thonburi

*Figure: Title slide with CPE department logo (top left), KMUTT logo (bottom left), and Big Data Experience Center logo (bottom right).*

## Slide 2 — Course Learning Outcome

- CLO1: Demonstrate mastery in concepts and details of supervised learning algorithms.
- CLO2: Demonstrate mastery in concepts and details of unsupervised and reinforcement learning algorithms.
- CLO3: Implement machine learning models and workflows.

## Slide 3 — Grading

- Midterm Exam 30%
- Final Exam 35%
- Homework and assignments 35%

A: ≥ 85, B+: [84,80], B: [79,75], C+: [74,65], C: [64,55], D+: [54,50], D: [49,45], F: < 45

The instructor reserves the right to change the grading policy as deemed appropriate.

## Slide 4 — References

- G. James, et.al., Introduction to Statistical Learning with Application with Python, 2023
- A. Geron, Hands-On Machine Learning with Scikit-Learn & Tensorflow, O'Reilly, 2019

## Slide 5 — Class Policies

- Assignments are due in one week before class in LEB2.
- Late submissions are only accepted under reasonable excuses and explicit permission from the instructor. No submission is accepted after the solution has been posted.
- Posted solutions will be brief and does not show routine works. You should attempt to work out detailed solutions on your own.
- Academic integrity is strictly enforced.

## Slide 6 — Topics

- Introduction to ML
- Statistical learning concepts
- Bayes' classifier
- Discriminant analysis

## Slide 7 — Introduction to ML / Statistical Learning Concepts

Section 1

## Slide 8 — Consumer ML

- Face Detection
- Face Recognition
- Expression Recognition
- Gender Prediction / Age Estimation
- Voice Interface
- Smart Home

*Figure: Photo collage of consumer ML applications — a woman's face with a face-recognition bounding box labeled "Nicole, Female, 26" and "Smile, 96%"; a smartphone voice-assistant screen reading "What can I help you with?"; and an Amazon Echo smart speaker surrounded by app icons (Pandora, Spotify, WeMo, Philips Hue, SmartThings, iHeartRadio, NPR News, Domino's, Uber, Audible, IFTTT).*

## Slide 9 — What exactly is machine learning?

- Machine learning (ML) is a method of data analysis that automates analytical model building.
- Using algorithms that iteratively learn from data, machine learning allows computers to find hidden insights without being explicitly programmed where to look.

## Slide 10 — Why machine learning matter

- Automatic: Train it once and it can be run automatically
- Fast: With big data, work faster than human
- Accurate: Can predict groups more accurately than manual methods
- Scale: Able to handle large data

## Slide 11 — Timeline

*Figure: Timeline graphic spanning the 1950s–2010s showing three overlapping eras — "Artificial Intelligence" (early artificial intelligence stirs excitement, robot icon), "Machine Learning" (machine learning begins to flourish, head-with-gears icon), and "Deep Learning" (deep learning breakthroughs drive AI boom, brain/circuit icon).*

## Slide 12 — Types of ML

*Figure: Tree diagram. "Machine Learning" branches into "Supervised Learning" and "Unsupervised Learning". Supervised Learning branches into "Classification" (Support Vector Machines, Discriminant Analysis, Naive Bayes, Nearest Neighbor, Neural Networks) and "Regression" (Linear Regression/GLM, SVR/GPR, Ensemble Methods, Decision Trees, Neural Networks). Unsupervised Learning branches into "Clustering" (K-Means/K-Medoids/Fuzzy C-Means, Hierarchical, Gaussian Mixture, Hidden Markov Model, Neural Networks).*

## Slide 13 — Style of Learning

*Figure: Four-column comparison table.*
- **Column 1:** Data has known labels or output. Examples: Insurance underwriting, Fraud detection.
- **Column 2:** Labels or output unknown. Focus on finding patterns and gaining insight from the data. Examples: Customer clustering, Association rule mining.
- **Column 3:** Labels or output known for a subset of data. A blend of supervised and unsupervised learning. Examples: Medical predictions (where tests and expert diagnoses are expensive, and only part of the population...).
- **Column 4:** Focus on making decisions based on previous experience. Policy-making with feedback. Examples: Game AI, Complex decision problems, Reward systems.

## Slide 14 — Figure 2.1 (Advertising data set)

**FIGURE 2.1.** The `Advertising` data set. The plot displays `sales`, in thousands of units, as a function of `TV`, `radio`, and `newspaper` budgets, in thousands of dollars, for 200 different markets. In each plot we show the simple least squares fit of `sales` to that variable, as described in Chapter 3. In other words, each blue line represents a simple model that can be used to predict `sales` using `TV`, `radio`, and `newspaper`, respectively.

*Figure: Three scatter plots of Sales (y-axis) vs TV, Radio, and Newspaper advertising budgets (x-axis), each with a blue least-squares fit line overlaid on red data points.*

## Slide 15 — Representing relationship

- Suppose that we observe a quantitative response Y and p different predictors, X₁, X₂,…,Xₚ.
- Assume that there is some relationship between Y and X = (X₁, X₂,…,Xₚ),

$$Y = f(X) + \epsilon.$$

## Slide 16 — Figure 2.2 (Income data set)

**FIGURE 2.2.** The `Income` data set. Left: The red dots are the observed values of `income` (in tens of thousands of dollars) and `years of education` for 30 individuals. Right: The blue curve represents the true underlying relationship between `income` and `years of education`, which is generally unknown (but is known in this case because the data were simulated). The black lines represent the error associated with each observation. Note that some errors are positive (if an observation lies above the blue curve) and some are negative (if an observation lies below the curve). Overall, these errors have approximately mean zero.

*Figure: Two scatter plots of Income vs Years of Education for 30 individuals — left shows raw red data points only; right adds a blue curve of the true underlying relationship with black vertical error lines connecting each point to the curve.*

## Slide 17 — Why estimate f?

- Prediction

$$\hat{Y} = \hat{f}(X),$$

- Inference
  - Which predictors are associated with the response?
  - What is the relationship between the response and each predictor?
  - Can the relationship between Y and each predictor be adequately summarized using a linear equation, or is the relationship more complicated?

**FIGURE 2.3.** The plot displays `income` as a function of `years of education` and `seniority` in the `Income` data set. The blue surface represents the true underlying relationship between `income` and `years of education` and `seniority`, which is known since the data are simulated. The red dots indicate the observed values of these quantities for 30 individuals.

*Figure: 3D surface plot of Income as a function of Years of Education and Seniority — a blue wavy surface (true relationship) with red dots (observed data for 30 individuals).*

## Slide 18 — How do we estimate f?

- Linear models

$$f(X) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \ldots + \beta_p X_p.$$

- Non-linear models

*Figure: Three example decision trees (genre==comedy / actor==top box office draw; type==mp3 / artist==highly clicked; type==e-book / author==bestselling author / genre==fiction), each branching yes/no down to leaf values (e.g., +0.8, +0.2, +0.05, +0.0, +0.75, +0.1).*

## Slide 19 — Explainability vs Accuracy

Duval, Alexandre. (2019). Explainable Artificial Intelligence (XAI). 10.13140/RG.2.2.24722.09929.

*Figure: Scatter plot with axes Accuracy (vertical) vs Explainability (horizontal), plotting model types along a downward-sloping trend line: NN, Boosting, Bagging, SVM (high accuracy, low explainability) down through Graphical model, Decision Tree, Naive Bayes, Logistic, Linear Regression, Lasso, to Classification (high explainability, low accuracy).*

## Slide 20 — Supervised vs Unsupervised

Qian, Bin & Su, Jie & Wen, Zhenyu & Yang, Renyu & Zomaya, Albert & Rana, Omer. (2019). Orchestrating the Development Lifecycle of Machine Learning-Based IoT Applications: A Taxonomy and Survey.

*Figure: Side-by-side scatter plots comparing supervised learning (red/blue labeled points separated by a dashed decision line) and unsupervised learning (unlabeled gray points grouped into dashed-circle clusters).*

## Slide 21 — Regression vs Classification

*Figure: Side-by-side scatter plots. "Classification" panel shows blue circles and purple crosses separated by a dashed red decision line. "Regression" panel shows scattered blue points with a dashed red best-fit line through them.*

## Slide 22 — Machine Learning Basics

- Deep learning is a specific kind of machine learning.
- To understand deep learning well, one must have a solid understanding of the basic principles of machine learning.

*Figure: Concentric circles diagram — outer "Artificial Intelligence" (a program that can sense, reason, act, and adapt), middle "Machine Learning" (algorithms whose performance improve as they are exposed to more data over time), inner "Deep Learning" (subset of machine learning in which multilayered neural networks learn from vast amounts of data).*

## Slide 23 — Learning Algorithm - Definition

"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E." (Mitchell, 1997)

*Figure: Diagram showing E (experience) feeding upward into an arrow from T (tasks) to P (performance measure).*

## Slide 24 — Tasks, T

**Classification**
- In this type of task, the computer program is asked to specify which of k categories some input belongs to.
- To solve this task, the learning algorithm is usually asked to produce a function f: Rⁿ → {1,..., k}.
- When y = f(x), the model assigns an input described by vector x to a category identified by numeric code y.

## Slide 25 — Tasks, T

**Regression**
- In this type of task, the computer program is asked to predict a numerical value given some input.
- To solve this task, the learning algorithm is asked to output a function f: Rⁿ → R.
- This type of task is similar to classification, except that the format of output is a value instead of a class.

## Slide 26 — Tasks, T

**Clustering**
- In this type of task, the computer program is asked to divide data into groups.
- To solve this task, the learning algorithm is asked to output a function f: Rⁿ → {1,…,k}, but without the label.
- The goal is usually to divide data into groups based on specific features, e.g. Recency-Frequency-Monetary customer segmentation

## Slide 27 — Tasks, T

**Transcription**
- In this type of task, the machine learning system is asked to observe a relatively unstructured representation of some kind of data and transcribe the information into discrete textual form.

*Figure: "How a Speech Application Learns" diagram in three steps — Step 1: Record voices (person speaking into a mic, "the quick brown fox jumps over the lazy dog"); Step 2: Input voice data through an STT Engine Algorithm producing incorrect transcriptions ("do", "kick", "bound", marked with red X) versus correct ones ("the", "quick", "brown", marked with green checkmarks); Step 3: Train the speech algorithm via a deep learning architecture (Generate, Check, Correct, Update, Learn).*

## Slide 28 — Tasks, T

**Machine Translation**
- In a machine translation task, the input already consists of a sequence of symbols in some language, and the computer program must convert this into a sequence of symbols in another language.

*Figure: Vauquois-triangle diagram with source text and target text at the base corners connected by a "direct translation" arrow, and "analysis" / "transfer" / "generation" paths rising toward an "interlingua" apex.*

## Slide 29 — Tasks, T

**Anomaly Detection**
- In this type of task, the computer program sifts through a set of events or objects and flags some of them as being unusual or atypical.

*Figure: Pipeline diagram: Model (network graph icon) → Prediction (donut chart showing "Probability of fraud 85.6%") → Explanation (bar chart icon) → Human (person icon).*

## Slide 30 — Tasks, T

**Synthesis and sampling**
- In this type of task, the machine learning algorithm is asked to generate new examples that are similar to those in the training data.

*Figure: Grid of face photos comparing "Ground truth" images of two people (a blonde woman, a man being interviewed) against AI-generated "1-shot", "8-shot", and "32-shot" synthesis results of the same faces.*

## Slide 31 — Performance, P

**Classification**

Precision = $\dfrac{\text{True Positive}}{\text{Actual Results}}$ or $\dfrac{\text{True Positive}}{\text{True Positive} + \text{False Positive}}$

Recall = $\dfrac{\text{True Positive}}{\text{Predicted Results}}$ or $\dfrac{\text{True Positive}}{\text{True Positive} + \text{False Negative}}$

Accuracy = $\dfrac{\text{True Positive} + \text{True Negative}}{\text{Total}}$

*Figure: Left — an ROC curve plot (TPR vs FPR) with the area under the curve (AOC) shaded gray. Middle — a 2×2 confusion-matrix grid (Predicted vs Actual) coloring True Positive, False Positive, False Negative, True Negative. Right — a diagram of "relevant elements" vs "selected elements" as overlapping regions showing true positives, false positives, false negatives, true negatives, with pie-slice icons illustrating the Precision and Recall formulas.*

## Slide 32 — Performance, P

**Regression**

$R^2$

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} |x_i - x|$$

*Figure: Left — scatter plot illustrating $R^2$, showing squared residuals from the mean ȳ as red squares over two data points. Right — scatter plot showing a fitted line/function f with predicted values (blue squares) versus actual data points.*

## Slide 33 — Performance, P

**Train set and Test set**

*Figure: Horizontal bar split into "Training Set" (larger, yellow — "Train and tune your models (using cross-validation)") and "Test Set" (smaller, black — "Don't touch this until the very end.").*

## Slide 34 — Experience, E

**Train set and Test set**

*Figure: Same horizontal bar diagram as the previous slide — "Training Set" (yellow, train/tune with cross-validation) and "Test Set" (black, don't touch until the very end).*

## Slide 35 — Cross-validation

*Figure: K-fold cross-validation diagram showing 5 iterations (1st–5th); each iteration marks a different one of five blocks as the "Validation Fold" (blue) and the remaining four as "Training Fold" (gray), producing a Performance score per iteration.*

$$\text{Performance} = \frac{1}{5}\sum_{i=1}^{5} \text{Performance}_i$$

## Slide 36 — Example: Linear Regression

- Linear regression solves a regression problem.
- In other words, the goal is to build a system that can take a vector **x** ∈ Rⁿ as input and predict the value of a scalar y ∈ R as its output.
- The output of linear regression is a linear function of the input.
- Let ŷ be the value that our model predicts y should take on. We define the output to be

$$\hat{y} = \boldsymbol{w}^\top \boldsymbol{x},$$

where **w** ∈ Rⁿ is a vector of parameters

## Slide 37 — Linear regression: Task, T

To predict y from **x** by outputting

$$\hat{y} = \boldsymbol{w}^\top \boldsymbol{x},$$

## Slide 38 — Performance measure, P

Mean square error

$$\text{MSE}_{\text{test}} = \frac{1}{m}\sum_i (\hat{y}^{(\text{test})} - y^{(\text{test})})_i^2.$$

## Slide 39 — Experience, E

$$\nabla_{\boldsymbol{w}} \text{MSE}_{\text{train}} = 0$$

$$\Rightarrow \nabla_{\boldsymbol{w}} \frac{1}{m}\left\lVert \hat{\boldsymbol{y}}^{(\text{train})} - \boldsymbol{y}^{(\text{train})} \right\rVert_2^2 = 0$$

$$\Rightarrow \frac{1}{m}\nabla_{\boldsymbol{w}} \left\lVert \boldsymbol{X}^{(\text{train})}\boldsymbol{w} - \boldsymbol{y}^{(\text{train})} \right\rVert_2^2 = 0$$

$$\Rightarrow \nabla_{\boldsymbol{w}} \left(\boldsymbol{X}^{(\text{train})}\boldsymbol{w} - \boldsymbol{y}^{(\text{train})}\right)^\top \left(\boldsymbol{X}^{(\text{train})}\boldsymbol{w} - \boldsymbol{y}^{(\text{train})}\right) = 0$$

$$\Rightarrow \nabla_{\boldsymbol{w}} \left(\boldsymbol{w}^\top \boldsymbol{X}^{(\text{train})\top}\boldsymbol{X}^{(\text{train})}\boldsymbol{w} - 2\boldsymbol{w}^\top \boldsymbol{X}^{(\text{train})\top}\boldsymbol{y}^{(\text{train})} + \boldsymbol{y}^{(\text{train})\top}\boldsymbol{y}^{(\text{train})}\right) = 0$$

$$\Rightarrow 2\boldsymbol{X}^{(\text{train})\top}\boldsymbol{X}^{(\text{train})}\boldsymbol{w} - 2\boldsymbol{X}^{(\text{train})\top}\boldsymbol{y}^{(\text{train})} = 0$$

$$\Rightarrow \boldsymbol{w} = \left(\boldsymbol{X}^{(\text{train})\top}\boldsymbol{X}^{(\text{train})}\right)^{-1}\boldsymbol{X}^{(\text{train})\top}\boldsymbol{y}^{(\text{train})}$$

## Slide 40 — Linear regression – learning weight

*Figure: Left — scatter plot "Linear regression example" of y vs x₁ with a fitted blue line through data points. Right — "Optimization of w" plot showing MSE^(train) as a convex curve over w₁, with the minimum marked near w₁ ≈ 1.5.*

## Slide 41 — Regression, underfitting and overfitting

*Figure: Three panels — "Underfitting" (a straight line poorly fitting curved data), "Appropriate capacity" (a quadratic curve fitting the data well), "Overfitting" (a high-degree polynomial curve passing exactly through every point).*

Underfitting: $\hat{y} = b + wx.$

Appropriate capacity: $\hat{y} = b + w_1 x + w_2 x^2.$

Overfitting: $\hat{y} = b + \displaystyle\sum_{i=1}^{9} w_i x^i.$

## Slide 42 — Classification, underfitting and overfitting

*Figure: Three scatter-plot panels with X and O classes. "Under-fitting" (too simple to explain the variance — a single straight decision line). "Appropirate-fitting" [sic] (a smooth curved decision boundary). "Over-fitting" (forcefitting — too good to be true — a highly convoluted, wiggly decision boundary).*

## Slide 43 — Bayes' Classifier

Section 2

## Slide 44 — Bayes' Classifier

- assigns each observation to the most likely class, given its predictor values.
- In other words, we should simply assign a test observation with predictor vector x₀ to the class j for which

$$\Pr(Y = j \mid X = x_0)$$

is the largest

- This is a conditional probability, the probability conditional that Y = j, given the observed predictor vector x₀.

## Slide 45 — Figure 2.13

**FIGURE 2.13.** A simulated data set consisting of 100 observations in each of two groups, indicated in blue and in orange. The purple dashed line represents the Bayes decision boundary. The orange background grid indicates the region in which a test observation will be assigned to the orange class, and the blue background grid indicates the region in which a test observation will be assigned to the blue class.

*Figure: Scatter plot of X₁ vs X₂ with orange and blue circles for two classes, overlaid on an orange/blue background grid indicating predicted class regions, separated by a purple dashed Bayes decision boundary.*

## Slide 46 — (untitled — spam-filtering pipeline diagram)

*No slide title is visible on this slide; it appears to illustrate the general email-classification pipeline as a lead-in to the Bayesian spam filter discussion.*

*Figure: Diagram showing three input files (spam.eml, ham.eml, ham.eml), each parsed into "Email" objects that feed into a "Spam Trainer" (which also receives new "Text" input), producing an output classification into "Spam" or "Ham" bins.*

## Slide 47 — Motivation for Bayes' Theorem

- Bayes' theorem allows us to use probability to answer questions such as the following:
  - Given that someone tests positive for having a particular disease, what is the probability that they actually do have the disease?
  - Given that someone tests negative for the disease, what is the probability, that in fact they do have the disease?
- Bayes' theorem has applications to medicine, law, artificial intelligence, engineering, and many diverse other areas.

## Slide 48 — Bayes' Theorem

**Bayes' Theorem**: Suppose that E and F are events from a sample space S such that p(E) ≠ 0 and p(F) ≠ 0. Then:

$$p(F|E) = \frac{p(E|F)p(F)}{p(E|F)p(F) + p(E|\overline{F})p(\overline{F})}$$

*Figure: Portrait of Thomas Bayes (1702–1761), with a handwritten annotation bracketing the denominator of the formula and labeling it p(E).*

## Slide 49 — Derivation of Bayes' Theorem

Recall the definition of the conditional probability p(E|F):

$$p(E|F) = \frac{p(E \cap F)}{p(F)}$$

From this definition, it follows that:

$$p(E|F) = \frac{p(E \cap F)}{p(F)}, \qquad p(F|E) = \frac{p(E \cap F)}{p(E)}$$

## Slide 50 — Derivation of Bayes' Theorem

$$p(E|F)p(F) = p(E \cap F), \qquad p(F|E)p(E) = p(E \cap F)$$

Equating the two formulas for p(E∩F) shows that

$$p(E|F)p(F) = p(F|E)p(E)$$

Solving for p(E|F) and for p(F|E) tells us that

$$p(E|F) = \frac{p(F|E)p(E)}{p(F)}, \qquad p(F|E) = \frac{p(E|F)p(F)}{p(E)}$$

## Slide 51 — Bayes' Theorem

$$p(F|E) = \frac{p(E|F)p(F)}{p(E)}$$

Labeled terms:
- p(E|F) — **likelihood**
- p(F) — **Prior probability of F**
- p(F|E) (left-hand side) — **Posterior probability**
- p(E) (denominator) — **Prior probability of E**

*Figure: The formula for Bayes' theorem with arrows annotating each term as likelihood, prior probability of F, posterior probability, and prior probability of E.*

## Slide 52 — Derivation of Bayes' Theorem

$$p(F|E) = \frac{p(E|F)p(F)}{p(E)}$$

Note that

$$p(E) = p(E|F)p(F) + p(E|\overline{F})p(\overline{F})$$

since $p(E) = p(E \cap F) + p(E \cap \overline{F})$

$$p(E) = p(E \cap F) + p(E \cap \overline{F}) = p(E|F)p(F) + p(E|\overline{F})p(\overline{F})$$

Hence,

$$p(F|E) = \frac{p(E|F)p(F)}{p(E|F)p(F) + p(E|\overline{F})p(\overline{F})}$$

## Slide 53 — Applying Bayes' Theorem

**Example**: Suppose that one person in 100,000 has a particular disease. There is a test for the disease that gives a positive result 99% of the time when given to someone with the disease. When given to someone without the disease, 99.5% of the time it gives a negative result. Find

a) the probability that a person who test positive has the disease.

b) the probability that a person who test negative does not have the disease.

Should someone who tests positive be worried?

## Slide 54 — Applying Bayes' Theorem

**Solution**: Let D be the event that the person has the disease, and E be the event that this person tests positive. We need to compute p(D|E) from p(D), p(E|D), p(E|D̄), p(D̄).

$$p(D) = 1/100{,}000 = 0.00001 \qquad p(\overline{D}) = 1 - 0.00001 = 0.99999$$

$$p(E|D) = .99 \qquad p(\overline{E}|D) = .01 \qquad p(E|\overline{D}) = .005 \qquad p(\overline{E}|\overline{D}) = .995$$

$$p(D|E) = \frac{p(E|D)p(D)}{p(E|D)p(D) + p(E|\overline{D})p(\overline{D})} = \frac{(0.99)(0.00001)}{(0.99)(0.00001) + (0.005)(0.99999)} \approx 0.002$$

Note: "Can you use this formula to explain why the resulting probability is surprisingly small?"

Note: "So, don't worry too much, if your test for this disease comes back positive."

## Slide 55 — Applying Bayes' Theorem

- What if the result is negative?

Note: "So, the probability you have the disease if you test negative is $p(D|\overline{E}) \approx 1 - 0.9999999 = 0.0000001.$"

$$p(\overline{D}|\overline{E}) = \frac{p(\overline{E}|\overline{D})p(\overline{D})}{p(\overline{E}|\overline{D})p(\overline{D}) + p(\overline{E}|D)p(D)} = \frac{(0.995)(0.99999)}{(0.995)(0.99999) + (0.01)(0.00001)} \approx 0.9999999$$

- So, it is extremely unlikely you have the disease if you test negative.

## Slide 56 — Generalized Bayes' Theorem

**Generalized Bayes' Theorem**: Suppose that E is an event from a sample space S and that F₁, F₂, …, Fₙ are mutually exclusive events such that

$$\bigcup_{i}^{n} F_i = S.$$

Assume that p(E) ≠ 0 for i = 1, 2, …, n. Then

$$p(F_j|E) = \frac{p(E|F_j)p(F_j)}{\sum_{i=1}^{n} p(E|F_i)p(F_i)}.$$

## Slide 57 — Bayesian Spam Filters

- How do we develop a tool for determining whether an email is likely to be spam?
- If we have an initial set B of spam messages and set G of non-spam messages. We can use this information along with Bayes' law to predict the probability that a new email message is spam.
- We look at a particular word w, and count the number of times that it occurs in B and in G; n_B(w) and n_G(w).
  - Estimated probability that an email containing w is spam: p(w) = n_B(w)/|B|
  - Estimated probability that an email containing w is not spam: q(w) = n_G(w)/|G|

## Slide 58 — Bayesian Spam Filters

- Let S be the event that the message is spam, and E be the event that the message contains the word w.
- Using Bayes' rule

$$p(S|E) = \frac{p(E|S)p(S)}{p(E|S)p(S) + p(E|\overline{S})p(\overline{S})}$$

$$p(S|E) = \frac{p(E|S)}{p(E|S) + p(E|\overline{S})}$$

Note: "Assuming that it is equally likely that an arbitrary message is spam and is not spam; i.e., p(S) = ½."

## Slide 59 — Bayesian Spam Filters

$$r(w) = \frac{p(w)}{p(w) + q(w)}$$

Note: "Using our empirical estimates of p(E | S) and p(E | S̄)."

Note: "r(w) estimates the probability that the message is spam. We can class the message as spam if r(w) is above a **threshold**."

## Slide 60 — Bayesian Spam Filters

**Example**: We find that the word "Rolex" occurs in 250 out of 2000 spam messages and occurs in 5 out of 1000 non-spam messages. Estimate the probability that an incoming message is spam. Suppose our threshold for rejecting the email is 0.9.

**Solution**: p(Rolex) = 250/2000 = .125 and q(Rolex) = 5/1000 = 0.005.

$$r(Rolex) = \frac{p(Rolex)}{p(Rolex) + q(Rolex)} = \frac{0.125}{0.125 + .005} \approx 0.962$$

Note: "We class the message as spam and reject the email!"

## Slide 61 — Bayesian Spam Filters using Multiple Words

- Accuracy can be improved by considering more than one word as evidence.
- Consider the case where E₁ and E₂ denote the events that the message contains the words w₁ and w₂ respectively.
- We make the simplifying assumption that the events are independent. And again we assume that p(S) = ½.

$$p(S|E_1 \cap E_2) = \frac{p(E_1|S)p(E_2|S)}{p(E_1|S)p(E_2|S) + p(E_1|\overline{S})p(E_2|\overline{S})}$$

$$r(w_1, w_2) = \frac{p(w_1)p(w_2)}{p(w_1)p(w_2) + q(w_1)q(w_2)}$$

## Slide 62 — Bayesian Spam Filters using Multiple Words

**Example**: We have 2000 spam messages and 1000 non-spam messages.

- The word "stock" occurs 400 times in the spam messages and 60 times in the non-spam.
- The word "undervalued" occurs in 200 spam messages and 25 non-spam.

## Slide 63 — Bayesian Spam Filters using Multiple Words

**Solution**: p(stock) = 400/2000 = .2

q(stock) = 60/1000 = .06

p(undervalued) = 200/2000 = .1

q(undervalued) = 25/1000 = .025

$$r(stock, undervalued) = \frac{p(stock)\,p(undervalued)}{p(stock)\,p(undervalued) + q(stock)\,q(undervalued)} = \frac{(0.2)(0.1)}{(0.2)(0.1)+(0.06)(0.025)} \approx 0.930$$

Note: "If our threshold is .9, we class the message as spam and reject it."

Footer credit on slide: CPE121 Discrete Mathematics for Computer Engineering

## Slide 64 — Bayesian Spam Filters using Multiple Words

In general, the more words we consider, the more accurate the spam filter. With the independence assumption if we consider k words:

$$p\!\left(S \,\middle|\, \bigcap_{i=1}^{k} E_i\right) = \frac{\prod_{i=1}^{k} p(E_i|S)}{\prod_{i=1}^{k} p(E_1|S) + \prod_{i=1}^{k} p(E_i|\overline{S})}$$

$$r(w_1, w_2, \ldots w_n) = \frac{\prod_{i}^{k} p(w_i)}{\prod_{i=1}^{k} p(w_i) + \prod_{i=1}^{k} q(w_i)}$$

*(Note: the first formula's denominator is transcribed exactly as printed on the slide — the first product term reads `p(E₁|S)` rather than `p(Eᵢ|S)`, which appears to be a typo in the original.)*

Note: "We can further improve the filter by considering pairs of words as a single block or certain types of strings."

## Slide 65 — Discriminant analysis

Section 3

## Slide 66 — Linear classification

- Focus on linear classification model, i.e., the decision boundary is a linear function of **x**
  - Defined by (D – 1)-dimensional hyperplane
- If the data can be separated exactly by linear decision surfaces, they are called **linearly separable**
- Implicit assumption: Classes can be modeled well by Gaussians
- Simply speaking, treat **classification as a projection** problem

Citation: From PRML (Bishop, 2006)

*Figure: 2D scatter plot with blue and red points separated by a diagonal decision line, reproduced from Bishop's Pattern Recognition and Machine Learning (2006).*

## Slide 67 — Projection

- Assume we know the basic vector **w**, we can compute the projection, y, of any points, **x**.
- Threshold w₀, such that we decide on C₁ if y ≧ w₀ and C₂ otherwise.

*Figure: Diagram of a projection axis vector w with a threshold point w₀ marked; red squares (class C₁) and blue x-marks (class C₂) are each connected by dashed lines to their projected positions along the w axis.*

## Slide 68 — LDA

Citation: From PRML (Bishop, 2006)

- Separate samples of distinct groups by projecting them onto a space that
  - Maximize their between-class separability while
  - Minimize their within-class variability

*Figure: Scatter plot of two classes (blue and red points) with histograms of their 1D projections shown on the left axis, and green lines indicating class means connected along the projection direction.*

## Slide 69 — Linear discriminant analysis

- We model the distribution of the predictors X separately in each of the response classes (i.e. given Y), and then use Bayes' theorem to flip these around into estimates for Pr(Y = k | X = x)
- Assume that we have 1 predictor
- Suppose we assume that fₖ(x) is normal or Gaussian

$$f_k(x) = \frac{1}{\sqrt{2\pi}\,\sigma_k} \exp\left(-\frac{1}{2\sigma_k^2}(x - \mu_k)^2\right)$$

## Slide 70 — Bayes' theorem for classification

- Let πₖ be the overall or prior probability of the kth class;
- This is the probability that a given observation is associated with the kth category of the response variable Y.
- Let fₖ(x) ≡ Pr(X = x|Y = k) denote the density function of X for an observation that comes from the kth class

$$\Pr(Y = k|X = x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^{K} \pi_l f_l(x)}.$$

## Slide 71 — Bayes' theorem for classification

$$p_k(x) = \frac{\pi_k \dfrac{1}{\sqrt{2\pi}\sigma}\exp\left(-\dfrac{1}{2\sigma^2}(x-\mu_k)^2\right)}{\sum_{l=1}^{K}\pi_l \dfrac{1}{\sqrt{2\pi}\sigma}\exp\left(-\dfrac{1}{2\sigma^2}(x-\mu_l)^2\right)}.$$

Taking a log, we get

$$\delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \log(\pi_k)$$

We will assign x to class k if δₖ(x) is largest.

## Slide 72 — Deriving Bayes' classifier solution

$$p_k(x) = \frac{\pi_k \dfrac{1}{\sqrt{2\pi}\sigma}\exp\left(-\dfrac{1}{2\sigma^2}(x-\mu_k)^2\right)}{p(X=x)}$$

$$\log(p_k(x)) = \log(\pi_k) + \log\left(\frac{1}{\sqrt{2\pi}\sigma}\right) + \log\left(\exp\left(-\frac{1}{2\sigma^2}(x-\mu_k)^2\right)\right) - \log(p(X=x))$$

$$\log(p_k(x)) = \log(\pi_k) + \log\left(\frac{1}{\sqrt{2\pi}\sigma}\right) + \left(-\frac{1}{2\sigma^2}(x-\mu_k)^2\right) - \log(p(X=x))$$

$$\log(p_k(x)) = \log(\pi_k) + \log\left(\frac{1}{\sqrt{2\pi}\sigma}\right) - \frac{x^2}{2\sigma^2} + \frac{x\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} - \log(p(X=x))$$

$$\delta_k(x) = \log(\pi_k) + \frac{x\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2}$$

## Slide 73 — Linear discriminant analysis (LDA)

The linear discriminant analysis method approximates the Bayes classifier by plugging estimates for πₖ, μₖ, and σ²:

$$\hat{\mu}_k = \frac{1}{n_k}\sum_{i: y_i = k} x_i$$

$$\hat{\sigma}^2 = \frac{1}{n-K}\sum_{k=1}^{K}\sum_{i: y_i = k} (x_i - \hat{\mu}_k)^2$$

$$\hat{\pi}_k = n_k/n.$$

## Slide 74 — LDA discriminant function

Assign x to class k if

$$\hat{\delta}_k(x) = x \cdot \frac{\hat{\mu}_k}{\hat{\sigma}^2} - \frac{\hat{\mu}_k^2}{2\hat{\sigma}^2} + \log(\hat{\pi}_k)$$

is the largest

## Slide 75 — Bayes decision boundary and LDA

**FIGURE 4.4.** Left: Two one-dimensional normal density functions are shown. The dashed vertical line represents the Bayes decision boundary. Right: 20 observations were drawn from each of the two classes, and are shown as histograms. The Bayes decision boundary is again shown as a dashed vertical line. The solid vertical line represents the LDA decision boundary estimated from the training data.

*Figure: Left — two overlapping bell-curve density functions (green and pink) with a dashed vertical line marking the Bayes decision boundary at x=0. Right — histograms of 20 observations per class with both the dashed Bayes boundary and a solid LDA-estimated boundary shown.*

## Slide 76 — Figure 4.5

**FIGURE 4.5.** Two multivariate Gaussian density functions are shown, with p = 2. Left: The two predictors are uncorrelated. Right: The two variables have a correlation of 0.7.

*Figure: Two 3D bell-shaped surface plots of bivariate Gaussian densities over X₁, X₂ — left shows a symmetric (uncorrelated) bump; right shows a tilted/elongated (correlated, ρ = 0.7) bump.*

## Slide 77 — Discriminant analysis with more than one predictors

**FIGURE 4.6.** An example with three classes. The observations from each class are drawn from a multivariate Gaussian distribution with p = 2, with a class-specific mean vector and a common covariance matrix. Left: Ellipses that contain 95% of the probability for each of the three classes are shown. The dashed lines are the Bayes decision boundaries. Right: 20 observations were generated from each class, and the corresponding LDA decision boundaries are indicated using solid black lines. The Bayes decision boundaries are once again shown as dashed lines.

*Figure: Two scatter plots (X₁ vs X₂) with three classes (orange, teal, blue). Left shows 95%-probability ellipses per class with dashed Bayes decision boundaries. Right shows the 20 sampled points per class with solid black LDA decision boundaries and dashed Bayes boundaries overlaid.*

## Slide 78 — Quadratic Discriminant Analysis

A generic class of discriminant analysis

From the distribution function, if we take log of the function

$$\log P(y=k|x) = \log P(x|y=k) + \log P(y=k) + Cst$$

$$= -\frac{1}{2}\log|\Sigma_k| - \frac{1}{2}(x-\mu_k)^t \Sigma_k^{-1}(x-\mu_k) + \log P(y=k) + Cst,$$

where the constant term Cst corresponds to the denominator P(x), in addition to other constant terms from the Gaussian. The predicted class is the one that maximises this log-posterior.

LDA is a special case of LDA when each class assume shared covariance.

*(Note: the last sentence is transcribed exactly as printed on the slide. It reads "LDA is a special case of LDA..." which appears to be a typo in the original — likely intended to read "QDA is a special case of LDA" or "LDA is a special case of QDA," since LDA is normally described as QDA restricted to a shared/common covariance matrix across classes.)*

## Slide 79 — Accuracy, Precision and Recall

| | Actual Positive (p) | Actual Negative (n) |
|---|---|---|
| The model says "Yes" = positive (y) | True positives | False positives |
| The model says "No" = not positive (n) | False negatives | True negatives |

- Accuracy = (TP + TN)/(TP + FP + TN + FN)
- Recall (Completeness) = true positive rate = TP/(TP + FN)
- Precision (Exactness) = the accuracy over the cases predicted to be positive, TP/(TP + FP)
- F-measure = the harmonic mean of precision and recall = the balance between recall and precision

$$= 2 \cdot \frac{precision * recall}{precision + recall}$$

*Figure: Diagram (same style as Slide 31) illustrating "relevant elements" vs "selected elements" as overlapping regions showing true positives, false positives, false negatives, true negatives, with pie-slice icons illustrating the Precision and Recall formulas.*

## Slide 80 — Receiver operating characteristics / Area under the ROC curve

True Positive Rate (TPR) is a synonym for recall and is therefore defined as follows:

$$TPR = \frac{TP}{TP+FN}$$

False Positive Rate (FPR) is defined as follows:

$$FPR = \frac{FP}{FP+TN}$$

Figure 5. AUC (Area under the ROC Curve).

Figure 4. TP vs. FP rate at different classification thresholds.

*Figure: Left — ROC curve (TP Rate vs FP Rate) with the area under the curve shaded gray. Right — a similar ROC curve annotated with callout boxes pointing to points on the curve labeled "TP vs. FP rate at one decision threshold" and "TP vs. FP rate at another decision threshold".*

## Slide 81 — AUC - ROC

| AUC values | Test quality |
|---|---|
| 0.9–1.0 | Excellent |
| 0.8–0.9 | Very good |
| 0.7–0.8 | Good |
| 0.6–0.7 | Satisfactory |
| 0.5–0.6 | Unsatisfactory |

*Figure: ROC space plot (True Positive vs False Positive) showing two ROC curves — "ROC 1 (AUC = 0.9)" (closer to the top-left corner, better) and "ROC 2 (AUC = 0.65)" (closer to the diagonal, worse) — plus the diagonal chance line.*

## Slide 82 — Coding Practice

- Implementing linear discriminant analysis (LDA) in Python - IBM Developer *(hyperlink)*
- Linear Discriminant Analysis Made Simple & How To Tutorial (spotintelligence.com) *(hyperlink)*

## Slide 83 — End of Lecture 1

End of Lecture 1

Question?

*Figure: Big Data Experience Center logo.*
