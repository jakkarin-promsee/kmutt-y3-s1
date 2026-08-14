# Chapter 2 — Factors, Effect of Time & Interest on Money

Text cache of `Chapter+2+-+Factors,+Effect+of+Time+&+Interest+on+Money.pdf` (26 slides), PRE380
Engineering Economy, Dr. Suriyaphong Nilsang. Transcribed by reading the page images, because the
cash-flow diagrams are images that `pdftotext` drops entirely.

---

## Slide 2-1 — Chapter 2: Factors, Effect of Time & Interest on Money

*[Footer on this slide misprints as "1-1" instead of "2-1".]*

Title slide. Left sidebar (rotated text, repeated on every slide): "PRE 380 Engineering Economy".

Cover art: the textbook cover "ENGINEERING ECONOMY" next to a photo of a bird's nest holding
rolled-up US dollar bills like eggs.

**Chapter 2:**
**Factors, Effect of Time & Interest on Money**

Dr. Suriyaphong Nilsang

This material is modified and based on the presentation by Blank and Tarquin (2012) 7th Edition

---

## Slide 2-2 — Learning Outcomes

1. F/P and P/F Factors
2. P/A and A/P Factors
3. F/A and A/F Factors
4. Factor Values
5. Arithmetic Gradient
6. Geometric Gradient
7. Find i or n

---

## Slide 2-3 — Commonly used Symbols

- t = **Time**, usually in periods such as years or months
- P = **Present**, value or amount of money at a time *t* designated as present or time 0
- F = **Future**, value or amount of money at some future time, such as at *t = n* periods in the
  future
- A = **Annual**, series of consecutive, equal, end-of-period amounts of money
- n = **number of interest periods**; years, months
- i = **interest rate or rate of return** per time period; percent per year or month

---

## Slide 2-4 — Single Payment Factors (F/P and P/F)

Single payment factors involve only P and F. Cash flow diagrams are as follows:

*(a) Find F given P — thick/emphasized arrows mark the diagram's own unknowns as drawn; timeline
runs from 0 to n with a break shown between period 2 and period n-2 to indicate skipped periods.)*

```
                                                     F = ?
                                                       ^
                                                       |
  0-----1-----2----//----(n-2)-----(n-1)-----n     (i = given)
       |
       v
   P = given
```

*(b) Find P given F — same timeline shape; F is the given quantity at period n, P is the sought
quantity at period 0.)*

```
   F = given
       ^
       |
  0-----1-----2----//----(n-2)-----(n-1)-----n     (i = given)
       |
       v
   P = ?
```

**Formulas are as follows:**

$$F = P(1 + i)^n \qquad\qquad P = F\left[\frac{1}{(1+i)^n}\right]$$

Terms in parentheses or brackets are called *factors*. Values are in tables for i and n values.

Factors are represented in standard factor notation such as *(F/P,i,n)*, where letter to left of
slash is what is sought; letter to right represents what is given.

---

## Slide 2-5 — F/P and P/F Interest Factors

Compound Interest Factors table for **i = 8%**. Column groups: Single Payment (Compound Amount
Factor F/P — Find F Given P; Present Worth Factor P/F — Find P Given F), Uniform Payment Series
(Sinking Fund Factor A/F — Find A Given F; Capital Recovery Factor A/P — Find A Given P; Compound
Amount Factor F/A — Find F Given A; Present Worth Factor P/A — Find A Given A... i.e. Find P Given
A), Arithmetic Gradient (Gradient Uniform Series A/G — Find A Given G; Gradient Present Worth P/G —
Find P Given G).

*The slide draws a red box around the n = 10 row's F/P and P/F columns, highlighting the exact
values needed for the "Finding Future Value" example on Slide 2-8 (10-year, 8% problem).*

