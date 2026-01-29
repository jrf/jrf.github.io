---
title: "Measures Integrals and Martingales"
---

# Prologue: Examples

The least we should expect from a reasonable [measure](/notes/areas/mathematics/definitions_theorems/measure_theory/measure/) $\mu$ is that it is

1.  Well-defined, takes values in $\left. \lbrack 0,\infty\rbrack \right.$, and $\mu\left. (\varnothing) \right. = 0$;

2.  Additive, i.e. $\mu\left. (A \cup B) \right. = \mu\left. (A) \right. + \mu\left. (B) \right.$ whenever $A \cap B = \varnothing$ (finite additivity).

With the additional property that the [measure](/notes/areas/mathematics/definitions_theorems/measure_theory/measure/) $\mu$ is invariant under congruences and translations.

# Prologue: Exercises

## Exercise 1.1

> Use (1.4) to find the area of a circle with radius $r$.

See this [example](https://math.stackexchange.com/q/1075851).

Restating (1.4):



$$
\text{ area }\left. ( ○ ) \right. = \lim\limits_{n \rightarrow \infty}2^{n} \times \text{ area }\left. \left( \bigtriangleup \mathrm{\text{ at step }}n \right) \right.
$$



We have to calculate the area of an isosceles triangle with side length $b$, base $b$, height $h$, and angle $\phi = 2\pi/2^{j}$. From elementary geometry we know that



$$
\cos\frac{\phi}{2} = \frac{h}{r}\quad\mathrm{\text{and}}\quad\sin\frac{\phi}{2} = \frac{b}{2r}
$$



such that



$$
\text{ area }\left. ( \bigtriangleup ) \right. = \frac{1}{2}bh = r^{2}\cos\frac{\phi}{2}\sin\frac{\phi}{2} = \frac{r^{2}}{2}\sin\phi
$$



Since $\lim\limits_{\phi \rightarrow 0}\frac{\sin\phi}{\phi} = 1$, we have



$$
\begin{aligned}
\text{ area }\left. ( ○ ) \right. & = \lim\limits_{j \rightarrow \infty}2^{j}\frac{r^{2}}{2}\sin\frac{2\pi}{2^{j}} \\
 & = \pi r^{2}\lim\limits_{j \rightarrow \infty}\frac{\sin\left. \left( 2\pi/2^{j} \right) \right.}{2\pi/2^{j}} \\
 & = \pi r^{2}
\end{aligned}
$$



## Exercise 1.2

> Where was [sigma-additivity](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-additivity/) used when calculating the length of the [Cantor_set](/notes/areas/mathematics/definitions_theorems/real_analysis/cantor_set/)?

By construction of the [Cantor_set](/notes/areas/mathematics/definitions_theorems/real_analysis/cantor_set/), we have



$$
C_{n + 1} = [0, 1] \setminus \left[{\color{cyan}\left(\frac{1}{3}, \frac{2}{3}\right)} \cup {\color{magenta}\left(\frac{1}{9}, \frac{2}{9}\right) \cup \left(\frac{7}{9}, \frac{8}{9}\right)} \cup \cdots \right]
$$



where each interval has length $1/3^{n}$. As $n \rightarrow \infty$, we have for all removed intervals



$$
\sum_{n = 0}^{\infty}\frac{2^{n}}{3^{n + 1}} = 1
$$



where the last line above requires [sigma-additivity](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-additivity/).

## Exercise 1.3

> Consider the following variation of the [Cantor_set](/notes/areas/mathematics/definitions_theorems/real_analysis/cantor_set/): fix $r \in \left. (0,1) \right.$ and delete from $I_{0}$ the open interval $\left. \left( \frac{1}{2} - \frac{1}{4}r,\frac{1}{2} + \frac{1}{4}r \right) \right.$. This defines the set $I_{1}$ consisting of two intervals , $\left. \left\lbrack 0,\frac{1}{2} - \frac{1}{4}r \right\rbrack \right.$ and $\left. \left\lbrack \frac{1}{2} + \frac{1}{4}r,1 \right\rbrack \right.$. We get $I_{2}$ by removing from each of these intervals the open middles of length $r/8$ and $I_{3}$ by removing all open middles of length $r/32$. This defines recursively the sets $I_{1},I_{2},\ldots,I_{n}$. Find the length of the interval $I_{n}$ and of the generalized [Cantor_set](/notes/areas/mathematics/definitions_theorems/real_analysis/cantor_set/) $I = \bigcap_{n = 0}^{\infty}$. Is $I$ empty?

Recording the length of the removed pieces in each step, we have

1.  In step 1, we remove one ()$= 2^{0}$) piece of length $\left. \left( \frac{1}{2} + \frac{1}{4}r \right) \right. - \left. \left( \frac{1}{2} - \frac{1}{4}r \right) \right. = \frac{r}{2}$

2.  In step 2, we remove two ()$= 2^{1}$) pieces of length $\frac{1}{8}r$

3.  In step 3, we remove four ()$= 2^{2}$) pieces of length $\frac{1}{32}r$

We recognize the lengths of pieces removed as a geometric series with first term $\frac{r}{2}$ and common ratio $\frac{1/8r}{1/2r} = 1/4$. So at the $n$th step, the length is $\frac{r}{2}\left. \left( \frac{1}{4} \right) \right.^{n - 1} = 2^{1 - 2n}r$. So in each step we remove $2^{n - 1}2^{1 - 2n}r = 2^{- n}r$, i.e. we remove



$$
\sum_{n = 1}^{\infty}2^{- n}r = r
$$



Thus, $\mathcal{l}\left. (I) \right. = \mathcal{l}\left. \lbrack 0,1\rbrack \right. - r = 1 - r$. Thus the set has length $> 0$ and cannot be empty.

## Exercise 1.4

> Let $K_{0} \subseteq \mathbb{R}$ be a line of length 1. We get $K_{1}$ by replacing the middle third of $K_{0}$ by the sides of an equilateral triangle. By iterating this procedure we get the curves $K_{0},K_{1},K_{2},\ldots,K_{n}$ (see below) which defines in the limit the Koch_snowflake $K_{\infty}$. Find the length of $K_{n}$ and $K_{\infty}$.
>
> ![](/images/notes/Areas/mathematics/books/graphics/MIM/1.4.png)

In each step, the total length increases by the factor $4/3$, since we remove the middle interval with length $1/3$ and replace it with two copies constituting the sides of an equilateral triangle with length $2/3$. Thus,



$$
\mathcal{l}\left. \left( K_{n} \right) \right. = \frac{4}{3} \times \mathcal{l}\left. \left( K_{n - 1} \right) \right. = \cdots = \left. \left( \frac{4}{3} \right) \right.^{n}\mathcal{l}\left. \left( K_{0} \right) \right. = \left. \left( \frac{4}{3} \right) \right.^{n}
$$



In particular, $\lim\limits_{n \rightarrow \infty}\mathcal{l}\left. \left( K_{n} \right) \right. = \infty$.

Again, [sigma-additivity](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-additivity/) comes in the form of a limit (compare with Exercise 1.2).

Aside: from our course in discrete dynamical systems, we know that the [fractal_dimension](/notes/areas/mathematics/definitions_theorems/real_analysis/fractal_dimension/) of the Koch_snowflake is



$$
D = \frac{\log\left. \left( \mathrm{\text{number of copies}} \right) \right.}{\log\left. \left( \mathrm{\text{scaling factor}} \right) \right.} = \frac{\log\left. (4) \right.}{\log\left. (3) \right.} = 1.26186
$$



## Exercise 1.5

> Let $S_{0} \subseteq \mathbb{R}^{2}$ be a solid equilateral triangle. We get $S_{1}$ by removing the middle triangle whose vertices are the midpoints of the sides of $S_{1}$. By repeating this procedure with the four triangles which make up $S_{1}$ etc, we get $S_{0},S_{1},S_{2},\ldots,S_{n}$ (see below). The Sierpinksi_triangle is $S_{\infty} = \bigcap_{n = 0}^{\infty}S_{n}$. Find the area of $S_{n}$ and $S$ if the side-length of $S_{0}$ is $s = 1$.
>
> ![](/images/notes/Areas/mathematics/books/graphics/MIM/1.5.png)

