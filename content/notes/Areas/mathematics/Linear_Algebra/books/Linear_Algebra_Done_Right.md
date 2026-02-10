---
title: "Linear Algebra Done Right"
---

# Section 1.A Exercises

## Exercise 1.A.1

> Suppose that $a$ and $b$ are real numbers, not both 0. Find real numbers $c$ and $d$ such that
>
> 

$$
1/\left. (a + bi) \right. = c + di
$$



We need to use the complex conjugate of $\left. (a + bi) \right.$ by multiplying it by $\left. (a - bi) \right.$, which gives $a^{2} - abi + abi - b^{2}i^{2} = a^{2} + b^{2}$.



$$
\frac{1}{a + bi}\frac{a - bi}{a - bi} = \frac{a - bi}{a^{2} + b^{2}}
$$



Now we have



$$
\frac{a - bi}{a^{2} + b^{2}} = c + di = \frac{a}{a^{2} + b^{2}} - \frac{b}{a^{2} + b^{2}}i
$$



Now, equating coefficients gives $c = a/\left. \left( a^{2} + b^{2} \right) \right.$ and $d = - b/\left. \left( a^{2} + b^{2} \right) \right.$.

## Exercise 1.A.2

> Show that
>
> 

$$
\frac{- 1 + \sqrt{3}i}{2}
$$


>
> is a cube root of 1 (meaning that its cube equals 1)

Let's just brute force this. Multiply the following



$$
\left. \left( \frac{- 1 + \sqrt{3}i}{2} \right) \right.\left. \left( \frac{- 1 + \sqrt{3}i}{2} \right) \right. = \left. \left( - \frac{1}{2} - \frac{2\sqrt{3}}{4}i \right) \right.
$$



Now



$$
\left. \left( - \frac{1}{2} - \frac{2\sqrt{3}}{4}i \right) \right.\left. \left( \frac{- 1 + \sqrt{3}i}{2} \right) \right. = 1
$$



## Exercise 1.A.3

> Find two distinct square roots of $i$.

We have that



