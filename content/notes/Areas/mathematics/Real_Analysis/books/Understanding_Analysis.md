---
title: "Understanding Analysis"
---

# Section 1.2 Exercises

## Exercise 1.2.1

### (a)

> Prove that $\sqrt{3}$ is irrational. Does a similar argument work to show $\sqrt{6}$ is irrational?

Proceed via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/). Suppose that there exists some rational number in the form of $\frac{p}{q}$ where $p$ and $q$ are integers such that



$$
\left. \left( \frac{p}{q} \right) \right.^{2} = 3
$$



We can assume that $p$ and $q$ are co-prime (no factors in common other than 1). Then,



$$
p^{2} = 3q^{2}
$$



From here, we can see that $p$ must be a multiple of 3. This allows us to write $p = 3r$, where $r$ is also an integer. Substituting this gives



$$
\begin{aligned}
\left. (3r) \right.^{2} & = 3q^{2} \\
9r^{2} & = 3q^{2} \\
3r^{2} & = q^{2}
\end{aligned}
$$



where the last line above implies that $q^{2}$ is divisible by 3, when it was originally assumed that $p$ and $q$ had no common factor. So, by contradiction, $\sqrt{3}$ must be irrational.

A similar argument does indeed work for $\sqrt{6}$.

### (b)

> Where does the proof of Theorem 1.1.1 break down if we try to use it to prove $\sqrt{4}$ is irrational?

Suppose there exists some rational number in the form $\frac{p}{q} = \sqrt{4}$, which implies that $\frac{p^{2}}{q^{2}} = 4$. We can assume that $p$ and $q$ are co-prime (no factors in common other than 1). Then,



$$
p^{2} = 4q^{2}
$$



Since we know that $p^{2}$ must be even, we also know that $p$ is even, so we can write $p = 2r$. Substituting this gives



$$
\begin{aligned}
\left. (2r) \right.^{2} & = q^{2} \\
r^{2} & = q^{2}
\end{aligned}
$$



But here we are stuck. In the proof that $\sqrt{2}$ is irrational, we get $2r^{2} = q^{2}$ at this step, and the 2 allows us to show that $q$ is even and we then arrive at our contradiction, which is not the case here.

Said differently, we do not know, given that $p^{2}$ is divisible by 4, that $p$ also is divisible by 4. For example, 4 divides $p^{2} = 36$ but does not divide $p = 6$.

Note that this [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/) will never hold for a number that is a perfect square. Take $\sqrt{9}$ for example. Using the above logic in the case of $p^{2} = 9q^{2}$ we do not know, given that $p^{2}$ is divisible by 9, that $p$ also is divisible by 9. For example, 9 cleanly divides $p^{2} = 36$ into 4 but does not divide $p = 6$.

## Exercise 1.2.3

> Decide which of the following represent true statements about the nature of sets. For any that are false, provide a specific example where the statement in question does not hold.

### (a)

> If $A_{1} \supseteq A_{2} \supseteq A_{3} \supseteq A_{4}\cdots$ are all sets containing an infinte number of elements, then the intersection $\bigcap_{n = 1}^{\infty}$ is infinite as well.

False. This is similar to the situation in Example 1.2.2.

### (b)

> If $A_{1} \supseteq A_{2} \supseteq A_{3} \supseteq A_{4}\cdots$ are all finite, nonempty sets of real numbers, then the intersection $\bigcap_{n = 1}^{\infty}$ is finite and non-empty.

True.

### (c)

> $A \cap \left. (B \cup C) \right. = \left. (A \cap B) \right. \cup C$

False. Let $A = \{ 1,2,3\},B = \{ 3\},C = \{ 5\}$.

Then, $A \cap \left. (B \cup C) \right. = \{ 3\}$.

Where $\left. (A \cap B) \right. \cup C = \{ 3,5\}$

### (d)

> $A \cap \left. (B \cap C) \right. = \left. (A \cap B) \right. \cap C$

True.

### (e)

> $A \cap \left. (B \cup C) \right. = \left. (A \cap B) \right. \cup \left. (A \cap C) \right.$

True.

## Exercise 1.2.5 (De Morgan's Laws)

### (a)

> If $x \in \left. (A \cap B) \right.^{c}$, explain why $x \in A^{c} \cup B^{c}$. This shows that $\left. (A \cap B) \right.^{c} \subseteq A^{c} \cup B^{c}.$

Graphically:

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/1.2.5a.png)

In words:

If $x \in \left. (A \cap B) \right.^{c}$, then $x \notin \left. (A \cap B) \right.$, which implies that $x \notin A$ or $x \notin B$. From here, it must be true that $x \in A^{c}$ or $x \in B^{c}$, rather $x \in A^{c} \cup B^{c}$.

### (b)

> Prove the reverse inclusion $\left. (A \cap B) \right.^{c} \supseteq A^{c} \cup B^{c}$, and conclude that $\left. (A \cap B) \right.^{c} = A^{c} \cup B^{c}$.

To show that $A^{c} \cup B^{c}$ is a [subset](/notes/areas/mathematics/set_theory/definitions/subset/) of $\left. (A \cap B) \right.^{c}$, first let $x \in A^{c} \cup B^{c}$, then show that $x \in \left. (A \cap B) \right.^{c}$.

If $x \in A^{c} \cup B^{c}$, then $x \in A^{c}$ *or* $x \in B^{c}$. This means that $x \notin A$ or $x \notin B$. This implies that it is not the case that ($x \in A$ and $x \in B$), which is the definition of $x \notin (A \cap B)$. Therefore, $x \in (A \cap B)^{c}$. This shows that $\left. (A \cap B) \right.^{c} \supseteq A^{c} \cup B^{c}$.

### (c)

> Show $\left. (A \cup B) \right.^{c} = A^{c} \cap B^{c}$ by demonstrating inclusion both ways.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/1.2.5c.png)

We need to show two things to demonstrate inclusion both ways:

1.  $\left. (A \cup B) \right.^{c} \supseteq A^{C} \cap B^{c}$

2.  $\left. \left( A^{c} \cap B^{c} \right) \right. \supseteq \left. (A \cup B) \right.^{c}$

Starting with part 1, we have:

Let $x \in \left. \left( A^{c} \cap B^{c} \right) \right.$ and show that $x \in \left. (A \cup B) \right.^{c}$. If $x \in \left. \left( A^{c} \cap B^{c} \right) \right.$, then $x \in A^{c}$ *and* $x \in B^{c}$. From this, we know that $x \notin A$ *and* $x \notin B$, which implies that $x \notin \left. (A \cup B) \right.$, which implies that $x \in \left. (A \cup B) \right.^{c}$.

Now for part 2:

Let $x \in \left. (A \cup B) \right.^{c}$ and show that $x \in A^{c} \cap B^{c}$. If $x \in \left. (A \cup B) \right.^{c}$, then $x \notin \left. (A \cup B) \right.$, which means that $x \notin A$ *and* $x \notin B$. Which implies that $x \in A^{c}$ *and* $x \in B^{c}$, rather $x \in \left. \left( A^{c} \cap B^{c} \right) \right.$.

## Exercise 1.2.6

### (a)

> Verify the triangle inequality in the special case where $a$ and $b$ have the same sign.

We know that $|x|$ is given by



$$
|x| = \begin{cases}
x, & x > 0 \\ - x, & x < 0
\end{cases}
$$



For the case $a,b > 0$, we know that $a + b > 0$, which implies that $|a + b| = a + b$. Also, $|a| = a$, and $|b| = b$, so $|a| + |b| = a + b$. This implies that $|a + b| = |a| + |b|$.

For the case $a,b < 0$, we know that $a + b < 0$, which implies that, given the piecewise [function](/notes/areas/mathematics/set_theory/definitions/function/) above, $|a + b| = - \left. (a + b) \right. = - a - b$. Also, $|a| = - a$ and $|b| = - b$ and $|a| + |b| = - a - b$. This implies that $|a + b| = |a| + |b|$.

### (b)

> Verify the triangle inequality in the case where $a \geq 0$ and $b < 0$.

Without loss of generality, assume $a \geq 0$ and $b < 0$. We need to show $|a + b| \leq |a| + |b|$.

Since $a \geq 0$, we have $|a| = a$. Since $b < 0$, we have $|b| = -b$.

Now consider $a + b$. There are two subcases:

**Case 1:** If $a + b \geq 0$, then $|a + b| = a + b$. We need to show $a + b \leq a + (-b) = a - b$. This simplifies to $b \leq -b$, or $2b \leq 0$, which is true since $b < 0$.

**Case 2:** If $a + b < 0$, then $|a + b| = -(a + b) = -a - b$. We need to show $-a - b \leq a + (-b) = a - b$. This simplifies to $-a \leq a$, or $0 \leq 2a$, which is true since $a \geq 0$.

In both cases, $|a + b| \leq |a| + |b|$.

### (c)

> Use (a) and (b) to give a complete proof of the triangle inequality $|a + b| \leq |a| + |b|$ for all $a, b \in \mathbb{R}$.

Given any $a, b \in \mathbb{R}$, exactly one of the following cases holds:

1. $a \geq 0$ and $b \geq 0$: By part (a), $|a + b| = |a| + |b| \leq |a| + |b|$.
2. $a \leq 0$ and $b \leq 0$: By part (a), $|a + b| = |a| + |b| \leq |a| + |b|$.
3. $a \geq 0$ and $b < 0$: By part (b), $|a + b| \leq |a| + |b|$.
4. $a < 0$ and $b \geq 0$: By symmetry (swapping $a$ and $b$ in part (b)), $|a + b| = |b + a| \leq |b| + |a| = |a| + |b|$.

Therefore, $|a + b| \leq |a| + |b|$ for all $a, b \in \mathbb{R}$.

### (d)

> Prove $\left\| \right.a| - |b\left\| \right. \leq |a - b|$. (The unremarkable identity $a = a - b + b$ may be useful.)

Given the hint $a = a - b + b$, we have



$$
\begin{aligned}
|a| & = |a - b + b| \\
 & \leq |a - b| + |b| \\
|a| - |b| & \leq |a - b| \\
|b| - |a| & \leq |b - a|
\end{aligned}
$$



Since $|a - b| = |b - a|$, the result follows.

## Exercise 1.2.7

> Given a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ and a subset $A$ of its [domain](/notes/areas/mathematics/set_theory/definitions/domain/), let $f\left. (A) \right.$ represent the [range](/notes/areas/mathematics/set_theory/definitions/range/) of $f$ over the set $A$; that is, $\{ f\left. (x) \right.:x \in A\}$.

### (a)

> Let $f\left. (x) \right. = x^{2}$. If $A = \left. \lbrack 0,2\rbrack \right.$ (the closed interval $\{ x \in \mathbb{R}:0 \leq x \leq 2\}$). and $B = \left. \lbrack 1,4\rbrack \right.$, find $f\left. (A) \right.$ and $f\left. (B) \right.$. Does $f\left. (A \cap B) \right. = f\left. (A) \right. \cap f\left. (B) \right.$ in this case? Does $f\left. (A \cap B) \right. = f\left. (A) \right. \cup f\left. (B) \right.$?

Here, $A$ is the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) and $f\left. (A) \right.$ is the [range](/notes/areas/mathematics/set_theory/definitions/range/). Similarly with $B$ and $f\left. (B) \right.$.

We are given that $f\left. (x) \right. = x^{2}$, $A = \left. \lbrack 0,2\rbrack \right.$, and $B = \left. \lbrack 1,4\rbrack \right.$.

Then,

$f\left. (A) \right. = \left. \left\lbrack 0^{2},2^{2} \right\rbrack \right. = \left. \lbrack 0,4\rbrack \right.$, and $f\left. (B) \right. = \left. \left\lbrack 1^{2},4^{2} \right\rbrack \right. = \left. \lbrack 1,16\rbrack \right.$.

$f\left. (A \cap B) \right. = f\left. \left( \left. \lbrack 0,2\rbrack \right. \cap \left. \lbrack 1,4\rbrack \right. \right) \right. = f\left. \left( \left. \lbrack 1,2\rbrack \right. \right) \right. = \left. \lbrack 1,4\rbrack \right.$.

$f\left. (A) \right. \cap f\left. (B) \right. = \left. \lbrack 0,4\rbrack \right. \cap \left. \lbrack 1,16\rbrack \right. = \left. \lbrack 1,4\rbrack \right.$.

$f\left. (A \cup B) \right. = f\left. \left( \left. \lbrack 0,2\rbrack \right. \cup \left. \lbrack 1,4\rbrack \right. \right) \right. = f\left. \left( \left. \lbrack 0,4\rbrack \right. \right) \right. = \left. \lbrack 0,16\rbrack \right.$.

$f\left. (A) \right. \cup f\left. (B) \right. = \left. \lbrack 0,2\rbrack \right. \cup \left. \lbrack 1,6\rbrack \right. = \left. \lbrack 0,16\rbrack \right.$.

### (b)

> Find two sets $A$ and $B$ for which $f\left. (A \cap B) \right. \neq f\left. (A) \right. \cap f\left. (B) \right.$.

Again, $f\left. (x) \right. = x^{2}$.

Let $A = \left. \lbrack - 1,2\rbrack \right.$ and $B = \left. \lbrack 0,1\rbrack \right.$.

Then, $f\left. (A) \right. = \left. \lbrack 1,4\rbrack \right.$, $f\left. (B) \right. = \left. \lbrack 0,1\rbrack \right.$.

And $f\left. (A) \right. \cap f\left. (B) \right. = \left. \lbrack 1,4\rbrack \right. \cap \left. \lbrack 0,1\rbrack \right. = \left. \lbrack 1\rbrack \right.$

$f\left. (A \cap B) \right. = f\left. \left( \left. \lbrack 1,4\rbrack \right. \cap \left. \lbrack 0,1\rbrack \right. \right) \right. = f\left. \left( \left. \lbrack 0,1\rbrack \right. \right) \right. = \left. \lbrack 0,1\rbrack \right.$

### (c)

> Show that, for an arbitrary [function](/notes/areas/mathematics/set_theory/definitions/function/) $g:\mathbb{R} \rightarrow \mathbb{R}$, it is always true that $g\left. (A \cap B) \right. \subseteq g\left. (A) \right. \cap g\left. (B) \right.$ for all sets $A,B \subseteq \mathbb{R}$.

We are given that $g\left. (A) \right. \cap g\left. (B) \right. \supseteq g\left. (A \cap B) \right.$, and we need to show that $y \in g\left. (A \cap B) \right.$ implies that $y \in g\left. (A) \right. \cap g\left. (B) \right.$. If $y \in g\left. (A \cap B) \right.$, then there exists an $x \in \left. (A \cap B) \right.$ such that $g\left. (x) \right. = y$. But this means that $x \in A$ *and* $x \in B$, so $g\left. (x) \right. \in g\left. (A) \right.$ *and* $g\left. (x) \right. \in g\left. (B) \right.$. Thus $g\left. (x) \right. = y \in g\left. (A) \right. \cap g\left. (B) \right.$.

### (d)

> Form and prove a conjecture about the relationship between $g\left. (A \cup B) \right.$ and $g\left. (A) \right. \cup g\left. (B) \right.$ for an arbitrary [function](/notes/areas/mathematics/set_theory/definitions/function/) $g$.

We need to show that



$$
g\left. (A \cup B) \right. = g\left. (A) \right. \cup g\left. (B) \right.
$$



That is, we need to show inclusion both ways to show equality:

1.  $g\left. (A) \right. \cup g\left. (B) \right. \supseteq g\left. (A \cup B) \right.$

2.  $g\left. (A \cup B) \right. \supseteq g\left. (A) \right. \cup g\left. (B) \right.$

Starting with 1:

Let $y \in g\left. (A \cup B) \right.$ and show that $y \in g\left. (A) \right.$ and $g\left. (B) \right.$. If $y \in g\left. (A \cup B) \right.$, then there exists an $x \in A \cup B$ such that $g\left. (x) \right. = y$. But this means that $x \in A$ *or* $x \in B$, and thus that $g\left. (x) \right. \in g\left. (A) \right.$ *or* $g\left. (x) \right. \in g\left. (B) \right.$. So, $g\left. (x) \right. = y \in g\left. (A) \right. \cup g\left. (B) \right.$.

Now for 2:

Let $y \in g\left. (A) \right. \cup g\left. (B) \right.$ and show that $g\left. (A \cup B) \right.$. If $y \in g\left. (A) \right. \cup g\left. (B) \right.$, then there exists an $x \in A$ *or* $x \in B$ such that $g\left. (x) \right. = y$. This means that $x \in A \cup B$ and thus that $g\left. (x) \right. \in g\left. (A \cup B) \right.$. So, $g\left. (x) \right. = y \in g\left. (A \cup B) \right.$.

Therefore, since we have shown 1 and 2, $g\left. (A \cup B) \right. = g\left. (A) \right. \cup g\left. (B) \right.$.

## Exercise 1.2.9

> Given a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:D \rightarrow R$ and a subset $B \subseteq \mathbb{R}$, let $f^{- 1}\left. (B) \right.$ be the set of all points from the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $D$ that get mapped into $B$; that is, $f^{- 1}\left. (B) \right. = \{ x \in D:f\left. (x) \right. \in B\}$. This set is called [preimage](/notes/areas/mathematics/set_theory/definitions/preimage/) of $B$.

### (a)

> Let $f\left. (x) \right. = x^{2}$. If $A$ is the closed interval [0, 4] and $B$ is the closed interval [-1, 1], find $f^{- 1}\left. (A) \right.$ and $f^{- 1}\left. (B) \right.$. Does $f^{- 1}\left. (A \cap B) \right. = f^{- 1}\left. (A) \right. \cap f^{- 1}\left. (B) \right.$ in this case? Does $f^{- 1}\left. (A \cup B) \right. = f^{- 1}\left. (A) \right. \cup f^{- 1}\left. (B) \right.?$

To find a [preimage](/notes/areas/mathematics/set_theory/definitions/preimage/) for $a$, we need to solve the equation $f\left. (x) \right. = a$ for $x$.

We are given that $f\left. (x) \right. = x^{2}$, so

$A = \left. \lbrack 0,4\rbrack \right.,B = \left. \lbrack - 1,1\rbrack \right.$.

Then, $f^{- 1}\left. (A) \right. = \left. \lbrack - 2,2\rbrack \right.$ (solving $x^{2} = 0$ gives $x = 0$ and solving $x^{2} = 4$ gives $x = \pm 2$)

and $f^{- 1}\left. (B) \right. = \left. \lbrack - 1,1\rbrack \right.$ (solving $x^{2} = 1$ gives $x = \pm 1$ and solving $x^{2} = - 1$ gives $x = \pm i$).

where $f:\left. \lbrack - 2,2\rbrack \right. \rightarrow \left. \lbrack 0,4\rbrack \right.$, where $\left. \lbrack - 2,2\rbrack \right.$ is the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) and $\left. \lbrack 0,4\rbrack \right.$ is the range.

To show this, plot $x^{2}$ using the following Mathematica command:

    Plot[x^2, {x, -2, 2}]

where the $x$-axis runs from -2 to 2, and so the values on the $y$-axis run from 0 to 4.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/1.2.9-1.png)

and $f:\left. \lbrack - 1,1\rbrack \right. \rightarrow \left. \lbrack 0,1\rbrack \right.$.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/1.2.9-2.png)

Now, $A \cap B = \left. \lbrack 0,1\rbrack \right.$, and so $f^{- 1}\left. (A \cap B) \right. = f^{- 1}\left. \left( \left. \lbrack 0,1\rbrack \right. \right) \right. = \left. \lbrack - 1,1\rbrack \right..$

and $f^{- 1}\left. (A) \right. \cap f^{- 1}\left. (B) \right. = \left. \lbrack - 1,1\rbrack \right.$.

Now, $A \cup B = \left. \lbrack - 1,4\rbrack \right.$

and $f^{- 1}\left. (A \cup B) \right. = \left. \lbrack - 2,2\rbrack \right.$

and $f^{- 1}\left. (A) \right. \cup f^{- 1}\left. (B) \right. = \left. \lbrack - 2,2\rbrack \right.$.

So, addressing the question "Does $f^{- 1}\left. (A \cap B) \right. = f^{- 1}\left. (A) \right. \cap f^{- 1}\left. (B) \right.$ in this case? Does $f^{- 1}\left. (A \cup B) \right. = f^{- 1}\left. (A) \right. \cup f^{- 1}\left. (B) \right.?$"...

The answer is yes in both cases.

### (b)

> The good behavior of [preimage](/notes/areas/mathematics/set_theory/definitions/preimage/)s demonstrated in (a) is completely general. Show that for an arbitrary [function](/notes/areas/mathematics/set_theory/definitions/function/) $g:\mathbb{R} \rightarrow \mathbb{R}$, it is always true that $g^{- 1}\left. (A \cap B) \right. = g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right.$ and $g^{- 1}\left. (A \cup B) \right. = g^{- 1}g^{- 1}\left. (A) \right. \cup g^{- 1}\left. (B) \right.$ for all sets $A,b \subseteq \mathbb{R}$

In the case of $g^{- 1}\left. (A \cap B) \right. = g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right.$:

### Part 1

We need to show inclusion both ways to show equality:

1.  $g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right. \supseteq g^{- 1}\left. (A \cap B) \right.$

2.  $g^{- 1}\left. (A \cap B) \right. \supseteq g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right.$

Starting with 1:

Let $x \in g^{- 1}\left. (A \cap B) \right.$ and show that $x \in g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right.$. If $x \in g^{- 1}\left. (A \cap B) \right.$, then $g\left. (x) \right. \in \left. (A \cap B) \right.$. This means that $g\left. (x) \right. \in A$ *and* $g\left. (x) \right. \in B$. By the definition of [preimage](/notes/areas/mathematics/set_theory/definitions/preimage/), $x \in g^{- 1}\left. (A) \right.$ *and* $x \in g^{- 1}\left. (B) \right.$. Therefore, $x \in g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right.$.

Now, for 2:

Let $x \in g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right.$ and show that $x \in g^{- 1}\left. (A \cap B) \right.$. If $x \in g^{- 1}\left. (A) \right. \cap g^{- 1}\left. (B) \right.$, then $g\left. (x) \right. \in A$ *and* $g\left. (x) \right. \in B$, and thus that $g\left. (x) \right. \in A \cap B$. This means that $x \in g^{- 1}\left. (A \cap B) \right.$.

### Part 2

Again, we need to show inclusion both ways to show equality:

1.  $g^{- 1}\left. (A) \right. \cup g^{- 1}\left. (B) \right. \supseteq g^{- 1}\left. (A \cup B) \right.$

2.  $g^{- 1}\left. (A \cup B) \right. \supseteq g^{- 1}\left. (A) \right. \cup g^{- 1}\left. (B) \right.$

Starting with 1:

Let $x \in g^{- 1}\left. (A \cup B) \right.$ and show that $x \in g^{- 1}\left. (A) \right. \cup g^{- 1}\left. (B) \right.$. So, if $x \in g^{- 1}\left. (A \cup B) \right.$ then $g\left. (x) \right. \in \left. (A \cup B) \right.$. But this means $g\left. (x) \right. \in A$ or $g\left. (x) \right. \in B$ which implies that $x \in g^{- 1}\left. (A) \right.$ *or* $x \in g^{- 1}\left. (B) \right.$. From this we know that $x \in g^{- 1}\left. (A) \right. \cup g^{- 1}\left. (B) \right.$.

Now, for 2:

Let $x \in g^{- 1}\left. (A) \right. \cup g^{- 1}\left. (B) \right.$ and show that $x \in g^{- 1}\left. (A \cup B) \right.$. So, if $x \in g^{- 1}\left. (A) \right. \cup g^{- 1}\left. (B) \right.$ then $x \in g^{- 1}\left. (A) \right.$ or $x \in g^{- 1}\left. (B) \right.$. This implies that $g\left. (x) \right. \in A$ *or* $g\left. (x) \right. \in B$ and hence $g\left. (x) \right. \in A \cup B$. This means that $x \in g^{- 1}\left. (A \cup B) \right.$.

## Exercise 1.2.11

> Form the logical negation of each claim. One trivial way to do this is to simply add "It is not the case that..." in front of each assertion. To make this interesting, fashion the negation into a positive statement that avoids using the word "not" altogether. In each case, make an intuitive guess as to whether the claim or its negation is the true statement.

### (a)

> For all real numbers satisfying $a < b$, there exists an $n \in \mathbb{N}$ such that $a + \frac{1}{n} < b$.

For all real numbers satisfying $a < b$, there exists an $n \in \mathbb{N}$ such that $a + \frac{1}{n} \geq b$.

### (b)

> Between every two distinct real numbers, there is a rational number.

There exist two rational numbers such that every rational number between them is irrational.

### (c)

> For all natural numbers $n \in \mathbb{N},\sqrt{n}$ is either a natural number or an irrational number.

There exists a natural number $n \in \mathbb{N}$ such that $\sqrt{n}$ is rational but not a natural number.

### (d)

> Given any real number $x \in \mathbb{R}$, there exists $n \in \mathbb{N}$ satisfying $n > x$.

There exists a real number $x$ such that $n < x$ for all $n \in \mathbb{N}$.

## Exercise 1.2.12

> Let $y_{1} = 6$, and for each $n \in \mathbb{N}$ define $y_{n + 1} = \frac{2}{3}y_{n} - 6$.

### (a)

> Use induction to prove that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) satisfies $y_{n} > - 6$ for all $n \in \mathbb{N}$.

Base step: For $n = 1$, $y_{1} = 6 > - 6$, so our base step holds.

Induction step: Assume $y_{n} > - 6$ is true, then show that $y_{n + 1} > - 6$. Starting from the induction hypothesis $y_{n} > - 6$, multiply both sides by $\frac{2}{3}$ and subtract 2:



$$
\begin{aligned}
\frac{2}{3}y_{n} - 2 & > - 6\left. \left( \frac{2}{3} \right) \right. - 2 \\
\frac{2}{3}y_{n} - 2 & > - 6
\end{aligned}
$$



which gives the desired result.

### (b)

> Use another induction argument to show that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( y_{1},y_{2},y_{3},\ldots \right) \right.$ is decreasing.

Base step: We are given that, for $n = 1$, $y_{1} = 6$. For $n = 2$, $y_{2} = \frac{2\left. (6) \right. - 6}{3} = 2$. So, $y_{1} < y_{2}$ and our base step holds.

Induction step: Show that if we have $y_{n} \leq y_{n + 1}$, then it follows that $y_{n + 1} \leq y_{n + 2}$. Starting from the induction hypothesis, again multiply both sides by $\frac{2}{3}$ and subtract 2, which gives



$$
\frac{2}{3}y_{n} - 2 \leq \frac{2}{3}y_{n + 1} - 2
$$



which is the desired result.

# Section 1.3 Exercises

## Exercise 1.3.1

### (a)

> Write a formal definition in the style of Definition 1.3.2 for the [greatest_lower_bound](/notes/areas/mathematics/real_analysis/definitions/greatest_lower_bound/) or greatest lower bound of a set.

A real number $i$ is the greatest lower bound for a set $A \subseteq \mathbb{R}$ if it meets the following criteria:

1.  $i$ is a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for $A$

2.  If $l$ is any [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for $A$, then $i \geq l$

### (b)

> Now, state and prove a version of Lemma 1.3.8 for greatest lower bounds.

Lemma: Assume $i \in \mathbb{R}$ is a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for a set $A \subseteq \mathbb{R}$. Then, $i = \inf\left. (A) \right.$ if and only if, for every choice of $\epsilon > 0$, there exists an element $a \in A$ satisfying $i + \epsilon > a$.

Proof: First, a rephrasing of the lemma: Given that $i$ is a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), $i$ is the greatest lower bound if and only if any number larger than $i$ is not a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/).

Note that, since this is an "if and only if" statement, we need to prove this in both directions.

Now to the meat of the proof:

In the forward direction ($\Rightarrow$): Assume that $i = \inf\left. (A) \right.$ and consider $i + \epsilon$ for some arbitrary $\epsilon > 0$. Since $i + \epsilon > l$ part (ii) from (a) implies that $i + \epsilon$ is not a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for $A$. If this is the case, then there must be some element $a \in A$ for which $i + \epsilon > a$ (otherwise it would be a [lower bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/)).

In the backward direction ($\Leftarrow$): Assume $i$ is a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) with the property that no matter how $\epsilon > 0$ is selected, $i + \epsilon$ is no longer a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for $A$. Notice that this implies that if $l$ is any number greater than $i$, then $i$ is not a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/). To prove that $i = \inf\left. (A) \right.$, we must verify part (ii) of (a). Because we have just argued that any number larger than $i$ cannot be a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), it follows that if $i$ is some other [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), then $i \geq l$.

## Exercise 1.3.3

### (a)

> Let $A$ be non-empty and bounded below, and define
>
> 

$$
B = \{ b \in \mathbb{R}:b\mathrm{\text{ is a lower bound for }}A\}
$$


>
> Show that $\sup B = \inf A$.

To say that $B = \{ b \in \mathbb{R}:b\mathrm{\text{ is a lower bound for }}A\}$ means that the set $B$ consists of all [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/)s for $A.$

Since $A$ is bounded below, $B$ is not empty. Also, for all $a \in A$ and $b \in B$, $b \leq a$. So, $B$ is bounded above and $\alpha = \sup\left. (B) \right.$ exists by the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/).

Now to show that $\alpha = \inf\left. (A) \right.$. By part (ii) of the definition of a [supremum](/notes/areas/mathematics/real_analysis/definitions/supremum/), $\alpha \leq a$ for all $a \in A$ and $\alpha$ is a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for $A$. Which is also a greatest lower bound since if $l$ is some arbitrary [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for $A$, then $l \in B$ and part (i) of the definition of a [supremum](/notes/areas/mathematics/real_analysis/definitions/supremum/) implies $l \leq \alpha$.

### (b)

> Use (a) to expalin why there is no need to assert that greatest lower bounds exist as part of the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/).

By part (a), we have a proof that greatest lower bounds exist as part of the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/).

## Exercise 1.3.5

> As in Example 1.3.7, let $A \subseteq \mathbb{R}$. be non-empty and bounded above, and let $c \in \mathbb{R}$. This time define the set $cA = \{ ca:a \in A\}$.

### (a)

> If $c \geq 0$, show that $\sup\left. (cA) \right. = c\sup A$

Let $s = \sup A$.

In the case that $c = 0$, $cA = \{ 0\}$. Obviously here, $\sup\left. (cA) \right. = 0$.

For $c > 0$, $cs$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $cA$. Now we have to show that if $d$ is any [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $cA$, then $cs \leq d$. We know that $ca \leq d$ for all $a \in A$, and thus $a \leq \frac{d}{c}$ for all $a \in A$. This means that $\frac{d}{c}$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$, and by Definition 1.3.2, $s \leq \frac{d}{c}$. But this implies that $cs \leq c\left. \left( \frac{d}{c} \right) \right. = d$, which is exactly what we wanted to show.

### (b)

> Postulate a similar type of statement for $\sup\left. (cA) \right.$ for the case $c < 0$.

Let $i = \inf\left. (A) \right.$.

Assuming $A$ is bounded below, let us claim that $\sup\left. (cA) \right. = ci$ for $c < 0$. To prove this claim, we must first show that $ci$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $cA$. Since $i \leq a\quad\forall a \in A$, this implies that $ci \leq ca$. This shows that $ci$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $cA$.

Next, show that if $d$ is any [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $cA$, then $ca \leq d$. We know that $ca \leq d\quad\forall a \in A$, and thus $\frac{d}{c} \leq a\quad\forall a \in A$. This means that $\frac{d}{c}$ is a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for $A$ and from Exercise 1.3.1, $\frac{d}{c} \leq i$. This implies that $ci \leq c\left. \left( \frac{d}{c} \right) \right. \leq d$, which is exactly what we wanted to show.

## Exercise 1.3.7

> Prove that if $a$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$, and if $a$ is also an element of $A$, then it must be that $a = \sup A$.

We are given that $a$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$, and that $a \in A$.

Since $a$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$, we just need to verify that part (ii) of Definition 1.3.2 holds and that if $d$ is any [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$, then $a \leq d$. By the definition of the [upper bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/), $a \leq d$ because $a$ is an element of $A$. So be Definition 1.3.2, $a = \sup A$.

## Exercise 1.3.9

### (a)

> If $\sup A < \sup B$, show that there exists an element $b \in B$ that is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$.

Let $s_{a} = \sup A$ and $s_{b} = \sup B$.

Now let $\epsilon = s_{b} - s_{a} > 0$. By Lemma 1.3.8, there exists an element $b \in B$ satisfying $s_{b} - \epsilon < b$, which implies that $s_{a} < b$. Because $s_{a}$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$, then $b$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) as well.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/1.3.9a.png)

### (b)

> Give an example to show that this is not always the case if we only assume $\sup A \leq \sup B$.

Let $A = \left. \lbrack 0,1\rbrack \right.$ and $B = \left. (0,1) \right.$.

## Exercise 1.3.11

> Decide if the following statements about suprema and infima are true or false. Give a short proof for those that are true. For any that are false, supply an example where the claim in question does not appear to hold.

### (a)

> If $A$ and $B$ are non-empty, bounded, and satisfy $A \subseteq B$, then $\sup A \leq \sup B$.

True.

Since $B \supseteq A$, all elements of $B$ are elements of $A$, thus $\sup A \leq b\quad\forall b \in B$. By Definition 1.3.2 part (ii), for some $c \in R$ that is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $B$, $b \leq c\quad\forall b \in B$. Because $\sup B$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $A$, $\sup A \leq \sup B$.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/1.3.11a.png)

### (b)

> If $\sup A < \inf B$ for sets $A$ and $B$, then there exists a $c \in \mathbb{R}$ satisfying $a < c, < b\quad\forall a \in A\mathrm{\text{ and }}\forall b \in B$.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/1.3.11b.png)

### (c)

> If there exists a $c \in \mathbb{R}$ satisfying $a < c < b\quad\forall A \in A\mathrm{\text{ and }}\forall b \in B$, then $\sup A < \inf B$.

False.

Consider the [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s $A = \left. (1,2) \right.$ and $B = \left. (2,3) \right.$. Then $a < c < b\quad\forall A \in A\mathrm{\text{ and }}\forall b \in B$, but $\sup A = c = \inf B$.

# Section 1.4 Exercises

# Exercise 1.4.1

> Recall that $\mathbb{I}$ denotes the set of irrational numbers.

## (a)

> Show that if $a,b \in Q$, then $ab$ and $a + b$ are elements of $\mathbb{Q}$ as well.

Let $a = \frac{c}{d} \in \mathbb{Q}\mathrm{\text{ where }}c,d \in \mathbb{Z}$.

Let $b = \frac{e}{f} \in \mathbb{Q}\mathrm{\text{ where }}e,f \in \mathbb{Z}$.

Then, $ab = \frac{c}{d} \times \frac{e}{f} = \frac{ce}{df} \in \mathbb{Q}$.

And $a + b = \frac{c}{d} + \frac{e}{f} = \frac{c}{d} \times \frac{f}{f} + \frac{e}{f} \times \frac{d}{d} = \frac{cf + de}{df} \in \mathbb{Q}$.

## (b)

> Show that if $a \in \mathbb{Q}$ and $t \in \mathbb{I}$, then (i) $a + t \in \mathbb{I}$ and (ii) $at \in \mathbb{I}$ as long as $a \neq 0$.

Part (i): Proceed via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/). Assume $t + a \in \mathbb{Q}$. Then $t = \left. (t + a) \right. - a$ is the difference of two rational numbers, and by part (a), $t$ must be rational as well. This contradiction (an irrational number is not equal to a rational number) implies that $a + t \in \mathbb{I}$.

Part (ii): Again via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/). Assume that $at \in \mathbb{Q}$. Then $\left. \right.\left. (at) \right.(\frac{1}{a})) = t$ would be rational by part (a). This contradiction implies that $at \in \mathbb{I}$.

## (c)

> Part (a) can be summarized by saying that $\mathbb{Q}$ is closed under addition and multiplication. Is $\mathbb{I}$ closed under addition and multiplication? Given two irrational numbers $s$ and $t$, when can we say about $s + t$ and $st$?

The set of irrationals is not closed under addition and multiplication. Given two irrationals $s$ and $t$, $s + t$ can either be irrational or rational. For example, if $s = \sqrt{2}$ and $t = - \sqrt{2}$, then $s + t = 0$ which is an element of $\mathbb{Q}$. However, if $s = \sqrt{2}$ and $t = 2\sqrt{2}$, then $s + t = \sqrt{2} + 2\sqrt{2} = 3\sqrt{3}$ which is an element of $\mathbb{I}$.

Similarly, $st$ can be either irrational or rational. If $s = \sqrt{2}$ and $t = - \sqrt{2}$, then $st = - 1$ which is rational. However, if $s = \sqrt{2}$ and $t = \sqrt{3}$, then $st = \sqrt{2}\sqrt{3} = \sqrt{6}$, which is irrational.

# Exercise 1.4.3

> Prove that $\bigcap_{n = 1}^{\infty}$ $\left. \left( 0,\frac{1}{n} \right) \right. = \varnothing$. Notice that this demonstrates that the intervals in the [Nested_Interval_Property](/notes/areas/mathematics/real_analysis/definitions/nested_interval_property/) must be closed for the conclusion of the theorem to hold.

Let $x \in \mathbb{R}$ be arbitrary. Now show that $x \in \left. \left( 0,\frac{1}{n} \right) \right.$ for some $n \in \mathbb{N}$. If $x \leq 0$ then we can take $n = 1$ for which $x \in \left. (0,1) \right.$. If $x > 0$ then by Theorem 1.4.2 ([Archimedean_Property](/notes/areas/mathematics/real_analysis/definitions/archimedean_property/)), we know that there exists some $n_{0} \in \mathbb{N}$ such that $\frac{1}{n_{0}} < x$. This means that any element of the intersection would be greater than zero, yet less than $\frac{1}{n}\quad\forall n \in \mathbb{N}$. There is no such element by Theorem 1.4.2. This implies that $x \notin \bigcap_{n = 1}^{\infty}\left. \left( 0,\frac{1}{n} \right) \right.$.

# Exercise 1.4.5

> Using Exercise 1.4.1, supply a proof for Corollary 1.4.4 by considering the real numbers $a - \sqrt{2}$ and $b - \sqrt{2}$.

It will help to restate Theorem 1.4.3 [Density_of_Q_in_R](/notes/areas/mathematics/real_analysis/definitions/density_of_q_in_r/) and Corollary 1.4.4 here:

Theorem 1.4.3 (Density of $\mathbb{Q}$ in $\mathbb{R}$): For every two real numbers $a$ and $b$, with $a < b$, there exists a rational number $r$ satisfying $a < r,b$.

Corollary 1.4.4: Given any two real numbers $a < b$, there exists an irrational number $t$ satisfying $a < t < b$.

Now to the proof:

By Theorem 1.4.3, we can find a rational number $r$ such that



$$
a - \sqrt{2} < r < b - \sqrt{2}
$$



This implies that $a < r + \sqrt{2} < b$. From Exercise 1.4.2(b), we know that $r + \sqrt{2}$ is an irrational number between $a$ and $b$.

