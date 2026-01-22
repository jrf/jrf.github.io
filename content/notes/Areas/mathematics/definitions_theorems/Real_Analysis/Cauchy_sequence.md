---
title: "Cauchy sequence"
---

# [Cauchy_sequence](/notes/areas/mathematics/definitions_theorems/real_analysis/cauchy_sequence/)

## Definition

A [sequence](/notes/areas/mathematics/definitions_theorems/real_analysis/sequence/) $\left. \left( a_{n} \right) \right.$ is called a *Cauchy sequence* if, for every $\epsilon > 0$, there exists an $N \in \mathbb{N}$ such that whenever $m,n \geq N$ it follows that $\left| a_{n} - a_{m} \right| < \epsilon$.

Compare this to the definition of [convergence](/notes/areas/mathematics/definitions_theorems/real_analysis/convergence/).

## Theorem: Every convergent sequence is a Cauchy sequence

Proof: Assume $\left. \left( x_{n} \right) \right. \rightarrow x$. Let $\epsilon > 0$ be arbitrary. There exists an $N \in \mathbb{N}$ such that $n,m \geq N$ implies that $\left| x_{n} - x \right| < \frac{\epsilon}{2}$ and $\left| x_{m} - x \right| < \frac{\epsilon}{2}$.

By the triangle inequality



$$
\begin{aligned}
\left| x_{n} - x_{m} \right| & = \left| x_{n} - x + x - x_{m} \right| \\
 & \leq \left| x_{n} - x \right| + \left| x_{m} - x \right| \\
 & < \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
 & = \epsilon
\end{aligned}
$$