$$
\begin{aligned}
e^{i\pi/2} & = \cos\left. \left( \frac{- \pi}{2} \right) \right. + i\sin\left. \left( \frac{- \pi}{2} \right) \right.\quad\mathrm{\text{(Euler's formula)}} \\
 & = \cos\left. \left( \frac{3\pi}{2} \right) \right. + i\sin\left. \left( \frac{3\pi}{2} \right) \right. \\
 & = 0 + i\left. ( - 1) \right. \\
 & = - i
\end{aligned}
$$



Using the above, we have our two distinct square roots of $i$:



$$
\pm e^{i\pi/4} = \pm \left. \left( \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} \right) \right.
$$



## Exercise 1.A.4

> Show that $\alpha + \beta = \beta + \alpha$ for all $\alpha,\beta \in \mathbb{C}$.

Let $\alpha = a + bi$ and $\beta = c + di$. Then the left-hand side of the equation gives



$$
\begin{aligned}
\alpha + \beta & = \left. (a + bi) \right. + \left. (c + di) \right. \\
 & = a + bi + c + di \\
 & = \left. (a + c) \right. + \left. (b + d) \right.i
\end{aligned}
$$



And the RHS gives



$$
\begin{aligned}
\alpha + \beta & = \left. (c + di) \right. + \left. (a + bi) \right. \\
 & = c + di + a + bi \\
 & = \left. (c + a) \right. + \left. (d + b) \right.i
\end{aligned}
$$



Thus $\alpha + \beta = \beta + \alpha$ via the above and via commutativity of the real numbers.

## Exercise 1.A.5

> Show that $\left. (\alpha + \beta) \right. + \lambda = \alpha + \left. (\beta + \lambda) \right.$ for all $\alpha,\beta,\lambda \in \mathbb{C}$.

Let $\alpha = a + bi$ and $\beta = c + di$ and $\lambda = e + fi$.

Then the left-hand side of the equation gives



$$
\begin{aligned}
\left. (\alpha + \beta) \right. + \lambda & = \left. \left\lbrack \left. (a + bi) \right. + \left. (c + di) \right. \right\rbrack \right. + \left. (e + fi) \right. \\
 & = a + bi + c + di + e + fi \\
 & = \left. \left\lbrack \left. (a + c) \right. + e \right\rbrack \right. + \left. \left\lbrack \left. (b + d) \right.i + fi \right\rbrack \right.
\end{aligned}
$$



Similarly, the RHS gives



$$
\begin{aligned}
\alpha + \left. (\beta + \lambda) \right. & = \left. (a + bi) \right. + \left. \left\lbrack \left. (c + di) \right. + \left. (e + fi) \right. \right\rbrack \right. \\
 & = a + bi + c + di + e + fi \\
 & = \left. \left\lbrack a + \left. (c + e) \right. \right\rbrack \right. + \left. \left\lbrack bi + \left. (d + f) \right.i \right\rbrack \right.
\end{aligned}
$$



The above and the associativity of addition of real numbers show that $\left. (\alpha + \beta) \right. + \lambda = \alpha + \left. (\beta + \lambda) \right.$.

## Exercise 1.A.6

> Show that $\left. (\alpha\beta) \right.\lambda = \alpha\left. (\beta\lambda) \right.$ for all $\alpha,\beta,\lambda \in \mathbb{C}$.

Let $\alpha = a + bi$ and $\beta = c + di$ and $\lambda = e + fi$.

Then the LHS gives



$$
\begin{aligned}
\left. (e + fi) \right. & = \left. \left\lbrack \left. (ac - bd) \right. + \left. (ad + bc) \right.i \right\rbrack \right.\left. (e + fi) \right. \\
 & = \left. \left\lbrack \left. (ac - bd) \right.e - \left. (ad + bc) \right.f \right\rbrack \right. + \left. \left\lbrack \left. (ac - bd) \right.f + \left. (ad + bc) \right.e \right\rbrack \right.i \\
 & = \left. (ace - bde - adf - bcf) \right. + \left. (acf - bdf + ade + bce) \right.i
\end{aligned}
$$



And the RHS gives



$$
\begin{aligned}
\left. (a + bi) \right.\left. \left\lbrack \left. (c + di) \right.\left. (e + fi) \right. \right\rbrack \right. & = \left. (a + bi) \right.\left. \left\lbrack \left. (ce - df) \right. + \left. (cf + de) \right.i \right\rbrack \right. \\
 & = \left. \left\lbrack a\left. (ce - df) \right. - b\left. (cf + de) \right. \right\rbrack \right. + \left. \left\lbrack a\left. (cf + de) \right. + b\left. (ce - df) \right. \right\rbrack \right.i \\
 & = \left. (ace - adf - bcf - bde) \right. + \left. (acf + ade + bce - bdf) \right.i
\end{aligned}
$$



The results above and the commutativity of addition of real numbers show that $\left. (\alpha\beta) \right.\lambda = \alpha\left. (\beta\lambda) \right.$.

## Exercise 1.A.7

> Show that for every $\alpha \in \mathbb{C}$, there exists a unique $\beta in\mathbb{C}$ such that $\alpha + \beta = 0$.

Let $\alpha = a + bi$, where $a,b \in \mathbb{R}$. Then, $\beta = - a - bi$ satisfies $\alpha + \beta = 0$. Now suppose that there exists some $B' \in \mathbb{C}$ such that $\alpha + \beta' = 0$. Then



$$
\begin{aligned}
\beta & = \beta + \left. (\alpha + \beta') \right. \\
 & = \left. (\beta + \alpha) \right. + \beta' \\
 & = \beta'
\end{aligned}
$$



The above equations show that $\beta' = \beta$.

## Exercise 1.A.8

> Show that for every $\alpha \in \mathbb{C}$ with $\alpha \neq 0$ there exists a unique $\beta \in \mathbb{C}$ such that $\alpha\beta = 1$

We already know that $\beta$ exists given the results of Exercise 1.A.1. We just need to show uniqueness now.

Suppose that there exists another $\beta' \in \mathbb{C}$ such that $\alpha\beta = 1$. Then



$$
\begin{aligned}
\beta & = \beta\left. (\alpha\beta') \right. \\
 & = \left. (\beta\alpha) \right.\beta' \\
 & = \beta'
\end{aligned}
$$



The above equations show that $\beta' = \beta$.

## Exercise 1.A.9

> Show that $\lambda\left. (\alpha + \beta) \right. = \lambda\alpha + \lambda\beta$ for all $\lambda,\alpha,\beta \in \mathbb{C}$.

Let $\alpha = a + bi$ and $\beta = c + di$ and $\lambda = e + fi$, where $a,b,c,d,e,f \in \mathbb{R}$.

Computing the LHS gives



$$
\begin{aligned}
\lambda\left. (\alpha + \beta) \right. & = \left. (e + fi) \right.\left. \left\lbrack \left. (a + c) \right. + \left. (b + d) \right.i \right\rbrack \right. \\
 & = ae + bei + ce + dei + afi - bf + cfi - df
\end{aligned}
$$



Computing the RHS gives



$$
\begin{aligned}
\lambda\alpha + \lambda\beta & = \left. (e + fi) \right.\left. (a + c) \right. + \left. (e + fi) \right.\left. (b + d) \right. \\
 & = ae + bei + ce + dei + afi - bf + cfi - df
\end{aligned}
$$



So the LHS equals the RHS.

## Exercise 1.A.10

> Find $x \in \mathbb{R}^{4}$ such that
>
> 

$$
\left. (4, - 3,1,7) \right. + 2x = \left. (5,9, - 6,8) \right.
$$



$x = \left. \left( \frac{1}{2},6, - \frac{7}{2},\frac{1}{2} \right) \right.$

## Exercise 1.A.11

> Explain why there does not exist a $\lambda \in \mathbb{C}$ such that
>
> 

$$
\lambda\left. (2 - 3i,5 + 4i, - 6 + 7i) \right. = \left. (12 - 5i,7 + 22i, - 32 - 9i) \right.
$$



For the first term, we have $\lambda\left. (2 - 3i) \right. = 12 - 5i \Rightarrow \lambda = 3 + 2i$.

But



$$
\begin{aligned}
\lambda\left. (2 - 3i,5 + 4i, - 6 + 7i) \right. & = \left. (3 + 2i) \right.\left. (2 - 3i,5 + 4i, - 6 + 7i) \right. \\
 & = \left. (12 - 5i,7 + 22i, - 32 + 9i) \right. \\
 & \neq \left. (12 - 5i,7 + 22i, - 32 - 9i) \right.
\end{aligned}
$$



Thus $\lambda$ does not exist.

## Exercise 1.A.12

> Show that $\left. (x + y) \right. + z = x + \left. (y + z) \right.$ for all $x,y,z \in \mathbb{F}^{n}$.

Let $x = \left. \left( x_{1},x_{2},\ldots,x_{n} \right) \right.,y = \left. \left( y_{1},y_{2},\ldots,y_{n} \right) \right.,z = \left. \left( z_{1},z_{2},\ldots,z_{n} \right) \right.$. Using Definition 1.12 (addition in $\mathbb{F}^{n}$), we compute the LHS:



$$
\begin{aligned}
\left. (x + y) \right. + z & = \left. \left( x_{1} + y_{1},x_{2} + y_{2},\ldots,x_{n} + y_{n} \right) \right. + \left. \left( z_{1},z_{2},\ldots,z_{n} \right) \right. \\
 & = \lbrack\left. \left( x_{1} + y_{1} \right) \right. + z_{1},\ldots,\left. \left( x_{n} + y_{n} \right) \right. + z_{n})
\end{aligned}
$$



Computing the RHS gives



$$
\begin{array}{rlr}
x + \left. (y + z) \right. & = \left. \left( x_{1},x_{2},\ldots,x_{n} \right) \right. + \left. \left( y_{1} + z_{1},y_{2} + z_{2},\ldots,y_{n} + z_{n} \right) \right. & = \left. \left\lbrack x_{1} + \left. \left( y_{1} + z_{1} \right) \right.,\ldots,x_{n} + \left. \left( y_{n} + z_{n} \right) \right. \right\rbrack \right.
\end{array}
$$



The equations above and the associativity of addition in $\mathbb{F}$ show that $\left. (x + y) \right. + z = x + \left. (y + z) \right.$.

## Exercise 1.A.13

> Show that $\left. (ab) \right.x = a\left. (bx) \right.$ for all $x \in \mathbb{F}^{n}$ and all $a,b \in \mathbb{F}$.

Let $x = \left. \left( x_{1},x_{2},\ldots,x_{n} \right) \right.$, where $x_{1},x_{2},\ldots,x_{n} \in \mathbb{F}$. Definition 1.17 (scalar multiplication in $\mathbb{F}^{n}$) shows that



$$
\left. (ab) \right.x = \left. \left\lbrack \left. (ab) \right.x_{1},\left. (ab) \right.x_{2},\ldots,\left. (ab) \right.x_{n} \right\rbrack \right.
$$



and



$$
\begin{aligned}
a\left. (bx) \right. & = a\left. \left( bx_{1},bx_{2},\ldots,bx_{n} \right) \right. \\
 & = \left. \left\lbrack a\left. \left( bx_{1} \right) \right.,a(bx_{2},\ldots,a\left. \left( bx_{n} \right) \right. \right\rbrack \right.
\end{aligned}
$$



The equations above and the associativity of multiplication in $\mathbb{F}$ show that $\left. (ab) \right.x = a\left. (bx) \right.$.

## Exercise 1.A.14

> Show that $1x = x$ for all $x \in \mathbb{F}^{n}$

Let $x = \left. \left( x_{1},x_{2},\ldots,x_{n} \right) \right.$, where $x_{1},x_{2},\ldots,x_{n} \in \mathbb{F}$. Definition 1.17 (scalar multiplication in $\mathbb{F}^{n}$), and the fact that 1 is the multiplicative identify of $\mathbb{F}$ shows that



$$
\begin{aligned}
1x & = \left. \left( 1x_{1},1x_{2},\ldots,1x_{n} \right) \right. \\
 & = \left. \left( x_{1},x_{2},\ldots,x_{n} \right) \right. \\
 & = x
\end{aligned}
$$



## Exercise 1.A.15

> Show that $\lambda\left. (x + y) \right. = \lambda x + \lambda y$ for all $\lambda \in \mathbb{F}$ and all $x,y \in \mathbb{F}^{n}$.

Let $x = \left. \left( x_{1},x_{2},\ldots,x_{n} \right) \right.$, where $x_{1},x_{2},\ldots,x_{n} \in \mathbb{F}$. Definition 1.12 (addition in $\mathbb{F}^{n}$) and Definition 1.17 (scalar multiplication in $\mathbb{F}^{n}$) shows that



$$
\begin{aligned}
\lambda\left. (x + y) \right. & = \lambda\left. \left( x_{1} + y_{1},x_{2} + y_{2},\ldots,x_{n} + y_{n} \right) \right. \\
 & = \left. \left\lbrack \lambda\left. \left( x_{1} + y_{1} \right) \right.,\lambda\left. \left( x_{2} + y_{2} \right) \right.,\ldots,\lambda\left. \left( x_{n} + y_{n} \right) \right. \right\rbrack \right.
\end{aligned}
$$



and



$$
\begin{aligned}
\lambda x + \lambda y & = \left. \left( \lambda x_{1},\lambda x_{2},\ldots,\lambda x_{n} \right) \right. + \left. \left( \lambda y_{1},\lambda y_{2},\ldots,\lambda y_{n} \right) \right. \\
 & = \left. \left( \lambda x_{1} + \lambda y_{1},\lambda x_{2} + \lambda y_{2},\ldots,\lambda x_{n} + \lambda y_{n} \right) \right.
\end{aligned}
$$



The equations above and the distributive property of $\mathbb{F}$ show that $\lambda\left. (x + y) \right. = \lambda x + \lambda y$.

## Exercise 1.A.16

> Show that $\left. (a + b) \right.x = ax + bx$ for all $a,b \in \mathbb{F}$ and all $x \in \mathbb{F}^{n}$

Let $x = \left. \left( x_{1},x_{2},\ldots,x_{n} \right) \right.$, where $x_{1},x_{2},\ldots,x_{n} \in \mathbb{F}$. Definition 1.12 (addition in $\mathbb{F}^{n}$) and Definition 1.17 (scalar multiplication in $\mathbb{F}^{n}$) shows that



$$
\left. (a + b) \right.x = \left. \left\lbrack \left. (a + b) \right.x_{1},\left. (a + b) \right.x_{2},\ldots,\left. (a + b) \right.x_{n} \right\rbrack \right.
$$



and



$$
\begin{aligned}
ax + bx & = \left. \left( ax_{1},ax_{2},\ldots,ax_{n} \right) \right. + \left. \left( bx_{1},bx_{2},\ldots,bx_{n} \right) \right. \\
 & = \left. \left( ax_{1} + bx_{1},ax_{2} + bx_{2},\ldots,ax_{n} + bx_{n} \right) \right.
\end{aligned}
$$



The equations above and the distributive property of $\mathbb{F}$ show that $\left. (a + b) \right.x = ax + bx$.

# Section 1.B Examples

## Example 1.22

> $\mathbb{F}^{\infty}$ is defined to be the set of all sequences of elements of $\mathbb{F}$:
>
> 

$$
\mathbb{F}^{\infty} = \{\left. \left( x_{1},x_{2},\ldots \right) \right.:x_{j} \in \mathbb{F}\mathrm{\text{ for }}j = 1,2,\ldots\}
$$


>
> Addition and scalar multiplication of $\mathbb{F}^{\infty}$ are defined as expected:
>
> 

$$
\left. \left( x_{1},x_{2},\ldots \right) \right. + \left. \left( y_{1},y_{2},\ldots \right) \right. = \left. \left( x_{1} + y_{1},x_{2} + y_{2},\ldots \right) \right.
$$


>
> and
>
> 

$$
\lambda\left. \left( x_{1},x_{2},\ldots \right) \right. = \left. \left( \lambda x_{1},\lambda x_{2},\ldots \right) \right.
$$


>
> With these definitions $F^{\infty}$ becomes a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{F}$, *as you should verify*. The additive identity in this [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) is the sequence of all 0's.

## Example 1.24: $\mathbb{F}^{S}$ is a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/)

See this [example](https://math.stackexchange.com/questions/3599186/example-1-24-in-axlers-linear-algebra).

Verify the following

1.  If $S$ is a non-empty set, then $\mathbb{F}^{S}$ (with the operations of addition and scalar multiplication as defined above) is a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{F}$.

2.  The additive identity of $\mathbb{F}^{S}$ is the function $0:S \rightarrow \mathbb{F}$ defined by

    

$$
0\left. (x) \right. = 0
$$

 for all $x \in S$

3.  For $f \in \mathbb{F}^{S}$, the additive inverse of $f$ is the function $- f:S \rightarrow \mathbb{F}$ defined by

    

$$
\left. ( - f) \right.\left. (x) \right. = - f\left. (x) \right.
$$

 for all $x \in S$.

By definition,



$$
\mathbb{F}^{S} = \{ f:f \rightarrow \mathbb{R}:S \neq \varnothing\}
$$



With addition being defined on $\mathbb{F}^{S}$ as



$$
\left. (f + g) \right.\left. (x) \right. = f\left. (x) \right. + g\left. (x) \right.
$$



for all $x \in S$. By definition, this takes inputs in $S$ and produces two outputs, $f\left. (x) \right.$ and $g\left. (x) \right.$, in $F$, and since $F$ is closed under addition, $f\left. (x) \right. + g\left. (x) \right. \in \mathbb{F}$. Hence $f + g \in \mathbb{F}^{S}$.

Similarly, by definition, scalar multiplication is defined as



$$
\left. (\lambda f) \right.\left. (x) \right. = \lambda f\left. (x) \right.
$$



for $\lambda \in \mathbb{F}$ and $f \in \mathbb{F}^{S}$. By definition, $\lambda f$ takes inputs in $S$. Since $f$ maps $S$ to $\mathbb{F}$, $f\left. (x) \right. \in \mathbb{F}$. By [closure](/notes/areas/mathematics/topology/definitions/closure/) of $\mathbb{F}$ under scalar multiplication, $\lambda f\left. (x) \right. \in \mathbb{F}$, so scalar multiplication likewise holds.

*Commutativity*: Let $f,g \in \mathbb{F}^{S}$. For any $x \in S$



$$
\left. (f + g) \right.\left. (x) \right. = f\left. (x) \right. + g\left. (x) \right. = g\left. (x) \right. + f\left. (x) \right. = \left. (g + f) \right.\left. (x) \right.
$$



so addition on $\mathbb{F}^{S}$ is commutative, which follows from commutativity under addition on $\mathbb{F}$.

*Associativity of addition*: This follows from associativity on $\mathbb{F}$. Let $f,g,h \in \mathbb{F}^{S}$. Then, for any $x \in S$,



$$
\begin{aligned}
\left. \left( \left. (f + g) \right. + h \right) \right.\left. (x) \right. & = \left. (f + g) \right.\left. (x) \right. + h\left. (x) \right. \\
 & = \left. \left( f\left. (x) \right. + g\left. (x) \right. \right) \right. + h\left. (x) \right. \\
 & = f\left. (x) \right. + \left. \left( g\left. (x) \right. + h\left. (x) \right. \right) \right. \\
 & = \left. \left( f + \left. (g + h) \right. \right) \right.\left. (x) \right.
\end{aligned}
$$



so addition in $\mathbb{F}^{S}$ is associative.

*Associativity of scalar multiplication*: Let $\alpha,\beta \in \mathbb{F}$. For any $f \in \mathbb{F}^{S}$ and $x \in S$, we have



$$
\begin{aligned}
\left. \left( \left. (\alpha\beta) \right.\left. (f) \right. \right) \right.\left. (x) \right. & = \left. (\alpha\beta) \right.f\left. (x) \right. \\
 & = \alpha\left. \left( \beta f\left. (x) \right. \right) \right. \\
 & = \alpha\left. \left( \left. (\beta f) \right.\left. (x) \right. \right) \right. \\
 & = \left. \left( \alpha\left. (\beta f) \right. \right) \right.\left. (x) \right.
\end{aligned}
$$



by associativity in $F$.

*Additive identity*: We consider the defined function $0\left. (x) \right. = 0$. For any $f \in \mathbb{F}^{S}$ and $x \in S$, we have



$$
\left. (f + 0) \right.\left. (x) \right. = f\left. (x) \right. + 0 = f\left. (x) \right.
$$



by the additive identity in $\mathbb{F}$. So $0\left. (x) \right.$ is the identity in $\mathbb{F}^{S}$.

*Additive inverse*: Given $f \in \mathbb{F}^{S}$, take $- f:S \rightarrow \mathbb{F}$ given by $\left. ( - f) \right.\left. (x) \right. = - f\left. (x) \right.$. By [closure](/notes/areas/mathematics/topology/definitions/closure/) under scalar multiplication, $- f \in \mathbb{F}^{S}$. By the definition of addition, for any $x \in S$, we have



$$
\begin{aligned}
\left. \left( f + \left. ( - f) \right. \right) \right.\left. (x) \right. & = f\left. (x) \right. + \left. ( - f) \right.\left. (x) \right. \\
 & = f\left. (x) \right. + \left. \left( - f\left. (x) \right. \right) \right. \\
 & = 0
\end{aligned}
$$



by the additive inverse axiom in $\mathbb{F}$.

*Multiplicative identity*: For any $f \in \mathbb{F}^{S}$ and $x \in S$, the definition of scalar multiplication gives



$$
\left. (1f) \right.\left. (x) \right. = 1f\left. (x) \right. = f\left. (x) \right.
$$



by the multiplicative identity axiom of $\mathbb{F}$.

*Distributivity*: Let $\lambda \in \mathbb{F}$ and $f,g \in \mathbb{F}^{S}$. For any $x \in S$, we have



$$
\begin{aligned}
\left. \left( \lambda\left. (f + g) \right. \right) \right.\left. (x) \right. & = \lambda\left. \left( \left. (f + g) \right.\left. (x) \right. \right) \right. \\
 & = \lambda\left. \left( f\left. (x) \right. + g\left. (x) \right. \right) \right. \\
 & = \lambda f\left. (x) \right.
\end{aligned}
$$



by distributivity in $\mathbb{F}$. So distributivity over addition of functions holds.

*Distributivity over field addition*: Taking $\alpha,\beta \in \mathbb{F}$ and $f \in \mathbb{F}^{S}$, for any $x \in S$, we have



$$
\left. \left( \left. (\alpha + \beta) \right.f \right) \right.\left. (x) \right. = \left. (\alpha + \beta) \right.f\left. (x) \right. = \alpha f\left. (x) \right. = \beta f\left. (x) \right.
$$



by distributivity in $\mathbb{F}$.

Thus, $\mathbb{F}^{S}$ is a [vector space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/).

# Section 1.B Exercises

## Exercise 1.B.1

> Prove that $- \left. ( - v) \right. = v$ for every $v \in V$.

Proof:



$$
\begin{aligned}
 \text{-} v\left. ( - v) \right. & = - \left. ( - v) \right. + 0 \\
 & = - \left. ( - v) \right. + \left. \left\lbrack \left. ( - v) \right. + v \right\rbrack \right. \\
 & = \left. \left\lbrack - \left. ( - v) \right. + \left. ( - v) \right. \right\rbrack \right. + v \\
 & = 0 + v \\
 & = v
\end{aligned}
$$



## Exercise 1.B.2

> Suppose that $a \in \mathbb{F},v \in V$, and $av = 0$. Prove that $a = 0$ or $v = 0$.

Proof: proceed via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/), and assume that $a \neq 0$ and $v \neq 0$. Then,



$$
\begin{aligned}
v & = 1v \\
 & = \left. \left( \frac{1}{a}a \right) \right.v \\
 & = \frac{1}{a}\left. (av) \right. \\
 & = 0
\end{aligned}
$$



But here $v = 0$, which contradicts our assumption that $v \neq 0$. Thus, $a = 0$ or $v = 0$.

## Exercise 1.B.3

> Suppose $v,w \in V$. Explain why there exists a unique $x \in V$ such that $v + 3x = w$.

We claim that $x = \left. (1/3) \right.\left. (w - v) \right.$ satisfies $v + 3x = w$.

Proof:



$$
\begin{aligned}
v + 3x & = v + 3\frac{1}{3}\left. (w - v) \right. \\
 & = v + \left. (w - v) \right. \\
 & = w
\end{aligned}
$$



This implies existence. Now we need to show uniqueness.

Suppose that there exists another $x' \in V$ such that $v + 3x' = w$. Then,



$$
\begin{aligned}
0 & = w - w \\
 & = \left. (v + 3x) \right. - \left. (v + 3x') \right. \\
 & = v + 3x - v - 3x' \\
 & = 3x - 3x'
\end{aligned}
$$



Thus



$$
\begin{aligned}
x' & = x' + \frac{1}{3} \times 0 \\
 & = x' + \frac{1}{3}\left. (3x - 3x') \right. \\
 & = x' + x - x' \\
 & = x
\end{aligned}
$$



which shows uniqueness.

## Exercise 1.B.4

> The empty set is not a vector space. The empty set fails to satisfy only one of the requirements listed in 1.19. Which one?

The empty set fails to satisfy the additive identity requirement. This is because there does not exist an element $0 \in \varnothing$.

## Exercise 1.B.5

> Show that in the definition of a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) (1.19), the additive inverse condition can be replaced with the condition that
>
> 

$$
0v = 0\mathrm{\text{ for all }}v \in V
$$

 Here the 0 on the left side is the number 0, and the 0 on the right side is the additive identity of $V$. (The phrase "a condition can be replaced" in a definition means that the collection of objects satisfying the definition is unchanged if the original condition is replaced with the new condition.)

The original definition of the additive inverse from 1.19 states that there exists an element $0 \in V$ such that $v + 0 = v$ for all $v \in V$.

We already showed that $0v = 0$ for all $v \in V$ in Theorem 1.29. Now we assume that $0v = 0$ for all $v \in V$ and then show the additive inverse condition.



$$
\begin{aligned}
v + \left. ( - 1) \right.v & = 1v + \left. ( - 1) \right.v \\
 & = \left. \left\lbrack 1 + \left. ( - 1) \right. \right\rbrack \right.v \\
 & = 0v \\
 & = 0
\end{aligned}
$$



So the new definition implies the original definition.

## Exercise 1.B.6

> Let $\infty$ and $- \infty$ denote two distinct objects, neither of which is in $\mathbb{R}$. Define an addition and scalar multiplication on $\mathbb{R} \cup \{\infty\} \cup \{ - \infty\}$ as you could guess from the notation. Specifically, the sum and product of two real numbers is as usual, and for $t \in \mathbb{R}$ define
>
> 

$$
\begin{array}{r}
t\infty = \{ - \infty,\mathrm{\text{ if }}t < 0, \\
0,\mathrm{\text{ if }}t = 0, \\
\infty,\mathrm{\text{ if }}t > 0,\quad t\left. ( - \infty) \right.\{\infty,\mathrm{\text{ if }}t < 0, \\
0,\mathrm{\text{ if }}t = 0, \\
\text{-} \infty,\mathrm{\text{ if }}t > 0,
\end{array}
$$


>
> where
>
> $t + \infty = \infty + t = \infty$,
>
> $t + \left. ( - \infty) \right. = \left. ( - \infty) \right. + t = - \infty$,
>
> $\infty + \infty = \infty$,
>
> $\left. ( - \infty) \right. + \left. ( - \infty) \right. = - \infty$,
>
> $\infty + \left. ( - \infty) \right. = 0$.
>
> Now, is $R \cup \{\infty\} \cup \{ - \infty\}$ a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{R}$? Explain.

This is not a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{R}$. Consider the distributive properties in 1.19. If this is a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{R}$, we will have



$$
\begin{aligned}
\infty & = \left. \left\lbrack 2 + \left. ( - 1) \right. \right\rbrack \right.\infty \\
 & = 2\infty + \left. ( - 1) \right.\infty \\
 & = \infty + \left. ( - \infty) \right. \\
 & = 0
\end{aligned}
$$



Hence for any $t \in \mathbb{R}$, one has



$$
\begin{aligned}
t & = 0 + t \\
 & = \infty + t \\
 & = \infty \\
 & = 0
\end{aligned}
$$



Which is a contradiction since the zero vector is unique. See [here](http://pages.cs.wisc.edu/~matthewb/pages/notes/pdf/linearalgebra/VectorSpaces.pdf).

# Section 1.C Examples

## Example 1.C.35: [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)

### (a)

> If $b \in \mathbb{F}$, then
>
> 

$$
\{\left. \left( x_{1},x_{2},x_{3},x_{4} \right) \right. \in \mathbb{F}^{4}:x_{3} = 5x_{4} + b\}
$$


>
> is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{F}^{4}$ if and only if $b = 0$.

Since $\left. (0,0,0,0) \right. \in U$, then for $\left. (0,0,b,0) \right.$ to be an element of $U$, $b$ must be zero.

### (b)

> The set of continuous real-valued functions on the interval $\left. \lbrack 0,1\rbrack \right.$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{\left. \lbrack 0,1\rbrack \right.}$.

Claim: The sum of two continuous functions $f$ and $g$ is continuous.

Proof: Let $\epsilon > 0$ be arbitrary. There exists a $\delta > 0$ such that whenever $|x - c| < \delta$, it follows that $\left| \left. (f + g) \right.\left. (x) \right. - \left. (f + g) \right.\left. (c) \right. \right| < \epsilon$.

For $\epsilon/2$, we can find a $\delta_{1}$ such that $\left| f\left. (x) \right. - f\left. (c) \right. \right| < \epsilon/2$ whenever $|x - c| < \delta_{1}$.

Similarly, for $\epsilon/2$, we can find a $\delta_{2}$ such that $\left| g\left. (x) \right. - g\left. (c) \right. \right| < \epsilon/2$ whenever $|x - c| < \delta_{2}$.

Now, using the [triangle inequality](/notes/areas/mathematics/real_analysis/definitions/triangle_inequality/), we have



$$
\begin{aligned}
\left| \left. (f + g) \right.\left. (x) \right. - \left. (f + g) \right.\left. (c) \right. \right| & = \left| f\left. (x) \right. + g\left. (x) \right. - f\left. (c) \right. - g\left. (c) \right. \right| \\
 & = |\left. \left\lbrack f\left. (x) \right. - f\left. (c) \right. \right\rbrack \right. + \left. \left\lbrack g\left. (x) \right. - g\left. (c) \right. \right\rbrack \right. \\
 & \leq \left| f\left. (x) \right. - f\left. (c) \right. \right| + \left| g\left. (x) \right. - g\left. (c) \right. \right| \\
 & < \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
 & = \epsilon
\end{aligned}
$$



Now, take $\delta = \min\{ d_{1},d_{2}\}$, so that whenever $|x - c| < \delta$, it follows that $\left| \left. (f + g) \right.\left. (x) \right. - \left. (f + g) \right.\left. (c) \right. \right| < \epsilon$, as desired.

Thus we have shown that the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) is closed under addition. A similar argument can be used to show it is closed under scalar multiplication. Also, the zero function is a continuous function. Thus, this is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).

### (c)

> The set of differentiable real-valued functions on $\mathbb{R}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) $\mathbb{R}^{\mathbb{R}}$.

Proof: Let $\mathbb{D}$ denote the set of all [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) functions on $\mathbb{R}$. It is clear that $\mathbb{D}$ inherits most of the required properties from the [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) of all functions on $\mathbb{R}$, so we only need to verify that $\mathbb{D}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/). Let $f\left. (x) \right.$ and $g\left. (x) \right.$ be in $\mathbb{D}$, and let $c$ be an arbitrary real number. By the [Algebraic_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_differentiability_theorem/) (Abbott --- Theorem 5.2.4 part (i)), we know that



$$
\left. (f + g) \right.' = f' + g'
$$



To show this formally, we write



$$
\begin{aligned}
\left. (f + g) \right.' & = \lim\limits_{x \rightarrow c}\frac{\left. (f + g) \right.\left. (x) \right. - \left. (f + g) \right.\left. (c) \right.}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{f\left. (x) \right. + g\left. (x) \right. - f\left. (c) \right. + g\left. (c) \right.}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{\left. \left\lbrack f\left. (x) \right. - f\left. (c) \right. \right\rbrack \right. + \left. \left\lbrack g\left. (x) \right. - g\left. (c) \right. \right\rbrack \right.}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{f\left. (x) \right. - f\left. (c) \right.}{x - c} + \lim\limits_{x \rightarrow c}\frac{g\left. (x) \right. - g\left. (c) \right.}{x - c} \\
 & = f' + g'
\end{aligned}
$$



Again by the [Algebraic_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_differentiability_theorem/) (Abbott --- Theorem 5.2.4 part (ii)), we know that



$$
\left. (cf) \right.' = c \cdot f'
$$



Which means that $\mathbb{D}$ is closed under vector addition and scalar multiplication and is thus a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).

### (d)

> The set of differentiable real-valued functions $f$ on the interval $\left. (0,3) \right.$ such that $f'\left. (2) \right. = b$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{\left. (0,3) \right.}$ if and only if $b = 0$.

### (e)

> The set of all sequences of complex numbers with limit 0 is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{C}^{\infty}$.

See: <https://math.stackexchange.com/a/3777128>

Let $U$ be the set of all complex sequences $\left. \left( z_{n} \right) \right._{n = 0}^{\infty}$ such that



$$
\lim\limits_{n \rightarrow \infty}z_{n} = 0
$$



Let us now show that $U$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).