# Exercise 1.4.7

> Finish the proof of Theorem 1.4.5 by showing that the assumption $\alpha^{2} > 2$ leads to a contradiction of the fact that $\alpha = \sup T$.

Let $\alpha = \sup T$.

Now, write



$$
\begin{aligned}
\left. \left( \alpha - \frac{1}{n} \right) \right.^{2} & = \alpha^{2} - \frac{2\alpha}{n} + \frac{1}{n^{2}} \\
 & > \alpha^{2} - \frac{2\alpha}{n}
\end{aligned}
$$



Aside: Above, set $\alpha^{2} - \frac{2\alpha}{n} = 2$ which gives



$$
\frac{1}{n_{0}} = \frac{\alpha^{2} - 2}{2\alpha}
$$



Now, choose $n_{0}$ large enough so that



$$
\frac{1}{n_{0}} < \frac{\alpha^{2} - 2}{2\alpha}
$$



This implies that $\frac{2\alpha}{n_{0}} < \alpha^{2} - 2$ and consequently that



$$
\begin{aligned}
\left. \left( \alpha - \frac{1}{n} \right) \right.^{2} & > \alpha^{2} - \left. \left( \alpha^{2} - 2 \right) \right. \\
 & = 2
\end{aligned}
$$



Thus $\left. \left( \alpha - \frac{1}{n} \right) \right.^{2} > 2$. This means that $\alpha - \frac{1}{n_{0}}$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $T$. But then $\alpha - \frac{1}{n_{0}} < \alpha = \sup T$, which is a contradiction since all upper bounds of $T$ should be greater to or equal than the [supremum](/notes/areas/mathematics/real_analysis/definitions/supremum/) $\alpha$. Thus, from the first part of the proof of Theorem 1.4.5, as well as the proof given above that $\alpha^{2} > 2$ is not possible, it follows that $\alpha^{2} = 2$ or $a = \sqrt{2}$.

# Exercise 1.4.8

> Give an example of each or state that the request is impossible. When a request is impossible, provide a compelling argument for why this is the case.

## (a)

> Two sets $A$ and $B$ with $A \cap B = \varnothing$, $\sup A = \sup B$, $\sup A \notin A$, and $\sup B \notin B$.

$A = \left. \left\{ n \in \mathbb{N}:1 - \frac{1}{2n} \right\} \right.$

$B = \left. \left\{ n \in \mathbb{N}:1 - \frac{1}{2n + 1} \right\} \right.$

## (b)

> A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of nested open intervals $J_{1} \supseteq J_{2} \supseteq J_{3} \supseteq \cdots$ with $\bigcap_{n = 1}^{\infty}J_{n}$ non-empty but containing only a finite number of elements.

$J_{n} = \left. \left( - \frac{1}{n},\frac{1}{n} \right) \right.$. Then $J_{1} \supseteq J_{2} \supseteq J_{3} \supseteq \cdots$ with $\bigcap_{n = 1}^{\infty}J_{n} = \{ 0\}$.

## (c)

> A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of nested unbounded closed intervals $L_{1} \supseteq L_{2} \supseteq L_{3} \supseteq \cdots$ with $\bigcap_{n = 1}^{\infty}L_{n} = \varnothing$. (An unbounded closed interval has the form $\left. \lbrack a,\infty\rbrack \right. = \{ x \in \mathbb{R}:x \geq a\}$.)

$L_{n} = \lbrack n,\infty)$ for $n \in \mathbb{N}$.

## (d)

> A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of closed (not necessarily nested) intervals $I_{1},I_{2},I_{3},\ldots$ with the property that $\bigcap_{n = 1}^{N}I_{n} \neq \varnothing$ for all $N \in \mathbb{N}$, but $\bigcap_{n = 1}^{\infty} = \varnothing$.

Impossible.

# Section 1.5 Exercises

## Exercise 1.5.1

See: <https://math.stackexchange.com/a/168827/79854>

> Finish the following proof for Theorem 1.5.7.
>
> Assume $B$ is a [countable](/notes/areas/mathematics/set_theory/definitions/countable/) set. Thus, there exists $f:\mathbb{N} \rightarrow B$, which is one-to-one and onto. Let $A \subseteq B$ be an infinite subset of $B$. We must show that $A$ is countable.
>
> Let $n_{1} = \min\{ n \in \mathbb{N}:f\left. (n) \right. \in A\}$. As a start to a definition of $g:\mathbb{N} \rightarrow A$ set $g\left. (1) \right. = f\left. \left( n_{1} \right) \right.$. Show how to inductively continue this process to produce a one-to-one [function](/notes/areas/mathematics/set_theory/definitions/function/) $g$ from $\mathbb{N}$ onto $A$.
>
> Restating Theorem 1.5.7: If $A \subseteq B$ is [countable](/notes/areas/mathematics/set_theory/definitions/countable/), then $A$ is either [countable](/notes/areas/mathematics/set_theory/definitions/countable/) or finite.

It is also useful to restate some relevant definitions:

> Definition 1.5.1: A [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:A \rightarrow B$ is one-to-one if $a_{1} \neq a_{2}$ in $A$ implies that $f\left. \left( a_{1} \right) \right. \neq f\left. \left( a_{2} \right) \right.$ in $B$. The [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ is onto if, given any $b \in B$, it is possible to find an element $a \in A$ for which $f\left. (a) \right. = b$.
>
> Definition 1.5.2 The set $A$ has the same [cardinality](/notes/areas/mathematics/set_theory/definitions/cardinality/) as $B$ if there exists $f:A \rightarrow B$ that is one-to-one and onto. In this case, we write $A \sim B$.
>
> Definition 1.5.5: A set $A$ is [countable](/notes/areas/mathematics/set_theory/definitions/countable/) if $\mathbb{N} \sim A$. An infinite set that is not [countable](/notes/areas/mathematics/set_theory/definitions/countable/) is called an uncountable set.

Now to the proof:

Let's start with the [countable](/notes/areas/mathematics/set_theory/definitions/countable/) infinite set $B$. There exists a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/) (one-to-one, onto) $f:\mathbb{N} \rightarrow B$. For each $n \in \mathbb{N}$, let $x_{n} = f\left. (n) \right.$, so $B = \{ x_{n}:n \in \mathbb{N}\}$ is an enumeration of $B$.

Now, consider the infinite set $A \subseteq B$. Imagine traversing the listing $\{ x_{1},x_{2},\ldots\}$ one element at a time -- eventually we must reach an element of $A$ since $A \neq \varnothing$. Let



$$
I_{1} = \{ n \in \mathbb{N}:x_{n} \in A\}
$$



$I_{1}$ is a set of positive integers so it has a smallest element, call it



$$
n_{1} = \min\{ n \in \mathbb{N}:f\left. (n) \right. \in A\}
$$



Now, let $I_{2} = I_{1}\backslash\{ n_{1}\}$, which is all of $I$ except the smallest element $n_{1}$. $I_{2}$ is another set of positive integers, which also has a smallest element, call it



$$
n_{2} = \min\{ n \in \mathbb{N}:f\left. (n) \right. \in A\backslash\{ f\left. \left( n_{1} \right) \right.\}\}
$$



In general, suppose that we have chosen $n_{1},n_{2},\ldots,n_{k - 1}$ such that $x_{n_{1}},x_{n_{2}},\ldots,x_{n_{k}} \in A$. Let $I_{k} = I_{1}\backslash\{ n_{1},n_{2},\ldots,n_{k - 1}\}$. $A$ is an infinite [subset](/notes/areas/mathematics/set_theory/definitions/subset/), so $A\backslash\{ x_{n_{1}},x_{n_{2}},\ldots,x_{n_{k}}\} \neq \varnothing$ and thus $I_{k} \neq \varnothing$. Thus, we may let $n_{k}$ be the smallest element of $I_{k}$ and continue constructing the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( n_{1},n_{2},\ldots \right) \right.$.

All we are doing here is going through $B$ in the order $x_{1},x_{2},\ldots$ until we come to the first element of $A$. That element is $x_{n_{1}}$ for some positive integer $n_{1}$. Then we continue through $B$ until we come to another element of $A$. That element is $x_{n_{2}}$ for some positive integer $n_{2} > n_{1}$. At each stage we have only found finitely many members of $A$, and since $A$ is infinite we can keep going. It is intuitively clear that this procedure cannot miss any elements of $A$, because at each stage we take the first one in the listing that we haven't already taken.

Thus, at the end of all of this, the map $g:\mathbb{N} \rightarrow A:k \mapsto x_{n_{k}}$ is a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/) between $\mathbb{N}$ and $A$, so $A$ is countably infinite.

## Exercise 1.5.3

> Use the following outline to supply proofs for the statements in Theorem 1.5.8.

### (a)

> First, prove statement (i) for two [countable](/notes/areas/mathematics/set_theory/definitions/countable/) sets, $A_{1}$ and $A_{2}$. Example 1.5.3 (ii) may be a useful reference. Some technicalities can be avoided by first replacing $A_{2}$ with the set $B_{2} = A_{2}\: A_{1} = \{ x \in A_{2}:x \notin A_{1}\}$. The point of this is that the union $A_{1} \cup B_{2}$ is equal to $A_{1} \cup A_{2}$ and the sets $A_{1}$ and $B_{2}$ are disjoint. (What happens if $B_{2}$ is finite?)
>
> Now, explain how the more general statement in (i) follows.

### (b)

> Explain why induction *cannot* be used to prove part (ii) of Theorem 1.5.8 from part (i).

## Exercise 1.5.5

### (a)

> Why is $A \sim A$ for every set $A$?

Since there must be a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/) $f:A \rightarrow A$ for $A \sim A$, the identity [function](/notes/areas/mathematics/set_theory/definitions/function/) $f\left. (a) \right. = a\quad\forall a \in A$ shows that $A \sim A$.

### (b)

> Given sets $A$ and $B$, explain why $A \sim B$ is equivalent to asserting $B \sim A$.

Since $A \sim B$, we know that there is a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/) $f:A \rightarrow B$. This means that we can define another [function](/notes/areas/mathematics/set_theory/definitions/function/) $g:B \rightarrow A$ that is bijective. More specifically, if $f:A \rightarrow B$ is a bijfection, then there exists an inverse [function](/notes/areas/mathematics/set_theory/definitions/function/) $f^{- 1}:B \rightarrow A$ which is also a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/).

### (c)

> For three sets $A,B,C$, show that $A \sim B$ and $B \sim C$ implies that $A \sim C$. These three properties are what is meant by saying that $\sim$ is an *equivalence relation*.

Since $A \sim B$, we know that there is a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/) $g:A \rightarrow B$. Since $B \sim C$, there is a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/) $f:B \rightarrow C$. Likewise, $h:A \rightarrow C$ is a [bijection](/notes/areas/mathematics/set_theory/definitions/bijection/). Let us define $h = f \circ g$, meaning $f$ composed with $g$.

To show that $h$ is one-to-one, take $a_{1},a_{2} \in A$, where $a_{1} \neq a_{2}$ and show that $f\left. \left( g\left. \left( a_{1} \right) \right. \right) \right. \neq f\left. \left( g\left. \left( a_{2} \right) \right. \right) \right.$. Then, $a_{1} \neq a_{2}$ implies that $g\left. \left( a_{1} \right) \right. \neq g\left. \left( a_{2} \right) \right.$ because $g$ is one-to-one. And $g\left. \left( a_{1} \right) \right. \neq g\left. \left( a_{2} \right) \right.$ implies that $f\left. \left( g\left. \left( a_{1} \right) \right. \right) \right. \neq f\left. \left( g\left. \left( a_{2} \right) \right. \right) \right.$ because $f$ is one-to-one. Thus, $h = f \circ g$ is one-to-one.

To show that $f \circ g$ is onto, take $c \in C$ and show that there exists an $a \in A$ with $f\left. \left( g\left. (a) \right. \right) \right. = c$. If $c \in C$, then there exists a $b \in B$ such that $f\left. (b) \right. = c$ because $f$ is onto. But for this same $b$, we have an $a \in A$ such that $g\left. (a) \right. = b$ since $g$ is onto. This implies that $f\left. (b) \right. = f\left. \left( g\left. (a) \right. \right) \right. = c$ and thus $h = f \circ g$ is onto.

## Exercise 1.5.6

### (a)

> Give an example of a [countable](/notes/areas/mathematics/set_theory/definitions/countable/) collection of disjoint open intervals.

Here, [disjoint](/notes/areas/mathematics/real_analysis/definitions/disjoint/) means "non-overlapping."

One such example is $\{ n \in \mathbb{N}:\left. (n,n + 1) \right.\} = \left. (0,1) \right.,\left. (1,2) \right.,\left. (2,3) \right.,\ldots$.

### (b)

> Give an example of an uncountable collection of disjoint open intervals, or argue that no such collection exists.

No such collection exists. Suppose that $C$ is any infinite collection of [disjoint](/notes/areas/mathematics/real_analysis/definitions/disjoint/) intervals. Every open interval contains at least one rational number $q_{I} \in \mathbb{I}$. Note that $q_{I} \neq q_{J}$ for $I = J$ since $I$ and $J$ must be [disjoint](/notes/areas/mathematics/real_analysis/definitions/disjoint/), so the set $\{ I \in C:q_{I}\}$ is in one-to-one correspondence with the elements of $C$. But this set is [countable](/notes/areas/mathematics/set_theory/definitions/countable/), being a [subset](/notes/areas/mathematics/set_theory/definitions/subset/) of $\mathbb{Q}$.

## Exercise 1.5.7

> Consider the open interval $\left. (0,1) \right.$, and let $S$ be the set of points in the open unit square; that is, $S = \{\left. (x,y) \right.:0 < x,y < 1\}$.

### (a)

> Find a one-to-one [function](/notes/areas/mathematics/set_theory/definitions/function/) that maps $\left. (0,1) \right.$ into, but not necessarily onto, $S$.

The [function](/notes/areas/mathematics/set_theory/definitions/function/) $f\left. (x) \right. = \left. \left( x,\frac{1}{3} \right) \right.$ is one-to-one.

### (b)

> Use the fact that every real number has a decimal expansion to produce a 1-1 [function](/notes/areas/mathematics/set_theory/definitions/function/) that maps $S$ into (0, 1). Discuss whether the formulated [function](/notes/areas/mathematics/set_theory/definitions/function/) is onto. (Keep in mind that any terminating decimal expansion such as .235 represents the same real number as $.234999\ldots$).

Given $\left. (x,y) \right. \in S$, let's write $x$ and $y$ in their decimal expansions:



$$
x = .x_{1}x_{2}x_{3\ldots}\quad y = .y_{1}y_{2}y_{3\ldots}
$$



where we make the convention that we always use the terminating form (or the repeated 0s) over the repeating 9s form when the situation arises.

Now define $f:S \rightarrow \left. (0,1) \right.$ by



$$
f\left. (x,y) \right. = .x_{1}y_{1}x_{2}y_{2}x_{3}y_{3\ldots}
$$



In order to show that $f$ is one-to-one, assume that we have two distinct points $\left. (x,y) \right. \neq \left. (w,z) \right.$ from $S$. Then it must be that either $x \neq w$ or $y \neq z$, and this implies that in at least one decimal place we have $x_{i} \neq w_{i}$ or $y_{i} \neq z_{i}$. But this enough to conclude that $f\left. (x,y) \right. \neq f\left. (w,z) \right.$

The [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ is not onto. For instance the point $t = .555959595\ldots$ is not in the [range](/notes/areas/mathematics/set_theory/definitions/range/) of $f$ because the ordered pair $\left. (x,y) \right.$ with $x = .555\ldots$ and $y = .5999\ldots$ would not be allowed due to our convention of using terminating decimals instead of repeated 9s.

## Exercise 1.5.9

> A real number $x \in \mathbb{R}$ is called algebraic if there exist integers
>
> 

$$
a_{0},a_{1},a_{2},\ldots,a_{n} \in \mathbb{Z}
$$


>
> not all zero, such that
>
> 

$$
a_{n}x^{n} + a_{n - 1}x^{n - 1} + \cdots + a_{1}x + a_{0} = 0
$$


>
> Said another way, a real number is algebraic if it is the root of a polynomial with integer coefficients. Real numbers that are not algebraic are called transcendental numbers. Reread the last paragraph of Section 1.1. The final question posed here is closely related to the question of whether or not transcendental numbers exist.
>
> Last paragraph of section 1.1:
>
> The question of how to actually construct $\mathbb{R}$ from $\mathbb{Q}$ is rather complicated business. It is discussed in Section 1.3, and then again in more detail in Section 8.6. For the moment, it is not too inaccurate to say that $\mathbb{R}$ is obtained by filling in the gaps in $\mathbb{Q}$. Wherever there is a hole, a new irrational number is defined and placed into the ordering that already exists on $\mathbb{Q}$. The real numbers are then the union of these irrational numbers together with the more familiar rational ones. What properties does the set of irrational numbers have? How do the sets of rational and irrational numbers fit together? Is there a kind of symmetry between the rationals and the irrationals, or is there some sense in which we can argue that one type of real number is more common than the other? The one method we have seen so far for generating examples of irrational numbers is through square roots. Not too surprisingly, other roots such as $2^{\frac{1}{3}}$ or $3^{\frac{1}{5}}$ are most often irrational. Can all irrational numbers be expressed as algebraic combinations of $n$th roots and rational numbers, or are there still other irrational numbers beyond those of this form?

### (a)

> Show that $\sqrt{2},2^{\frac{1}{3}},\mathrm{\text{ and }}\sqrt{3} + \sqrt{2}$ are algebraic.

### (b)

Fix $n \in \mathbb{N}$ and let $A_{n}$ be the algebraic numbers obtained as roots of polynomials with integer coefficients that have degree $n$. Using the fact that every [polynomial](/notes/areas/mathematics/linear_algebra/definitions/polynomial/) has a finite number of roots, show that $A_{n}$ is [countable](/notes/areas/mathematics/set_theory/definitions/countable/).

### (c)

> Now, argue that the set of all algebraic numbers is countable. What may we conclude about the set of transcendental numbers?

## Exercise 1.5.11 (Schröder-Bernstein Theorem)

> Assume there exists a one-to-one [function](/notes/areas/mathematics/set_theory/definitions/function/) $fX \rightarrow Y$ and another one-to-one [function](/notes/areas/mathematics/set_theory/definitions/function/) $g:Y \rightarrow X$. Follow the steps to show that there exists a one-to-one [function](/notes/areas/mathematics/set_theory/definitions/function/) $h:X \rightarrow Y$ and hence $X \sim Y$.

The strategy is to partition $X$ and $Y$ into components



$$
X = A \cup A'\quad\mathrm{\text{and}}\quad Y = B \cup B'
$$



with $A \cap A' = \varnothing$ and $B \cap B' = \varnothing$, in such a way that $f$ maps $A$ onto $B$, and $g$ maps $B'$ onto $A'$.

### (a)

> Explain how achieving this would lead to a proof that $X \sim Y$.

### (b)

> Set $A_{1} = X\backslash g\left. (Y) \right. = \{ x \in X:x \notin g\left. (Y) \right.\}$ (what happens if $A_{1} = \varnothing$?) and inductively define a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of sets by letting $A_{n + 1} = g\left. \left( f\left. \left( A_{n} \right) \right. \right) \right.$. Show that $\{ A_{n}:n \in \mathbb{N}\}$ is a pairwise disjoint collection of subsets of $X$, while $\{ f\left. \left( A_{n} \right) \right.:n \in \mathbb{N}\}$ is a similar collection in $Y$.

### (c)

> Let $A = \bigcup_{n = 1}^{\infty}A_{n}$ and $B = \bigcup_{n = 1}^{\infty}f\left. \left( A_{n} \right) \right.$. Show that $f$ maps $A$ onto $B$.

### (d)

> Let $A' = X\backslash A$ and $B' = Y\backslash B$. Show that $g$ maps $B'$ onto $A'$.

# Section 1.6 Exercises

## Exercise 1.6.1

# Section 2.2 Exercises

## Exercise 2.2.1

> What happens if we reverse the order of the quantifiers in Definition 2.2.3?
>
> *Definition*: A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right.$ *verconges* to $x$ if there exists an $\epsilon > 0$ such that for all $N \in \mathbb{N}$ it is true that $n \geq N$ implies $\left| x_{n} - x \right| < \epsilon$.
>
> Given an example of a vercongent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/). Is there an example of a vercongent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) to two different values? What exactly is being described in this strange definition?

Take the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)



$$
\left. \left\{ - \frac{1}{2},\frac{1}{2}, - \frac{1}{2},\frac{1}{2} \right\} \right.
$$



This [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) "verconges" to $x = 0$. To see this, note that we only have to produce a single $\epsilon > 0$ where the condition follows, and in this case we take $\epsilon = 1$. This works since for all $N \in \mathbb{N}$, it is true that $n \geq N$ implies that $\left| x_{n} - \frac{1}{2} \right| < 1$. This is also an example of both a "vercongent" and a divergent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/).

In general, a vercongent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is a bounded [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/). That is, there exists some $M > 0$ satisfying $\left| x_{n} \right| \leq M$ for all $n \in \mathbb{N}$. In this case we can always take $x = 0$ and $\epsilon M + 1$. Then $\left| x_{n} - x \right| = \left| x_{n} \right| < \epsilon$ and the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) "verconges" to 0.

## Exercise 2.2.2

> Verify, using the definition of [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) of a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/), that the following [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s converge to the proposed limit.

### (a)

> $\lim\frac{2n + 1}{5n + 4} = \frac{2}{5}$.

Scratch work: We have for suitably large values of $n$,



$$
\left| \frac{2n + 1}{5n + 4} - \frac{2}{5} \right| < \epsilon
$$



where



$$
\begin{aligned}
\left| \frac{2n + 1}{5n + 4} - \frac{2}{5} \right| & = \left| - \frac{3}{20 + 25n} \right| \\
 & = \frac{3}{20 + 25n} \\
 & < \epsilon
\end{aligned}
$$



or $n > - \frac{4}{5} + \frac{3}{25\epsilon}$.

Moving on to the proof:

Let $\epsilon > 0$ be arbitrary. There exists some $N \in N$ such that whenever $N > - \frac{4}{5} + \frac{3}{25\epsilon}$, we have



$$
\left| \frac{2n + 1}{5n + 4} - \frac{2}{5} \right| < \epsilon
$$



This ends the proof.

### (b)

> $\lim\frac{2n^{2}}{n^{3} + 3} = 0$

Scratch work: We have for suitably large values of $n$,



$$
\left| \frac{2n^{2}}{n^{3} + 3} - 0 \right| < \epsilon
$$



## Exercise 2.2.3

> Describe what we would have to demonstrate in order to disprove each of the following statements.

### (a)

> At every college in the United States, there is a student who is at least seven feet tall.

That for at least one college, all students are less than seven feet tall.

### (b)

> For all colleges in the United States, there exists a professor who gives every student a grade of either A or B.

That for at least one college, all professors give at least one student a C or less.

### (c)

> There exists a college in the United States where every student is at least six feet tall.

That for all colleges, there exists a student less than six feet tall.

## 2.2.4

> Give an example of each or state that the request is impossible. For any that are impossible, give a compelling argument for why that is not the case.

### (a)

> A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) with an infinite number of ones that does not converge to one.

The [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. (1,2,3,1,2,3,\ldots) \right.$ has an infinite number of ones and is divergent.

### (b)

> A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) with an infinite number of ones that converges to a limit not equal to one.

Not possible. Suppose that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( a_{n} \right) \right.$ had infinitely many ones but converged to $a \neq 1$. Assume that $1 < a$ (the other case is handled similarly. Then let $\epsilon = a - 1 > 0$. Since $\left. \left( a_{n} \right) \right.$ converges to $a$, there exists some $N \in \mathbb{N}$ such that if $n \geq N$, then $\left| a_{n} - a \right| < a - 1$. This implies, in particular, that $- a + 1 < a_{n} - a$, which implies that $1 < a_{n}$ for all $n \geq N$. But this means that all but a finite number of the $a_{n}$ terms are strictly greater than 1, which is a contradiction.

### (c)

> A divergent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) such that for every $n \in \mathbb{N}$ it is possible to find $n$ consecutive ones somewhere in the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/).

The [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)



$$
\left. (1,2,1,1,3,1,1,1,1,4,1,1,1,1,5) \right.
$$



has $n$ consecutive ones for any $n$ but is unbounded and thus divergent.

## Exercise 2.2.5

> Let $\lbrack\left. \lbrack x\rbrack \right.$ be the greatest integer less than or equal to $x$. For example, $\left. \left\lbrack \left. \lbrack\pi\rbrack \right. \right\rbrack \right. = 3$ and $\left. \left\lbrack \left. \lbrack 3\rbrack \right. \right\rbrack \right. = 3$. For each [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/), find $\lim a_{n}$ and verify it with the definition of [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/).

### (a)

> $a_{n} = \left. \left\lbrack \left. \lbrack 5/n\rbrack \right. \right\rbrack \right.$

Scratch work: we have that



$$
\begin{aligned}
\lim\limits_{n \rightarrow \infty}\left. \left( \left. \left\lbrack \left. \lbrack 5/n\rbrack \right. \right\rbrack \right. \right) \right. & = \left. \left\lbrack \left. \left\lbrack \lim\limits_{n \rightarrow \infty}5/n \right\rbrack \right. \right\rbrack \right. \\
 & = \lbrack\left. \left\lbrack 5\lim\limits_{n \rightarrow \infty}1/n \right\rbrack \right. \\
 & = \left. \left\lbrack \left. \left\lbrack 5 \cdot \frac{1}{\lim\limits_{n \rightarrow \infty}n} \right\rbrack \right. \right\rbrack \right. \\
 & = 0
\end{aligned}
$$



Proof: Let $\epsilon > 0$ be arbitrary. There exists an $N \in \mathbb{N}$ such that $n \geq N$ implies



$$
\left| \left. \left\lbrack \left. \left\lbrack \frac{5}{n} \right\rbrack \right. \right\rbrack \right. - 0 \right| < \epsilon
$$



For example, pick $N = 6$. If $n \geq N$, we then have $\left| \left. \left\lbrack \left. \left\lbrack \frac{5}{n} \right\rbrack \right. \right\rbrack \right. - 0 \right| = |0 - 0| < \epsilon$ because $\left. \left\lbrack \left. \left\lbrack \frac{5}{n} \right\rbrack \right. \right\rbrack \right. = 0$ for all $n > 5$

### (b)

> $a_{n} = \left. \left\lbrack \left. \left\lbrack \left. (12 + 4n) \right./3n \right\rbrack \right. \right\rbrack \right.$

Scratch work: we have that



$$
\begin{aligned}
\lim\limits_{n \rightarrow \infty}\left. \left( \left. \left\lbrack \left. \left\lbrack \left. (12 + 4n) \right./3n \right\rbrack \right. \right\rbrack \right. \right) \right. & = \left. \left\lbrack \left. \left\lbrack \lim\limits_{n \rightarrow \infty}\left. (12 + 4n) \right./3n \right\rbrack \right. \right\rbrack \right. \\
 & = \left. \left\lbrack \left. \left\lbrack \lim\limits_{n \rightarrow \infty}4/3 + \lim\limits_{n \rightarrow \infty}4/n \right\rbrack \right. \right\rbrack \right. \\
 & = \left. \left\lbrack \left. \left\lbrack \lim\limits_{n \rightarrow \infty}4/3 + 4/\left. \left( \lim\limits_{n \rightarrow \infty}n \right) \right. \right\rbrack \right. \right\rbrack \right. \\
 & = \left. \left\lbrack \left. \lbrack 4/3\rbrack \right. \right\rbrack \right. + \left. \left\lbrack \left. \lbrack 0\rbrack \right. \right\rbrack \right. \\
 & = 1
\end{aligned}
$$



Proof: Let $\epsilon > 0$ be arbitrary. By choosing $N = 7$, we have that for $n \geq N$, $\left| \left. \left\lbrack \left. \left\lbrack \left. (12 + 4n) \right./3n - 1 \right\rbrack \right. \right\rbrack \right. \right| = |1 - 1| < \epsilon$ because $\left. \left\lbrack \left. \left\lbrack \left. (12 + 4n) \right. \right\rbrack \right. \right\rbrack \right. = 1$ for all $n \geq 7$.

Answering the last part --- the choice of $N$ does not depend on $\epsilon$ in the usual way. In part (b) for example, setting $N = 7$ is a suitable response for *every* choice of $\epsilon > 0$. This is a rare example where a smaller $\epsilon > 0$ does not require a larger $N$ in response.

## Exercise 2.2.7

> Here are two useful definitions:
>
> 1.  A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( a_{n} \right) \right.$ is *eventually* in a set $A \subseteq \mathbb{R}$ if there exists an $N \in \mathbb{N}$ such that $a_{n} \in A$ for all $n \geq N$.
>
> 2.  A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( a_{n} \right) \right.$ is *frequently* in a set $A \subseteq \mathbb{R}$ if, for every $N \in \mathbb{N}$, there exists an $n \geq N$ such that $a_{n} \in A$.

### (a)

> Is the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. ( - 1) \right.^{n}$ eventually or frequently in the set?

$$
\left. ( - 1) \right.^{n} = \{ - 1,1, - 1,1,dots\}
$$



This [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is frequently in the set.

### (b)

> Which definition is stronger? Does frequently imply eventually or does eventually imply frequently?

Definition (1) is stronger. Frequently does not necessarily imply eventually, but eventually always implies frequently.

### (c)

> Given an alternate rephrasing of Definition 2.2.3B using either frequently or eventually. Which is the term we want?

A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( a_{n} \right) \right.$ converges to $a$ if given any $\epsilon$-neighborhood $V_{\epsilon}\left. (a) \right.$, $a_{n}$ is eventually in $V_{\epsilon}\left. (a) \right.$.

### (d)

> Suppose an infinite number of terms of a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right.$ are equal to 2. Is $\left. \left( x_{n} \right) \right.$ necessarily eventually in the interval $\left. (1.9,2.1) \right.$? Is it frequently in $\left. (1.9,2.1) \right.$

For the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right. = \left. (2,2,2,\ldots,1) \right.$, $\left. \left( x_{n} \right) \right.$ is frequently but not eventually in the interval $\left. (1.9,2.1) \right.$.

For the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right. = \left. (1,1,1,2,2,2,2,2,\ldots) \right.$, $\left. \left( x_{n} \right) \right.$ is frequently and also eventually in the interval $\left. (1.9,2.1) \right.$.

## Exercise 2.2.8

# Section 2.6 Exercises

## Exercise 2.6.1

> Supply a proof for Theorem 2.6.2.
>
> Restating Theorem 2.6.2: Every convergent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/).

Assume $\left. \left( x_{n} \right) \right. \rightarrow x$. Let $\epsilon > 0$ be arbitrary. There exists an $N \in \mathbb{N}$ such that $n,m \geq N$ implies that $\left| x_{n} - x \right| < \frac{\epsilon}{2}$ and $\left| x_{m} - x \right| < \frac{\epsilon}{2}$.

By the [triangle inequality](/notes/areas/mathematics/real_analysis/definitions/triangle_inequality/)



$$
\begin{aligned}
\left| x_{n} - x_{m} \right| & = \left| x_{n} - x + x - x_{m} \right| \\
 & \leq \left| x_{n} - x \right| + \left| x_{m} - x \right| \\
 & < \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
 & = \epsilon
\end{aligned}
$$



## Exercise 2.6.3

> If $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ are [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/)s, then one easy way to prove that $\left. \left( x_{n} + y_{n} \right) \right.$ is Cauchy is to use the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/). By Theorem 2.6.4, $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ must be convergent, and the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/) then implies $\left. \left( x_{n} + y_{n} \right) \right.$ is convergent and hence Cauchy.

### (a)

> Give a direct argument that $\left. \left( x_{n} + y_{n} \right) \right.$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/) that does not use the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) or the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/).

Let $\epsilon > 0$ be arbitrary. We need to find an $N$ such that $n,m \geq$ implies that $\left| \left. \left( x_{n} + y_{n} \right) \right. - \left. \left( x_{m} + y_{m} \right) \right. \right| < \epsilon$. Because $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ are Cauchy we can choose $N$ such that when $n,m \geq N$ it follows that $\left| x_{n} - x_{m} \right| < \frac{\epsilon}{2}$ and $\left| y_{n} - y_{m} \right| < \frac{\epsilon}{2}$ Now write,



$$
\begin{aligned}
\left| \left. \left( x_{n} + y_{n} \right) \right. - \left. \left( x_{m} + y_{m} \right) \right. \right| & \leq \left| x_{n} - x_{m} \right| + \left| y_{n} - y_{m} \right| \\
 & < \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
 & = \epsilon
\end{aligned}
$$



### (b)

> Do the same for the product $\left. \left( x_{n}y_{n} \right) \right.$.

Let $\epsilon > 0$ be arbitrary. We need to find an $N$ such that $n,m \geq$ implies that $\left| x_{n}y_{n} - x_{m}y_{m} \right| < \epsilon$. Employing the usual "adding zero" trick to exploit the [triangle inequality](/notes/areas/mathematics/real_analysis/definitions/triangle_inequality/) gives



$$
\begin{aligned}
\left| x_{n}y_{n} - x_{m}y_{m} \right| & = \left| x_{n}y_{n} - x_{n}y_{m} + x_{n}y_{m} - x_{m}y_{m} \right| \\
 & \leq \left| x_{n}y_{n} - x_{n}y_{m} \right| + \left| x_{n}y_{m} - x_{m}y_{m} \right| \\
 & = \left| x_{n} \right|\left| y_{n}y_{m} \right| + \left| y_{m} \right|\left| x_{n} - x_{m} \right|
\end{aligned}
$$



Since $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ are Cauchy, we know by Lemma 2.6.3 that [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/)s are bounded. Now, let $\left| x_{n} \right| \leq K$ and $\left| y_{m} \right| \leq L\quad\forall m,n$. We can choose $N_{1}$ such that $m,n \geq N_{1}$ implies $\left| x_{n} - x_{m} \right| < \frac{\epsilon}{2L}$. Similarly, choose $N_{2}$ such that $m,n \geq N_{2}$ implies $\left| y_{n} - y_{m} \right| < \frac{\epsilon}{2K}$. Now let $N = \max\{ N_{1},N_{2}\}$. Then for $m,n \geq N$ it follows that



$$
\begin{aligned}
\left| x_{n}y_{n} - x_{m}y_{m} \right| & \leq \left| x_{n} \right|\left| y_{n}y_{m} \right| + \left| y_{m} \right|\left| x_{n} - x_{m} \right| \\
 & < K\frac{\epsilon}{2K} + L\frac{\epsilon}{2L} \\
 & = \epsilon
\end{aligned}
$$



## Exercise 2.6.5

> Consider the following (invented) definition: A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( s_{n} \right) \right.$ is *pseudo-Cauchy* if, for all $\epsilon > 0$, there exists an $N$ such that if $n \geq N$, then $\left| s_{n + 1} - s_{n} \right| < \epsilon$.
>
> Decide which one of the following two propositions is actually true. Supply a proof for the valid statement and a counter example for the other.
>
> 1.  Pseudo-[Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/)s are bounded.
>
> 2.  If $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ are pseudo-Cauchy, then $\left. \left( x_{n} + y_{n} \right) \right.$ is pseudo-Cauchy as well.

The given definition of the Pseudo-[Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/) only requires that difference between consecutive terms in the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) be arbitrarily small, whereas the real Cauchy property requires that the difference between any two terms beyond a certain point ($m,n \geq N$) be arbitrarily small.

Thus, (i) is not necessarily bounded. A counterexample would be the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of partial sums of the harmonic series



$$
\left. (1) \right.,\left. \left( (1 + \frac{1}{2} \right) \right.,\left. \left( 1 + \frac{1}{2} + \frac{1}{3} \right) \right.,\left. \left( 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} \right) \right.
$$



Also, (ii) is true. Proof: Let $e > 0$ be arbitrary. Choose $N$ such that $n \geq N$ implies that $\left| (x_{n + 1} + y_{n + 1} - \left. \left( x_{n} + y_{n} \right) \right. \right| < \epsilon$. Because $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ are psuedo Cauchy, we can choose $N$ so that when $n,m \geq N$, it follows that $\left| x_{n + 1} - x_{n} \right| < \frac{\epsilon}{2}$ and $\left| y_{n + 1} - y_{n} \right| < \frac{\epsilon}{2}$.



$$
\begin{aligned}
\left| \left. \left( x_{n + 1} + y_{n + 1} \right) \right. - \left. \left( x_{n} - y_{n} \right) \right. \right| & \leq \left| x_{n + 1} - x_{n} \right| + \left| y_{n + 1} - y_{n} \right| \\
 & < \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
 & = \epsilon
\end{aligned}
$$



# Section 2.7 Exercises

## Exercise 2.7.1

> Proving the [Alternating_Series_Test](/notes/areas/mathematics/real_analysis/definitions/alternating_series_test/) (Theorem 2.7.7) amounts to showing that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of partial sums
>
> 

$$
s_{n} = a_{1} - a_{2} + a_{3} - \cdots \pm a_{n}
$$


>
> converges. (The opening example in Section 2.1 includes a typical illustration of $\left. \left( s_{n} \right) \right.$.) Different characterizations of completeness lead to different proofs.

> Restating Theorem 2.7.7 ([Alternating_Series_Test](/notes/areas/mathematics/real_analysis/definitions/alternating_series_test/)): Let $\left. \left( a_{n} \right) \right.$ be a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) satisfying
>
> 1.  $a_{1} \geq a_{2} \geq a_{3} \geq \cdots \geq a_{n} \geq a_{n + 1}\cdots$
>
> 2.  $\left. \left( a_{n} \right) \right. \rightarrow 0$
>
> Then, the alternative series $\sum_{n = 1}^{\infty}\left. ( - 1) \right.^{n + 1}a_{n}$ converges.

### (a)

> Prove the [Alternating_Series_Test](/notes/areas/mathematics/real_analysis/definitions/alternating_series_test/) by showing that $\left. \left( s_{n} \right) \right.$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/).

Let $\epsilon > 0$ be arbitrary. We need to find an $N$ such that $n > m \geq N$ implies $\left| s_{n} - s_{m} \right| < \epsilon$. We know that



$$
\begin{aligned}
\left| s_{n} - s_{m} \right| & = |\left. \left( a_{1} - a_{2} + a_{3} - \cdots + a_{m + 1} - a_{m + 2} + \cdots \pm a_{n} \right) \right. \\
 & - \left. \left( a_{1} - a_{2} + a_{3} - \cdots \pm a_{m} \right) \right.| \\
 & = \left| a_{m + 1} - a_{m + 2} + \cdots \pm a_{n} \right|
\end{aligned}
$$



(continued on next page)

Given our hypothesis from part (i), we know that $\left. \left( a_{n} \right) \right.$ is monotonically decreasing and since all the terms are positive, we can show by induction that for all $n > m$



$$
\left| a_{m + 1} - a_{m + 2} + \cdots \pm a_{n} \right| \leq \left| a_{m + 1} \right|
$$