| n  | F/P (Find F, Given P) | P/F (Find P, Given F) | A/F (Find A, Given F) | A/P (Find A, Given P) | F/A (Find F, Given A) | P/A (Find P, Given A) | A/G (Find A, Given G) | P/G (Find P, Given G) |
|----|------------------------|------------------------|-------------------------|-------------------------|------------------------|------------------------|------------------------|------------------------|
| 1  | 1.080 | .9259 | 1.0000 | 1.0800 | 1.000  | 0.926 | 0     | 0      |
| 2  | 1.166 | .8573 | .4808  | .5608  | 2.080  | 1.783 | 0.481 | 0.857  |
| 3  | 1.260 | .7938 | .3080  | .3880  | 3.246  | 2.577 | 0.949 | 2.445  |
| 4  | 1.360 | .7350 | .2219  | .3019  | 4.506  | 3.312 | 1.404 | 4.650  |
| 5  | 1.469 | .6806 | .1705  | .2505  | 5.867  | 3.993 | 1.846 | 7.372  |
| 6  | 1.587 | .6302 | .1363  | .2163  | 7.336  | 4.623 | 2.276 | 10.523 |
| 7  | 1.714 | .5835 | .1121  | .1921  | 8.923  | 5.206 | 2.694 | 14.024 |
| 8  | 1.851 | .5403 | .0940  | .1740  | 10.637 | 5.747 | 3.099 | 17.806 |
| 9  | 1.999 | .5002 | .0801  | .1601  | 12.488 | 6.247 | 3.491 | 21.808 |
| **10** | **2.159** | **.4632** | .0690  | .1490  | 14.487 | 6.710 | 3.871 | 25.977 |
| 11 | 2.332 | .4289 | .0601  | .1401  | 16.645 | 7.139 | 4.240 | 30.266 |
| 12 | 2.518 | .3971 | .0527  | .1327  | 18.977 | 7.536 | 4.596 | 34.634 |
| 13 | 2.720 | .3677 | .0465  | .1265  | 21.495 | 7.904 | 4.940 | 39.046 |
| 14 | 2.937 | .3405 | .0413  | .1213  | 24.215 | 8.244 | 5.273 | 43.472 |
| 15 | 3.172 | .3152 | .0368  | .1168  | 27.152 | 8.559 | 5.594 | 47.886 |

---

## Slide 2-6 — F/P and P/F for Spreadsheets

Future value F is calculated using FV function:

```
= FV(i%,n,,P)
```

Present value P is calculated using PV function:

```
= PV(i%,n,,F)
```

Note the use of double commas in each function.

---

## Slide 2-7 — Introduction to Spreadsheet Functions

**Excel financial functions**

- Present Value, P: `= PV(i%,n,A,F)`
- Future Value, F: `= FV(i%,n,A,P)`
- Equal, periodic value, A: `= PMT(i%,n,P,F)`
- Number of periods, n: `= NPER((i%,A,P,F)`
- Compound interest rate, i: `= RATE(n,A,P,F)`
- Compound interest rate, i: `= IRR(first_cell:last_cell)`
- Present value, any series, P: `= NPV(i%,second_cell:last_cell) + first_cell`

Example: Estimates are P = $5000, n = 5 years, i = 5% per year. Find A in $ per year.

Function and display: `= PMT(5%, 5, 5000)` displays A = $1154.87

---

## Slide 2-8 — Example: Finding Future Value

A person deposits $5000 into an account which pays interest at a rate of 8% per year. The amount in
the account after 10 years is closest to:

(A) $2,792   (B) $9,000   (C) $10,795   (D) $12,165

*The slide's text layer labels a "cash flow diagram" box next to the solution, but — like the
solution text below — it does not render in the rasterized page (the source PDF appears to keep
these as a hidden/animation-reveal layer) and, unlike the diagrams on Slides 2-13/2-14/2-20/2-22,
no numeric position data leaked into the extracted text, so its exact layout could not be
reconstructed. It is presumably the standard single-payment "find F" diagram from Slide 2-4 with
P = $5000 given at t = 0 and F = ? sought at t = 10, i = 8%.*

**Solution:**

$$F = P(F/P,i,n) = 5000(F/P,8\%,10) = 5000(2.1589) = \$10{,}794.50$$

**Answer is (C)**

---

## Slide 2-9 — Example: Finding Present Value