\(1\) Remember that the additive identity of our [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) $\mathbb{C}^{\infty}$ is the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) whose terms are all zero: $\left. (0,0,0,\ldots) \right.$. It is indeed the case that the limit of this [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is zero, so it is an element of $U$.

\(2\) Now take two sequences $\left. \left( z_{n} \right) \right._{n = 0}^{\infty}$ and $\left. \left( w_{n} \right) \right._{n = 0}^{\infty}$, both in $U$. Then



$$
\begin{aligned}
\lim\limits_{n \rightarrow \infty}\left. \left( z_{n} + w_{n} \right) \right. & = \lim\limits_{n \rightarrow \infty}z_{n} + \lim\limits_{n \rightarrow \infty}w_{n} \\
 & = 0 + 0 \\
 & = 0
\end{aligned}
$$



So the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( z_{n} + w_{n} \right) \right._{n = 0}^{\infty}$ is in $U$. This shows that $U$ is closed under vector addition.

\(3\) Now let $\lambda$ be an arbitrary complex number. We see that



$$
\begin{aligned}
\lim\limits_{n \rightarrow \infty}\lambda z_{n} & = \lambda\lim\limits_{n \rightarrow \infty}z_{n} \\
 & = \lambda \cdot 0 \\
 & = 0
\end{aligned}
$$



So the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( \lambda z_{n} \right) \right._{n = 0}^{\infty}$ is in $U$. This shows that $U$ is closed under scalar multiplication.

So we can therefore conclude that $U$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{C}^{\infty}$

## Example 1.C.37

> Suppose $U$ is the set of all elements of $\mathbb{F}^{3}$ whose second and third coordinates equal 0, and $W$ is the set of all elements of $\mathbb{F}^{3}$ whose first and third coordinates equal 0:
>
> 

$$
U = \{\left. (a,0,0) \right. \in \mathbb{F}^{3}:a \in \mathbb{F}\}\quad\mathrm{\text{and}}\quad W = \{\left. (0,b,0) \right. \in \mathbb{F}^{3}:b \in \mathbb{F}\}
$$


>
> Then
>
> 

$$
U + W = \{\left. (x,y,0) \right.:x,y \in \mathbb{F}\}
$$



We must show that $U + W = S$, where $S = \{\left. (x,y,0) \right.:x,y \in \mathbb{F}\}$.

Showing $\subseteq$: Let $u = \left. (x,0,0) \right. \in U$ and $w = \left. (0,y,0) \right. \in W$. Then



$$
u + w = \left. (x + 0,0 + y,0 + 0) \right.
$$



is in $S$ because $x + 0,0 + y,0 + 0$ are all elements of $\mathbb{F}$.

Now, showing $\supseteq$: Let $s = \left. (x,y,0) \right.$. We need to find $u \in W$ and $w \in W$ such that $s = u + w$. Consider $u = \left. (x,0,0) \right.$ and $w = \left. (0,y,0) \right.$. Then $u \in W$ and $w \in W$ and



$$
\begin{aligned}
s & = \left. (x,y,0) \right. \\
 & = \left. (x,0,0) \right. + \left. (0,y,0) \right. \\
 & = u + w \in U + W
\end{aligned}
$$



## Example 1.C.38

> Suppose that $U = \{\left. (x,x,y,y) \right. \in \mathbb{F}^{4}:x,y \in \mathbb{F}\}$ and $W = \{\left. (x,x,x,y) \right. \in \mathbb{F}^{4}:x,y \in \mathbb{F}\}$. Then
>
> 

$$
U + W = \{\left. (x,x,y,z) \right. \in \mathbb{F}^{4}:x,y,z \in \mathbb{F}\}
$$


>
> *as you should verify*.

See <https://math.stackexchange.com/questions/2397605/sum-of-vector-subspaces>

Recall that if we want to show that two sets $A$ and $B$ are equal, then we need to show $A \subseteq B$ and $B \subseteq A$.

We must show that $U + W = S$, where $S = \{\left. (x,x,y,z) \right. \in \mathbb{F}^{4}:x,y,z \in \mathbb{F}\}$.

Showing $\subseteq$: Let $u = \left. (x,x,y,y) \right. \in U$ and $w = \left. (a,a,a,b) \right. \in W$. Then



$$
u + w = \left. (x + a,x + a,y + a,y + b) \right.
$$



is in $S$ because $x + a,x + a,y + a,y + b$ are all elements of $\mathbb{F}$.

Showing $\supseteq$: Let $s = \left. (x,x,y,z) \right. \in S$. We need to find $u \in U$ and $w \in W$ such that $s = u + w$. Consider $u = \left. (x - y,x - y,0,0) \right. \in U$ and $w = \left. (y,y,y,z) \right. \in W$. Then,



$$
\begin{aligned}
s & = \left. (x,x,y,z) \right. \\
 & = \left. (x - y,x - y,0,0) \right. + \left. (y,y,y,z) \right. \\
 & = u + w \in U + W
\end{aligned}
$$



Therefore $U + W = \{\left. (x,x,y,z) \right. \in \mathbb{F}^{4}:x,y,z \in \mathbb{F}\}$.

## Theorem 1.39

> Suppose $U_{1},\ldots,U_{m}$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$. Then $U_{1} + \cdots + U_{m}$ is the smallest [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$ containing $U_{1},\ldots,U_{m}$.

See [here](https://math.stackexchange.com/questions/1601065/the-sum-of-subspaces-is-the-smallest-subspace-containing-all-the-summands).

Claim: $U_{1} + \cdots + U_{m}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) containing $U_{1},\ldots,U_{m}$, and if $W \subseteq V$ is any [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) with $U_{1},\ldots,U_{m} \subseteq W$, then we already have $U_{1} + \cdots + U_{m} \subseteq W$.

Proof: It is easy to see that $0 \in U_{1} + \cdots + U_{m}$ and that $U_{1} + \cdots + U_{m}$ is closed under addition and scalar multiplication. Thus Theorem 1.34 implies that $U_{1} + \cdots + U_{m}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$.

Now, suppose that $W \subseteq V$ is some [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) containing $U_{1},\ldots,U_{m}$. For all $u_{1} \in U_{1},\ldots,u_{m} \in U_{m}$, we then have $u_{1},\ldots,u_{m} \in W$. Because $W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) it follows that $u_{1} + \cdots + u_{m} \in W$ (because $W$ is closed under finite sums). Therefore



$$
U_{1} + \cdots U_{n} = \{ u_{1} + \cdots + u_{n}|u_{1} \in U_{1},\ldots,u_{n} \in U_{n}\} \subseteq W
$$



## Example 1.C.41

> Suppose $U$ is the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{F}^{3}$ of those vectors whose last coordinate equals 0, and $W$ is the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{F}^{3}$ of those vectors whose first two coordinates equal 0:
>
> 

$$
U = \{\left. (x,y,0) \right. \in \mathbb{F}^{3}:x,y \in \mathbb{F}\}\quad\mathrm{\text{and}}\quad W = \{\left. (0,0,z) \right. \in \mathbb{F}^{3}:z \in \mathbb{F}\}.
$$


>
> Then $\mathbb{F}^{3} = U \oplus W$.

See [here](https://math.stackexchange.com/questions/3818834/prove-that-mathbff3-u-oplus-w).

Let $v \in \mathbb{F}^{3}$. Then we can write $v = \left. (x,y,z) \right.$ for $x,y,z, \in \mathbb{F}$. Let $u = \left. (x,y,0) \right. \in U$ and $w = \left. (0,0,z) \right. \in W$. Then $v = u + w$, so $v \in U + W$. Now let $u' \in U$ and $w' \in W$ be arbitrary such that $u' + w' = v$. So, $u' = \left. (a,b,0) \right.$ and $w' = \left. (0,0,c) \right.$ for $a,b,c \in \mathbb{F}$. It follows that



$$
\begin{aligned}
u' + w' & = \left. (a,b,0) \right. + \left. (0,0,c) \right. \\
 & = \left. (a,b,c) \right. \\
 & = v \\
 & = \left. (x,y,0) \right. + \left. (0,0,z) \right. \\
 & = \left. (x,y,z) \right.
\end{aligned}
$$



See also [here](https://math.stackexchange.com/questions/3276496/single-elements-of-subspaces).

## Example 1.C.42

> Suppose $U_{j}$ is the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{F}^{n}$ of those vectors whose coordinates are all 0, except possible in the $j^{\mathrm{\text{th}}}$ (thus, for example, $U_{2} = \{\left. (0,x,0,\ldots,0) \right. \in \mathbb{F}^{n}:x \in \mathbb{F}\}$). Then
>
> 

$$
\mathbb{F}^{n} = U_{1} \oplus \cdots \oplus U_{n}
$$



# Section 1.C Exercises

## Exercise 1.C.1

> For each of the following subsets of $\mathbb{F}^{3}$, determine whether it is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{F}^{3}$:

### (a)

> $\{\left. \left( x_{1},x_{2},x_{3} \right) \right. \in \mathbb{F}^{3}:x_{1} + 2x_{2} + 3x_{3} = 0\}$

Let $U = \{\left. \left( x_{1},x_{2},x_{3} \right) \right. \in \mathbb{F}^{3}:x_{1} + 2x_{2} + 3x_{3} = 0\}$.

See <https://www.youtube.com/watch?v=pUkYjBw6qJw>

Proving the three properties of [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s:

\(1\) Notice that $0 + 2\left. (0) \right. + 3\left. (0) \right. = 0$. So, $\left. (0,0,0) \right. \in U$.

\(2\) Take any $\left. \left( x_{1},x_{2},x_{3} \right) \right. \in U$ and $\left. \left( y_{1},y_{2},y_{3} \right) \right. \in U$. Then



$$
x_{1} + 2x_{2} + 3x_{3} = 0\quad\mathrm{\text{ and }}y_{1} = 2y_{2} + 3y_{3} = 0
$$



Then



$$
\left. \left( x_{1} + 2x_{2} + 3x_{3} \right) \right. + \left. \left( y_{1} + 2y_{2} + 3y_{3} \right) \right. = 0 + 0 = 0
$$



From which we can conclude that $\left. \left( x_{1} + y_{1},x_{2} + y_{2},x_{3} + y_{3} \right) \right. \in U$.

\(3\) Take any $a \in \mathbb{F}$ and $\left. \left( x_{1},x_{2},x_{3} \right) \right. \in U$. This means that $x_{1} + 2x_{2} + 3x_{3} = 0$. Then



$$
\begin{aligned}
\left. \left( ax_{1} \right) \right. + 2\left. \left( ax_{2} \right) \right. + 3\left. \left( ax_{3} \right) \right. & = a\left. \left( x_{1} + 2x_{2} + 3x_{3} \right) \right. \\
 & = a \cdot 0 \\
 & = 0
\end{aligned}
$$



Thus this is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).

### (b)

> $\{\left. \left( x_{1},x_{2},x_{3} \right) \right. \in \mathbb{F}^{3}:x_{1} + 2x_{2} + 3x_{3} = 4\}$

Of course this is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).. This fails part (1) of Theorem 1.34 since $0 + 2\left. (0) \right. + 3\left. (0) \right. \neq 4$.

### (c)

> $\{\left. \left( x_{1},x_{2},x_{3} \right) \right. \in \mathbb{F}^{3}:x_{1}x_{2}x_{3} = 0\}$

Let $U = \{\left. \left( x_{1},x_{2},x_{3} \right) \right. \in \mathbb{F}^{3}:x_{1}x_{2}x_{3} = 0\}$.

$U$ is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{F}^{3}$. Take $u = \left. (0,1,1) \right. \in U$ and $w = \left. (1,1,0) \right. \in U$. Then, $u + w = \left. (1,2,1) \right. \notin U$. So this fails the condition of [closure](/notes/areas/mathematics/topology/definitions/closure/) under vector addition.

### (d)

> $\{\left. \left( x_{1},x_{2},x_{3} \right) \right. \in \mathbb{F}^{3}:x_{1} = 5x_{3}\}$

Let $U = \{\left. \left( x_{1},x_{2},x_{3} \right) \right. \in \mathbb{F}^{3}:x_{1} = 5x_{3}\}$

1\) Take any $x_{1} = x_{2} = x_{3} = 0$. Then $x_{1} = 5x_{3}$ gives $0 = 0$. So, $\left. (0,0,0) \right. \in U$.

2\) Take any $x = \left. \left( x_{1},x_{2},x_{3} \right) \right. \in U$ and $y = \left. \left( y_{1},y_{2},y_{3} \right) \right. \in U$. Then $x + y$ gives



