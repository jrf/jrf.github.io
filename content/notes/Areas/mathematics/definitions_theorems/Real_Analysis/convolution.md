---
title: "convolution"
---

# Convolution

## Definition

Wikipedia:

In mathematics (in particular, functional analysis), *convolution* is a mathematical operation on two [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/)s ($f$ and $g$) that produces a third [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/) $\left. (f*g) \right.$ that expresses how the shape of one is modified by the other. The term convolution refers to both the result [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/) and to the process of computing it. It is defined as the integral of the product of the two [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/)s after one is reversed and shifted. And the integral is evaluated for all values of shift, producing the convolution [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/).

Wolfram:

A convolution is an integral that expresses the amount of overlap of one function g as it is shifted over another [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/) $f$. It therefore "blends" one [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/) with another.

Abstractly, a convolution is defined as a product of [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/)s $f$ and $g$ that are objects in the algebra of [Schwartz_function](/notes/areas/mathematics/definitions_theorems/functional_analysis/schwartz_function/)s in $\mathbb{R}^{n}$. Convolution of two [function](/notes/areas/mathematics/definitions_theorems/set_theory/function/)s $f$ and $g$ over a finite range $\left. \lbrack 0,t\rbrack \right.$ is given by



$$
\left. \lbrack f*g\rbrack \right.\left. (t) \right. = \int_{0}^{t}f\left. (\tau) \right.g\left. (t - \tau) \right.d\tau
$$



where $\left. \lbrack f*g\rbrack \right.$ denotes the convolution of $f$ and $g$.

## Related Articles

[Convolution Integral Example 05 - Convolution Of Unit Step With Pulse](https://www.youtube.com/watch?v=r40Zdwsf1ds)

[Understanding Convolutions](https://colah.github.io/posts/2014-07-Understanding-Convolutions/)