In each step the total area is decreased by factor $3/4$, since we remove the middle triangle with area $1/4$. Thus



$$
\text{ area }\left. \left( S_{n} \right) \right. = \frac{3}{4} \times \text{ area }\left. \left( S_{n - 1} \right) \right. = \cdots = \text{ area }\left. \left( S_{0} \right) \right. = \left. \left( \frac{3}{4} \right) \right.^{n}\frac{\sqrt{3}}{4}
$$



In particular, $\text{area }\left. (S) \right. = \lim\limits_{n \rightarrow \infty}\text{ area }\left. \left( S_{n} \right) \right. = 0$.

Again, [sigma-additivity](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-additivity/) comes in the form of a limit (compare with Exercise 1.2). Notice that $S$ is non-empty as it contains the vertices of all black triangles (see figure above) of each stage.

# Chapter 2: The Pleasures of Counting -- Examples

See Exercise 1.2.3(c, d) in [Understanding_Analysis](/notes/areas/mathematics/books/understanding_analysis/) for a proof of (2.1).

See Exercise 1.2.5 in [Understanding_Analysis](/notes/areas/mathematics/books/understanding_analysis/) for a proof of [de_Morgan's_laws](/notes/areas/mathematics/definitions_theorems/set_theory/de_morgans_laws/) (2.2).

See Exercise 1.2.13(c) in [Understanding_Analysis](/notes/areas/mathematics/books/understanding_analysis/) for a proof of (2.3).

See Exercise 1.2.7 in [Understanding_Analysis](/notes/areas/mathematics/books/understanding_analysis/) for a proof of (2.5).

See [here](https://www.whitman.edu/mathematics/higher_math_online/section01.06.html) for an excellent explanation of index sets and families of sets.

## Theorem 2.10

> For any set $X$ we have that $\# X < \#\mathcal{P}\left. (X) \right.$.

Proof: We have to show that no [injection](/notes/areas/mathematics/definitions_theorems/set_theory/injection/) $\Phi:X \rightarrow \mathcal{P}\left. (X) \right.$ can also be a [surjection](/notes/areas/mathematics/definitions_theorems/set_theory/surjection/). Fix such an [injection](/notes/areas/mathematics/definitions_theorems/set_theory/injection/) and define



$$
B = \{ x \in X:x \notin \Phi\left. (x) \right.\}
$$



Note that $\Phi\left. (x) \right.$ and $B$ are both sets. Clearly, $B \in \mathcal{P}\left. (X) \right.$. Now, let us proceed via [proof_by_contradiction](/notes/areas/mathematics/definitions_theorems/proof_techniques/proof_by_contradiction/) and assume that $\Phi$ is a [surjection](/notes/areas/mathematics/definitions_theorems/set_theory/surjection/). If this were the case, then $B$, which again is always an element of $\mathcal{P}\left. (X) \right.$, must correspond to some element $z \in X$. Now, assume that $z$ is also an element of $B$ (which may not always be the case), then by construction of $B$, $z$ cannot be an element of $\Phi\left. (z) \right.$. But this implies that, since $\Phi\left. (z) \right. = B$, $z$ cannot be an element of $B$. This is impossible and thus $\Phi$ is not a [surjection](/notes/areas/mathematics/definitions_theorems/set_theory/surjection/).

# Chapter 2: The Pleasures of Counting -- Exercises

## Exercise 2.1

> Let $A,B,C \subseteq X$ be sets. Show that

### (i)

> $A\backslash B = A \cap B^{c}$

We have that



$$
\begin{aligned}
x \in A\backslash B & \Leftrightarrow x \in A\mathrm{\text{ and }}x \notin B \\
 & \Leftrightarrow x \in A\mathrm{\text{ and }}x \in B^{c} \\
 & \Leftrightarrow x \in A \cap B^{c}
\end{aligned}
$$



### (ii)

> $\left. (A\backslash B) \right.\backslash C = A\backslash\left. (B \cup C) \right.$

By [de_Morgan's_laws](/notes/areas/mathematics/definitions_theorems/set_theory/de_morgans_laws/) (DM) and part (i) above, we have



$$
\begin{aligned}
\left. (A\backslash B) \right.\backslash C & = \left. \left( A \cap B^{c} \right) \right. \cap C^{c}\mathtt{\text{ (by (i) above)}} \\
 & = A \cap B^{c} \cap C^{c} \\
 & = A \cap \left. \left( B^{c} \cap C^{c} \right) \right. \\
 & = A \cap \left. (B \cup C) \right.^{c}\mathtt{\text{ (DM)}} \\
 & = A\backslash\left. (B \cup C) \right.
\end{aligned}
$$



### (iii)

> $A\backslash\left. (B\backslash C) \right. = \left. (A\backslash B) \right. \cup \left. (A \cap C) \right.$

By [de_Morgan's_laws](/notes/areas/mathematics/definitions_theorems/set_theory/de_morgans_laws/) (DM) and part (i) above, we have



$$
\begin{aligned}
A\backslash\left. (B\backslash C) \right. & = A \cap \left. \left( B \cap C^{c} \right) \right.^{c}\mathtt{\text{ (by part (i))}} \\
 & = A \cap \left. \left( B^{c} \cup C \right) \right.\mathtt{\text{ (DM)}} \\
 & = \left. \left( A \cap B^{c} \right) \right. \cup \left. (A \cap C) \right. \\
 & = \left. (A\backslash B) \right. \cup \left. (A \cap C) \right.\mathtt{\text{ (by part (i))}}
\end{aligned}
$$



### (iv)

> $A\backslash\left. (B \cap C) \right. = \left. (A\backslash B) \right. \cup \left. (A\backslash C) \right.$

By [de_Morgan's_laws](/notes/areas/mathematics/definitions_theorems/set_theory/de_morgans_laws/) (DM) and part (i) above, we have



$$
\begin{aligned}
A\backslash\left. (B \cap C) \right. & = A \cap \left. (B \cap C) \right.^{c}\mathtt{\text{ (by part (i))}} \\
 & = A \cap \left. \left( B^{c} \cup C^{c} \right) \right.\mathtt{\text{ (DM)}} \\
 & = \left. \left( A \cap B^{c} \right) \right. \cup \left. \left( A \cap C^{c} \right) \right. \\
 & = \left. (A\backslash B) \right. \cup \left. (A\backslash C) \right.\mathtt{\text{ (by part (i))}}
\end{aligned}
$$



### (v)

> $A\backslash\left. (B \cup C) \right. = \left. (A\backslash B) \right. \cap \left. (A\backslash C) \right.$

By [de_Morgan's_laws](/notes/areas/mathematics/definitions_theorems/set_theory/de_morgans_laws/) (DM) and part (i) above, we have



$$
\begin{aligned}
A\backslash\left. (B \cup C) \right. & = A \cap \left. (B \cup C) \right.^{c}\mathtt{\text{ (by part (i))}} \\
 & = A \cap \left. \left( B^{c} \cap C^{C} \right) \right.\mathtt{\text{ (DM)}} \\
 & = A \cap B^{c} \cap C^{c} \\
 & = A \cap B^{c} \cap A \cap C^{c} \\
 & = \left. (A\backslash B) \right. \cap \left. (A\backslash C) \right.\mathtt{\text{ (by part (i))}}
\end{aligned}
$$



### (vi)

> $\left. (A \cup B) \right.\backslash C = \left. (A\backslash C) \right. \cup \left. (B\backslash C) \right.$

By definition and the distributive laws for sets we find that



$$
\begin{aligned}
\left. (A \cup B) \right.\backslash C & = \left. (A \cup B) \right. \cap C^{c} \\
 & = \left. \left( A \cap C^{c} \right) \right. \cup \left. \left( B \cap C^{c} \right) \right. \\
 & = \left. (A\backslash C) \right. \cup \left. (B\backslash C) \right.
\end{aligned}
$$



$▫$

## Exercise 2.2

> Let $A,B,C \subseteq X$. The [symmetric_difference](/notes/areas/mathematics/definitions_theorems/set_theory/symmetric_difference/) of $A$ and $B$ is $A \bigtriangleup B ≔ \left. (A\backslash B) \right. \cup \left. (B\backslash A) \right.$. Verify that
>
> 

$$
\left. (A \cup B \cup C) \right.\backslash\left. (A \cap B \cap C) \right. = \left. (A \bigtriangleup B) \right. \cup \left. (B \bigtriangleup C) \right.
$$

.

First, note that



$$
A\backslash C \subseteq \left. (A\backslash B) \right. \cup \left. (B\backslash C) \right.\mathtt{\text{ (*)}}
$$



This follows easily from



$$
\begin{aligned} A \setminus C &= (A \setminus C) \cap X \\ &= (A \cap C^{c}) \cap (B \cup B^{c}) \\ &= (A \cap C^{c} \cap B) \cup (A \cap C^{c} \cap B^{c}) \texttt{ (by the \href{https://math.stackexchange.com/questions/2411960/elementary-set-theory-proof-of-distributive-property}{distributive property of sets (DPS)})} \\ &\subseteq (B \cap C^{c}) \cup (A \cap B^{c}) \\ &= (B \setminus C) \cup (A \setminus B) \texttt{ (by Exercise 2.1(a))} \\ \end{aligned}
$$



Using the above and the analogous formula for $C\backslash A$, we have



$$
\begin{aligned} (A \cup B \cup C) \setminus (A \cap B \cap C) &= (A \cup B \cup C) \cap (A \cap B \cap C)^{c} \texttt{ (by 2.1(i))} \\ &= [A \cap (A \cap B \cap C)^{c}] \cup [B \cap (A \cap B \cap C)^{c}] \cup [C \cap (A \cap B \cap C)^{c}] \texttt{ (by \href{https://math.stackexchange.com/questions/2411960/elementary-set-theory-proof-of-distributive-property}{DPS})} \\ &= [A \setminus (A \cap B \cap C)] \cup [B \setminus (A \cap B \cap C)] \cup [C \setminus (A \cap B \cap C)] \texttt{ (by 2.1(i))} \\ &= [A \setminus (B \cap C)] \cup [B \setminus (A \cap C)] \cup [C \setminus (A \cap B)] \\ &= (A \setminus B) \cup (A \setminus C) \cup (B \setminus A) \cup (B \setminus C) \cup (C \setminus A) \cup (C \setminus B) \texttt{ (by 2.1(iv))}\\ &= (A \setminus B) \cup (B \setminus A) \cup (B \setminus C) \cup (C \setminus B) \texttt{ (by ()*))}\\ &= (A \triangle B) \cup (B \triangle C) \end{aligned}
$$



$▫$

## Exercise 2.3

> Prove [de_Morgan's_laws](/notes/areas/mathematics/definitions_theorems/set_theory/de_morgans_laws/) (2.2) and (2.3).

For (2.2), see Exercise 1.2.5 from [Understanding_Analysis](/notes/areas/mathematics/books/understanding_analysis/).

For (2.3) part 2, in order to prove that



$$
\left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c} = \bigcap_{i \in I}A_{i}^{c}
$$



we have have to show,



$$
\left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c} \subseteq \bigcap_{i \in I}A_{i}^{c}
$$



and



$$
\bigcap_{i \in I}A_{i}^{c} \supseteq \left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c}
$$



To demonstrate the first inclusion, let $x \in \left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c}$ and show that $x \in \bigcap_{i \in I}A_{i}^{c}$. If $x \in \left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c}$, then $x \notin A_{i}\forall i \in I.$ This implies that $x$ is in the complement of each $i \in I$, and by the definition of intersection, $x \in \bigcap_{i \in I}A_{i}^{c}$.

To demonstrate the reverse inclusion, let $x \in \bigcap_{i \in I}A_{i}^{c}$ and show that $x \in \left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c}$. So, if $x \in \bigcap_{i \in I}A_{i}^{c}$, then $x \in \bigcap_{i \in I}A_{i}^{c}$, then $x \in A_{i}^{c}\forall i \in I$, which means that $x \notin A_{i}\forall i \in I$. This implies that $x \notin \left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.$, from which we can conclude that $x \in \left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c}.$

For (2.3) part 1, in order to prove that



$$
\left. \left( \bigcap_{i \in I}A_{i} \right) \right.^{c} = \bigcup_{i \in I}A_{i}^{c}
$$



we have have to show,



$$
\left. \left( \bigcap_{i \in I}A_{i} \right) \right.^{c} \subseteq \bigcup_{i \in I}A_{i}^{c}
$$



and



$$
\bigcup_{i \in I}A_{i}^{c} \supseteq \left. \left( \bigcap_{i \in I}A_{i} \right) \right.^{c}
$$



Let $x \in \left. \left( \cap_{i \in I}A_{i} \right) \right.^{c}$ and show that $x \in \bigcup_{i \in I}A_{i}^{c}$. If $x \in \left. \left( \cap_{i \in I}A_{i} \right) \right.^{c}$, i.e. $x \notin \left. \left( \cap_{i \in I}A_{i} \right) \right.$, then there must be at least one set $A_{i}$ that does not contain $x$ (if all $A_{i}$ would contain $x$, then $x$ would be in the intersection as well). Call this set $A$. Since $x \notin A$, then $x \in A^{c}$. But then, $x$ is also in the union of all complements of $A_{i}$ since $A$ is one of these sets, i.e. $x \in A^{c} \subseteq \bigcup_{i \in I}A_{i}^{c}$.

Now, let $x \in \bigcup_{i \in I}A_{i}^{c}$ and show that $x \in \left. \left( \bigcup_{(i \in I)}A_{i} \right) \right.^{c}$. Then, there must be one such $A_{i}^{c}$ that contains $x$, or one such $A_{i}$ that does not contain $x$. But then $x$ is not in the intersection of all $A_{i}$, i.e. $x \notin \left. \left( \bigcap_{i \in I}A_{i} \right) \right.$ and thus, $x \in \left. \left( \bigcap_{i \in I}A_{i} \right) \right.^{c}$.

## Exercise 2.4

### (i)

> Find examples showing that $f\left. (A \cap B) \right. \neq f\left. (A) \right. \cap f\left. (B) \right.$ and $f\left. (A\backslash B) \right. \neq f\left. (A) \right.\backslash f\left. (B) \right.$. In both relations one inclusion \"$\subseteq$\" or \"$\supseteq$\" is always true. Which one?

### (ii)

> Prove (2.6).

## Exercise 2.5

The [indicator_function](/notes/areas/mathematics/definitions_theorems/measure_theory/indicator_function/) of a set $A \subseteq X$ is defined by



$$
\mathbb{1}_{A}\left. (x) \right. ≔ \begin{cases}
1 & \mathrm{\text{if }}x \in A \\
0 & \mathrm{\text{if }}x \notin A
\end{cases}
$$



Check that for $A,B,A_{i} \subseteq X,i \in I$ (arbitrary index_set) the following equalities hold:

### (i)

> 

$$
\mathbb{1}_{A \cap B} = \mathbb{1}_{A}\mathbb{1}_{B}
$$



We have that



$$
\begin{aligned}
\mathbb{1}_{A \cap B}\left. (x) \right. = 1 & \Leftrightarrow x \in A \cap B \\
 & \Leftrightarrow x \in A,x \in B \\
 & \Leftrightarrow \mathbb{1}_{A}\left. (x) \right. = 1 = \mathbb{1}_{B}\left. (x) \right. \\
 & \Leftrightarrow \mathbb{1}_{A}\left. (x) \right.\mathbb{1}_{B}\left. (x) \right. = 1
\end{aligned}
$$



### (ii)

> 

$$
\mathbb{1}_{A \cup B} = \min\{\mathbb{1}_{A} + \mathbb{1}_{B},1\}
$$





$$
\begin{aligned}
\mathbb{1}_{A \cup B}\left. (x) \right. = 1 & \Leftrightarrow x \in A \cup B \\
 & \Leftrightarrow x \in A\mathrm{\text{ or }}x \in B \\
 & \Leftrightarrow \mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right. \geq 1 \\
 & \Leftrightarrow \min\{\mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right.\} = 1
\end{aligned}
$$



In the second line above, $x \in A\mathrm{\text{ or }}x \in B$ means that $\mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right.$ is at least 1, but $x$ could potentially be in both $A$ and $B$, thus $\mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right.$ could potentially equal 2.

### (iii)

> 

$$
\mathbb{1}_{A\backslash B} = \mathbb{1}_{A} - \mathbb{1}_{A \cap B}
$$



Since $A = \left. (A \cap B) \right. \sqcup \left. (A\backslash B) \right.$ (where $\sqcup$ denotes the union of disjoint sets), we see that $\mathbb{1}_{A \cap B} + \mathbb{1}_{A\backslash B}$ can never equal 2 ()\*), thus part (ii) implies that



$$
\begin{aligned}
\mathbb{1}_{A}\left. (x) \right. & = \mathbb{1}_{A \cap B}\left. (x) \right. + \mathbb{1}_{A\backslash B}\left. (x) \right. \\
 & = \min\{\mathbb{1}_{A \cap B}\left. (x) \right. + \mathbb{1}_{A\backslash B}\left. (x) \right.,1\} \\
 & = \mathbb{1}_{A \cap B}\left. (x) \right. + \mathbb{1}_{A\backslash B}\left. (x) \right.
\end{aligned}
$$



and all we have to do is subtract $\mathbb{1}_{A \cap B}\left. (x) \right.$ from both sides of the equation.

()\*): Note that if the below function equals 1



$$
\mathbb{1}_{A \cap B}\left. (x) \right. ≔ \begin{cases}
1 & \mathrm{\text{if }}x \in A \cap B \\
0 & \mathrm{\text{if }}x \notin A
\end{cases}
$$



then it immediately follows that



$$
\mathbb{1}_{A\backslash B}\left. (x) \right. ≔ \begin{cases}
1 & \mathrm{\text{if }}x \in A\backslash B \\
0 & \mathrm{\text{if }}x \notin A
\end{cases}
$$



is equal to 0, and vice versa. Again, this is because $A \cap B$ and $A\backslash B$ are disjoint.

### (iv)

> 

$$
\mathbb{1}_{A \cup B} = \mathbb{1}_{A} + \mathbb{1}_{B} - \mathbb{1}_{A \cap B}
$$



With the same argument that we use in (iii) and with the result of (iii), we get



$$
\begin{aligned}
\mathbb{1}_{A \cup B}\left. (x) \right. & = \mathbb{1}_{\left. (A\backslash B) \right. \sqcup \left. (A \cap B) \right. \sqcup \left. (B\backslash A) \right.}\left. (x) \right. \\
 & = \mathbb{1}_{A\backslash B}\left. (x) \right. + \mathbb{1}_{\left. (A \cap B) \right.}\left. (x) \right. + \mathbb{1}_{\left. (B\backslash A) \right.}\left. (x) \right. \\
 & = \mathbb{1}_{A}\left. (x) \right. - \mathbb{1}_{A \cap B}\left. (x) \right. + \mathbb{1}_{A \cap B}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right. - \mathbb{1}_{B \cap A}\left. (x) \right. \\
 & = \mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right. - \mathbb{1}_{A \cap B}\left. (x) \right.
\end{aligned}
$$



### (v)

> 

$$
\mathbb{1}_{A \cup B} = \max\{\mathbb{1}_{A},\mathbb{1}_{B}\}
$$



From part (ii), we have that $\mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right. \geq 1$, thus $\mathbb{1}_{A}\left. (x) \right. = 1 - \mathbb{1}_{B}\left. (x) \right.$ or $\mathbb{1}_{B}\left. (x) \right. = 1 - \mathbb{1}_{A}\left. (x) \right.$. Thus, $\max\{\mathbb{1}_{A},\mathbb{1}_{B}\} = 1$.

### (vi)

> 

$$
\mathbb{1}_{A \cap B} = \min\{\mathbb{1}_{A},\mathbb{1}_{B}\}
$$



From part (i) we have that, $\mathbb{1}_{A}\left. (x) \right. = 1 = \mathbb{1}_{B}\left. (x) \right.$, thus $\min\{\mathbb{1}_{A},\mathbb{1}_{B}\} = 1$.

### (vii)

> 

$$
\mathbb{1}_{\bigcup_{(i \in I)}A_{i}} = \sup\limits_{i \in I}\mathbb{1}_{A_{i}}
$$



### (viii)

> 

$$
\mathbb{1}_{\bigcap_{i \in I}A_{i}} = \inf\limits_{i \in I}\mathbb{1}_{A_{i}}
$$



## Exercise 2.6

> Let $A,B,C \subseteq X$ and denoate by $A \bigtriangleup B$ the [symmetric_difference](/notes/areas/mathematics/definitions_theorems/set_theory/symmetric_difference/) as shown in Problem
>
> 2.  [Hint: use [indicator_function](/notes/areas/mathematics/definitions_theorems/measure_theory/indicator_function/)s for (ii) and (iii).] Show that

Again, $A \bigtriangleup B = \left. (A\backslash B) \right. \cup \left. (B\backslash A) \right.$.

### (i)

> 

$$
\mathbb{1}_{A \bigtriangleup B} = \mathbb{1}_{A} + \mathbb{1}_{B} - 2\mathbb{1}_{A}\mathbb{1}_{B} = \left| \mathbb{1}_{A} - \mathbb{1}_{B} \right| = \mathbb{1}_{A} + \mathbb{1}_{B}\operatorname{mod}\: 2
$$



Using 2.5 (iii) and (iv), we see that



$$
\begin{aligned}
\mathbb{1}_{A \bigtriangleup B} & = \mathbb{1}_{\left. (A\backslash B) \right. \sqcup \left. (B\backslash A) \right.}\left. (x) \right. \\
 & = \mathbb{1}_{A\backslash B}\left. (x) \right. + \mathbb{1}_{\left. (B\backslash A) \right.}\left. (x) \right. \\
 & = \mathbb{1}_{A}\left. (x) \right. - \mathbb{1}_{A \cap B}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right. - \mathbb{1}_{B \cap A}\left. (x) \right. \\
 & = \mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right. - 2\mathbb{1}_{A \cap B}\left. (x) \right.
\end{aligned}
$$



and this expression is 1, if and only if, $x$ is either in $A$ or in $B$ but not in both sets. Thus



$$
\mathbb{1}_{A \bigtriangleup B}\left. (x) \right. \Leftrightarrow \mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right. = 1 \Leftrightarrow \mathbb{1}_{A}\left. (x) \right. + \mathbb{1}_{B}\left. (x) \right.\operatorname{mod}\: 2 = 1
$$



It is also possible to show that



$$
\mathbb{1}_{A \bigtriangleup B}\left. (x) \right. = \left| \mathbb{1}_{A} - \mathbb{1}_{B} \right|
$$



This follows from



$$
\mathbb{1}_{A}\left. (x) \right. - \mathbb{1}_{B}\left. (x) \right. = \begin{cases}
0, & \mathrm{\text{if }}x \in A \cap B \\
0, & \mathrm{\text{if }}x \in A^{c} \cap B^{c} \\
1, & \mathrm{\text{if }}x \in A\backslash B \\
1, & \mathrm{\text{if }}x \in B\backslash A
\end{cases}
$$



Thus,



$$
\left| \mathbb{1}_{A}\left. (x) \right. - \mathbb{1}_{B}\left. (x) \right. \right| = 1 \Leftrightarrow x \in \left. (A\backslash B) \right. \cup \left. (B\backslash A) \right. = A \bigtriangleup B
$$



### (ii)

> 

$$
A \bigtriangleup \left. (B \bigtriangleup C) \right. = \left. (A \bigtriangleup B) \right. \bigtriangleup C
$$



From part (i), we see that



$$
\begin{aligned}
\mathbb{1}_{A \bigtriangleup \left. (B \bigtriangleup C) \right.} & = \mathbb{1}_{A} + \mathbb{1}_{B \bigtriangleup C} - 2\mathbb{1}_{A}\mathbb{1}_{B \bigtriangleup C} \\
 & = \mathbb{1}_{A} + \mathbb{1}_{B} + \mathbb{1}_{C} - 2\mathbb{1}_{B}\mathbb{1}_{C} - 2\mathbb{1}_{A}\left. \left( \mathbb{1}_{B} + \mathbb{1}_{C} - 2\mathbb{1}_{B}\mathbb{1}_{C} \right) \right. \\
 & = \mathbb{1}_{A} + \mathbb{1}_{B} + \mathbb{1}_{C} - 2\mathbb{1}_{B}\mathbb{1}_{C} - 2\mathbb{1}_{A}\mathbb{1}_{B} - 2\mathbb{1}_{A}\mathbb{1}_{C} + 4\mathbb{1}_{A}\mathbb{1}_{B}\mathbb{1}_{C}
\end{aligned}
$$



and this expression treats $A,B,C$ in a completely symmetric way, i.e.



$$
\mathbb{1}_{A \bigtriangleup \left. (B \bigtriangleup C) \right.}\left. (x) \right. = \mathbb{1}_{\left. (A \bigtriangleup B) \right. \bigtriangleup C}\left. (x) \right. =
$$



### (iii)

> $\mathcal{P}\left. (X) \right.$ is commutative ring (in the usual algebraist's sense) with "addition" $\bigtriangleup$ and "multiplication" $\cap$.

## Exercise 2.7

> Let $f:X \rightarrow Y$ be a map, $A \subseteq X$ and $B \subseteq Y$. Show that, in general
>
> 

$$
f \circ f^{- 1}\left. (B) \right. \subsetneq B\quad\mathrm{\text{and}}\quad f^{- 1}\left. (A) \right. \circ f \supsetneq A
$$



Let $f:X \rightarrow Y$. Then,



$$
\begin{aligned}
f\mathrm{\text{ surjective }} & \Leftrightarrow \forall B \subseteq Y:\left. \left( f \circ f^{- 1}\left. (B) \right. \right) \right. = B \\
 & \Leftrightarrow \forall B \subseteq Y:\left. \left( f \circ f^{- 1}\left. (B) \right. \right) \right. \supseteq B
\end{aligned}
$$



From: [Wikipedia: Surjective function](https://en.wikipedia.org/wiki/Surjective_function#Properties), we know that if $f:X \rightarrow Y$ is surjective and if $B$ is a subset of $Y$, then $\left. \left( f \circ f^{- 1} \right) \right.\left. (B) \right. = B$. That is, $B$ can be recovered from its [preimage](/notes/areas/mathematics/definitions_theorems/set_theory/preimage/) $f^{- 1}\left. (B) \right.$. Thus,



$$
\begin{aligned}
\left. \left( f \circ f^{- 1} \right) \right.\left. (B) \right. & = f\left. \left( f^{- 1}\left. (B) \right. \right) \right. \\
 & = f(\{ x:f\left. (x) \right. \in B\} \\
 & = \{ f\left. (x) \right.:f\left. (x) \right. \in B\} \\
 & \subseteq \{ y:y \in B\}
\end{aligned}
$$



where we have equality in the last step if and only if we can guarantee that every $y \in B$ is of the form $y = f\left. (x) \right.$ for some $x$. Since this must hjold for all sets $B$, this amounts to saying that $f\left. (X) \right. = Y$, i.e. that $f$ is surjective. The second equivalence is clear since our argument shows that the inclusion $\subseteq$ always holds.

Thus, we can construct a counterexample by setting $f:\mathbb{R} \rightarrow \mathbb{R},f\left. (x) \right. = x^{2}$ and $B = \left. \lbrack - 1,1\rbrack \right.$. Then,



$$
f^{- 1}\left. \left( \left. \lbrack - 1,1\rbrack \right. \right) \right. = \left. \lbrack 0,1\rbrack \right.
$$



and



$$
\left. \left( f \circ f^{- 1} \right) \right.\left. \left( \left. \lbrack - 1,1\rbrack \right. \right) \right. = f\left. \left( \left. \lbrack 0,1\rbrack \right. \right) \right. = \left. \lbrack 0,1\rbrack \right. = \left. \lbrack 0,1\rbrack \right. \nsubseteq \left. \lbrack - 1,1\rbrack \right.
$$



On the other hand...

## Exercise 2.8

> Let $f$ and $g$ be two injective maps. Show that $f \circ g$, if it exists, is injective.

Assume that for $x,y$ we have $\left. (f \circ g) \right.\left. (x) \right. = \left. (f \circ g) \right.\left. (y) \right.$. Since $f$ is injective, we conclude that



$$
f\left. \left( g\left. (x) \right. \right) \right. = f\left. \left( g\left. (y) \right. \right) \right. \Rightarrow g\left. (x) \right. = g\left. (y) \right.
$$



and, since $g$ is also injective,



$$
g\left. (x) \right. = g\left. (y) \right. \Rightarrow x = y
$$



showing that $f \circ g$ is injective.

## Exercise 2.9

> Show that the following sets have the same [cardinality](/notes/areas/mathematics/definitions_theorems/set_theory/cardinality/) as $\mathbb{N}$: $\{ m \in \mathbb{N}:m\mathrm{\text{ is odd}}\},\mathbb{N} \times \mathbb{Z},\mathbb{Q}^{m}\left. \left( m \in \mathbb{N} \right) \right.,\bigcup_{m \in \mathbb{N}}\mathbb{Q}^{m}$.

Part 1: Call the set of odd numbers $\mathcal{O}$. Every odd number is of the form $2k - 1$ where $k \in \mathbb{N}$. We are done, if we can show that the map $f:\mathbb{N} \rightarrow \mathcal{O},k \mapsto 2k - 1$ is bijective. surjectivity is clear as $f\left. \left( \mathbb{N} \right) \right. = \mathcal{O}$. For injectivity, we take $i,j \in \mathbb{N}$ such that $f\left. (i) \right. = f\left. (j) \right.$. The latter means that $2i - 1 = 2j - 1$, so $i = j$, i.e. injectivity.

# Chapter 3: [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/)s -- Exercises

## Exercise 3.1

> Let $\mathcal{A}$ be a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/). Show that

### (i)

> if $A_{1},A_{2},\ldots,A_{N} \in \mathcal{A}$, then $A_{1} \cap A_{2}\cdots A_{N} \in \mathcal{A}$;

This was shown in Properties 3.2 part (iii).

### (ii)

> $A \in \mathcal{A}$ if and only if $A^{c} \in \mathcal{A}$, i.e. $A \in \mathcal{A} \Leftrightarrow A^{c} \in \mathcal{A}$;

$\left. ( \Rightarrow ) \right.$: $A \in \mathcal{A} \Longrightarrow A^{c} \in \mathcal{A}$: This is by definition.

$\left. ( \Leftarrow ) \right.$: Substitute $A$ with $A^{c}$. Now, $A^{c} \in \mathcal{A} \Longrightarrow \left. \left( A^{c} \right) \right.^{c} \in \mathcal{A}$, which is the same as $A^{c} \in \mathcal{A} \Longrightarrow A \in \mathcal{A}$. $▫$

### (iii)

> if $A,B \in \mathcal{A}$, then $A\backslash B \in \mathcal{A}$ and $A \bigtriangleup B \in \mathcal{A}$.

By definition, since $A,B \in \mathcal{A}$, we know that $A^{c},B^{c} \in \mathcal{A}$ as well. By Exercise 2.1(i), $A\backslash B = A \cap B^{c}$, and by Exercise 3.1(i), we know that $A \cap B^{c} \in \mathcal{A}$. Using similar logic, $A \bigtriangleup B = \left. (A\backslash B) \right. \cup \left. (B\backslash A) \right. \in \mathcal{A}$.

## Exercise 3.2

> Prove the assertions made in Example 3.3(iv), (vi), and (vii). [Hint: use (2.6) for (vii).]

Restating 3.3(iv):

> $\{\varnothing,B,X\}$ is not a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) (unless $B = \varnothing$ or $B = X$).

Proof: By definition of a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/), this must be true. If $B \in \mathcal{A}$, then $B^{c} \in \mathcal{A}$ as well. If $B = \varnothing$ or $B = X$, then we have the minimal [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) in 3.3(ii). $▫$

Restating 3.3(vi):

> Trace of [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/): Let $E \subseteq X$ be any set and let $\mathcal{A}$ be some [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) in $X$. Then
>
> 

$$
\mathcal{A}_{E} ≔ E \cap \mathcal{A} ≔ \{ E \cap A:A \in \mathcal{A\rbrack}\}
$$


>
> is a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) in $E$.

Proof:

()$\Sigma_{1}$) Clearly, $\varnothing = E \cap \varnothing \in \mathcal{A}_{E}$.

()$\Sigma_{2}$) If $B \in \mathcal{A}$, then $B = E \cap A$ for some (not all) $A \in \mathcal{A}$, and the complement of $B$ relative to $E$ is $E\backslash B = E \cap B^{c} = E \cap \left. \left( E^{c} \cap A^{c} \right) \right. = E \cap A^{c} \in \mathcal{A}_{E}$ as $A^{c} \in \mathcal{A}$.

()$\Sigma_{3}$) Finally, let $\left. \left( B_{j} \right) \right._{j \in \mathbb{N}} \subseteq \mathcal{E}$. Then there are $\left. \left( A_{j} \right) \right._{j \in \mathbb{N}} \in \mathcal{A}$ such that $B_{j} = E \cap A_{j}$. Since $A = \bigcup_{j \in \mathbb{N}}A_{j} \in \mathcal{A}$, we get $\bigcup_{j \in \mathbb{N}}B_{j} = \bigcup_{j \in \mathbb{N}}\left. \left( E \cap A_{j} \right) \right. = E \cap \bigcup_{j \in \mathbb{N}}A_{j} = E \cap A \in \mathcal{A}_{E}$.