A small company wants to make a single deposit now so it will have enough money to purchase a
backhoe costing $50,000 five years from now. If the account will earn interest of 10% per year, the
amount that must be deposited now is nearest to:

(A) $10,000   (B) $31,050   (C) $33,250   (D) $319,160

*As with Slide 2-8, the slide's text layer labels a "cash flow diagram" box next to the solution
that does not render visibly, with no recoverable numeric layout. Presumably the standard
single-payment "find P" diagram from Slide 2-4 with F = $50,000 given at t = 5 and P = ? sought at
t = 0, i = 10%.*

**Solution:**

$$P = F(P/F,i,n) = 50{,}000(P/F,10\%,5) = 50{,}000(0.6209) = \$31{,}045$$

**Answer is (B)**

---

## Slide 2-10 — Example: Finding Present Value

Show present worth at present time, t = 0. If Mr. Sompong deposit $5000 at 10 years ago, $10,000 at
5 years ago, and $20,000 a year ago, which bank pays interest at a rate of 8% per year.

*(Posed with no solution on the slide — in-class assessment problem. No answer choices given, no
diagram drawn — text-only problem statement.)*

---

## Slide 2-11 — Uniform Series Involving P/A and A/P

The uniform series factors that involve **P and A** are derived as follows:

1. Cash flow occurs in *consecutive* interest periods
2. Cash flow amount is *same* in each interest period

The cash flow diagrams are:

*(a) Find P given A — A is given as equal up-arrows at periods 1 through 5; P is the sought
down-arrow at period 0. Note that P lands one full period before the first A, i.e. one period
ahead of it.)*

```
        A = Given
        ^    ^    ^    ^    ^
        |    |    |    |    |
   0----1----2----3----4----5
   |
   v
 P = ?
```

*(b) Find A given P — mirror image: P is given at period 0, A is the sought (emphasized) up-arrows
at periods 1 through 5.)*

```
        A = ?
        ^    ^    ^    ^    ^
        |    |    |    |    |
   0----1----2----3----4----5
   |
   v
 P = Given
```

$$P = A(P/A,i,n) \quad \xleftarrow{\text{Standard Factor Notation}} \quad A = P(A/P,i,n)$$

**Note:** P is one period *Ahead* of first A value

---

## Slide 2-12 — Uniform Series Involving F/A and A/F

The uniform series factors that involve **F and A** are derived as follows:

1. Cash flow occurs in *consecutive* interest periods
2. Last cash flow occurs in *same* period as F

Cash flow diagrams are:

*(a) Find F given A — A is given as equal up-arrows at periods 1 through 5; F is the sought
quantity, drawn as an emphasized arrow coincident with period 5 — the same period as the last A,
not one period later.)*

```
   A = Given
   ^    ^    ^    ^    ^
   |    |    |    |    |
0--1----2----3----4----5
                        |
                        v
                      F = ?
```

*(b) Find A given F — mirror image: F is given at period 5 (same period as the last A), A is the
sought (emphasized) up-arrows at periods 1 through 5.)*

```
   A = ?
   ^    ^    ^    ^    ^
   |    |    |    |    |
0--1----2----3----4----5
                        |
                        v
                    F = Given
```

$$F = A(F/A,i,n) \quad \xleftarrow{\text{Standard Factor Notation}} \quad A = F(A/F,i,n)$$

**Note:** F takes place in the *same* period as last A

---

## Slide 2-13 — Example: Uniform Series Involving P/A

A chemical engineer believes that by modifying the structure of a certain water treatment polymer,
his company would earn an extra $5000 per year. At an interest rate of 10% per year, how much could
the company afford to spend now to just break even over a 5 year project period?

(A) $11,170   (B) 13,640   (C) $15,300   (D) $18,950

*Cash flow diagram (recovered from the PDF's text layer — the rasterized page renders this area
blank, but the diagram's number labels survive as text objects at their original coordinates, and
match the standard P/A pattern from Slide 2-11): A = $5000 given as equal end-of-period arrows at
periods 1–5, i = 10%, P = ? sought at period 0 — one period ahead of the first A.*