$$
x + y = \left. \left( x_{1} + y_{1},x_{2} + y_{2},x_{3} + y_{3} \right) \right.
$$



and



$$
x_{1} + y_{1} = 5x_{3} + 5y_{3} = 5\left. \left( x_{3} + y_{3} \right) \right.
$$



so $U$ is closed under vector addition.

3\) Choose any $a \in \mathbb{F}$ and $x = \left. \left( x_{1},x_{2},x_{3} \right) \right. \in U$. Then, $ax = a\left. \left( 5x_{3} \right) \right. = 5\left. \left( ax_{3} \right) \right.$. So, $U$ is closed under scalar multiplication.

## Exercise 1.C.2

> Verify all the assertions in Example 1.35.

This was worked through previously. See above.

## Exercise 1.C.3

> Show that the set of differentiable real-valued functions $f$ on the interval $\left. ( - 4,4) \right.$ such that $f'\left. ( - 1) \right. = 3f\left. (2) \right.$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{\left. ( - 4,4) \right.}$.

See <https://math.stackexchange.com/a/3471524>

Let $X = \{ f \in \mathbb{R}^{\left. ( - 4,4) \right.}:f\mathrm{\text{ is differentiable and }}f'\left. ( - 1) \right. = 3f\left. (2) \right.\}$.

Prove the three properties of [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s.

\(1\) The zero vector of the [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) $\mathbb{R}^{\left. ( - 4,4) \right.}$ is the function $0:\left. ( - 4,4) \right. \rightarrow \mathbb{R}$ defined by $0\left. (x) \right. = 0$. The zero function is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) and satisfies that $0'\left. (1) \right. = 3 \cdot 0\left. (2) \right. = 0$. So $0 \in X$.

\(2\) Choose $f,g \in X$. We know that $\left. (f + g) \right.$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) by the [Algebraic_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_differentiability_theorem/) (Abbott --- Theorem 5.2.4 part i), and $\left. (f + g) \right.'\left. ( - 1) \right. = f'\left. ( - 1) \right. + g'\left. ( - 1) \right. = 3f\left. (2) \right. + 3g\left. (2) \right. = 3\left. \left\lbrack f\left. (2) \right. + g\left. (2) \right. \right\rbrack \right. = 3\left. \left\lbrack \left. (f + g) \right.\left. (2) \right. \right\rbrack \right.$. Thus $f + g \in X$.

\(3\) Choose $a \in \mathbb{F}$ and $f \in X$. By the [Algebraic_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_differentiability_theorem/) (Abbott --- Theorem 5.2.4 part ii), we know that $af$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/), and that $\left. (af) \right.'\left. ( - 1) \right. = a\left. \left( f'\left. ( - 1) \right. \right) \right. = a\left. \left\lbrack 3f\left. (2) \right. \right\rbrack \right. = 3\left. \left\lbrack \left. (af) \right.\left. (2) \right. \right\rbrack \right.$. Thus $af \in X$.

## Exercise 1.C.4

> Suppose $b \in \mathbb{R}$. Show that the set of continuous real-valued functions $f$ on the interval $\left. \lbrack 0,1\rbrack \right.$ such that $\int_{0}^{1}f = b$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{\left. \lbrack 0,1\rbrack \right.}$ if and only if $b = 0$.

Let X = $\{ f \in \mathbb{R}^{\left. \lbrack 0,1\rbrack \right.}:f\mathrm{\text{ is continuous and }}\int_{0}^{1}f = b\}$.

\(1\) Certainly, $0 \in X$ since the zero function $0\left. (x) \right. = 0$ is continuous and $\int_{0}^{1}0\left. (x) \right.dx = 0$.