Restating 3.3(vii):

> Pre-image of [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/): Let $f:X \rightarrow X'$ be a map and let $\mathcal{A}'$ be a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) in $X'$. Then
>
> 

$$
\mathcal{A} ≔ f^{- 1}\left. \left( \mathcal{A}' \right) \right. ≔ \{ f^{- 1}\left. (A') \right.:A' \in \mathcal{A}'\}
$$



Note that $f^{- 1}$ interchanges with all set operations. Let $A,A_{j},j \in \mathbb{N}$ be sets in $\mathcal{A}$. We know then that $A = f^{- 1}\left. (A') \right.,A_{j} = f^{- 1}\left. \left( A_{j}' \right) \right.$ for suitable $A,A_{j}' \in \mathcal{A}'$. Since $\mathcal{A}'$ is, by assumption, a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/), we have

()$\Sigma_{1}$): $\varnothing = f^{- 1}\left. (\varnothing) \right. \in \mathcal{A}$, as $\varnothing \in \mathcal{A}'$

()$\Sigma_{2}$): $A^{c} = \left. \left( f^{- 1}\left. (A') \right. \right) \right.^{c} = f^{- 1}\left. \left( A'^{c} \right) \right. \in \mathcal{A}$ as $A'^{c} \in \mathcal{A}'$

()$\Sigma_{3}$): $\bigcup_{j \in \mathbb{N}}A_{j} = \bigcup_{j \in \mathbb{N}}f^{- 1}\left. \left( A_{j}' \right) \right. = f^{- 1}\left. \left( \bigcup_{j \in \mathbb{N}}A_{j}' \right) \right. \in \mathcal{A}$ as $\bigcup_{j \in \mathbb{N}}A_{j}' \in \mathcal{A}'$.

