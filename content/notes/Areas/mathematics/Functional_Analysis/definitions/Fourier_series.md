---
title: "Fourier series"
---

# Fourier Series

A **Fourier series** represents a periodic function as an infinite sum of sines and cosines (or complex exponentials) at integer multiples of a fundamental frequency.

## Definition

For a function $f(x)$ with period $T$, the Fourier series is:



$$
f(x) = \sum_{n=-\infty}^{\infty} c_n \, e^{j 2\pi n x / T}
$$



where the **Fourier coefficients** are:



$$
c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(x) \, e^{-j 2\pi n x / T} \, dx
$$



## Real Form

Using Euler's formula, the series can be written with sines and cosines:



$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\left(\frac{2\pi n x}{T}\right) + b_n \sin\left(\frac{2\pi n x}{T}\right) \right]
$$



where:



$$
a_n = \frac{2}{T} \int_{-T/2}^{T/2} f(x) \cos\left(\frac{2\pi n x}{T}\right) dx
$$





$$
b_n = \frac{2}{T} \int_{-T/2}^{T/2} f(x) \sin\left(\frac{2\pi n x}{T}\right) dx
$$



## Relationship to Fourier Transform

| Fourier Series | [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) |
|----------------|-------------------|
| Periodic functions | Aperiodic functions |
| Discrete spectrum (harmonics) | Continuous spectrum |
| Coefficients $c_n$ | Transform $F(f)$ |
| Sum over integers | Integral over all frequencies |

The [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of a periodic function yields [Dirac delta functions](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) at the harmonic frequencies, with weights equal to the Fourier coefficients:



$$
\mathcal{F}\{f(x)\} = \sum_{n=-\infty}^{\infty} c_n \, \delta\left(f - \frac{n}{T}\right)
$$



## Convergence

The Fourier series converges to $f(x)$ under various conditions:

| Condition | Type of [Convergence](/notes/areas/mathematics/real_analysis/definitions/convergence/) |
|-----------|---------------------|
| $f$ is piecewise smooth | Pointwise (to midpoint at jumps) |
| $f$ is continuous | Uniform |
| $f \in L^2$ | Mean-square (Parseval's theorem) |

At points of discontinuity, the series converges to the average of left and right limits.

## Parseval's Theorem

The total "energy" in a period equals the sum of squared coefficients:



$$
\frac{1}{T} \int_{-T/2}^{T/2} |f(x)|^2 \, dx = \sum_{n=-\infty}^{\infty} |c_n|^2
$$



## Examples

### Square Wave



$$
f(x) = \text{sgn}(\sin(2\pi x/T))
$$





$$
f(x) = \frac{4}{\pi} \sum_{n=1,3,5,...}^{\infty} \frac{1}{n} \sin\left(\frac{2\pi n x}{T}\right)
$$



Only odd harmonics are present (due to symmetry).

### Triangle Wave



$$
f(x) = \frac{8}{\pi^2} \sum_{n=1,3,5,...}^{\infty} \frac{(-1)^{(n-1)/2}}{n^2} \sin\left(\frac{2\pi n x}{T}\right)
$$



Coefficients decay as $1/n^2$ (faster than square wave) because the function is smoother.

## Applications in Optics

- **[Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) gratings**: Periodic structures analyzed via Fourier series
- **Periodic objects**: Produce discrete [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) orders at harmonic frequencies
- **[Holography](/notes/areas/electrical_engineering/physical_optics/definitions/holography/)**: Periodic fringe patterns encode Fourier coefficients

## 2D Generalization

For a function periodic in both $x$ and $y$ with periods $X$ and $Y$:



$$
f(x, y) = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} c_{nm} \, e^{j 2\pi (nx/X + my/Y)}
$$



## See Also

- [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)
- [Dirac delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/)
- [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/)
- [Parseval theorem](/notes/areas/mathematics/functional_analysis/definitions/parseval_theorem/)