\(2\) Choose $f,g \in X$. It follows by the [Algebraic_Continuity_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_continuity_theorem/) (Abbott -- Theorem 4.3.4 part ii) that $f + g$ is continuous. By the [Properties_of_the_Integral](/notes/areas/mathematics/real_analysis/definitions/properties_of_the_integral/) (Abbott -- Theorem 7.4.2 part i), we know that $\left. (f + g) \right.$ is integrable. So we have $\int_{0}^{1}f\left. (x) \right.dx + \int_{0}^{1}g\left. (x) \right. = 0 + 0 = 0$.

\(3\) Choose $a \in \mathbb{F}$ and $f \in X$. Again by the [Algebraic_Continuity_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_continuity_theorem/) (Abbott --- Theorem 7.4.2 part i), $af$ is continuous. Then, $af$ is also integrable by the [Properties_of_the_Integral](/notes/areas/mathematics/real_analysis/definitions/properties_of_the_integral/) (Abbott --- Theorem 7.4.2 part ii) So we have $\int_{0}^{1}0\left. (x) \right.dx = 0 = b$.

## Exercise 1.C.5

> Is $\mathbb{R}^{2}$ a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of the complex [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) $\mathbb{C}^{2}$?

If $\mathbb{R}^{2}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of the complex [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) $\mathbb{C}^{2}$, then



$$
i\left. (1,1) \right. = \left. (i,i) \right. \in \mathbb{R}^{2}
$$



which is a contradiction. Thus, $\mathbb{R}^{2}$ is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of the complex [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) $\mathbb{C}^{2}$.

## Exercise 1.C.6

### (a)

> Is $\{\left. (a,b,c) \right. \in \mathbb{R}^{3}:a^{3} = b^{3}\}$ a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{3}$?

Because $a^{3} = b^{3}$ if and only if $a = b \in R$,



$$
\{\left. (a,b,c) \right. \in \mathbb{R}^{3}\} = \{\left. (a,b,c) \right. \in \mathbb{R}^{3}:a = b\}
$$



is obviously a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{3}$ by similar arguments in Exercise 1.C.1 and 1.C.2.

### (b)

> Is $\{\left. (a,b,c) \right. \in \mathbb{C}^{3}:a^{3} = b^{3}\}$ a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{C}^{3}$?

Note that



$$
x = \left. \left( 1,\frac{- 1 + \sqrt{3}i}{2},0 \right) \right. \in \{\left. (a,b,c) \right. \in \mathbb{C}^{3}:a^{3} = b^{3}\}
$$



and



$$
y = \left. \left( 1,\frac{- 1 - \sqrt{3}i}{2},0 \right) \right. \in \{\left. (a,b,c) \right. \in \mathbb{C}^{3}:a^{3} = b^{3}\}
$$



However



$$
x + y = \left. (2, - 1,0) \right. \notin \{\left. (a,b,c) \right. \in \mathbb{C}^{3}:a^{3} = b^{3}\}
$$



This implies that $\{\left. (a,b,c) \right. \in \mathbb{C}^{3}:a^{3} = b^{3}\}$ is not closed under addition and thus is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{C}^{3}$.

## Exercise 1.C.7

> Give an example of a nonempty subset $U$ of $\mathbb{R}^{2}$ such that $U$ is closed under addition and under taking additive inverses (meaning $- u \in U$ whenever $u \in U$), but $U$ is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{2}$.

Let $U = \{\left. (x,y) \right. \in \mathbb{R}^{2}:x,y, \in \mathbb{Z}\}$. $U$ is not empty. If $\left. \left( x_{1},y_{1} \right) \right. \in A$ and $\left. \left( x_{2},y_{2} \right) \right. \in A$, then $x_{1},x_{2},y_{1},y_{2} \in \mathbb{Z}$. Hence $x_{1} + x_{2}$ and $y_{1} + y_{2}$ are integers. This means that $\left. \left( x1 + x_{2},y_{1} + y_{2} \right) \right. = \left. \left( x_{1},y_{1} \right) \right. + \left. \left( x_{2},y_{2} \right) \right. \in U$, and that $U$ is closed under addition. Similarly, since $\left. \left( - x_{1}, - y_{1} \right) \right. \in U$, it follows that $U$ is closed under additive inverses. However, $U$ is not closed under sclar multiplication since $\left. (1,1) \right. \in A$ while $\frac{1}{2}\left. (1,1) \right. \notin U$. Hence $U$ is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{2}$.

## Exercise 1.C.8

> Give an example of a nonempty subset $U$ of $\mathbb{R}^{2}$ such that $U$ is closed under scalar multiplication, but $U$ is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{2}$.

Let $U = \{\left. (x,y) \right. \in \mathbb{R}^{2}:x = 0\mathrm{\text{ or }}y = 0\}$. $U$ is not empty. If $\left. (x,0) \right. \in U$, then for any $\lambda \in \mathbb{R}$, we have



$$
\lambda\left. (x,0) \right. = \left. (\lambda x,0) \right. \in U
$$



Similarly, $\lambda\left. (0,y) \right. \in U$. Hence $U$ is closed under sclar multiplication. However, $\left. (1,0) \right.,\left. (0,1) \right. \in U$ while $\left. (1,1) \right. = \left. (1,0) \right. + \left. (0,1) \right. \notin U$. This implies that $U$ is not closed under addition, and thus is not a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{2}$.

## Exercise 1.C.9

> A function $f:\mathbb{R} \rightarrow \mathbb{R}$ is called *periodic* if there exists a positive number $p$ such that $f\left. (x) \right. = f\left. (x + p) \right.$ for all $x \in \mathbb{R}$. Is the set of periodic functions from $\mathbb{R}$ to $\mathbb{R}$ a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{R}^{\mathbb{R}}$? Explain.

Let $f\left. (x) \right. = \cos\left. (\pi x) \right. + \cos\left. (x) \right.$. $f\left. (x) \right.$ is not periodic.

## Exercise 1.C.10

> Suppose $U_{1}$ and $U_{2}$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$. Prove that the intersection $U_{1} \cap U_{2}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of V.

Proving the three properties of [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s:

\(1\) By definition, $0 \in U_{1}$ and $0 \in U_{2}$, thus $0 \in U_{1} \cap U_{2}$.

\(2\) If $x \in U_{1} \cap U_{2}$ and $y \in U_{1} \cap U_{2}$, then $x \in U_{1}$ and $y \in U_{1}$, thus $x + y \in U_{1}$ because $U_{1}$ is closed under addition (since we are given that $U_{1}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) ). Similarly for $x + y \in U_{2}$. Therefore $x + y \in U_{1} \cap U_{2}$.

\(3\) If $x \in U_{1} \cap U_{2}$, then $x \in U_{1}$. Then for any $\lambda \in \mathbb{F}$, we have $\lambda x \in U_{1}$ since $U_{1}$ is closed under scalar multiplication (since we are given that $U_{1}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) ). Similarly, $\lambda x \in U_{2}$. Therefore $\lambda x \in U_{1} \cap U_{2}$.

## Exercise 1.C.11

> Prove that the intersection of every collection of [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$.

Let $U_{i}$ be [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$, where $i \in I$. We claim that $\bigcap_{i \in I}U_{i}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$.

Proving the three properties of [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s:

\(1\) By definition, $0 \in U_{i}\forall i \in I$, thus $0 \in \bigcap_{i \in I}U_{i}$.

\(2\) If $x \in \bigcap_{i \in I}U_{i}$ and $y \in \bigcap_{i \in I}U_{i}$, then for any given $i \in I$, we have $x \in U_{i}$ and $y \in U_{i}$, thus $x + y \in U_{i}$ since $U_{i}$ is closed under addition because we are given that $U_{i}$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/). Thus $x + y \in \bigcap_{i \in I}U_{i}$.

\(3\) If $x \in \bigcap_{i \in I}U_{i}$ for any given $i \in I$, then $x \in U_{i}$. Then for any $\lambda \in \mathbb{F}$, we have $\lambda x \in U_{i}$ since $U_{i}$ is closed under scalar multiplication. Thus $\lambda x \in \bigcap_{i \in I}U_{i}$.

## Exercise 1.C.12

> Prove that the union two [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$ if and only if one of the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s is contained in the other.

See: [here](https://yutsumura.com/union-of-subspaces-is-a-subspace-if-and-only-if-one-is-included-in-another/).

Let $U$ and $W$ be [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$.

$\left. ( \Rightarrow ) \right.$ Claim: If $U \subseteq W$ or $W \subseteq U$, then $U \cup W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$.

Proof: Assume $U \cup W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/). Proceed via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/) and assume that $U \nsubseteq W$ and $W \nsubseteq U$. This means that there are elements $u \in U\backslash W$ and $winW\backslash U$. Now, since $U \cup W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/), it is closed under addition. Thus we have $u + w \in U + W$. It follows that



$$
u + w \in U\quad\mathrm{\text{or}}\quad u + w \in W
$$



Suppose that $u + w \in U$. Then we write



$$
w = \left. (u + w) \right. - u
$$



Since both $u$ and $u + w$ are elements of the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) $U$, their difference $u = \left. (u + w) \right. - w$ is also in $U$. However, this contradicts the choice of $w \in W\backslash U$. The same is true for the other case, $u + w \in W$. By contradiction, then, we have either $U \subseteq W$ or $W \subseteq U$.

$\left. ( \Leftarrow ) \right.$ Claim: $U \cup W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$ if $U \subseteq W$ $W \subseteq U$.

Proof: Assume $U \subseteq W$, in which case $U \cup W = W$. Since $W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/), it follows that $U \cup W$ is also a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).

## Exercise 1.C.13

