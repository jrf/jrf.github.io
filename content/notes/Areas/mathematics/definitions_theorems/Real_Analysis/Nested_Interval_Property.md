---
title: "Nested Interval Property"
---

# [Nested_Interval_Property](/notes/areas/mathematics/definitions_theorems/real_analysis/nested_interval_property/)

For each $n \in \mathbb{N}$, assume we are given a closed interval $I_{n} = \left. \left\lbrack a_{n},b_{n} \right\rbrack \right. = \{ x \in \mathbb{R}:a_{n} \leq x \leq b_{n}\}$. Assume also that each $I_{n}$ contains $I_{n + 1}$. Then, the resulting nested [sequence](/notes/areas/mathematics/definitions_theorems/real_analysis/sequence/) of closed intervals



$$
I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq I_{4} \supseteq \cdots
$$



has a non-empty intersection. That is to say



$$
{\bigcap(n = 1)}^{\infty}I_{n} \neq \varnothing
$$



## Proof

In order to show that ${\bigcap(n = 1)}^{\infty}I_{n}$ is not empty, we are going to use the Axiom_of_Completeness (AoC) to produce a single real number $x$ satisfying $x \in I_{n}$ for every $n \in \mathbb{N}$. Now, the AoC is a statement about bounded sets, and the one we want to consider is the set



$$
A = \{ a_{n}:n \in \mathbb{N}\}
$$



of left-hand endpoints of the intervals.

Because the intervals are nested, we see that every $b_{n}$ serves as an [upper_bound](/notes/areas/mathematics/definitions_theorems/real_analysis/upper_bound/) for $A$. Thus, we are justified in setting



$$
x = \sup A
$$



Now, consider a particular $I_{n} = \left. \left\lbrack a_{n},b_{n} \right\rbrack \right.$. Because $x$ is an [upper_bound](/notes/areas/mathematics/definitions_theorems/real_analysis/upper_bound/) for $A$, we have $a_{n} \leq x$. The fact that each $b_{n}$ is an [upper_bound](/notes/areas/mathematics/definitions_theorems/real_analysis/upper_bound/) for $A$ and that $x$ is the least upper bound implies $x \leq b_{n}$.

All together then, we have $a_{n} \leq x \leq b_{n}$, which means $x \in I_{n}$ for every choice of $n \in \mathbb{N}$. Hence, $x \in {\bigcap(n = 1)}^{\infty}I_{n}$, and the intersection is not empty.
