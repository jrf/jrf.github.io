---
title: "linearly dependent"
---

# Linearly_dependent

## Definition

A [list](/notes/areas/mathematics/definitions_theorems/linear_algebra/list/) of vectors in $V$ is called *linearly dependent* if it is not [linearly_independent](/notes/areas/mathematics/definitions_theorems/linear_algebra/linearly_independent/).

In other words a [list](/notes/areas/mathematics/definitions_theorems/linear_algebra/list/) $v_{1},\ldots,v_{m}$ of vectors in $V$ is linearly dependent if there exist $a_{1},\ldots,a_{m} \in \mathbb{F}$, not all 0, such that $a_{1}v_{1} + \cdots + a_{m}v_{m} = 0$.

## Linear Dependence Lemma (Axler --- Theorem 2.21)

Suppose $v_{1},\ldots,v_{m}$ is a *linearly dependent* [list](/notes/areas/mathematics/definitions_theorems/linear_algebra/list/) in $V$. Then there exists $j \in \{ 1,2,\ldots,m\}$ such that the following hold:

1.  $v_{j} \in \text{ span }\left. \left( v_{1},\ldots,v_{j - 1} \right) \right.$;

2.  if the $j^{\mathrm{\text{th}}}$ term is removed from $v_{1},\ldots,v_{m}$, the [span](/notes/areas/mathematics/definitions_theorems/linear_algebra/span/) of the remaining [list](/notes/areas/mathematics/definitions_theorems/linear_algebra/list/) equals $\text{span }\left. \left( v_{1},\ldots,v_{m} \right) \right.$.

For (1), this means that for $j \in \{ 1,2,\ldots,m\}$, there exists at least one vector which belongs to the [span](/notes/areas/mathematics/definitions_theorems/linear_algebra/span/) of the rest of the vectors.

Proof: see this [example](https://math.stackexchange.com/a/494203), this [example](https://math.stackexchange.com/a/1614562), and this [example](http://mathonline.wikidot.com/linear-dependence-lemma).