> Prove that the union of three [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$ if and only if one of the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s contains the other two. [This exercise is surprisingly harder than the previous exercise, possibly because this exercise is not true if we replace $\mathbb{F}$ with a field containing only two elements.]

See [here](https://math.stackexchange.com/questions/60698/if-a-field-f-is-such-that-leftf-rightn-1-why-is-v-a-vector-space-over) and [here](https://math.stackexchange.com/questions/692376/a-question-on-vector-space-over-an-infinite-field?rq=1).

## Exercise 1.C.14

> Verify the assertion in Example 1.38.

This has been worked through above.

## Exercise 1.C.15

> Suppose $U$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$. What is $U + U$?

$U$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$ and thus closed under addition.

\(1\) For any $x,y \in U$, since $U$ is closed under addition, we have $x + y \in U$, i.e. $U + U \subseteq U$.

\(2\) If $x \in U$, then $x = x + 0 \in U + U$, thus $U \subseteq U + U$.

Having shown these two things, it follows that $U + U = U$.

## Exercise 1.C.16

> Is the operation of addition on the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$ commutative? In other words, if $U$ and $W$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$, is $U + W = W + U$?

For $x \in U$ and $y \in W$, because addition in a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) $V$ is commutative, we have $x + y = y + x \in W + U$. This implies that $U + W \subseteq W + U$. Similarly, $W + U \subseteq U + W$. Thus $U + W = W + U$.

## Exercise 1.C.17

> Is the operation of addition on the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of V associative? In other words, if $U_{1},U_{2},U_{3}$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$, is
>
> 

$$
\left. \left( U_{1} + U_{2} \right) \right. + U_{3} = U_{1} + \left. \left( U_{2} + U_{3} \right) \right.?
$$



In some [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) $V$, we have $\left. (x + y) \right. + z = x + \left. (y + z) \right.$. Let $xi \in U_{i}$ for $i = 1,2,3$, then



$$
\left. \left( x_{1} + x_{2} \right) \right. + x_{3} = x_{1} + \left. \left( x_{2} + x_{3} \right) \right. \in U_{1} + \left. \left( U_{2} + U_{3} \right) \right.
$$



Since every element in $\left. \left( U_{1} + U_{2} \right) \right. + U_{3}$ can be expressed in the form $\left. \left( x_{1} + x_{2} \right) \right. + x_{3}$, it follows that $\left. \left( U_{1} + U_{2} \right) \right. + U_{3} \subseteq U_{1} + \left. \left( U_{2} + U_{3} \right) \right.$. Similarly, $U_{1} + \left. \left( U_{2} + 3 \right) \right. \subseteq \left. \left( U_{1} + U_{2} \right) \right. + U_{3}$. Hence $\left. \left( U_{1} + U_{2} \right) \right. + U_{3} = U_{1} + \left. \left( U_{2} + U_{3} \right) \right.$.

## Exercise 1.C.18

> Does the operation of addition on the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$ have an additive identity? Which [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s have additive inverses?

Claim: The [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) $\{ 0\}$ is the additive identity, i.e. $U + \{ 0\} = U$ for all [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s $U$.

Proof: (1) Choose $v \in U + \{ 0\}$. There exists a $u \in U$ such that $v = u + 0$, and this shows that $v = u \in U$. Thus $U + \{ 0\} \subseteq U$.

\(2\) Now, choose $u \in U$. Then, $u = u + 0$ shows that $u \in U + \{ 0\}$. Thus $U \subseteq U + \{ 0\}$.

\(1\) and (2) above imply that $U + \{ 0\} = U$.

We claim that for all [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s $U$ and $W$, $U + W = \{ 0\}$ implies $U = W = \{ 0\}$, which means that the [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s that have additive inverses are only $\{ 0\}$ itself.

Choose [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s $U$ and $W$. Assume $U + W = \{ 0\}$. Theorem 1.39 of Axler shows that $U \subseteq U + W$ and $W \subseteq U + W$. Thus, $U \subseteq \{ 0\}$ and $W \subseteq \{ 0\}$. Note that the only two subsets of $\{ 0\}$ are $\varnothing$ and $\{ 0\}$. Also, the premise that $U$ and $W$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s implies that $0 \in U$ and $0 \in W$, thus $U = W = \{ 0\}$.

## Exercise 1.C.19

> Prove or give a counterexample: if $U_{1}$, $U_{2}$, $W$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$ such that
>
> 

$$
U_{1} + W = U_{2} + W
$$


>
> then $U_{1} = U_{2}$.

Counterexample: Define the following:

$V = \mathbb{R}^{2}$

$U_{1} = \mathbb{R}^{2}$

$U_{2} = \{\left. (x,0) \right.:x \in \mathbb{R}\}$

$W = \{\left. (0,x) \right.:x \in \mathbb{R}\}$

Then $U_{1} + W = U_{2} + W$, but $U_{1} \neq U_{2}$.

## Exercise 1.C.20

> Suppose
>
> 

$$
U = \{\left. (x,x,y,y) \right. \in \mathbb{F}^{4}:x,y \in \mathbb{F}\}
$$


>
> Find a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) $W$ of $\mathbb{F}^{4}$ such that $\mathbb{F}^{4} = U \oplus W$

Restating Theorem 1.C.45

> Suppose $U$ and $W$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$. Then $U + W$ is a direct sum if and only if $U \cap W = \{ 0\}$.

Let $W = \{\left. (0,b,0,d) \right. \in \mathbb{F}^{4}:b,d \in \mathbb{F}\}$. For any $\left. (a,b,c,d) \right. \in \mathbb{F}^{4}$, we have



$$
\left. (a,b,c,d) \right. = \left. (x,x,y,y) \right. + \left. (0,b - x,0,d - y) \right. \in U + W
$$



since $\left. (x,x,y,y) \right. \in U$ and $\left. (0,b - x,0,d - y) \right. \in W$. So we have $\mathbb{F}^{4} = U + W$.

Moreover, if $\left. (a,b,c,d) \right. \in U \cap W$, then $a = b$ and $c = d$ since $\left. (a,b,c,d) \right. \in U$.

Similarly, since $\left. (a,b,c,d) \right. \in W$, we have $a = 0$ and $b = 0$. Therefore, $a = b = 0$ and $c = d = 0$, thus $\left. (a,b,c,d) \right. = \left. (0,0,0,0) \right.$. It follows that $U \cap W = \{ 0\}$. Hence $F = U \oplus W$ by Theorem 1.4.5.

## Exercise 1.C.21

> Suppose
>
> 

$$
U = \{\left. (x,y,x + y,x - y,2x) \right. \in \mathbb{F}^{5}:x,y \in F\}
$$


>
> Find a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) W of $\mathbb{F}^{5}$ such that $\mathbb{F}^{5} = U \oplus W$.

Let $W = \{\left. (0,0,c,d,e) \right. \in \mathbb{F}^{5}:c,d,e \in \mathbb{F}\}$. For any $\left. (a,b,c,d,e) \right. \in \mathbb{F}^{5}$, we have



$$
\left. (a,b,c,d,e) \right. = \left. (x,y,x + y,x - y,2x) \right. + \left. (0,0,c - x - y,d - x + y,e - 2x) \right. \in U + W
$$



Since $\left. (x,y,x + y,x - y,2x) \right. \in U$ and $\left. (0,0,c - x - y,d - x + y,e - 2x) \right. \in W$, $\mathbb{F}^{5} = U + W$.

Finally, since $U \cap W = 0$, it follows from Theorem 1.45 that $\mathbb{F}^{5} = U \oplus W$.

## Exercise 1.C.22

> Suppose
>
> 

$$
U = \{\left. (x,y,x + y,x - y,2x) \right. \in \mathbb{F}^{5}:x,y \in F\}
$$


>
> Find three [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s $W_{1},W_{2},W_{3}$ of $\mathbb{F}^{5}$, none of which equals $\{ 0\}$, such that $\mathbb{F}^{5} = U \oplus W_{1} \oplus W_{2} \oplus W_{3}$.

Let $W_{1} = \{\left. (0,0,a,0,0) \right. \in \mathbb{F}^{5}:a \in \mathbb{F}\}$ and

Let $W_{2} = \{\left. (0,0,0,b,0) \right. \in \mathbb{F}^{5}:b \in \mathbb{F}\}$ and

Let $W_{3} = \{\left. (0,0,0,0,c) \right. \in \mathbb{F}^{5}:c \in \mathbb{F}\}$ and

By the same arguments in Exercises 1.C.20/21,



$$
\mathbb{F}^{5} = U \oplus W1 \oplus W2 \oplus W3
$$



## Exercise 1.C.23

> Prove or give a counterexample: if $U_{1},U_{2},W$ are [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)s of $V$ such that
>
> 

$$
V = U_{1} \oplus W\quad\mathrm{\text{and}}\quad V = U_{2} \oplus W.
$$

 then $U_{1} = U_{2}$.

Counterexample: Let

$V = \mathbb{R}^{2}$,

$U_{1} = \{\left. (x,0) \right. \in \mathbb{R}^{2}:x \in \mathbb{R}\}$,

$U_{2} = \{\left. (0,y) \right. \in \mathbb{R}^{2}:y \in \mathbb{R}\}$,

$W = \{\left. (a,a) \right. \in \mathbb{R}^{2}:a \in \mathbb{R}\}$,

Then by the same argument in Exercise 1.C.21, we have



$$
V = U_{1} \oplus W\quad\mathrm{\text{and}}\quad U_{2} \oplus W
$$



but $U_{1} \neq U_{2}$.

## Exercise 1.C.24

> A function $f:\mathbb{R} \rightarrow \mathbb{R}$ is called *even* if
>
> 

$$
f\left. ( - x) \right. = f\left. (x) \right.
$$


>
> for all $x \in \mathbb{R}$. A function $f:\mathbb{R} \rightarrow \mathbb{R}$ is called *odd* if
>
> 

$$
f\left. ( - x) \right. = - f\left. (x) \right.
$$


>
> for all $x \in \mathbb{R}$. Let $U_{e}$ denote the set of real-valued functions on $\mathbb{R}$ and let $U_{o}$ denote the set of real-valued functions on $\mathbb{R}$. Show that $\mathbb{R}^{\mathbb{R}} = U_{e} \oplus U_{o}$.

Given any $f \in \mathbb{R}^{\mathbb{R}}$, define $f_{e}\left. (x) \right.$ to be $\left. \left\lbrack f\left. (x) \right. + f\left. ( - x) \right. \right\rbrack \right./2$ and define $f_{o}\left. (x) \right.$ to be $\left. \left\lbrack f\left. (x) \right. - f\left. ( - x) \right. \right\rbrack \right./2$ for all $x \in \mathbb{R}$. Then $f_{e},f_{o} \in \mathbb{R}^{\mathbb{R}}$. Morever, for all $x \in \mathbb{R}$, we have



$$
f_{e}\left. ( - x) \right. = \frac{f\left. ( - x) \right. + f\left. (x) \right.}{2} = \frac{f\left. (x) \right. + f\left. ( - x) \right.}{2} = f_{e}\left. (x) \right.
$$



and



$$
f_{o}\left. ( - x) \right. = \frac{f\left. ( - x) \right. - f\left. (x) \right.}{2} = - \frac{f\left. (x) \right. - f\left. ( - x) \right.}{2} = f_{o}\left. (x) \right.
$$



hence $f = f_{e} + f_{0} \in U_{e} + U_{o}$. Since we can choose any $f$ arbitrarily, one has $\mathbb{R}^{\mathbb{R}} = U_{e} + U_{o}$.

By Theorem 1.45, to show $\mathbb{R}^{\mathbb{R}} = U_{e} \oplus U_{o}$, it sufficies to prove that $U_{e} \cap U_{o} = \{ 0\}$. Let $f \in U_{e} \cap U_{o}$, then $f\left. (x) \right. = f\left. ( - x) \right.$ since $f \in U_{e}$ and $f\left. (x) \right. = - f\left. ( - x) \right.$ since $f \in U_{o}$ for all $x \in \mathbb{R}$. Sum up $f\left. (x) \right. = f\left. ( - x) \right.$ and $f\left. (x) \right. = - f\left. ( - x) \right.$, we have $f\left. (x) \right. = 0$ for all $x \in \mathbb{R}$. Hence $f = 0$, which implies $U_{e} \cap U_{o} = \{ 0\}$.

# Section 2.A Examples

## Example 2.A.4

> $\left. (17, - 4,2) \right.$ is a [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) of $\left. (2,1,3) \right.,\left. (1, - 2,4) \right.$ because 

$$
\left. (17, - 4,2) \right. = 6\left. (2,1, - 3) \right. + 5\left. (1, - 2,4) \right.
$$


>
> However, $\left. (17, - 4,5) \right.$ is *not* a [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) of $\left. (2,1, - 3) \right.,\left. (1, - 2,4) \right.$ because there do not exist numbers $a_{1},a_{2} \in \mathbb{F}$ such that 

$$
\left. (17, - 4,5) \right. = a_{1}\left. (2,1, - 3) \right. + a_{2}\left. (1, - 2,4) \right.
$$


>
> In other words, the system of equations
>
> 

$$
\begin{aligned}
2a_{1} + a_{2} & = 17 \\
a_{1} - 2a_{2} & = - 4 \\
\text{-} 3a_{1} + 4a_{2} & = 5
\end{aligned}
$$


>
> has no solutions ()*as you should verify*).

If we take the above system of equations and put it into reduced row echelon form, we get



$$
\begin{pmatrix}
2 & 1 & 17 \\
1 & - 2 & - 4 \\ - 3 & 4 & 5
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$



Since the last row has a nonzero number in the last column and 0's in all other columns, we know that this system of equations has no solution.

## Theorem 2.7: [span](/notes/areas/mathematics/linear_algebra/definitions/span/) is the smallest containing [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/)

> The [span](/notes/areas/mathematics/linear_algebra/definitions/span/) of a [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of vectors in $V$ is the smallest [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$ containing all the vectors in the [list](/notes/areas/mathematics/linear_algebra/definitions/list/).

See this [example](https://math.stackexchange.com/questions/3061117/prove-span-is-the-smallest-containing-subspace).

Also see this [video](https://www.youtube.com/watch?v=aSEnxo_YxIs).

Let $L = \left. \left( v_{1},\ldots,v_{m} \right) \right.$ be a [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of vectors in $V$.

\(1\) We will show that $\text{span }\left. (L) \right.$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $V$. The additive identity is in $\text{span }\left. (L) \right.$, because



$$
0 = 0v_{1} + \cdots + 0v_{m}
$$



Also, $\text{span }\left. (L) \right.$ is closed under addition, because



$$
\left. \left( a_{1}v_{1} + \cdots + a_{m}v_{m} \right) \right. + \left. \left( c_{1}v_{1} + \cdots + c_{m}v_{m} \right) \right. = \left. \left( a_{1} + c_{1} \right) \right.v_{1} + \cdots + \left. \left( a_{m} + c_{m} \right) \right.v_{m}
$$



which of course is an element of $\text{span }\left. (L) \right.$.

Furthermore, $\text{span }\left. (L) \right.$ is closed under scalar multiplication, because



$$
\lambda\left. \left( a_{1}v_{1} + \cdots + a_{m}v_{m} \right) \right. = \lambda a_{1}v_{1} + \cdots + \lambda a_{m}v_{m}
$$



which again is an element of $\text{span }\left. (L) \right.$. So, $\text{span }\left. (L) \right.$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).

\(2\) Here, we want to show that $\text{span }\left. (L) \right.$ contains $v_{1},\ldots,v_{m}$. We wish to express $v_{j}$ as a [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) of the vectors $v_{1},\ldots,v_{m}$. So suppose that



$$
v_{j} = a_{1}v_{1} + \cdots + a_{j}v_{j} + \cdots + a_{m}v_{m}
$$



Then, we can let $a_{j} = 1$ and let all other $a$ terms be zero, so we then get $v_{j}$ back. Which means we can get any of the individual vectors back. So we have shown that $\text{span }\left. (L) \right.$ contains each $v_{j}$.

\(3\) Suppose that $W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) containing $v_{1},\ldots,v_{m}$. Then we show that $W$ contains $\text{span }\left. (L) \right.$. Let $u \in \text{ span }\left. (L) \right.$. Then $u = a_{1}v_{1} + \cdots + a_{m}v_{m}$.[1] Since $W$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/), it is closed under scalar multiplication and addition, thus it contains $u$, so we know that $u \in W$. Thus, $u \in \text{ span }\left. (L) \right. \Rightarrow u \in W$ and thus $\text{span }\left. (L) \right. \subseteq W$.

[1] [The Math Sorcerer](https://www.youtube.com/watch?v=qeILRsTnHSs)

## Definition 2.11

> A function $p:\mathbb{F} \rightarrow \mathbb{F}$ is called a [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/) with coefficients in $\mathbb{F}$ if there exist $a_{0},\ldots,a_{m} \in \mathbb{F}$ such that
>
> 

$$
p\left. (z) \right. = a_{0} + a_{1}z + a_{2}z^{2} + \cdots + a_{m}z^{m}
$$


>
> for all $z \in \mathbb{F}$.
>
> $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ is the set of all [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)s with coefficients in $\mathbb{F}$.

> With the usual operations of addition and scalar multiplication, $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ is a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{F}$, *as you should verify*. In other words, $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/) of $\mathbb{F}^{\mathbb{F}}$, the [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) of functions from $\mathbb{F}$ to $\mathbb{F}$.

See this [example](https://www.youtube.com/watch?v=k3CnCq9b65M).

Instead of checking all ten [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) axioms, we only need to check that $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/). To determine this, we need to check that $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ : (1) contains the zero vector, (2) is closed under addition, (3) is closed under scalar multiplication.

\(1\) For all $a \in R$, let $a = 0 \Rightarrow p\left. (z) \right. = 0$.

\(2\) For $b_{0},b_{1},\ldots,b_{m} \in \mathbb{F}$ and $c_{0},c_{1},\ldots,c_{m} \in \mathbb{F}$, we have that



$$
\left. \left( b_{0} + b_{1}z + \cdots + b_{m}z^{m} \right) \right. + \left. \left( c_{0} + c_{1}z + \cdots c_{m}z^{m} \right) \right. = \left. \left( b_{0} + c_{0} \right) \right. + \left. \left( b_{1} + c_{1} \right) \right.z + \cdots + \left. \left( a_{m} + b_{m} \right) \right.z^{m}
$$



Which is an element of $p\left. (z) \right. = a_{0} + a_{1}z + a_{2}z^{2} + \cdots + a_{m}z^{m}$.

\(3\) For some arbitrary scalar $d \in \mathbb{F}$, $b \cdot \left. \left( a_{0} + a_{1}z + \cdots + a_{m}z^{m} \right) \right. = ba_{0} + ba_{1}z + \cdots + ba_{m}z^{m}$, which again is an element of $p\left. (z) \right. = a_{0} + a_{1}z + a_{2}z^{2} + \cdots + a_{m}z^{m}$.

Thus, $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ is a [subspace](/notes/areas/mathematics/linear_algebra/definitions/subspace/).

## Example 2.14

> $\mathcal{P}_{m}\left. \left( \mathbb{F} \right) \right.$ is a finite-dimensional [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) for each non-negative integer $m$.

## Example 2.16

> Show that $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ is infinite-dimensional.

Solution: Consider any [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of elements of $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$. Let $m$ denote the highest degree of the [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)s in this list. Then every [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/) in the [span](/notes/areas/mathematics/linear_algebra/definitions/span/) of this list has degree at most $m$. Thus $z^{m + 1}$ is not in the [span](/notes/areas/mathematics/linear_algebra/definitions/span/) of our list. Hence no list spans $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$. Thus $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ is infinite-dimensional.

## Example 2.18

> 1.  A list $v$ of one vector $v \in V$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) *if and only if* $v \neq 0$.
>
> 2.  A list of two vectors in $V$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) *if and only if* neither vector is a scalar multiple of the other.
>
> 3.  $\left. (1,0,0,0) \right.,\left. (0,1,0,0) \right.,\left. (0,0,1,0) \right.$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathbb{F}^{4}$.
>
> 4.  The list $1,z,\ldots,z^{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ for each non-negative integer $m$.

> If some vectors are removed from a [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) list, the remaining list is also [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/), *as you should verify*.

See this [example](https://math.stackexchange.com/a/2095420).

Proceed via [proof_by_contrapositive](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contrapositive/): if the vectors of a list are [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/), then when we add a vector, the new list will still be [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/).

It should be immediately obvious then that you can append any list of vectors, finite or infinite, even uncountable, to a [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/) set and the result is still a [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/) set. That's because once you have a nontrivial [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) summing to zero, you can add any additional vectors into that sum with all additional coefficients identically zero; this means that (1) the sum is still zero, and (2) the [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) is still non-trivial.

## Example 2.20: [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/) lists

### Part 1

> $\left. (2,3,1) \right.,\left. (1, - 1,2) \right.,\left. (7,3,8) \right.$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/) in $\mathbb{F}^{3}$ because
>
> 

$$
2\left. (2,3,1) \right. + 3\left. (1, - 1,2) \right. + \left. ( - 1) \right.\left. (7,3,8) \right. = \left. (0,0,0) \right.
$$



### Part 2

> The list $\left. (2,3,1) \right.,\left. (1, - 1,2) \right.,\left. (7,3,c) \right.$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/) in $\mathbb{F}^{3}$ *if and only if* $c = 8$, *as you should verify*.

We need to solve the following system of equations



$$
\begin{aligned}
x\left. (2,3,1) \right. + y\left. (1, - 1,2) \right. + z\left. (7,3,c) \right. & = \left. (0,0,0) \right. \\
\left. (2x + y + 7z,3x - y + 3z,x + 2y + cz) \right. & = \left. (0,0,0) \right.
\end{aligned}
$$



Let us isolate $y$ in the first element of the above list, which gives $y = - 7z - 2x$. Substituting this in the second element of the above list gives $3x - \left. ( - 7z - 2x) \right. + 3z = 0$. Then, solving for $x$ gives $x = - 2z$.

Then, plugging $x$ back into either equation and solving for $y$ gives $y = - 3z$.

Then, plugging $x$ and $y$ into the third element of the above list gives $- 2z + 2\left. ( - 3z) \right. + c*z = 0$, where solving for $c$ gives $c = 8$.

### Part 3

> If some vector in a list of vectors in V is a [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) of the other vectors, then the list is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/). (Proof: After writing one vector in the list as equal to a [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) of the other vectors, move that vector to the other side of the equation, where it will be multiplied by -1.)

### Part 4

> Every list of vectors in $V$ containing the 0 vector is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/). (This is a special case of the previous bullet point.)

# Section 2.A Exercises

## Exercise 2.A.1 (alternative [span](/notes/areas/mathematics/linear_algebra/definitions/span/) from an existing [span](/notes/areas/mathematics/linear_algebra/definitions/span/))

> Suppose $v_{1},v_{2},v_{3},v_{4}$ spans $V$. Prove that the [list](/notes/areas/mathematics/linear_algebra/definitions/list/)
>
> 

$$
v_{1} - v_{2},v_{2} - v_{3},v_{3} - v_{4},v_{4}
$$


>
> also [span](/notes/areas/mathematics/linear_algebra/definitions/span/)s $V$.

We need to show that $v_{1},v_{2},v_{3},v_{4}$ can be expressed as a [linear_combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) of $v_{1} - v_{2},v_{2} - v_{3},v_{3} - v_{4},v_{4}$.



$$
\begin{aligned}
v_{1} & = \left. \left( v_{1} - v_{2} \right) \right. + \left. \left( v_{2} - v_{3} \right) \right. + \left. \left( v_{3} - v_{4} \right) \right. + v_{4} \\
v_{2} & = \left. \left( v_{2} - v_{3} \right) \right. + \left. \left( v_{3} - v_{4} \right) \right. + v_{4} \\
v_{3} = \left. \left( v_{3} - v_{4} \right) \right. + v4 \\
v_{4} = v_{4}
\end{aligned}
$$



## Exercise 2.A.2 (examples of [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/)s)

> Verify the assertions in Example 2.18.

### (a)

> A list $v$ of one vector $v \in V$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) *if and only if* $v \neq 0$.

$\left. ( \Rightarrow ) \right.$: Assume that $v \in V$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/). Then, $v \neq 0$, otherwise we have that $1v = v = 0$, which means that $v$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/), which is a contradiction.

