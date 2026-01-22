---
title: "Density of Q in R"
---

# Density_of_\$bb(Q)\$_in_\$bb(R)\$ {#density-of-mathbbq-in-mathbbr}

Theorem: For every two real numbers $a$ and $b$ with $a < b$, there exists a rational number $r$ satisfying $a < r < b$.

Proof: A rational number is a quotient of integers, so we must produce an $m \in \mathbb{Z}$ and $n \in \mathbb{N}$ such that



$$
a < \frac{m}{n} < b
$$



The first step is to choose the denominator $n$ large enough so that the consecutive increments of size $1/n$ are too close together to "step over" the interval $\left. (a,b) \right.$.

Using the [Archimedean_Property](/notes/areas/mathematics/definitions_theorems/real_analysis/archimedean_property/), we may pick $n \in \mathbb{N}$ large enough such that



$$
\frac{1}{n} < b - a
$$



Inequality (1), which we are trying to prove, is equivalent to $na < m < ab$. With $n$ already chosen, the idea now is to choose $m$ to be the smallest integer greater than $na$. In other words, pick $m \in \mathbb{Z}$ such that



$$
\frac{m - 1}{n} \leq a \leq \frac{m}{n}
$$



rather, that



$$
m - 1\overset{\left. (3) \right.}{\leq}na\overset{\left. (4) \right.}{<}m
$$



Now, inequality (4) immediately yields $a < \frac{m}{n}$, which is half the battle. Keeping in mind the inequality (2) is equivalent to $a < b - \frac{1}{n}$, we can use (3) to write



$$
\begin{aligned}
m - 1 & \leq na \\
m & \leq na + 1 \\
 & < n\left. \left( b - \frac{1}{n} \right) \right. + 1 \\
 & = nb
\end{aligned}
$$



Because $m < nb$ imples $\frac{m}{n} < b$, we have $a < \frac{m}{n} < b$ as desired.

So $\mathbb{Q}$ is dense in $\mathbb{R}$.