## Exercise 3.3

> Let $X = \mathbb{R}$. Find the [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) generated by the singletons $\{\{ x\}:x \in \mathbb{R}\}$.

See [here](https://math.stackexchange.com/questions/1476323/the-sigma-algebra-on-mathbbr-generated-by-the-collection-of-all-one-poin) and [here](https://math.stackexchange.com/questions/1670611/sigma-algebra-containing-all-singletons) and [here](https://math.stackexchange.com/questions/932535/describe-the-sigma-algebra-generated-by-singleton-subsets) [here](https://math.stackexchange.com/questions/2954720/sigma-algebra-generated-by-singletons-of-x).

Let $\mathcal{A} ≔ \{ A \subseteq X:\# A \leq \#\mathbb{N}\mathrm{\text{ or }}\# A^{c} \leq \#\mathbb{N}\}$ be a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/), as in Example 3.3(v).

()$\subseteq$): By definition of a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/), $\{ x\} \in \mathcal{A}$. Thus, by Remark 3.5, $\{ x\} \subseteq \mathcal{A}$ implies that $\sigma\left. \left( \{ x\} \right) \right. \subseteq \mathcal{A}$.

()$\supseteq$): If $\{ x\} \in \mathcal{A}$, then by definition, either $A$ or $A^{c}$ is countable. Without loss of generality, assume that $A$ is countable. Then $A$ is a countable union of singletons, and so $A \in \sigma\left. \left( \{ x\} \right) \right.$ and $A^{c} \in \sigma\left. \left( \{ x\} \right) \right.$. This means that $\sigma\left. \left( \{ x\} \right) \right. \supseteq \mathcal{A}$.

