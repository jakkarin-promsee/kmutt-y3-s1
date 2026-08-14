# Lecture 2 — Training Models (text cache)

> Auto-generated Markdown cache of [[Lecture+2+-+Training+Models.pdf]] (38 slides), generated 2026-08-15 by a Sonnet subagent reading all 38 slides. Formulas transcribed as LaTeX; figures described in italics. This is a lossy proxy — open the PDF for exact figures and layout.

## Slide 1 — Machine Learning

- **Machine Learning**
- Lecture 2: Training Models
- **Asst. Prof. Dr. Santitham Prom-on**
- Department of Computer Engineering, Faculty of Engineering
- King Mongkut's University of Technology Thonburi

*Figure: Title slide with CPE department logo (top left), KMUTT logo (bottom left), and Big Data Experience Center logo (bottom right).*

## Slide 2 — Topics

- Direct approach: linear regression with ordinary least square
- Iterative approach
  - Gradient descent
  - Batch gradient descent
  - Stochastic gradient descent
  - Mini-batch gradient descent
- Logistic regression

Notebook: https://colab.research.google.com/drive/1jcPGje7ymfGZLL9C2OV0VdqJQXWpe7h9?usp=sharing

## Slide 3 — Model training

Two different ways

- Using a direct "closed-form" equation.
- Using an iterative optimization approach.

## Slide 4 — Direct approach: Linear regression with Ordinary Least Square (OLS)

- Linear regression model can be expressed by the following formula

$$\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \ldots + \theta_n x_n$$

$$y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \ldots + \theta_n x_n + \varepsilon$$

where

- $\hat{y}$ is the predicted value
- $n$ is the number of features
- $x_i$ is the $i^{th}$ feature value

## Slide 5 — Simple linear regression

$$Y_i = \alpha + \beta X_i + \varepsilon_i$$

$$e_i \sim N(0, \sigma^2) \quad i.i.d.$$

$$\varepsilon_i \text{ is independent of } X_i$$

- The intercept is $\alpha$
- The slope is $\beta$
- We use the normal distribution to describe the "error"

## Slide 6 — Method of least squares

- Choose the $\beta$'s so that the sum of the squares of the errors, $\varepsilon_i$, are minimized
- The least squares function is

$$S = \sum_{i=1}^{n} \varepsilon_i^2 = \sum_{i=1}^{n} \left(y_i - \alpha - \beta x_i\right)^2$$

## Slide 7 — OLS solution

Minimum of a function is the point where the slope is zero

*Figure: Plot of $E(\alpha)$ (y-axis) vs $\alpha$ (x-axis) — a convex, bowl-shaped blue curve. A red dot marks the minimum, with a red horizontal arrow pointing right from the minimum along the flat (zero-slope) direction, illustrating that the minimum occurs where the derivative is zero.*

## Slide 8 — Derivative of the error functions

The function S is to be minimized with respect to $\beta_0, \beta_1$

$$\frac{\partial S}{\partial \alpha} = -2\sum_{i=1}^{n}\left(y_i - \alpha - \beta x_i\right) = 0$$

and

$$\frac{\partial S}{\partial \beta} = -2\sum_{i=1}^{n}\left(y_i - \alpha - \beta x_i\right)x_i = 0$$

## Slide 9 — Least square normal equation

$$n\alpha + \beta \sum_{i=1}^{n} x_i = \sum_{i=1}^{n} y_i$$

$$\alpha \sum_{i=1}^{n} x_i + \beta \sum_{i=1}^{n} x_i^2 = \sum_{i=1}^{n} x_i y_i$$

## Slide 10 — Find alpha (intercept)

$$\alpha = \frac{\begin{vmatrix} \displaystyle\sum_{i=1}^{n} y_i & \displaystyle\sum_{i=1}^{n} x_i \\[6pt] \displaystyle\sum_{i=1}^{n} x_i y_i & \displaystyle\sum_{i=1}^{n} x_i^2 \end{vmatrix}}{\begin{vmatrix} n & \displaystyle\sum_{i=1}^{n} x_i \\[6pt] \displaystyle\sum_{i=1}^{n} x_i & \displaystyle\sum_{i=1}^{n} x_i^2 \end{vmatrix}} = \frac{\displaystyle\sum_{i=1}^{n} x_i^2 \sum_{i=1}^{n} y_i - \sum_{i=1}^{n} x_i y_i \sum_{i=1}^{n} x_i}{\displaystyle n\sum_{i=1}^{n} x_i^2 - \left(\sum_{i=1}^{n} x_i\right)^2}$$

