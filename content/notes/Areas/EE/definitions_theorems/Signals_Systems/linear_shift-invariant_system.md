---
title: "linear shift-invariant system"
---

# Linear Shift-Invariant System

A **linear shift-invariant (LSI)** system is an operator $\mathcal{H}$ that satisfies two properties:

## Definition

1. **Linearity**: For any inputs $g_1(x)$, $g_2(x)$ and scalars $a$, $b$:


$$
\mathcal{H}\{a g_1(x) + b g_2(x)\} = a\mathcal{H}\{g_1(x)\} + b\mathcal{H}\{g_2(x)\}
$$



2. **Shift-Invariance**: If $\mathcal{H}\{g(x)\} = h(x)$, then:


$$
\mathcal{H}\{g(x - x_0)\} = h(x - x_0)
$$



Physically, shifting the input shifts the output by the same amount without changing its form.

## Characterization

An LSI system is completely characterized by its [impulse response](/notes/areas/ee/definitions_theorems/signals_systems/impulse_response/) $h(x)$. The output for any input is given by [convolution](/notes/areas/mathematics/definitions_theorems/real_analysis/convolution/):



$$
g_{\text{out}}(x) = g_{\text{in}}(x) * h(x) = \int_{-\infty}^{\infty} g_{\text{in}}(\xi) \, h(x - \xi) \, d\xi
$$



## Eigenfunctions

Complex exponentials $e^{j2\pi f x}$ are eigenfunctions of all LSI systems:



$$
\mathcal{H}\{e^{j2\pi f x}\} = H(f) \cdot e^{j2\pi f x}
$$



where $H(f) = \mathcal{F}\{h(x)\}$ is the [transfer function](/notes/areas/ee/definitions_theorems/signals_systems/transfer_function/) (eigenvalue).

## Examples in Optics

**Shift-invariant:**
- Diffraction
- Defocus blur
- Spherical aberration

**Not shift-invariant:**
- Coma
- Astigmatism
- Distortion

## Related Articles

- [impulse_response](/notes/areas/ee/definitions_theorems/signals_systems/impulse_response/)
- [transfer_function](/notes/areas/ee/definitions_theorems/signals_systems/transfer_function/)
- [point_spread_function](/notes/areas/ee/definitions_theorems/signals_systems/point_spread_function/)
- [convolution](/notes/areas/mathematics/definitions_theorems/real_analysis/convolution/)