## Exercise 3.4

> Verify the assertions made in Remark 3.5.

Restating remark 3.5:

1.  If $\mathcal{G}$ is a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/), then $\mathcal{G} = \sigma\left. \left( \mathcal{G} \right) \right.$.

2.  For $A \subseteq X$ we have $\sigma\left. \left( \{ A\} \right) \right. = \{\varnothing,A,A^{c},X\}$.

3.  If $\mathcal{F} \subseteq \mathcal{G} \subseteq \mathcal{A}$, then $\sigma\left. \left( \mathcal{F} \right) \right. \subseteq \sigma\left. \left( \mathcal{G} \right) \right. \subseteq \sigma\left. \left( \mathcal{A} \right) \right. =^{\mathrm{3.5(i)}}\mathcal{A}$.

Proof:

\(i\) Since $\mathcal{G}$ is a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/), $\mathcal{G}$ "competes" in the intersection of all [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/)s $\mathcal{C} \supseteq \mathcal{G}$ appearing in the definition of $\mathcal{A}$ in the proof of Theorem 3.4(ii). Thus, $\mathcal{G} \supseteq \sigma\left. \left( \mathcal{G} \right) \right.$ while $\mathcal{G} \subseteq \sigma\left. \left( \mathcal{G} \right) \right.$ is always true.

