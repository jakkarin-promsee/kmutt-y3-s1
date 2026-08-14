# Engineering Economy Factors — formula sheet

Text cache of `Chapter+2+-+Engineering+Economy+Factors.pdf` (3 pages). Transcribed by reading the
pages: the PDF was produced by Aladdin Ghostscript 5.50 with non-standard font encoding, so
`pdftotext` returns pure mojibake for every line. This cache is the only readable text.

Notation: `i` = interest rate per period, `n` = number of periods, `r` = nominal rate for continuous
compounding, `g` = geometric growth rate, `A` = continuous (funds-flow) payment.

---

## Page 1 — Discrete Payments and Discrete Compounding

| Factor | Find | Given | Formula |
| --- | --- | --- | --- |
| **Single-Payment** | | | |
| Compound-Amount | F | P | $F = P(1+i)^n = P(F/P, i, n)$ |
| Present-Worth | P | F | $P = F\dfrac{1}{(1+i)^n} = F(P/F, i, n)$ |
| **Equal-Payment Series** | | | |
| Compound-Amount | F | A | $F = A\left[\dfrac{(1+i)^n - 1}{i}\right] = A(F/A, i, n)$ |
| Sinking-Fund | A | F | $A = F\left[\dfrac{i}{(1+i)^n - 1}\right] = F(A/F, i, n)$ |
| Present-Worth | P | A | $P = A\left[\dfrac{(1+i)^n - 1}{i(1+i)^n}\right] = A(P/A, i, n)$ |
| Capital-Recovery | A | P | $A = P\left[\dfrac{i(1+i)^n}{(1+i)^n - 1}\right] = P(A/P, i, n)$ |
| **Uniform-Gradient Series** | A | G | $A = G\left[\dfrac{1}{i} - \dfrac{n}{(1+i)^n - 1}\right] = G(A/G, i, n)$ |
| **Geometric-Gradient Series** | P | $F_1, g$ | $P = \dfrac{F_1}{(i-g)}\left[1 - \dfrac{(1+g)^n}{(1+i)^n}\right]$ |
| **Infinite Series** | P | A | $P = A\left[\dfrac{1}{i}\right] = A(P/A, i, \infty)$, $i > 0$ |
| | P | G | $P = G\left[\dfrac{1}{i^2}\right] = G(P/G, i, \infty)$, $i > 0$ |
| | P | $F_1, g$ | $P = \dfrac{F_1}{(i-g)}$, $i > g$ |

## Page 2 — Discrete Payments and Continuous Compounding

| Factor | Find | Given | Formula |
| --- | --- | --- | --- |
| **Single-Payment** | | | |
| Compound-Amount | F | P | $F = Pe^{rn} = P[F/P, r, n]$ |
| Present-Worth | P | F | $P = Fe^{-rn} = F[P/F, r, n]$ |
| **Equal-Payment Series** | | | |
| Compound-Amount | F | A | $F = A\left[\dfrac{e^{rn} - 1}{e^r - 1}\right] = A[F/A, r, n]$ |
| Sinking-Fund | A | F | $A = F\left[\dfrac{e^r - 1}{e^{rn} - 1}\right] = F[A/F, r, n]$ |
| Present-Worth | P | A | $P = A\left[\dfrac{1 - e^{-rn}}{e^r - 1}\right] = A[P/A, r, n]$ |
| Capital-Recovery | A | P | $A = P\left[\dfrac{e^r - 1}{1 - e^{-rn}}\right] = P[A/P, r, n]$ |

### Continuous Payments and Continuous Compounding

| Factor | Find | Given | Formula |
| --- | --- | --- | --- |
| Funds Flow Conversion | A | $\bar{A}$ | $A = \bar{A}\left[\dfrac{e^r - 1}{r}\right] = \bar{A}[A/\bar{A}, r]$ |
| **Equal-Payment Series** | | | |
| Compound-Amount | F | $\bar{A}$ | $F = \bar{A}\left[\dfrac{e^{rn} - 1}{r}\right] = \bar{A}[F/\bar{A}, r, n]$ |
| Sinking-Fund | $\bar{A}$ | F | $\bar{A} = F\left[\dfrac{r}{e^{rn} - 1}\right] = F[\bar{A}/F, r, n]$ |
| Present-Worth | P | $\bar{A}$ | $P = \bar{A}\left[\dfrac{e^{rn} - 1}{re^{rn}}\right] = \bar{A}[P/\bar{A}, r, n]$ |
| Capital-Recovery | $\bar{A}$ | P | $\bar{A} = P\left[\dfrac{re^{rn}}{e^{rn} - 1}\right] = P[\bar{A}/P, r, n]$ |

## Page 3 — Conventional Loan Payment Formulas

$$A = P(A/P, i, n)$$
$$R_t = A(P/A, i, n-t) = P(F/P, i, t) - A(F/A, i, t)$$
$$I_t = iR_{(t-1)} = iA(P/A, i, n-t+1)$$
$$B_t = A - I_t$$

**Fixed loan particulars**

- $P$ — the principal amount of the loan
- $A$ — the loan payment amount
- $i$ — the interest rate
- $n$ — the number of payments

**Time-dependent quantities** (at time $t$)

- $R_t$ — the remaining balance after making the payment
- $I_t$ — the part of the payment going toward interest
- $B_t$ — the part of the payment going toward principal

$$\text{total paid toward principal} = P - R_t$$
$$\text{total paid toward interest} = tA - (P - R_t)$$
$$\text{equity} = \text{market value} - R_t$$