## Slide 11 — Find beta (slope)

$$\beta = \frac{\begin{vmatrix} n & \displaystyle\sum_{i=1}^{n} y_i \\[6pt] \displaystyle\sum_{i=1}^{n} x_i & \displaystyle\sum_{i=1}^{n} x_i y_i \end{vmatrix}}{\begin{vmatrix} n & \displaystyle\sum_{i=1}^{n} x_i \\[6pt] \displaystyle\sum_{i=1}^{n} x_i & \displaystyle\sum_{i=1}^{n} x_i^2 \end{vmatrix}} = \frac{\displaystyle n\sum_{i=1}^{n} x_i y_i - \sum_{i=1}^{n} x_i \sum_{i=1}^{n} y_i}{\displaystyle n\sum_{i=1}^{n} x_i^2 - \left(\sum_{i=1}^{n} x_i\right)^2}$$

## Slide 12 — Example: Multiple regression

| x₁  | x₂  | y   |
| --- | --- | --- |
| 1   | 2   | 12  |
| 2   | 1   | 9   |
| 3   | 2   | 19  |
| 1   | 1   | 8   |

$$y = c_1 x_1 + c_2 x_2 + c_3$$

$$c_1 + 2c_2 + c_3 = 12$$
$$2c_1 + c_2 + c_3 = 9$$
$$3c_1 + 2c_2 + c_3 = 19$$
$$c_1 + c_2 + c_3 = 8$$

$$\begin{bmatrix} 1 & 2 & 1 \\ 2 & 1 & 1 \\ 3 & 2 & 1 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} c_1 \\ c_2 \\ c_3 \end{bmatrix} = \begin{bmatrix} 12 \\ 9 \\ 19 \\ 8 \end{bmatrix}$$

## Slide 13 — Pseudoinverse

- **Y** — $N \times 1$ vector
- **A** — $N \times M$ matrix, where $M$ is the number of parameters
- **B** — $M \times 1$ vector

$$\mathbf{Y} = \mathbf{A}\mathbf{B}$$
$$\mathbf{A}\mathbf{B} = \mathbf{Y}$$
$$\mathbf{A}^T\mathbf{A}\mathbf{B} = \mathbf{A}^T\mathbf{Y}$$
$$\underbrace{\left(\mathbf{A}^T\mathbf{A}\right)^{-1}\mathbf{A}^T\mathbf{A}}_{=\,\mathbf{I}}\mathbf{B} = \left(\mathbf{A}^T\mathbf{A}\right)^{-1}\mathbf{A}^T\mathbf{Y}$$
$$\mathbf{B} = \left(\mathbf{A}^T\mathbf{A}\right)^{-1}\mathbf{A}^T\mathbf{Y}$$

(The slide marks the $\left(\mathbf{A}^T\mathbf{A}\right)^{-1}\mathbf{A}^T\mathbf{A}$ term with an underbrace to show it cancels to the identity, giving the pseudoinverse solution for $\mathbf{B}$.)

## Slide 14 — Python: pseudoinverse

```python
A = np.array([[1,2,1],
              [2,1,1],
              [3,2,1],
              [1,1,1]])
print(A)
```

```
[[1 2 1]
 [2 1 1]
 [3 2 1]
 [1 1 1]]
```

```python
B = np.array([12,9,19,8])
B.shape = (-1,1)
print(B)
```

```
[[12]
 [ 9]
 [19]
 [ 8]]
```

```python
np.matmul(np.linalg.pinv(A),B)
```

```
array([[ 3. ],
       [ 5.5],
       [-1.5]])
```

## Slide 15 — Iterative approach: Gradient descent

- A very generic optimization algorithm capable of finding optimal solutions to a wide range of problems.

Suppose you are lost in the mountains in a dense fog; you can only feel the slope of the ground below your feet.

A good strategy to get to the bottom of the valley quickly is to go downhill in the direction of the steepest slope.

*Figure: Cost (y-axis) vs $\theta$ (x-axis) — a convex, bowl-shaped curve. A sequence of purple dots starts at a "Random initial value" near the top-left and steps down the curve via decreasing "Learning step" arcs, converging to the "Minimum" (yellow dot) marked $\hat{\theta}$. Captioned "Figure 4-3. Gradient Descent" (from Géron).*

## Slide 16 — Nonlinear Least Square