$\left. ( \Leftarrow ) \right.$: Conversely, assume that $v \neq 0$. By Exericse 1.B.2, if $v \neq 0$, then $av = 0$ implies that $a = 0$, so $v \in V$ must be [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

### (b)

> A list of two vectors in $V$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) *if and only if* neither vector is a scalar multiple of the other.

$\left. ( \Rightarrow ) \right.$: Assume that $v_{1},v_{2} \in V$ are [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/). Then, by definition, neither vector is a scalar multiple of the other. Otherwise, without loss of generality, we can assume that $v_{1} = cv_{2}$, then $1v_{1} + \left. ( - c) \right.v_{2} = 0$. It follows that $v_{1} \in V$, $v_{2} \in V$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/), which is a contradiction.

$\left. ( \Leftarrow ) \right.$: Conversely, if $v_{1} \in V$ and $v_{2} \in V$ are [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/), then there exist $a_{1}$ and $a_{2}$ such that $a_{1}v_{1} + a_{2}v_{2} = 0$ where $a_{1}$ and $a_{2}$ are not both zero. Without loss of generality, we can assume that $a_{1} \neq 0$. Then, $a_{1}v_{2} + a_{2}v_{2} = 0$ means that $v_{1} = - \left. \left( a_{2}/a_{1} \right) \right.v_{2}$, which is a contradiction since neither vector is a scalar multiple of the other.

### (c)

> $\left. (1,0,0,0) \right.,\left. (0,1,0,0) \right.,\left. (0,0,1,0) \right.$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathbb{F}^{4}$.

If there exist $x,y,z \in \mathbb{F}$ such that



$$
x\left. (1,0,0,0) \right. + y\left. (0,1,0,0) \right. + z\left. (0,0,1,0) \right. = 0
$$



then it means $\left. (x,y,z,0) \right. = \left. (0,0,0,0) \right.$. Hence $x = y = z = 0$, and it follows that the [list](/notes/areas/mathematics/linear_algebra/definitions/list/) is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathbb{F}^{4}$.

Put differently, consider the matrix form



$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} = \begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$



Since the coefficient matrix is non-singular, the only solution is $x = y = z = 0$.

### (d)

> The list $1,z,\ldots,z^{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ (see [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)) for each non-negative integer $m$.

To say that "the list $1,z,\ldots,z^{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathcal{P}\left. \left( \mathbb{F} \right) \right.$ (see [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)) for each non-negative integer $m$" means that the only choice of $a_{1},\ldots,a_{m} \in \mathbb{F}$ that makes $1 + a_{1}z + \cdots + a_{m}z^{m} = 0$ is $a_{1} = \cdots = a_{m} = 0$.

From page 31 of Axler, we have the conclusion that "the coefficients of a [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/) are uniquely determined by the [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)." Then, by the definition of [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) and using a similar method as in part c above, we can prove this case.

Another proof: consider the [function](/notes/areas/mathematics/set_theory/definitions/function/)



$$
f\left. (z) \right. = x_{0} + x_{1}z + \cdots + x_{N - 1}^{N - 1}
$$



where $N - 1 \geq 0$ and $x_{0},x_{1},\ldots,x_{N - 1} \in \mathbb{F}$. Suppose that $f\left. (z) \right. = 0$ for all $z \in \mathbb{F}$. Then, in particular, $f\left. (1) \right. = 0,f\left. (2) \right. = 0,\ldots,f\left. (N) \right. = 0$. In matrix form



$$
\begin{bmatrix}
1 & 1 & 1 & 1 & \cdots & 1 \\
1 & 2 & 1 & 1 & \cdots & 1 \\
1 & 3 & 1 & 1 & \cdots & 1 \\
 \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
1 & N & N^{2} & N^{3} & \cdots & N^{N - 1} \\
 & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & 
\end{bmatrix}\begin{bmatrix}
x_{0} \\
x_{1} \\
 \vdots \\
x_{N - 1}
\end{bmatrix} = \begin{bmatrix}
0 \\
0 \\
 \vdots \\
0
\end{bmatrix}
$$



Notice that the above coefficient matrix is a Vandermonde matrix. Since all the numbers $1,2,\ldots,N$ are distinct, its determinant is non-zero. Therefore the only solution is $x_{0} = x_{1} = \cdots = x_{N - 1} = 0$.

## Exercise 2.A.3 (a [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) list)

> Find a number $t$ such that
>
> 

$$
\left. (3,1,4) \right.,\left. (2, - 3,5) \right.,\left. (5,9,t) \right.
$$


>
> is not [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) (i.e., is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/)) in $\mathbb{R}^{3}$.

Similar to Example 2.18 part 2, we set



$$
x\left. (3,1,4) \right. + y\left. (2, - 3,5) \right. + z\left. (5,9,t) \right. = \left. (0,0,0) \right.
$$



So we have



$$
\left. (3x + 2y + 5z,x - 3y + 9z,4x + 5y + zt) \right. = \left. (0,0,0) \right.
$$



Let's look for a convenient variable to solve for. In the second element of the above list, solve for $x$: $x - 3y + 9z = 0 \Rightarrow x = 3y - 9z$.

Plugging $x = 3y - 9z$ into the first element of the list and solving for $y$ gives $y = 2z$.