\(ii\) Without loss of generality, we can assume that $\varnothing \neq A \neq X$ since this would simplify the problem. Clearly, $\{\varnothing,A,A^{c},X\}$is a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) containing $A$ and no element can be removed without losing this property. Thus, $\{ 0,A,A^{c},X\}$ is minimal and therefore $\sigma\left. \left( \{ A\} \right) \right.$.

\(iii\) Assume that $\mathcal{F} \subseteq \mathcal{G}$. Then we have $\mathcal{F} \subseteq \mathcal{G} \subseteq \sigma\left. \left( \mathcal{G} \right) \right.$. Now, $\mathcal{C} ≔ \sigma\left. \left( \mathcal{G} \right) \right.$ is a potential "competitor" in the intersection appearing in the proof of Theorem 3.4(ii), and as such $\mathcal{C} \supseteq \sigma\left. \left( \mathcal{F} \right) \right.$, i.e. $\sigma\left. \left( \mathcal{G} \right) \right. \supseteq \sigma\left. \left( \mathcal{F} \right) \right.$.

## Exercise 3.5

> Let $X = \left. \lbrack 0,1\rbrack \right.$. Find the [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) generated by the sets

### (i)

> $\left. \left( 0,\frac{1}{2} \right) \right.$

We are given that $G = \left. \left( 0,\frac{1}{2} \right) \right. \subseteq X$. Now, $G^{c} = \left. \left( 0,\frac{1}{2} \right) \right.^{c} = \{ 0\} \cup \left. \left\lbrack \frac{1}{2},1 \right\rbrack \right.$ and $G \cup G^{C} = \left. \lbrack 0,1\rbrack \right.$. So we have that $\sigma\left. (G) \right. = \{\varnothing,G,G^{c},X\} = \{\varnothing,\left. \left( 0,\frac{1}{2} \right) \right.,0 \cup \left. \left\lbrack \frac{1}{2},1 \right\rbrack \right.,\left. \lbrack 0,1\rbrack \right.\}$.