- Suppose that we have a sample of $n$ observations on the response and the regressor, say, $y_i, x_{i1}, x_{i2}, \ldots, x_{ik}$ for $i=1,2,\ldots,n$
- The least square method involves minimizing the least square function

$$S(\boldsymbol{\beta}) = \sum_{i=1}^{n} \left[y_i - f(\mathbf{x}_i, \boldsymbol{\beta})\right]^2$$

## Slide 17 — Nonlinear objective function

Non-linear objective function

Unsolvable for roots of derivative of error

$$\frac{dE}{dx} = e^{-x}$$

*Figure: Plot of Error $E(x)$ (y-axis) vs $x$ (x-axis) — a wiggly, non-convex blue curve with several local dips and a deeper minimum toward the right, illustrating that a nonlinear objective function can have multiple local minima and no closed-form root for its derivative.*

## Slide 18 — Gradient Descent Basic 1: Objective function

Minimum of a function is found by following the slope of the function

*Figure: Plot of $f$ (y-axis, range 1–10) vs $x$ (x-axis, range 1–12). A red curve $f(x)$ (roughly parabolic) has its minimum $f(m)$ at $x = m \approx 5.3$ (marked with blue dashed guide lines). A blue point labeled "guess" sits on the curve around $x \approx 10$–$11$, $f \approx 7$, with a black arrow tangent to the curve there showing the local slope direction. Source: http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf*

## Slide 19 — Gradient Descent Basic 2: Moving opposite to gradient

*Figure: Same $f(x)$ plot as Slide 18. A new point labeled "next step" appears below and to the left of "guess" (around $x \approx 9$–$10$, $f \approx 5$), with a green curved arrow from "guess" to "next step" showing a move opposite the gradient (downhill, toward smaller $x$ and $f$). Source: http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf*

## Slide 20 — Gradient Descent Basic 3: Iterative gradient evaluation

*Figure: Same $f(x)$ plot. From "next step" a new black tangent arrow labeled "new gradient" is drawn, showing the slope re-evaluated at the updated point; the earlier "guess" point and its tangent are still shown above/right. Source: http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf*

## Slide 21 — Gradient Descent Basic 4: Moving opposite to gradient

*Figure: Same $f(x)$ plot, now with three points connected by green curved arrows stepping down the curve from "guess" through intermediate points to "next step," each step following the locally re-evaluated gradient. Source: http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf*

## Slide 22 — Gradient Descent Basic 5: Iteratively descent opposite to the gradient

*Figure: Same $f(x)$ plot showing a full chain of black dots connected by green curved arrows, descending stepwise from "guess" (upper right, $x \approx 11$, $f = 7$) down to "stop" at the minimum ($x = m \approx 5.3$, $f = f(m) \approx 1$), illustrating convergence of the iterative descent. Source: http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf*

## Slide 23 — Gradient Descent – algorithm (overview)

- Start with a point (randomly guessing)
- Repeat
  - Determine a descent direction
  - Choose a step
  - Update
- Until stopping criterion is satisfied

*Figure: Inset of the stepwise-descent plot from Slide 22 (points labeled "guess" and "stop" on the curve $f(x)$), with a red arrow pointing at the "guess" point to highlight the algorithm's starting point. Source: http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf*

## Slide 24 — Gradient Descent – algorithm (determine a descent direction)

- Start with a point (randomly guessing)
- Repeat
  - **Determine a descent direction**
  - Choose a step
  - Update
- Until stopping criterion is satisfied

*Figure: Same inset plot, with a red arrow and a "Di" label pointing at the "guess" point, highlighting that a descent direction $D_i$ is computed there.*

## Slide 25 — Gradient Descent – algorithm (choose a step)

- Start with a point (randomly guessing)
- Repeat
  - Determine a descent direction
  - **Choose a step**
  - Update
- Until stopping criterion is satisfied

*Figure: Same inset plot, with a red arrow and a short red double-tick bracket on the curve near $x \approx 9$–$10$, marking the step size being chosen along the descent direction.*

## Slide 26 — Gradient Descent – algorithm (update)

- Start with a point (randomly guessing)
- Repeat
  - Determine a descent direction
  - Choose a step
  - **Update**
- Until stopping criterion is satisfied

*Figure: Same inset plot, with a red arrow pointing at the "next step" point on the curve (around $x \approx 9$, $f \approx 5$), showing the parameter after the update.*

## Slide 27 — Gradient Descent – algorithm (stopping criterion)

