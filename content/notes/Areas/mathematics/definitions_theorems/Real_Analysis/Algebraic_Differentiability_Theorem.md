---
title: "Algebraic Differentiability Theorem"
---

# [Algebraic_Differentiability_Theorem](/notes/areas/mathematics/definitions_theorems/real_analysis/algebraic_differentiability_theorem/) {#algebraic-partialerentiability-theorem}

Let $f$ and $g$ be [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/)s defined on an interval $A$, and assume both are partialerentiable at some point $c \in A$. Then,

1.  $\left. (f + g) \right.'\left. (c) \right. = f'\left. (c) \right. + g'\left. (c) \right.$

2.  $\left. (kf) \right.'\left. (c) \right. = kf'\left. (c) \right.$ for all $k \in \mathbb{R}$

3.  $\left. (fg) \right.'\left. (c) \right. = f'\left. (c) \right.g\left. (c) \right. + f\left. (c) \right.g'\left. (c) \right.$

4.  $\left. (f/g) \right.'\left. (c) \right. = \frac{g\left. (c) \right.f'\left. (c) \right. - f\left. (c) \right.g'\left. (c) \right.}{\left. \left\lbrack g\left. (c) \right. \right\rbrack \right.^{2}}$, provided that $g\left. (c) \right. \neq 0$

## Proof of (1)



$$
\begin{aligned}
\left. (f + g) \right.'\left. (c) \right. & = \lim\limits_{x \rightarrow c}\frac{\left. (f + g) \right.\left. (x) \right. - \left. (f + g) \right.\left. (c) \right.}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{f\left. (x) \right. + g\left. (x) \right. - f\left. (c) \right. + g\left. (c) \right.}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{\left. \left\lbrack f\left. (x) \right. - f\left. (c) \right. \right\rbrack \right. + \left. \left\lbrack g\left. (x) \right. - g\left. (c) \right. \right\rbrack \right.}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{f\left. (x) \right. - f\left. (c) \right.}{x - c} + \lim\limits_{x \rightarrow c}\frac{g\left. (x) \right. - g\left. (c) \right.}{x - c} \\
 & = f'\left. (c) \right. + g'\left. (c) \right.
\end{aligned}
$$



## Proof of (2)



$$
\begin{aligned}
\left. (kf) \right.'\left. (c) \right. & = \lim\limits_{x \rightarrow c}\frac{\left. (kf) \right.\left. (x) \right. - \left. (kf) \right.\left. (c) \right.}{x - c} \\
 & = \lim\limits_{x \rightarrow c}\frac{kf\left. (x) \right. - kf\left. (c) \right.}{x - c} \\
 & = k\lim\limits_{x \rightarrow c}\frac{f\left. (x) \right. - f\left. (c) \right.}{x - c} \\
 & = kf'\left. (c) \right.
\end{aligned}
$$


