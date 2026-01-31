---
title: "Archimedean Property"
---

# [Archimedean_Property](/notes/areas/mathematics/real_analysis/definitions/archimedean_property/)

## Theorem

1.  Given any number $x \in \mathbb{R}$, there exists an $n \in \mathbb{N}$ satisfying $n > x$.

2.  Given any real number $y > 0$, there exists an $n \in \mathbb{N}$ satisfying $1/n < y$

## Proof

Proceed via [proof_by_contradiction](/notes/areas/mathematics/proof_techniques/definitions/proof_by_contradiction/). Assume, for contradiction, that $N$ is bounded above. By the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/) (AoC), $\mathbb{N}$ should then have a least upper bound, and we can set $\alpha = \sup\mathbb{N}$. If we consider $\alpha - 1$, then we no longer have an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/), and therefore there exists an $n \in \mathbb{N}$ satisfying $\alpha - 1 < n$ But this is equivalent to $\alpha < n + 1$. Because $n + 1 \in \mathbb{N}$, we have a contradiction to the fact that $\alpha$ is supposed to be an [upper_bound](/notes/areas/mathematics/real_analysis/definitions/upper_bound/) for $\mathbb{N}$. (Notice that the contradiction here depends only on the [axiom_of_completeness](/notes/areas/mathematics/real_analysis/definitions/axiom_of_completeness/) and the fact that $\mathbb{N}$ is closed under addition.)
