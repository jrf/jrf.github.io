---
title: "Fun with Chaos Attractors"
date: 2025-05-30T09:29:00-06:00
categories: [chaos]
math: true
---

![Clifford Attractor](/img/clifford_attractor.png)

The Clifford attractor is a 2D strange attractor defined by the iterative map:

$$
\begin{aligned}
x_{n+1} &= \sin(a \cdot y_n) + c \cdot \cos(a \cdot x_n) \\
y_{n+1} &= \sin(b \cdot x_n) + d \cdot \cos(b \cdot y_n)
\end{aligned}
$$

With parameters $a = 1.8$, $b = -1.9$, $c = 1.0$, $d = 1.5$, the system traces out intricate fractal structures. The image above was generated from 300 million iterations, rendered as a density histogram with logarithmic scaling to reveal the fine detail in regions where the trajectory lingers.

[Code](/code/clifford_attractor/)