- Start with a point (randomly guessing)
- Repeat
  - Determine a descent direction
  - Choose a step
  - Update
- **Until stopping criterion is satisfied**

*Figure: Same inset plot, with a red arrow pointing down to the "stop" point at the minimum, and a horizontal red line spanning from the descent path down to that stopping point, showing the algorithm terminating once the criterion is met.*

## Slide 28 — Gradient Descent – algorithm (formulas)

- Start with a point (randomly guessing) → Randomly guessing $\beta$
- Repeat
  - Determine a descent direction → $\text{direction} = -\dfrac{dS(\beta)}{d\beta}$
  - Choose a step → $\text{step} > 0$
  - Update → $\beta^{t+1} = \beta^{t} - \text{step}\dfrac{dS(\beta)}{d\beta}$
- Until stopping criterion is satisfied → $\dfrac{dS(\beta)}{d\beta} \approx 0$

Source: http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf

## Slide 29 — Batch Gradient Descent

- To implement Gradient Descent, you need to compute the gradient of the cost function with regards to each model parameter $\theta_j$.
- Batch gradient descent uses data of the whole batch to compute gradient

$$\frac{\partial}{\partial \theta_j}\text{MSE}(\boldsymbol{\theta}) = \frac{2}{m}\sum_{i=1}^{m}\left(\boldsymbol{\theta}^T \mathbf{x}^{(i)} - y^{(i)}\right)x_j^{(i)}$$

$$\boldsymbol{\theta}^{(\text{next step})} = \boldsymbol{\theta} - \eta \nabla_{\boldsymbol{\theta}} \text{MSE}(\boldsymbol{\theta})$$

## Slide 30 — Stochastic gradient descent

- Batch Gradient Descent uses the whole training set to compute the gradients at every step, which makes it very slow when the training set is large.
- Stochastic gradient descent samples random instances for training at each training step

*Figure: Contour plot of the cost function in $(\theta_1, \theta_2)$ space — concentric rings shaded from light (low cost, center) to dark (high cost, outer edge), forming a bullseye. A jagged purple path of connected dots bounces irregularly from the outer rings toward the center, illustrating the noisy, non-monotonic convergence path of stochastic gradient descent compared to batch gradient descent's smooth path. Captioned "Figure 4-9. Stochastic Gradient Descent" (from Géron).*

## Slide 31 — Mini-Batch Gradient Descent

- Both stochastic and use small batch
- Apply for small batch instead of an instance.
- Faster by GPU computing

**Algorithm 8.1** Stochastic gradient descent (SGD) update at training iteration $k$

```
Require: Learning rate ε_k
Require: Initial parameter θ
while stopping criterion not met do
    Sample a minibatch of m examples from the training set {x⁽¹⁾, …, x⁽ᵐ⁾} with
    corresponding targets y⁽ⁱ⁾.
    Compute gradient estimate: ĝ ← + (1/m) ∇_θ Σᵢ L(f(x⁽ⁱ⁾; θ), y⁽ⁱ⁾).
    Apply update: θ ← θ − ε ĝ.
end while
```

(Reproduced from Goodfellow, Bengio & Courville, *Deep Learning*, Algorithm 8.1.)

## Slide 32 — Example: Logistic Regression

Classification

*Figure: Scatter plot titled "Classification" (axes unlabeled). Blue circles cluster in the bottom-left region; purple plus-signs cluster in the top-right region. A red dashed diagonal line separates the two classes, representing the decision boundary that logistic regression would learn.*

## Slide 33 — Logistic regression

Logistic regression has the following mathematical formulae,

$$\log\left(\frac{H_{\boldsymbol{\theta}}(x_i)}{1-H_{\boldsymbol{\theta}}(x_i)}\right) = f(x_i) = \theta_0 + \sum_{i=1}^{n}\theta_i x_i$$

and

$$H_{\boldsymbol{\theta}}(x_i) = \frac{1}{1+e^{-f(x)}}.$$

## Slide 34 — Loss function

This function has a nice property that,

$$\frac{\partial}{\partial \boldsymbol{\theta}} H_{\boldsymbol{\theta}}(x_i) = H_{\boldsymbol{\theta}}(x_i)\left(1-H_{\boldsymbol{\theta}}(x_i)\right)x_i.$$

For logistic regression, we can formulate the loss function as follows,

$$J(\boldsymbol{\theta}) = \frac{1}{n}\sum_{i=1}^{n}\left[-y_i \log H_{\boldsymbol{\theta}}(x_i) - (1-y_i) \log\left(1-H_{\boldsymbol{\theta}}(x_i)\right)\right].$$

