---
title: "functional limit"
---

# Functional Limit

## Definition

Let $f:A \rightarrow \mathbb{R}$, and let $c$ be a [limit_point](/notes/areas/mathematics/topology/definitions/limit_point/) of the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) $A$. We say that $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$ provided that, for all $\epsilon > 0$, there exists a $\delta > 0$ such that whenever $0 < |x - c| < \delta$ (and $x \in A$) it follows that $\left| f\left. (x) \right. - L \right| < \epsilon$.

This is often referred to as the "$\epsilon - \delta$" of the definition for *functional limit*s. Recall that the statement



$$
\left| f\left. (x) \right. - L \right| < \epsilon\mathrm{\text{ is equivalent to }}f\left. (x) \right. \in V_{\epsilon}\left. (L) \right.
$$



Likewise, the statement is equivalent to



$$
|x - c| < \delta\mathrm{\text{ is satisfied if and only if }}x \in V_{\delta}\left. (c) \right.
$$



# Functional Limit: Topological Version

## Definition

Let $c$ be a [limit_point](/notes/areas/mathematics/topology/definitions/limit_point/) of the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) of $f:A \rightarrow \mathbb{R}$. We say that $\lim\limits_{x \rightarrow c}f\left. (x) \right. = L$ provided that, for every $\epsilon$-neighborhood (see [epsilon-neighborhood](/notes/areas/mathematics/real_analysis/definitions/epsilon-neighborhood/)) $V_{\delta}\left. (c) \right.$ around $c$ with the property that for all $x \in V_{\delta}\left. (c) \right.$ different from $c$ (with $x \in$ A), it follows that $f\left. (x) \right. \in V_{\epsilon}\left. (L) \right.$.

The parenthetical reminder "($x \in A$)" present in both versions of the definition is included to ensure that $x$ is an allowable input for the [function](/notes/areas/mathematics/set_theory/definitions/function/) in question. When no confusion is likely, we may omit this reminder with the understanding that the appearance of $f\left. (x) \right.$ carries with it the implicit assumption that $x$ is in the [domain](/notes/areas/mathematics/set_theory/definitions/domain/) of $f$. On a related note, there is no reason to discuss functional limits at [isolated_point](/notes/areas/mathematics/topology/definitions/isolated_point/)s of the [domain](/notes/areas/mathematics/set_theory/definitions/domain/). Thus, functional limits will only be considered as $x$ tends toward a [limit_point](/notes/areas/mathematics/topology/definitions/limit_point/) of the [function](/notes/areas/mathematics/set_theory/definitions/function/)'s [domain](/notes/areas/mathematics/set_theory/definitions/domain/).
