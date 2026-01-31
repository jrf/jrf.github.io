---
title: "discrete probability measure"
---

# Discrete_Probability_Measure

## Definition

Let $\Omega = \{\omega_{1},\omega_{2},\ldots\}$ be a [countable](/notes/areas/mathematics/set_theory/definitions/countable/) set and $\left. \left( p_{n} \right) \right._{n \in \mathbb{N}}$ be a sequence of real numbers $p_{n} \in \left. \lbrack 0,1\rbrack \right.$ such that $\sum_{n \in \mathbb{N}}p_{n} = 1$. On $(\Omega,\mathcal{P}\left. (\Omega) \right.$ the set function



$$
P\left. (A) \right. = \sum_{n:\omega_{n} \in A}p_{n} = \sum_{n \in \mathbb{N}}p_{n}\delta_{\omega_{n}}\left. (A) \right.,\quad A \subseteq \Omega
$$



defines a [probability_measure](/notes/areas/mathematics/measure_theory/definitions/probability_measure/). The triplet $\left. \left( \Omega,\mathcal{P}\left. (\Omega) \right.,\mathbb{P} \right) \right.$ is called a [discrete_probability_space](/notes/areas/mathematics/measure_theory/definitions/discrete_probability_space/).