## Slide 35 — Gradient

$$\frac{\partial J(\boldsymbol{\theta})}{\partial \boldsymbol{\theta}} = \frac{\partial}{\partial \boldsymbol{\theta}}\left(\frac{1}{n}\sum_{i=1}^{n}\left(-y_i \log H_{\boldsymbol{\theta}}(x_i) - (1-y_i)\log\left(1-H_{\boldsymbol{\theta}}(x_i)\right)\right)\right)$$

$$= \frac{1}{n}\sum_{i=1}^{n}\left(-y_i \frac{\partial}{\partial \boldsymbol{\theta}}\log H_{\boldsymbol{\theta}}(x_i) - (1-y_i)\frac{\partial}{\partial \boldsymbol{\theta}}\log\left(1-H_{\boldsymbol{\theta}}(x_i)\right)\right)$$

$$= \frac{1}{n}\sum_{i=1}^{n}\left(-\frac{y_i}{H_{\boldsymbol{\theta}}(x_i)}\frac{\partial}{\partial \boldsymbol{\theta}}H_{\boldsymbol{\theta}}(x_i) - \frac{1-y_i}{1-H_{\boldsymbol{\theta}}(x_i)}\frac{\partial}{\partial \boldsymbol{\theta}}\left(1-H_{\boldsymbol{\theta}}(x_i)\right)\right)$$

$$= \frac{1}{n}\sum_{i=1}^{n}\left(-\frac{y_i}{H_{\boldsymbol{\theta}}(x_i)}H_{\boldsymbol{\theta}}(x_i)\left(1-H_{\boldsymbol{\theta}}(x_i)\right)x_i - \frac{1-y_i}{1-H_{\boldsymbol{\theta}}(x_i)}H_{\boldsymbol{\theta}}(x_i)\left(1-H_{\boldsymbol{\theta}}(x_i)\right)(-x_i)\right)$$

$$= \frac{1}{n}\sum_{i=1}^{n}\left(-y_i\left(1-H_{\boldsymbol{\theta}}(x_i)\right)x_i - (1-y_i)H_{\boldsymbol{\theta}}(x_i)(-x_i)\right)$$

$$= \frac{1}{n}\sum_{i=1}^{n}\left(-y_i\left(1-H_{\boldsymbol{\theta}}(x_i)\right) + (1-y_i)H_{\boldsymbol{\theta}}(x_i)\right)x_i$$

$$= \frac{1}{n}\sum_{i=1}^{n}\left(-y_i + y_i H_{\boldsymbol{\theta}}(x_i) + H_{\boldsymbol{\theta}}(x_i) - y_i H_{\boldsymbol{\theta}}(x_i)\right)x_i$$

$$= \frac{1}{n}\sum_{i=1}^{n}\left(H_{\boldsymbol{\theta}}(x_i) - y_i\right)x_i$$

## Slide 36 — Gradient descent

We can then iteratively update the parameters using the gradient descent approach,

$$\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - \alpha\frac{\partial J\boldsymbol{\theta}}{\partial \boldsymbol{\theta}} = \boldsymbol{\theta}^{(k)} - \alpha\left(\sum_{i=1}^{n}\left(H_{\boldsymbol{\theta}^{(k)}}(x_i) - y_i\right)x_i\right),$$

where $\alpha$ is the learning rate. The initial parameters $\boldsymbol{\theta}^{(0)}$ can be randomized or set to any values as the loss function is convex.

## Slide 37 — Results

*Figure: Scatter plot titled "Iteration: 1" with x-axis X1 (0–4) and y-axis X2 (0–4). Red circular points (Class 0) cluster in the lower-left; teal triangular points (Class 1) cluster in the upper-right. A gray diagonal decision-boundary line runs from lower-left to upper-right, separating the two classes — the logistic regression fit after 1 iteration of gradient descent.*

## Slide 38 — End of Lecture 3 / Question?

- End of Lecture 3
- Question?

*Figure: Closing slide with CPE and KMUTT logos (bottom left) and Big Data Experience Center logo (bottom right).*

> Note: the closing slide says "End of Lecture 3" even though the title slide and file are "Lecture 2: Training Models" — printed as-is on the slide, likely a copy-paste artifact from a reused/renumbered deck (see the class [[CPE342-machine-learning/CLAUDE|CLAUDE.md]] note about slide reuse across offerings).