### (ii)

Check for accuracy converting from tex to typ:

> $\left. \left( 0,\frac{1}{4} \right) \right.,\left. \left( \frac{3}{4},1 \right) \right.$

Let $A = \left. \left( 0,\frac{1}{4} \right) \right.,B = \left. \left( \frac{3}{4},1 \right) \right.$. Now, $A^{c} = \left. \left( \frac{1}{4},1 \right) \right.,B^{c} = \left. \left( 0,\frac{3}{4} \right) \right.,A \cup B = \left. \left( 0,\frac{1}{4} \right) \right. \cup \left. \left( \frac{3}{4},1 \right) \right.,\left. (A \cup B) \right.^{c} = \left. \left\lbrack \frac{1}{4},\frac{3}{4} \right\rbrack \right.$.

So we have $\sigma\left. \left( \{ A,B\} \right) \right. = \{\varnothing,A,B,A^{c},B^{c},A \cup B,\left. (A \cup B) \right.^{c},X\} = \{\varnothing,\left. \left( 0,\frac{1}{4} \right) \right.,\left. \left( \frac{3}{4},1 \right) \right.,\left. \left\lbrack \frac{1}{4},1 \right\rbrack \right.,\left. \left\lbrack 0,\frac{3}{4} \right\rbrack \right.,\left. \left\lbrack 0,\frac{1}{4} \right\rbrack \right. \cup \lbrack\left\lbrack \frac{3}{4},1 \right\rbrack),\left. \left\lbrack \frac{1}{4},\frac{3}{4} \right\rbrack \right.,\left. \lbrack 0,1\rbrack \right.\}$

### (iii)

Check for accuracy converting from tex to typ:

> $\left. \left( 0,\frac{1}{4} \right) \right.,\left. \left( \frac{3}{4},1 \right) \right.$

This has the same answer as (ii).

## Exercise 3.6

> Let $A_{1},A_{2},...,A_{N}$ be non-empty subsets of $X$.

### (i)

> If the $A_{n}$ are disjoint and $\sqcup A_{n} = X$, then $\#\sigma\left. \left( A_{1},A_{2},...,A_{N} \right) \right. = \#\sigma\left. \left( A_{1} \right) \right.\#\sigma\left. \left( A_{2} \right) \right.\#\sigma\left. \left( A_{3} \right) \right....\#\sigma\left. \left( A_{N} \right) \right. = 2^{N}$.
>
> Remark: A set $A$ in a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) $\mathcal{A}$ is called an *atom* if there is no proper subset $\varnothing \neq B \subset A$ such that $B \in \mathcal{A}$. In this sense all $A_{n}$ are all atoms.

### (ii)

> Show that $\sigma\left. \left( A_{1},A_{2},\ldots,A_{N} \right) \right.$ consists of finitely many sets.
>
> [Hint: show that $\sigma\left. \left( A_{1},A_{2},\cdots,A_{N} \right) \right.$ has only finitely many atoms.]

# Chapter 4: Measures -- Exercises

## Exercise 4.2

> Check that the [set_function](/notes/areas/mathematics/definitions_theorems/set_theory/set_function/)s defined in Example 4.5 are [measure](/notes/areas/mathematics/definitions_theorems/measure_theory/measure/)s.

### (i)

> [Dirac_measure](/notes/areas/mathematics/definitions_theorems/measure_theory/dirac_measure/), unit mass: Let $\left. \left( X,\mathcal{A} \right) \right.$ be a [measurable_space](/notes/areas/mathematics/definitions_theorems/measure_theory/measurable_space/) and let $x \in X$ be some point. Then $\delta_{x}:\mathcal{A} \rightarrow \{ 0,1\}$, defined for $A \in \mathcal{A}$ by
>
> 

$$
\delta_{x}\left. (A) \right. = \begin{cases}
0 & \mathrm{\text{if }}x \notin A \\
1 & \mathrm{\text{if }}x \in A
\end{cases}
$$



Checking the conditions for a measure, we have:

(M${}_{0}$): That $\mathcal{A}$ is a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) is given.

(M${}_{1}$): Since $\varnothing$ contains no points, $x \notin \varnothing$ and so $\delta_{x}\left. (\varnothing) \right. = 0$.

(M${}_{2}$): Let $\left. \left( A_{j} \right) \right._{j \in \mathbb{N}} \subseteq \mathcal{A}$ be a sequence of pairwise disjoint [measurable sets](/notes/areas/mathematics/definitions_theorems/measure_theory/measure/). If $x \in \bigcup_{j \in \mathbb{N}}A_{j}$, $j_{0}$ with $x \in A_{j_{0}}$, i.e. that there is exactly one such set (and no more, since all sets that we are considering are pairwise disjoint) that contains $x$. Hence,



$$
\begin{aligned}
\delta_{x}\left. \left( \bigcup_{j \in \mathbb{N}}A_{j} \right) \right. & = 1 = 1 + 0 + 0 + \cdots \\
 & = \delta_{x}\left. \left( A_{j_{0}} \right) \right. + \sum_{j \neq j_{0}}\delta_{x}\left. \left( A_{j} \right) \right. \\
 & = \sum_{j \in \mathbb{N}}\delta_{x}\left. \left( A_{j} \right) \right.
\end{aligned}
$$



On the other hand, if $x \notin \bigcup_{j \in \mathbb{N}}A_{j}$, then $x \notin A_{j}$ for all $j \in \mathbb{N}$, hence



$$
\begin{aligned}
\delta_{x}\left. \left( \bigcup_{j \in \mathbb{N}}A_{j} \right) \right. & = 0 = 0 + 0 + 0 + \cdots \\
 & = \sum_{j \in \mathbb{N}}\delta_{x}\left. \left( A_{j} \right) \right.
\end{aligned}
$$



### (iii)

> Counting measure: Let $\left. \left( X,\mathcal{A} \right) \right.$ be a [measurable_space](/notes/areas/mathematics/definitions_theorems/measure_theory/measurable_space/) and $A \in \mathcal{A}$. Then
>
> 

$$
|A| = \begin{cases}
\# A & \mathrm{\text{if }}A\mathrm{\text{ is finite}} \\
\infty & \mathrm{\text{if }}A\mathrm{\text{ is infinite}}
\end{cases}
$$



(M${}_{0}$): That $\mathcal{A}$ is a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) is given.

(M${}_{1}$): Since $\varnothing$ contains no elements, applying the above [set_function](/notes/areas/mathematics/definitions_theorems/set_theory/set_function/) gives $|\varnothing| = \#\varnothing = 0$.

(M${}_{2}$): Let $\left. \left( A_{j} \right) \right._{j \in \mathbb{N}}$ be a sequence of pairwise disjoint sets in $\mathcal{A}$. We have three cases:

Case 1: All sets in $\left. \left( A_{j} \right) \right._{j \in \mathbb{N}}$ are infinite and only finitely many, say the first $k$, are non-empty, then $A = \bigcup_{j \in \mathbb{N}}A_{j}$ is effectively a finite union of $k$ finite sets and it is clear that



$$
|A| = \left| A_{1} \right| + \left| A_{2} \right| + \cdots + \left| A_{k} \right| + |\varnothing| + |\varnothing| + \cdots + |\varnothing| = \sum_{j \in \mathbb{N}}\left| A_{j} \right|
$$



Case 2: All $A_{j}$ are finite and infinitely many are non-empty. Then their union $A = \bigcup_{j \in \mathbb{N}}A_{j}$ is an infinite set and we have



$$
|A| = \infty = \sum_{j \in \mathbb{N}}\left| A_{j} \right|
$$



