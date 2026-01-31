---
title: "Schwartz function"
---

# [Schwartz_function](/notes/areas/mathematics/functional_analysis/definitions/schwartz_function/)

## Definition

A function $f \in C^{\infty}\left. \left( \mathbb{R}^{n} \right) \right.$is called a *Schwartz function* if it goes to zero as $|x| \rightarrow \infty$ faster than any inverse power of $x$, as do all its derivatives. That is, a [function](/notes/areas/mathematics/set_theory/definitions/function/) is a Schwartz function if there exist real constants $C_{\alpha\beta}$ such that



$$
\sup\limits_{x \in \mathbb{R}^{n}}\left| x^{\alpha}\partial_{\beta}f\left. (x) \right. \right| \leq C^{\alpha\beta}
$$



where [multi-index notation](https://mathworld.wolfram.com/Multi-IndexNotation.html) has been used for $\alpha$ and $\beta$.

## Related Articles

<https://mathworld.wolfram.com/SchwartzFunction.html>