```
P = ?
  ^
  |
  0----1----2----3----4----5
       |    |    |    |    |
       v    v    v    v    v
      5000 5000 5000 5000 5000   (A = $5000 each, i = 10%)
```

**Solution:**

$$P = 5000(P/A,10\%,5) = 5000(3.7908) = \$18{,}954$$

**Answer is (D)**

---

## Slide 2-14 — Example: Uniform Series Involving F/A

An industrial engineer made a modification to a chip manufacturing process that will save her
company $10,000 per year. At an interest rate of 8% per year, how much will the savings amount to
in 7 years?

(A) $45,300   (B) $68,500   (C) $89,228   (D) $151,500

*Cash flow diagram (recovered from the PDF's text layer, same rendering caveat as Slide 2-13):
A = $10,000 given as equal end-of-period arrows at periods 1–7, i = 8%, F = ? sought — coincident
with period 7, the same period as the last A — matching the standard F/A pattern from Slide 2-12.*

```
   A = $10,000
   ^    ^    ^    ^    ^    ^    ^
   |    |    |    |    |    |    |
0--1----2----3----4----5----6----7
                                  |
                                  v
                                F = ?     (i = 8%)
```

**Solution:**

$$F = 10{,}000(F/A,8\%,7) = 10{,}000(8.9228) = \$89{,}228$$

**Answer is (C)**

---

## Slide 2-15 — Factor Values for Untabulated i or n

**3 ways to find factor values for untabulated i or n values**

- Use formula
- Use spreadsheet function with corresponding P, F, or A value set to 1
- Linearly interpolate in interest tables

Callout: Formula or spreadsheet function is fast and accurate. Interpolation is only approximate.

---

## Slide 2-16 — Example: Untabulated i

Determine the value for (F/P, 8.3%, 10)

**Formula:** $F = (1 + 0.083)^{10} = 2.2197$ — OK

**Spreadsheet:** `= FV(8.3%,10,,1) = 2.2197` — OK

**Interpolation:**

```
8%   ------  2.1589
8.3% ------     x
9%   ------  2.3674
```

$$x = 2.1589 + \left[\frac{8.3 - 8.0}{9.0 - 8.0}\right][2.3674 - 2.1589] = 2.2215 \quad \text{(Too high)}$$

**Absolute Error = 2.2215 − 2.2197 = 0.0018**

---

## Slide 2-17 — Arithmetic Gradients

Arithmetic gradients *change* by the *same amount* each period.

The cash flow diagram for the $P_G$ of an arithmetic gradient is:

*Pure-gradient diagram: no cash flow shown at period 1 at all — the gradient's first nonzero step
appears at period 2 (amount G), growing by G each period after that. $P_G$ is drawn as the sought
up-arrow sitting at period 0, i.e. two full periods ahead of the first change (which occurs at
period 2).*

```
P_G = ?
  ^
  |
  0----1----2----3----4----···----n
            |    |    |            |
            v    v    v            v
            G   2G   3G          (n-1)G
```

**G starts between periods 1 and 2** (not between 0 and 1)

This is because cash flow in year 1 is usually not equal to G and is handled separately as a *base
amount* (shown on next slide).

**Note that $P_G$ is located Two Periods Ahead of the first change that is equal to G**

Standard factor notation is:

$$P_G = G(P/G,i,n)$$

---

## Slide 2-18 — Typical Arithmetic Gradient Cash Flow

$i = 10\%$

*Top diagram — the "real" cash flow: a base amount of 400 in year 1, growing by 50 each year
through year 5. A dashed reference line runs across at the height of the year-1 (base) arrow.*

```
P_T = ?
  ^
  |
  0----1----2----3----4----5
       |    |    |    |    |
       v    v    v    v    v
      400  450  500  550  600
```

Label: "Amount in year 1 is base amount", pointing at the 400 arrow.

Callout: "This diagram = *this* (base amount) plus *this* (gradient)" — connects the top diagram to
the two diagrams below.

*Bottom-left diagram — the base-amount (uniform) series: 400 at every period 1 through 5.*

```
P_A = ?
  ^
  |
  0----1----2----3----4----5
       |    |    |    |    |
       v    v    v    v    v
      400  400  400  400  400
```

$$P_A = 400(P/A,10\%,5)$$

*Bottom-right diagram — the pure-gradient series: no cash flow at period 1, then G = 50, 2G = 100,
3G = 150, 4G = 200 at periods 2 through 5 — again $P_G$ sits two periods ahead of the first change.*

```
P_G = ?
  ^
  |
  0----1----2----3----4----5
            |    |    |    |
            v    v    v    v
            50  100  150  200
```

$$P_G = 50(P/G,10\%,5)$$

**Combined:**

$$P_T = P_A + P_G = 400(P/A,10\%,5) + 50(P/G,10\%,5)$$

---

## Slide 2-19 — Converting Arithmetic Gradient to A

Arithmetic gradient can be converted into equivalent A value using $G(A/G,i,n)$.

*Left diagram — pure increasing gradient, no flow at period 1, then G, 2G, 3G, 4G at periods
2–5.*

```
i = 10%
  0----1----2----3----4----5
            |    |    |    |
            v    v    v    v
            G   2G   3G   4G
```

converts to →

*Right diagram — equivalent uniform series A at every period 1–5 (dashed reference line at top).*

```
i = 10%
  0----1----2----3----4----5
       ^    ^    ^    ^    ^
       |    |    |    |    |
            A = ?
```

**General equation when base amount is involved is:**

$$A = \text{base amount} + G(A/G,i,n)$$

*Bottom diagram — the same pure-gradient shape repeated (G, 2G, 3G, 4G at periods 2–5), used to
illustrate the sign-flip rule for decreasing gradients:*

```
i = 10%
  0----1----2----3----4----5
            |    |    |    |
            v    v    v    v
            G   2G   3G   4G
```

"For decreasing gradients, change plus sign to minus":

$$A = \text{base amount} - G(A/G,i,n)$$

---

## Slide 2-20 — Example: Arithmetic Gradient

The present worth of $400 in year 1 and amounts increasing by $30 per year through year 5 at an
interest rate of 12% per year is closest to:

(A) $1532   (B) $1,634   (C) $1,744   (D) $1,829

*Cash flow diagram (recovered from the PDF's text layer, same rendering caveat as Slide 2-13) —
this is the combined (base + gradient) diagram in the style of Slide 2-18: the actual year-by-year
amounts are shown directly (400, then +30 each year), rather than split into separate base and
gradient diagrams.*

```
PT = ?
  ^
  |
  0----1----2----3----4----5      (i = 12%, 5-year)
       |    |    |    |    |
       v    v    v    v    v
      400  430  460  490  520     (G = $30 per year)
```

**Solution:**

$$P_T = 400(P/A,12\%,5) + 30(P/G,12\%,5) = 400(3.6048) + 30(6.3970) = \$1{,}633.83$$

**Answer is (B)**

The cash flow could also be converted into an A value as follows:

$$A = 400 + 30(A/G,12\%,5) = 400 + 30(1.7746) = \$453.24$$

---

## Slide 2-21 — Geometric Gradients

*Geometric gradients* change by the *same percentage* each period.

*Cash flow diagram for present worth of geometric gradient — unlike the arithmetic gradient, the
first cash flow $A_1$ DOES occur at period 1 (there is no separate "base amount" step); each
subsequent period multiplies by $(1+g)$ again, so the growth factor $(1+g)$ first appears going
from period 1 to period 2. $P_g$ is the sought up-arrow at period 0, one period ahead of $A_1$.*

```
P_g = ?
  ^
  |
  0----1----2----3----4----···----n
       |    |    |               |
       v    v    v               v
       A1  A1(1+g)^1  A1(1+g)^2 ... A1(1+g)^(n-1)
```

**Note:** g starts between periods 1 and 2

There are *no tables* for geometric factors. Use following equation for $g \neq i$:

$$P_g = A_1\left\{1 - \left[\frac{1+g}{1+i}\right]^n\right\}\Big/(i-g)$$

where: $A_1$ = cash flow in period 1, $g$ = rate of increase

If $g = i$: $P_g = A_1 n/(1+i)$

**Note:** If g is negative, change signs in front of both g values

---

## Slide 2-22 — Example: Geometric Gradient

Find the present worth of $1,000 in year 1 and amounts increasing by 7% per year through year 10.
Use an interest rate of 12% per year.

(a) $5,670   (b) $7,333   (c) $12,670   (d) $13,550

*Cash flow diagram (recovered from the PDF's text layer, same rendering caveat as Slide 2-13),
matching the standard geometric-gradient pattern from Slide 2-21: $A_1 = 1000$ at period 1, growing
7% per period, through period 10 (1000 → 1070 → 1145 → ... → 1838), i = 12%, $P_g$ = ? sought at
period 0.*

```
Pg = ?
  ^
  |
  0----1----2----3----···----10      (i = 12%)
       |    |    |            |
       v    v    v            v
      1000 1070 1145  ...    1838    (g = 7% growth per year)
```

**Solution:**

$$P_g = 1000\left[1 - \left(\frac{1+0.07}{1+0.12}\right)^{10}\right]\Big/(0.12-0.07) = \$7{,}333$$

**Answer is (b)**

To find A, multiply $P_g$ by (A/P,12%,10)

---

## Slide 2-23 — Example: Geometric Gradient

One measuring instrument costs $16,000 and there is expected to be used for 6 years and a scrap
value of $5,000. The first year maintenance costs are $1,700 and will increase by 11% per year.
Find the total present value if given the interest rate is 8% per annum.

*(Posed with no solution on the slide — in-class assessment problem. No answer choices given, no
diagram drawn — text-only problem statement.)*

---

## Slide 2-24 — Unknown Interest Rate i

Unknown interest rate problems involve solving for i, given n and 2 other values (P, F, or A).

*(Usually requires a trial and error solution or interpolation in interest tables)*

**Procedure:** Set up equation with all symbols involved and solve for i

A contractor purchased equipment for $60,000 which provided income of $16,000 per year for 10
years. The annual rate of return of the investment was closest to:

(a) 15%   (b) 18%   (c) 20%   (d) 23%

**Solution:** Can use either the P/A or A/P factor. Using A/P:

$$60{,}000(A/P,i\%,10) = 16{,}000 \implies (A/P,i\%,10) = 0.26667$$

From A/P column at n = 10 in the interest tables, i is between 22% and 24%.

**Answer is (d)**

---

## Slide 2-25 — Unknown Recovery Period n

Unknown recovery period problems involve solving for n, given i and 2 other values (P, F, or A).

*(Like interest rate problems, they usually require a trial & error solution or interpolation in
interest tables)*

**Procedure:** Set up equation with all symbols involved and solve for n

A contractor purchased equipment for $60,000 that provided income of $8,000 per year. At an
interest rate of 10% per year, the length of time required to recover the investment was closest
to:

(a) 10 years   (b) 12 years   (c) 15 years   (d) 18 years

**Solution:** Can use either the P/A or A/P factor. Using A/P:

$$60{,}000(A/P,10\%,n) = 8{,}000 \implies (A/P,10\%,n) = 0.13333$$

From A/P column in i = 10% interest tables, n is between 14 and 15 years.

**Answer is (c)**

---

## Slide 2-26 — Summary of Important Points

- In P/A and A/P factors, P is *one period ahead* of first A
- In F/A and A/F factors, F is in *same period* as last A
- To find untabulated factor values, best way is to use *formula or spreadsheet*
- For arithmetic gradients, gradient G starts between *periods 1 and 2*
- Arithmetic gradients have 2 parts, *base amount* (year 1) and *gradient amount*
- For geometric gradients, gradient g starts been *periods 1 and 2* [sic — slide reads "been"
  where "between" is meant]
- In geometric gradient formula, $A_1$ is amount in *period 1*
- To find unknown i or n, *set up equation involving all terms* and solve for i or n