Because $\left. \left( a_{n} \right) \right. \rightarrow 0$, we can choose $N$ such that $m \geq N$ implies $\left| a_{m} \right| \leq \epsilon$. But this implies



$$
\left| s_{n} - s_{m} \right| = \left| a_{m + 1} - a_{m + 2} + \cdots \pm a_{n} \right| \leq \left| a_{m + 1} \right| < \epsilon
$$



for $n > m \geq N$.

### (b)

See: [Proof of Alternating Series Test](https://tutorial.math.lamar.edu/classes/calcii/AlternatingSeries.aspx#Series_AltSeries_Proof)

> Supply another proof for this result using the [Nested_Interval_Property](/notes/areas/mathematics/real_analysis/definitions/nested_interval_property/) (Theorem 1.4.1).

Restating Theorem 1.4.1 ([Nested_Interval_Property](/notes/areas/mathematics/real_analysis/definitions/nested_interval_property/)): For each $n \in \mathbb{N}$, assume we are given a closed interval $I_{n} = \left. \left\lbrack a_{n},b_{n} \right\rbrack \right. = \{ x \in \mathbb{R}:a_{n} \leq x \leq b_{n}\}$. Assume also that each $I_{n}$ contains $I_{n + 1}$. Then, the resulting nested [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of closed intervals



$$
I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots
$$



has a non-empty intersection; that is, $\bigcap_{n = 1}^{\infty}I_{n} \neq 0$

Now to the requested proof:

Let $I_{1}$ be the closed interval $\left. \left\lbrack 0,s_{1} \right\rbrack \right.$. Then let $I_{2}$ be the closed interval $\left. \left\lbrack s_{2},s_{1} \right\rbrack \right.$, which must be contained in $I_{1}$ since $\left. \left( a_{n} \right) \right.$ is monotonically decreasing. Continuing on, we can construct a nested [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of closed intervals



$$
I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots
$$



By the [Nested_Interval_Property](/notes/areas/mathematics/real_analysis/definitions/nested_interval_property/) there exists at least one point $S$ satisfying $S \in I_{n}$ for every $n \in \mathbb{N}$. So now we have a candidate for the limit, and we must show that $\left. \left( s_{n} \right) \right. \rightarrow S$.

Let $\epsilon > 0$ be arbitrary. We need to show that there exists an $N$ such that $\left| s_{n} - S \right| < \epsilon$ whenever $n \geq N$. By construction, the length of $I_{n}$ is $\left| s_{n} - s_{n - 1} \right| = a_{n}$. Because $\left. \left( a_{n} \right) \right. \rightarrow 0$ we can choose $N$ such that $a_{n} < \epsilon$ whenever $n \geq N$. Thus



$$
\left| s_{n} - S \right| \leq a_{n} < \epsilon
$$



because both $s_{n},S \in I_{n}$.

Some depictions of this are shown on the next page.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/2.7.1b.png)

### (c)

> Consider the [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/)s $\left. \left( s_{2n} \right) \right.$ and $\left. \left( s_{2n + 1} \right) \right.$, and show how the [Monotone_Convergence_Theorem](/notes/areas/mathematics/real_analysis/definitions/monotone_convergence_theorem/) leads to a third proof for the [Alternating_Series_Test](/notes/areas/mathematics/real_analysis/definitions/alternating_series_test/).

Restating Theorem 2.4.2 ([Monotone_Convergence_Theorem](/notes/areas/mathematics/real_analysis/definitions/monotone_convergence_theorem/)): If a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is monotonic and bounded, then it converges.

We need to show that the [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) $\left. \left( s_{2n} \right) \right.$ is increasing. The assumption



$$
\begin{aligned}
s_{2} & = a_{1} - a_{2} \\
s_{4} & = \left. \left( a_{1} - a_{2} \right) \right. + a_{3} - a_{4} = s_{2} + a_{3} - a_{4} \geq s_{2} \\
s_{6} & = \left. \left( a_{1} - a_{2} + a_{3} - a_{4} \right) \right. + a_{5} - a_{6} = s_{4} + a_{5} - a_{6} \geq s_{4} \\
 & \vdots \\
s_{2n} & = s_{2n - 2} + a_{2n - 1} - a_{2n} \geq s_{2n - 2}
\end{aligned}
$$



Now to show that $\left. \left( s_{2n} \right) \right.$ is bounded above. Writing out the term $s_{2n}$, we have



$$
\begin{aligned}
s_{2n} & = a_{1} - a_{2} + a_{3} - a_{4} + a_{5} + \cdots - a_{2n - 2} + a_{2n - 1} - a_{2n} \\
 & = a_{1} - \left. \left( a_{2} - a_{3} \right) \right. - \left. \left( a_{4} - a_{5} \right) \right. + \cdots - \left. \left( a_{2n - 2} - a_{2n - 1} \right) \right. - a_{2n}
\end{aligned}
$$



Each of the quantities in parenthesis are positive and by assumption we know that $a_{2n}$ is also positive. So, this tells us that $s_{2n} \leq a_{1}$ for all $n$.

So we know the [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) $\left. \left( s_{2n} \right) \right.$ is also bounded above.

Knowing these two things, the [Monotone_Convergence_Theorem](/notes/areas/mathematics/real_analysis/definitions/monotone_convergence_theorem/) allows us to assert that $\left. \left( s_{2n} \right) \right.$ converges and that there exists an $s \in \mathbb{R}$ satisfying $s = \lim\left. \left( s_{2n} \right) \right.$.

(continued on next page)

Now we can determine the limit of the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of odd partial sums as follows:



$$
\begin{aligned}
\lim\limits_{n \rightarrow \infty}\left. \left( s_{2n + 1} \right) \right. & = \lim\limits_{n \rightarrow \infty}\left. \left( s_{2n} + a_{2n + 1} \right) \right. \\
 & = \lim\limits_{n \rightarrow \infty}\left. \left( s_{2n} \right) \right. + \lim\limits_{n \rightarrow \infty}\left. \left( a_{2n + 1} \right) \right. \\
 & = s + 0 \\
 & = s
\end{aligned}
$$



The fact that both $\left. \left( s_{2n} \right) \right.$ and $\left. \left( s_{2n + 1} \right) \right.$ converge to $s$ implies that $\left. \left( s_{n} \right) \right. \rightarrow S$ as well (see Exercise 2.3.5).

## Exercise 2.7.3

### (a)

> Provide the details for the proof of the [Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/) (Theorem 2.7.4) using the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) for Series.

Restating Theorem 2.7.4 ([Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/)):

> Assume $\left. \left( a_{k} \right) \right.$ and $\left. \left( b_{k} \right) \right.$ are [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s satisfying $0 \leq a_{k} \leq b_{k}\quad\forall k \in \mathbb{N}$. Then,
>
> 1.  If $\sum_{k = 1}^{\infty}b_{k}$ converges, then $\sum_{k = 1}^{\infty}a_{k}$ converges
>
> 2.  If $\sum_{k = 1}^{\infty}a_{k}$ diverges, then $\sum_{k = 1}^{\infty}b_{k}$ diverges

Restating Theorem 2.7.2 ([Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) for Series):

> The series $\sum_{k = 1}^{\infty}a_{k}$ converges if and only if, given $\epsilon > 0$, there exists an $N \in \mathbb{N}$ such that whenever $n > m \geq N$ it follows that
>
> 

$$
\left| a_{m + 1} + a_{m + 2} + \cdots + a_{n} \right| < \epsilon
$$



Proof of part 1 of the [Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/):

Assume that $\sum_{k = 1}^{\infty}b_{k}$ converges. Thus, given $\epsilon > 0$, there exists an $N \in \mathbb{N}$ such that whenever $n > m \geq N$, it follows that $\left| b_{m + 1} + b_{m + 2} + \cdots + b_{n} \right| < \epsilon$. Since $0 \leq a_{k} \leq b_{k}\quad\forall k \in \mathbb{N}$, we have



$$
\left| a_{m + 1} + a_{m + 2} + \cdots + a_{n} \right| < \left| b_{m + 1} + b_{m + 2} + \cdots + b_{n} \right| < \epsilon
$$



whenever $n > m \geq N$, and so $\sum_{k = 1}^{\infty}a_{k}$ converges as well.

(continued on next page)

Proof of part 2:

We could attempt this proof by working with a negated version of the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/), but let's proceed via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/). This is actually an example of a *contrapositive* proof.

Rather than proving "If P, then Q," we can argue that "Not Q implies not P."

In the context of this problem, "Not Q implies not not P" is just the statement "$\sum_{k = 1}^{\infty}b_{k}$" cconverges implies that "$\sum_{k = 1}^{\infty}a_{k}$" converges. But this is exactly what we just showed in part 1 above.

### (b)

> Give another proof for the [Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/), this time using the [Monotone_Convergence_Theorem](/notes/areas/mathematics/real_analysis/definitions/monotone_convergence_theorem/).

Restating Theorem 2.4.2 ([Monotone_Convergence_Theorem](/notes/areas/mathematics/real_analysis/definitions/monotone_convergence_theorem/)):

> If a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is monotonic and bounded, then it converges.

Proof of part 1:

Let $s_{n} = a_{1} + a_{2} + \cdots + a_{n}$ be the partial sums for $\sum_{k = 1}^{\infty}a_{k}$ and let $t_{n} = b_{1} + b_{2} + \cdots + b_{n}$ be the partial sums for $\sum_{k = 1}^{\infty}b_{k}$. Because $0 \leq a_{k} \leq b_{k}\quad\forall k \in \mathbb{N}$, both $\left. \left( s_{n} \right) \right.$ and $\left. \left( t_{n} \right) \right.$ are increasing, and in addition we have $s_{n} \leq t_{n}\quad\forall n \in \mathbb{N}$. Because $\sum_{k = 1}^{\infty}b_{k}$ converges, $\left. \left( t_{n} \right) \right.$ is bounded and thus $\left. \left( s_{n} \right) \right.$ is also bounded. By the [Monotone_Convergence_Theorem](/notes/areas/mathematics/real_analysis/definitions/monotone_convergence_theorem/), $\sum_{k = 1}^{\infty}a_{k}$ converges.

Proof of part 2: As above, this is the contrapositive version of the statement in (i).

## Exercise 2.7.5

> Now that we have proved the basic facts about geometric series, supply a proof for Corollary 2.4.7.

Restating Corollary 2.4.7:

> The series $\sum_{n = 1}^{\infty}\frac{1}{n^{p}}$ converges if and only if $p > 1$.

> Restating Theorem 2.4.6 ([Cauchy_Condensation_Test](/notes/areas/mathematics/real_analysis/definitions/cauchy_condensation_test/)): Suppose $\left. \left( b_{n} \right) \right.$ is decreasing and satisfies $b_{n} \geq 0\quad\forall n \in \mathbb{N}$. Then, the series $\sum_{n = 1}^{\infty}b_{n}$ converges if and only if the series
>
> 

$$
\sum_{n = 0}^{\infty}2^{n}b_{2^{n}} = b_{1} + 2b_{2} + 4b_{4} + 8b_{8} + 16b_{16}
$$


>
> converges.

Proof: For $p > 1$ we know that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( \frac{1}{n^{p}} \right) \right.$ is decreasing and satisfies $\left. \left( \frac{1}{n^{p}} \right) \right. > 0\quad\forall n \in \mathbb{N}$, so we can apply the [Cauchy_Condensation_Test](/notes/areas/mathematics/real_analysis/definitions/cauchy_condensation_test/), which states that $\sum_{n = 1}^{\infty}\frac{1}{n^{p}}$ converges if and only if



$$
\begin{aligned}
\sum_{n = 0}^{\infty}2^{n}\left. \left( \frac{1}{2^{n}} \right) \right.^{p} & = \sum_{n = 0}^{\infty}2^{n}\left. \left( 2^{- n} \right) \right.^{p} \\
 & = \sum_{n = 0}^{\infty}2^{n - np} \\
 & = \sum_{n = 0}^{\infty}2^{n\left. (1 - p) \right.} \\
 & = \sum_{n = 0}^{\infty}\left. \left( \frac{1}{2^{p - 1}} \right) \right.^{n}
\end{aligned}
$$



converges.

By the [Geometric_Series_Test](/notes/areas/mathematics/real_analysis/definitions/geometric_series_test/) given in Example 2.7.5, the above series converges if and only if $\left| \frac{1}{2^{p - 1}} \right| < 1$. Solving for $p$ we find



$$
\begin{aligned}
\frac{1}{2^{p - 1}} & > 1 \\
\log\left. \left( 2^{p - 1} \right) \right. & > \log\left. (1) \right. \\
\left. (p - 1) \right.\log\left. (2) \right. & > 0 \\
p\log\left. (2) \right. - \log\left. (2) \right. & > 0 \\
p\log\left. (2) \right. & > \log\left. (2) \right. \\
p & > \frac{\log\left. (2) \right.}{\log\left. (2) \right.} \\
p & > 1
\end{aligned}
$$



## Exercise 2.7.7

### (a)

> Show that if $a_{n} > 0$ and $\lim\left. \left( na_{n} \right) \right. = l$ with $l \neq 0$, then the series $\sum a_{n}$ diverges.

If $\lim\limits_{n \rightarrow \infty}\left. \left( na_{n} \right) \right. = l$ and $a_{n} > 0$, it follows that $l \geq 0$. But by hypothesis, $l \neq 0$, hence $l > 0$. Let $\epsilon = \frac{l}{2}$. There exists an $N \in \mathbb{N}$ such that $n \geq N$ implies that $\left| na_{n} - l \right| < \frac{l}{2}$.

Hence $- \frac{l}{2} < na_{n} - l < \frac{l}{2}$, where some algebra shows that $\frac{l}{2} < na_{n}$ and hence that $a_{n} > \frac{l/2}{n}$. Since $\sum_{n = 1}^{\infty}\frac{1}{n}$ diverges, it follows that $\sum_{n = 1}^{\infty}\frac{l/2}{n}$ diverges as well. Since for all $n \geq N$, the terms of $\sum_{n = 1}^{\infty}a_{n}$ are larger than the terms of $\sum_{n = 1}^{\infty}\frac{l/2}{n}$, it follows from part (ii) of the [Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/) that $\sum_{n = 1}^{\infty}a_{n}$ diverges.

### (b)

> Assume $a_{n} > 0$ and $\lim\left. \left( n^{2}a_{n} \right) \right.$ exists. Show that $\sum a_{n}$ converges.

Let $\epsilon = \frac{l}{2}$. There exists an $N \in \mathbb{N}$ such that $n \geq N$ implies that $\left| n^{2}a_{n} - l \right| < \frac{l}{2}$.

Hence $- \frac{l}{2} < n^{2}a_{n} - l < \frac{l}{2}$, where some algebra shows that $\frac{l}{2} < n^{2}a_{n}$ and hence that $a_{n} > \frac{l/2}{n^{2}}$. Since $\sum_{n = 1}^{\infty}\frac{1}{n^{2}}$ converges, it follows that $\sum_{n = 1}^{\infty}\frac{l/2}{n^{2}}$ converges as well. Since for all $n \geq N$, the terms of $\sum_{n = 1}^{\infty}a_{n}$ are larger than the terms of $\sum_{n = 1}^{\infty}\frac{l/2}{n^{2}}$, it follows from part (i) of the [Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/) that $\sum_{n = 1}^{\infty}a_{n}$ converges.

## Exercise 2.7.9 ([Ratio_Test](/notes/areas/mathematics/real_analysis/definitions/ratio_test/))

> Given a series $\sum_{n = 1}^{\infty}a_{n}$ with $a_{n} \neq 0$, the [Ratio_Test](/notes/areas/mathematics/real_analysis/definitions/ratio_test/) states that if $\left. \left( a_{n} \right) \right.$ satisfies
>
> 

$$
\lim\left| \frac{a_{n + 1}}{a_{n}} \right| = r < 1
$$


>
> then the series converges absolutely.

### (a)

> Let $r'$ satisfy $r < r' < 1$. Explain why there exists an $N$ such that $n \geq N$ implies $\left| a_{n + 1} \right| \leq \left| a_{n} \right|r'$.

### (b)

> Why does $\left| a_{N} \right|\sum\left. (r') \right.^{n}$ converge?

### (c)

> Now, show that $\sum\left| a_{n} \right|$ converges, and conclude that $\sum a_{n}$ converges.

## Exercise 2.7.11

> Find examples of two series $\sum a_{n}$ and $\sum b_{n}$ both of which diverge but for which $\sum\min\{ a_{n},b_{n}\}$ converges. To make it more challenging, produce examples where $\left. \left( a_{n} \right) \right.$ and $\left. \left( b_{n} \right) \right.$ are strictly positive and decreasing.

## Exercise 2.7.12 (Summation-by-parts)

> Let $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ be [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s, let $s_{n} = x_{1} + x_{2} + \cdots + x_{n}$ and set $s_{0} = 0$. Use the observation that $x_{j} = s_{j} - s_{j - 1}$ to verify the formula
>
> 

$$
\sum_{j = m}^{n}x_{j}y_{j} = s_{n}y_{n + 1} - s_{m - 1}y_{m} + \sum_{j = m}^{n}s_{j}\left. \left( y_{j} - y_{j + 1} \right) \right.
$$



Starting with the right-hand side of the above formula, we have



$$
\begin{aligned}
s_{n}y_{n + 1} - s_{m - 1}y_{m} + \sum_{j = m}^{n}s_{j}\left. \left( y_{j} - y_{j + 1} \right) \right. & = s_{n}y_{n + 1} - s_{m - 1}y_{m} + \sum_{j = m}^{n}s_{j}y_{j} - s_{j}y_{j + 1} \\
 & = \left. \left( x_{1} + \cdots + x_{n} \right) \right.y_{n + 1} - \left. \left( x_{1} + \cdots x_{m - 1} \right) \right.y_{m} \\
 & + \left. \left( x_{1} + \cdots + x_{m} \right) \right.y_{m} - \left. \left( x_{1} + \cdots + x_{m} \right) \right.y_{m + 1} \\
 & + \left. \left( x_{1} + \cdots + x_{m} + x_{m + 1} \right) \right.y_{m + 1} - \left. \left( x_{1} + \cdots + x_{m} + x_{m + 1} \right) \right.y_{m + 2} \\
 & \vdots \\
 & + \left. \left( x_{1} + \cdots + x_{n - 2} \right) \right.y_{n - 2} - \left. \left( x_{1} + \cdots x_{n - 2} \right) \right.y_{n - 1} \\
 & + \left. \left( x_{1} + \cdots + x_{n - 1} \right) \right.y_{n - 1} - \left. \left( x_{1} + \cdots x_{n - 1} \right) \right.y_{n} \\
 & + \left. \left( x_{1} + \cdots + x_{n} \right) \right.y_{n} - \left. \left( x_{1} + \cdots x_{n} \right) \right.y_{n + 1} \\
 & = x_{m + 1}y_{m + 1} + x_{m + 2}y_{m + 2} + \cdots + x_{n}y_{n} \\
 & = \sum_{j = m}^{n}x_{j}y_{j}
\end{aligned}
$$



## Exercise 2.7.13 ([Abel's_Test](/notes/areas/mathematics/real_analysis/definitions/abels_test/))

> [Abel's_Test](/notes/areas/mathematics/real_analysis/definitions/abels_test/) for [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) states that if the series $\sum_{k = 1}^{\infty}x_{k}$ converges, and if $\left. \left( y_{k} \right) \right.$ is a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) satisfying
>
> 

$$
y_{1} \geq y_{2} \geq y_{3} \geq \cdots \geq 0
$$


>
> then the series $\sum_{k = 1}^{\infty}x_{k}y_{k}$ converges.

### (a)

> Use Exercise 2.7.12 to show that
>
> 

$$
\sum_{k = 1}^{n}x_{k}y_{k} = s_{n}y_{n + 1} + \sum_{k = 1}^{n}s_{k}\left. \left( y_{k} - y_{k + 1} \right) \right.
$$


>
> where $s_{n} = x_{1} + x_{2} + \cdots x_{n}$.

Let $s_{n} = \sum_{k = 1}^{n}x_{k}$. By hypothesis, $\left. \left( s_{n} \right) \right.$ converges to a limit $L$. Among other things, this implies that there exists $M > 0$ satisfying $\left| s_{n} \right| \leq M$ for all $n \in \mathbb{N}$.

For each $n \in \mathbb{N}$, Exercise 2.7.12 implies that



$$
\sum_{k = 1}^{n}x_{k}y_{k} = s_{n}y_{n + 1} + \sum_{k = 1}^{n}s_{k}\left. \left( y_{k} - y_{k + 1} \right) \right.
$$



### (b)

> Use the [Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/) to argue that $\sum_{k = 1}^{\infty}s_{k}\left. \left( y_{k} - y_{k + 1} \right) \right.$ converges absolutely, and show how that leads directly to a proof of [Abel's_Test](/notes/areas/mathematics/real_analysis/definitions/abels_test/).

We would like to take the limit across the result in part (a) as $n \rightarrow \infty$. We know that $\left. \left( s_{n} \right) \right.$ and $\left. \left( y_{n + 1} \right) \right.$ both converge, but what about the sum? Using a telescoping argument we can show that it converges absolutely. More precisely, observe that



$$
\begin{aligned}
\sum_{k = 1}^{n}\left| s_{k}(y_{k} - y_{k + 1} \right| & \leq \sum_{k = 1}^{n}M\left. \left( y_{k} - y_{k + 1} \right) \right. \\
 & = M\left. \left( y_{1} - y_{n + 1} \right) \right.
\end{aligned}
$$



and $\left. \left( y_{n + 1} \right) \right.$ converges as $n \rightarrow \infty$. This proves that $\sum_{k = 1}^{n}s_{k}\left. \left( y_{k} - y_{k + 1} \right) \right.$ converges absolutely. Applying the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/) to the result in part (a) gives the result.

# Section 3.2 Exercises

## Exercise 3.2.1

### (a)

> Where in the proof of Theorem 3.2.3 part (ii) does the assumption that the collection of [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s be *finite* get used?

We cannot always take minimums of ininfite sets. Thus the step where we let $\epsilon = \min\{(\epsilon)_{1},(\epsilon)_{2},\ldots,(\epsilon)_{n}\} > 0$ requires that we are working with a finite collection of [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s. We can, however, take the [infimum](/notes/areas/mathematics/real_analysis/definitions/infimum/) of an infinite set, but the [infimum](/notes/areas/mathematics/real_analysis/definitions/infimum/) of the set could be 0.

### (b)

> Give an example of a [countable](/notes/areas/mathematics/set_theory/definitions/countable/) collection of [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s $\{ O_{1},O_{2},O_{3},\ldots\}$ whose intersection $\bigcup_{n = 1}^{\infty}O_{n}$ is closed, not empty, and not all of $\mathbb{R}$.

Let $O_{n} = \left. \left( - \frac{1}{n},\frac{1}{n} \right) \right.$. Then $\bigcap_{n = 1}^{\infty}O_{n} = \varnothing$.

## Exercise 3.2.3

> Decide whether the following sets are open, closed, or neither. If a set is not open, find a point in the set for which there is no $\epsilon$-neighborhood contained in the set. If a set is not closed, find a limit point that is not contained in the set.

### (a)

> $\mathbb{Q}$.

Neither. Let's check the definitions to see why:

$\mathbb{Q}$ is open in $\mathbb{R}$ if for all $x \in \mathbb{Q}$ there exists an $\epsilon$-neighborhood $V_{\epsilon}\left. (x) \right. \subseteq \mathbb{Q}$. This is not the case for any rational $x$ because every open interval contains irrational numbers. So $\mathbb{Q}$ is not open.

But neither is $\mathbb{Q}$ closed. $\mathbb{Q}$ is closed if $\mathbb{R}\backslash\mathbb{Q}$ is open. This is also not the case because the $\epsilon$-neighborhood always contains rational numbers too.

In general, for some set $S$, if every open interval contains elements of $S$ and $\mathbb{R} - S$, then $S$ is neither open nor closed.

### (b)

> $\mathbb{N}$.

$\mathbb{N}$ is closed. Given any point in $\mathbb{N}$, there is no $\epsilon$-neighborhood of that point contained in the set.

Said differently, the set $\mathbb{N}^{c}$ is equivalent to $\mathbb{R}\backslash\mathbb{N} = \left. ( - \infty,1) \right. \cup \left. (1,2) \right. \cup \left. (2,3) \right. \cup \cdots \cup \left. (n - 1,n) \right.$, which is a union of [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s, which by Theorem 3.2.3(i), must be open. Therefore, by Theorem 3.2.13, $\mathbb{N}$ must be closed.

### (c)

> $\{ x \in \mathbb{R}:x \neq 0\}$.

Open. The [limit point](/notes/areas/mathematics/topology/definitions/limit_point/) 0 is not contained in the set $\{ x \in \mathbb{R}:x \neq 0\}$.

### (d)

> $\left. \left\{ 1 + \frac{1}{4} + \frac{1}{9} + \cdots + \frac{1}{n^{2}}:n \in \mathbb{N} \right\} \right.$

Neither. None of the points in this set have $\epsilon$-neighborhoods contained in the set. The set is not closed because the series $\sum\frac{1}{n^{2}}$ converges to some finite limit, and this limit is not an element of the set.

### (e)

> $\left. \left\{ 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}:x \in \mathbb{N} \right\} \right.$

Closed. There is no $\epsilon$-neighborhood of any point in the set that is contained in the set. Because the series $\sum\frac{1}{n}$ diverges, this particular [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of points does not have a limit in $\mathbb{R}$, and a set that does not have any limit points is necessarily vacuously closed.

## Exercise 3.2.4

> Let $A$ be non-empty and bounded above so that $s = \sup A$ exists.

### (a)

> Show that $s \in \overline{A}$.

Let $A$ be bounded above and let $s = \sup A$ which exists by the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/). Then we need to show that $s \in \overline{A} = A \cup L$, where $L$ is the set of limit points of $A$. Since $s$ can either be in $A$ or not in $A$, we examine each case separately:

If $s \in A$, then clearly $s \in \overline{A}$.

If $s \notin A$, then we will show that $s$ is a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/). Let $\epsilon > 0$ be arbitrary. Then, by the characterization of [supremum](/notes/areas/mathematics/real_analysis/definitions/supremum/), there exists an $a \in A$ such that $s - \epsilon < a$. Since $s \notin A$, we have $a \neq s$ and hence $V_{\epsilon}\left. (s) \right.j$ intersects $A$ in a point that is not $s$. Therefore, $s$ is a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/) of $A$ and hence $s \in \overline{A}$.

### (b)

> Can an [open_set](/notes/areas/mathematics/topology/definitions/open_set/) contain its [supremum](/notes/areas/mathematics/real_analysis/definitions/supremum/)?

No. Let $U$ be an [open_set](/notes/areas/mathematics/topology/definitions/open_set/) in $\mathbb{R}$ that is non-empty and bounded above. Then $s = \sup U$ exists. If $s \in U$, then because $U$ is open, there exists some $\epsilon > 0$ such that $V_{\epsilon\left. (s) \right.} \subseteq U$. However, $s < s + \epsilon/2$, yet $s + \epsilon/2$ is contained in $V_{\epsilon}\left. (s) \right.$ and therefore in $U$ contradicting that $s$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $U$. Therefore, $s \notin U$.

## Exercise 3.2.5

> Prove Theorem 3.2.8.

Restating Theorem 3.2.8:

> A set $F \subseteq \mathbb{R}$ is closed *if and only if* every [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/) contained in $F$ has a limit that is also an element of $F$.

$\left. ( \Rightarrow ) \right.$: Assume that the set $F \subseteq \mathbb{R}$ is closed. Then $F$ contains its limit points. We will show that that every [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/) $\left. \left( a_{n} \right) \right.$ contained in $F$ has its limit in $F$ by showing that the limit of $\left. \left( a_{N} \right) \right.$ is either a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/) or possibly an [isolated point](/notes/areas/mathematics/topology/definitions/isolated_point/) of $F$. Because $\left. \left( a_{n} \right) \right.$ is Cauchy, we know $x = lima_{n}$ exists. If $a_{n} \neq x$ for all $x$, then it follows from Theorem 3.2.5 that $x$ is a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/) of $F$. Now consider a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/) an where $a_{n} = x$ for some $n$. Because $\left. \left( a_{n} \right) \right. \subseteq F$ it follows that $x \in F$ as well. (Note that if $a_{n}$ is eventually equal to $x$, then it may not be true that $x$ is a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/) of $F$.)

$\left. ( \Leftarrow ) \right.$: Assume that every [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/) contained in $F$ has a limit that is also an element of $F$. To show that $F$ is closed we want to show that it contains its limit points. Let $x$ be a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/) of $F$. By Theorem 3.2.5, $x = lima_{n}$ for some [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( a_{n} \right) \right.$. Because $\left. \left( a_{n} \right) \right.$ converges, it must be a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/). So $x$ is contained in $F$, and therefore $F$ is closed.

## Exercise 3.2.6

> Decide whether the following statements are true or false. Provide counterexamples for those that are false, and supply proofs for those that are true.

### (d)

> The Cantor set is closed.

True. As the number of iterations of the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/) approaches infinity, we remove the union of all open middle-third intervals, and the union of an arbitrary collection of [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s is open by Theorem 3.2.3.

Then, by Theorem 3.2.13, the complement of what is left after removing all of these intervals, which is the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/), must be closed.

# Section 3.3 Exercises

## Exercise 3.3.1

> Show that if $K$ is compact and non-empty, then $\sup K$ and $\inf K$ both exist and are elements of $K$.

By Theorem 3.3.8 ([Heine-Borel_Theorem](/notes/areas/mathematics/real_analysis/definitions/heine-borel_theorem/)), we know that if $K$ is compact then it is also closed and bounded.

Then, by the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/), we know that every non-empty set of real numbers that is bounded above has a least upper bound, so we know that $\sup K$ exists.

Then, by Exercise 3.2.4, we know that $\sup K \in \overline{K}$. Since $K$ is closed, $K = \overline{K}$ and thus $\sup K \in K$.

A similar argument can be made for $\inf K \in K$.

## Exercise 3.3.3

> Prove the converse of Theorem 3.3.4 by showing that if a set $K \subseteq \mathbb{R}$ is closed and bounded, then it is compact.

Let $K$ be closed and bounded. Show $K$ is compact.

Since $K$ is closed, $K$ contains its limit points. Since $K$ is bounded, there exists an $M > 0$ such that $|k| \leq M$ for all $k \in K$, i.e. $k \in \left. \lbrack - M,M\rbrack \right.$.

Now, let $\left. \left( x_{n} \right) \right.$ be a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) in $K$. Then, since $K$ is bounded, the [Bolzano-Weierstrass_Theorem](/notes/areas/mathematics/real_analysis/definitions/bolzano-weierstrass_theorem/) guarantees a convergent [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) $\left. \left( x_{n_{k}} \right) \right.$, and since $K$ is also closed, we know that $K$ contains its limit points and thus the limit of $\left. \left( x_{n_{k}} \right) \right.$ is also in $K$. Thus, $K$ is compact.

## Exercise 3.3.5

> Decide whether the following propositions are true or false. If the claim is valid, supply a short proof, and if the claim is false, provide a counterexample.

### (a)

> The arbitrary intersection of compact sets is compact.

True. Let $\mathcal{G}$ be a collection of compact sets. We will show that $\bigcap_{A \in \mathcal{G}}A$ is compact. Note that every $A \in \mathcal{G}$ is compact, and thus is also closed and bounded by the [Heine-Borel_Theorem](/notes/areas/mathematics/real_analysis/definitions/heine-borel_theorem/). Since the intersection of arbitrarily many closed sets is closed, $\bigcap_{A \in \mathcal{G}}A$ is also closed. Now, chose any $A' \in \mathcal{G}$. Since $\bigcap_{A \in \mathcal{G}}A \subset A'$ and $A'$ is bounded, then $\bigcap_{A \in \mathcal{G}}A$ is bounded. Thus, $\bigcap_{A \in \mathcal{G}}A$ is closed and bounded; thus is it compact.

### (b)

> The arbitrary union of compact sets is compact.

False. The union of the compact sets $\left. \lbrack 1/n,2\rbrack \right.$ over all $n \in \mathbb{N}$ is equal to $(0,2\rbrack$ which is not closed and thus not compact. The union of the compact sets $\left. \lbrack n,n + 1\rbrack \right.$ over all $n \in \mathbb{N}$ is the unbounded set $\lbrack 1,\infty)$.

### (c)

> Let $A$ be arbitrary, and let $K$ be compact. Then, the intersection of $A \cap K$ is compact.

False. Take $A = \left. (0,1) \right.$ and $K = \left. \lbrack 0,1\rbrack \right.$. Then $A \cap K = \left. (0,1) \right.$ is not compact.

### (d)

> If $F_{1} \supseteq F_{2} \supseteq F_{3} \supseteq F_{4} \supseteq \cdots$ is a nested [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of nonempty closed sets, then the intersection $\bigcap_{n = 1}^{\infty}F_{n} \neq \varnothing$

False. Let $F_{n} = \lbrack n,\infty)$. Then $F_{n}$ is closed for all $n$, but the intersection of these sets is empty.

## Exercise 3.3.7

> As some more evidence of the surprising nature of the Cantor set, follow these steps to show that the sum $C + C = \{ x + y:x,y \in C\}$ is equal to the closed interval $\left. \lbrack 0,2\rbrack \right.$. (Keep in mind that $C$ has zero length and contains no intervals.)
>
> Because $C \subseteq \left. \lbrack 0,1\rbrack \right.,C + C \subseteq \left. \lbrack 0,2\rbrack \right.$, so we only need to prove the reverse inclusion $\left. \lbrack 0,2\rbrack \right. \subseteq \{ x + y:x,y \in C\}$. Thus, given $s \in \left. \lbrack 0,2\rbrack \right.$, we must find two elements $x,y \in C$ satisfying $x + y = s$.

### (a)

> Show that there exist $x_{1},y_{1} \in C_{1}$ for which $x_{1} + y_{1} = s$. Show in general that, for an arbitrary $n \in \mathbb{N}$, we can always find $x_{n},y_{n} \in C_{n}$ for which $x_{n} + y_{n} = s$.

Let $s \in \left. \lbrack 0,2\rbrack \right.$. We need to find an $x_{1},y_{1} \in C_{1}$ such that $x_{1} + y_{1} = s$. We know that $C_{1} = \left. \lbrack 0,1/3\rbrack \right. \cup \left. \lbrack 2/3,1\rbrack \right.$. Then we have that



$$
\left. \lbrack 0,1/3\rbrack \right. + \left. \lbrack 0,1/3\rbrack \right. = \left. \lbrack 0,2/3\rbrack \right.
$$





$$
\left. \lbrack 0,1/3\rbrack \right. + \left. \lbrack 2/3,1\rbrack \right. = \left. \lbrack 2/3,4/3\rbrack \right.
$$





$$
\left. \lbrack 2/3,1\rbrack \right. + \left. \lbrack 2/3,1\rbrack \right. = \left. \lbrack 4/3,1\rbrack \right.
$$



So, $C_{1} + C_{1} = \left. \lbrack 0,2/3\rbrack \right. \cup \left. \lbrack 2/3,4/3\rbrack \right. \cup \left. \lbrack 4/3,2\rbrack \right. = \left. \lbrack 0,2\rbrack \right.$, so for any $s \in \left. \lbrack 0,2\rbrack \right.$, we can find an $x_{1},y_{1} \in C_{1}$ such that $x_{1} + y_{1} = s$

A way to visualize this (see below) result in the $\left. (x,y) \right.$-plane is to shade in the four squares corresponding to the components of $C_{1} \times C_{1}$. This is the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/) in two dimensions, or what is called the Sierpinski carpet. It is constructed by removing the middle third of the unit square in both the $x$ and $y$ directions.

For each $s \in \left. \lbrack 0,2\rbrack \right.$, the line $x + y = s$ must intersect at least one of the squares. For each $n$, we can draw a similar picture (with increasing numbers of smaller squares), and our job is to argue that the line $x + y = s$ continues to intersect at least one of the smaller squares.

To argue by indiction, suppose that we can find $x_{n},y_{n} \in C_{n}$ such that $x_{n} + y_{n} = s$. To show that this must hold for $n + 1$, let's focus attention on a square from the $n$th stage where $x_{n} + y_{n} = s$ holds (i.e., where $x + y = s$ intersects an $n$th stage square). Moving to the $\left. (n + 1) \right.$th stage means removing the open middle third of this shaded region. But this results in a situation precisely like the one in Figure 3.1, implying that the line $x + y = s$ must intersect a $\left. (n + 1) \right.$st stage square. This shows that there exist $x_{n + 1},y_{n + 1} \in C_{n + 1}$ where $x_{n + 1} + y_{n + 1} = s$.

![](/images/notes/Areas/mathematics/Real_Analysis/books/graphics/UA/3.3.7a.png)

### (b)

> Keeping mind that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ do not necessarily converge, show how they can nevertheless be used to produce the desired $x$ and $y$ in $C$ satisfying $x + y = s$.

We have $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ with $x_{n},y_{n} \in C_{n}$ and $x_{n} + y_{n} = s$ for all $n$. The [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right.$ doesn't converge, but $\left. \left( x_{n} \right) \right.$ is bounded so by the [Bolzano-Weierstrass_Theorem](/notes/areas/mathematics/real_analysis/definitions/bolzano-weierstrass_theorem/) there exists a convergent [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) $\left. \left( x_{n_{k}} \right) \right.$. Set $x = \lim x_{n_{k}}$. Now look at the corresponding [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) $\left. \left( y_{n_{k}} \right) \right. = s - x_{n_{k}}$. Using the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/), we see that this [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) converges to $y = \lim\left. \left( x - x_{n_{k}} \right) \right. = s - x$. This shows that $x + y = s$. We now need to argue that $x,y \in C$.

One temptation is to say that because $C$ is closed, $x = \lim\left. \left( x_{n_{k}} \right) \right.$ must be in $C$. However, we don't know (and it probably isn't true) that $\left. \left( x_{n_{k}} \right) \right.$ is in $C$. We *can* say that $\left. \left( x_{n_{k}} \right) \right.$ is in $C_{1}$, and because $C_{1}$ is closed we may conclude that $x \in C_{1}$. In fact, given any fixed $n_{0}$, we can argue that $x \in C_{n_{0}}$ because $x_{n_{k}}$ is (with the exception of some finite number of terms) contained in $C_{n_{0}}$. This implies that $x \in \bigcap_{n = 1}^{\infty}C_{n} = C$ as desired, and a similar argument works for $y$.

## Exercise 3.3.9

> Follow these seteps to prove the final implication in Theorem 3.3.8. Assume $K$ satisfies (i) and (ii), and let $\{ O_{\lambda}:\lambda \in \Lambda\}$ be an open cover for $K$. For contradiction, let's assume that no finite subcover exists. Let $I_{0}$ be a closed interval containing $K$.

Restating Theorem 3.3.8 - [Heine-Borel_Theorem](/notes/areas/mathematics/real_analysis/definitions/heine-borel_theorem/)

> Let $K$ be a subset of $\mathbb{R}$. All of the following statements are equivalent in the sense that any one of them implies the two others:
>
> 1.  $K$ is compact.
>
> 2.  $K$ is closed and bounded.
>
> 3.  Every open cover for $K$ has a finite subcover.

