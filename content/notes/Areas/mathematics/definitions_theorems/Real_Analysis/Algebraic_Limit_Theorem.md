---
title: "Algebraic Limit Theorem"
---

# [Algebraic_Limit_Theorem](/notes/areas/mathematics/definitions_theorems/real_analysis/algebraic_limit_theorem/)

Let $\lim a_{n} = a$ and $\lim b_{n} = b$. Then,

1.  $\lim\left. \left( ca_{n} \right) \right. = ca$, for all $c \in \mathbb{R}$

2.  $\lim\left. \left( a_{n} + b_{n} \right) \right. = a + b$

3.  $\lim\left. \left( a_{n}b_{n} \right) \right. = ab$

4.  $\lim\left. \left( a_{n}/b_{n} \right) \right. = a/b$, provided $b \neq 0$

## Proof of (1)

Consider the case where $c \neq 0$. We want to show that the sequence $\left. \left( ca_{n} \right) \right.$ converges to $ca$. Let $\epsilon > 0$ be arbitrary. Our goal is to find some point in the sequence $\left. \left( ca_{n} \right) \right.$ after which we have



$$
\left| ca_{n} - ca \right| < \epsilon
$$



Now,



$$
\left| ca_{n} - ca \right| = |c|\left| a_{n} - a \right|
$$



We are given that $\left. \left( a_{n} \right) \right. \rightarrow a$, so we know we can make $\left| a_{n} - a \right|$ as small as we like. In particular, we can choose an $N$ such that



$$
\left| a_{n} - a \right| < \frac{\epsilon}{|c|}
$$



whenever $n \geq N$. To see that this $N$ indeed works, observe that, for all $n \geq N$,



$$
\left| ca_{n} - ca \right| = |c|\left| a_{n} - a \right| < |c|\frac{\epsilon}{|c|} = \epsilon
$$



The case $c = 0$ reduces to showing that the constant sequence $\left. (0,0,0,\ldots) \right.$ converges to 0, which is easily verified.

## Proof of (2)

To prove this statement, we need to argue that the identity



$$
\left| \left. \left( a_{n} + b_{n} \right) \right. - \left. (a + b) \right. \right|
$$



can be made less than an arbitrary $\epsilon$ using the assumptions that $\left| a_{n} - a \right|$ and $\left| b_{n} - b \right|$ can be made as small as we like for large $n$. The first step is to use the triangle inequality to say



$$
\left| \left. \left( a_{n} + b_{n} \right) \right. - \left. (a + b) \right. \right| = \left| \left. \left( a_{n} - a \right) \right. + \left. \left( b_{n} - b \right) \right. \right| \leq \left| a_{n} - a \right| + \left| b_{n} - b \right|
$$



Again, we let $\epsilon > 0$ be arbitrary. The technique this time is to divide the $\epsilon$ between the two expressions on the right-hand side in the preceding inequality. Using the hypothesis that $\left. \left( a_{n} \right) \right. \rightarrow a$, we know there exists an $N_{1}$ such that



$$
\left| a_{n} - a \right| < \frac{\epsilon}{2}\quad\mathrm{\text{whenever }}n \geq N_{1}
$$



Likewise, the assumption that $\left. \left( b_{n} \right) \right. \rightarrow b$ means that we can choose an $N_{2}$ such that



$$
\left| b_{n} - b \right| < \frac{\epsilon}{2}\quad\mathrm{\text{whenever }}n \geq N_{b}
$$



The question now arises as to which of $N_{1}$ or $N_{2}$ we should take to be our choice of $N$. By choosing $N = \max\{ N_{1},N_{2}\}$, we ensure that if $n \geq N$, then $n \geq N_{1}$ and $n \geq N_{2}$. This allows us to conclude that



$$
\begin{aligned}
|\left. \left( a_{n} + b_{n} \right) \right. - \left. (a + b) \right. & \leq \left| a_{n} - a \right| + \left| b_{n} - b \right| \\
 & < \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
 & = \epsilon
\end{aligned}
$$



for all $n \geq N$, as desired.