Case 3: At least one $A_{j}$ is infinite and so then is the union $A = \bigcup_{j \in \mathbb{N}}A_{j}$. Thus



$$
|A| = \infty = \sum_{j \in \mathbb{N}}\left| A_{j} \right|
$$



### (iv)

> Discrete [probability_measure](/notes/areas/mathematics/definitions_theorems/measure_theory/probability_measure/): Let $\Omega = \{\omega_{1},\omega_{2},\ldots\}$ be a [countable](/notes/areas/mathematics/definitions_theorems/set_theory/countable/) set and $\left. \left( p_{n} \right) \right._{n \in \mathbb{N}}$ be a sequence of real numbers $p_{n} \in \left. \lbrack 0,1\rbrack \right.$ such that $\sum_{n \in \mathbb{N}}p_{n} = 1$. On $\left. \left( \Omega,\mathcal{P}\left. (\Omega) \right. \right) \right.$ the [set_function](/notes/areas/mathematics/definitions_theorems/set_theory/set_function/)
>
> 

$$
P\left. (A) \right. = \sum_{n:\omega_{n} \in A}p_{n} = \sum_{n \in \mathbb{N}}p_{n}\delta_{\omega_{n}}\left. (A) \right.,\quad A \subseteq \Omega
$$


>
> defines a [probability_measure](/notes/areas/mathematics/definitions_theorems/measure_theory/probability_measure/). The triplet $\left. \left( \Omega,\mathcal{P}\left. (\Omega) \right.,P \right) \right.$ is called a discrete [probability_space](/notes/areas/mathematics/definitions_theorems/measure_theory/probability_space/).

(M${}_{0}$): That $\mathcal{P}\left. (\Omega) \right.$ is a [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) is given.

(M${}_{1}$): Since the empty set contains no elements, $P\left. (\varnothing) \right. = \sum_{n:\omega_{n} \in \varnothing}p_{n} = \sum_{n \in \mathbb{N}}p_{n}\delta_{\omega_{n}}\left. (A) \right.$, where $\delta$ is the [Dirac_measure](/notes/areas/mathematics/definitions_theorems/measure_theory/dirac_measure/) from part (i). Since the [Dirac_measure](/notes/areas/mathematics/definitions_theorems/measure_theory/dirac_measure/) is defined as



$$
\delta_{\omega_{n}}\left. (A) \right. = \begin{cases}
0 & \mathrm{\text{if }}x \notin \omega_{n} \\
1 & \mathrm{\text{if }}x \in \omega_{n}
\end{cases}
$$



it will always be zero since $\omega_{n} \notin \varnothing$. Thus, $P\left. (\varnothing) \right. = 0$.

(M${}_{2}$): Let $\left. \left( A_{k} \right) \right._{k \in \mathbb{N}}$ be pairwise disjoint subsets of $\Omega$. Then



$$
\begin{aligned}
\sum_{k \in \mathbb{N}}P\left. \left( A_{k} \right) \right. & = \sum_{k \in \mathbb{N}}\sum_{j \in \mathbb{N}}p_{j}\delta_{\omega_{j}}\left. \left( A_{k} \right) \right. \\
 & = \sum_{j \in \mathbb{N}}\sum_{k \in \mathbb{N}}p_{j}\delta_{\omega_{j}}\left. \left( A_{k} \right) \right.\quad\mathrm{\text{(justify the re-ordering of indices)}} \\
 & = \sum_{j \in \mathbb{N}}p_{j}\left. \left( \sum_{k \in \mathbb{N}}\delta_{\omega_{j}}\left. \left( A_{k} \right) \right. \right) \right. \\
 & = \sum_{j \in \mathbb{N}}p_{j}\delta_{\omega_{j}}\left. \left( \cup_{k \in \mathbb{N}}A_{k} \right) \right. \\
 & = P\left. \left( \cup_{k \in \mathbb{N}}A_{k} \right) \right.
\end{aligned}
$$



### (v)

> Trivial measures: Let $\left. \left( X,\mathcal{A} \right) \right.$ be a [measurable_space](/notes/areas/mathematics/definitions_theorems/measure_theory/measurable_space/) and $A \in \mathcal{A}$. Then
>
> 

$$
\mu\left. (A) \right. = \begin{cases}
0 & \mathrm{\text{if }}A = \varnothing \\
\infty & \mathrm{\text{if }}A \neq \varnothing
\end{cases}
$$


>
> and also $\mu\left. (A) \right. = 0$.

(M${}_{1}$): By definition of $\mu$, $\mu\left. (\varnothing) \right. = 0$.

(M${}_{2}$): Let $\left. \left( A_{j} \right) \right._{j \in \mathbb{N}}$ be pairwise disjoint sets in $\mathcal{A}$. Then



$$
\mu\left. \left( \bigcup_{j \in \mathbb{N}}A_{j} \right) \right. = \infty + \infty + \cdots = \sum_{j \in \mathbb{N}}\mu\left. \left( A_{j} \right) \right.
$$



# Chapter 5: Uniqueness of Measures -- Exercises

## Exercise 5.1

> Verify the claims made in Remark 5.2.

Restating Remark 5.2:

> As for [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/)s, see Properties 3.2, one sees that $\varnothing \in \mathcal{D}$ and that finite disjoint unions are again in $\mathcal{D}:D,E \in \mathcal{D},D \cap E = \varnothing \Longrightarrow D \sqcup E \in \mathcal{D}$. Of course, every [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) is a [Dynkin_system](/notes/areas/mathematics/definitions_theorems/measure_theory/dynkin_system/), but the converse is, in general, wrong.

By definition, $X \in \mathcal{D}$ and, similar to [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/), complements are also in $\mathcal{D}$. So, we have that $\varnothing = X^{c} \in \mathcal{D}$. If $A,B \in \mathcal{D}$ are disjoint, we set $A_{1} = A;A_{2} = B;A_{j} = \varnothing\forall j \geq 3$. Then $\left. \left( A_{j} \right) \right._{j \in \mathbb{N}}$ is a sequence of pairwise disjoint sets, and by (D${}_{3}$) we find that



$$
A \sqcup B = \bigsqcup_{j \in \mathbb{N}}A_{j} \in \mathcal{D}
$$



Since $\left. \left( \Sigma_{1} \right) \right. =$(D${}_{1}$), $\left. \left( \Sigma_{2} \right) \right. =$(D${}_{2}$), and $\left. \left( \Sigma_{3} \right) \right. \Longrightarrow$(D${}_{3}$), it is clear that every [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/) is also a [Dynkin_system](/notes/areas/mathematics/definitions_theorems/measure_theory/dynkin_system/).

## Exercise 5.2

> The following exercise shows that [Dynkin_system](/notes/areas/mathematics/definitions_theorems/measure_theory/dynkin_system/)s and [sigma-algebra](/notes/areas/mathematics/definitions_theorems/measure_theory/sigma-algebra/)s are, in general, different. Let $X = \{ 1,2,3,\ldots,4k - 1,4k\}$ for some $k \in \mathbb{N}$. Then $\mathcal{D} = \{ A \subseteq X:\# A\mathrm{\text{ is even}}\}$.

As given, $X$ has an even number of elements. For example, for $k = 1$, we have $X = \{ 4k - 3 = 1,4k - 2 = 2,4k - 1 = 3,4k = 4\}$. Similarly, for $k = 2$, we have $X = \{ 1,2,3,4,4k - 3 = 5,4k - 2 = 6,4k - 1 = 7,4k = 8\}$. It is now obvious that if $A,B \in \mathcal{D}$ are disjoint, then $A,B$ and $A \sqcup B$ contain an even number of elements. But if $A,B$ have a non-empty intersection, and if this intersection contains an odd number of elements, then $A \cup B$ contains an odd number of elements. For example:



$$
A = \{ 1,2\} \in \mathcal{D},\quad B = \{ 2,3,4,5\} \in \mathcal{D}
$$



then



$$
A \cup B = \{ 1,2,3,4,5\} \in \mathcal{D}
$$



This means that (D${}_{3}$) holds, but $\left. \left( \Sigma_{3} \right) \right.$ fails.