### (a)

> Show that there exists a nested [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of closed intervals $I_{0} \supseteq I_{1} \supseteq I_{2} \supseteq \cdots$ with the property that, for each $n,I_{n} \cap K$ cannot be finitely covered and $\lim\left| I_{n} \right| = 0$.

This is a standard bisection argument. Bisect $I_{0}$ into two halves $A_{1}$ and $B_{1}$. If $A_{1} \cap K$ and $B_{1} \cap K$ both had finite subcovers consisting of sets from the collection $\{ O_{\lambda}:\lambda \in \Lambda\}$, then there would exist a finite subcover for $K$. But we assumed that such a finite subcover did not exist for $K$. Hence either $A_{1} \cap K$ or $B_{1} \cap K$ (or both) has no finite subcover.

Let $I_{1}$ be a half of $I_{0}$ whose intersection with $K$ does not have a finite subcover, so that $I_{1} \cap K$ cannot be finitely covered and $I_{1} \subseteq I_{0}$. Then bisect $I_{1}$ into two closed intervals, $A_{2}$ and $B_{2}$ and again let $I_{2} = A_{2}$ if $A_{2} \cap K$ does not have a finite subcover. Otherwise, let $I_{2} = B_{2}$. Continuing this process of bisecting the interval $I_{n}$, we get the desired [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $I_{n}$ with $\lim\left| I_{n} \right| = 0$

### (b)

> Argue that there exists an $x \in K$ such that $x \in I_{n}$ for all $n$.

Because $K$ is compact, $K \cap I_{n}$ is also compact for each $n \in \mathbb{N}$. By the [Nested_Compact_Set_Property](/notes/areas/mathematics/real_analysis/definitions/nested_compact_set_property/), $\bigcap_{n = 1}^{\infty}I_{n} \cap K$ is non-empty, and there exists an $x \in K \cap I_{n}$ for all $n$.

### (c)

> Because $x \in K$, there must exist an [open_set](/notes/areas/mathematics/topology/definitions/open_set/) $O_{\lambda_{0}}$ from the original collection that contains $x$ as an element. Explain how this leads to the desired contradiction.

Let $x \in K$ and let $O_{\lambda_{0}}$ be an [open_set](/notes/areas/mathematics/topology/definitions/open_set/) that contains $x$. Because $O_{\lambda_{0}}$ is open, there exists $(\epsilon)_{0} > 0$ such that ${V_{\epsilon}}_{0}\left. (x) \right. \subseteq O_{\lambda_{0}}$. Now choose $n_{0}$ such that $|I_{n_{0}} < (\epsilon)_{0}$. Then $I_{n_{0}}$ is contained in the single [open_set](/notes/areas/mathematics/topology/definitions/open_set/) $O_{\lambda_{0}}$ and thus it has a finite subcover. This contradiction implies that $K$ must have originally had a finite subcover.

## Exercise 3.3.11

> Consider each of the sets listed in Exercise 3.3.2. For each one that is not compact, find an open cover for which there is no finite subcover.

### (a)

> $\mathbb{N}$

Let $O_{\lambda} = \left. (\lambda - 1,\lambda + 1) \right.$ where $\lambda \in \mathbb{N}$. This open cover has no finite subcover.

> $\mathbb{Q} \cap \left. \lbrack 0,1\rbrack \right.$

Let $\alpha$ be a fixed irrational number in the interval $\left. (0,1) \right.$. For each $n \in \mathbb{N}$ set $O_{n} = \left. ( - 1,\alpha - 1/n) \right. \cup \left. (\alpha + 1/n,2) \right.$ The union over $n$ of all of these sets gives $\left. ( - 1,\alpha) \right. \cup \left. (\alpha,2) \right.$, which contains $\mathbb{Q} \cap \left. \lbrack 0,1\rbrack \right.$. This cover has no finite subcover.

### (c)

> The Cantor set.

The [cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/) is compact.

### (d)

> $\{ 1 + 1/2^{2} + 1/3^{2} + \cdots + 1/n^{2}:n \in \mathbb{N}\}$

For each point $s_{n} = 1 + 1/2^{2} + 1/3^{2} + \cdots + 1/n^{2}$ in the set, let $O_{n} = \left. \left( s_{n} - 1/\left. (n + 1) \right.^{2},s_{n} + 1/\left. (1 + n) \right.^{2} \right) \right.$. This open cover has no finite subcover.

> $\{ 1,1/2,2/3,3/4,4/5,\ldots\}$

This set is compact.

## Exercise 3.3.13

> Let's call a set *clompact* if it has the property that every closed cover (i.e., a cover consisting of closed sets) admits a finite subcover. Describe all of the clompact subsets of $\mathbb{R}$.

If $A$ is a finite set then it is clearly clompact. Conversely, assume $A$ is compact. Because a singleton set is a [closed set](/notes/areas/mathematics/topology/definitions/closed_set/), the collection of singleton sets consisting of the elements of $A$ is a closed cover. This cover must have a finite subcover, and it follows that $A$ is a finite set. To summarize, a set is clompact if and only if it is finite.

# Section 3.4 Exercises

## Exercise 3.4.1

> If $P$ is a perfect set and $K$ is compact, is the intersection $P \cap K$ always compact? Is it always perfect?

If $P$ is perfect, then it is closed and contains no isolated points. If $K$ is compact, then it is closed and bounded.

By Theorem 3.2.4 (the intersection of an arbitrary collection of closed sets is closed), then $P \cap K$ is closed. Since $P \cap K \subseteq K$, and since $K$ is bounded, $P \cap K$ is also bounded.

However, $P \cap K$ is not necessarily perfect. For example, let $K$ be a singleton set contained in $P$. Then $P \cap K$ is a singleton set and is not perfect.

## Exercise 3.4.2

> Does there exist a perfect set consisting of only rational numbers?

No. By Theorem 1.5.6, the set $\mathbb{Q}$ is [countable](/notes/areas/mathematics/set_theory/definitions/countable/). Then, by Theorem 3.4.3, no such set consisting of only rational numbers is perfect.

## Exercise 3.4.3

> Review the portion of the proof given for Theorem 3.4.2 and follow these steps to complete the argument

### (a)

> Because $x \in C_{1}$, argue that there exists an $x_{1} \in C \cap C_{1}$ with $x_{1} \neq x$ satisfying $\left| x - x_{1} \right| \leq 1/3$

### (b)

> Finish the proof by showing that for each $n \in \mathbb{N}$, there exists $x_{n} \in C \cap C_{n}$ different from $x$ satisfying $\left| x - x_{n} \right| \leq 1/3^{n}$.

## Exercise 3.4.4

> Repeat the Cantor construction from Section 3.1 starting with the interval $\left. \lbrack 0,1\rbrack \right.$. This time, however, remove the open middle *fourth* from each component.

### (a)

> Is the resulting set compact?

### (b)

> Using the algorithms from Section 3.1, compute the length and dimension of this Cantor-like set.

See: <https://arxiv.org/pdf/1411.7110.pdf>

Let us denote the middle fourths set as $C^{1/4}$

At step 0, we have $C_{0}^{1/4} = \left. \lbrack 0,1\rbrack \right.$. At step 1, we have $C_{1}^{1/4} = \left. \lbrack 0,3/8\rbrack \right. \cup \left. \lbrack 5/8,1\rbrack \right.$. At step 2, we have $C_{2}^{1/4} = \left. \lbrack 0,9/64\rbrack \right. \cup \left. \lbrack 15/64,3/8\rbrack \right. \cup \left. \lbrack 5/8,49/64\rbrack \right. \cup \left. \lbrack 55/64,1\rbrack \right.$, and so on.

Its length can be obtained by subtracting from 1 the sum of the length of all of the open intervals



$$
\begin{aligned}
1 - \left. \left\lbrack 2^{0}\frac{1}{4} - 2^{1}\frac{3}{32} - 2^{2}\frac{9}{256} + \cdots \right\rbrack \right. & = 1 - \frac{1}{4}\left. \left\lbrack 1 + \frac{3}{4} - \frac{9}{16} + \cdots \right\rbrack \right. \\
 & = 1 - \frac{1}{4}\frac{1}{1 - \frac{3}{4}} \\
 & = 1 - \frac{1}{4}\frac{\frac{1}{1}}{4} \\
 & = 1 - 1 \\
 & = 0
\end{aligned}
$$



The [fractal_dimension](/notes/areas/mathematics/real_analysis/definitions/fractal_dimension/) is $\frac{\log 2}{\log 8/3}$.

## Exercise 3.4.5

> Let $A$ and $B$ be non-empty subsets of $\mathbb{R}$. Show that if there exist disjoint [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s $U$ and $V$ with $A \subseteq U$ and $B \subseteq V$, then $A$ and $B$ are separated.

## Exercise 3.4.6

> Prove Theorem 3.4.6

## Exercise 3.4.7

> A set $E$ is *totally disconnected* if, given any two distinct points $x,y \in E$, there exist separated sets $A$ and $B$ with $x \in A$, $y \in B$, and $E = A \cup B$.

### (a)

> Show that $\mathbb{Q}$ is totally disconnected

Given any $x,y \in \mathbb{Q}$, choose $z \in \mathbb{I}$ such that $x < z < y$. We know that such a $z$ exists because the irrational numbers are dense. Then let $\mathbb{Q} = A \cup B$, where $A = \mathbb{Q} \cap \left. ( - \infty,z) \right.$ and $B\mathbb{Q} \cap \left. (z,\infty) \right.$. The sets $A$ and $B$ are separated (see Example 3.4.5(ii)), and $x \in A$ and $y \in B$.

### (b)

> Is the set of irrational numbers totally disconnected?

The set of irrational numbers is totally disconnected because the rational numbers are also dense in $\mathbb{R}$. Thus we can follow the same argument as in part (a) by letting $x,y \in \mathbb{I}$ and choosing $z \in \mathbb{Q}$.

## Exercise 3.4.8

> Follow these steps to show that the Cantor set is totally disconnected in the sense described in Exercise 3.4.7.
>
> Let $C = \bigcap_{n = 0}^{\infty}C_{n}$ as defined in Section 3.1.

### (a)

> Given $x,c \in C$, with $x < y$, set $\epsilon = y - x$. For each $n = 0,1,2,\ldots$, the set $C_{n}$ consists of a finite number of closed intervals. Explain why there must exist an $N$ large enough so that it is impossible for $x$ and $y$ both to belong to the same closed interval of $C_{N}$.

### (b)

> Show that $C$ is totally disconnected.

## Exercise 3.4.9

> Let $\{ r_{1},r_{2},r_{3},\ldots\}$ be an enumeration of the rational numbers, and for each $n \in \mathbb{N}$, set $(\epsilon)_{n} = 1/2^{n}$. Define $O = \bigcup_{n = 1}^{\infty}V_{(\epsilon)_{n}}\left. \left( r_{n} \right) \right.$, and let $F = O^{c}$.

### (a)

> Argue that $F$ is a closed, non-empty set consisting only of irrational numbers

### (b)

> Does $F$ contain any non-empty open intervals? Is $F$ totally disconnected? (See Exercise 3.4.7) for the definition.)

### (c)

> Is it possible to know whether $F$ is perfect? If not, can we modify this construction to produce a non-empty perfect set of irrational numbers?

# Section 3.5 Exercises

## Exercise 3.5.1

> Argue that a set $A$ is a $G_{\delta}$ ([G-delta_set](/notes/areas/mathematics/topology/definitions/g-delta_set/)) if and only if its complement is an $F_{\sigma}$ ([F-sigma_set](/notes/areas/mathematics/topology/definitions/f-sigma_set/)).

$\left. ( \Rightarrow ) \right.$ Let $A$ be a $G_{\delta}$ set. We want to show that this implies that $A^{c}$ is an $F_{\sigma}$ set. By the definition of a $G_{\delta}$ set, A can be written as the [countable](/notes/areas/mathematics/set_theory/definitions/countable/) intersection of [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s. In symbols, $A = \bigcap_{n = 1}^{\infty}O_{n}$ where $O_{n}$ is open for each $n \in \mathbb{N}$. Then by De Morgan's Law, $A^{c} = \bigcup_{n = 1}^{\infty}O_{n}^{c}$. Because $O_{n}$ is open, $O_{n}^{c}$ is closed (Theorem 3.2.13). Hence, $A^{c}$ is the [countable](/notes/areas/mathematics/set_theory/definitions/countable/) union of closed sets, and therefore it is an $F_{\sigma}$ set.

$\left. ( \Leftarrow ) \right.$ Now let $B$ be an $F_{\sigma}$ set. Then we know that $B = \bigcup_{n = 1}^{\infty}F_{n}$ where $F_{n}$ is closed for each $n \in \mathbb{N}$. It then follows from De Morgan's Law that $B^{c} = \bigcap_{n = 1}^{\infty}F_{n}^{c}$. Therefore, $B^{c}$ is the [countable](/notes/areas/mathematics/set_theory/definitions/countable/) intersection of [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s, which makes it a $G_{\delta}$ set.

## Exercise 3.5.2

See: [Finite unions and intersections [F-sigma_set](/notes/areas/mathematics/topology/definitions/f-sigma_set/)s and [G-delta_set](/notes/areas/mathematics/topology/definitions/g-delta_set/)s](https://math.stackexchange.com/questions/290884/finite-unions-and-intersections-f-sigma-and-g-delta-sets)

> Replace each ------ with the word *finite* or *countable*, depending on which is more appropriate

### (a)

The [countable](/notes/areas/mathematics/set_theory/definitions/countable/) union of $F_{\sigma}$ sets is an $F_{\sigma}$ set.

### (b)

The [countable](/notes/areas/mathematics/set_theory/definitions/countable/) intersection of $F_{\sigma}$ sets is an $F_{\sigma}$ set.

### (c)

The finite union of $G_{\delta}$ sets is a $G_{\delta}$ set.

### (d)

The finite intersection of $G_{\delta}$ sets is a $G_{\delta}$ set.

## Exercise 3.5.3

> (This exercise has already appeared as Exercise 3.2.15)

### (a)

> Show that a closed interval $\left. \lbrack a,b\rbrack \right.$ is a $G_{\delta}$ set.

$$
\left. \lbrack a,b\rbrack \right. = \bigcap_{n = 1}^{\infty}\left. \left( a - \frac{1}{n},b + \frac{1}{n} \right) \right.
$$



### (b)

> Show that the half-open interval $(a,b\rbrack$ is both a $G_{\delta}$ and an $F_{\sigma}$ set.

$$
(a,b\rbrack = \bigcap_{n = 1}^{\infty}\left. \left( a,b + \frac{1}{n} \right) \right.
$$



and



$$
(a,b\rbrack = \bigcup_{n = 1}^{\infty}\left. \left\lbrack a + \frac{1}{n},b \right\rbrack \right.
$$



### (c)

> Show that $\mathbb{Q}$ is an $F_{\sigma}$ set, and the set of irrationals $\mathbb{I}$ forms a $G_{\delta}$ set.

Because $\mathbb{Q}$ is [countable](/notes/areas/mathematics/set_theory/definitions/countable/), we can write $\mathbb{Q} = \{ r_{1},r_{2},r_{3},\ldots\}$ . Note that each singleton set $\{ r_{n}\}$ is closed and the complement $\{ r_{n}\}^{c}$ is open. Then $\mathbb{Q} = \bigcup_{n = 1}^{\infty}\{ r_{n}\}$ shows that $\mathbb{Q}$ is an $F_{\sigma}$, and $\mathbb{I} = \mathbb{Q}^{c} = \bigcap_{n = 1}^{\infty}\{ r_{n}\}^{c}$ shows that $\mathbb{I}$ is a $G_{\delta}$ set.

## Exercise 3.5.4

> Starting with $n = 1$, inductively construct a nested [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of *closed* intervals $I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots$ satisfying $I_{n} \subseteq G_{n}$. Give special attention to the issue of the endpoints of each $I_{n}$. Show how this leads to a proof of the theorem.

## Exercise 3.5.5

> Show that it is impossible to write
>
> 

$$
\mathbb{R} = \bigcup_{n = 1}^{\infty}F_{n}
$$


>
> where for each $n \in \mathbb{N}$ $F_{n}$ is a closed set containing no non-empty open intervals.

Let $F$ be a [closed set](/notes/areas/mathematics/topology/definitions/closed_set/) containing no non-empty open intervals. Then $F^{c}$ is open and we claim that it must also be dense in $\mathbb{R}$. To see why, assume, $x,y \in \mathbb{R}$ satisfy $x < y$. By hypothesis, the open interval, $\left. (x,y) \right.$ is *not* contained in $F$ which means there exists a point $z \in F^{c}$ satisfying $x < z < y$. This proves that $F^{c}$ is dense.

Turning to the statement in the exercise, assume for contradiction that $\mathbb{R} = \bigcup_{n = 1}^{\infty}F_{n}$, where each $F_{n}$ is a [closed set](/notes/areas/mathematics/topology/definitions/closed_set/) containing no non-empty open intervals. Taking complements we get $\varnothing = \bigcap_{n = 1}^{\infty}F_{n}^{c}$, and we have just seen that each $F_{c}^{n}$ is a dense [open_set](/notes/areas/mathematics/topology/definitions/open_set/) in $\mathbb{R}$. But this is a contradiction, because the intersection of dense [open_set](/notes/areas/mathematics/topology/definitions/open_set/)s is not empty, as Theorem 3.5.2 states.

## Exercise 3.5.6

> Show how the previous exercise implies that the set $\mathbb{I}$ of irrationals cannot be an $F_{\sigma}$ set, and $\mathbb{Q}$ cannot be a $G_{\delta}$ set.

## Exercise 3.5.7

> Using Exercise 3.5.6 and versions of the statements in Exercise 3.5.2, construct a set that is neither in $F_{\sigma}$ nor $G_{\delta}$.

The set $\left. \left( \mathbb{I} \cap \left. \left( - \infty,0\rbrack \right) \right. \cup \left. \left( \mathbb{Q} \cap \lbrack 0,\infty \right) \right. \right) \right.$ is neither an $F_{\sigma}$ set nor a $G_{\delta}$ set.

## Exercise 3.5.8

> Show that a set $E$ is nowhere-dense in $\mathbb{R}$ if and only if the complement of $\overline{E}$ is dense in $\mathbb{R}$.

## Exercise 3.5.9

> Decide whether the following sets are dense in $\mathbb{R}$, nowhere-dense in $\mathbb{R}$, or somewhere in between.

### (a)

> $A = \mathbb{Q} \cap \left. \lbrack 0,5\rbrack \right.$.

Somewhere in between.

### (b)

> $B = \{ 1/n:n \in \mathbb{N}\}$.

Nowhere-dense.

### (c)

> $\mathbb{I}$.

The irrationals are dense in $\mathbb{R}$. See page 22 of Abbott.

### (d)

> The Cantor set.

Nowhere-dense. By Exercise 3.2.6(d), we know that the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/) is closed.

The [closure](/notes/areas/mathematics/topology/definitions/closure/) of the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/) *is* the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/), for it is closed. The interior of the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/) is empty, thus the [Cantor set](/notes/areas/mathematics/real_analysis/definitions/cantor_set/) is nowhere dense.

## Exercise 3.5.10

> Finish the proof of Theorem 3.5.4 by finding a contradiction to the results in this section.

Restating Theorem 3.5.4:

> ([Baire's_Theorem](/notes/areas/mathematics/real_analysis/definitions/baires_theorem/)): The set of real numbers $\mathbb{R}$ cannot be written as the [countable](/notes/areas/mathematics/set_theory/definitions/countable/) union of nowhere-dense sets.

# Section 4.2 Exercises

## Exercise 4.2.1

### (a)

> Supply the details for how Corollary 4.2.4 part (ii) follows from the [Sequential_Criterion_for_Functional_Limits](/notes/areas/mathematics/real_analysis/definitions/sequential_criterion_for_functional_limits/) in Theorem 4.2.3 and the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/) for [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s proved in Chapter
>
> 2.  

Restating Theorem 2.3.3(ii) ([Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/)):

> Let $\lim a_{n} = a$ and $\lim b_{n} = b$. Then, $\lim\left. \left( a_{n} + b_{n} \right) \right. = a + b$.

Showing that $\lim\limits_{x \rightarrow c}\left. \left\lbrack f\left. (x) \right. + g\left. (x) \right. \right\rbrack \right. = L + M$ is equivalent to showing that $f\left. \left( x_{n} \right) \right. + g\left. \left( x_{n} \right) \right. \rightarrow L + M$ whenever $\left. \left( x_{n} \right) \right. \rightarrow c$. Since we are given that $f\left. \left( x_{n} \right) \right. \rightarrow L$ and $g\left. \left( x_{n} \right) \right. \rightarrow M$, we can use Theorem 2.3.3 part (ii) to conclude that $f\left. \left( x_{n} \right) \right. + g\left. \left( x_{n} \right) \right. \rightarrow L + M$.

### (b)

> Now, write another proof of Corollary 4.2.4 part (ii) directly from Definition 4.2.1 without using the sequential criterion in Theorem 4.2.3.

Restating Definition 4.2.1:

> [functional_limit](/notes/areas/mathematics/real_analysis/definitions/functional_limit/): Let $f:A \rightarrow \mathbb{R}$, and let $c$ be a limit point of the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $A$. We say that $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$ provided that, for all $\epsilon > 0$, there exists a $\delta > 0$ such that whenever $0 < |x - c| < \delta$ (and $x \in A$) it follows that $\left| f\left. (x) \right. - L \right| < \epsilon$.

Let $\epsilon > 0$ be arbitrary. We need to show that there exists a $\delta$ such that $0 < |x - c| < \delta$ implies that $\left| \left. \left( f\left. (x) \right. + g\left. (x) \right. \right) \right. - \left. (L + M) \right. \right| < \epsilon$. Note that



$$
\left| \left. \left( f\left. (x) \right. + g\left. (x) \right. \right) \right. - \left. (L + M) \right. \right| = \left| \left. \left( f\left. (x) \right. - L \right) \right. + \left. \left( g\left. (x) \right. - M \right) \right. \right| \leq \left| f\left. (x) \right. - L \right| + \left| g\left. (x) \right. - M \right|
$$



Since $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$, there exists $\delta_{1}$ such that $0 < |x - c| < \delta_{1}$ implies that $\left| f\left. (x) \right. - L \right| < \epsilon/2$. In addition, because $\lim\limits_{x \rightarrow c}g\left. (x) \right. = M$, there exists a $\delta_{2}$ such that $0 < |x - c| < \delta_{2}$ implies that $\left| g\left. (x) \right. - M \right| < \epsilon/2$. Now if we pick $\delta = \min\{\delta_{1},\delta_{2}\}$ then $0 < |x - c| < \delta$ implies that



$$
\begin{aligned}
|\left. \left( f\left. (x) \right. + g\left. (x) \right. \right) \right. - \left. (L + M) \right. & \leq \left| f\left. (x) \right. - L \right| + \left| g\left. (x) \right. - M \right| \\
 & = < \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
 & = \epsilon
\end{aligned}
$$



### (c)

> Repeat (a) and (b) for Corollary 4.2.4 part (iii).

Showing that $\lim\limits_{x \rightarrow c}\left| f\left. (x) \right.g\left. (x) \right. \right| = LM$ is equivalent to showing that $f\left. \left( x_{n} \right) \right.g\left. \left( x_{n} \right) \right. \rightarrow LM$ whenever $\left. \left( x_{n} \right) \right. \rightarrow c$. Since we are given that $f\left. \left( x_{n} \right) \right. \rightarrow L$ and $g\left. \left( x_{n} \right) \right. \rightarrow M$, we can use Theorem 2.3.3 part (iii) to conclude that $f\left. \left( x_{n} \right) \right.g\left. \left( x_{n} \right) \right. \rightarrow LM$.

Now let's write another proof of the corollary based on Definition 4.2.1. Note that



$$
\begin{aligned}
\left| f\left. (x) \right.g\left. (x) \right. - \left. (LM) \right. \right| & = \left| f\left. (x) \right.g\left. (x) \right. - f\left. (x) \right.M + f\left. (x) \right.M - \left. (LM) \right. \right| \\
 & \leq \left| f\left. (x) \right.\left. \left( g\left. (x) \right. - M \right) \right. \right| + \left| M\left. \left( f\left. (x) \right. - L \right) \right. \right| \\
 & = \left| f\left. (x) \right. \right|\left| g\left. (x) \right. - M \right| + |M|\left| f\left. (x) \right. - L \right|
\end{aligned}
$$



Since $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$, there exists a $\delta_{1}$ such that $0 < |x - c| < \delta_{1}$ implies that $\left| f\left. (x) \right. - L \right| < \epsilon/\left. (2M) \right.$.

Next we need a lemma that says that $f\left. (x) \right.$ is bounded. Although this may not be the cause over the whole [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $A$, it is certainly true in some neighborhood around $x = c$. Given $(\epsilon)_{0} = 1$, for instances, we know there exists $\delta_{2} > 0$ such that $0 < |x - c| < \delta_{2}$ implies that $\left| f\left. (x) \right. - L \right| < 1$, and in this scase we then have $\left| f\left. (x) \right. \right| < |L| + 1$.

We now use the fact that $\lim\limits_{x \rightarrow c}g\left. (x) \right. = M$ to assert that there exists $\delta_{3} > 0$ such that $0 < |x - c| < \delta_{3}$ implies that $\left| g\left. (x) \right. - M \right| < \epsilon/\left. \left( 2\left. \left( |L| + 1 \right) \right. \right) \right.$. Finally, if we pick $\delta = \min\{\delta_{1},\delta_{2},\delta_{3}\}$, then



$$
\begin{aligned}
\left| f\left. (x) \right.g\left. (x) \right. - \left. (LM) \right. \right| & \leq \left| f\left. (x) \right. \right|\left| g\left. (x) \right. - M \right| + |M|\left| f\left. (x) \right. - L \right| \\
 & = \left. \left( |L| + 1 \right) \right.\left. \left( \frac{\epsilon}{2\left. \left( |L| + 1 \right) \right.} \right) \right. + M\left. \left( \frac{\epsilon}{2M} \right) \right. \\
 & = \epsilon
\end{aligned}
$$



Finally, we point out that this proof assumes $M \neq 0$. This minor hiccup can be remedied by replacing $M$ with $M + 1$ in the above argument. Another strategy is to handle it as a special case. It also follows as a corollary to Exercise 4.2.7.

## Exercise 4.2.3

> Review the definition of Thomae's [function](/notes/areas/mathematics/set_theory/definitions/function/) $t\left. (x) \right.$ from Section 4.1.

### (a)

> Construct three different [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s $\left. \left( x_{n} \right) \right.$, $\left. \left( y_{n} \right) \right.$, and $\left. \left( z_{n} \right) \right.$, each of which converges to 1 without using the number 1 as a term in the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/).

Let $\left. \left( x_{n} \right) \right. = \left. (n + 1) \right./n$ and $y_{n} = \sqrt{\left. (n + 1) \right./n}$ and $z_{n} = \left. (2n + 1) \right./2n$. Note that $\lim\left. \left( x_{n} \right) \right. = \lim\left. \left( y_{n} \right) \right. = \lim\left. \left( z_{n} \right) \right. = 1$.

### (b)

> Now, compute $\lim t\left. \left( x_{n} \right) \right.$, $\lim t\left. \left( y_{n} \right) \right.$, and $\lim t\left. \left( z_{n} \right) \right.$.

For $\left. \left( x_{n} \right) \right.$ we get $t\left. \left( x_{n} \right) \right. = 1/n$ which converges to 0.

For $\left. \left( y_{n} \right) \right.$ we get $t\left. \left( y_{n} \right) \right. = 0$ which converges to 0.

For $\left. \left( z_{n} \right) \right.$ we get $t\left. \left( z_{n} \right) \right. = 1/\left. (2n) \right.$ which converges to 0.

### (c)

> Make an educated conjecture for $\lim\limits_{x \rightarrow 1}t\left. (x) \right.$, and use Definition 4.2.1B to verify the claim. (Given $\epsilon > 0$, consider the set of points $\{ xin\mathbb{R}:t\left. (x) \right. \geq \epsilon\}$). Argue that all the points in this set are isolated.

The point to make is that the closer a rational number is to 1, the larger its denominator has to be, and thus the smaller the value of $t\left. (x) \right.$. Because $t\left. (x) \right. = 0$ for all irrational numbers, the conjecture is that $\lim\limits_{x \rightarrow 1}t\left. (x) \right. = 0$.

In order to prove our claim, we have to show that given $\epsilon > 0$, there exists a $\delta$-neighborhood around 1 such that $x \in V_{\delta}\left. (1) \right.$ implies that $t\left. (x) \right. \in V_{\epsilon}\left. (0) \right.$. If we set $T = \{ x \in R:t\left. (x) \right. \geq \epsilon\}$, then notice that $x \in T$ if and only if $x$ is a rational number of the form $x = m/n$ where $n \leq 1/\epsilon$. If we focus on some finite interval such as $\left. \lbrack 0,2\rbrack \right.$, then the restriction on the size of $n$ implies that the set $T \cap \left. \lbrack 0,2\rbrack \right.$ is *finite*. With finite sets, we are allowed to take minimums and so let



$$
\delta = \min\{ y:y \in T \cap \left. \lbrack 0,2\rbrack \right.\rbrack\} > 0
$$



To see that this choice of $\delta$ works, we note that if $x \in V_{\delta}\left. (1) \right.$ then $x \in T$ and thus $t\left. (x) \right. \in V_{\epsilon}\left. (0) \right.$.

## Exercise 4.2.5

> Use Definition 4.2.1 to supply a proper proof for the following limit statements.

### (a)

> $\lim\limits_{x \rightarrow 2}\left. (3x + 4) \right. = 10$

Following the structure of Example 4.2.2, let $\epsilon > 0$ be arbitrary. Definition 4.2.1 requires that we produce a $\delta > 0$ so that $0 < |x - 2| < \delta$ leads to the conclusion $\left| f\left. (x) \right. - 7 \right| < \epsilon$. Notice that



$$
\left| \left. (3x + 4) \right. - 10 \right| = |3x - 6| = 3|x - 2|
$$



Thus, if we choose $\delta > \epsilon/3$, then $0 < |x - 2| < \delta$ implies $\left| \left. (3x + 4) \right. - 10 \right| < 3\left. (\epsilon/3) \right. = \epsilon$.

### (b)

> $\lim\limits_{x \rightarrow 0}x^{3} = 0$

Let $\epsilon > 0$ be arbitrary. Then choose $\delta = \epsilon^{1/3}$. Then $0 < |x| < \delta = \epsilon^{1/3}$ implies that



$$
\left| x^{3} - 0 \right| = \left| x^{3} \right| < \left. \left( \epsilon^{\frac{1}{3}} \right) \right.^{3} = \epsilon
$$



### (c)

> $\lim\limits_{x \rightarrow 2}\left. \left( x^{2} + x - 1 \right) \right. = 5$

Let $(\epsilon)_{0}$ be arbitrary. Notice that



$$
\left| \left. \left( x^{2} + x - 1 \right) \right. - 5 \right| = \left| x^{2} + x - 6 \right| = |x + 3||x - 2|
$$



Similiar to Example 4.2.2 (ii), we can make $|x - 2|$ arbitrarily small, but we need to have an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) on $|x + 3|$ so that we know how small to choose $\delta$. If we agree that our $\delta$-neighborhood around $c = 2$ must have radius no larger than $\delta = 1$, then we get the [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) $|x + 3| \leq |3 + 3| = 6$ for all $x \in V_{\delta}\left. (c) \right.$.

Now, choose $\delta = \min\{ 1,\epsilon/6\}$. If $0 < |x - 2| < \delta$, then it follows that



$$
\left| \left. \left( x^{2} + 2 - 1 \right) \right. - 5 \right| = |x + 3||x - 2| < 6\left. \left( \frac{\epsilon}{6} \right) \right. = \epsilon
$$



### (d)

> $\lim\limits_{x \rightarrow 3}1/x = 1/3$

Let $\epsilon > 0$ be arbitrary. Notice that



$$
\left| \frac{1}{x} - \frac{1}{3} \right| = \frac{|3 - x|}{|3x|}
$$



To bound this expression we need to prevent $x$ from being too close to zero. To this end, let's insist again that $\delta \leq 1$ so that $x \in \left. (2,4) \right.$. Under this restriction, $1/|3x| \leq 1/6$.

Now choose $\delta = \min\{ 1,6\epsilon\}$. If $0 < |x - 3| < \delta$, then it follows that



$$
\left| \frac{1}{x} - \frac{1}{3} \right| = \frac{|3 - x|}{|3x|} < \frac{1}{6}\left. (6\epsilon) \right. = \epsilon
$$



## Exercise 4.2.7

> Let $g:A \rightarrow \mathbb{R}$ and assume that $f$ is a bounded [function](/notes/areas/mathematics/set_theory/definitions/function/) on $A$ in the sense that there exists $M > 0$ satisfying $\left| f\left. (x) \right. \right| \leq M$ for all $x \in A$.
>
> Show that if $\lim\limits_{x \rightarrow c}g\left. (x) \right. = 0$, then $\lim\limits_{x \rightarrow c}g\left. (x) \right.f\left. (x) \right. = 0$ as well.

As instructed, we assume that $f$ is bounded, i.e. there exists an $M > 0$ such that $\left| f\left. (x) \right. \right| \leq M$ for all $x \in A$. Now let $\epsilon > 0$ be arbitrary. Because we know that $\lim\limits_{x \rightarrow c}g\left. (x) \right. = 0$, there exists a $\delta > 0$ such that $0 < |x - c| < \delta$ implies $\left| g\left. (x) \right. - 0 \right| = \left| g\left. (x) \right. \right| < \epsilon/M$. Since we know that $f$ is bounded above by $M$, it follows that



$$
\left| g\left. (x) \right.f\left. (x) \right. - 0 \right| = \left| g\left. (x) \right. \right|\left| f\left. (x) \right. \right| < \left. \left( \frac{\epsilon}{M} \right) \right.M = \epsilon
$$



whenever $0 < |x - c| < \delta$. Therefore, $\lim\limits_{x \rightarrow c}g\left. (x) \right.f\left. (x) \right. = 0$.

## Exercise 4.2.9 (Infinite Limits)

> The statement $\lim\limits_{x \rightarrow 0}1/x^{2} = \infty$ certainly makes intuitive sense. To construct a rigorous definition in the challenge-response style of Definition 4.2.1 for an infinite limit statement of this form, we replace the (arbitrarily small) $\epsilon > 0$ challenge with an (arbitrarily large) $M > 0$ challenge:
>
> *Definition*: $\lim\limits_{x \rightarrow c}f\left. (x) \right. = \infty$ means that for all $M > 0$ we can find a $\delta > 0$ such that whenever $0 < |x - c| < \delta$, it follows that $f\left. (x) \right. > M$.

### (a)

> Show $\lim\limits_{x \rightarrow 0}1/x^{2} = \infty$ in the sense described in the previous definition.

We say $\lim\limits_{x \rightarrow \infty}f\left. (x) \right. = \infty$ if for every arbitrarily large $M$, there exists a $\delta > 0$ such that whenever $0 < |x - c| < \delta$ it follows that $f\left. (x) \right. > M$.

Let $M > 0$ be arbitrary. To prove that $\lim\limits_{x \rightarrow c}1/x^{2} = \infty$, we can choose $\delta = \sqrt{1/M}$. Then $0 < |x| < \delta = \sqrt{1/M}$ as desired.

### (b)

> Now, construct a definition for the statement $\lim\limits_{x \rightarrow \infty}f\left. (x) \right. = L$. Show that $\lim\limits_{x \rightarrow \infty}1/x = 0$.

We say that $\lim\limits_{x \rightarrow \infty}f\left. (x) \right. = L$ if for every $\epsilon > 0$, there exists $K > 0$ such that whenever $x > K$, it follows that $\left| f\left. (x) \right. - L \right| < \epsilon$.

Let $\epsilon > 0$ be arbitrary. To prove that $\lim\limits_{x \rightarrow \infty}1/x = 0$, choose $K = 1/\epsilon$. If $x > K = 1/\epsilon$, then $1/x < \epsilon$ as desired.

### (c)

> What would a rigorous definition for $\lim\limits_{x \rightarrow \infty}f\left. (x) \right. = \infty$ look like? Give an example of such a limit.

We say that $\lim\limits_{x \rightarrow \infty}f\left. (x) \right. = \infty$ if for every $M > 0$ there exists a $K > 0$ such that whenever $x > K$ it follows that $f\left. (x) \right. > M$. An example of a [function](/notes/areas/mathematics/set_theory/definitions/function/) with such a limit would be $f\left. (x) \right. = \sqrt{x}$. Given an arbitrary $M > 0$, choose $K = M^{2}$. If $x > K = M^{2}$, then it follows that $\sqrt{x} > M$ as desired.

## Exercise 4.2.11 (Squeeze Theorem)

Let $f,g$, and $h$ satisfy $f\left. (x) \right. \leq g\left. (x) \right. \leq h\left. (x) \right.$ for all $x$ in some common [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $A$. If $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$ and $\lim\limits_{x \rightarrow c}h\left. (x) \right. = L$ at some [limit point](/notes/areas/mathematics/topology/definitions/limit_point/) $c$ of $A$, show that $\lim\limits_{x \rightarrow c}g\left. (x) \right. = L$ as well.

Let $\epsilon$ be arbitrary. Because $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$, there exists a $\delta_{1} > 0$ such that $0 < |x - c| < \delta_{1}$ implies $L - \epsilon < f\left. (x) \right. < L + \epsilon$. Likewise, there exists $\delta_{2} > 0$ such that $0 < |x - c| < \delta_{2}$ implies $L - \epsilon < h\left. (x) \right. < L + \epsilon$. Choosing $\delta = \min\{\delta_{1},\delta_{2}\}$, we see that



$$
L - \epsilon < f\left. (x) \right. \leq g\left. (x) \right. \leq h\left. (x) \right. < L + \epsilon
$$



whenever $0 < |x - c| < \delta$, which implies $\left| g\left. (x) \right. - L \right| < \epsilon$ as desired.

# Section 4.3 Exercises

## Exercise 4.3.1

> Let $g\left. (x) \right. = x^{1/3}$.

### (a)

> Prove that $g$ is continuous at $c = 0$.

Let $\epsilon > 0$. Note that $\left| g\left. (x) \right. - c \right| = \left| x^{1/3} - 0 \right| = \left| x^{1/3} \right|$ where $c = 0$. Now if we set $\delta = \epsilon^{3}$, then $|x - 0| < \delta = \epsilon^{3}$ implies that $\left| x^{1/3} \right| < \epsilon$. This shows that $g\left. (x) \right.$ is continuous at $c = 0$.

### (b)

Prove that $g$ is continuous at a point $c \neq 0$. (The identity $a^{3} - b^{3} = \left. (a - b) \right.\left. \left( a^{2} + ab + b^{2} \right) \right.$ will be helpful.

For $c \neq 0$ we write



$$
\begin{aligned}
\left| g\left. (x) \right. - g\left. (c) \right. \right| & = \left| x^{1/3} - c^{1/3} \right| \\
 & = \left| x^{1/3} - c^{1/3} \right|\left. \left( \frac{x^{2/3} + \left. (xc) \right.^{1/3} + c^{2/3}}{x^{2/3} + \left. (xc) \right.^{1/3} + c^{2/3}} \right) \right. \\
 & = \frac{|x - c|}{x^{2/3} + \left. (xc) \right.^{1/3} + c^{2/3}} \\
 & \leq \frac{|x - c|}{c^{2/3}}
\end{aligned}
$$



Therefore, if we choose $\delta = \epsilon c^{2/3}$, then $|x - c| < \delta = \epsilon c^{2/3}$ implies



$$
\begin{aligned}
\left| g\left. (x) \right. - g\left. (c) \right. \right| & = \left| x^{1/3} - x^{1/3} \right| \\
 & \leq \frac{|x - c|}{c^{2/3}} \\
 & < \frac{\epsilon c^{2/3}}{c^{2/3}} \\
 & = \epsilon
\end{aligned}
$$



## Exercise 4.3.3

### (a)

> Supply a proof for Theorem 4.3.9 using the $\epsilon - \delta$ characterization of continuity.

Let $\epsilon > 0$. Because $g$ is continuous at $f\left. (c) \right. \in B$, for every $\epsilon > 0$, there exists an $\alpha > 0$ such that $\left| g\left. (y) \right. - g\left. \left( f\left. (c) \right. \right) \right. \right| < \epsilon$ whenever $y$ satisfies $\left| y - f\left. (c) \right. \right| < \alpha$. Now, because $f$ is continuous at $c \in A$, for this value of $\alpha$, we can find a $\delta > 0$ such that $|x - c| < \delta$ implies that $\left| f\left. (x) \right. - f\left. (c) \right. \right| < \delta$. Combining the two statments, we see that for $\epsilon > 0$, there exists a $\delta > 0$ such that $|x - c| < \delta$ implies $\left| g\left. \left( f\left. (x) \right. \right) \right. - g\left. \left( f\left. (c) \right. \right) \right. \right| < \epsilon$. Therefore, $g \circ f$ is continuous at $c$.

### (b)

> Give another proof of this theorem using the sequential characterization of [continuity](/notes/areas/mathematics/real_analysis/definitions/continuity/) (from Theorem 4.3.2(iii)).

Assume that $\left. \left( x_{n} \right) \right. \rightarrow c$ (with $c \in A$). Our goal is to show that $g\left. \left( f\left. \left( x_{n} \right) \right. \right) \right. \rightarrow g\left. \left( f\left. (c) \right. \right) \right.$. Because $f$ is continuous at $c$, we know that $f\left. \left( x_{n} \right) \right. \rightarrow f\left. (c) \right.$. Then, because $g$ is continuous at $f\left. (c) \right.$, we know that $g\left. \left( f\left. \left( x_{n} \right) \right. \right) \right. \rightarrow g\left. \left( f\left. (c) \right. \right) \right.$. This completes the proof.

## Exercise 4.3.5

> Show using Definition 4.3.1 that if $c$ is an isolated point of $A \subseteq \mathbb{R}$, then $f:A \rightarrow \mathbb{R}$ is continuous at $c$.

Restating Definition 4.3.1:

> [continuity](/notes/areas/mathematics/real_analysis/definitions/continuity/): A [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:A \rightarrow \mathbb{R}$ is *continuous* at a point $c \in A$ if, for all $\epsilon > 0$, there exists a $\delta > 0$ such that whenever $|x - c| < \delta$ (and $\in A$) it follows that $\left| f\left. (x) \right. - f\left. (c) \right. \right| < \epsilon$. If $f$ is continuous at every point in the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $A$, then we say that $f$ is continuous on $A$.

Let $\epsilon > 0$ be arbitrary. If $c$ is an [isolated point](/notes/areas/mathematics/topology/definitions/isolated_point/) of $A$, then there exists a neighborhood $V_{\delta}\left. (c) \right.$ that intersects the set $A$ only at $c$. Because $x \in V_{\delta}\left. (c) \right. \cap A$ implies that $x = c$, we see that $f\left. (x) \right. = f\left. (c) \right. \in V_{\epsilon}\left. \left( f\left. (c) \right. \right) \right.$. Thus $f\left. (x) \right.$ is continuous at the [isolated point](/notes/areas/mathematics/topology/definitions/isolated_point/) $c$ using the criterion in Theorem 4.3.2 (ii).

## Exercise 4.3.7

### (a)

> Referring to the proper theorems, give a formal argument that Dirichlet's [function](/notes/areas/mathematics/set_theory/definitions/function/) from Section 4.1 is nowhere-continuous on $\mathbb{R}$.

### (b)

> Review the definition of Thomae's [function](/notes/areas/mathematics/set_theory/definitions/function/) in Section 4.1 and demonstrate that it fails to be continuous at every rational point.

### (c)

> Use the characterization of [continuity](/notes/areas/mathematics/real_analysis/definitions/continuity/) in Theorem 4.3.2 (iii) to show that Thomae's [function](/notes/areas/mathematics/set_theory/definitions/function/) is continuous at every irrational point in $\mathbb{R}$. (Given $\epsilon > 0$, consider the set of points $\{ x \in \mathbb{R}:t\left. (x) \right. \geq \epsilon\}.)$

## Exercise 4.3.9

> Assume $h:\mathbb{R} \rightarrow \mathbb{R}$ is continuous on $\mathbb{R}$ and let $K = \{ x:h\left. (x) \right. = 0\}.$ Show that $K$ is a closed set.

## Exercise 4.3.11 (Contraction Mapping Theorem)

> Let $f$ be a [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on all of $\mathbb{R}$, and assume there is a constant $c$ such that $0 < c < 1$ and
>
> 

$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| \leq c|x - y|
$$


>
> for all $x,y \in \mathbb{R}$

### (a)

> Show that $f$ is continuous on $\mathbb{R}$.

Let $\epsilon > 0$ and fix $y \in \mathbb{R}$. To show that $f$ is continuous at $y$, choose $\epsilon/c$ and observe that $|x - y| < \delta = \epsilon/c$ implies



$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| \leq c|x - y| < c\left. \left( \frac{\epsilon}{c} \right) \right. = \epsilon
$$



Because $y$ is arbitrary, $f\left. (x) \right.$ must be continuous on $\mathbb{R}$.

### (b)

> Pick some point $y_{1} \in \mathbb{R}$ and construct the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)
>
> 

$$
\left. \left( y_{1},f\left. \left( y_{1} \right) \right.,f\left. \left( f\left. \left( y_{1} \right) \right. \right) \right.,\ldots \right) \right.
$$


>
> In general, if $y_{n + 1} = f\left. \left( y_{n} \right) \right.$, show that the resulting [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( y_{n} \right) \right.$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/). Hence we may let $y = \lim y_{n}$.

Observe that for any fixed $n \in \mathbb{N}$,



$$
\left| y_{m + 1} - y_{m + 2} \right| = \left| f\left. \left( y_{m} \right) \right. - f\left. \left( y_{m + 1} \right) \right. \right| \leq c\left| y_{m} - y_{m + 1} \right|
$$



This idea can be extended inductively to conclude that



$$
\begin{aligned}
\left| y_{m + 1} - y_{m + 2} \right| & \leq c\left| y_{m} - y_{m + 1} \right| \\
 & \leq c^{2}\left| y_{m - 1} - y_{m} \right| \\
 & = \cdots \leq c^{m}\left| y_{1} - y_{2} \right|
\end{aligned}
$$



The fact that $0 < c < 1$ means that $\sum_{n = 1}^{\infty}c^{n}$ converges, and this will enable us to conclude that $\left. \left( y_{n} \right) \right.$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/). To see how, first note that for $m < n$ we have



$$
\begin{aligned}
\left| y_{m} - y_{n} \right| & \leq \left| y_{m + 1} \right| + \left| y_{m + 1} - y_{m + 2} \right| + \cdots + \left| y_{n - 1} - y_{n} \right| \\
 & \leq c^{m - 1}\left| y_{1} - y_{2} \right| + c^{m}\left| y_{1} - y_{2} \right| + \cdots + c^{n - 2}\left| y_{1} - y_{2} \right| \\
 & = c^{m - 1}\left| y_{1} - y_{2} \right|(1 + c + \cdots + c^{n - m - 1} \\
 & < c^{m - 1}\left| y_{1} - y_{2} \right|\left. \left( \frac{1}{1 - c} \right) \right.
\end{aligned}
$$



Let $\epsilon > 0$ and choose $N \in \mathbb{N}$ large enough so that $c^{N - 1} < \epsilon\left. (1 - c) \right./\left| y_{1} - y_{2} \right|$. Then the previous calculation shows that $n > m \geq \mathbb{N}$ implies that $\left| y_{m} - y_{n} \right| < \epsilon$. We conclude that $\left. \left( y_{n} \right) \right.$ is Cauchy.

### (c)

> Prove that $y$ is a fixed point of $f$ (i.e., $f\left. (y) \right. = y$) and that it is unique in this regard.

Set $y = \lim y_{n}$. Because $f$ is continuous , $f\left. (y) \right. = \lim f\left. \left( y_{n} \right) \right.$. But $f\left. \left( y_{n} \right) \right. = y_{n + 1}$ and so $f\left. (y) \right. = \lim y_{n + 1}$. Because $\lim y_{n + 1} = \lim y_{n} = y$, it follows that $f\left. (y) \right. = y$ and y is a fixed point.

### (d)

> Finally, prove that if $x$ is *any* arbitrary point in $\mathbb{R}$, then the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x,f\left. (x) \right.,f\left. \left( f\left. (x) \right. \right) \right.,\ldots \right) \right.$ converges to $y$ defined in (b).

The argument in (b) and (c) applies to any [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of iterates. Thus, given an arbitrary $x$, we may assert that $\left. \left( x,f\left. (x) \right.,f\left. \left( f\left. (x) \right. \right) \right.,\ldots \right) \right.$ converges to a limit $x'$ and that $x'$ is a fixed point of $f$. But $y$ is also a fixed point and so



$$
\left| f\left. (x') \right. - f\left. (y) \right. \right| = |x' - y|
$$



However,



$$
\left| f\left. (x') \right. - f\left. (y) \right. \right| \leq c|x' - y|
$$



must also be true, and because $0 < c < 1$ we conclude that $x' = y$. In summary if $f$ is a contraction on $\mathbb{R}$, then $f$ has a unique fixed point, and every [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of iterates converges to this unique point.

## Exercise 4.3.13

> Let $f$ be a [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on all of $\mathbb{R}$ that satisfies the additive condition $f\left. (x + y) \right. = f\left. (x) \right. + f\left. (y) \right.$ for all $x,y \in \mathbb{R}$.

### (a)

> Show that $f\left. (0) \right. = 0$ and that $f\left. ( - x) \right. = - f\left. (x) \right.$ for all $x \in \mathbb{R}$.

Note that $f\left. (0) \right. = f\left. (0 + 0) \right. = f\left. (0) \right. + f\left. (0) \right.$ which implies that $f\left. (0) \right. = 0$. For any $x \in \mathbb{R}$, $f\left. (0) \right. = f\left. (x - x) \right. = f\left. (x) \right. + f\left. ( - x) \right. = 0$. This implies that $f\left. ( - x) \right. = - f\left. (x) \right.$.

### (b)

> Let $k = f\left. (1) \right.$. Show that $f\left. (n) \right. = kn$ for all $n \in \mathbb{N}$, and then prove that $f\left. (z) \right. = kz$ for all $z \in \mathbb{Z}$. Now, prove that $f\left. (r) \right. = kr$ for any rational number $r$.

For any $n \in \mathbb{N}$, we have



$$
f\left. (n) \right. = f\left. (1 + 1 + \ldots + 1) \right. = f\left. (1) \right. + f\left. (1) \right. + \ldots + f\left. (1) \right. = nf\left. (1) \right. = nk
$$



For $z \in \mathbb{Z}$, the case $z < 0$ is all that remains to do. In (a) we saw that $f\left. ( - x) \right. = - f\left. (x) \right.$. Observing that $z = - |z|$ and $|z| \in \mathbb{N}$, we can write



$$
f\left. (z) \right. = f\left. \left( - |z| \right) \right. = - f\left. \left( |z| \right) \right. = - |z|k = zk
$$



Before taking on an arbitrary rational number, let's consider $1/n$ where $n \in \mathbb{N}$. In this case,



$$
\begin{aligned}
k = f\left. (1) \right. & = f\left. \left( \frac{1}{n} + \frac{1}{n} + \cdots + \frac{1}{n} \right) \right. \\
 & = nf\left. \left( \frac{1}{n} \right) \right.
\end{aligned}
$$



which gives $f\left. (1/n) \right. = k/n$. For $m,n \in \mathbb{N}$ we then get



$$
\begin{aligned}
k = f\left. (m/n) \right. & = f\left. \left( \frac{1}{n} + \frac{1}{n} + \cdots + \frac{1}{n} \right) \right. \\
 & = mf\left. \left( \frac{1}{n} \right) \right. \\
 & = k\left. (m/n) \right.
\end{aligned}
$$



Finally for any $r \in \mathbb{Q}$ satisfying $r < 0$, an argument similar to equation (1) above gives the result.

### (c)

> Show that if $f$ is continuous at $x = 0$, then $f$ is continuous at every point in $\mathbb{R}$ and conclude that $f\left. (x) \right. = kx$ for all $x \in \mathbb{R}$. Thus any additive [function](/notes/areas/mathematics/set_theory/definitions/function/) that is continuous at $x = 0$ must necessarily be a linear [function](/notes/areas/mathematics/set_theory/definitions/function/) through the origin.

Fix $x \in \mathbb{R}$. Because $\mathbb{Q}$ is dense in $\mathbb{R}$, there exists a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( r_{n} \right) \right. \subseteq \mathbb{Q}$ with $\left. \left( r_{n} \right) \right. \rightarrow x$. By our work in part (c) we know that $f\left. \left( r_{n} \right) \right. = kr_{n}$ for all $n$. Then, because $f$ is continuous at $x$, we have



$$
f\left. (x) \right. = \lim f\left. \left( r_{n} \right) \right. = \lim kr_{n} = kx
$$



This completes the proof.

# Section 4.4 Exercises

## Exercise 4.4.1

### (a)

> Show that $f\left. (x) \right. = x^{3}$ is continuous on all of $\mathbb{R}$.

Recognizing that this is the difference of cubes, we have



$$
\left| f\left. (x) \right. - f\left. (c) \right. \right| = \left| x^{3} - c^{3} \right| = |x - c|\left| x^{2} + xc + c^{2} \right|
$$



Per similar examples, we need an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) on the right-hand part of the expression. We will insist again that $\delta \leq 1$, which means that $x$ will fall in the interval $\left. (c - 1,c + 1) \right.$ and thus



$$
\left| x^{2} + xc + c^{2} \right| < \left. (c + 1) \right.^{2} + \left. (c + 1) \right.^{2} + c^{2} < 3\left. (c + 1) \right.^{2}
$$



Now choose $\delta = \min\{ 1,\epsilon/\left. \left( 3\left. (c + 1) \right.^{2} \right) \right.\}$. Then $|x - c| < \delta$ implies that



$$
\left| f\left. (x) \right. - f\left. (c) \right. \right| < \left. \left( \frac{\epsilon}{3\left. (c + 1) \right.^{2}} \right) \right.3\left. (c + 1) \right.^{2} = \epsilon
$$



### (b)

> Argue, using Theorem 4.4.5, that $f$ is not uniformly continuous on $\mathbb{R}$.

Restating Definition 4.4.4 ([uniform_continuity](/notes/areas/mathematics/real_analysis/definitions/uniform_continuity/)):

> [uniform_continuity](/notes/areas/mathematics/real_analysis/definitions/uniform_continuity/): A [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:A \rightarrow \mathbb{R}$ is uniformly continuous on $A$ if for every $\epsilon > 0$ there exists a $\delta > 0$ such that for all $x,y \in A$, $|x - y| < \delta$ implies that $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \epsilon$.

Restating Theorem 4.4.5:

> Sequential Criterion for Absence of [uniform_continuity](/notes/areas/mathematics/real_analysis/definitions/uniform_continuity/): A [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:A \rightarrow \mathbb{R}$ fails to be uniformly continuous on $A$ if and only if there exists a particular $(\epsilon)_{0} > 0$ and two [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ in $A$ satisfying
>
> 

$$
\left| x_{n} - y_{n} \right| \rightarrow 0\quad\mathrm{\text{but}}\quad\left| f\left. \left( x_{n} \right) \right. - f\left. \left( y_{n} \right) \right. \right| \geq (\epsilon)_{0}
$$



The dependence of $\epsilon$ on the point $c$ is evidence in the previous formula with large choices of $c$ resulting in smaller values of $\delta$. This means that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ we seek are necessarily going to tend to infinity.

Set $x_{n} = n$ and $y_{n} = n + 1/n$. Then $\left| x_{n} - y_{n} \right| = 1/n$ tends to zero as required, while



$$
\left| f\left. \left( x_{n} \right) \right. - f\left. \left( y_{n} \right) \right. \right| = \left| n^{3} - \left. \left( n + \frac{1}{n})^{3} \right) \right. \right| = 3n + \frac{3}{n} + \frac{1}{n^{3}} \geq 3
$$



stays $(\epsilon)_{0} = 3$ units apart for all $n \in \mathbb{N}$. This proves that $f$ is not uniformly continuous on $\mathbb{R}$.

### (c)

> Show that $f$ is uniformly continuous on any bounded subset of $\mathbb{R}$.

Let $A$ be bounded by $M$. If $x,c \in A$ then $\left| x^{2} + xc + c^{2} \right| \leq 3M^{2}$. Given $\epsilon > 0$ we can now choose $\delta = \epsilon/\left. \left( 3M^{2} \right) \right.$, which is indepent of $c$. If $|x - c| < \delta$, it follows that



$$
\left| f\left. (x) \right. - f\left. (c) \right. \right| \leq \left. \left( \frac{\epsilon}{3M^{2}} \right) \right.3M^{2} = \epsilon
$$



and $f$ is uniformly continuous on $A$.

## Exercise 4.4.3

> Show that $f\left. (x) \right. = 1/x^{2}$ is uniformly continuous on the set $\lbrack 1,\infty)$ but not on the set $(0,1\rbrack$.

For $f\left. (x) \right. = 1/x^{2}$ we have



$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| = \left| \frac{1}{x^{2}} - \frac{1}{y^{2}} \right| = \left| \frac{y^{2} - x^{2}}{x^{2}y^{2}} \right| = |y - x|\left. \left( \frac{y + x}{x^{2}y^{2}} \right) \right.
$$



If we restrict our attention to $x,y \geq 1$, then we can estimate



$$
\frac{y + x}{x^{2}y^{2}} = \frac{1}{x^{2}y} + \frac{1}{xy^{2}} \leq 1 + 1 = 2
$$



Given $\epsilon > 0$, we may then choose $\delta = \epsilon/2$ (independent of $x$ and $y$), and it follows that $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \left. (\epsilon/2) \right.2 = \epsilon$ whenever $|x - y| < \delta$. This shows that $f$ is uniformly continuous on $\lbrack 1,\infty)$.

If $x$ and $y$ are allowed to be arbitrarily close to zero, then the expression $\left. (x + y) \right./\left. \left( x^{2}y^{2} \right) \right.$ is unbounded and we get into trouble. To see this more explicity, set $x_{n} = 1/\sqrt{n}$ and $y_{n} = 1/\sqrt{n + 1}$. Then $\left| x_{n} - y_{n} \right| \rightarrow 0$ while



$$
\left| f\left. \left( x_{n} \right) \right. - f\left. \left( y_{n} \right) \right. \right| = \left| n - \left. (n + 1) \right. \right| = 1
$$



By the criterion in Theorem 4.4.5, we conclude that $f$ is not uniformly continuous on $(0,1\rbrack$.

## Exercise 4.4.5

> Assume that $g$ is defined on an open interval $\left. (a,c) \right.$ and it is known to be uniformly continuous on $(a,b\rbrack$ and $\lbrack b,c)$, where $a < b < c$. Prove that $g$ is uniformly continuous on $\left. (a,c) \right.$.

Let $\epsilon > 0$ be arbitrary. Because $f$ is uniformly continuous on $(a,b\rbrack$, there exists $\delta_{1} > 0$ such that $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \epsilon/2$ whenever $x,y \in (a,b\rbrack$ satisfy $|x - y| < \delta_{1}$. Likewise, there exists $d_{2} > 0$ such that $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \epsilon/2$ whenever $x,y \in \lbrack b,c)$ satisfy $|x - y| < \delta_{2}$.

Now set $\delta = \min\{\delta_{1},\delta_{2}\}$ and assume we have $x$ and $y$ satisfying $|x - y| < \delta$. If both $x$ and $y$ fall in $(a,b\rbrack$, or ify they both fall in $\lbrack b,c)$, then we get $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \epsilon/2 < \epsilon$. In the case where $x < b$ and $y > b$ we may write



$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| \leq \left| f\left. (x) \right. - f\left. (b) \right. \right| + \left| f\left. (b) \right. - f\left. (y) \right. \right| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
$$



Because $d_{1}$ and $d_{2}$ are both independent of $x$ and $y$, $\delta$ is as well and we conclude that $f$ is uniformly continuous on $\left. (a,c) \right.$.

## Exercise 4.4.7

> Prove that $f\left. (x) \right. = \sqrt{x}$ is uniformly continuous on $\lbrack 0,\infty)$.

Let's first focus our attention on the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $\lbrack 1,\infty)$. If $x,y \geq 1$, it follows that



$$
\left| \sqrt{x} - \sqrt{y} \right| = \left| \frac{x - y}{\sqrt{x} + \sqrt{y}} \right| \leq |x - y|\frac{1}{2}
$$



So, given $\epsilon > 0$ we can choose $\delta = 2\epsilon$, and it follows that $f\left. (x) \right. = \sqrt{x}$ uniformly continuous on $\lbrack 1,\infty)$.

Now, the interval $\left. \lbrack 0,1\rbrack \right.$ is compact, so $f$ is uniformly continuous on this [domain](/notes/areas/mathematics/set_theory/definitions/domain/) as well. Putting these two pieces together and repeating the argument in Exercise 4.4.5 gives the result.

## Exercise 4.4.9 ([Lipschitz_Function](/notes/areas/mathematics/real_analysis/definitions/lipschitz_function/)s)

> A [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:A \rightarrow \mathbb{R}$ is called *Lipschitz* if there exists a bound $M > 0$ such that
>
> 

$$
\left| \frac{f\left. (x) \right. - f\left. (y) \right.}{x - y} \right| \leq M
$$


>
> for all $x \neq y \in A$. Geometrically speaking, a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ is Lipschitz if there is a uniform bound on the magnitude of the slopes of lines drawn through any two points on the graph of $f$.

### (a)

> Show that if $f:A \rightarrow \mathbb{R}$ is Lipschitz, then it is uniformly continuous on $A$.

First write the Lipschitz condition in the form



$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| \leq M|x - y|\quad\mathrm{\text{for all }}x,y \in A
$$



Given $\epsilon > 0$, we choose $\delta = \epsilon/M$. Then $|x - y|$ implies



$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| < M\frac{\epsilon}{M} = \epsilon
$$



This proves that $f$ is uniformly continuous.

### (b)

> Is the converse statement true? Are all uniformly continuous functions necessarily Lipschitz?

No. All uniformly continuous functions are not Lipschitz. Consider $f\left. (x) \right. = \sqrt{x}$ on $\left. \lbrack 0,1\rbrack \right.$. A continuous [function](/notes/areas/mathematics/set_theory/definitions/function/) on a compact set is uniformly continuous. However, if we set $y = 0$ and consider $x > 0$, then we get



$$
\left| \frac{f\left. (x) \right. - f\left. (y) \right.}{x - y} \right| = \left| \frac{\sqrt{x}}{x} \right| = \frac{1}{\sqrt{x}}
$$



which is *not* bounded for values of $x$ arbitrarily close to zero.

## Exercise 4.4.11 (Topological Characterization of Continuity)

> Let $g$ be defined on all of $\mathbb{R}$. If $B$ is a subset of $\mathbb{R}$, define the set $g^{- 1}\left. (B) \right.$ by 

$$
g^{- 1}\left. (B) \right. = \{ x \in \mathbb{R}:g\left. (x) \right. \in B\}
$$


>
> Show that $g$ is continuous *if and only if* $g^{- 1}\left. (O) \right.$ is open whenever $O \subseteq \mathbb{R}$ is an [open_set](/notes/areas/mathematics/topology/definitions/open_set/).

$\left. ( \Rightarrow ) \right.$: Assume $g$ is continuous on $\mathbb{R}$ and let $O \subseteq \mathbb{R}$ be open. We want to prove that $g^{- 1}\left. (O) \right.$ is open. To do this, we fix $c \in g^{- 1}\left. (O) \right.$ and show that there is a $\delta$-neighborhood of $c$ satisfying $V_{\delta}\left. (c) \right. \subseteq g^{- 1}\left. (O) \right.$.

Because $c \in g^{- 1}\left. (O) \right.$, we know that $g\left. (c) \right. \in O$. Now, $O$ is open, so there exists an $\epsilon > 0$ such that $V_{\epsilon}\left. \left( g\left. (c) \right. \right) \right. \subseteq O$. Given this particular $\epsilon$, the [continuity](/notes/areas/mathematics/real_analysis/definitions/continuity/) of $g$ at $c$ allows us to assert that there exists a neighborhood $V_{\delta}\left. (c) \right.$ with the property that $x \in V_{\delta}\left. (c) \right.$ implies that $g\left. (x) \right. \in V_{\epsilon}\left. \left( g\left. (c) \right. \right) \right. \subseteq O$. But this implies that $V_{\delta}\left. (c) \right. \subseteq g^{- 1}\left. (O) \right.$, which proves that $g^{- 1}\left. (O) \right.$ is open.

$\left. ( \Leftarrow ) \right.$: Conversely, we assume that $g^{- 1}\left. (O) \right.$ is open whenever $O$ is open, and show that $g$ is continuous at an arbitrary point $c \in \mathbb{R}$.

Let $\epsilon > 0$, and set $O = V_{\epsilon}\left. \left( g\left. (c) \right. \right) \right.$. Certainly $O$ is open, so our hypothesis gives us that $g^{- 1}\left. (O) \right.$ is open. Because $c \in g^{- 1}\left. (O) \right.$, there exists a $\delta > 0$ with $V_{\delta}\left. (c) \right. \subseteq g^{- 1}\left. (O) \right.$. But this means that whenever $x \in V_{\delta}\left. (c) \right.$ we get $g\left. (x) \right. \in O = V_{\epsilon}\left. \left( g\left. (c) \right. \right) \right.$, and we conclude that $g$ is continuous at $c$ by the criterion in Theorem 4.3.2(iii).

## Exercise 4.4.13 ([Continuous_Extension_Theorem](/notes/areas/mathematics/real_analysis/definitions/continuous_extension_theorem/))

### (a)

> Show that a uniformly continuous [function](/notes/areas/mathematics/set_theory/definitions/function/) preserves [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/)s; that is, if $f:A \rightarrow \mathbb{R}$ is uniformly continuous and $\left. \left( x_{n} \right) \right. \subseteq A$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/), then show $f\left. \left( x_{n} \right) \right.$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/).

We want to show that $f\left. \left( x_{n} \right) \right.$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/), so let $\epsilon > 0$ be arbitrary. Because $f$ is uniformly continuous, there exists $\delta > 0$ such that $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \delta$. Given this $\delta$, we use the fact that $\left. \left( x_{n} \right) \right.$ is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/) to say that there exists an $N \in \mathbb{N}$ such that $\left| x_{n} - y_{n} \right| < \delta$ whenever $m,n \geq N$. Combining the last two statements we see that $\left| f\left. \left( x_{n} \right) \right. - f\left. \left( y_{n} \right) \right. \right| < \epsilon$ whenever $m,n \geq N$, which shows that $f\left. \left( x_{n} \right) \right.$ is Cauchy.

### (b)

> Let $g$ be a continuous [function](/notes/areas/mathematics/set_theory/definitions/function/) on the open interval $\left. (a,b) \right.$. Prove that $g$ is uniformly continuous on $\left. (a,b) \right.$ *if and only if* it is possible to define values $g\left. (a) \right.$ and $g\left. (b) \right.$ at the endpoints so that the extended [function](/notes/areas/mathematics/set_theory/definitions/function/) $g$ is continuous on $\left. \lbrack a,b\rbrack \right.$. (In the forward direction, first produce candidates for $g\left. (a) \right.$ and $g\left. (b) \right.$, and then show the extended $g$ is continuous.)

$\left. ( \Rightarrow ) \right.$: Let's first assume that $f$ is uniformly continuous on $\left. (a,b) \right.$ Now fix a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right.$ in $\left. (a,b) \right.$ with $\left. \left( x_{n} \right) \right. \rightarrow a$. It follows from (a) that $g\left. \left( x_{n} \right) \right.$ converges, so let's *define* the value of $g\left. (a) \right. = \lim g\left. \left( x_{n} \right) \right.$.

Proving that $g$ is continuous at $a$ amounts to showing that if we now take an *arbitrary* [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( y_{n} \right) \right.$ that converges to $a$, then it follows that $g\left. (a) \right. = \lim g\left. \left( y_{n} \right) \right.$ as well. This is equivalent to showing that



$$
\lim\left. \left\lbrack g\left. \left( y_{n} \right) \right. - g\left. \left( x_{n} \right) \right. \right\rbrack \right. = 0
$$



Given $\epsilon > 0$, there exists a $\delta > 0$ such that $\left| g\left. (y) \right. - g\left. (x) \right. \right| < \epsilon$ whenever $|x - y| < \delta$. Because $\left. \left( x_{n} \right) \right.$ and $\left. \left( y_{n} \right) \right.$ each converge to $a$, we see that $\left. \left( y_{n} - x_{n} \right) \right. \rightarrow 0$. Thus, there exists an $N \in \mathbb{N}$ such that $\left| y_{n} - x_{n} \right| < \delta$ for all $n \geq N$. But this implies that 

$$
\left| g\left. \left( y_{n} \right) \right. - g\left. \left( x_{n} \right) \right. \right| < \epsilon\quad\mathrm{\text{for all }}n \geq N
$$



and we conclude that $\lim\left. \left\lbrack g\left. \left( y_{n} \right) \right. - g\left. \left( x_{n} \right) \right. \right\rbrack \right. = 0$. Because this implies that $g\left. (x) \right. = \lim g\left. \left( y_{n} \right) \right.$, we see that $g$ is continuous at $a$.

$\left. ( \Leftarrow ) \right.$: Given that $g$ can be continuously extended to the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $\left. \lbrack a,b\rbrack \right.$, we immediately get that $g$ is uniformly continuous because $\left. \lbrack a,b\rbrack \right.$ is a compact set. Thus $g$ is certainly uniformly continuous on the smaller set $\left. (a,b) \right.$.

## Extra Exercise 1

> Prove the [Extreme_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/extreme_value_theorem/).

Restating the [Extreme Value Theorem](/notes/areas/mathematics/real_analysis/definitions/extreme_value_theorem/):

> If $f:K \rightarrow \mathbb{R}$ is continuous on a compact set $K \subseteq \mathbb{R}$, then $f$ attains a maximum and minimum value. In other words, there exist $x_{0},x_{1} \in K$ such that $f\left. \left( x_{0} \right) \right. \leq f\left. (x) \right. \leq f\left. \left( x_{1} \right) \right.$ for all $x \in K$.

Proof: Because $f\left. (K) \right.$ is compact, we can set $\alpha = \sup f\left. (K) \right.$ and know $\alpha \in f\left. (K) \right.$ (Exercise 3.3.1). It follows that there exists $x_{1} \in K$ with $\alpha = f\left. \left( x_{1} \right) \right.$. The argument for the minimum value is similar.

# Section 4.5 Exercises

## Exercise 4.5.1

> Show how the [Intermediate_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/intermediate_value_theorem/) follows as a corollary to Theorem 4.5.2.

Restating Theorem 4.5.1:

> [Intermediate_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/intermediate_value_theorem/): If $f:\left. \lbrack a,b\rbrack \right. \rightarrow \mathbb{R}$ is continuous, and if $L$ is a real number satisfying $f\left. (a) \right. < L < f\left. (b) \right.$ or $f\left. (b) \right. > L > f\left. (b) \right.$, then there exists a point $c \in \left. (a,b) \right.$ where $f\left. (c) \right. = L$.

In other words, the IVT states that a continuous [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ on a closed interval $\left. \lbrack a,b\rbrack \right.$ attains every value that falls between the [range](/notes/areas/mathematics/set_theory/definitions/range/) values $f\left. (b) \right.$ and $f\left. (b) \right.$.

Restating Theorem 3.4.6:

> A set $E \subseteq \mathbb{R}$ is connected if and only if, for all non-empty disjoint sets $A$ and $B$ satisfying $E = A \cup B$, there always exists a convergent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( x_{n} \right) \right. \rightarrow x$ with $\left. \left( x_{n} \right) \right.$ contained in one of $A$ or $B$, and $x$ an element of the other.

Restating Theorem 4.5.2:

> Preservation of [Connected_Sets](/notes/areas/mathematics/real_analysis/definitions/connected_sets/): Let $f:G \rightarrow \mathbb{R}$ be continuous. If $E \subseteq G$ is connected, then $f\left. (E) \right.$ is connected as well.

In $\mathbb{R}$, a set is connected if and only if it is a (possibly unbounded) interval. We can combine this with Theorem 4.5.2 to prove the IVT.

The set $\left. \lbrack a,b\rbrack \right.$ is connected, and so by Theorem 4.5.2, the image set $f\left. \left( \left. \lbrack a,b\rbrack \right. \right) \right.$ is also connected. Because $f\left. (a) \right.$ and $f\left. (b) \right.$ are both elements of $f\left. \left( \left. \lbrack a,b\rbrack \right. \right) \right.$ (this is because $\left. \lbrack a,b\rbrack \right.$ is also compact, and by Theorem 4.4.1, $f\left. \left( \left. \lbrack a,b\rbrack \right. \right) \right.$ is compact and contains its limit points and thus $f\left. (a) \right.,f\left. (b) \right. \in f\left. \left( \left. \lbrack a,b\rbrack \right. \right) \right.$), we see that $L \in f\left. \left( \left. \lbrack a,b\rbrack \right. \right) \right.$ as well by Theorem 3.4.6. But this implies that there exists a point $c \in \left. (a,b) \right.$ satisfying $L = f\left. (c) \right.$, as desired.

## Exercise 4.5.3

> A [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ is increasing on $A$ if $f\left. (x) \right. \leq f\left. (y) \right.$ for all $x < y$ in $A$. Show that if $f$ is increasing on $\left. \lbrack a,b\rbrack \right.$ and satisfies the intermediate value property (Definition 4.5.3), then $f$ is continuous on $\left. \lbrack a,b\rbrack \right.$.

Restating Definition 4.5.3:

> A [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ has the intermediate value property on an interval $\left. \lbrack a,b\rbrack \right.$ if for all $x < y$ in $\left. \lbrack a,b\rbrack \right.$ and all $L$ between $f\left. (x) \right.$ and $f\left. (y) \right.$, it is always possible to find a point $c \in \left. (x,y) \right.$ where $f\left. (c) \right. = L$.

Let $\epsilon > 0$ be arbitrary. Because $f$ is uniformly continuous on $(a,b\rbrack$, there exists a $\delta_{1} > 0$ such that $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \epsilon/2$ whenever $x,y \in (a,b\rbrack$ satisfy $|x - y| < \delta_{1}$. Likewise, there exists $\delta_{2} > 0$ such that $|f\left. (x) \right. - f\left. (y) \right. < \epsilon/2$ whenever $x,y \in \lbrack b,c)$ satisfy $|x - y| < \delta_{2}$.

Now set $\delta = \min\{\delta_{1},\delta_{2}\}$ and assume we have $x$ and $y$ satisfying $|x - y| < \delta$. If both $x$ and $y$ fall in $(a,b\rbrack$, or if they both fall in $\lbrack b,c)$, then we get $\left| f\left. (x) \right. - f\left. (y) \right. \right| < \epsilon/2 < \epsilon$. In the case where $x < b$ and $y > b$ we may write



$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| \leq \left| f\left. (x) \right. - f\left. (b) \right. \right| + \left| f\left. (b) \right. - f\left. (y) \right. \right| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
$$



Because $\delta_{1}$ and $\delta_{2}$ are both independent of $x$ and $y$, $\delta$ is as well and we conclude that $f$ is uniformly continuous on $\left. (a,c) \right.$.

## Exercise 4.5.5

### (a)

> Finish the proof of the [Intermediate_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/intermediate_value_theorem/) using the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/) started previously.

Proceed via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/), and assume that $f\left. (c) \right. > 0$. If we set $(\epsilon)_{0} = f\left. (c) \right.$, then the [continuity](/notes/areas/mathematics/real_analysis/definitions/continuity/) of $f$ implies that there exists a $\delta_{0} > 0$ with the property that $x \in V_{\delta_{0}}\left. (c) \right.$ implies that $f\left. (x) \right. \in V_{(\epsilon)_{0}}\left. \left( f\left. (c) \right. \right) \right.$. But this implies that $f\left. (x) \right. > 0$ and thus $x \in K$ for all $x \in V_{\delta_{0}}\left. (c) \right.$. What this means is that if $c$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) on $K$, then $c - \delta_{0}$ is a smaller [upper bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/), violating the definition of the supremeum. We conclude that $f\left. (x) \right. > 0$ is not allowed.

Now assume $f\left. (c) \right. < 0$. This time, the [continuity](/notes/areas/mathematics/real_analysis/definitions/continuity/) of $f$ allows us to produce a neighborhood $V_{\delta_{1}}\left. (c) \right.$ where $x \in V_{\delta_{1}}\left. (c) \right.$ implies $f\left. (x) \right. < 0$. But this implies that a point such as $c + \delta_{1}/2$ is an element of K, violating the fact that $c$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $K$.

It follows that $f\left. (c) \right. < 0$ is also impossible, and we conclude that $f\left. (c) \right. = 0$ as desired.

This proves the [Intermediate_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/intermediate_value_theorem/) for the special case where $L = 0$. To prove the more general version, we consider the auxiliary [function](/notes/areas/mathematics/set_theory/definitions/function/) $h\left. (x) \right. = f\left. (x) \right. - L$ which is certainly continuous. From the special case just considered, we know that $h\left. (c) \right. = 0$ for some point $c \in \left. (a,b) \right.$ from which it follows that $f\left. (c) \right. = L$.

### (b)

> Finish the proof of the [Intermediate_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/intermediate_value_theorem/) using the [Nested_Interval_Property](/notes/areas/mathematics/real_analysis/definitions/nested_interval_property/) started previously.

By repeating the construction started in the text, we get a nested [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of intervals $I_{n} = \left. \left\lbrack a_{n},b_{n} \right\rbrack \right.$ where $f\left. \left( a_{n} \right) \right. < 0$ and $f\left. \left( b_{n} \right) \right. \geq 0$ for all $n \in \mathbb{N}$. By the [Nested Interval Property](/notes/areas/mathematics/real_analysis/definitions/nested_interval_property/), there exists a point $c \in \cap_{n = 1}^{\infty}I_{n}$. The fact that the lengths of the intervals are tending to zero means that the two [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s $\left. \left( a_{n} \right) \right.$ and $\left. \left( b_{n} \right) \right.$ each converge to $c$.

Because $f$ is continuous at $c$, we get $f\left. (c) \right. = \lim f\left. \left( a_{n} \right) \right.$ where $f\left. \left( a_{n} \right) \right. < 0$ for all $n$. Then the [Order_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/order_limit_theorem/) implies that $f\left. (c) \right. \leq 0$. Because we also have $f\left. (c) \right. = \lim f\left. \left( b_{n} \right) \right.$ with $f\left. \left( b_{n} \right) \right. \geq 0$, it must be that $f\left. (c) \right. \geq 0$. We conclude that $f\left. (c) \right. = 0$.

## Exercise 4.5.7

> Let $f$ be a continuous [function](/notes/areas/mathematics/set_theory/definitions/function/) on the closed interval $\left. \lbrack 0,1\rbrack \right.$ with [range](/notes/areas/mathematics/set_theory/definitions/range/) also contained in $\left. \lbrack 0,1\rbrack \right.$. Prove that $f$ must have a fixed point; that is, show $f\left. (x) \right. = x$ for at least one value of $x \in \left. \lbrack 0,1\rbrack \right.$.

Apply the [Intermediate_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/intermediate_value_theorem/) to the [function](/notes/areas/mathematics/set_theory/definitions/function/) $g\left. (x) \right. = f\left. (x) \right. - x$. Because the [range](/notes/areas/mathematics/set_theory/definitions/range/) of $f$ is contained in the interval $\left. \lbrack 0,1\rbrack \right.$, we see that



$$
g\left. (0) \right. = f\left. (0) \right. \geq 0\quad\mathrm{\text{and}}\quad g\left. (1) \right. = g\left. (1) \right. - 1 \leq 0
$$



It follows from IVT that we must have $g\left. (c) \right. = 0$ for some point $c \in \left. \lbrack 0,1\rbrack \right.$. This is equivalent to $f\left. (c) \right. = c$.

# Section 4.6 Exercises

## Exercise 4.6.1

> Using modifications of these functions, construct a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:\mathbb{R} \rightarrow \mathbb{R}$ so that

### (a)

> $D_{f} = \mathbb{Z}^{c}$

See 4.3.11. The greatest integer [function](/notes/areas/mathematics/set_theory/definitions/function/) $h\left. (x) \right. = \text{ GIF }\left. (x) \right.$ suffices here.

### (b)

> $D_{f} = \{ x:0 < x \leq 1\}$

## Exercise 4.6.3

> State a similar definition for the left-hand limit
>
> 

$$
\lim\limits_{x \rightarrow c^{-}}f\left. (x) \right. = L
$$



We say that $\lim\limits_{x \rightarrow c^{-}f\left. (x) \right. = L}$ if for all $\epsilon > 0$ there exists a $\delta > 0$ such that $f\left. (x) \right. - L| < \epsilon$ whenever $0 < c - x < \delta$. Note the subtle difference between Definition 4.2.1 and Definition 4.6.2.

## Exercise 4.6.5

> Prove that the only type of discontinuity a monotone [function](/notes/areas/mathematics/set_theory/definitions/function/) can have is a jump discontinuity.

This argument is similar to the proof for the [Monotone_Convergence_Theorem](/notes/areas/mathematics/real_analysis/definitions/monotone_convergence_theorem/).

Given $c \in \mathbb{R}$, let's prove that $\lim\limits_{x \rightarrow c^{-}}f\left. (x) \right.$ exists for an increasing [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$. Our first task is to produce a candidate for the value of the limit. To this end, set



$$
A = \{ f\left. (x) \right.:x < c\}
$$



Because $f$ is increasing, $A$ is bounded above by $f\left. (c) \right.$. By the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/), we can set $L = \sup A$. The claim is that $\lim\limits_{x \rightarrow c^{-}}f\left. (x) \right. = L$.

Let $\epsilon > 0$. By the least upper bound property of the [supremum](/notes/areas/mathematics/real_analysis/definitions/supremum/), we know that there exists an $x_{0} < c$ satisfying



$$
L - \epsilon < f\left. \left( x_{0} \right) \right. \leq L
$$



If we set $\delta = c - x_{0}$, then the fact that $f$ is increasing implies that



$$
L - \epsilon < f\left. \left( x_{0} \right) \right. \leq f\left. (x) \right. \leq L
$$



whenever $0 < c - x < \delta$. This proves the claim.

Similarly, for the right-hand limit, we have a similar argument



$$
\lim\limits_{x \rightarrow c^{+}}f\left. (x) \right. = L'
$$



where $L' = \inf\{ f\left. (x) \right.:x > c\}$. A final con[sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of this argument is that the value of the [function](/notes/areas/mathematics/set_theory/definitions/function/) at $c$ must satisfy



$$
L \leq f\left. (c) \right. \leq L'
$$



If $L = L'$ then $f$ is continuous at $c$, and if $L < L'$ then we have a jump discontinuity. There are no other possibilities.

## Exercise 4.6.7

### (a)

> Show that for each of the [Dirichlet_function](/notes/areas/mathematics/real_analysis/definitions/dirichlet_function/), the modified [Dirichlet_function](/notes/areas/mathematics/real_analysis/definitions/dirichlet_function/), and the [Thomae_function](/notes/areas/mathematics/real_analysis/definitions/thomae_function/), we get an $F_{\sigma}$ set as the set where the [function](/notes/areas/mathematics/set_theory/definitions/function/) is discontinuous.

Restating Definition 4.6.4:

> A set that can be written as the [countable](/notes/areas/mathematics/set_theory/definitions/countable/) union of closed sets is in the class of $F_{\sigma}$.

### (b)

> Show that the two sets of discontinuity in Exercise 4.6.1 are $F_{\sigma}$.

## Exercise 4.6.9

> If $\alpha < \alpha'$, show that $D_{f}^{\alpha'} \subseteq D_{f}^{\alpha}$.

## Exercise 4.6.11

> Show that if $f$ is not continuous at $x$, then $f$ is not $\alpha$-continuous for some $\alpha > 0$. Now explain why this guarantees that
>
> 

$$
D_{f} = \bigcap_{n = 1}^{\infty}D_{f}^{\alpha_{n}}
$$


>
> where $\alpha_{n} = 1/n$.

# Section 5.2 Exercises

## Exercise 5.2.1

> Supply proofs for parts (i) and (ii) of Theorem 5.2.4 ([Algebraic_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_differentiability_theorem/)).

Restating Theorem 4.2.4

> [Algebraic_Limit_Theorem_for_Functional_Limits](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem_for_functional_limits/): Let $f$ and $g$ be functions defined on a [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $A \subseteq \mathbb{R}$, and assume $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$ and $\lim\limits_{x \rightarrow c}g\left. (x) \right. = M$ for some limit point $c$ of $A$. Then,
>
> 1.  $\lim\limits_{x \rightarrow c}kf\left. (x) \right. = kL$ for all $k \in \mathbb{R}$
>
> 2.  $\lim\limits_{x \rightarrow c}\left. \left\lbrack f\left. (x) \right. + g\left. (x) \right. \right\rbrack \right. = L + M$
>
> 3.  $\lim\limits_{x \rightarrow c}\left. \left\lbrack f\left. (x) \right.g\left. (x) \right. \right\rbrack \right. = LM$
>
> 4.  $\lim\limits_{x \rightarrow c}\left. \left\lbrack f\left. (x) \right./g\left. (x) \right. \right\rbrack \right. = L/M$, provided that $M \neq 0$

Restating Theorem 5.2.4:

> [Algebraic_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_differentiability_theorem/): Let $f$ and $g$ be functions defined on an interval $A$, and assume both are [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at some point $c \in A$. Then,
>
> 1.  $\left. (f + g) \right.'\left. (c) \right. = f'\left. (c) \right. + g'\left. (c) \right.$
>
> 2.  $\left. (kf) \right.'\left. (c) \right. = kf'\left. (c) \right.$, for all $k \in \mathbb{R}$
>
> 3.  $\left. (fg) \right.'\left. (c) \right. = f'\left. (c) \right.g\left. (c) \right. + f\left. (c) \right.g'\left. (c) \right.$
>
> 4.  $\left. (f/g) \right.'\left. (c) \right. = \frac{g\left. (c) \right.f'\left. (c) \right. - f\left. (c) \right.g'\left. (c) \right.}{\left. \left\lbrack g\left. (c) \right. \right\rbrack \right.^{2}}$, provided that $g\left. (c) \right. \neq 0$

For part (i) we apply the difference quotient:



$$
\begin{aligned}
\left. (f + g) \right.'\left. (c) \right. & = \frac{\left. (f + g) \right.\left. (x) \right. - \left. (f + g) \right.\left. (c) \right.}{x - c} \\
 & = \frac{f\left. (x) \right. + g\left. (x) \right. - f\left. (c) \right. - g\left. (c) \right.}{x - c} \\
 & = \frac{f\left. (x) \right. - f\left. (c) \right.}{x - c} + \frac{g\left. (x) \right. - g\left. (c) \right.}{x - c}
\end{aligned}
$$



The fact that $f$ and $g$ are [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $c$ together with the functional-limit version of the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/) (Theorem 4.2.4) justifies the conclusion that



$$
\left. (f + g) \right.'\left. (c) \right. = f'\left. (c) \right. + g'\left. (c) \right.
$$



For part (ii), again apply the difference quotient:



$$
\begin{aligned}
\left. (kf) \right.'\left. (c) \right. & = \frac{kf\left. (x) \right. - kf\left. (c) \right.}{x - c} \\
 & = k\left. \left( \frac{f\left. (x) \right. - f\left. (c) \right.}{x - c} \right) \right.
\end{aligned}
$$



The fact that $f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $c$ together with the functional-limit version of the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/) (Theorem 4.2.4) justifies the conclusion that



$$
\left. (kf) \right.'\left. (c) \right. = kf'\left. (c) \right.
$$



## Exercise 5.2.3

### (a)

> Use Definition 5.2.1 to produce the proper formula for the derivative of $h\left. (x) \right. = 1/x$.

Restating Definition 5.2.1:

> Differentiability: Let $g:A \rightarrow \mathbb{R}$ be a [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on an interval $A$. Given $c \in A$, the derivative of $g$ at $c$ is defined by
>
> 

$$
g'\left. (c) \right. = \lim\limits_{x \rightarrow c}\frac{g\left. (x) \right. - g\left. (c) \right.}{x - c}
$$


>
> provided this limit exists. In this case we say that $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $c$. If $g'$ exists for all points $c \in A$, we say that $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $A$.

For $c \neq 0$, the derivative of $f$ at $c$ is given by the formula



$$
\begin{aligned}
f'\left. (c) \right. & = \lim\limits_{x \rightarrow c}\frac{1/x - 1/c}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{\left. (c - x) \right./xc}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{- 1}{xc} \\
 & = - \frac{1}{c^{2}}
\end{aligned}
$$



### (b)

> Combine the result in part (a) with the Chain Rule (Theorem 5.2.5) to supply a proof for part (iv) of Theorem 5.2.4 ([Algebraic_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_differentiability_theorem/)).

Restating Theorem 5.2.5:

> Chain Rule: Let $f:A \rightarrow \mathbb{R}$ and $g:B \rightarrow \mathbb{R}$ satisfy $f\left. (a) \right. \subseteq B$ so that the composition $g \circ f$ is defined. If $f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $c \in A$ and if $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $f\left. (c) \right. \in B$, then $g \circ f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $c$ with $\left. (g \circ f) \right.'\left. (c) \right. = g'\left. \left( f\left. (c) \right. \right) \right. \cdot f'\left. (c) \right.$

Let $h\left. (x) \right. = 1/x$. Then by the Chain Rule (or the [Reciprocal Rule](https://en.wikipedia.org/wiki/Reciprocal_rule)),



$$
\left. \left( \frac{1}{g\left. (x) \right.} \right) \right.' = \left. (h \circ g) \right.'\left. (x) \right. = - \frac{g'\left. (x) \right.}{\left. \left\lbrack g\left. (x) \right. \right\rbrack \right.^{2}\rbrack}
$$



Then using the product rule (Theorem 5.2.4 (iii)), we have



$$
\begin{aligned}
\left. \left( \frac{f}{g} \right) \right.'\left. (x) \right. = \left. \left\lbrack f\left. (x) \right.\left. (h \circ g) \right.\left. (x) \right. \right\rbrack \right.' & = f'\left. (x) \right.\left. (h \circ g) \right.\left. (x) \right. + f\left. (x) \right.\left. (h \circ g) \right.'\left. (x) \right. \\
 & = \frac{f'\left. (x) \right.}{g\left. (x) \right.} - \frac{f\left. (x) \right.g'\left. (x) \right.}{\left. \left\lbrack g\left. (x) \right. \right\rbrack \right.^{2}} \\
 & = \frac{g\left. (x) \right.f'\left. (x) \right. - f\left. (x) \right.g'\left. (x) \right.}{\left. \left\lbrack g\left. (x) \right. \right\rbrack \right.^{2}}
\end{aligned}
$$



provided that $g\left. (c) \right. \neq 0$.

### (c)

> Supply a direct proof of Theorem 5.2.4 (iv) by algebraically manipulating the difference quotient for $\left. (f/g) \right.$ in a style similar to the proof of theorem 5.2.4 (iii).

Rewrite the difference quotient as



$$
\begin{aligned}
\frac{\left. (f/g) \right.\left. (x) \right. - \left. (f/g) \right.\left. (c) \right.}{x - c} & = \frac{1}{x - c}\left. \left( \frac{f\left. (x) \right.}{g\left. (x) \right.} - \frac{f\left. (c) \right.}{g\left. (c) \right.} \right) \right. \\
 & = \frac{1}{x - c}\left. \left( \frac{f\left. (x) \right.g\left. (c) \right. - f\left. (c) \right.g\left. (x) \right.}{g\left. (x) \right.g\left. (c) \right.} \right) \right. \\
 & = \frac{1}{x - c}\left. \left( \frac{f\left. (x) \right.g\left. (c) \right. - f\left. (c) \right.g\left. (c) \right. + f\left. (c) \right.g\left. (c) \right. - f\left. (c) \right.g\left. (x) \right.}{g\left. (x) \right.g\left. (c) \right.} \right) \right. \\
 & = \frac{1}{g\left. (x) \right.g\left. (c) \right.}\left. \left( g\left. (c) \right.\frac{f\left. (x) \right. - f\left. (c) \right.}{x - c} - f\left. (c) \right.\frac{g\left. (x) \right. - g\left. (c) \right.}{x - c} \right) \right.
\end{aligned}
$$



Applying the [Algebraic_Theorem_for_Functional_Limits](/notes/areas/mathematics/real_analysis/definitions/algebraic_theorem_for_functional_limits/) gives



$$
\left. \left( \frac{f}{g} \right) \right.'\left. (c) \right. = \frac{1}{\left. \left\lbrack g\left. (c) \right. \right\rbrack \right.^{2}}\left. \left( g\left. (c) \right.f'\left. (c) \right. - f\left. (c) \right.g'\left. (c) \right. \right) \right.
$$



which gives the result.

## Exercise 5.2.5

> Let 

$$
f_{a}\left. (x) \right. = \begin{cases}
x^{a} & \mathrm{\text{if }}x > 0 \\
0 & \mathrm{\text{if }}x \leq 0
\end{cases}
$$



### (a)

> For which values of $a$ is $f$ continuous at zero?

From the left of zero we have $\lim\limits_{x \rightarrow 0^{-}}f\left. (x) \right. = 0$, so we require that $\lim\limits_{x \rightarrow 0^{+}}x^{a} = 0$ as well. This occurs if and only if $a > 0$.

### (b)

> For which values of $a$ is $f$ [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at zero? In this case, is the derivative [function](/notes/areas/mathematics/set_theory/definitions/function/) continuous?

From part (a) we know that $f_{a}\left. (0) \right. = 0$. For $f_{a}'\left. (0) \right.$ we again begin by considering the limit from the left and see that



$$
\lim\limits_{x \rightarrow 0^{-}}\frac{f_{a}\left. (x) \right. - f_{a}\left. (0) \right.}{x - 0} = \lim\limits_{x \rightarrow 0^{-}}\frac{0}{x} = 0
$$



Thus we require that



$$
\lim\limits_{x \rightarrow 0^{+}}\frac{x^{a}}{x} = \lim\limits_{x \rightarrow 0^{+}}x^{a - 1} = 0
$$



as well. This occurs if and only if $a > 1$. The derivative formula $\left. \left( x^{a} \right) \right.' = ax^{a - 1}$ (which we have not justified for $a \notin \mathbb{N}$) shows that $f_{a}'\left. (x) \right.$ is continuous in this case.

### (c)

> For which values of $a$ is $f$ twice-differentiable?

Because we continue to get zero on the left, for the second derivative to exist we must have



$$
\lim\limits_{x \rightarrow 0^{+}}\frac{\left. \left( x^{a} \right) \right.' - 0}{x - 0} = \lim\limits_{x \rightarrow 0^{+}}\frac{ax^{a - 1}}{x} = \lim\limits_{x \rightarrow 0^{+}}ax^{a - 2} = 0
$$



This occurs whenever $a > 2$.

## Exercise 5.2.7

> Let 

$$
g_{a}\left. (x) \right. = \begin{cases}
x^{a}\sin\left. (1/x) \right. & \mathrm{\text{if }}x \neq 0 \\
0 & \mathrm{\text{if }}x = 0
\end{cases}
$$

 Find a particular (potentially non-integer) value for $a$ so that

### (a)

> $g_{a}$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\mathbb{R}$ but such that $g_{a}'$ is unbounded on $\left. \lbrack 0,1\rbrack \right.$

With regards to the existence of $g_{a}'\left. (x) \right.$ at $x = 0$ we see that



$$
g_{a}'\left. (0) \right. = \lim\limits_{x \rightarrow 0}\frac{x^{a}\sin\left. (1/x) \right.}{x} = \lim\limits_{x \rightarrow 0}a^{a - 1}\sin\left. (1/x) \right. = 0
$$



as long as $a > 1$. For $x \neq 0$, $g_{a}'\left. (x) \right.$ always exists and using the standard rules of differentiation we get



$$
g_{a}'\left. (x) \right. = - x^{a - 2}\cos\left. (1/x) \right. + ax^{a - 1}\sin\left. (1/x) \right.
$$



Setting $1 < a < 2$ makes $x^{a - 2}\cos\left. (1/x) \right.$ unbounded near zero and yields the desired function.

### (b)

> $g_{a}$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\mathbb{R}$ with $g_{a}'$ continuous but not [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at zero.

For $g_{a}'\left. (x) \right.$ to be continuous we need



$$
\lim\limits_{x \rightarrow 0}g_{a}'\left. (x) \right. = g_{a}'\left. (x) \right. = 0
$$



and, looking at the above expression for $g_{a}'\left. (x) \right.$, we see that this happens as long as $a > 2$. For the second derivative $g_{a}''\left. (0) \right.$ we consider the limit



$$
\begin{aligned}
g_{a}''\left. (0) \right. = \lim\limits_{x \rightarrow 0}\frac{g_{a}'\left. (x) \right.}{x} & = \lim\limits_{x \rightarrow 0}\left. \left( \frac{1}{x} \right) \right.\left. \left( - x^{a - 2}\cos\left. (1/x) \right. + ax^{a - 1}\sin\left. (1/x) \right. \right) \right. \\
 & = \lim\limits_{x \rightarrow 0}\left. \left( - x^{a - 3}\cos\left. (1/x) \right. + ax^{a - 2}\sin\left. (1/x) \right. \right) \right.
\end{aligned}
$$



which exists if and only if $a > 3$. Thus setting $2 < a \leq 3$ gives the desired function.

### (c)

> $g_{a}$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\mathbb{R}$ and $g_{a}'$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\mathbb{R}$, but such that $g_{a}''$ is not continuous at zero.

From (b) se wee that choosing $a > 3$ makes $g_{a}'$ [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at zero. Away from zero we get



$$
g_{a}''\left. (x) \right. - x^{a - 4}\sin\left. (1/x) \right. - \left. (2a - 2) \right.x^{a - 3}\cos\left. (1/x) \right. + a\left. (a - 1) \right.x^{a - 2}\sin\left. (1/x) \right.
$$



which fails to be continuous at zero when $a \leq 4$. Setting $3 < a \leq 4$ gives the desired function.

## Exercise 5.2.9

> Decide whether each conjecture is true or false. Provide an argument for those that are true and a counterexample for each one that is false.

### (a)

> If $f'$ exists on an interval and is not constant, then $f'$ must take on some irrational values.

Although the derivative [function](/notes/areas/mathematics/set_theory/definitions/function/) need not be continuous, it does satisfy the intermediate value property. Thus, if the derivative of a [function](/notes/areas/mathematics/set_theory/definitions/function/) takes on two distinct values then it attains every value both rational and irrational in between these two.

### (b)

> If $f'$ exists on an open interval and there is some point $c$ where $f'\left. (c) \right. > 0$, then there exists a $\delta$-neighborhood $V_{\delta}\left. (c) \right.$ around $c$ in which $f'\left. (x) \right. > 0$ for all $x \in V_{\delta}\left. (c) \right.$.

False. Consider



$$
f\left. (x) \right. = \begin{cases}
x/2 + x^{2}\sin\left. (1/x) \right. & \mathrm{\text{if }}x \neq 0 \\
0 & \mathrm{\text{if }}x = 0
\end{cases}
$$



At zero we can show that $f'\left. (0) \right. = 1/2$. Away from zero we get



$$
f'\left. (x) \right. = 1/2 - \cos\left. (1/x) \right. + 2x\sin\left. (1/x) \right.
$$



which takes on negative values in every $\delta$-neighborhood of zero.

### (c)

> If $f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on an interval containing zero and if $\lim\limits_{x \rightarrow 0}f'\left. (x) \right. = L$, then it must be that $L = f'\left. (0) \right.$.

True. Proceed by contradiction. Assume that $L \neq f'\left. (0) \right.$ and choose $(\epsilon)_{0} > 0$ so that $(\epsilon)_{0} < \left| f'\left. (0) \right. - L \right|$. From the hypothesis that $\lim\limits_{x \rightarrow 0}f'\left. (x) \right. = L$ we know there exists a $\delta > 0$ such that $0 < |x| < \delta$ implies that $\left| f'\left. (x) \right. - L \right| < (\epsilon)_{0}$. Now our choice of $(\epsilon)_{0}$ guarantees that there exists a point $\alpha$ between $f'\left. (0) \right.$ and $L$ but outside $V_{(\epsilon)_{0}}\left. (L) \right.$. However, by Darboux's Theorem, there exists a point $x \in V_{\delta}$ such that $f'\left. (x) \right. = \alpha$. This suggests that $\alpha \in V_{(\epsilon)_{0}}\left. (L) \right.$, which is a contradiction. Therefore $L = f'\left. (0) \right.$.

## Exercise 5.2.11

> Assume that $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\left. \lbrack a,b\rbrack \right.$ and satisfies $g'\left. (a) \right. < 0 < g'\left. (b) \right.$.

### (a)

> Show that there exists a point $x \in \left. (a,b) \right.$ where $g\left. (a) \right. > g\left. (x) \right.$ and a point $y \in \left. (a,b) \right.$ where $g\left. (y) \right. < g\left. (b) \right.$.

First, let's prove that there exists $x \in \left. (a,b) \right.$ where $g\left. (x) \right. < g\left. (a) \right.$. Let $\left. \left( x_{n} \right) \right.$ be a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) in $\left. (a,b) \right.$ satisfying $\left. \left( x_{n} \right) \right. \rightarrow a$. Then we have



$$
g'\left. (a) \right. = \lim\limits_{n \rightarrow \infty}\frac{g\left. \left( x_{n} \right) \right. - g\left. (a) \right.}{x_{n} - a} < 0
$$



The denominator is always positive. If the numerator were always positive then the [Order_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/order_limit_theorem/) would imply $g'\left. (a) \right. \geq 0$. Because we know this is not the case, we may conclude that the numerator is eventually negative and thus $g\left. (x) \right. < g\left. (a) \right.$ for some $x$ near $a$.

The proof that there exists $y \in \left. (a,b) \right.$ where $g\left. (y) \right. < g\left. (b) \right.$

> Now complete the proof of Darboux's Theorem started earlier.

We must show that $g'\left. (c) \right. = 0$ for some $c \in \left. (a,b) \right.$. Because $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on the compact set $\left. \lbrack a,b\rbrack \right.$ it must also be continuous here, and so by the [Extreme_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/extreme_value_theorem/) (Theorem 4.4.2), $g$ attains a minimum at a point $c \in \left. \lbrack a,b\rbrack \right.$. From our work in (a) we know that the minimum of $g$ is neither $g\left. (a) \right.$ nor $g\left. (b) \right.$, and therefore $c \in \left. (a,b) \right.$. Finally, the [Interior_Extremum_Theorem](/notes/areas/mathematics/real_analysis/definitions/interior_extremum_theorem/) (Theorem 5.2.6) allows us to conclude that $g'\left. (c) \right. = 0$.

To prove the general result stated in the theorem we just observe that $g'\left. (c) \right. = 0$ is equivalent to the conclusion $f'\left. (c) \right. = \alpha$.

# Section 5.3 Exercises

## Exercise 5.3.1

> Recall from Exercise 4.4.9 that a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:A \rightarrow \mathbb{R}$ is Lipschitz on $A$ if there exists an $M > 0$ such that
>
> 

$$
\left| \frac{f\left. (x) \right. - f\left. (y) \right.}{x - y} \right| \leq M
$$


>
> for all $x \neq y \in A$

### (a)

> Show that if $f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on a closed interval $\left. \lbrack a,b\rbrack \right.$ and if $f'$ continuous on $\left. \lbrack a,b\rbrack \right.$, then $f$ is Lipschitz on $\left. \lbrack a,b\rbrack \right.$.

Assume that $f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) and that $f'$ is continuous on the compact set $\left. \lbrack a,b\rbrack \right.$. We need to show that $f$ is Lipschitz on $\left. \lbrack a,b\rbrack \right.$.

By the [Extreme_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/extreme_value_theorem/), since $f'$ is continuous on the compact set $\left. \lbrack a,b\rbrack \right.$, we know that $f'$ attains a maximum and minimum value (i.e., it is bounded). Thus, there exists some $M > 0$ such that $\left| f'\left. (x) \right. \right| \leq M$ for all $x \in \left. \lbrack a,b\rbrack \right.$.

Now, given $x < y$ in the interval $\left. \lbrack a,b\rbrack \right.$, the [Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/) says that there exists a point $c \in \left. (a,b) \right.$ for which



$$
f'\left. (c) \right. = \frac{f\left. (x) \right. - f\left. (y) \right.}{x - y}
$$



Because $\left| f'\left. (c) \right. \right| \leq M$ (regardless of the value of $c$), it follows that



$$
\left| \frac{f\left. (x) \right. - f\left. (y) \right.}{x - y} \right| \leq M
$$



### (b)

> Review the definition of a contractive [function](/notes/areas/mathematics/set_theory/definitions/function/) in Exercise 4.3.11. If we add the assumption that $\left| f'\left. (x) \right. \right| < 1$ on $\left. \lbrack a,b\rbrack \right.$, does it follow that $f$ is contractive on this set?

Because $f'$ is continuous on a compact set $I$, the [Extreme_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/extreme_value_theorem/) can be applied to conclude that $f'\left. (c) \right.$ attains a maximum and a minimum value on $I$. Thinking in terms of absolute value, this means that there exists a point $x_{0} \in I$ where $\left| f'\left. (x) \right. \right| \leq \left| f'\left. \left( x_{0} \right) \right. \right|$ for all $x \in I$. Setting $s = \left| f'\left. \left( x_{0} \right) \right. \right|$, we see from our hypothesis that $0 \leq s < 1$.

Now, given $x < y$ in $I$, the [Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/) tells us that there exists a point $c \in I$ where



$$
\left| \frac{f\left. (x) \right. - f\left. (y) \right.}{x - y} \right| = \left| f'\left. (c) \right. \right| \leq \left| f'\left. \left( x_{0} \right) \right. \right| = s
$$



It follows that



$$
\left| f\left. (x) \right. - f\left. (y) \right. \right| \leq s|x - y|
$$



and thus $f$ is contractive on $I$.

## Exercise 5.3.3

> Let $h$ be a [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on the interval $\left. \lbrack 0,3\rbrack \right.$, and assume that $h\left. (0) \right. = 1,h\left. (1) \right. = 2$, and $h\left. (3) \right. = 2$.

### (a)

> Argue that there exists a piont $d \in \left. \lbrack 0,3\rbrack \right.$ where $h\left. (d) \right. = d$

Set $g\left. (x) \right. = x - h\left. (x) \right.$. Because $g\left. (1) \right. = - 1$ and $g\left. (3) \right. = 1$, by the [Intermediate Value Theorem](/notes/areas/mathematics/real_analysis/definitions/intermediate_value_theorem/), there must exist a $d \in \left. \lbrack 0,3\rbrack \right.$ where $g\left. (d) \right. = 0$. In terms of $h$, we note that this implies that $h\left. (d) \right. = d$, as desired.

### (b)

> Argue that at some piont $c$ we have $h'\left. (c) \right. = 1/3$.

Applying the [Mean Value Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/) to $h$ on the interval $\left. \lbrack 0,3\rbrack \right.$ implies that there exists a point $c \in \left. (0,3) \right.$ where



$$
h'\left. (c) \right. = \frac{h\left. (3) \right. - h\left. (0) \right.}{3 - 0} = \frac{2 - 1}{3} = \frac{1}{3}
$$



### (c)

> Argue that $h'\left. (x) \right. = 1/4$ at some point in the [domain](/notes/areas/mathematics/set_theory/definitions/domain/)

Applying Rolle's Theorem to $h$ on the interval $\left. \lbrack 1,3\rbrack \right.$, we see that there must exist a point $a' \in \left. (1,3) \right.$ where $h'\left. (a) \right. = 0$. In (b), we found a point where $h'\left. (c) \right. = 1/3$. Because $1/4$ falls between $0$ and $1/3$, we can appeal to Darboux's Theorem to assert that $h'\left. (x) \right. = 1/4$ at some point between $c$ and $a$.

## Exercise 5.3.5

### (a)

> Supply the details for the proof of Cauchy's [Generalized_Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/generalized_mean_value_theorem/) (Theorem 5.3.5).

Let



$$
h\left. (x) \right. = \left. \left\lbrack f\left. (b) \right. - f\left. (a) \right. \right\rbrack \right.g\left. (x) \right. - \left. \left\lbrack g\left. (b) \right. - g\left. (a) \right. \right\rbrack \right.f\left. (x) \right.
$$



From the set of algebraic limit theorems presented previously, we know that $h$ is continuous on $\left. \lbrack a,b\rbrack \right.$ and [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\left. (a,b) \right.$. We also have $h\left. (a) \right. = g\left. (a) \right.f\left. (b) \right. - f\left. (a) \right.g\left. (b) \right. = h\left. (b) \right.$. Thus, by Rolle's Theorem, there exists a $c \in \left. (a,b) \right.$ where $h'\left. (c) \right. = 0$. Because



$$
h'\left. (x) \right. = \left. \left\lbrack f\left. (b) \right. - f\left. (a) \right. \right\rbrack \right.g'\left. (x) \right. - \left. \left\lbrack g\left. (b) \right. - g\left. (a) \right. \right\rbrack \right.f'\left. (x) \right. = 0
$$



we see that



$$
\left. \left\lbrack f\left. (b) \right. - f\left. (a) \right. \right\rbrack \right.g'\left. (c) \right. - \left. \left\lbrack g\left. (b) \right. - g\left. (a) \right. \right\rbrack \right.f'\left. (c) \right. = 0
$$



and the result follows.

### (b)

> Give a graphical interpretation of the [Generalized_Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/generalized_mean_value_theorem/) analogous to the one given for the [Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/) at the beginning of Section 5.3. (Consider $f$ and $g$ as parametric equations for a curve.)

Set $x = g\left. (t) \right.$ and $y = f\left. (t) \right.$ and consider the parametric curve in the $x - y$ plane drawn as $t$ ranges over the interval $\left. \lbrack a,b\rbrack \right.$. The quantity $\left. \left\lbrack f\left. (b) \right. - f\left. (a) \right. \right\rbrack \right./\left. \left\lbrack g\left. (b) \right. - g\left. (a) \right. \right\rbrack \right.$ corresponds to the slope of the segment joining the endpoints of this curve, while $f'\left. (c) \right./g'\left. (c) \right.$ gives the slope of the line tangent to the curve at the point $\left. \left( g\left. (c) \right.,f\left. (c) \right. \right) \right.$. In this context, the [Generalized_Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/generalized_mean_value_theorem/) says that if $g'$ is never zero, then at some point along the parametric curve, the tangent line must be parallel to the segment joining the two endpoints.

## Exercise 5.3.7

> A fixed point of a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ is a value $x$ where $f\left. (x) \right. = x$. Show that if $f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on an interval with $f'\left. (x) \right. \neq 1$, then $f$ can have at most one fixed point.

Proceed by contraction. Assume that $f$ has two distinct fixed points $x_{1}$ and $x_{2}$. Noting that $f\left. \left( x_{1} \right) \right. = x_{1}$ and $f\left. \left( x_{2} \right) \right. = x_{2}$, the [Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/) implies that there exists $c$ where



$$
f'\left. (c) \right. = \frac{f\left. \left( x_{1} \right) \right. - f\left. \left( x_{2} \right) \right.}{x_{1} - x_{2}} = \frac{x_{1} - x_{2}}{x_{1} - x_{2}} = 1
$$



Because this is impossible, we conclude that $f$ can have at most one fixed point.

## Exercise 5.3.9

> Assume $f$ and $g$ are as described in Theorem 5.3.6, but now add the assumption that $f$ and $g$ are [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $a$, and $f'$ and $g'$ are continuous at a with $g'\left. (a) \right. \neq 0$. Find a short proof for the $0/0$ case of [L'Hospital's_Rule](/notes/areas/mathematics/real_analysis/definitions/lhospitals_rule/) under this stronger hypothesis.

For all $x \neq a$ we



$$
\frac{f\left. (x) \right.}{g\left. (x) \right.} = \frac{f\left. (x) \right. - f\left. (a) \right.}{g\left. (x) \right. - g\left. (a) \right.} = \frac{\left. \left( f\left. (x) \right. - f\left. (a) \right. \right) \right./\left. (x - a) \right.}{\left. \left( g\left. (x) \right. - g\left. (a) \right. \right) \right./\left. (x - a) \right.}
$$



Because $f$ and $g$ are [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at $a$, we may use the [Algebraic_Limit_Theorem](/notes/areas/mathematics/real_analysis/definitions/algebraic_limit_theorem/) to conclude that $\lim\limits_{x \rightarrow a}\frac{f\left. (x) \right.}{g\left. (x) \right.} = \frac{f'\left. (a) \right.}{g'\left. (a) \right.}$

Finally, the [continuity](/notes/areas/mathematics/real_analysis/definitions/continuity/) of $f'$ and $g'$ at $a$ implies



$$
L = \lim\limits_{x \rightarrow a}\frac{f'\left. (x) \right.}{g'\left. (x) \right.} = \frac{f'\left. (a) \right.}{g'\left. (a) \right.}
$$



and the result follows. (Note that this argument also assumes $g'\left. (a) \right. \neq 0$.)

## Exercise 5.3.11

### (a)

Let $\epsilon > 0$ be arbitrary. Because $L = \lim\limits_{x \rightarrow a}f'\left. (x) \right./g'\left. (x) \right.$, we know that there exists a $\delta > 0$ such that



$$
\left| \frac{f'\left. (t) \right.}{g'\left. (t) \right.} - L \right| < \epsilon
$$



provided that $0 < |t - a| < \delta$.

This $\delta$ is going to suffice to prove $L = \lim\limits_{x \rightarrow a}f\left. (x) \right./g\left. (x) \right.$ as well. To see why, pick $x \in V_{\delta}\left. (a) \right.$ with $a < x$ (the case $x < a$ is similar) and apply the [Generalized_Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/generalized_mean_value_theorem/) to $f$ and $g$ on the interval $\left. \lbrack a,x\rbrack \right.$. In this case we get a point $c \in \left. (a,x) \right.$ where



$$
\frac{f'\left. (c) \right.}{g'\left. (c) \right.} = \frac{f\left. (x) \right. - g\left. (a) \right.}{g\left. (x) \right. - g\left. (a) \right.} = \frac{f\left. (x) \right.}{g\left. (x) \right.}
$$



Because $c$ must satisfy $0 < |c - a| < \delta$, it follows that



$$
\left| \frac{f\left. (x) \right.}{g\left. (x) \right.} - L \right| = \left| \frac{f'\left. (c) \right.}{g'\left. (c) \right.} - L \right| < \epsilon
$$



whenever $0 < |x - a| < \delta$. This completes the proof.

> Use the [Generalized_Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/generalized_mean_value_theorem/) to furnish a proof of the 0/0 case of [L'Hospital's_Rule](/notes/areas/mathematics/real_analysis/definitions/lhospitals_rule/) (Theorem 5.3.6).

### (b)

> If we keep the first part of the hypothesis of Theorem 5.3.6 the same but we assume that
>
> 

$$
\lim\limits_{x \rightarrow a}\frac{f'\left. (x) \right.}{g'\left. (x) \right.} = \infty
$$

,
>
> does it necessarily follow that
>
> 

$$
\lim\limits_{x \rightarrow a}\frac{f\left. (x) \right.}{g\left. (x) \right.} = \infty?
$$



Yes. The proof is exactly the same as in part (a)

# Section 5.4 Exercises

# Section 6.2 Exercises

## Exercise 6.2.1

> Let
>
> 

$$
f_{n}\left. (x) \right. = \frac{nx}{1 + nx^{2}}
$$



### (a)

> Find the pointwise limit of $\left. \left( f_{n} \right) \right.$ for all $x \in \left. (0,\infty) \right.$.

Dividing the numerator and denominator by $n$ gives



$$
\lim\limits_{n \rightarrow \infty}f_{n}\left. (x) \right. = \lim\limits_{n \rightarrow \infty}\frac{nx}{1 + nx^{2}} = \lim\limits_{n \rightarrow \infty}\frac{x}{1/n + x^{2}} = \frac{1}{x}
$$



So $f_{n}\left. (x) \right.$ converges pointwise to $f\left. (x) \right. = 1/x$.

### (b)

> Is the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) uniform on $\left. (0,\infty) \right.$?

Restating Definition 6.2.3:

> [uniform_convergence](/notes/areas/mathematics/real_analysis/definitions/uniform_convergence/): Let $\left. \left( f_{n} \right) \right.$ be a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions defined on a set $A \subseteq \mathbb{R}$. Then $\left. \left( f_{n} \right) \right.$ converges uniformly on $A$ to a limit [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ defined on $A$ if, for every $\epsilon > 0$, there exists an $N \in \mathbb{N}$ such that $\left| f_{n}\left. (x) \right. - f\left. (x) \right. \right| < \epsilon$ whenever $n \geq N$ and $x \in A.$

Applying Definition 6.2.3, we have



$$
\left| f_{n}\left. (x) \right. - f\left. (x) \right. \right| = \left| \frac{nx}{1 + nx^{2}} - \frac{1}{x} \right| = \frac{1}{x + nx^{3}}
$$



Now, in order to make $\left| f_{n}\left. (x) \right. - f\left. (x) \right. \right| < \epsilon$, we must choose



$$
N \geq \frac{1 - \epsilon x}{\epsilon x^{3}}
$$



For a fixed $\epsilon > 0$, the expression $\left. (1 - \epsilon x) \right./\left. \left( \epsilon x^{3} \right) \right.$ grows without bound as $x$ tends to zero, and thus there is no way to pick a value of $N$ that will work for every value of $x$ in $\left. (0,\infty) \right.$. So, no, the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is not uniform on $\left. (0,\infty) \right.$.

### (c)

> Is the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) uniform on $\left. (0,1) \right.$?

The [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is not uniform on $\left. (0,1) \right.$ either. As in (b), the problem occurs when $x$ approaches zero, and this is also true on the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $\left. (0,1) \right.$.

### (d)

> Is the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) uniform on $\left. (1,\infty) \right.$?

Yes. If $x > 1$, then it follows that



$$
\left| f_{n}\left. (x) \right. - f\left. (x) \right. \right| = \frac{1}{x + nx^{3}} \leq \frac{1}{1 + n} < \epsilon
$$



Let $\epsilon > 0$ be arbitrary. Choose $N$ large enough so that $1/\left. (1 + n) \right. < \epsilon$ whenever $n \geq N$. It follows that $\left| f_{n}\left. (x) \right. - f\left. (x) \right. \right| < \epsilon$ for all $n \geq N$ and so $\left. \left( f_{n} \right) \right.$ converges to $f$ uniformly on $\left. (1,\infty) \right.$.

## Exercise 6.2.3

> For each $n \in \mathbb{N}$ and $x \in \lbrack 0,\infty)$, let
>
> 

$$
g_{n}\left. (x) \right. = \frac{x}{1 + x^{n}}\quad\mathrm{\text{and}}\quad h_{n}\left. (x) \right. = \begin{cases}
1 & \mathrm{\text{if }}x \geq 1/n \\
nx & \mathrm{\text{if }}0 \leq x < 1/n
\end{cases}
$$


>
> Answer the following questions for the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s $\left. \left( g_{n} \right) \right.$ and $\left. \left( h_{n} \right) \right.$:

### (a)

> Find the pointwise limit on $\lbrack 0,\infty)$.

Retating Definition 6.2.1

> [pointwise_convergence](/notes/areas/mathematics/real_analysis/definitions/pointwise_convergence/): For each $n \in \mathbb{N}$, let $f_{n}$ be a [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on a set $A \subseteq \mathbb{R}$. The [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( f_{n} \right) \right.$ of functions is pointwise convergent on $A$ to a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f:A \rightarrow \mathbb{R}$ if, for all $x \in A$ the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of real numbers $f_{n}\left. (x) \right.$ converges to $f\left. (x) \right.$.

For $\left. \left( g_{n} \right) \right.$ the pointwise limit is



$$
g\left. (x) \right. = \lim\limits_{n \rightarrow \infty}\frac{x}{1 + x^{n}} = \begin{cases}
x & \mathrm{\text{if }}0 \leq x < 1 \\
1/2 & \mathrm{\text{if }}x = 1 \\
0 & \mathrm{\text{if }}x > 1
\end{cases}
$$



See Example 2.5.3 for the case when $0 \leq x < 1$.

Now, for $\left. \left( h_{n} \right) \right.$, the pointwise limit is



$$
h\left. (x) \right. = \begin{cases}
1 & \mathrm{\text{if }}x > 0 \\
0 & \mathrm{\text{if }}x = 0
\end{cases}
$$



### (b)

> Explain how we know that the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) *cannot* be uniform on $\lbrack 0,\infty)$.

For $\left. \left( g_{n} \right) \right.$, Theorem 6.2.6 tells us that if the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) were uniform then $g\left. (x) \right.$ would be continuous. However, $g\left. (x) \right.$ is not continuous at $x = 1$ and so the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) cannot be uniform on any [domain](/notes/areas/mathematics/set_theory/definitions/domain/) containing this point. In fact, the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is not uniform over any [domain](/notes/areas/mathematics/set_theory/definitions/domain/) that has $x = 1$ as a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/).

For $\left. \left( h_{n} \right) \right.$, each of the functions $h_{n}$ is continuous, but the limit [function](/notes/areas/mathematics/set_theory/definitions/function/) $h$ is not (since the limit is different depending on which side one approaches it from). Therefore, Theorem 6.2.6 tells us that the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) cannot be uniform.

### (c)

> Choose a smaller set over which the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is uniform and supply an argument to show that this is indeed the case.

For $\left. \left( g_{n} \right) \right.$, consider the set $\lbrack 2,\infty)$. If $x \geq 2$ then



$$
\left| g_{n}\left. (x) \right. - g\left. (x) \right. \right| = \left| \frac{x}{1 + x^{n}} \right| < \frac{x}{x^{n}} \leq \frac{1}{2^{n - 1}}
$$



Given $\epsilon > 0$, pick $N$ so that $n \geq N$ implies that $1/2^{n - 1} < \epsilon$. Then $\left| g_{n}\left. (x) \right. - g\left. (x) \right. \right| < \epsilon$ for all $n \geq N$, and we conclude that $g_{n} \rightarrow g$ uniformly on $\lbrack 2,\infty)$.

It is possible to prove [uniform_convergence](/notes/areas/mathematics/real_analysis/definitions/uniform_convergence/) on set set of the form $\lbrack a,\infty)$ where $a > 0$. On such a set, we can choose $N$ large enough so that $1/N < a$. Then for all $n \geq N$, it follows that $\left| h_{n}\left. (x) \right. - h\left. (x) \right. \right| = |1 - 1| = 0$ whenever $x \geq a$. This shows that $N$ is a suitable response for any value of $\epsilon > 0$ on the set $\lbrack a,\infty)$.

## Exercise 6.2.5

> Using the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) for convergent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s of real numbers (Theorem 2.6.4), supply a proof for Theorem 6.2.5. (First, define a candidate for f (x), and then argue that $f_{n} \rightarrow f$ uniformly.)

Restating Theorem 2.6.4:

> [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/): A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) converges if and only if it is a [Cauchy_sequence](/notes/areas/mathematics/real_analysis/definitions/cauchy_sequence/).

Restating Theorem 6.2.5

> [Cauchy_Criterion_for_Uniform_Convergence](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion_for_uniform_convergence/): A [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions $\left. \left( f_{n} \right) \right.$ defined on a set $A \subseteq \mathbb{R}$ converges uniformly on $A$ if and only if for every $\epsilon > 0$ there exists an $N \in \mathbb{N}$ such that $\left| f_{n}\left. (x) \right. - f_{m}\left. (x) \right. \right| < \epsilon$ whenever $m,n \geq N$ and $x \in A$.

## Exercise 6.2.7

> Let $f$ be uniformly continuous on all of $\mathbb{R}$, and define a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions by $f_{n}\left. (x) \right. = f\left. (x + 1/n) \right.$. Show that $f_{n} \rightarrow f$ uniformly. Give an example to show that this proposition fails if $f$ is only assumed to be continuous and not uniformly continuous on $\mathbb{R}$.

## Exercise 6.2.9

> Assume $\left. \left( f_{n} \right) \right.$ and $\left. \left( g_{n} \right) \right.$ are uniformly convergent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s of functions.

### (a)

> Show that $\left. \left( f_{n} + g_{n} \right) \right.$ is a uniformly convergent [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions.

### (b)

> Give an example to show that the product $\left. \left( f_{n}g_{n} \right) \right.$ may not converge uniformly.

### (c)

> Prove that if there exists an $M > 0$ such that $\left| f_{n} \right| \leq M$ and $\left| g_{n} \right| \leq M$ for all $n \in \mathbb{N}$, then $\left. \left( f_{n}g_{n} \right) \right.$ does converge uniformly.

## Exercise 6.2.11 ([Dini's_Theorem](/notes/areas/mathematics/real_analysis/definitions/dinis_theorem/))

> Assume $f_{n} \rightarrow f$ pointwise on a compact set $K$ and assume that for each $x \in K$ the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $f_{n}\left. (x) \right.$ is increasing. Follow these steps to show that if $f_{n}$ and $f$ are continuous on $K$, then the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is uniform.

### (a)

> Set $g_{n} = f - f_{n}$ and translate the preceding hypothesis into statements about the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( g_{n} \right) \right.$.

### (b)

> Let $\epsilon > 0$ be arbitrary, and define $K_{n} = \{ x \in K:g_{n}\left. (x) \right. \geq \epsilon\}$. Argue that $K_{1} \supseteq K_{2} \supseteq K_{3} \supseteq \cdots$, and use this observation to finish the argument.

## Exercise 6.2.13

> Recall that the [Bolzano-Weierstrass_Theorem](/notes/areas/mathematics/real_analysis/definitions/bolzano-weierstrass_theorem/) (Theorem 2.5.5) states that every bounded [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of real numbers has a convergent [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/). An analogous statement for bounded [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)s of functions is not true in general, but under stronger hypotheses several different conclusions are possible. One avenue is to assume the common [domain](/notes/areas/mathematics/set_theory/definitions/domain/) for all of the functions in the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is countable. (Another is explored in the next two exercises.)
>
> Let $A = \{ x_{1},x_{2},x_{3},\ldots\}$ be a [countable](/notes/areas/mathematics/set_theory/definitions/countable/) set. For each $n \in \mathbb{N}$, let $f_{n}$ be defined on $A$ and assume there exists an $M > 0$ such that $\left| f_{n}\left. (x) \right. \right| \leq M$ for all $n \in \mathbb{N}$ and $x \in A$. Follow these steps to show that there exists a [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) of $\left. \left( f_{n} \right) \right.$ that converges pointwise on $A$.

### (a)

> Why does the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of real numbers $f_{n}\left. \left( x_{1} \right) \right.$ necessarily contain a convergent [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) $(f_{n_{k})}$ To indicate that the [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) of functions $\left. \left( f_{n_{k}} \right) \right.$ is generated by considering the values of the functions at x1, we will use the notation $f_{n_{k}} = f_{1,k}$.

### (b)

> Now, explain why the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $f_{1,k}\left. \left( x_{2} \right) \right.$ contains a convergent [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/).

### (c)

> Carefully construct a nested family of [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/)s $\left. \left( f_{m,k} \right) \right.$ and show how this can be used to produce a single [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) of $\left. \left( f_{n} \right) \right.$ that converges at every point of $A$.

## Exercise 6.2.15 ([Arzela-Ascoli_Theorem](/notes/areas/mathematics/real_analysis/definitions/arzela-ascoli_theorem/))

> For each $n \in \mathbb{N}$, let $f_{n}$ be a [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on $\left. \lbrack 0,1\rbrack \right.$. If $\left. \left( f_{n} \right) \right.$ is bounded on $\left. \lbrack 0,1\rbrack \right.$ --- that is, there exists an $M > 0$ such that $\left| f_{n}\left. (x) \right. \right| \leq M$ for all $n \in \mathbb{N}$ and $x \in \left. \lbrack 0,1\rbrack \right.$ --- and the collection of functions $\left. \left( f_{n} \right) \right.$ is equicontinuous (Exercise 6.2.14), follow these steps to show that $\left. \left( f_{n} \right) \right.$ contains a uniformly convergent [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/).

### (a)

> Use Exercise 6.2.13 to produce a [subsequence](/notes/areas/mathematics/real_analysis/definitions/subsequence/) $\left. \left( f_{n_{k}} \right) \right.$ that converges at every rational point in $\left. \lbrack 0,1\rbrack \right.$. To simplify the notation, set $g_{k} = f_{n_{k}}$. It remains to show that $\left. \left( g_{k} \right) \right.$ converges uniformly on all of $\left. \lbrack 0,1\rbrack \right.$.

### (b)

> Let $\epsilon > 0$. By equicontinuity, there exists a $\delta > 0$ such that
>
> 

$$
\left| g_{k}\left. (x) \right. - g_{k}\left. (y) \right. \right| < \frac{\epsilon}{e}
$$


>
> for all $|x - y| < \delta$ and $k \in \mathbb{N}$. Using this $\delta$, let $r_{1},r_{2},\ldots,r_{m}$ be a *finite* collection of rational points with the property that the union of the neighborhoods $V_{\delta}\left. \left( r_{i} \right) \right.$ contains $\left. \lbrack 0,1\rbrack \right.$.
>
> Explain why there must exist an $N \in \mathbb{N}$ such that
>
> 

$$
\left| g_{s}\left. \left( r_{i} \right) \right. - g_{t}\left. \left( r_{i} \right) \right. \right| < \frac{\epsilon}{e}
$$


>
> for all $s,t \geq N$ and $r_{i}$ in the finite subset of $\left. \lbrack 0,1\rbrack \right.$ just described. Why does having the set $\{ r_{1},r_{2},\ldots,r_{m}\}$ be finite matter?

### (c)

> Finish the argument by showing that, for an arbitrary $x \in \left. \lbrack 0,1\rbrack \right.$,
>
> 

$$
\left| g_{s}\left. (x) \right. - g_{t}\left. (x) \right. \right| < \epsilon
$$


>
> for all $s,t \geq N$.

# Section 6.3 Exercises

## Exercise 6.3.1

> Consider the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions defined by
>
> 

$$
g_{n}\left. (x) \right. = \frac{x^{n}}{n}
$$



### (a)

> Show $\left. \left( g_{n} \right) \right.$ converges uniformly on $\left. \lbrack 0,1\rbrack \right.$ and find $g = \lim g_{n}$. Show that $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) and compute $g'\left. (x) \right.$ for all $x \in \left. \lbrack 0,1\rbrack \right.$.

Restating Definition 6.2.3:

> [uniform_convergence](/notes/areas/mathematics/real_analysis/definitions/uniform_convergence/): Let $\left. \left( f_{n} \right) \right.$ be a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions defined on a set $A \subseteq \mathbb{R}$. Then $\left. \left( f_{n} \right) \right.$ converges uniformly on $A$ to a limit [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ defined on $A$ if, for every $\epsilon > 0$, there exists an $N \in \mathbb{N}$ such that $\left| f_{n}\left. (x) \right. - f\left. (x) \right. \right| < \epsilon$ whenever $n \geq N$ and $x \in A.$

We can make a guess here that $g = \lim g_{n} = 0$. We just need to prove now that this is so. Note that



$$
\left| \frac{x^{n}}{n} - 0 \right| \leq \frac{1}{n} < \epsilon\quad\forall x \in \left. \lbrack 0,1\rbrack \right.
$$



Let $\epsilon > 0$ be arbitrary. Choose $N > 1/\epsilon$. Then $n \geq N$ implies that $\left| g_{n} \right| < \epsilon\quad\forall x \in \left. \lbrack 0,1\rbrack \right.$, as desired.

Because $g\left. (x) \right. = 0\quad\forall x \in \left. \lbrack 0,1\rbrack \right.$, $g\left. (x) \right.$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) and $g'\left. (0) \right. = 0$.

### (b)

> Now, show that $\left. \left( g'_{n} \right) \right.$ converges on $\left. \lbrack 0,1\rbrack \right.$. Is the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) uniform? Set $h = \lim g_{n}'$ and compare $g$ and $g'$. Are they the same?

Computing $g_{n}'\left. (x) \right.$, we have



$$
g_{n}'\left. (x) \right. = \frac{nx^{n - 1}}{n} = x^{n - 1}
$$



where the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions $\left. \left( g_{n}' \right) \right.$ converges pointwise on $\left. \lbrack 0,1\rbrack \right.$ to



$$
\begin{array}{r}
h\left. (x) \right. = \lim\limits_{n \rightarrow \infty}g'\left. (x) \right. = \{ 0,\mathrm{\text{ if }}x \neq 1 \\
1,\mathrm{\text{ if }}x = 1
\end{array}
$$



The [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is not uniform over $\left. \lbrack 0,1\rbrack \right.$, and in fact it is not uniform over any set that contains 1 as a [limit point](/notes/areas/mathematics/topology/definitions/limit_point/). Comparing $h = \lim g_{n}'$ to $g'$ is illuminating. Note in particular that $h\left. (1) \right. \neq g\left. (1) \right.$, so that it is possible for the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of derivatives to converge to the "wrong" value when the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) of $g_{n}'$ is not uniform. On the other hand, the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) of $g_{n}'$ is uniform on sets of the form $\left. \lbrack 0,c\rbrack \right.$ where $c < 1$, and this is reflected by the fact that $h\left. (x) \right. = g\left. (x) \right.$ on $\lbrack 0,1)$.

## Exercise 6.3.2

> Consider the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/)
>
> 

$$
h_{n}\left. (x) \right. = \sqrt{x^{2} + \frac{1}{n}}
$$



### (a)

> Compute the pointwise limit of $\left. \left( h_{n} \right) \right.$ and then prove that the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is uniform on $\mathbb{R}$.

Computing the pointwise limit gives



$$
\lim\limits_{n \rightarrow \infty}h_{n}\left. (x) \right. = \sqrt{x^{2}}
$$



Using the fact that $\sqrt{a + b} \leq \sqrt{a} + \sqrt{b}$ for $a,b \geq 0$, we have that $\sqrt{x^{2} + 1/n} \leq \sqrt{x^{2}} + \sqrt{1/n}$ and that $\sqrt{x^{2} + 1/n} - \sqrt{x^{2}} \leq \sqrt{1/n}$.

Let $\epsilon > 0$ be arbitrary. There exists an $n \geq N$ such that $\left| \sqrt{x^{2} + 1/n} - \sqrt{x^{2}} \right| = \sqrt{x^{2} + 1/n} - \sqrt{x^{2}} \leq \sqrt{1/n} < \epsilon$.

Choose $N > 1/\epsilon^{2}$. This implies that $\left| h_{n} \right| < \epsilon$ for all $x \in \mathbb{R}$.

### (b)

> Note that each $\left. \left( h_{n} \right) \right.$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/). Show $g\left. (x) \right. = \lim h_{n}'\left. (x) \right.$ exists for all $x$, and explain how we can be certain that the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is not uniform on any neighborhood of zero.

### Exercise 6.3.3

> Consider the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions
>
> 

$$
f_{n}\left. (x) \right. = \frac{x}{1 + nx^{2}}
$$



### (a)

> Find the points on $\mathbb{R}$ where each $f_{n}\left. (x) \right.$ attains its maximum and minimum value. Use this to prove $\left. \left( f_{n} \right) \right.$ converges uniformly on $\mathbb{R}$. What is the limit function?

Taking the derivative of the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of functions gives



$$
f_{n}'\left. (x) \right. = \left. \left( \frac{x}{1 + nx^{2}} \right) \right.' = \frac{1 - nx^{2}}{\left. (1 + nx) \right.^{2}}
$$



Setting the above equal to zero gives the critical values $\pm 1/\sqrt{n}$. Using the second derivative test leads to the conclusion that the maximum of $f$ occurs at $1/\sqrt{n}$ and the minimum at $- 1/\sqrt{n}$. Because $f_{n}\left. \left( - 1/\sqrt{n} \right) \right. = \left| f_{n}\left. \left( - 1/\sqrt{n} \right) \right. \right| = 1/\left. \left( 2\sqrt{n} \right) \right.$, we see that



$$
\left| f_{n}\left. (x) \right. \right| \leq \frac{1}{2\sqrt{n}}\quad\forall x \in \mathbb{R}
$$



To show that $\left. \left( f_{n} \right) \right. \rightarrow 0$ uniformly on $\mathbb{R}$, we let $\epsilon > 0$ and choose $N$ large enough so that $n \geq N$ implies $1/\left. \left( 2\sqrt{n} \right) \right. < \epsilon$. It follows that $\left| f_{n}\left. (x) \right. - 0 \right| < \epsilon$ whenever $n \geq N$, as desired.

### (b)

> Let $f = \lim f_{n}$. Compute $f_{n}'\left. (x) \right.$ and find all the values of $x$ for which $f'\left. (x) \right. = \lim f_{n}'\left. (x) \right.$

Because $f_{n} \rightarrow 0$ uniformly, the limit $f = \lim f_{n}$ satisfies $f'\left. (x) \right. = 0$ for all values of $x$.

Taking the derivative of each $f_{n}$ we get



$$
f_{n}'\left. (x) \right. = \frac{1 - nx^{2}}{1 + 2nx^{2} + n^{2}x^{4}}
$$



If $x \neq 0$ then we can show $\lim f_{n}'\left. (x) \right. = 0 = f'\left. (x) \right.$. However, for $x = 0$ we get $f_{n}'\left. (0) \right. = 1$ for all $n$ and thus $f'\left. (0) \right. \neq \lim f_{n}'\left. (0) \right.$.

## Exercise 6.3.4

> Let
>
> 

$$
h_{n}\left. (x) \right. = \frac{\sin\left. (nx) \right.}{\sqrt{n}}
$$


>
> Show that $h_{n} \rightarrow 0$ uniformly on $\mathbb{R}$ but that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of derivatives $\left. \left( h_{n}' \right) \right.$ diverges for every $x \in \mathbb{R}$.

We have that



$$
\lim\limits_{x \rightarrow \infty}\frac{\sin\left. (nx) \right.}{\sqrt{n}} = 0
$$



Since the numerator will always oscillate between $- 1$ and $1$, we have that



$$
\left| \frac{\sin\left. (nx) \right.}{\sqrt{n}} - 0 \right| \leq \frac{1}{\sqrt{n}} < \epsilon
$$



Let $\epsilon > 0$ be arbitrary. Choose $N > 1/\epsilon^{2}$. Then $n \geq N$ implies that $\left| h_{n} \right| < \epsilon$ as desired. Thus $h_{n} \rightarrow 0$ uniformly on $\mathbb{R}$.

However,



$$
h_{n}'\left. (x) \right. = \sqrt{n}\cos\left. (nx) \right.
$$



which clearly diverges for all $x \in \mathbb{R}$ as $n \rightarrow \infty$.

## Exercise 6.3.5

> Let
>
> 

$$
g_{n}\left. (x) \right. = \frac{nx + x^{2}}{2n}
$$


>
> and set $g\left. (x) \right. = \lim g_{n}\left. (x) \right.$. Show that $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) in two ways:

### (a)

> Compute $g\left. (x) \right.$ by algebraically taking the limit as $n \rightarrow \infty$ and then find $g'\left. (x) \right.$.

Taking the limit, we have



$$
\lim\limits_{n \rightarrow \infty}g_{n}\left. (x) \right. = \lim\limits_{n \rightarrow \infty}\frac{nx + x^{2}}{2n} = \lim\limits_{n \rightarrow \infty}\frac{nx}{2n} + \lim\limits_{n \rightarrow \infty}\frac{x^{2}}{2n} = \frac{x}{2}
$$



Then $g'\left. (x) \right. = 1/2$.

### (b)

> Compute $g_{n}'\left. (x) \right.$ for each $n \in \mathbb{N}$ and show that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of derivatives $\left. \left( g_{n}' \right) \right.$ converges uniformly on every interval $\left. \lbrack - M,M\rbrack \right.$. Use Theorem 6.3.3 to conclude that $g'\left. (x) \right. = \lim g_{n}'\left. (x) \right.$.

Restating Theorem 6.3.3

> Let $\left. \left( f_{n} \right) \right.$ be a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) functions defined on the closed interval $\left. \lbrack a,b\rbrack \right.$, and assume $\left. \left( f_{n}' \right) \right.$ converges uniformly to a [function](/notes/areas/mathematics/set_theory/definitions/function/) $g$ on $\left. \lbrack a,b\rbrack \right.$. If there exists a point $x_{0} \in \left. \lbrack a,b\rbrack \right.$ for which $f_{n}\left. \left( x_{0} \right) \right.$ is convergent, then $\left. \left( f_{n} \right) \right.$ converges uniformly. Moreover, the limit [function](/notes/areas/mathematics/set_theory/definitions/function/) $f = \lim f_{n}$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) and satisfies $f' = g$.

Now, as opposed to part (a), we compute $g_{n}'\left. (x) \right.$ first:



$$
g_{n}'\left. (x) \right. = \frac{1}{2} + \frac{x}{n}
$$



and note that the pointwise limit of this [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) is $\lim\limits_{n \rightarrow \infty}g_{n}'\left. (x) \right. = 1/2$. For $x \in \left. \lbrack - M,M\rbrack \right.$ we can write



$$
\left| g_{n}'\left. (x) \right. - 1/2 \right| = \left| \frac{x}{n} \right| \leq \frac{M}{n}
$$



Let $\epsilon > 0$ be arbitrary. Choose $N > M/\epsilon$, independent of $x$. Then $n \geq N$ implies that $\left| g_{n}'\left. (x) \right. - 1/2 \right| < \epsilon$, and we conclude that $g_{n}' \rightarrow 1/2$ uniformly on $\left. \lbrack - M,M\rbrack \right.$. It follows from Theorem 6.3.3 that $g'\left. (x) \right. = 1/2$.

### (c)

> Repeat parts (a) and (b) for the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $f_{n}\left. (x) \right. = \left. \left( nx^{2} + 1 \right) \right./\left. (2n + x) \right.$.

Repeating part (a) gives



$$
\lim\limits_{n \rightarrow \infty}f_{n}\left. (x) \right. = \lim\limits_{n \rightarrow \infty}\frac{nx^{2} + 1}{2n + x} = \lim\limits_{n \rightarrow \infty}\frac{nx^{2}}{2n + x} + \lim\limits_{n \rightarrow \infty}\frac{1}{2n + x} = \frac{x^{2}}{2 + x/n} + 0 = \frac{x^{2}}{2}
$$



Then $f'\left. (x) \right. = x$.

Repeating part (b) gives



$$
g_{n}'\left. (x) \right. = \frac{4n^{2}x + nx^{2} - 1}{\left. (2n + x) \right.^{2}}
$$



for which the pointwise limit is $\lim\limits_{n \rightarrow \infty}g_{n}'\left. (x) \right. = x$.

Now we have



$$
\left| f_{n}'\left. (x) \right. - x \right| = \left| - \frac{3nx^{2} + x^{3} + 1}{\left. (2n + x) \right.^{2}} \right| \leq \frac{nM^{2} + M^{3} + 1}{4n^{2} - 4nM}
$$



as long as $n > M$. Because this estimate does not depend on $x$ and tends to zero as $n \rightarrow \infty$, it follows that $f_{n}'\left. (x) \right. \rightarrow x$ uniformly on $\left. \lbrack - M,M\rbrack \right.$.

## Exercise 6.3.7

> Use the [Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/) to supply a proof for Theorem 6.3.2. To get started, observe that the [triangle_inequality](/notes/areas/mathematics/real_analysis/definitions/triangle_inequality/) implies that, for any $x \in \left. \lbrack a,b\rbrack \right.$ and $m,n \in \mathbb{N}$,
>
> 

$$
\left| f_{n}\left. (x) \right. - f_{m}\left. (x) \right. \right| \leq \left| \left. \left( f_{n}\left. (x) \right. - f_{m}\left. (x) \right. \right) \right. - \left. \left( f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right) \right. \right| + \left| f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right|
$$



Restating Theorem 5.3.2:

> [Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/): If $f:\left. \lbrack a,b\rbrack \right. \rightarrow \mathbb{R}$ is continuous on $\left. \lbrack a,b\rbrack \right.$ and [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\left. (a,b) \right.$, then there exista a point $c \in \left. (a,b) \right.$ where
>
> 

$$
f'\left. (c) \right. = \frac{f\left. (b) \right. - f\left. (a) \right.}{b - a}
$$



Restating Theorem 6.3.2:

> Let $\left. \left( f_{n} \right) \right.$ be a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) functions defined on the closed interval $\left. \lbrack a,b\rbrack \right.$, and assume $\left. \left( f_{n}' \right) \right.$ converges uniformly on $\left. \lbrack a,b\rbrack \right.$. If there exists a point $x_{0} \in \left. \lbrack a,b\rbrack \right.$ where $f_{n}\left. \left( x_{0} \right) \right.$ is convergent, then $\left. \left( f_{n} \right) \right.$ converges uniformly on $\left. \lbrack a,b\rbrack \right.$.

Let $x \in \left. \lbrack a,b\rbrack \right.$ and assume, without loss of generality, that $x > x_{0}$. Applying the [Mean_Value_Theorem](/notes/areas/mathematics/real_analysis/definitions/mean_value_theorem/) to the [function](/notes/areas/mathematics/set_theory/definitions/function/) $f_{n} - f_{m}$ on the interval $\left. \left\lbrack x_{0},x \right\rbrack \right.$ we get that there exists a point $\alpha$ such that



$$
\left. \left( f_{n}\left. (x) \right. - f_{m}\left. (x) \right. \right) \right. - \left. \left( f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right) \right. = \left. \left( f_{n}'\left. (\alpha) \right. - f_{m}'\left. (\alpha) \right. \right) \right.\left. (b - a) \right.
$$



Let $\epsilon > 0$ be arbitrary. Because $\left. \left( f_{n}' \right) \right.$ converges uniformly, the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) asserts that there exists an $N_{1}$ such that



$$
\left| f_{n}'\left. (c) \right. - f_{m}'\left. (c) \right. \right| < \frac{\epsilon}{2\left. (b - a) \right.}\quad\forall n,m \geq N\quad\mathrm{\text{and }}c \in \left. \lbrack a,b\rbrack \right.
$$



Our hypothesis states that $\left. \left( f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right) \right.$ converges so there exists an $N_{2}$ such that



$$
\left| f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right| < \frac{\epsilon}{2}\quad\forall n,m \geq N_{2}
$$



Finally, let $N = \max\{ N_{1},N_{2}\}$. Then if $n,m \geq N$ it follows that



$$
\begin{aligned}
\left| f_{n}\left. (x) \right. - f_{m}\left. (x) \right. \right| & \leq \left| \left. \left( f_{n}\left. (x) \right. - f_{m}\left. (x) \right. \right) \right. - \left. \left( f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right) \right. \right| + \left| f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right| \\
 & = \left| \left. \left( f_{n}'\left. (\alpha) \right. - f_{m}'\left. (\alpha) \right. \right) \right.\left. (b - a) \right. \right| + \left| f_{n}\left. \left( x_{0} \right) \right. - f_{m}\left. \left( x_{0} \right) \right. \right| \\
 & < \frac{\epsilon}{2\left. (b - a) \right.}\left. (b - a) \right. + \frac{\epsilon}{2} = \epsilon
\end{aligned}
$$



Because our choice of $N$ is independent of the point $x$, the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) implies that the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( f_{n} \right) \right.$ converges uniformly on $\left. \lbrack a,b\rbrack \right.$.

# Section 6.4 Exercises

## Exercise 6.4.1

> Supply the details for the proof of the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) (Corollary 6.4.5)

Restating Corollary 6.4.5:

> [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/): For each $n \in \mathbb{N}$, let $f_{n}$ be a [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on a set $A \subseteq \mathbb{R}$, and let $M_{n} > 0$ be a real number satisfying
>
> 

$$
\left| f_{n}\left. (x) \right. \right| \leq M_{n}
$$


>
> for all $x \in A$. If $\sum_{n = 1}^{\infty}M_{n}$ converges, then $\sum_{n = 1}^{\infty}f_{n}$ converges uniformly on $A$.

Restating Theorem 2.7.2:

> The series $\sum_{k = 1}^{\infty}a_{k}$ converges if and only if, given $\epsilon > 0$, there exists an $N \in \mathbb{N}$ such that whenever $n > m \geq N$ it follows that
>
> 

$$
\left| a_{m + 1} + a_{m + 2} + \cdots + a_{n} \right| < \epsilon
$$



Restating Theorem 6.4.4:

> [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) for Uniform Convergence of Series: A series $\sum_{n = 1}^{\infty}f_{n}$ converges uniformly on $A \subseteq \mathbb{R}$ if and only if for every $\epsilon > 0$ there exists an $N \in \mathbb{N}$ such that:
>
> 

$$
\left| f_{m + 1}\left. (x) \right. + f_{m + 2}\left. (x) \right. + f_{m + 3}\left. (x) \right. + \cdots + f_{n}\left. (x) \right. \right| < \epsilon
$$


>
> whenever $n > m \geq N$ and $x \in A$.

Use the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) for [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) of a series of real numbers (Theorem 2.7.2). Let $\epsilon > 0$ be arbitrary. We assume that $\sum_{n = 1}^{\infty}M_{n}$ converges, and so there exists an $N$ such that $n > m \geq N$ implies



$$
\left| M_{m + 1} + M_{m + 2} + \cdots + M_{n} \right| < \epsilon
$$



Because



$$
\left| f_{m + 1}\left. (x) \right. + f_{m + 2}\left. (x) \right. + \cdots + f_{n}\left. (x) \right. \right| \leq M_{m + 1} + M_{n + 2} + \cdots M_{n}
$$



we can appeal to the [Cauchy_Criterion](/notes/areas/mathematics/real_analysis/definitions/cauchy_criterion/) for [uniform_convergence](/notes/areas/mathematics/real_analysis/definitions/uniform_convergence/) of series (Theorem 6.4.4) to conclude that $\sum_{n = 1}^{\infty}f_{n}$ converges uniformly.

## Exercise 6.4.3

### (a)

> Show that
>
> 

$$
g\left. (x) \right. = \sum_{n = 0}^{\infty}\frac{\cos\left. \left( 2^{n}x \right) \right.}{2^{n}}
$$


>
> is continuous on all of $\mathbb{R}$.

Restating Theorem 6.4.2:

> [Term-by-term_Continuity_Theorem](/notes/areas/mathematics/real_analysis/definitions/term-by-term_continuity_theorem/): Let $f_{n}$ be continuous functions defined on a set $A \subseteq \mathbb{R}$, and assume $\sum_{n = 1}^{\infty}f_{n}$ converges uniformly on $A$ to a [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$. Then, $f$ is continuous on $A$.

Since we know the numerator in the expression given to us will always oscillate between -1 and 1, we have that



$$
\left| \frac{\cos\left. \left( 2^{n}x \right) \right.}{2^{n}} \right| \leq \frac{1}{2^{n}}
$$



and we know that $\sum_{n = 1}^{\infty}1/2^{n}$ converges (Example 2.4.4), it follows by the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) that $\sum_{n = 1}^{\infty}\cos\left. \left( 2^{n}x \right) \right./2^{n}$ converges uniformly. Because each of the summands is continuous, the limit as continuous as well by Theorem 6.4.2.

### (b)

> The [function](/notes/areas/mathematics/set_theory/definitions/function/) $g$ was cited in Section 5.4 as an example of a continuous nowhere [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) function. What happens if we try to use Theorem 6.4.3 to explore whether $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/)?

Restating Theorem 6.4.3:

> [Term-by-term_Differentiability_Theorem](/notes/areas/mathematics/real_analysis/definitions/term-by-term_differentiability_theorem/): let $f_{n}$ be [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) functions defined on an interval $A$, and assume $\sum_{n = 1}^{\infty}f_{n}'\left. (x) \right.$ converges uniformly to a limit $g\left. (x) \right.$ on $A$. If there exists a point $x_{0} \in \left. \lbrack a,b\rbrack \right.$ where $\sum_{n = 1}^{\infty}f_{n}\left. \left( x_{0} \right) \right.$ converges, then the series $\sum_{n = 1}^{\infty}f_{n}\left. (x) \right.$ converges uniformly to a [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) [function](/notes/areas/mathematics/set_theory/definitions/function/) $f\left. (x) \right.$ satisfying $f'\left. (x) \right. = g\left. (x) \right.$ on $A$. In other words
>
> 

$$
f\left. (x) \right. = \sum_{n = 1}^{\infty}f_{n}\left. (x) \right.\quad\mathrm{\text{and}}\quad f'\left. (x) \right. = \sum_{n = 1}^{\infty}f_{n}'\left. (x) \right.
$$



Again we have an infinite sum of continuous functions, and we would like to conclude that the limit is continuous. This will follow if we can argue the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is uniform. On $\left. \lbrack - 1,1\rbrack \right.$ we can make the estimate $\left. \left\lbrack x^{n}/n^{2} \right\rbrack \right. \leq 1/n^{2}$. Because $\sum_{n = 1}^{\infty}1/n^{2}$ converges, we may invoke the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) to assert that $\sum_{n = 1}^{\infty}x^{n}/n^{2}$ converges uniformly on $\left. \lbrack - 1,1\rbrack \right.$. This completes the proof.

## Exercise 6.4.5

### (a)

> Prove that
>
> 

$$
h\left. (x) \right. = \sum_{n = 1}^{\infty}\frac{x^{n}}{n^{2}} = x + \frac{x^{2}}{4} + \frac{x^{3}}{9} + \frac{x^{4}}{16} + \cdots
$$


>
> is continuous on $\left. \lbrack - 1,1\rbrack \right.$.

For $x \in \left. \lbrack - 1,1\rbrack \right.$, we have $\left| x^{2}/n^{2} \right| \leq 1/n^{2}$. Again, we know that $1/n^{2}$ converges, so by the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/), we know that the series converges uniformly. Now we can invoke Theorem 6.4.2 ([Term-by-term_Continuity_Theorem](/notes/areas/mathematics/real_analysis/definitions/term-by-term_continuity_theorem/)), which implies that $h$ is continuous as well.

### (b)

> The series
>
> 

$$
h\left. (x) \right. = \sum_{n = 1}^{\infty}\frac{x^{n}}{n} = x + \frac{x^{2}}{2} + \frac{x^{3}}{3} + \frac{x^{4}}{4} + \cdots
$$


>
> converges for every $x$ in the half-open interval $\lbrack - 1,1)$ but does not converge when $x = 1$. For a fixed $x_{0} \in \left. ( - 1,1) \right.$, explain how we can still use the Weierstrass M-Test to prove that $f$ is continuous at $x_{0}$.

For a fixed $x_{0} \in \left. ( - 1,1) \right.$, choose $c$ to satisfy $\left| x_{0} \right| < c < 1$ and apply the M-test on $\left. \lbrack - c,c\rbrack \right.$. Over this interval we get the estimate $\left| x^{n}/n \right| \leq c^{n}/n$. Because $\sum_{n = 1}^{\infty}c^{n}/n$ converges, the M-test implies that the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is uniform and by Theorem 6.4.2, $f$ is continuous at $x_{0} \in \left. \lbrack - c,c\rbrack \right.$.

## Exercise 6.4.7

> Let
>
> 

$$
f\left. (x) \right. = \sum_{k = 1}^{\infty}\frac{\sin\left. (kx) \right.}{k^{3}}
$$



### (a)

> Show that $f\left. (x) \right.$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) and that the derivative $f'\left. (x) \right.$ is continuous.

By Theorem 6.4.3, we need to take the derivative of the series, which is



$$
\sum_{n = 1}^{\infty}\frac{\cos\left. (kx) \right.}{k^{2}}
$$



Per many previous exercises, we know that



$$
\left| \frac{\cos\left. (kx) \right.}{k^{2}} \right| \leq \frac{1}{k^{2}}
$$



and that $\sum_{n = 1}^{\infty}1/k^{2}$ converges. Thus, the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) asserts that the series $\left| \frac{\cos\left. (kx) \right.}{k^{2}} \right| \leq \frac{1}{k^{2}}$ is uniformly convergent. Now, Theorem 6.4.3 asserts that $f$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) and that



$$
f'\left. (x) \right. = \sum_{n = 1}^{\infty}\frac{\cos\left. (kx) \right.}{k^{2}}
$$



Finally, the [uniform_convergence](/notes/areas/mathematics/real_analysis/definitions/uniform_convergence/) also implies, by Theorem 6.4.2, that $f'\left. (x) \right.$ is continuous because each of the summands is.

### (b)

> Can we determine if $f$ is twice-differentiable?

By Theorem 6.4.3, we need to take the second derivative of the series, which is



$$
\sum_{n = 1}^{\infty}\frac{- \sin\left. (kx) \right.}{k}
$$



We clearly cannot use the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) here since $\sum_{n = 1}^{\infty}1/k$ is divergent.

## Exercise 6.4.9

> Let
>
> 

$$
h\left. (x) \right. = \sum_{n = 1}^{\infty}\frac{1}{x^{2} + n^{2}}
$$



### (a)

> Show that $h$ is a continuous [function](/notes/areas/mathematics/set_theory/definitions/function/) defined on all of $\mathbb{R}$.

We know that all of the summation terms are continuous functions and satisfy



$$
\left| \frac{1}{x^{2} + n^{2}} \right| \leq \frac{1}{n^{2}}\quad\forall x \in \mathbb{R}
$$



As always, we know that $\sum_{n = 1}^{\infty}1/n^{2}$ converges, the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) implies the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is uniform and thus that $h\left. (x) \right.$ is continuous on $\mathbb{R}$

### (b)

> Is $h$ [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/)? If so, is the derivative [function](/notes/areas/mathematics/set_theory/definitions/function/) $h'$ continuous?

To use Theorem 6.4.3, we need to examine the differentiated series on some arbitrary interval, say, $\left. \lbrack - M,M\rbrack \right.$



$$
\left| \frac{- 2x}{x^{2} + n^{2}} \right| \leq \frac{2M}{n^{2}}
$$



Again, $\sum_{n = 1}^{\infty}2M/n^{2}$ converges. This proves that the differentiated series converges uniformly to $h'\left. (x) \right.$ and that $h'$ is continuous on $\lbrack - M,M$. Because $\left. \lbrack - M,M\rbrack \right.$ is arbitrary in our argument, we can conclude that $h'$ exists and is continuous on $\mathbb{R}$.

# Section 6.5 Exercises

## Exercise 6.5.1

> Consider the [function](/notes/areas/mathematics/set_theory/definitions/function/) $g$ defined by the power series
>
> 

$$
g\left. (x) \right. = x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4} + \frac{x^{5}}{5} + \cdots
$$



### (a)

> Is $g$ defined on $\left. ( - 1,1) \right.?$ Is it continuous on this set? Is $g$ defined on $( - 1,1\rbrack$? Is it continuous on this set? What happens on $\left. \lbrack - 1,1\rbrack \right.$? Can the power series for $g\left. (x) \right.$ possibly converges for any other points $|x| > 1$? Explain

$g\left. (x) \right.$ is given by



$$
\sum_{n = 1}^{\infty}\left. ( - 1) \right.^{n + 1}\frac{x^{n}}{n}
$$



The series $g$ converges for all $x \in ( - 1,1\rbrack$ and is continuous over this interval. The series goes off to infinity when $x = - 1$ and thus does not converge. Theorem 6.5.1 implies that the series does not converge for any values of $|x| > 1$.

### (b)

> For what values of $x$ is $g'\left. (x) \right.$ defined? Find a formula for $g'$.

By Theorem 6.5.6, $g$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) on $\left. ( - 1,1) \right.$ with



$$
\sum_{n = 1}^{\infty}\left. ( - 1) \right.^{n + 1}x^{n - 1} = 1 - x + x^{2} - x^{3} + \cdots
$$



$g'\left. (x) \right.$ no longer converges when $x = 1$, although the [function](/notes/areas/mathematics/set_theory/definitions/function/) is technically [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) at this point.

## Exercise 6.5.3

> Use the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) to prove Theorem 6.5.2.

Set $M_{n} = \left| a_{n}x_{0}^{n} \right|$ and note that absolute [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) at $x_{0}$ implies that



$$
\sum_{n = 0}^{\infty}\left| a_{n}x_{0}^{n} \right| = \sum_{n = 0}^{\infty}M_{n}
$$



converges. If $x \in \left. \lbrack - c,c\rbrack \right.$, then we get the estimate



$$
\left| a_{n}x^{n} \right| \leq \left| a_{n}x_{0}^{n} \right| = M_{n}
$$



and the [Weierstrass_M-test](/notes/areas/mathematics/real_analysis/definitions/weierstrass_m-test/) implies that $\sum_{n = 0}^{\infty}a_{n}x^{n}$ converges uniformly on $\left. \lbrack - c,c\rbrack \right.$.

## Exercise 6.5.5

### (a)

> If $s$ satisfies $0 < s < 1$, show $ns^{n - 1}$ is bounded for all $n \geq 1$.

Let's set $y_{n} = ns^{n - 1}$. We want to argue that $\left. \left( y_{n} \right) \right.$ is *eventually* decreasing, and in fact converges to 0. A good way to see this is to look at the ratio $y_{n + 1}/y_{n} = s\left. (n + 1) \right./n$, and note that it is eventually less than 1. In particular, if $n > s/\left. (1 - s) \right.$ then $y_{n + 1}/y_{n} < 1$ at which point the [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) starts decreasing. Since all we really need to know that $\left. \left( y_{n} \right) \right.$ is bounded, we can stop here.

### (b)

> Given an arbitrary $x \in \left. ( - R,R) \right.$, pick $t$ to satisfy $|x| < t < R$. Use this to start to construct a proof for Theorem 6.5.6.

Let $x \in \left. ( - R,R) \right.$ be arbitrary and pick $t$ to satisfy $|x| < t < R$. We will show that $\sum\left| na_{n}x^{n - 1} \right|$ converges, implying that $\sum na_{n}x^{n - 1}$ converges by the [Comparison_Test](/notes/areas/mathematics/real_analysis/definitions/comparison_test/). First write



$$
\sum_{n = 1}^{\infty}\left| na_{n}x^{n - 1} \right| = \sum_{n = 1}^{\infty}\frac{1}{t}\left. \left( n\left| \frac{x}{t} \right|^{n - 1} \right) \right.\left| a_{n}t^{n} \right|
$$



Because $|x/t| < 1$, be part (a) we can pick a bound $L$ satisfying



$$
n\left| \frac{x}{t} \right|^{n - 1} \leq L\quad\forall n \in \mathbb{N}
$$



Now we have



$$
\sum_{n - 1}^{\infty}\left| na_{n}x^{n - 1} \right| = \sum_{n = 1}^{\infty}\frac{1}{t}\left. \left( n\left| \frac{x}{t} \right|^{n - 1} \right) \right.\left| a_{n}t^{n} \right| \leq \frac{L}{t}\sum_{n = 1}^{\infty}\left| a_{n}t^{n} \right|
$$



where the last sum converges because $t \in \left. ( - R,R) \right.$. Therefore, $\sum_{n = 1}^{\infty}na_{n}x^{n - 1}$ converges absolutely and thus converges.

## Exercise 6.5.7

Let $\sum a_{n}x^{n}$ be a power series with $a_{n} \neq 0$, and assume



$$
L = \lim\limits_{n \rightarrow \infty}\left| \frac{a_{n + 1}}{a_{n}} \right|
$$



### (a)

> Show that if $L \neq 0$, then the series converges for all $x \in \left. ( - 1/L,1/L) \right.$. (The advice in Exercise 2.7.9 may be helpful.)

For a fixed $x$, apply the [Ratio_Test](/notes/areas/mathematics/real_analysis/definitions/ratio_test/) to the series $\sum a_{n}x^{n}$ to get



$$
\lim\limits_{n \rightarrow \infty}\left| \frac{a_{n + 1}x^{n + 1}}{a_{n}x_{n}} \right| = \sum_{n \rightarrow \infty}\left| \frac{a_{n + 1}}{a_{n}} \right||x| = L|x|
$$



If $|x| < 1/L$ then $L|x| = 0 < 1$ and the series converges.

### (b)

> Show that if $L = 0$, then the series converges for all $x \in \mathbb{R}$.

If $L = 0$, then $L|x| = 0 < 1$ for every value of $x$, and the [Ratio_Test](/notes/areas/mathematics/real_analysis/definitions/ratio_test/) implies that the series converges on all of $\mathbb{R}$.

### (c)

> Show that $\left. (a) \right.$ and $\left. (b) \right.$ continue to hold if $L$ is replaced by the limit
>
> 

$$
L' = \lim\limits_{n \rightarrow \infty}s_{n}\quad\mathrm{\text{where}}\quad s_{n} = \sup\left. \left\{ \left| \frac{a_{k + 1}}{a_{k}} \right|:k \geq n \right\} \right.
$$


>
> (General properties of the *limit superior* are discussed in Exercise 2.4.7.)

This will follow using the same proofs if we can prove the following modified version of the [Ratio_Test](/notes/areas/mathematics/real_analysis/definitions/ratio_test/):

Given a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( b_{n} \right) \right.$, let



$$
L' = \lim\limits_{n \rightarrow \infty}s_{n}\quad\mathrm{\text{where}}\quad s_{n} = \sup\left. \left\{ \left| \frac{b_{k + 1}}{b_{k}} \right|:k \geq n \right\} \right.
$$



If $L' < 1$, then $\sum b_{n}$ converges.

The proof is very similar to the proof of the [Ratio_Test](/notes/areas/mathematics/real_analysis/definitions/ratio_test/) in Exercise 2.7.9. First choose $R$ to satisfy $L' < R < 1$. The [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) $\left. \left( s_{n} \right) \right.$ is decreasing, and because it converges to $L'$ we know there exists an $N$ such that



$$
\left| \frac{b_{k + 1}}{b_{k}} \right| \leq R\quad\forall k \geq N
$$



An induction proof like the one before shows



$$
\left| b_{k} \right| \leq \left| b_{N} \right|R^{k - N}\quad\forall k \geq N
$$



and then we may compare the series $\sum b_{k}$ to the convergent geometric series $\left| a_{N} \right|\sum R^{k}$ to conclude that $\sum b_{k}$ converges.

## Exercise 6.5.9

> Review the definitions and results from Section 2.8 concerning products of series and Cauchy products in particular. At the end of Section 2.9, we mentioned the following result: If both $\sum a_{n}$ and $\sum b_{n}$ converge conditionally to $A$ and $B$ respectively, then it is possible for the Cauchy product
>
> 

$$
\sum d_{n}\quad\mathrm{\text{where}}\quad d_{n} = a_{0}b_{n} + a_{1}b_{n - 1} + \cdots + a_{n}b_{0}
$$


>
> to diverge. However, if $\sum d_{n}$ does converge, then it must converge to $AB$. To prove this, set
>
> 

$$
f\left. (x) \right. = \sum a_{n}x^{n},\quad g\left. (x) \right. = \sum b_{n}x^{n},\quad h\left. (x) \right. = \sum d_{n}x^{n}
$$


>
> Use [Abel's_Theorem](/notes/areas/mathematics/real_analysis/definitions/abels_theorem/) and the result in Exercise 2.8.7 to establish this result.

We are assuming that $\sum a_{n}$, $\sum b_{n}$, and $\sum d_{n}$ each converge, which, according to [Abel's_Theorem](/notes/areas/mathematics/real_analysis/definitions/abels_theorem/), implies that the series for $f,g,h$ converge uniformly on $\left. \lbrack 0,1\rbrack \right.$. Among other things, this implies that $f,g,h$ are all continuous functions over the closed interval $\left. \lbrack 0,1\rbrack \right.$.

Fix $x \in \lbrack 0,1)$. Because we know that we have [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) at 1, Theorem 6.5.1 implies that $f,g,h$ each converge absolutely. This fact means that we can invoke the result in Exercise 2.8.7 to assert that



$$
h\left. (x) \right. = \sum d_{n}x^{n} = f\left. (x) \right.g\left. (x) \right.
$$



Because this is true for all $x \in \lbrack 0,1)$, and because $f,g,h$ are continuous on the closed interval $\left. \lbrack 0,1\rbrack \right.$, it follows that $h\left. (1) \right. = f\left. (1) \right.g\left. (1) \right.$, or



$$
\sum d_{n} = \left. \left( \sum a_{n} \right) \right.\left. \left( b_{n} \right) \right.
$$



as desired.

## Exercise 6.5.11

> A series $\sum_{n = 0}^{\infty}a_{n}$ is aid to be *Abel-summable* to $L$ if the power series
>
> 

$$
f\left. (x) \right. = \sum_{n = 0}a^{n}x^{n}
$$


>
> converges for all $x \in \lbrack 0,1)$ and $L = \lim\limits_{x \rightarrow 1^{-}}f\left. (x) \right.$.