Finally, plugging both $x = 3y - 9z$ and $y = 2z$ into the third element of the list and solving for $t$ gives $t = 2$.

## Exercise 2.A.4 (conditions to linear independence)

> Verify the assertion in the second bullet point in Example 2.20.

This was worked through above.

## Exercise 2.A.5 (difference between $\mathbb{C}$ and $\mathbb{R}$ as scalar fields)

### (a)

> Show that if we think of $\mathbb{C}$ as a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{R}$, then the list $\left. (1 + i,1 - i) \right.$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

For $x,y \in \mathbb{R}$ and $x\left. (1 + i) \right. + y\left. (1 - i) \right. = 0$, we have



$$
x\left. (1 + i) \right. + y\left. (1 - i) \right. = x + ix + y - iy = \left. (x + y) \right. + \left. (x - y) \right.i = 0
$$



From the above, since $x + y = 0$ and $x - y = 0$, it follows that $x = 0$ and $y = 0$. Thus the list $\left. (1 + i,1 - i) \right.$ [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) over $\mathbb{R}$.

### (b)

> Show that if we think of $\mathbb{C}$ as a [vector_space](/notes/areas/mathematics/linear_algebra/definitions/vector_space/) over $\mathbb{C}$, then the list $\left. (1 + i,1 - i) \right.$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/).

For $\left. (a + bi) \right.,\left. (c + di) \right. \in \mathbb{C}$, where $a,b,c,din\mathbb{R}$, we have



$$
\left. (a + bi) \right.\left. (1 + i) \right. + \left. (c + di) \right.\left. (1 - i) \right. = \left. (a - b + c + d) \right. + \left. (a + b - c + d) \right.i = 0
$$



From the above, since $\left. (a - b + c + d) \right. = 0$ and $\left. (a + b - c + d) \right. = 0$, it follows that $a = b = c = d = 0$. Thus the list $\left. (1 + i,1 - i) \right.$ [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) over $\mathbb{C}$.

## Exercise 2.A.6 (constructing another independent [list](/notes/areas/mathematics/linear_algebra/definitions/list/) from a [list](/notes/areas/mathematics/linear_algebra/definitions/list/))

> Suppose $v_{1},v_{2},v_{3},v_{4}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $V$. Prove that the list
>
> 

$$
v_{1} - v_{2},v_{2} - v_{3},v_{3} - v_{4},v_{4}
$$


>
> is also [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

Let $x,y,z,w \in \mathbb{F}$ such that



$$
x\left. \left( v_{1} - v_{2} \right) \right. + y\left. \left( y_{2} - v_{3} \right) \right. + z\left. \left( v_{3} - v_{4} \right) \right. + wv_{4} = 0
$$



Then,



$$
\begin{aligned}
x\left. \left( v_{1} - v_{2} \right) \right. + y\left. \left( y_{2} - v_{3} \right) \right. + z\left. \left( v_{3} - v_{4} \right) \right. + wv_{4} & = xv_{1} - xv_{2} + yv_{2} - yv_{3} + zv_{3} - zv_{4} + wv_{4} \\
 & = xv_{1} + \left. (y - x) \right.v_{2} + \left. (z - y) \right.v_{3} + \left. (w - z) \right.v_{4} = 0
\end{aligned}
$$



Because $v_{1},v_{2},v_{3},v_{4}$ are all assumed to be [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/), then $x = 0,y - x = 0,z - y = 0,w - z = 0$, which implies that $x = y = z = w = 0$. Thus the list



$$
v_{1} - v_{2},v_{2} - v_{3},v_{3} - v_{4},v_{4}
$$



is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $V$.

## Exercise 2.A.7 (constructing another independent [list](/notes/areas/mathematics/linear_algebra/definitions/list/) from a [list](/notes/areas/mathematics/linear_algebra/definitions/list/))

> Prove or give a counterexample: If $v_{1},v_{2},\ldots,v_{m}$ is a [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) list of vectors in $V$, then
>
> 

$$
5v_{1} - 4v_{2},v_{2},v_{3},\ldots,v_{m}
$$


>
> is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

This is true. For $a_{1},\ldots,a_{m} \in \mathbb{F}$ we have



$$
a_{1}\left. \left( 5v_{1} - 4v_{2} \right) \right. + a_{2}v_{2} + a_{3}v_{3} + \cdots + a_{m}v_{m} = 0
$$



so



$$
5a_{1}v_{1} + \left. \left( a_{2} - 4a_{1} \right) \right.v_{2} + a_{3}v_{3} + \cdots + a_{m}v_{m} = 0
$$



Because we are given that $v_{1},\ldots,v_{m}$ is a [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) list of vectors in $V$, it follows that



$$
5a_{1} = 0,a_{2} - 4a_{1} = 0,a_{3} = \cdots = a_{m} = 0
$$



so it must be that $a_{1} = a_{2} = \cdots = a_{m} = 0$, hence the list of vectors



$$
5v_{1} - 4v_{2},v_{2},v_{3},\ldots,v_{m}
$$



is also [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

## Exercise 2.A.8 ()[linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/) multiplied by scalar)

> Prove or give a counterexample: If $v_{1},\ldots,v_{m}$ is a [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of vectors in $V$ and $\lambda \in \mathbb{F}$ with $\lambda \neq 0$, then $\lambda v_{1},\lambda v_{2},\ldots,\lambda v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

This is true. For $a_{1},\ldots,a_{m} \in \mathbb{F}$ such that



$$
a_{1}\left. \left( \lambda v_{1} \right) \right. + a_{2}\left. \left( \lambda v_{2} \right) \right. + \cdots + a_{m}\left. \left( \lambda v_{m} \right) \right. = 0
$$



we have



$$
\left. \left( a_{1}\lambda \right) \right.v_{1} + \left. \left( a_{2}\lambda \right) \right.v_{2} + \cdots + \left. \left( a_{m}\lambda \right) \right.v_{m} = 0
$$



Since $v_{1},v_{2},\ldots,v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/), it follows that



$$
a_{1}\lambda = a_{2}\lambda = \cdots = a_{m}\lambda
$$



Since $\lambda = 0$, we can conclude that $a_{1} = a_{2} = \cdots = a_{m} = 0$, hence $\lambda v_{1},\lambda v_{2},\ldots,\lambda v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

## Exercise 2.A.9 (Addition of two [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/)s)

> Prove or give a counterexample: if $v_{1},\ldots,v_{m}$ and $w_{1},\ldots,w_{m}$ are [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/)s of vectors in $V$, then $v_{1} + w_{1},\ldots,v_{m} + w_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/).

Counterexample: let $w_{i} = - v_{i}$. Then, if $v_{1},v_{2},\ldots,v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/), we have $w_{1},w_{2},\ldots,w_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) by Exercise 2.A.8. However, $v_{1} + w_{1} = 0,v_{2} + w_{2} = 0,v_{m} + w_{m} = 0$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/).

## Exercise 2.A.10 (Adding a vector to a [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/))

> Suppose $v_{1},\ldots,v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $V$ and $w \in V$. Prove that if $v_{1} + w,\ldots,v_{m} + w$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/) then $w \in \text{ span }\left. \left( v_{1},\ldots,v_{m} \right) \right.$ (see [span](/notes/areas/mathematics/linear_algebra/definitions/span/)).

Assume that $v_{1} + w,\ldots,v_{m} + w$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/). Then there exist $a_{1},\ldots,a_{m} \in \mathbb{F}$, not all 0, such that



$$
a_{1}\left. \left( v_{1} + w \right) \right. + a_{2}\left. \left( v_{2} + w \right) \right. + a_{3}\left. \left( v_{3} + w \right) \right. + \cdots + a_{m}\left. \left( v_{m} + w \right) \right. = 0
$$



So we have



$$
\begin{aligned}
a_{1}\left. \left( v_{1} + w \right) \right. + a_{2}\left. \left( v_{2} + w \right) \right. + a_{3}\left. \left( v_{3} + w \right) \right. + \cdots + a_{m}\left. \left( v_{m} + w \right) \right. & = a_{1}v_{1} + \cdots + a_{m}v_{m} + \left. \left( a_{1} + \cdots + a_{m} \right) \right.w = 0 \\
 & = \left. \left( a_{1}v_{1} + a_{1}w \right) \right. + \left. \left( a_{2}v_{2} + a_{2}w \right) \right. + \cdots + \left. \left( a_{m}v_{m} + a_{m}w \right) \right. \\
 & = a_{1}v_{1} + \cdots + a_{m}v_{m} + \left. \left( a_{1} + \cdots + a_{m} \right) \right.w \\
 & = 0
\end{aligned}
$$



If $a_{1} + \cdots + a_{m} = 0$, then we get $a_{1}v_{1} + \cdots + a_{m}v_{m} = 0$, from which we can deduce that $a_{i} = 0$. Hence $a_{1} + \cdots + a_{m} \neq 0$. It follows that



$$
w = - \frac{1}{a_{1} + \cdots + a_{m}}\left. \left( a_{1}v_{1} + \cdots + a_{m}v_{m} \right) \right. \in \text{ span }\left. \left( v_{1},\ldots,v_{m} \right) \right.
$$



$\square$

## Exercise 2.A.11 (concatenating a vector to a [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/))

> Suppose $v_{1},\ldots,v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $V$ and $w \in V$. Show that $v_{1},\ldots,v_{m},w$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) *if and only if*
>
> 

$$
w \notin \text{ span }\left. \left( v_{1},\ldots,v_{m} \right) \right.
$$



See [span](/notes/areas/mathematics/linear_algebra/definitions/span/).

Also, see this [video](https://www.youtube.com/watch?v=qeILRsTnHSs), particularly at the 5m30s mark.

It is equivalent to show that $v_{1},\ldots,v_{m}$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/) *if and only if*



$$
w \in \text{ span }\left. \left( v_{1},\ldots,v_{m} \right) \right.
$$



()$\Rightarrow$): Assume that $v_{1},\ldots,v_{m},w$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/). Then there exist $a_{1},\ldots,a_{m},b \in \mathbb{F}$, not all 0, such that



$$
a_{1}v_{1} + \cdots + a_{m}v_{m} + bw = 0
$$



If $b = 0$, we get $a_{1}v_{1} + \cdots + a_{m}v_{m} = 0$, which implies that $v_{1},\ldots,v_{m}$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/), which contradicts the supposition in the problem description that $v_{1},\ldots,v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/). Thus, it must be that $b \neq 0$ and the above equation implies that



$$
w = - \frac{1}{b}\left. \left( a_{1}v_{1} + a_{2}v_{2} + \cdots + a_{m}v_{m} \right) \right. \in \text{ span }\left. \left( v_{1},\ldots,v_{m} \right) \right.
$$



()$\Leftarrow$): Assume that $w \in \text{ span }\left. \left( v_{1},\ldots,v_{m} \right) \right.$. Then there exist $a_{1},\ldots,a_{m} \in \mathbb{F}$ such that



$$
w = a_{1}v_{1} + \ldots + a_{m}v_{m} \Rightarrow a_{1}v_{1} + \cdots + a_{m}v_{m} - w = 0
$$



Again, our supposition in the problem description states that $v_{1},\ldots,v_{m}$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/), which implies that $a_{1}v_{1} + \cdots + a_{m}v_{m} = 0$, so we can conclude that $v_{1},\ldots,v_{m},w$ is [linearly_dependent](/notes/areas/mathematics/linear_algebra/definitions/linearly_dependent/).

## Exercise 2.A.12 ()[linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/)s in $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$) {#exercise-2.a.12-linearly-independent-lists-in-mathcalp_4mathbbf}

> Explain why there does not exist a [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of six [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)s that is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$.

From page 31 of Axler, we know that the list $1,z,z^{2},z^{3},z^{4}$ [span](/notes/areas/mathematics/linear_algebra/definitions/span/)s $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$, which has length 5. By Theorem 2.23 (length of [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/) $\leq$ length of [span](/notes/areas/mathematics/linear_algebra/definitions/span/)ning [list](/notes/areas/mathematics/linear_algebra/definitions/list/)), the length of every [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of vectors in $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$ is therefore less than or equal to 5. Thus there does not exist a [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of 6 [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)s that is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$.

## Exercise 2.A.13 (possible spans of $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$) {#exercise-2.a.13-possible-spans-of-mathcalp_4mathbbf}

> Explain why no [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of four [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)s [span](/notes/areas/mathematics/linear_algebra/definitions/span/)s $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$.

By Exercise 2.A.2(d), we know that the list $\left. \left( 1,z,z^{2},z^{3},z^{4} \right) \right.$ is [linearly_independent](/notes/areas/mathematics/linear_algebra/definitions/linearly_independent/) in $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$, which has length 5. By Theorem 2.23, we know that the length of every [span](/notes/areas/mathematics/linear_algebra/definitions/span/)ning [list](/notes/areas/mathematics/linear_algebra/definitions/list/) of $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$ is greater than or equal to 5. Thus no list of 4 [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/)s [span](/notes/areas/mathematics/linear_algebra/definitions/span/)s $\mathcal{P}_{4}\left. \left( \mathbb{F} \right) \right.$.