### (a)

> Show that any series that converges to a limit $L$ is also Abel-summable to $L$.

Assume that $\sum a_{n}$ converges to $L$. If we set $f\left. (x) \right. = \sum a_{n}x^{n}$, then [Abel's_Theorem](/notes/areas/mathematics/real_analysis/definitions/abels_theorem/) implies that the series for $f$ converges uniformly on the interval $\left. \lbrack 0,1\rbrack \right.$. Because the summands are continuous polynomials, this proves that $f$ is continuous on $\left. \lbrack 0,1\rbrack \right.$. In particular, this implies that $\lim\limits_{x \rightarrow 1^{-}}f\left. (x) \right. = f\left. (1) \right.$. But notice that $f\left. (1) \right. = L$ and thus we have shown that $\sum a_{n}$ is Abel-summable to $L$.

### (b)

> Show that $\sum_{n = 0}^{\infty}\left. ( - 1) \right.^{n}$ is Abel-summable and find the sum.

Using some familiar facts about geometric series, observe that



$$
\begin{aligned}
\sum_{n = 0}^{\infty}\left. ( - 1) \right.^{n}x^{n} & = 1 - x + x^{2} - x^{3} + x^{4} - \cdots \\
 & = \frac{1}{1 - \left. ( - x) \right.} \\
 & = \frac{1}{1 + x}
\end{aligned}
$$



provided $|x| < 1$. Then $\lim\limits_{x \rightarrow 1^{-}}1/\left. (1 + x) \right. = 1/2$ show that our series is Abel-summable to 1/2.

# Section 6.6 Exercises

## Exercise 6.6.1

> The derivation in Example 6.6.1 shows the Taylor series for $\arctan\left. (x) \right.$ is valid for all $x \in \left. ( - 1,1) \right.$. Notice, however, that the series also converges when $x = 1$. Assuming that $\arctan\left. (x) \right.$ is continuous, explain why the value of the series at $x = 1$ must necessarily be $\arctan\left. (1) \right.$. What indentity do we get in this case?

Because the series converges when $x = 1$, [Abel's_Theorem](/notes/areas/mathematics/real_analysis/definitions/abels_theorem/) implies that we get [uniform_convergence](/notes/areas/mathematics/real_analysis/definitions/uniform_convergence/) over the interval $\left. \lbrack 0,1\rbrack \right.$ and thus the series represents a continuous [function](/notes/areas/mathematics/set_theory/definitions/function/) over the interval $\left. \lbrack 0,1\rbrack \right.$. Assuming that $\arctan\left. (x) \right.$ is continuous over $\left. \lbrack 0,1\rbrack \right.$, it follows that if these two continuous functions agree for all values of $x \in \lbrack 0,1)$, then they must also agree when $x = 1$. Setting $x = 1$ into this formula gives \"Leibniz's formula,\"



$$
\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots
$$



## Exercise 6.6.3

> Derive the formula for the Taylor coefficients given in Theorem 6.6.2.

Restating Theorem 6.6.2 ([Taylor's_formula](/notes/areas/mathematics/real_analysis/definitions/taylors_formula/)):

> Let
>
> 

$$
f\left. (x) \right. = a_{0} + a_{1}x + a_{2}x^{2} + a_{3}x^{3} + a_{4}x^{4} + a_{5}x^{5} + \cdots
$$


>
> be defined on some non-trivial interval centered at zero. Then,
>
> 

$$
a_{n} = \frac{f^{\left. (n) \right.}\left. (0) \right.}{n!}
$$



We have that

$f\left. (0) \right. = a_{0}$

$f'\left. (0) \right. = 0 + a_{1} + \cdots = a_{1}$

$f''\left. (0) \right. = 0 + 0 + 2 \cdot 1 \cdot a_{2} + \cdots$

$f'''\left. (0) \right. = 0 + 0 + 0 + 3 \cdot 2 \cdot 2 \cdot a_{3}$

We can see a pattern emerging here, which is $f^{\left. (n) \right.}\left. (0) \right. = n!a_{n}$. Rather that $a_{n} = \frac{f^{\left. (n) \right.}\left. (0) \right.}{n!}$, which is the result we wanted.

## Exercise 6.6.5

### (a)

> Generate the Taylor coefficients for the exponential [function](/notes/areas/mathematics/set_theory/definitions/function/) $f\left. (x) \right. = e^{x}$, and then prove that the corresponding Taylor series converges uniformly to $e^{x}$ on any interval of the form $\left. \lbrack - R,R\rbrack \right.$.

### (b)

> Verify the formula $f'\left. (x) \right. = e^{x}$.

### (c)

> Use a substitution to generate the series for $e^{- x}$, and then informally calculate $e^{x}{\dot{e}}^{- x}$ by multiplying together the two series and collecting common powers of $x$.

## Exercise 6.6.7

> Find an example of each of the following or explain why no such [function](/notes/areas/mathematics/set_theory/definitions/function/) exists.

### (a)

> An infinitely [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) [function](/notes/areas/mathematics/set_theory/definitions/function/) $g\left. (x) \right.$ on all of $\mathbb{R}$ with a Taylor series that converges to $g\left. (x) \right.$ only for $x \in \left. ( - 1,1) \right.$.

### (b)

> An infinitely [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) [function](/notes/areas/mathematics/set_theory/definitions/function/) $h\left. (x) \right.$ with the same Taylor series as $\sin\left. (x) \right.$ but such that $h\left. (x) \right.$ = $\sin\left. (x) \right.$ for all $x = 0$.

### (c)

> An infinitely [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) [function](/notes/areas/mathematics/set_theory/definitions/function/) $f\left. (x) \right.$ on all of $\mathbb{R}$ with a Taylor series that converges to $f\left. (x) \right.$ if and only if $x \leq 0$.

## Exercise 6.6.9 ([Cauchy's_Remainder_Theorem](/notes/areas/mathematics/real_analysis/definitions/cauchys_remainder_theorem/))

> Let $f$ be [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) $N + 1$ times on $\left. ( - R,R) \right.$. For each $a \in \left. ( - R,R) \right.$, let $S_{N}\left. (x,a) \right.$ be the partial sum of the Taylor series for $f$ centered at $a$; in other words, define
>
> 

$$
S_{N}\left. (x,a) \right. = \sum_{n = 0}^{N}c_{n}\left. (x - a) \right.^{n}\quad\mathrm{\text{where}}\quad c_{n} = \frac{f^{\left. (n) \right.\left. (a) \right.}}{n!}
$$


>
> Let $E_{N}\left. (x,a) \right. = f\left. (x) \right. - S_{N}\left. (x,a) \right.$. Now fix $x \neq 0$ in $\left. ( - R,R) \right.$ and consider $E_{N}\left. (x,a) \right.$ as a [function](/notes/areas/mathematics/set_theory/definitions/function/) of $a$.

### (a)

> Find $E_{N}\left. (x,x) \right.$

### (b)

> Explain why $E_{N}\left. (x,a) \right.$ is [differentiable](/notes/areas/mathematics/real_analysis/definitions/differentiable/) with respect to $a$, and show
>
> 

$$
E_{N}'\left. (x,a) \right. = \frac{- f^{N + 1}\left. (x) \right.}{N!}\left. (x - a) \right.^{N}
$$



### (c)

> Show
>
> 

$$
E_{N}\left. (x) \right. = E_{N}\left. (x,0) \right. = \frac{f^{N + 1}\left. (c) \right.}{N!}\left. (x - c) \right.^{N}x
$$


>
> for some $c$ between 0 and $x$. This is Cauchy's form of the remainder for Taylor series centered at the origin.

# Section 6.7 Exercises

# Section 7.2 Exercises

## Exercise 7.2.1

> Let $f$ be a bounded [function](/notes/areas/mathematics/set_theory/definitions/function/) on $\left. \lbrack a,b\rbrack \right.$, and let $P$ be an arbitrary partition of $\left. \lbrack a,b\rbrack \right.$. First, explain why $U\left. (f) \right. \geq L\left. (f,P) \right.$. Now, prove Lemma 7.2.6.

Restating Lemma 7.2.6:

> For any bounded [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ on $\left. \lbrack a,b\rbrack \right.$, it is always the case that $U\left. (f) \right. \geq L\left. (f,P) \right.$.

We know that $U\left. (f) \right.$ corresponds to the upper integral, or the [infimum](/notes/areas/mathematics/real_analysis/definitions/infimum/) of the upper sums over the collection of all possible partitions $\mathcal{P}$.

We also know that $L\left. (f,P) \right.$ corresponds to the lower sum of some arbitrary partition $P$.

Because $L\left. (f,P) \right.$ is a [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/) for the set of upper sums, it must be less than the greatest lower bound for this set, i.e. $L\left. (f,P) \right. \leq U\left. (f) \right.$.

Since $P$ is arbitrary in this discussion, we have that $U\left. (f) \right.$ is an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) on the set of lower sums. From the definition of the [supremum](/notes/areas/mathematics/real_analysis/definitions/supremum/) we get $L\left. (f) \right. \leq U\left. (f) \right.$ as desired.

## Exercise 7.2.3 (Sequential Criterion for Integrability)

### (a)

> Prove that a bounded [function](/notes/areas/mathematics/set_theory/definitions/function/) $f$ is integrable on $\left. \lbrack a,b\rbrack \right.$ *if and only if* there exists a [sequence](/notes/areas/mathematics/real_analysis/definitions/sequence/) of partitions $\left. \left( P_{n} \right) \right._{n = 1}^{\infty}$ satisfying
>
> 

$$
\lim\limits_{n \rightarrow \infty}\left. \left\lbrack U\left. \left( f,P_{n} \right) \right. - L\left. \left( f,P_{n} \right) \right. \right\rbrack \right. = 0
$$


>
> and in this case $\int_{a}^{b}f = \lim\limits_{n \rightarrow \infty}U\left. \left( f,P_{n} \right) \right. = \lim\limits_{n \rightarrow \infty}L\left. \left( f,P_{n} \right) \right.$

### (b)

> For each $n$, let $P_{n}$ be the partition of $\left. \lbrack 0,1\rbrack \right.$ into $n$ equal subintervals. Find formulas for $U\left. \left( f,P_{n} \right) \right.$ and $L\left. \left( f,P_{n} \right) \right.$ if $f\left. (x) \right. = x$. The formula $1 + 2 + 3 + \cdots + n = n\left. (n + 1) \right./2$ will be useful

### (c)

> Use the sequential criterion for integrability from (a) to show directly that $f\left. (x) \right. = x$ is integrable on $\left. \lbrack 0,1\rbrack \right.$ and compute $\int_{0}^{1}f$.

## Exercise 7.2.5

> Assume that, for each $n$, $f_{n}$ is an integrable [function](/notes/areas/mathematics/set_theory/definitions/function/) on $\left. \lbrack a,b\rbrack \right.$. If $\left. \left( f_{n} \right) \right. \rightarrow f$ uniformly on $\left. \lbrack a,b\rbrack \right.$, prove that $f$ is also integrable on this set. (We will see that this conclusion does not necessarily follow if the [convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) is pointwise.)

## Exercise 7.2.7

> Let $f:\left. \lbrack a,b\rbrack \right. \rightarrow \mathbb{R}$ be increasing on the set $\left. \lbrack a,b\rbrack \right.$ (i.e., $f\left. (x) \right. \leq f\left. (g) \right.$ whenever $x < y$). Show that $f$ is integrable on $\left. \lbrack a,b\rbrack \right.$.

# Section 7.3 Exercises

## Exercise 7.3.1

> Consider the function 

$$
h\left. (x) \right. = \begin{cases}
1, & \mathrm{\text{for }}0 \leq x < 1 \\
2, & \mathrm{\text{for }}x = 1
\end{cases}
$$


>
> over the interval $\left. \lbrack 0,1\rbrack \right.$.

### (a)

> Show that $L\left. (f,P) \right. = 1$ for every partition $P$ of $\left. \lbrack 0,1\rbrack \right.$.

Let $P$ be an arbitrary partition of $\left. \lbrack 0,1\rbrack \right.$. On any subinterval $\left. \left\lbrack x_{k - 1},x_{k} \right\rbrack \right.$, it must be that $m_{k} = \inf\{ h\left. (x) \right.:x \in \left. \left\lbrack x_{k - 1},x_{k} \right\rbrack \right.\} = 1$, and it follows that



$$
L\left. (h,P) \right. = \sum_{k = 1}^{n}m_{k}\delta_{k} = \sum_{k = 1}^{n}\delta x_{k} = 1
$$



### (b)

> Construct a partition $P$ for which $U\left. (f,P) \right. < 1 + 1/10$.

Consider the partition $P = \{ 0,0.95,1\}$. Then



$$
U\left. (h,P) \right. = \left. (1) \right.\left. (0.95) \right. + \left. (2) \right.\left. (0.05) \right. = 1.05
$$



### (c)

> Given $\epsilon > 0$, construct a partiation $P_{\epsilon}$ for which $U(f,P_{\epsilon} < 1 + \epsilon$.

Consider the partition $P_{\epsilon} = \left. (1) \right.\left. \left( 1 - \frac{\epsilon}{2} \right) \right. + 2\left. \left( \frac{\epsilon}{2} \right) \right. = 1 + \frac{\epsilon}{2}$.

The implication is that for this partition we have $U\left. \left( h,P_{\epsilon} \right) \right. - L\left. \left( h,P_{\epsilon} \right) \right. < \epsilon$, proving that $h$ is integrable.

# Section 8.5 Exercises

## Exercise 8.5.1

### (a)

> Verify that
>
> 

$$
u\left. (x,t) \right. = b_{n}\sin\left. (nx) \right.\cos\left. (nt) \right.
$$


>
> satisfies (1), (2), and (3) below
>
> 1.  $\frac{\partial^{2}u}{dx^{2}} = \frac{\partial^{2}}{dt^{2}}$
>
> 2.  $u\left. (0,t) \right.$ and $u\left. (\pi,t) \right. = 0$
>
> 3.  $\frac{\partial u}{\partial t}\left. (x,0) \right. = 0$

Taking partial derivatives gives



$$
\frac{\partial^{2}u}{dx^{2}} = \frac{\partial^{2}}{dt^{2}} = - b_{n}\sin\left. (nx) \right.\cos\left. (nt) \right. \cdot n^{2} = \frac{\partial^{2}u}{dx^{2}} = \frac{\partial^{2}}{dt^{2}}
$$



Also,



$$
u\left. (0,t) \right. = b_{n}\sin\left. (n \cdot 0) \right.\cos\left. (nt) \right. = 0
$$



and



$$
u\left. (\pi,t) \right. = b_{n}\sin\left. (\pi n) \right.\cos\left. (nt) \right. = 0
$$



Note that this second statement requires $n$ be an integer. Finally,



$$
\frac{\partial u}{\partial t} = - b_{n}\sin\left. (nx) \right.\sin\left. (nt) \right.n
$$



and setting $t = 0$ gives $\frac{\partial u}{\partial t}\left. (x,0) \right. = 0$.

### (b)

> Explain why any finite sum of functions of the form given in part (a) would also satisfy (1), (2), and (3). (Incidentally, it is possible to hear the different solutions in (a) for values of $n$ up to 4 or 5 by isolating the harmonics on a well-made stringed instrument.)

The derivative is a [linear_transformation](/notes/areas/mathematics/real_analysis/definitions/linear_transformation/), meaning that the derivative of the sum of functions is the sum of the derivatives of each one. This property makes (1) and (3) true for a sum of solutions, and (2) is easy to check as well.

## Exercise 8.5.2

> Using trigonometric identities when necessary, verify the following integrals.

### (a)

> For all $n \in \mathbb{N}$, 

$$
\int_{- \pi}^{\pi}\cos\left. (nx) \right.dx = 0\quad\mathrm{\text{and}}\quad\int_{- \pi}^{\pi}\sin\left. (nx) \right.dx = 0
$$



For the first integral, let $u = nx$ and $du = ndx$. Applying this substitution to the limits of integration gives, for the new [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), $u = \left. ( - \pi) \right.n = \pi\left. ( - n) \right.$ and [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) $u = \pi n$. So our new integral becomes



$$
\begin{aligned}
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\cos\left. (u) \right.du & = \frac{\sin\left. (u) \right.}{n}{\text{bar}.v}_{u = \pi\left. ( - n) \right.}^{u = \pi n} \\
 & = \frac{2\sin\left. (\pi n) \right.}{n}
\end{aligned}
$$



Which is equal to zero for all $n \in \mathbb{N}$.

For the second integral, again let $u = nx$ and $du = ndx$. Applying this substitution to the limits of integration gives, for the new [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), $u = \left. ( - \pi) \right.n = \pi\left. ( - n) \right.$ and [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) $u = \pi n$. So our new integral becomes



$$
\begin{aligned}
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\sin\left. (u) \right.du & = - \frac{\cos\left. (u) \right.}{n}{\text{bar}.v}_{u = \pi\left. ( - n) \right.}^{u = \pi n} \\
 & = 0
\end{aligned}
$$



### (b)

> For all $n \in \mathbb{N}$ 

$$
\int_{- \pi}^{\pi}\cos^{2}\left. (nx) \right.dx = 0\quad\mathrm{\text{and}}\quad\int_{- \pi}^{\pi}\sin^{2}\left. (nx) \right.dx = 0
$$



For the first integral, let $u = nx$ and $du = ndx$. Applying this substitution to the limits of integration gives, for the new [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), $u = \left. ( - \pi) \right.n = \pi\left. ( - n) \right.$ and [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) $u = \pi n$. So our new integral becomes



$$
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\cos^{2}\left. (u) \right.du
$$



Writing $\cos^{2}\left. (u) \right.$ as $1/2\cos\left. (2u) \right. + 1/2$ gives



$$
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\left. \left( \frac{1}{2}\cos\left. (2u) \right. + \frac{1}{2} \right) \right.du
$$



Now, take the above integral, and integrate term by term and factor out constants



$$
\frac{1}{2}\int\cos\left. (2u) \right.du + \frac{1}{2}\int 1du
$$



For the first integral above, let $s = 2u$ and $ds = 2du$, which gives



$$
\frac{1}{4}\int\cos\left. (s) \right.ds + \frac{1}{2}\int 1du
$$



Integrating the above gives



$$
\frac{\sin\left. (s) \right.}{4} + \frac{u}{2}
$$



Substituting back for $s = 2u$ gives



$$
\frac{u}{2} + \frac{1}{4}\sin\left. (2u) \right.
$$



Finally,



$$
\begin{aligned}
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\frac{u}{2} + \frac{1}{2}\sin\left. (2u) \right.du & = - \frac{\cos\left. (u) \right.}{n}{\text{bar}.v}_{u = \pi\left. ( - n) \right.}^{u = \pi n} \\
 & = \frac{\sin\left. (2\pi n) \right.}{2n} + \pi
\end{aligned}
$$



Which is equal to $\pi$ for all $n \in \mathbb{N}$.

Now for the second integral, as usual, let $u = nx$ and $du = ndx$. Applying this substitution to the limits of integration gives, for the new [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), $u = \left. ( - \pi) \right.n = \pi\left. ( - n) \right.$ and [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) $u = \pi n$. So our new integral becomes



$$
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\sin^{2}\left. (u) \right.du
$$



Writing $\sin^{2}\left. (u) \right.$ as $1/2 - 1/2\cos\left. (2u) \right.$ gives



$$
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\left. \left( \frac{1}{2} - \frac{1}{2}\cos\left. (2u) \right. \right) \right.du
$$



Now, take the above integral, and integrate term by term and factor out constants



$$
\text{-} \frac{1}{2}\int\cos\left. (2u) \right.du + \frac{1}{2}\int 1du
$$



For the first integral above, let $s = 2u$ and $ds = 2du$, which gives



$$
\text{-} \frac{1}{4}\int\cos\left. (s) \right.ds + \frac{1}{2}\int 1du
$$



Integrating the above gives



$$
\text{-} \frac{\sin\left. (s) \right.}{4} + \frac{u}{2}
$$



Substituting back for $s = 2u$ gives



$$
\frac{u}{2} - \frac{1}{4}\sin\left. (2u) \right.
$$





$$
\begin{aligned}
\frac{1}{n}\int_{\pi\left. ( - n) \right.}^{\pi n}\frac{u}{2} - \frac{1}{4}\sin\left. (2u) \right. & = - \frac{\cos\left. (u) \right.}{n}{\text{bar}.v}_{u = \pi\left. ( - n) \right.}^{u = \pi n} \\
 & = \pi - \frac{\sin\left. (2\pi n) \right.}{2n}
\end{aligned}
$$



Which is equal to $\pi$ for all $n \in \mathbb{N}$.

### (c)

> For all $n \in \mathbb{N}$, 

$$
\int_{- \pi}^{\pi}\cos\left. (mx) \right.\sin\left. (nx) \right. = 0
$$


>
> For $m \neq n$,
>
> 

$$
\int_{- \pi}^{\pi}\cos\left. (mx) \right.\cos\left. (nx) \right. = 0\quad\mathrm{\text{and}}\quad\int_{- \pi}^{\pi}\sin\left. (mx) \right.\sin\left. (nx) \right. = 0
$$



Let $u = nx$ and $du = ndx$. Applying this substitution to the limits of integration gives, for the new [lower_bound](/notes/areas/mathematics/real_analysis/definitions/lower_bound/), $u = \left. ( - \pi) \right.n = \pi\left. ( - n) \right.$ and [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) $u = \pi n$. So our new integral becomes

Using the trig identity $\sin\left. (\alpha) \right.\cos\left. (\beta) \right. = 1/2\left. \left\lbrack \sin\left. (\alpha - \beta) \right. + \sin\left. (\alpha + \beta) \right. \right\rbrack \right.$, where $\alpha = nx$ and $\beta = mx$, we have



$$
\frac{1}{2}\int\left. \left\lbrack \sin\left. \left( x\left. (m + n) \right. \right) \right. - \sin\left. \left( x\left. (m - n) \right. \right) \right. \right\rbrack \right.dx
$$



Now, integrate the sum term by term and factor out constants



$$
\frac{1}{2}\int\sin\left. \left\lbrack x\left. (m + n) \right. \right\rbrack \right.dx - \frac{1}{2}\sin\left. \left\lbrack x\left. (m - n) \right. \right\rbrack \right.dx
$$



For the first integrand $\sin\left. \left\lbrack x\left. (m + n) \right. \right\rbrack \right.$, let $u = x\left. (m + n) \right.$ and $du = \left. (m + n) \right.dx$. Then we have



$$
\frac{1}{2\left. (m + n) \right.}\int\sin\left. (u) \right.du - \frac{1}{2}\int\sin\left. \left\lbrack x\left. (m - n) \right. \right\rbrack \right.dx = - \frac{\cos\left. (u) \right.}{2\left. (m + n) \right.} - \frac{1}{2}\sin\left. \left\lbrack x\left. (m - n) \right. \right\rbrack \right.dx
$$



For the remaining integrand $\sin\left. \left\lbrack x\left. (m - n) \right. \right\rbrack \right.$, let $s = x\left. (m - n) \right.$ and $ds = \left. (m - n) \right.dx$. Then we have



$$
\text{-} \frac{\cos\left. (u) \right.}{2\left. (m + n) \right.} - \frac{1}{2\left. (m - n) \right.}\int\sin\left. (s) \right.ds = - \frac{\cos\left. (u) \right.}{2\left. (m + n) \right.} - \cos\left. (u) \right. + C
$$



Now, substituting back in for $s = x\left. (m - n) \right.$ and $u = x\left. (m + n) \right.$ gives



$$
\frac{m\sin\left. (mx) \right.\sin\left. (nx) \right. + n\cos\left. (mx) \right.\cos\left. (nx) \right.}{m^{2} - n^{2}} = \frac{\cos\left. \left\lbrack x\left. (m - n) \right. \right\rbrack \right.}{2\left. (m - n) \right.} - \frac{\cos\left. \left\lbrack x\left. (m + n) \right. \right\rbrack \right.}{2\left. (m + n) \right.}{\text{bar}.v}_{u = \pi\left. ( - n) \right.}^{u = \pi n} = 0
$$



## Exercise 8.5.3

> Derive the formulas
>
> 

$$
a_{m} = \frac{1}{\pi}\int_{- \pi}^{\pi}f\left. (x) \right.\cos\left. (mx) \right.dx\quad\mathrm{\text{and}}\quad b_{m} = \frac{1}{\pi}\int_{- \pi}^{\pi}f\left. (x) \right.\sin\left. (mx) \right.dx
$$


>
> for all $m \geq 1$.

Restating equation (6) from the text:



$$
f\left. (x) \right. = a_{0} + \sum_{n = 1}^{\infty}a_{n}\cos\left. (nx) \right. + b_{n}\sin\left. (nx) \right.
$$



Multiplying each side of this equation by $\cos\left. (mx) \right.$, we get



$$
\begin{aligned}
f\left. (x) \right.\cos\left. (mx) \right. & = a_{0}\cos\left. (mx) \right. \\
 & = \sum_{n = 1}^{\infty}a_{n}\cos\left. (nx) \right.\cos\left. (mx) \right. + b_{n}\sin\left. (nx) \right.\cos\left. (mx) \right.
\end{aligned}
$$



Now take the integral of each side of this equation from $- \pi$ to $\pi$ and, as before, distribute the integral through the infinite sum. Using Exercise 8.5.2, we see that for $a_{0}$ and for every value of $n \in \mathbb{N}$, we get an integral that equals zero except the one where $n = m$. When $n = m$ we get



$$
\int_{- \pi}^{\pi}a_{m}\cos^{2}\left. (mx) \right.dx = a_{m}\pi
$$



and it follows that



$$
\int_{- \pi}^{\pi}\cos^{2}\left. (mx) \right.dx = a_{m}\pi
$$



The formula for $a_{m}$ is immediate. To get the formula for $b_{m}$, we multiply across equation (6) by $\sin\left. (mx) \right.$ and follow the same procedure.
