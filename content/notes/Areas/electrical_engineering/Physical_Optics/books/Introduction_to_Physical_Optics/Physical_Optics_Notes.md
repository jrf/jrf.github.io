---
title: "Physical Optics Notes"
---

# Review of Linear Systems Theory

## I. Introduction

Physical optics is the study of the wave nature of light. [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/), polarization, [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) and interferometry are all physical optics effects, and play a key role in many modern optical systems. The first half of this course will be devoted to studying the key concepts of physical optics.

In the early 1960's, the mathematics of linear systems was applied to physical optics, providing a new and powerful way of analyzing optical systems. This analysis technique is now known as Fourier optics. With the tools of Fourier optics we will be able to explain the intricacies of [holography](/notes/areas/electrical_engineering/physical_optics/definitions/holography/), understand how astronomers can get incredibly detailed images of distant galaxies using radio telescopes separated by thousands of kilometers (a technique called Very Long Baseline Interferometry), calculate the [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) effects of microscopes which limit their resolution, understand Synthetic Aperture Radar, describe methods of "seeing through" a turbulent atmosphere, understand how optical pattern recognition machines work, and much more. Before we start, however, it is useful to review the most important aspects of linear systems theory.

## II. Linear Systems

Many optical devices and effects can be described as linear

systems. A system is **linear** if we can apply **[superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/)**.



$$
\mathcal{L}\{a_1 s(\bar{x}) + a_2 t(\bar{x})\} = a_1 \mathcal{L}\{s(\bar{x})\} + a_2 \mathcal{L}\{t(\bar{x})\}
$$



The operator $\mathcal{L}$ describes the linear system. In electronics for example, this system could be a filter. In optics it may be an imaging system of some kind.

The operator $\mathcal{L}$ can be described in various ways. One particularly useful way is by its **[impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** (often called a **[point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/)** in optics). Physically, it is the response of the linear system to a single point at a particular location in a plane. Consider the point (expressed as [delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/)) located at $x_0$. The response of the linear system to this point is given by:



$$
\mathcal{L}\{\delta(\bar{x}_1 - \bar{x}_0)\} = h(\bar{x}_2; \bar{x}_0)
$$



$h(\bar{x}_2; \bar{x}_0)$ is the **[point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/)** associated with the input point $\bar{x}_0$.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Notation $h(\bar{x}_2; \bar{x}_0)$</div>
<div class="callout-content">

The semicolon notation indicates that *h is also a function of where the point spread is placed in the input*. For a general linear system, the shape of the response can change depending on input location.

The [delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) is $\delta(\bar{x}_1 - \bar{x}_0)$ (the input point source). The $\mathcal{L}\{\cdot\}$ is the linear system operator applied to it, producing the [PSF](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/) $h(\bar{x}_2; \bar{x}_0)$ as output.

</div>
</div>

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Connection to Green's Functions</div>
<div class="callout-content">

The point spread function in optics is mathematically identical to the **Green's function** in differential equations. Both describe the system's response to a point source (impulse):

- **Optics:** Input a point of light $\delta(\bar{x} - \bar{x}_0)$ → output is the PSF $h(\bar{x}; \bar{x}_0)$
- **PDEs:** Apply a point source to a differential equation → output is the Green's function $G(\bar{x}; \bar{x}_0)$

In both cases, the response to an arbitrary input is found by superposition (convolution with the source distribution). This unifies optical imaging theory with the mathematical framework of linear PDEs.
In PDEs, the Green's function $G(\bar{x}; \bar{x}_0)$ is the solution when the source is a [delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/): $L\{G\} = \delta(\bar{x} - \bar{x}_0)$. The [point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/) is the same concept—the system's response to a point source, which lets you build up the response to any input via [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/).

</div>
</div>

Note that the input to the linear system can always be described by a weighted sum of delta functions:



$$
g_1(\bar{x}_1) = \int g_1(\bar{x}_0)\delta(\bar{x}_1 - \bar{x}_0)d\bar{x}_0
$$



This is simply equivalent to treating the input $g_1(\bar{x}_1)$ as an infinite number of samples (delta functions) with varying strengths. By linear [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/), each one of these samples can be passed through the operator separately and added together at the output.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Linear System and Superposition</div>
<div class="callout-content">

![Linear system diagram](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/linear_system.svg)

**Input plane (blue):** Point sources $g_1(\bar{x}_0)\delta(\bar{x}_1 - \bar{x}_0)$ represented as dots. Each point is a [delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) weighted by the input function $g_1(\bar{x}_1)$.

**Linear system $\mathcal{L}$:** The operator that transforms input to output (e.g., an imaging lens).

**Output plane (red):** Each input point produces an **[Airy disk](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/) pattern** — the [point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/) $h(\bar{x}_2; \bar{x}_0)$. The concentric circles represent diffraction rings caused by the finite aperture:
- Central dot = bright central maximum
- Surrounding rings = diffraction fringes (intensity decreasing outward)

**Key insight:** The output image $g_2(\bar{x}_2)$ is formed by summing all individual PSF responses — this is the [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) integral ([convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)). When PSFs overlap, fine details blur together, limiting resolution.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Sifting property of delta functions</div>
<div class="callout-content">

The sifting (or sampling) property of the [delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) states:


$$
\int f(x) \delta(x - x_0) \, dx = f(x_0)
$$


The delta function "sifts out" the value of $f$ at $x_0$. In the integral above, each delta function $\delta(\bar{x}_1 - \bar{x}_0)$ is weighted by $g_1(\bar{x}_0)$, and integrating over all $\bar{x}_0$ reconstructs the original function $g_1(\bar{x}_1)$. This representation lets us treat any input as a continuous sum of impulses, which is the foundation for the [superposition integral](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/).

</div>
</div>

### Superposition Integral

**Input → Output:**



$$
\mathcal{L}\{ g_1(\bar{x}_1) \} = g_2(\bar{x}_2)
$$



Substitute the delta function representation of the input:



$$
g_2(\bar{x}_2) = \mathcal{L}\left\{ \int g_1(\bar{x}_0)\,\delta(\bar{x}_1 - \bar{x}_0)\, d\bar{x}_0 \right\}
$$



By linearity, the operator moves inside the integral, and each delta function produces the PSF:



$$
= \int g_1(\bar{x}_0)\, h(\bar{x}_2; \bar{x}_0)\, d\bar{x}_0
$$



This is the **[Superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) Integral** - the response to a single input point of strength $g_1(\bar{x}_0)$ located at $\bar{x}_0$.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Assume system is shift-invariant</div>
<div class="callout-content">

For $\mathcal{L}\{ g_1(\bar{x}_1) \} = g_2(\bar{x}_2)$, **shift invariance implies**


$$
\mathcal{L}\{ g_1(\bar{x}_1 - \bar{x}_0) \} = g_2(\bar{x}_2 - \bar{x}_0)
$$


In plain terms: if you shift the input, the output shifts by the same amount but otherwise looks identical. The system behaves the same way regardless of where the input is located.

</div>
</div>

>[!note] Apply to point spread function
> 

$$
\Rightarrow \mathcal{L}\{ \delta(\bar{x}_1) \}
= \underbrace{h(\bar{x}_2;\,0)}_{\text{PSF}}
$$


>
> Then, by **shift invariance**,
> 

$$
\mathcal{L}\{ \delta(\bar{x}_1 - \bar{x}_0) \}
= h(\bar{x}_2 - \bar{x}_0;\,0)
= \underbrace{h(\bar{x}_2 - \bar{x}_0)}_{\text{PSF}}
$$


>
> Plugging this back into the superposition integral gives the [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) integral:
>
> 

$$
\underbrace{g_2(\bar{x}_2)}_{\text{output}}
=
\int
\underbrace{g_1(\bar{x}_0)}_{\text{input}}
\;
\underbrace{h(\bar{x}_2 - \bar{x}_0)}_{\text{PSF}}
\;
d\bar{x}_0
$$



In optics we are often interested in a special kind of linear operator called a **[shift-invariant](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) operator** (completely analogous to the time-[invariant](/notes/areas/mathematics/abstract_algebra/definitions/invariant/) operators in electronics).

If an operator is shift-[invariant](/notes/areas/mathematics/abstract_algebra/definitions/invariant/), then:



$$
\mathcal{L}\{g_1(\bar{x}_1)\} = g_2(\bar{x}_2)
$$



**Shift invariance** implies:



$$
\mathcal{L}\{g_1(\bar{x}_1 - \bar{x}_0)\} = g_2(\bar{x}_2 - \bar{x}_0)
$$



In other words, the **behavior of the system is not a function of the independent variable** (spatial position in this case).

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Time-invariance analogy</div>
<div class="callout-content">

Capacitors, resistors, etc. do not age - their behavior doesn't depend on absolute position, only relative position.

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Lens imaging system with finite resolution</div>
<div class="callout-content">

Assume magnification is unity, and ignore inversion.
![Lens imaging system with finite resolution](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/lens_finite_resolution.svg)

Point objects in the object plane (dots 1, 2, 3) are imaged through a lens onto the image plane. Due to **diffraction** and **aberrations**, each point does not map to a perfect point — instead it spreads into an **Airy disk** pattern (concentric rings). This spreading is described by the **point spread function (PSF)** of the system. The finite size of the PSF limits the system's ability to resolve fine details.

</div>
</div>
### Shift-Invariant Systems

Assume $\mathcal{L}\{g_1(x_1, y_1)\} = g_2(x_2, y_2)$, where $g_1(x_1, y_1)$ is the object, $g_2(x_2, y_2)$ is the image, and $\mathcal{L}$ represents the imaging process.

**Shift invariance** implies:



$$
\mathcal{L}\{g_1(x_1 - x_0, y_1 - y_0)\} = g_2(x_2 - x_0, y_2 - y_0)
$$



Physically, if we move the object around, the blurry image (from imperfect imaging) moves around also, but does not change appearance.

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Note</div>
<div class="callout-content">

This is not always true in optical systems. If the center of the image is "better resolved" than the edges (as is usually the case), the system is not shift-invariant.

</div>
</div>

Several imaging effects **are** shift [invariant](/notes/areas/mathematics/abstract_algebra/definitions/invariant/):
- [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/)
- Misfocussing
- Spherical aberration

Some are **not**:
- Coma
- Astigmatism
- Distortion

## Point Spread Function of Linear Shift-Invariant Systems

Consider the [point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/) of a **[linear shift-invariant (LSI)](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** system. If we place a delta function at the origin, we have:



$$
\mathcal{L}\{\delta(\bar{x}_1)\} = h(\bar{x}_2; 0)
$$



But from the definition of shift-invariance, we also have:



$$
\mathcal{L}\{\delta(\bar{x}_1 - \bar{x}_0)\} = h(\bar{x}_2 - \bar{x}_0; 0)
$$



Thus, the entire system can be described by a single **[point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/)** $h(\bar{x}_2)$. The **[superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/)** integral now becomes
### Convolution Integral



$$
g_2(\bar{x}_2) = \int g_1(\bar{x}_0) \, h(\bar{x}_2 - \bar{x}_0) \, d\bar{x}_0
$$



This is the familiar **[convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) integral**. It will become apparent that many optical phenomena (imaging, [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/), etc.) can be described in terms of **[point spread functions](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/)** and **[convolutions](/notes/areas/mathematics/real_analysis/definitions/convolution/)** in two dimensions.



$$
s(x,y) = \iint g(x',y') \, p(x-x', y-y') \, dx' \, dy'
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

Correlation = convolution for symmetric functions

</div>
</div>

## III. Fourier Transforms Applied to Linear Shift-Invariant Systems

In electronics, we know that a temporal [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) is a useful device for studying the behavior of linear circuits. For example, filters are easily described by a [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) $\tilde{H}(f)$, where $f$ is a temporal frequency variable. We shall see that optical propagation is conveniently described by a two-dimensional [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) $\tilde{H}(f_x, f_y)$, where $f_x$ and $f_y$ are **spatial frequencies**.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

$p(x,y)$ acts like a filter with **[impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** $p(x,y)$ and **[transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)** $\mathcal{F}\{p(x,y)\}$.
**[Convolutions](/notes/areas/mathematics/real_analysis/definitions/convolution/)** in one domain = products in the other domain.

</div>
</div>

To understand why the **[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)** is so useful for describing **[linear shift invariant](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** systems, we recall that the **[superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/)** property allows us to:
1. Express the input function as a weighted sum of simple waveforms ([basis](/notes/areas/mathematics/linear_algebra/definitions/basis/) functions)
2. Pass each waveform through the operator separately
3. Sum the result at the end

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Choosing Good Basis Functions</div>
<div class="callout-content">

**Orthogonal:** Basis functions should be mutually orthogonal (zero inner product between different basis functions). This makes finding coefficients easy — the inner product with each basis function extracts only that component's weight, with no crosstalk from other components.

**Complete:** The basis should span the entire function space. Any function in the space must be expressible as a sum of basis functions. Completeness ensures no information is lost in the decomposition.

Complex exponentials $e^{j2\pi\bar{f}\cdot\bar{x}}$ satisfy both: they are orthogonal (different frequencies integrate to zero) and complete (any square-integrable function can be represented).

</div>
</div>

But what do we choose for these simple waveforms? Ideally, we would like to choose a waveform that is unaffected by the linear operator (except to be multiplied by a complex constant). Then, as each waveform is passed through the operator the effect of the operator is particularly easy to calculate.
### Eigenfunctions of Linear Operators

The set of functions which are unaffected by a linear operator (except to be multiplied by a complex constant) are called the **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) of the operator**.



$$
\mathcal{L}\{\psi(\bar{x}; \bar{f}_0)\} = H(\bar{f}_0)\psi(\bar{x}; \bar{f}_0)
$$



This is the **[Eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) Equation**.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Contrast: Delta Function vs Eigenfunction Input</div>
<div class="callout-content">

Two ways to characterize a linear system:

**Delta function input:** A point source $\delta(\bar{x})$ contains all frequencies equally. The system responds with its **impulse response** (point spread function) — a complicated pattern mixing all the system's frequency responses together. Useful for measuring the system, but the output shape bears no resemblance to the input.

**Eigenfunction input:** A complex exponential $e^{j2\pi\bar{f}\cdot\bar{x}}$ is a single pure frequency. The system responds with the *same* exponential, merely scaled by $H(\bar{f})$. The output shape is identical to the input — this is what makes eigenfunctions special.

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Complex Exponentials as Eigenfunctions of [LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) Operators</div>
<div class="callout-content">

*Notation: Bar denotes vectors. $\bar{x} = (x, y)$ is the position vector, $\bar{f} = (f_x, f_y)$ is the spatial frequency vector, and $\bar{f} \cdot \bar{x} = f_x x + f_y y$.*

**Claim:** The complex exponential $\exp[j 2\pi \bar{f}\cdot \bar{x}]$ is an **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** of any **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** operator.

**[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) System ([Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) Form):** Let the **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** operator be defined by **[convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)** with **[impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** $h$:


$$
g_2(\bar{x}) = \int_{\mathbb{R}^n} h(\bar{x}_0)\, g_1(\bar{x}-\bar{x}_0)\, d\bar{x}_0
$$



**Choose a Complex Exponential Input:** Let $g_1(\bar{x}) = \exp[j 2\pi \bar{f}_0 \cdot \bar{x}]$

**Apply the Operator:** Substitute $g_1$ into the convolution:


$$
g_2(\bar{x}) = \int h(\bar{x}_0)\, \exp[j 2\pi \bar{f}_0 \cdot (\bar{x}-\bar{x}_0)] \, d\bar{x}_0 = \int h(\bar{x}_0)\, \exp[j 2\pi \bar{f}_0 \cdot \bar{x}] \exp[-j 2\pi \bar{f}_0 \cdot \bar{x}_0] \, d\bar{x}_0
$$



Factor out the $\bar{x}$-dependent term:


$$
g_2(\bar{x}) = \exp[j 2\pi \bar{f}_0 \cdot \bar{x}] \int h(\bar{x}_0)\, \exp[-j 2\pi \bar{f}_0 \cdot \bar{x}_0] \, d\bar{x}_0
$$



**Eigenfunction Form:** Define $\lambda(\bar{f}_0) = \int h(\bar{x}_0)\, \exp[-j 2\pi \bar{f}_0 \cdot \bar{x}_0] \, d\bar{x}_0$. Then:


$$
g_2(\bar{x}) = \lambda(\bar{f}_0)\, g_1(\bar{x})
$$



**Conclusion:**
- $\exp[j 2\pi \bar{f}_0 \cdot \bar{x}]$ is an **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** of the **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** operator
- $\lambda(\bar{f}_0)$ is the eigenvalue, equal to the Fourier transform of $h$ evaluated at $\bar{f}_0$

**Key Insight:** **[Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)** in space corresponds to multiplication in frequency; Fourier modes diagonalize **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** systems.

</div>
</div>

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>From Single Eigenfunction to Family of Eigenfunctions</div>
<div class="callout-content">

The proof above used a fixed frequency $\bar{f}_0$. Letting $\bar{f}$ vary gives the **family of [eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)**: $\exp[j2\pi \bar{f} \cdot \bar{x}]$ for all $\bar{f}$.

The **[transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)** $H(\bar{f})$ is defined as the **[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)** of the **[impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)**:


$$
H(\bar{f}) = \int h(\bar{x}_0) \exp[-j2\pi \bar{f} \cdot \bar{x}_0] \, d\bar{x}_0
$$



The **general [eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) equation** is:


$$
\mathcal{L}\{\exp[j2\pi \bar{f} \cdot \bar{x}]\} = H(\bar{f}) \exp[j2\pi \bar{f} \cdot \bar{x}]
$$



| Component | Interpretation |
|-----------|----------------|
| $\exp[j2\pi \bar{f} \cdot \bar{x}]$ | Input: a pure sinusoid at frequency $\bar{f}$ |
| $\mathcal{L}\{\cdot\}$ | Any **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** operator (lens, filter, propagation, etc.) |
| $H(\bar{f})$ | **[Eigenvalue](/notes/areas/mathematics/linear_algebra/definitions/eigenvalue/)**: amplitude and phase change at that frequency |
| Output | Same sinusoid, scaled by $H(\bar{f})$ |

**Why this matters:** Any signal can be decomposed into complex exponentials (**[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)**). Each exponential just gets multiplied by $H(\bar{f})$. To analyze what an **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** system does to any input:
1. Decompose input into frequencies (**[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)**)
2. Multiply each frequency component by $H(\bar{f})$
3. Recombine (**inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)**)

</div>
</div>

There are in general an infinite number of **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** associated with an operator. In the above, $\psi(\bar{x}; \bar{f}_0)$ is the $\bar{f}_0$th **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** which is a function of $\bar{x}$. Thus, $\psi(\bar{x}; \bar{f})$ describes a family of **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)**. The **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** $\psi(\bar{x}; \bar{f}_0)$ can pass through the operator unchanged except that it is multiplied by the complex constant $H(\bar{f}_0)$. $H(\bar{f}_0)$ is the **[eigenvalue](/notes/areas/mathematics/linear_algebra/definitions/eigenvalue/)** associated with the $\bar{f}_0$th **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)**.

## Finding Eigenfunctions of Linear Shift-Invariant Operators

We are interested in finding the **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** associated with **[linear shift invariant](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** operators. We shall show that the **complex exponentials** are the **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** we desire. Let



$$
\mathcal{L}\{\exp(j2\pi\bar{f}_0 \cdot \bar{x})\} = g(\bar{x}; \bar{f}_0)
$$



Now consider a shifted version of this
### Complex Exponentials as Eigenfunctions



$$
\mathcal{L}\{\exp(j2\pi\bar{f}_0 \cdot (\bar{x} - \bar{x}_0))\} = \mathcal{L}\{\exp(-j2\pi\bar{f}_0 \cdot \bar{x}_0)\exp(j2\pi\bar{f}_0 \cdot \bar{x})\}
$$




$$
= \exp(-j2\pi\bar{f}_0 \cdot \bar{x}_0) \mathcal{L}\{\exp(j2\pi\bar{f}_0 \cdot \bar{x})\}
$$




$$
= \exp(-j2\pi\bar{f}_0 \cdot \bar{x}_0) g(\bar{x}; \bar{f}_0)
$$



But by shift-invariance:


$$
\mathcal{L}\{\exp(j2\pi \bar{f}_0 \cdot (\bar{x} - \bar{x}_0))\} = g(\bar{x} - \bar{x}_0; \bar{f}_0)
$$



Therefore:


$$
g(\bar{x} - \bar{x}_0; \bar{f}_0) = \exp(-j2\pi\bar{f}_0 \cdot \bar{x}_0) g(\bar{x}; \bar{f}_0)
$$



Now this is only true if $g(\bar{x}; \bar{f}_0)$ is of the form:



$$
g(\bar{x}; \bar{f}_0) = H(\bar{f}_0)\exp(j2\pi\bar{f}_0 \cdot \bar{x})
$$



where $H(\bar{f}_0)$ = complex constant. This is the solution to the equation above.

Thus we conclude:



$$
\mathcal{L}\{\exp(j2\pi\bar{f}_0 \cdot \bar{x})\} = H(\bar{f}_0)\exp(j2\pi\bar{f}_0 \cdot \bar{x})
$$



which satisfies the **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** equation.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

In general, the family of **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** is given by complex exponentials of all frequencies $\bar{f}$. They are orthonormal and complete.
- $|e^{j\theta}| = 1$ for all $\theta$
- Other orthonormal bases exist (Legendre, Laguerre, Hermite polynomials), but complex exponentials are special because they are eigenfunctions of **shift-invariant** operators

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Geometric Interpretation: Why Complex Exponentials are Orthogonal</div>
<div class="callout-content">

**Isolating a Single Frequency Component**

Start from the inverse Fourier representation of a signal:



$$
g(x) = \int G(f)\, e^{j2\pi f x}\, df
$$



To recover the spectrum $G(f')$, multiply both sides by $e^{-j2\pi f' x}$ and integrate over $x$:



$$
\int g(x)\, e^{-j2\pi f' x}\, dx = \int G(f)\left[\int e^{j2\pi (f - f')x}\, dx\right] df
$$



This step sets up an **inner product** between two complex exponentials. Whether this inner product vanishes or survives depends on the frequency difference $f - f'$.

**Phasor (Unit-Circle) Interpretation and Orthogonality**

The exponential $e^{j2\pi (f - f')x}$ can be viewed as a **phasor**: a unit-length vector rotating in the complex plane as $x$ changes.

- **If $f \neq f'$:** The phasor rotates continuously around the unit circle. Integrating over $x$ sums vectors pointing in all directions, producing complete cancellation.

- **If $f = f'$:** The phasor does not rotate and remains fixed at 1 on the real axis. All contributions add in the same direction, yielding an unbounded result.

This behavior is captured mathematically by the [Dirac delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/):



$$
\int e^{j2\pi (f - f')x}\, dx = \delta(f - f')
$$



The phasor diagram provides the **geometric explanation** for the orthogonality of complex exponentials and for the appearance of the delta function.

![Phasor interpretation of Fourier orthogonality](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/phasor_orthogonality.svg)

**Consequence for LSI Systems: Diagonalization in Frequency**

Let $\mathcal{L}$ be a [linear, shift-invariant](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) system and define the output:



$$
g_2(x) = \mathcal{L}\{g_1(x)\}
$$



Represent the input using its inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):



$$
g_1(x) = \int G(f)\, e^{j2\pi f x}\, df
$$



By linearity, the operator passes through the integral:



$$
g_2(x) = \int G(f)\, \mathcal{L}\{e^{j2\pi f x}\}\, df
$$



Shift invariance implies that complex exponentials are [eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/):



$$
\mathcal{L}\{e^{j2\pi f x}\} = H(f)\, e^{j2\pi f x}
$$



Substituting this result gives:



$$
g_2(x) = \int G(f)\, H(f)\, e^{j2\pi f x}\, df
$$



Thus, in the frequency domain:



$$
G_2(f) = G(f)\, H(f)
$$



**Key Result:** [Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) in space corresponds to **multiplication** in frequency. The [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) **diagonalizes** LSI systems — each frequency component is processed independently by multiplying by the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) $H(f)$.

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Scaling Operator and the Mellin Transform</div>
<div class="callout-content">

Just as the Fourier transform arises from analyzing **shift-invariant** systems, the **Mellin transform** arises from analyzing **scale-invariant** systems.

**The Scaling Operator**

The 2D scaling operator $\mathfrak{M}$ transforms a function by rescaling its arguments:



$$
g(x,y) \xrightarrow{\quad \mathfrak{M} \quad} g(ax, by)
$$



where $a$ and $b$ are the magnification factors along the $x$ and $y$ axes respectively.

**Eigenfunctions of the Scaling Operator**

The [eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) of the scaling operator are **complex power functions**:



$$
x^{j2\pi f_x} \cdot y^{j2\pi f_y}
$$



where $f_x$ and $f_y$ are continuous parameters (the "scale-frequencies").

**Proof:** Apply the scaling operator:



$$
\mathfrak{M}\left\{ x^{j2\pi f_x} \cdot y^{j2\pi f_y} \right\} = (ax)^{j2\pi f_x} \cdot (by)^{j2\pi f_y}
$$



Using $(ax)^n = a^n \cdot x^n$:



$$
= \underbrace{a^{j2\pi f_x} \cdot b^{j2\pi f_y}}_{\text{eigenvalue } \lambda(f_x, f_y)} \cdot \underbrace{x^{j2\pi f_x} \cdot y^{j2\pi f_y}}_{\text{original eigenfunction}}
$$



The function returns unchanged in form, multiplied by a constant. $\blacksquare$

**The Mellin Transform Pair**

*Inverse Mellin Transform (Synthesis):*


$$
g(x,y) = \iint G(f_x, f_y) \; x^{j2\pi f_x} \; y^{j2\pi f_y} \; df_x \, df_y
$$



*Forward Mellin Transform (Analysis):*


$$
G(f_x, f_y) = \iint g(x,y) \; x^{-j2\pi f_x - 1} \; y^{-j2\pi f_y - 1} \; dx \, dy
$$



**Comparison: Fourier vs. Mellin**

| Property | Shift-Invariant | Scale-Invariant |
|----------|-----------------|-----------------|
| Operator | $g(x) \to g(x - x_0)$ | $g(x) \to g(ax)$ |
| Eigenfunctions | $e^{j2\pi fx}$ | $x^{j2\pi f}$ |
| Transform | Fourier | Mellin |

![Fourier vs Mellin eigenfunctions](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/fourier_vs_mellin_eigenfunctions.svg)

**Connection to Fourier Transform**

Via logarithmic substitution $x = e^t$:



$$
x^{j2\pi f} = e^{j2\pi f t}
$$



The Mellin transform in $(x, f)$ becomes a [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) in $(\log x, f)$. This is why **log-polar coordinates** are useful for scale and rotation-invariant pattern recognition.

</div>
</div>

## Why Fourier Transform is Useful

It is now clear why the **[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)** is so useful in analyzing a **[linear shift-invariant](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** system. The input function can be decomposed into a [linear combination](/notes/areas/mathematics/linear_algebra/definitions/linear_combination/) of **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** $\exp(j2\pi\bar{f} \cdot \bar{x})$.

The amount of each **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** contained in the input is given by the **Forward [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)**:



$$
\tilde{G}(\bar{f}) = \int g_1(\bar{x})\exp(-j2\pi\bar{f} \cdot \bar{x})d\bar{x}
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Analysis and Synthesis</div>
<div class="callout-content">

**Forward transform (analysis):** To find the amplitude $\tilde{G}(\bar{f})$ of a particular frequency component, multiply the input by that frequency's eigenfunction $e^{-j2\pi\bar{f}\cdot\bar{x}}$ and integrate over all space. The integral extracts how much of that frequency is present — all other frequencies integrate to zero (orthogonality).

**Inverse transform (synthesis):** To reconstruct $g(\bar{x})$ from its spectrum, sum all eigenfunctions weighted by their amplitudes $\tilde{G}(\bar{f})$. This is done by the inverse Fourier transform.

</div>
</div>

Each weighted **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** is run through the **[linear shift invariant](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** system. The effect of the system is to multiply each of the **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** by a complex number $H(\bar{f})$, where H takes on different values for each different **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)**. The function $H(\bar{f})$ is called the **[transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)** of the linear system.

After passing through the operator a single **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** waveform becomes
### Individual Eigenfunction Response



$$
\tilde{G}(\bar{f}_0) \cdot H(\bar{f}_0)\exp(j2\pi\bar{f}_0 \cdot \bar{x})
$$



To calculate the output of the linear system we simply pass all weighted **[eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** through the operator and add up the result:



$$
g_2(\bar{x}) = \int \tilde{G}(\bar{f}) \cdot H(\bar{f})\exp(j2\pi\bar{f} \cdot \bar{x})d\bar{f}
$$



This is the **Inverse [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)** (sum of results).

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Biological Fourier Analysis: The Cochlea</div>
<div class="callout-content">

The cochlea (inner ear) performs a physical Fourier transform on incoming sound. The basilar membrane varies in stiffness along its length:
- **Base (stiff):** Resonates at high frequencies
- **Apex (flexible):** Resonates at low frequencies

Each position along the membrane responds maximally to a specific frequency, mapping frequency → position. Hair cells at each location detect the local vibration amplitude, effectively measuring $|G(f)|$ at that frequency. The brain receives a spatially-encoded frequency spectrum — a biological spectrum analyzer.

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Frequency Decomposition Through an **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** System</div>
<div class="callout-content">

![Frequency decomposition through LSI system](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/lsi_frequency_decomposition.svg)

The input signal $g_1(x)$ is decomposed via [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) into frequency components. Each component passes through the system independently — the [LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) operator multiplies each by the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) $H(f)$ at that frequency:



$$
G_1(f)e^{j2\pi f x} \xrightarrow{\mathcal{L}} G_1(f)H(f)e^{j2\pi f x}
$$



The output is the inverse Fourier transform (recombination) of all modified components:



$$
g_2(\bar{x}) = \int \underbrace{G_1(\bar{f}) H(\bar{f})}_{G_2(\bar{f})} \exp[j 2\pi \bar{f}\cdot\bar{x}] \, d\bar{f}
$$



**Key insights:**
- Each spatial frequency passes through independently
- Frequencies are not mixed by the **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** system
- Each component is multiplied by $H(f)$ (the **[transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)**)
- Complex exponentials are [eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) — they pass through unchanged in form, just scaled

</div>
</div>

## IV. Properties of the Spatial Fourier Transform

### A. Spatial Frequency

The spatial [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) is similar to the more familiar temporal transform in many respects. Mathematically, the only difference is that it is two-dimensional as opposed to its one-dimensional temporal counterpart. However, there are several conceptual differences which are worth exploring.

The concept of frequency is well understood for temporal signals. If a voltage has a temporal behavior expressed by:



$$
V(t) = A\sin(2\pi f_0 t)
$$



we know that this corresponds to a sinusoid which repeats itself every $\frac{1}{f_0}$ seconds. The frequency has units of inverse seconds.

Equivalently, a spatial description of a particular image might be expressed as:



$$
A(x,y) = \sin(2\pi f_x x) \cdot \sin(2\pi f_y y)
$$



This corresponds to a two-dimensional distribution which repeats itself every $\frac{1}{f_x}$ cm in the x direction and $\frac{1}{f_y}$ cm in the y direction. The spatial frequency has components in two directions, and units of **inverse centimeters**.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Why Complex Exponentials for the Fourier Transform?</div>
<div class="callout-content">

The expression $\sin(2\pi f_x x) \cdot \sin(2\pi f_y y)$ above creates a **grid pattern** — a checkerboard of peaks and valleys aligned with the $x$ and $y$ axes.

But a true 2D spatial frequency component should be a **tilted plane wave**:



$$
\sin(2\pi(f_x x + f_y y))
$$



representing wavefronts tilted at an angle determined by the ratio $f_y/f_x$.

![Grid pattern vs tilted plane wave](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/grid_vs_plane_wave.svg)

**The Problem with Sines:**



$$
\sin(2\pi f_x x) \cdot \sin(2\pi f_y y) \neq \sin(2\pi(f_x x + f_y y))
$$



Products of sines do **not** give tilted plane waves. The sine function lacks the algebraic property needed for separability.

**The Solution — Complex Exponentials:**

Complex exponentials satisfy $e^{a+b} = e^a \cdot e^b$, therefore:



$$
\exp\left[j2\pi(f_x x + f_y y)\right] = \exp\left[j2\pi f_x x\right] \cdot \exp\left[j2\pi f_y y\right]
$$



- The **left side** is a tilted plane wave with 2D spatial frequency $(f_x, f_y)$
- The **right side** is a separable product of 1D functions
- Both are **equal** — unlike the sine case

| | Sines/Cosines | Complex Exponentials |
|--|---------------|---------------------|
| **Separability** | $\sin(a)\sin(b) \neq \sin(a+b)$ | $e^a \cdot e^b = e^{a+b}$ |
| **2D product gives** | Grid pattern | Tilted plane wave |

Complex exponentials are the natural basis for [Fourier analysis](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) because they are [eigenfunctions](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) of the shift operator **and** satisfy the separability property needed for multi-dimensional analysis.

</div>
</div>

### Relationship Between Angular Plane Waves and Fourier Transform

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Preview</div>
<div class="callout-content">

This section introduces the connection between spatial frequencies and plane wave angles. For a complete worked example with propagation through an aperture, see [Complete Example: Tilted Plane Wave Through Circular Aperture](#complete-example-tilted-plane-wave-through-circular-aperture).

</div>
</div>

A solution to the Helmholtz equation for wave propagation is given by a **[plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/)**:



$$
A \exp(j\phi)\exp(j\vec{k} \cdot \vec{r})
$$



where $A$ and $\phi$ are the amplitude and phase of the [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/). In rectangular coordinates this becomes:



$$
u(x,y,z) = A \exp(j\phi)\exp(jk_z \cdot z)\exp(j(k_x \cdot x + k_y \cdot y))
$$



Now consider the field in a particular z plane $z = z_0$:



$$
u(x,y)_{z=z_0} = A \exp(j(\phi + k_z \cdot z_0))\exp(j(k_x \cdot x + k_y \cdot y))
$$



Notice that the field is described by a **complex exponential**. When one moves along the x-axis (or y-axis), the phase of this complex exponential changes. The rate at which it changes (frequency) is given by:



$$
k_x = k\cos\theta
$$



Thus a complex spatial frequency component is physically equivalent to a [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/), where the frequency of the component is proportional to the cosine of the propagation angle of the [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/).



$$
\exp(j2\pi f_x x)
$$





$$
f_x = \frac{\cos\theta}{\lambda} = \text{spatial freq.}
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Spatial Frequency vs Radian Frequency</div>
<div class="callout-content">

- Radian frequency: $k_x = k\cos\theta = \frac{2\pi}{\lambda}\cos\theta$
- Spatial frequency (cycles/cm): $f_x = \frac{\cos\theta}{\lambda}$
- Relation: $k_x = 2\pi f_x$

</div>
</div>

Negative and positive frequencies correspond to plane waves travelling in opposite directions (e.g., upward vs downward tilted). The spatial [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of an arbitrary two-dimensional field can be thought of as a **linear [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) of plane waves**, where:
- The **angle** of the [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) corresponds to the spatial frequency
- The **amplitude and phase** of the [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) corresponds to the complex Fourier component associated with that spatial frequency

![Plane Wave Geometry: Angle to Spatial Frequency](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/plane_wave_geometry.svg)

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Understanding the Diagram</div>
<div class="callout-content">

The diagram shows a plane wave with wavevector $\mathbf{k}$ tilted at angle $\theta$ from the x-axis. The dashed blue lines are **wavefronts** (surfaces of constant phase), perpendicular to $\mathbf{k}$.

As you move along the x-axis at observation plane $z_0$, you cross successive wavefronts. The spacing between crossings is the **apparent wavelength** $\lambda_x = \lambda / \cos\theta$, which is always larger than $\lambda$ (wavefronts appear "stretched" when viewed obliquely).

The **spatial frequency** $f_x = \cos\theta / \lambda$ is just the reciprocal — how many cycles per unit length you see along x. A steeper tilt (larger $\theta$) means fewer crossings per unit length, hence lower spatial frequency.

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Sanity Check: Limiting Cases</div>
<div class="callout-content">

Verify that $f_x = \frac{\cos\theta}{\lambda}$ behaves correctly at extreme angles:

**Case 1: $\theta = \pi/2$ (90°)**
- Wave propagates purely along $z$
- Wavefronts are vertical — no variation in $x$
- $f_x = \frac{\cos(\pi/2)}{\lambda} = 0$ ✓

**Case 2: $\theta = 0$**
- Wave propagates along $x$
- Phase changes rapidly in $x$ — maximum $x$-variation
- $f_x = \frac{\cos(0)}{\lambda} = \frac{1}{\lambda}$ (maximum spatial frequency) ✓

**Takeaway:** The spatial frequency along $x$ is the projection of the wavevector onto the $x$-axis.

</div>
</div>

![Sanity Check: Limiting Cases](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/sanity_check_limiting_cases.svg)

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Reading the Diagram</div>
<div class="callout-content">

**Left (θ = 90°):** The wavevector $\mathbf{k}$ points along $z$, so wavefronts are vertical lines. Moving along the x-axis, you stay on the same wavefront — no phase variation, hence $f_x = 0$.

**Right (θ = 0°):** The wavevector $\mathbf{k}$ points along $x$, so wavefronts are horizontal. Moving along x, you cross every wavefront at maximum rate — one cycle per wavelength, hence $f_x = 1/\lambda$.

</div>
</div>

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Convolution Theorem Reminder</div>
<div class="callout-content">

For LSI systems, convolution in space becomes multiplication in frequency:


$$
\tilde{G}_2(\bar{f}) = \tilde{G}_1(\bar{f}) \cdot \tilde{H}(\bar{f})
$$


where $\tilde{H}(\bar{f}) = \mathcal{F}\{h(\bar{x})\}$ is the transfer function.

</div>
</div>

## Causality (Spatial vs Temporal)

In time series analysis, **causality** states that the value of the output at time $t_0$ does not depend on future values of the input $t > t_0$. This relationship requires all **[impulse responses](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** to be nonsymmetric, and thus the **[transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)** must be complex.

When time is the independent variable, causality is required since "future" cannot affect "present", but "past" can.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

For real **[transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)**, **[impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** must be Hermitian.

</div>
</div>

| $g(x)$ | $\tilde{G}(f_x)$ |
|--------|------------------|
| Real | Hermitian |
| Hermitian | Real |
| Real/Even | Real/Even |
| Complex/Even | Complex/Even |
| Complex/Odd | Complex/Odd |

When a linear system is analyzed as a function of spatial variables, **causality no longer is required**. Values to the "right" of a point can effect the value of the point just as easily as values to the "left". The [point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/) can then be symmetric, and **real transfer functions are possible**.
## Two-Dimensionality and Separability

The most obvious difference between a temporal and spatial [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) is the two-dimensional aspect of the latter. If we write the forward [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) as:



$$
\tilde{U}(f_x, f_y) = \iint_{-\infty}^{\infty} u(x,y)\exp(-j2\pi(f_x \cdot x + f_y \cdot y))dxdy
$$



and if $u(x,y) = u_1(x) \cdot u_2(y)$, then we can express the transform as the product of two one-dimensional transforms:



$$
\tilde{U}(f_x, f_y) = \iint u_1(x) \cdot u_2(y)\exp(-j2\pi(f_x \cdot x + f_y \cdot y))dxdy
$$




$$
= \int u_1(x)\exp(-j2\pi(f_x \cdot x))dx \cdot \int u_2(y)\exp(-j2\pi(f_y \cdot y))dy
$$




$$
= \tilde{U}(f_x) \cdot \tilde{U}(f_y)
$$



## Circular Symmetry and Polar Coordinates

Many problems in optics involve fields with **circular symmetry**. For these problems, it is useful to express the two-dimensional [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) in polar coordinates. Consider a function with circular symmetry $u(\sqrt{x^2 + y^2})$.

The two-dimensional [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of u is given by:



$$
\tilde{V}(f_x, f_y) = \iint_{-\infty}^{\infty} u(\sqrt{x^2 + y^2})\exp(-j2\pi(f_x \cdot x + f_y \cdot y))dxdy
$$



Let $r, \theta$ be radial and angular variables in real space such that:


$$
x = r\cos\theta, \quad y = r\sin\theta
$$



Let $\rho, \phi$ be radial and angular variables in Fourier space such that:


$$
f_x = \rho\cos\phi, \quad f_y = \rho\sin\phi
$$



The [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) then becomes:



$$
\tilde{V}(\rho\cos\phi, \rho\sin\phi) = \int_0^{\infty} \int_0^{2\pi} u(r')\exp(-j2\pi(r'\cos\theta' \cdot \rho\cos\phi + r'\sin\theta' \cdot \rho\sin\phi))r'dr'd\theta'
$$


### Derivation of Hankel Transform

Since:


$$
\cos\theta'\cos\phi + \sin\theta'\sin\phi = \cos(\theta' - \phi)
$$





$$
\tilde{V}(\rho\cos\phi, \rho\sin\phi) = \int_0^{\infty} \int_0^{2\pi} u(r')\exp(-j2\pi\rho r'\cos(\theta' - \phi))r'dr'd\theta'
$$



Using the [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/) identity:


$$
\int_0^{2\pi} \exp(-ja\cos(\theta' - \phi))d\theta' = 2\pi J_0(a)
$$



we have:



$$
\tilde{V}(\rho\cos\phi, \rho\sin\phi) = 2\pi \int_0^{\infty} u(r')J_0(2\pi\rho r')r'dr'
$$



where $J_0()$ is the **zero-order [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/)**. Notice that the right-hand side of the equation is only a function of $\rho$. Hence we can define a new one-dimensional function:



$$
\tilde{U}(\rho) = \tilde{V}(\rho\cos\phi, \rho\sin\phi)
$$



such that:



$$
\tilde{U}(\rho) = 2\pi \int_0^{\infty} u(r')J_0(2\pi\rho r')r'dr'
$$



This is called the **zero order [Hankel transform](/notes/areas/electrical_engineering/physical_optics/definitions/hankel_transform/)**, or sometimes the **Fourier-Bessel transform**.

## V. Sampling Theorem

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Good practice in Fourier transforms</div>
<div class="callout-content">

It is often useful to represent a light field by an array of samples taken on a discrete set of points. The sampling theorem can be used to specify the sampling rate, as well as prescribe a recipe for recovering the original continuous function.

</div>
</div>

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Sampling Theorem</div>
<div class="callout-content">

If a signal is **band-limited**, and it is sampled at a rate greater than or equal to **twice the bandlimit**, then the original continuous signal can be obtained from the sampled signal exactly.

</div>
</div>

![Sampling Theorem](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/sampling_theorem.svg)

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Reading the Diagram</div>
<div class="callout-content">

**Top row (Real Space):** Sampling is multiplication of the continuous signal $g(x)$ by a comb function (a train of delta functions spaced by $a$). The result $g_s(x)$ is a series of impulses whose heights equal the signal values at sample points.

**Bottom row (Fourier Space):** Multiplication in real space becomes [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) in Fourier space. Convolving the band-limited spectrum $\tilde{G}(f)$ with a comb creates **spectral replicas** centered at multiples of $1/a$.

**Right panel (Nyquist Criterion):** If replicas are spaced far enough apart ($1/a \geq 2B$), they don't overlap and the original spectrum can be recovered with a low-pass filter. If they overlap (**aliasing**), high frequencies masquerade as low frequencies and perfect recovery is impossible.

</div>
</div>

### Sampling Theorem Proof

A function $g(x,y)$ is **band-limited** if its [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) $\tilde{G}(f_x, f_y)$ has compact support, i.e.:



$$
\tilde{G}(f_x, f_y) = 0 \text{ for } |f_x| > B_x \text{ and } |f_y| > B_y
$$



where $B_x$ and $B_y$ are the bandlimits.

## Proof of Sampling Theorem

Define a **[sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) function** (the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/)):



$$
\text{comb}(x) = \sum_{n=-\infty}^{\infty} \delta(x - n)
$$



Assume a function $g(x,y)$ is bandlimited so that:



$$
\tilde{G}(f_x, f_y) = 0 \text{ for } |f_x| > B_x, |f_y| > B_y
$$



Form a sampled version of $f(x,y)$ by multiplying with a [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) function:



$$
g_s(x,y) = g(x,y) \cdot \frac{\text{comb}(x/a)}{a} \cdot \frac{\text{comb}(y/b)}{b}
$$



We can show that:


$$
\mathcal{F}\{\text{comb}(x)\} = \text{comb}(f_x)
$$



where $\mathcal{F}$ is the Forward [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/).

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Why Sampling Creates Spectral Replicas</div>
<div class="callout-content">

**The key insight:** Sampling is multiplication by a comb. By the convolution theorem:


$$
\mathcal{F}\{g(x) \cdot \text{comb}(x)\} = \mathcal{F}\{g(x)\} * \mathcal{F}\{\text{comb}(x)\} = G(f) * \text{comb}(f)
$$



Convolving any function with a comb produces periodic copies of that function centered at each delta spike. This is why the spectrum of a sampled signal consists of the original spectrum repeated at intervals of $1/a$ (the sampling frequency).

**Grating analogy:** A diffraction grating is a periodic structure (like a comb in transmission). It produces discrete diffraction orders — the same mathematics explains both phenomena.

</div>
</div>

Hence:



$$
\mathcal{F}\{g_s(x,y)\} = \tilde{G}_s(f_x, f_y) = \tilde{G}(f_x, f_y) ** \left(\frac{a \cdot \text{comb}(af_x)}{a} \cdot \frac{b \cdot \text{comb}(bf_y)}{b}\right)
$$



where $**$ is a two-dimensional [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/).

The result shows:
- Continuous spectrum $\tilde{G}(f_x)$ gets replicated at intervals of $\frac{1}{a}$
- Sampled spectrum shows **folding** at the **folding frequency** $B_x$
- The **Nyquist frequency** is $\frac{1}{a}$ (the [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) rate)

### Nyquist Criterion

It is clear from the figure that the aliases will not overlap if:



$$
\frac{1}{a} \geq 2B_x, \text{ or } a \leq \frac{1}{2B_x}
$$



and



$$
\frac{1}{b} \leq 2B_y, \text{ or } b \leq \frac{1}{2B_y}
$$



This is the **[Nyquist Criterion](/notes/areas/electrical_engineering/physical_optics/definitions/nyquist_criterion/)**.

In real space, the [Nyquist criterion](/notes/areas/electrical_engineering/physical_optics/definitions/nyquist_criterion/) says that the **highest frequency component** in the x direction (frequency $B_x$), must be **sampled at least twice**.

## Recovery via Low-Pass Filtering

If we satisfy the [Nyquist criterion](/notes/areas/electrical_engineering/physical_optics/definitions/nyquist_criterion/), it is a simple matter to recover the original function $g(x,y)$ by low pass filtering the sampled result $g_s(x,y)$.



$$
\tilde{G}_s(f_x, f_y) \cdot \text{rect}\left(\frac{f_x}{2B_x}\right)\text{rect}\left(\frac{f_y}{2B_y}\right) = \tilde{G}(f_x, f_y)
$$



In real space, this equation becomes:



$$
g(x,y) = g_s(x,y) ** [4B_x B_y \, \text{sinc}(2B_x x) \, \text{sinc}(2B_y y)]
$$



where $\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}$ and $\text{rect}(x) = \begin{cases} 1, & |x| \leq \frac{1}{2} \\ 0, & \text{otherwise} \end{cases}$

Note: $\text{rect}(x/a)$ is a rectangle of width $a$ centered at the origin.

This is a statement of the **[Whittaker-Shannon Sampling Theorem](/notes/areas/electrical_engineering/signals_systems/definitions/whittaker-shannon_sampling_theorem/)**.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Why Sinc is the Perfect Interpolator</div>
<div class="callout-content">

The sinc function has a special property: $\text{sinc}(n) = 0$ for all nonzero integers $n$, but $\text{sinc}(0) = 1$.

When samples are spaced at the Nyquist interval $\Delta x = \frac{1}{2B_x}$, each sinc kernel centered on a sample point:
- Equals **1** at that sample location
- Equals **0** at all other sample locations

This means each sample contributes its value only at its own position, with no interference from neighboring samples. Between samples, the sincs overlap and sum to produce the smooth interpolated curve. This is the unique interpolation that perfectly reconstructs a bandlimited signal.

</div>
</div>

### Aliasing

What happens when the [Nyquist criterion](/notes/areas/electrical_engineering/physical_optics/definitions/nyquist_criterion/) is violated? **Aliasing** results, where high frequencies fold over and look like lower ones.

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Aliasing</div>
<div class="callout-content">

When a signal contains frequencies above the Nyquist limit ($f > f_s/2$), those frequencies don't simply disappear — they **fold back** into the sampled spectrum, masquerading as lower frequencies. This is aliasing.

**Common examples:**
- **Pinstripe suits on TV:** The fine stripes have spatial frequencies exceeding the camera sensor's sampling rate. The result is moiré patterns — false low-frequency waves that shimmer and shift as the person moves.
- **Wagon wheel effect:** In film (24 fps), a wheel spinning faster than 12 rotations/second appears to rotate backwards — high temporal frequency aliased to a negative low frequency.
- **Digital images of fine textures:** Brick walls, fabric weaves, or screen doors photographed with insufficient resolution show false patterns not present in the original scene.

Aliasing is irreversible — once frequencies are folded together, they cannot be separated. The only prevention is to **bandlimit the signal before sampling** (anti-aliasing filter).

</div>
</div>

Notice the important additional results which can be seen from the above proof of the [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) theorem:

- **[Sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) in real space** produces a repeated continuous function in Fourier space
- **[Sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) in Fourier space** produces a repeated continuous function in real space

## VI. Common Transform Pairs

| Function | Transform |
|----------|-----------|
| $\text{rect}(x)\text{rect}(y)$ | $\text{sinc}(x)\text{sinc}(y)$ |
| $\delta(x,y)$ | $1$ |
| $\delta(x \pm x_0, y \pm y_0)$ | $\exp[\pm j2\pi(x_0 f_x + y_0 f_y)]$ |
| $\text{comb}(x)\text{comb}(y)$ | $\text{comb}(f_x)\text{comb}(f_y)$ |
| $\text{circ}(r) = \begin{cases} 1, & r < 1 \\ 0, & \text{else} \end{cases}$ | $\frac{J_1(2\pi\rho)}{\rho}$ |

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Reference: Gaskill's Tables</div>
<div class="callout-content">

*Linear Systems, Fourier Transforms, and Optics* by Jack D. Gaskill contains comprehensive tables of:
- Fourier transform pairs (1D and 2D)
- Transform theorems and properties
- Special functions used in optics (rect, sinc, circ, comb, etc.)

These tables are invaluable for quickly looking up transforms without rederiving them.

</div>
</div>
### Aliasing in Practice

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Aliasing is Irreversible</div>
<div class="callout-content">

If a signal is not bandlimited (low-pass filtered) before sampling, aliased frequencies **cannot** be separated from the original spectrum afterward.

**Why:** Aliasing folds high frequencies on top of low frequencies. Once mixed, they occupy the same frequency bins. Without prior knowledge of the original spectrum, there is no way to determine which components are "real" and which are aliases.

**Prevention:** Always apply an anti-aliasing (low-pass) filter before sampling to remove frequencies above $f_s/2$.

</div>
</div>

## Anti-Aliasing Filter Chain

The standard signal processing chain to avoid aliasing:

```
Continuous   →   Low-Pass    →   Sampler   →   Digital
  Image          Filter           (CCD)        Signal
              (anti-alias)
```

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Why This Order Matters</div>
<div class="callout-content">

The low-pass filter **must come before sampling**. Once high frequencies alias into the baseband, they're indistinguishable from the original signal — no amount of post-processing can undo aliasing.

The filter must restrict bandwidth to less than $\frac{1}{2}$ the sampling frequency (Nyquist limit). If the sampling rate is $f_s$, frequencies above $f_s/2$ will fold back.

</div>
</div>

In optical systems, several mechanisms naturally provide anti-aliasing:

| Mechanism | How it works |
|-----------|--------------|
| **Optical blur (PSF)** | Finite aperture limits resolution, attenuating high frequencies |
| **Detector integration** | Each pixel averages over its area, acting as a spatial low-pass filter |
| **Intentional defocus** | Spreading the PSF further reduces bandwidth |

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Optical Systems as Low-Pass Filters</div>
<div class="callout-content">

The imaging optics themselves act as a low-pass filter — the [optical transfer function](/notes/areas/electrical_engineering/physical_optics/definitions/optical_transfer_function/) cuts off at $1/\lambda F$ for a diffraction-limited system. This is why well-designed cameras often don't need separate anti-aliasing filters: the optics already band-limit the image.

</div>
</div>

## Aliasing of Noise

Even if the signal satisfies Nyquist, broadband noise may not:

| Component | Spectrum | After [Sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) |
|-----------|----------|----------------|
| **Signal** | Band-limited (within Nyquist) | Clean replicated copies |
| **Noise** | Broadband (extends beyond Nyquist) | Aliases fold into signal band |

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Noise Aliasing Increases Noise Power</div>
<div class="callout-content">

High-frequency noise that would normally be outside the signal band folds back and adds to the in-band noise. This **degrades the signal-to-noise ratio**.

**Solution:** Low-pass filter the signal+noise together *before* sampling. This eliminates out-of-band noise before it can alias, improving SNR even though it slightly blurs the signal.

</div>
</div>
---

## VII. Fourier Transform Reference

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Reference Material</div>
<div class="callout-content">

The following sections contain key theorems, special functions, and properties used throughout physical optics.

</div>
</div>

### Fourier Theorems

#### 1. Linearity



$$
\mathcal{F}\{a \cdot g(x,y) + b \cdot h(x,y)\} = a \cdot \mathcal{F}\{g(x,y)\} + b \cdot \mathcal{F}\{h(x,y)\}
$$



#### 2. Similarity Theorem (Scaling Theorem)

If $\mathcal{F}\{g(x,y)\} = G(f_x, f_y)$

then $\mathcal{F}\{g(ax, by)\} = \frac{1}{|ab|} G\left(\frac{f_x}{a}, \frac{f_y}{b}\right)$

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Lens Aperture and Focus Spot</div>
<div class="callout-content">

The focal spot of a lens is the Fourier transform of its aperture (in the Fraunhofer limit). The similarity theorem directly predicts:

- **Larger aperture** (scale up by $a > 1$) → spectrum scales down by $1/a$ → **smaller, tighter focus**
- **Smaller aperture** → **larger, more spread-out focus**

This is why telescope mirrors and camera lenses are made as large as practical — a bigger aperture means sharper resolution. The diffraction limit $\theta \approx \lambda/D$ is just this scaling relationship.

</div>
</div>

#### 3. Shift Theorem

If $\mathcal{F}\{g(x,y)\} = G(f_x, f_y)$

then $\mathcal{F}\{g(x-a, y-b)\} = G(f_x, f_y) \exp[-j2\pi(f_x a + f_y b)]$

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>What This Means</div>
<div class="callout-content">

Shifting a function in space doesn't change the magnitude of its spectrum — only the phase. The shift $(a, b)$ adds a linear phase ramp $\exp[-j2\pi(f_x a + f_y b)]$ across the frequency domain.

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Prism as a Frequency Shifter</div>
<div class="callout-content">

A uniform field $E(x) = 1$ has a spectrum that's a delta at the origin (zero frequency — no spatial variation).

A prism tilts the wavefront, multiplying by $\exp\left[-j\frac{2\pi}{\lambda}x\sin\theta\right]$. By the **dual** of the shift theorem (multiplication by exponential ↔ shift in frequency), this moves the delta to a new location in frequency space.

The prism doesn't change the amplitude distribution — it shifts the angular spectrum, steering the beam.

</div>
</div>

#### 4. [Parseval's Theorem](/notes/areas/mathematics/functional_analysis/definitions/parseval_theorem/)

If $\mathcal{F}\{g(x,y)\} = G(f_x, f_y)$

Then:



$$
\iint_{-\infty}^{\infty} |g(x,y)|^2 \, dxdy = \iint_{-\infty}^{\infty} |G(f_x, f_y)|^2 \, df_x df_y
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Why This Matters</div>
<div class="callout-content">

The total energy (integrated intensity) is the same whether computed in the spatial domain or the frequency domain. This has practical consequences:

- **Power conservation:** Light passing through a lossless optical system conserves total power. Parseval's theorem ensures our Fourier-based models respect this.
- **Spectral analysis:** To find how much power is in a given spatial frequency band, integrate $|G(f_x, f_y)|^2$ over that band — no need to transform back to real space.
- **Unitarity:** The Fourier transform (with proper normalization) is a unitary operator, meaning it preserves inner products and norms. This is why frequency-domain and spatial-domain descriptions are equally valid.

</div>
</div>

#### 5. [Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) Theorem

If $\mathcal{F}\{g(x,y)\} = G(f_x, f_y)$ and $\mathcal{F}\{h(x,y)\} = H(f_x, f_y)$

then:



$$
\mathcal{F}\{g * h\} = G \cdot H
$$



or equivalently:



$$
\mathcal{F}\left\{\iint_{-\infty}^{\infty} g(\xi,\eta)h(x-\xi, y-\eta) \, d\xi d\eta\right\} = G(f_x, f_y) H(f_x, f_y)
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Why This Matters</div>
<div class="callout-content">

Convolution in real space becomes multiplication in frequency space (and vice versa). This is arguably the most important theorem in Fourier optics:

- **Imaging:** The output image is the input convolved with the [PSF](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/). In frequency space, this is just multiplication by the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/).
- **Diffraction:** The far-field pattern is the Fourier transform of the aperture. Multiplying apertures (masking) becomes convolution in the far field.
- **Computation:** Convolution is $O(N^2)$ directly, but FFT → multiply → IFFT is $O(N \log N)$.

</div>
</div>

#### 6. Autocorrelation Theorem

If $\mathcal{F}\{g(x,y)\} = G(f_x, f_y)$, then:



$$
\mathcal{F}\{g \star g^*\} = |G(f_x, f_y)|^2
$$



where $\star$ denotes correlation ([convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) with the conjugate-reversed function):



$$
\mathcal{F}\left\{\iint_{-\infty}^{\infty} g(\xi,\eta) g^*(\xi-x, \eta-y) \, d\xi d\eta\right\} = |G(f_x, f_y)|^2
$$



The dual relation (Wiener-Khinchin):



$$
\mathcal{F}\{|g(x,y)|^2\} = G \star G^* = \iint G(\xi,\eta) G^*(\xi-f_x, \eta-f_y) \, d\xi d\eta
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>What Autocorrelation Measures</div>
<div class="callout-content">

The **autocorrelation** measures how similar a function is to a shifted version of itself. It peaks at zero shift (perfect overlap) and decays as the shift increases.

- **First equation:** The Fourier transform of the autocorrelation is the **power spectrum** $|G|^2$. This is the Wiener-Khinchin theorem — fundamental to spectral analysis and coherence theory.
- **Second equation:** The Fourier transform of the intensity $|g|^2$ is the autocorrelation of the spectrum.

In optics, autocorrelation appears in:
- Coherence measurements (temporal and spatial)
- Speckle statistics
- Optical transfer function (OTF) as autocorrelation of the pupil function

</div>
</div>

#### 7. Fourier Integral Theorem



$$
\mathcal{F}\mathcal{F}^{-1}\{g(x,y)\} = \mathcal{F}^{-1}\mathcal{F}\{g(x,y)\} = g(x,y)
$$



for all points of $g(x,y)$ that are continuous.

### Special Functions

#### Rectangle Function (rect)



$$
\text{rect}(x) = \begin{cases} 1, & |x| \leq \frac{1}{2} \\ 0, & \text{else} \end{cases}
$$



**Shape:** A flat-topped pulse of width 1 centered at the origin.

**[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):** $\mathcal{F}\{\text{rect}(x)\} = \text{sinc}(f_x)$

**In optics:** Models slit apertures, uniform illumination, and ideal bandpass filters.

#### Sinc Function



$$
\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}
$$



**Shape:** An oscillating function that decays as $1/x$, with zeros at all nonzero integers. The central lobe has width 2; sidelobes alternate in sign.

**[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):** $\mathcal{F}\{\text{sinc}(x)\} = \text{rect}(f_x)$

**In optics:** The [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern of a slit; the ideal interpolation kernel for bandlimited signals (Shannon reconstruction).

#### Triangle Function (Λ)



$$
\Lambda(x) = \begin{cases} 1 - |x|, & |x| \leq 1 \\ 0, & \text{else} \end{cases}
$$



**Shape:** A symmetric triangle (tent) of width 2 and height 1.

**[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):** $\mathcal{F}\{\Lambda(x)\} = \text{sinc}^2(f_x)$

**In optics:** The autocorrelation of a rect (two rects convolved); appears in [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) theory and the MTF of defocused systems.

#### [Comb Function](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) (Shah)



$$
\text{comb}(x) = \sum_{n=-\infty}^{\infty} \delta(x - n)
$$



**Shape:** An infinite train of equally-spaced [delta functions](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) at integer positions.

**[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):** $\mathcal{F}\{\text{comb}(x)\} = \text{comb}(f_x)$ — the comb is its own [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/).

**In optics:** Represents [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) (multiplying by comb samples a function); [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) gratings; the reason sampled spectra are periodic.

#### Circle Function (circ)



$$
\text{circ}(r) = \text{circ}\left(\sqrt{x^2 + y^2}\right) = \begin{cases} 1, & r \leq 1 \\ 0, & \text{else} \end{cases}
$$



**Shape:** A uniform disk of radius 1 in 2D.

**[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):** $\mathcal{F}\{\text{circ}(r)\} = \dfrac{J_1(2\pi\rho)}{\rho}$ (the Airy pattern / jinc function)

**In optics:** Models circular apertures and lenses. Its transform is the [Airy disk](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/) — the fundamental [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) limit for circular pupils.

---

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Fourier-Bessel Transform of circ(r)</div>
<div class="callout-content">



$$
\mathcal{B}\{\text{circ}(r)\} = 2\pi \int_0^1 r \, J_0(2\pi r \rho) \, dr
$$



**Goal:** Get the argument of $J_0$ to just be the variable we're integrating over.

**Change of variables (u-substitution):**
1. Pick substitution: Let $u = 2\pi\rho r$ (the thing inside $J_0$)
2. Solve for the old variable: $r = \dfrac{u}{2\pi\rho}$
3. Find $dr$: Differentiate both sides: $dr = \dfrac{du}{2\pi\rho}$
4. Convert limits:
   - When $r = 0$: $u = 2\pi\rho(0) = 0$
   - When $r = 1$: $u = 2\pi\rho(1) = 2\pi\rho$
5. Substitute everything:


$$
\int_0^{2\pi\rho} \underbrace{\frac{u}{2\pi\rho}}_{r} \cdot J_0(\underbrace{u}_{2\pi r\rho}) \cdot \underbrace{\frac{du}{2\pi\rho}}_{dr}
$$


6. Simplify:


$$
= \frac{1}{(2\pi\rho)^2} \int_0^{2\pi\rho} u \cdot J_0(u) \, du
$$



**Summary:**


$$
\mathcal{B}\{\text{circ}(r)\} = \frac{1}{2\pi\rho^2} \int_0^{2\pi\rho} r' \, J_0(r') \, dr'
$$



**Bessel identity:** $\int_0^x z \, J_0(z) \, dz = x \, J_1(x)$

**Therefore:**


$$
\mathcal{B}\{\text{circ}(r)\} = \frac{1}{2\pi\rho^2} \int_0^{2\pi\rho} r' \, J_0(r') \, dr' = \frac{J_1(2\pi\rho)}{\rho}
$$



This result is known as the **Airy pattern**, **jinc function**, or **sombrero function**. It describes the diffraction pattern of a circular aperture.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Identity for $J_0(a)$</div>
<div class="callout-content">



$$
\int_0^{2\pi} \exp(-ia\cos\theta) \, d\theta = 2\pi J_0(a)
$$



When $a = 0$:


$$
2\pi = 2\pi J_0(0)
$$


so $J_0(0) = 1$.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Properties of $J_1$ and limit evaluation</div>
<div class="callout-content">

The Bessel function $J_1(x)$ has the series expansion:


$$
J_1(x) = \frac{x}{2} - \frac{x^3}{16} + \cdots
$$



Therefore:


$$
\frac{J_1(2\pi\rho)}{\rho} = \frac{2\pi\rho}{2\rho} + \cdots = \pi
$$



Hence:


$$
\lim_{\rho \to 0} \frac{J_1(2\pi\rho)}{\rho} = \pi
$$



This gives the central maximum of the Airy pattern.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Fourier transform at zero frequency</div>
<div class="callout-content">

Let $\mathcal{F}\{g(x)\} = G(f_x)$. Then:


$$
G(f_x) = \int g(x) \exp(-i2\pi f_x x) \, dx
$$



At zero frequency:


$$
G(0) = \int g(x) \, dx
$$



The Fourier transform at $f_x = 0$ equals the total area under $g(x)$.

</div>
</div>

### Physical Significance

In Fourier optics, this result describes:
- The **[Fraunhofer diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/fraunhofer_diffraction/) pattern** of a circular aperture
- The **[point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/)** of a circular lens
- The fundamental limit of optical resolution ([Airy disk](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/))

### Related Topics

- [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/)
- [Fraunhofer Diffraction](#fraunhofer-diffraction---airy-pattern)
- [Optical Transfer Function](#optical-transfer-function-otf)

### Useful Fourier Pairs for Apertures

When apertures are scaled, the similarity theorem applies. These are the most common Fourier pairs in [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) calculations:

| Aperture | Function | [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) |
|----------|----------|-------------------|
| Rectangular (width $a$, height $b$) | $\text{rect}\left(\dfrac{x}{a}, \dfrac{y}{b}\right)$ | $ab \cdot \text{sinc}(a\xi) \cdot \text{sinc}(b\eta)$ |
| Square (side $a$) | $\text{rect}\left(\dfrac{x}{a}, \dfrac{y}{a}\right)$ | $a^2 \cdot \text{sinc}(a\xi, a\eta)$ |
| Circular (radius $r_0$) | $\text{circ}\left(\dfrac{r}{r_0}\right)$ | $\pi r_0^2 \cdot \dfrac{2J_1(2\pi r_0 \rho)}{2\pi r_0 \rho}$ |

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Scaling Relationship</div>
<div class="callout-content">

Larger apertures produce narrower diffraction patterns (and vice versa). The product of aperture size and diffraction spread is constant — this is the Fourier uncertainty principle in action.

</div>
</div>

---

### Properties of [Delta Functions](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/)

## 1. Defining Properties



$$
\delta(x - x_0) = 0, \quad x \neq x_0
$$





$$
\int_{x_1}^{x_2} f(\alpha) \, \delta(\alpha - x_0) \, d\alpha = f(x_0), \quad x_1 < x_0 < x_2
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Sifting Property</div>
<div class="callout-content">

The second equation is the **sifting property**: the delta function "sifts out" the value of $f$ at the spike location $x_0$. This is the defining property that makes delta functions useful — they sample a function at a single point.

</div>
</div>

## 2. Scaling Properties



$$
\delta\left(\frac{x - x_0}{b}\right) = |b| \, \delta(x - x_0)
$$





$$
\delta(ax - x_0) = \frac{1}{|a|} \delta\left(x - \frac{x_0}{a}\right)
$$





$$
\delta(-x + x_0) = \delta(x - x_0)
$$





$$
\delta(-x) = \delta(x) \quad \text{(even function)}
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Why Scaling Produces a Factor of $|a|$</div>
<div class="callout-content">

The delta function must always integrate to 1. If you compress it horizontally by factor $a$, it becomes narrower — but the area must stay the same, so the height must increase by $|a|$. Conversely, $\delta(ax)$ is $a$ times narrower, so it must be divided by $|a|$ to preserve unit area.

</div>
</div>

## 3. Properties in Products



$$
f(x) \, \delta(x - x_0) = f(x_0) \, \delta(x - x_0)
$$





$$
x \, \delta(x - x_0) = x_0 \, \delta(x - x_0)
$$





$$
\delta(x) \, \delta(x - x_0) = 0, \quad x_0 \neq 0
$$





$$
\delta(x - x_0) \, \delta(x - y_0)
$$

 is not defined

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Freezing Property</div>
<div class="callout-content">

The first equation is the **freezing property**: when you multiply $f(x)$ by $\delta(x - x_0)$, the delta "freezes" the value of $f$ at $x_0$. Since the delta is zero everywhere except at $x_0$, only the value $f(x_0)$ matters. The result is a delta spike of strength $f(x_0)$.

</div>
</div>

## 4. Integral Properties



$$
\int_{-\infty}^{\infty} A \, \delta(\alpha - x_0) \, d\alpha = A
$$





$$
\int_{-\infty}^{\infty} \delta(\alpha - x_0) \, \delta(x - \alpha) \, d\alpha = \delta(x - x_0)
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Delta Convolution</div>
<div class="callout-content">

The second integral is a [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/): $\delta(x) * \delta(x - x_0) = \delta(x - x_0)$. Convolving with a shifted delta just shifts the function — the delta acts as a "copy and shift" operator.

</div>
</div>

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Convolution of Delta with Itself</div>
<div class="callout-content">



$$
\delta(x) * \delta(x) = \delta(x)
$$



**Proof via Fourier transform:**
1. $\mathcal{F}\{\delta(x)\} = 1$ (delta transforms to a constant)
2. $\mathcal{F}\{\delta * \delta\} = \mathcal{F}\{\delta\} \cdot \mathcal{F}\{\delta\} = 1 \cdot 1 = 1$ (convolution theorem)
3. $\mathcal{F}^{-1}\{1\} = \delta(x)$

**Interpretation:** The delta function is the identity element for convolution — convolving any function with $\delta$ returns that function unchanged. Convolving $\delta$ with itself just returns $\delta$.

</div>
</div>

### Properties of [Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)

## Commutative


$$
f(x) * h(x) = h(x) * f(x)
$$



## Distributive


$$
[a \, v(x) + b \, w(x)] * h(x) = a[v(x) * h(x)] + b[w(x) * h(x)]
$$



## Shift Invariance
If $f(x) * h(x) = g(x)$

then $f(x - x_0) * h(x) = g(x - x_0)$

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Why Shift Invariance Matters</div>
<div class="callout-content">

Shifting the input shifts the output by the same amount. This is the defining property of [LSI systems](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) — the system behaves the same regardless of where the input is located.

</div>
</div>

## Associative


$$
[v(x) * w(x)] * h(x) = v(x) * [w(x) * h(x)]
$$



<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Multiplication and Convolution Don't Mix</div>
<div class="callout-content">

$[v(x) \cdot w(x)] * h(x) \neq v(x) \cdot [w(x) * h(x)]$

Counter example: Let $w(x) = \delta(x)$
- $[v(x) \cdot \delta(x)] * h(x) = v(0) h(x)$
- But $v(x) \cdot [\delta(x) * h(x)] = v(x) h(0)$

</div>
</div>

## Identity Operator


$$
f(x) * \delta(x) = f(x)
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Delta as Identity</div>
<div class="callout-content">

The delta function is the identity element for convolution — convolving with $\delta$ leaves the function unchanged. This is analogous to multiplying by 1 or adding 0.

</div>
</div>

## Derivatives


$$
f(x) * \delta^{(k)}(x) = f^{(k)}(x)
$$



where $\delta^{(k)} = \frac{d^k \delta(x)}{dx^k}$ ($k$ = derivative)

and $f^{(k)} = \frac{d^k f(x)}{dx^k}$

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Differentiation via Convolution</div>
<div class="callout-content">

Convolving with the derivative of a delta differentiates the function. This works because convolution commutes with differentiation:



$$
\frac{d}{dx}[f * g] = f * \frac{dg}{dx} = \frac{df}{dx} * g
$$



Setting $g = \delta$ and using $f * \delta = f$ gives the result. In practice, this means you can compute derivatives by convolving with an approximation to $\delta'$ (a difference kernel like $[1, -1]$).

</div>
</div>

## Repeated Convolution

Convolving multiple functions together produces a result that tends toward a Gaussian, regardless of the original shapes (provided they have finite variance):



$$
f_1(x) * f_2(x) * f_3(x) * \cdots * f_n(x) \xrightarrow{n \to \infty} \text{Gaussian}
$$



Each [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) "smooths" the result further. Sharp features get rounded, asymmetries cancel out, and the characteristic bell curve emerges. After just a few convolutions, even rectangular or triangular functions look nearly Gaussian.

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Central Limit Theorem</div>
<div class="callout-content">

This is the [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) form of the Central Limit Theorem. In probability, convolution corresponds to summing independent random variables — the PDF of a sum is the convolution of the individual PDFs.

No matter what shape the original distributions have (as long as they have finite variance), their repeated convolution approaches a Gaussian. This is why:
- The Gaussian appears so often in nature (many small independent effects add up)
- Diffraction patterns from complex apertures often have Gaussian-like envelopes
- Repeated imaging through imperfect systems tends toward Gaussian blur

</div>
</div>

## Scaling
If $f(x) * h(x) = g(x)$

then $f\left(\frac{x}{b}\right) * h\left(\frac{x}{b}\right) = |b| \, g\left(\frac{x}{b}\right)$
### Example of Scaling Theorem

Let $f(x) = h(x) = \text{rect}(x)$



$$
g(x) = f(x) * h(x) = \text{tri}(x)
$$



where $\text{tri} = \begin{cases} 1 - |x|, & |x| \leq 1 \\ 0, & \text{else} \end{cases}$

---

Let $b = 2$



$$
f\left(\frac{x}{b}\right) = \text{rect}\left(\frac{x}{2}\right)
$$





$$
g(x) = \text{rect}\left(\frac{x}{2}\right) * \text{rect}\left(\frac{x}{2}\right) = 2 \, \text{tri}\left(\frac{x}{2}\right)
$$



Area with no shift $= 1 \times 2 = 2$

The triangle function now extends from $-2$ to $2$ with peak value of $2$ at $x = 0$.
### Examples of Convolutions in Two Dimensions

## i) $f(x,y) * \delta(x,y)$ - Perfect Sampling

*Laser beam scanning negligible width*



$$
g(x,y) = f(x,y) * \delta(x,y) = f(x,y)
$$



Detector receives exact photograph $f(x,y)$.

---

## ii) $f(x,y) * b(x,y)$ - Total Light Through Spot



$$
g(x',y') = \iint f(x,y) \, b(x-x', y-y') \, dx \, dy
$$



Detector receives: $g(x,y) = f(x,y) * b(x,y) = f(x,y) \otimes b(x,y)$

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>When Convolution Equals Correlation</div>
<div class="callout-content">

If $b(x,y)$ is symmetric (i.e., $b(-x,-y) = b(x,y)$), then convolution and correlation are identical:


$$
f * b = f \star b
$$



**Why:** Correlation is defined as convolution with the **flipped** function: $f \star b = f * b(-x,-y)$. If $b$ is already symmetric, flipping does nothing, so the two operations coincide.

**In optics:** Many PSFs are symmetric (e.g., Airy disk, Gaussian blur), so imaging can be described equivalently as convolution or correlation with the PSF.

</div>
</div>

---

## iii) $f(x,y) * \delta(x)$ - Line Response



$$
g(x,y) = f(x,y) * \delta(x) \cdot 1
$$





$$
= \int_{-\infty}^{\infty} f(x,\beta) \, d\beta = \ell_x(x)
$$



Detector receives line response: y-dependence is averaged out, result is only a function of x.
### Line Response and Transfer Function

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

This means that if we are interested in the frequency response along the x-axis only, we can apply a line function $\delta(x)$ to the system (to form $\ell_x(x)$), and take its Fourier transform (one-dim) to yield $H(z,0)$.

</div>
</div>



$$
\xrightarrow{d\omega} \boxed{h(x,y)} \xrightarrow{\ell_\omega} \quad \mathcal{F}\{\ell_x(x)\} = H(z,0)
$$



To find other profiles of the general [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/), we can rotate the line response to any angle (not necessary) just along x or y axis.



$$
H(z,0) = \iint f(x,y) e^{-j\pi f_x x} \, dx \, dy
$$





$$
= \int \left[\int f(x,\beta) \, d\beta\right] e^{-j2\pi f_x x} \, dx
$$



where $\ell_x(x)$ = line response

---

## Edge Response (Step Response)

Consider applying a step to the input:



$$
f(x,y) = \text{step}(x) \cdot 1
$$





$$
e_x(x) = \mathcal{L}\{\text{step}(x) \cdot 1\} = h(x,y) * * \text{step}(x) \cdot 1
$$





$$
= \iint h(\alpha,\beta) \, \text{step}(x-\alpha) \, d\alpha \, d\beta
$$





$$
= \int \left[\int h(\alpha,\beta) \, d\beta\right] \text{step}(x-\alpha) \, d\alpha
$$





$$
= \int_{-\infty}^{\infty} \ell_x(\alpha) \, \text{step}(x-\alpha) \, d\alpha = \int_{-\infty}^{x} \ell_x(\alpha) \, d\alpha
$$





$$
\therefore \quad \ell_x(x) = \frac{d}{dx} e_x(x)
$$



<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Measuring the Line Spread Function</div>
<div class="callout-content">

The line spread function $\ell_x(x)$ equals the derivative of the edge response $e_x(x)$:


$$
\ell_x(x) = \frac{d}{dx} e_x(x)
$$



**Why this matters practically:** Edges are easier to create than thin lines. To measure an optical system's LSF:
1. Image a sharp edge (knife-edge test)
2. Measure the blurred edge response $e_x(x)$
3. Differentiate numerically to get the LSF

This avoids the difficulty of creating a perfectly thin, uniform line source.

</div>
</div>
### Transfer Function from Line and Edge Response

Finally:



$$
H(z,0) = \mathcal{F}\{\ell_x(x)\} = \mathcal{F}\left\{\frac{d}{dx} e_x(x)\right\}
$$





$$
= j2\pi z \, \mathcal{F}\{e_x(x)\}
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

This means we can apply a step function to the system, Fourier transform the result in one-dimension, and multiply by $j2\pi z$ to obtain $H(z,0)$.

</div>
</div>

## Physical Interpretation

### Impulse Response


$$
\delta(x) \rightarrow \boxed{\frac{h(\alpha)}{H(z)}} \rightarrow h(x)
$$



- Spectrum of input: $1$
- Spectrum of output: $H(z) = \mathcal{F}\{h(x)\}$

### Step Response


$$
\text{step}(x) \rightarrow \boxed{\frac{h(x)}{H(z)}} \rightarrow \int h(\alpha) \, d\alpha = e_x(x)
$$



- Spectrum of input: $\frac{1}{j2\pi z}$ (plus DC)
- [Transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/): $H(z) = j2\pi z \, \mathcal{F}\{e_x(x)\}$

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

We use that the delta function can be thought of as generating all frequencies simultaneously in a **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** system. What causes all discussed, but all frequencies are needed of equal amplitude, but rather by $\frac{1}{z}$. We must therefore multiply the result by $z$ to compensate and obtain $H(z)$.

</div>
</div>
## VIII. Diffraction Theory Fundamentals

*Lecture start: 2025-02-05*

- Sound waves in gas require **scalar** values (scalar diff. theory)
- EM waves are **vectors** (vector theory)

## Maxwell's Equations (Current & Source-free)

<div class="callout callout-abstract">
<div class="callout-title"><span class="callout-icon">📄</span>Maxwell's Equations</div>
<div class="callout-content">

**Faraday's Law** (changing $\vec{H}$ induces $\vec{E}$):


$$
\nabla \times \vec{E} = -\mu \frac{\partial \vec{H}}{\partial t}
$$



**Ampère's Law** (changing $\vec{E}$ induces $\vec{H}$):


$$
\nabla \times \vec{H} = \epsilon(r) \frac{\partial \vec{E}}{\partial t}
$$



**Gauss's Law for Electricity** (no free charges):


$$
\nabla \cdot \vec{D} = 0
$$



**Gauss's Law for Magnetism** (no magnetic monopoles):


$$
\nabla \cdot \mu_0 \vec{H} = 0
$$



where $H$ is the magnetic field intensity.

</div>
</div>

## Derivation of Wave Equation

We have:



$$
\nabla \times (\nabla \times \vec{E}) = -\mu \cdot \nabla \times \left(\frac{\partial \vec{H}}{\partial t}\right) = -\mu_0 \epsilon(r) \frac{\partial^2 \vec{E}}{\partial t^2}
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Vector Identity</div>
<div class="callout-content">



$$
\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}
$$



</div>
</div>

Therefore:



$$
\nabla^2 \vec{E} - \nabla\left(\nabla \cdot \frac{\vec{D}}{\epsilon(r)}\right) - \mu_0 \epsilon(r) \frac{\partial^2 \vec{E}}{\partial t^2} = 0
$$



If medium is **homogeneous**, $\epsilon(r) = \text{constant}$, then:



$$
\nabla \cdot \frac{\vec{D}}{\epsilon(r)} = \frac{1}{\epsilon}[\nabla \cdot \vec{D}] = 0
$$



<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Homogeneous Wave Equation</div>
<div class="callout-content">



$$
\nabla^2 \vec{E} - \mu_0 \epsilon \frac{\partial^2 \vec{E}}{\partial t^2} = 0
$$



</div>
</div>
### Scalar Wave Equation

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Refractive Index</div>
<div class="callout-content">



$$
n = \sqrt{\frac{\epsilon}{\epsilon_0}}
$$



Also: $c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$ (speed of light), so $\mu_0 \epsilon = \mu_0 n^2 \epsilon_0 = \frac{n^2}{c^2}$

</div>
</div>

Then, for each component of the vector $E_x, E_y, E_z$, we have:



$$
\nabla^2 E_i - \frac{n^2}{c^2} \frac{\partial^2 E_i}{\partial t^2} = 0, \quad i = x, y, \text{ or } z
$$



where the wave propagation speed is $c/n$.

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Assumptions for Scalar Wave Equation</div>
<div class="callout-content">

1. $n(r)$ must not change significantly over a distance $\lambda$
2. All apertures must be $\geq \lambda$
3. Observations not too close to the aperture
4. Polarization state is linear and unaffected by diffraction

![Grating assumption](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/grating_assumption.svg)
![Aperture assumption](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/aperture_assumption.svg)

If $\epsilon(r)$ varies (e.g., phase grating), the medium is **not** homogeneous and an extra term $\nabla\left(\nabla \cdot \frac{\vec{D}}{\epsilon(r)}\right)$ couples vector components, making the problem more difficult.

</div>
</div>

When these assumptions hold, the cross term can be neglected and we can use a **scalar wave equation**:



$$
\nabla^2 E - \frac{n^2}{c^2} \frac{\partial^2 E}{\partial t^2} = 0
$$



where $E$ is a scalar representing the amplitude of a single field component.
### Helmholtz Equation (Frequency-Domain Form)

Starting from the wave equation:



$$
\nabla^2 E - \frac{n^2}{c_0^2} \frac{\partial^2 E}{\partial t^2} = 0
$$



**Take the time [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)** of the equation.

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Derivative mappings</div>
<div class="callout-content">



$$
\frac{\partial}{\partial t}(\cdot) \to j2\pi f(\cdot) = j\omega(\cdot)
$$




$$
\frac{\partial^2}{\partial t^2}(\cdot) \to (j2\pi f)^2(\cdot) = -\omega^2(\cdot)
$$



</div>
</div>

Thus:



$$
\nabla^2 \hat{u}(\bar{r},\omega) + \frac{n^2 \omega^2}{c_0^2} \hat{u}(\bar{r},\omega) = 0
$$



**Define the wavenumber:**



$$
k = \frac{n\omega}{c_0} = \frac{2\pi n}{\lambda}
$$



Therefore, the Helmholtz equation is:

<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Helmholtz Equation</div>
<div class="callout-content">



$$
\nabla^2 \hat{u}(\bar{r},\omega) + k^2 \hat{u}(\bar{r},\omega) = 0
$$



</div>
</div>

## Monochromatic Wave



$$
u(\bar{r},t) = a(x,y,z) \cos[2\pi\nu_0 t - \phi(x,y,z)]
$$





$$
= a(x,y,z) \cos\left[2\pi\nu_0 \left(t - \frac{\phi(x,y,z)}{2\pi\nu_0}\right)\right]
$$





$$
\Rightarrow \hat{u}(\bar{r},\omega_0) = a(x,y,z) \, \mathcal{F}\left\{\cos\left[2\pi\nu_0 \left(t - \frac{\phi(x,y,z)}{2\pi\nu_0}\right)\right]\right\}
$$





$$
= a(x,y,z) \, e^{-j2\pi\nu \frac{\phi(x,y,z)}{2\pi\nu_0}} \left[\frac{\delta(\nu-\nu_0)}{2} + \frac{\delta(\nu+\nu_0)}{2}\right]
$$





$$
= a(x,y,z) \, e^{-j\phi(x,y,z)} \frac{\delta(\nu-\nu_0)}{2} + a(x,y,z) \, e^{+j\phi(x,y,z)} \frac{\delta(\nu+\nu_0)}{2}
$$



where $a(x,y,z)$ is real.

### Complex Amplitude

We denote the complex amplitude as the amplitude of one of these delta functions (use $\delta(\nu + \nu_0)$):



$$
\boxed{\hat{u}(x,y,z) = \frac{a(x,y,z)}{2} \exp[-j\phi(x,y,z)]}
$$



**Complex Amplitude**

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

It is not surprising that the result of a Fourier transformation is a complex function. Only if the original is **even** (i.e., $\cos \phi = 0$) would the F.T. be real.

</div>
</div>

## Returning to Original Time Signal

To return to original time signal, we perform the inverse F.T. in time:



$$
u(x,y,z,t) = \mathcal{F}_t^{-1}\left\{\hat{u}(x,y,z)\delta(\nu+\nu_0) + \hat{u}^*(x,y,z)\delta(\nu-\nu_0)\right\}
$$





$$
= \int \frac{a(x,y,z)}{2} e^{+j\phi(x,y,z)} \delta(\nu+\nu_0) e^{+j2\pi\nu t} \, d\nu
$$





$$
+ \int \frac{a(x,y,z)}{2} e^{-j\phi(x,y,z)} \delta(\nu-\nu_0) e^{+j2\pi\nu t} \, d\nu
$$





$$
= \frac{a(x,y,z)}{2} e^{j\phi(x,y,z)} e^{-j2\pi\nu_0 t} + \frac{a(x,y,z)}{2} e^{-j\phi(x,y,z)} e^{j2\pi\nu_0 t}
$$





$$
= \frac{a(x,y,z)}{2}\left[e^{j(2\pi\nu_0 t - \phi(x,y,z))} + e^{-j(2\pi\nu_0 t - \phi(x,y,z))}\right]
$$





$$
= a(x,y,z) \cos(2\pi\nu_0 t - \phi(x,y,z))
$$



### Returning to Time Signal (Alternative Method)

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

We can also return to the original time signal by using the expression:

</div>
</div>



$$
u(x,y,z,t) = \text{Re}\left\{\hat{u}^*(x,y,z) e^{j2\pi\nu_0 t}\right\}
$$



But this is simply:



$$
u(x,y,z,t) = \frac{\hat{u}^*(x,y,z) e^{j2\pi\nu_0 t}}{2} + \frac{\hat{u}(x,y,z) e^{-j2\pi\nu_0 t}}{2}
$$



But note this is just a Fourier synthesis where we have added both positive & negative frequency components at frequency $\nu_0$ with weights given by the Fourier coefficients $\hat{u}(x,y,z)$.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

We can perform an inverse Fourier transform without knowing it, and are also restoring the $\delta(\nu - \nu_0)$ delta function.

</div>
</div>

---

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Summary</div>
<div class="callout-content">

But this is simply the real part of $\hat{u}^*(x,y,z)$.

$\Rightarrow$ We care about amplitude and phase separately, as the real part is a linear combination of both.

</div>
</div>

### Plane-Wave Solutions of the Helmholtz Equation

The Helmholtz equation is:



$$
\nabla^2 \hat{u}(\bar{r}) + k^2 \hat{u}(\bar{r}) = 0
$$



A plane-wave solution is:



$$
\hat{u}(\bar{r}) = \hat{C} e^{j\vec{k} \cdot \bar{r}}
$$



where the wavevector is $\vec{k} = (k_x, k_y, k_z)$.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Plane Wave Solution</div>
<div class="callout-content">

This is a **plane wave solution** to our E-M wave (or sound wave) in free space (3-dim).
- $\vec{k}$ is the direction of propagation
- $\hat{C}$ is a complex constant

</div>
</div>

## Alternative Expression

Let the complex amplitude be written as:



$$
\hat{C} = |A| e^{j\phi}
$$



Write the wavevector as:



$$
\vec{k} = (k_x, k_y, k_z) = k(\gamma_x, \gamma_y, \gamma_z)
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Direction Cosines</div>
<div class="callout-content">



$$
\gamma_x = \cos\theta_x, \quad \gamma_y = \cos\theta_y, \quad \gamma_z = \cos\theta_z
$$



where $\theta_x$, $\theta_y$, $\theta_z$ are angles from the respective axes.

</div>
</div>

## Plane Wave in Cartesian Coordinates

Thus:



$$
\hat{u}(x,y,z) = A e^{j\phi} e^{jk(\gamma_x x + \gamma_y y + \gamma_z z)}
$$



<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Plane-Wave Expression (Final Form)</div>
<div class="callout-content">



$$
\hat{u}(x,y,z) = A e^{j[k(\gamma_x x + \gamma_y y + \gamma_z z) + \phi]}
$$



- $A$ is the amplitude of the wave field
- $\phi$ is the phase at the origin

</div>
</div>

### Plane Wave Time Domain and Direction Cosines

The real field distribution is obtained by inverse Fourier transforming (in temporal frequency), this spatial distribution multiplied by $\frac{\delta(\nu+\nu_0) + \delta(\nu-\nu_0)}{2}$.

This gives:



$$
u(x,y,z,t) = \frac{A e^{j(k(\gamma_x x + \gamma_y y + \gamma_z z) + \phi)}}{2} e^{j2\pi\nu_0 t} + \frac{A e^{j(k(\gamma_x x + \gamma_y y + \gamma_z z) + \phi)}}{2} e^{-j2\pi\nu_0 t}
$$





$$
= A \cos(2\pi\nu_0 t - k(\gamma_x x + \gamma_y y + \gamma_z z) - \phi)
$$



## Direction Cosines Normalization

Recall: $\vec{k} = |\vec{k}|(\gamma_x, \gamma_y, \gamma_z)$

Then:


$$
\vec{k} \cdot \vec{k} = |\vec{k}|^2 (\gamma_x, \gamma_y, \gamma_z) \cdot (\gamma_x, \gamma_y, \gamma_z) = |\vec{k}|^2 (\gamma_x^2 + \gamma_y^2 + \gamma_z^2)
$$



But also $\vec{k} \cdot \vec{k} = |\vec{k}|^2$. Therefore:

<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Direction Cosines Normalization</div>
<div class="callout-content">



$$
\gamma_x^2 + \gamma_y^2 + \gamma_z^2 = 1
$$





$$
\Rightarrow \gamma_z = \left[1 - (\gamma_x^2 + \gamma_y^2)\right]^{1/2}
$$



</div>
</div>

## Propagating vs. Evanescent Components

**Case 1: Propagating wave**

If $\gamma_x^2 + \gamma_y^2 < 1$, then $\gamma_z$ is real and $e^{jk\gamma_z z}$ represents a **propagating wave** in the $+z$ direction.

**Case 2: Evanescent wave**

If $\gamma_x^2 + \gamma_y^2 > 1$, then $\gamma_z$ is imaginary. Write $\gamma_z = j\alpha$ where $\alpha > 0$. Then:



$$
e^{jk\gamma_z z} = e^{jk(j\alpha)z} = e^{-k\alpha z}
$$



<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Evanescent Field</div>
<div class="callout-content">

The field amplitude decays exponentially with $z$:


$$
e^{-k\alpha z}
$$


This is an **evanescent** (exponentially decaying) field that does not propagate.

</div>
</div>

### Plane Wave Propagation

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Free Space as a Linear System</div>
<div class="callout-content">

![Free space propagation](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/free_space_propagation.svg)

The diagram shows two transverse planes (z₀ and z₁) perpendicular to the optical axis, with free space between them. A field at the input plane z₀ propagates to produce a field at z₁.

This can be abstracted as a **linear system** — the same framework used for electronic filters. Because free space propagation is linear and shift-invariant, it has a [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):



$$
H(\gamma_x, \gamma_y) = e^{jk\gamma_z(z_1 - z_0)}
$$



The **input field** is the optical field distribution at the starting plane $z_0$ — what you feed into the "system." The **output field** is what you get at $z_1$ after propagation. Comparing input to output, the only change is the phase factor $e^{jk\gamma_z z_0} \to e^{jk\gamma_z z_1}$ — the transverse pattern $e^{jk(\gamma_x x + \gamma_y y)}$ stays identical.

This is the [eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) property: plane waves pass through free space unchanged in shape, just phase-shifted by the [eigenvalue](/notes/areas/mathematics/linear_algebra/definitions/eigenvalue/). This framing connects wave optics to Fourier optics: decompose any input field into plane waves (angular spectrum), propagate each by multiplying by $H$, then recombine — exactly like filtering in signal processing.

</div>
</div>

## Eigenfunctions of Free-Space Propagation

The transverse [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) factor $e^{jk(\gamma_x x + \gamma_y y)}$ is an **[eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/)** of the free-space propagation operator.

### Why This Works

Write the field at the input plane as:



$$
\hat{u}(x,y,z_0) = A e^{j\phi} e^{jk\gamma_z z_0} e^{jk(\gamma_x x + \gamma_y y)}
$$



Propagating from $z_0$ to $z_1$ multiplies the field by the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):



$$
H = e^{jk\gamma_z(z_1 - z_0)}
$$



Thus the output is:



$$
\hat{u}(x,y,z_1) = e^{jk\gamma_z(z_1 - z_0)} \cdot \hat{u}(x,y,z_0)
$$



Substituting the input field:



$$
\hat{u}(x,y,z_1) = A e^{j\phi} e^{jk\gamma_z z_1} e^{jk(\gamma_x x + \gamma_y y)}
$$



### Eigenvalue Interpretation

Since propagation acts as:



$$
e^{jk(\gamma_x x + \gamma_y y)} \to e^{jk\gamma_z(z_1 - z_0)} \cdot e^{jk(\gamma_x x + \gamma_y y)}
$$



<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Eigenfunction/Eigenvalue of Free-Space Propagation</div>
<div class="callout-content">

**Eigenfunction:** $e^{jk(\gamma_x x + \gamma_y y)}$

**Eigenvalue:** $e^{jk\gamma_z(z_1 - z_0)}$

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Analogy with Linear Algebra Eigenvectors</div>
<div class="callout-content">

Recall from linear algebra: if $\mathbf{v}$ is an [eigenvector](/notes/areas/mathematics/linear_algebra/definitions/eigenvector/) of matrix $A$, then:



$$
A\mathbf{v} = \lambda \mathbf{v}
$$



The matrix doesn't rotate or distort $\mathbf{v}$ — it just scales it by $\lambda$.

**Same thing here.** The propagation operator $\mathcal{P}$ acts on the transverse pattern:



$$
\mathcal{P}\{e^{jk(\gamma_x x + \gamma_y y)}\} = \underbrace{e^{jk\gamma_z(z_1-z_0)}}_{\text{eigenvalue}} \cdot e^{jk(\gamma_x x + \gamma_y y)}
$$



The shape in $(x,y)$ is unchanged. Only a phase factor multiplies it.

**Why this matters:**
- Plane waves don't diffract or spread — they just accumulate phase
- Free space doesn't mix spatial frequencies — each propagates independently
- Any field can be decomposed into plane waves, each propagated separately, then recombined

This is why Fourier optics works: propagation is "diagonal" in the plane-wave basis, just like [LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) systems are diagonal in the complex exponential (frequency) basis for time signals.

</div>
</div>

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Eigenvalue depends on propagation distance</div>
<div class="callout-content">

Unlike typical eigenvalue problems where eigenvalues are fixed constants, here we have a *parameterized family* of propagation operators — one for each distance $(z_1 - z_0)$.
- The **eigenfunction** (transverse spatial pattern) stays the same
- The **eigenvalue** (phase shift) accumulates with distance

This is why plane waves are useful: they maintain their shape while propagating, just picking up phase.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Physical Meaning</div>
<div class="callout-content">

- Each transverse plane wave propagates independently
- Free space does not mix spatial frequencies
- Propagation only adds a phase (or decay) along $z$

This is the foundation of:
- Angular spectrum theory
- Fresnel / Fraunhofer diffraction
- Fourier-optics propagation models

</div>
</div>

### Transfer Function of Propagation

Since the **[eigenvalue](/notes/areas/mathematics/linear_algebra/definitions/eigenvalue/)** describes the **[transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)**:



$$
H(\gamma_x, \gamma_y) = \exp\left[jk\gamma_z(z_1 - z_0)\right] = \exp\left[jk\sqrt{1-(\gamma_x^2 + \gamma_y^2)}(z_1-z_0)\right]
$$



where $\gamma_x^2 + \gamma_y^2 \leq 1$ (non-evanescent)

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>From Eigenvalue to FFT-Based Propagation</div>
<div class="callout-content">

This transfer function is the bridge connecting eigenfunction theory to computational propagation:

**The conceptual chain:**



$$
\text{Plane waves as eigenfunctions} \to \text{Eigenvalues as phase factors}
$$




$$
\to \text{Transfer function} \to \text{FFT-based propagation}
$$



**Frequency-domain propagation:** Since each plane-wave component propagates independently, propagation becomes multiplication in spatial-frequency space:



$$
\tilde{U}(f_x, f_y; z_1) = H(f_x, f_y) \cdot \tilde{U}(f_x, f_y; z_0)
$$



This is the **angular spectrum method**: take the 2D Fourier transform of the input field, multiply by $H$, then inverse transform to get the output field.

**Why the square root matters:** The factor $\sqrt{1 - \gamma_x^2 - \gamma_y^2}$ comes from the dispersion relation (Helmholtz equation), ensuring the wavevector magnitude equals $k = 2\pi/\lambda$. When $\gamma_x^2 + \gamma_y^2 > 1$, the square root becomes imaginary, giving exponential decay — this is how the formulation naturally handles:
- Near-field (evanescent) components
- Spatial-frequency cutoffs at $1/\lambda$
- The transition from propagating to decaying waves

</div>
</div>

### Complex Amplitude and Amplitude Transmittance

Consider complex amplitude (monochromatic, with time dependence removed) at a plane $z = z_i$:



$$
u(x,y,z_i) = u_i(x,y)
$$



We define the **complex amplitude transmittance** as:



$$
t_i(x,y) = \frac{u_i^+(x,y)}{u_i^-(x,y)}
$$



where:
- $u_i^-(x,y)$ = field just before the aperture (incident)
- $u_i^+(x,y)$ = field just after the aperture (transmitted)

![Amplitude Transmittance](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/amplitude_transmittance.svg)

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Reading the Diagram</div>
<div class="callout-content">

The diagram shows a cross-section of an opaque screen with an aperture (hole) at plane $z_0$. The gray regions block light ($t = 0$), while the opening transmits it unchanged ($t = 1$). The complex amplitude transmittance $t_i(x,y) = u^+/u^-$ is the ratio of transmitted to incident field at each point.

</div>
</div>

## Why t = 1 Inside, t = 0 Outside

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Aperture Transmittance</div>
<div class="callout-content">

**Inside the aperture (the hole):** The wave passes through unchanged


$$
u^+(x,y) = u^-(x,y) \Rightarrow t_i(x,y) = 1
$$



**Outside the aperture (opaque screen):** The wave is blocked


$$
u^+(x,y) = 0 \Rightarrow t_i(x,y) = 0
$$



</div>
</div>

Therefore, for an ideal aperture:



$$
t_i(x,y) = \begin{cases} 1, & (x,y) \text{ inside aperture} \\ 0, & (x,y) \text{ outside aperture} \end{cases}
$$



This is often called the **aperture function** or **pupil function**.

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Why This Matters</div>
<div class="callout-content">

Because the transmitted field is $u^+(x,y) = t_i(x,y) \cdot u^-(x,y)$, the aperture literally **multiplies** the field.

This is why apertures turn into **convolutions in Fourier space** — the gateway to diffraction theory.

</div>
</div>

## Other Types of Transmittance

- **Film (amplitude mask):** $t_i(x,y)$ describes the dark/light pattern; $0 \leq |t_i| \leq 1$

- **Phase object (clear but not flat):** $|t_i(x,y)| = 1$ but $t_i$ is complex, representing different **phase delays** from varying thickness

## Angular Plane Wave Spectrum

The **angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) spectrum** is the fundamental concept connecting spatial patterns to propagating waves. Any complex field distribution $u_i(x,y)$ at a plane $z = z_i$ can be decomposed into a [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) of plane waves traveling in different directions.

![Angular Plane Wave Spectrum](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/angular_plane_wave_spectrum.svg)

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Diagram Explanation</div>
<div class="callout-content">

This figure illustrates the duality between **spatial domain** and **frequency domain** representations of an optical field:

- **Left (Spatial Domain):** The complex field $u_i(x,y)$ at a plane $z = z_i$, shown as an arbitrary wavefront. This is the physical field distribution—what a detector would measure in amplitude and phase at that plane.

- **Right (Frequency Domain):** The angular spectrum $U_i(\xi, \eta)$, shown as a peaked distribution in frequency space. The center (origin) represents low spatial frequencies (slowly varying features, nearly on-axis propagation), while points farther from the origin represent higher spatial frequencies (fine detail, steep propagation angles).

- **Center Arrows:** The Fourier transform $\mathcal{F}$ converts from spatial to frequency domain; the inverse $\mathcal{F}^{-1}$ converts back. These are exact, lossless transformations—no information is lost.

- **Bottom Box:** The crucial physical interpretation: spatial frequency $\xi = \cos\theta_x / \lambda$ directly encodes propagation direction. A point $(\xi, \eta)$ in the spectrum represents a plane wave component traveling at angles $(\theta_x, \theta_y)$ from the coordinate axes. Higher frequencies correspond to steeper angles.

</div>
</div>

### Fourier Transform Relationship

The [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) $U_i(\xi, \eta)$ and the spatial field $u_i(x,y)$ form a [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) pair:



$$
U_i(\xi, \eta) = \mathcal{F}\{u_i(x,y)\} = \iint u_i(x,y) \, e^{-j2\pi(\xi x + \eta y)} \, dx \, dy
$$





$$
u_i(x,y) = \mathcal{F}^{-1}\{U_i(\xi, \eta)\} = \iint U_i(\xi, \eta) \, e^{j2\pi(\xi x + \eta y)} \, d\xi \, d\eta
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Physical Interpretation</div>
<div class="callout-content">

The inverse transform shows that $u_i(x,y)$ is a weighted sum of complex exponentials $e^{j2\pi(\xi x + \eta y)}$. Each exponential is the transverse part of a plane wave. The spectrum $U_i(\xi, \eta)$ gives the complex amplitude (magnitude and phase) of each plane wave component.

</div>
</div>

### Connecting Spatial Frequency to Propagation Angle

A [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) propagating in direction $(\gamma_x, \gamma_y, \gamma_z)$ has the form:



$$
C \exp\left[jk(\gamma_x x + \gamma_y y + \gamma_z z)\right]
$$



At a fixed plane $z = z_i$, the transverse part is:



$$
C \exp\left[jk(\gamma_x x + \gamma_y y)\right] = C \exp\left[j2\pi\left(\frac{\gamma_x}{\lambda} x + \frac{\gamma_y}{\lambda} y\right)\right]
$$



Comparing with the Fourier [basis](/notes/areas/mathematics/linear_algebra/definitions/basis/) $e^{j2\pi(\xi x + \eta y)}$, the spatial frequencies are:



$$
\boxed{\xi = \frac{\gamma_x}{\lambda} = \frac{\cos\theta_x}{\lambda} = f_x}
$$





$$
\boxed{\eta = \frac{\gamma_y}{\lambda} = \frac{\cos\theta_y}{\lambda} = f_y}
$$



where $\gamma_x = \cos\theta_x$ and $\gamma_y = \cos\theta_y$ are the direction cosines (angles measured from the $x$ and $y$ axes).

<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Key Insight: Frequency = Direction</div>
<div class="callout-content">

Each point $(\xi, \eta)$ in the angular spectrum corresponds to a plane wave propagating at a specific angle. Low spatial frequencies (near the origin) represent waves traveling nearly parallel to the $z$-axis. High spatial frequencies represent steeply tilted waves.

The constraint $\gamma_x^2 + \gamma_y^2 + \gamma_z^2 = 1$ means:
- If $\xi^2 + \eta^2 < 1/\lambda^2$: **propagating wave** (real $\gamma_z$)
- If $\xi^2 + \eta^2 > 1/\lambda^2$: **evanescent wave** (imaginary $\gamma_z$, exponential decay)

</div>
</div>

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Cosine Grating Decomposition</div>
<div class="callout-content">

Consider a 1D cosine grating as the input field:


$$
u_i(x,y) = \cos(2\pi f_0 x)
$$



The angular plane-wave spectrum is:


$$
U_i(\xi,\eta) = \iint u_i(x,y) \, e^{-j2\pi(\xi x + \eta y)} \, dx \, dy
$$



Using the Fourier transform of a cosine:


$$
\cos(2\pi f_0 x) = \frac{1}{2}\left(e^{j2\pi f_0 x} + e^{-j2\pi f_0 x}\right)
$$



we obtain:


$$
U_i(\xi,\eta) = \frac{1}{2}\Big[\delta(\xi - f_0) + \delta(\xi + f_0)\Big] \, \delta(\eta)
$$



Using the angular-frequency relations $\xi = \cos\theta_x / \lambda$ and $\eta = \cos\theta_y / \lambda$:


$$
U_i(\xi,\eta) = \frac{1}{2}\left[\delta\!\left(\frac{\cos\theta_x}{\lambda} - f_0\right) + \delta\!\left(\frac{\cos\theta_x}{\lambda} + f_0\right)\right] \delta\!\left(\frac{\cos\theta_y}{\lambda}\right)
$$



**Physical interpretation:** The cosine grating consists of exactly **two plane waves** propagating symmetrically at angles $\pm\theta_x$ where $\cos\theta_x = \lambda f_0$. The delta functions at $\pm f_0$ in frequency space correspond to these two discrete propagation directions. Higher grating frequencies $f_0$ mean steeper propagation angles.

</div>
</div>

### Why This Matters

The [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) representation is powerful because:

1. **Propagation becomes multiplication:** Each [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) component propagates independently, just multiplied by the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) $H(\xi, \eta) = e^{jk\gamma_z \Delta z}$

2. **[Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) is natural:** The finite extent of an aperture spreads the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/), causing the beam to diverge

3. **Computation is efficient:** Propagation via FFT → multiply by $H$ → IFFT is $O(N \log N)$

### Angular Spectrum Diffraction Formulation

The complete recipe for propagating a field from plane $z = z_i$ to plane $z = z_o$ using the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) method:

**Step 1: Input field and its [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/)**

The input field $u_i(x,y)$ at plane $z = z_i$ has [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/):



$$
U_i(\xi, \eta) = \iint u_i(x,y) \, e^{-j2\pi(\xi x + \eta y)} \, dx \, dy
$$



**Step 2: [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)**

The [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) for propagation through distance $\Delta z = z_o - z_i$ is:



$$
H(\xi, \eta) = \exp\left[jk(z_o - z_i)\sqrt{1 - \lambda^2(\xi^2 + \eta^2)}\right]
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Propagating vs Evanescent</div>
<div class="callout-content">

- When $\xi^2 + \eta^2 < 1/\lambda^2$: the square root is real → propagating wave (phase accumulation)
- When $\xi^2 + \eta^2 > 1/\lambda^2$: the square root is imaginary → evanescent wave (exponential decay)

</div>
</div>

**Step 3: Propagation in frequency domain**

Multiply the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) by the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):



$$
U_o(\xi, \eta) = U_i(\xi, \eta) \cdot H(\xi, \eta)
$$



**Step 4: Output field via inverse transform**

The output field at plane $z = z_o$ is:



$$
u_o(x,y) = \mathcal{F}^{-1}\{U_i(\xi, \eta) \cdot H(\xi, \eta)\}
$$



Explicitly:



$$
u_o(x,y) = \iint U_i(\xi, \eta) \exp\left[jk(z_o - z_i)\sqrt{1 - \lambda^2(\xi^2 + \eta^2)}\right] e^{j2\pi(\xi x + \eta y)} \, d\xi \, d\eta
$$



<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Angular Spectrum Method Summary</div>
<div class="callout-content">



$$
u_i(x,y) \xrightarrow{\mathcal{F}} U_i(\xi,\eta) \xrightarrow{\times H} U_o(\xi,\eta) \xrightarrow{\mathcal{F}^{-1}} u_o(x,y)
$$



This is exact (within the scalar wave approximation) and handles both near-field and far-field diffraction. The Fresnel and Fraunhofer approximations are limiting cases of this general formulation.

</div>
</div>

**[Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) Form**

By the [convolution theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/), multiplication in the frequency domain corresponds to [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) in the spatial domain:



$$
u_o(x,y) = u_i(x,y) * \mathcal{F}^{-1}\{H(\xi,\eta)\}
$$



The inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) $\mathcal{F}^{-1}\{H\}$ is the **[impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** ([point spread function](/notes/areas/electrical_engineering/signals_systems/definitions/point_spread_function/)) of free-space propagation.

### Paraxial Approximation

When the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) is concentrated near the optical axis (low spatial frequencies dominate), the **paraxial approximation** simplifies the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/).

**Condition:** $\lambda^2(\xi^2 + \eta^2) \ll 1$ (spatial frequencies much smaller than $1/\lambda$)

**Binomial expansion:** For small $a$:


$$
(1 - a)^{1/2} \approx 1 - \frac{a}{2}
$$



Applying this to the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):


$$
\sqrt{1 - \lambda^2(\xi^2 + \eta^2)} \approx 1 - \frac{\lambda^2}{2}(\xi^2 + \eta^2)
$$



The paraxial [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) becomes:


$$
H_{\text{paraxial}}(\xi,\eta) = \exp\left[jk\Delta z\right] \cdot \exp\left[-j\pi\lambda\Delta z(\xi^2 + \eta^2)\right]
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Physical Interpretation of the Factorized Form</div>
<div class="callout-content">

- **First factor** $\exp[jk\Delta z]$: A **global phase** that depends only on propagation distance. This is the on-axis phase accumulation and is often dropped since it doesn't affect intensity.
- **Second factor** $\exp[-j\pi\lambda\Delta z(\xi^2 + \eta^2)]$: Produces **diffraction spreading**. Higher spatial frequencies (larger $\xi, \eta$) accumulate more phase, causing fine details to spread faster than coarse features.

</div>
</div>

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Fresnel Approximation</div>
<div class="callout-content">

The paraxial transfer function leads directly to the **Fresnel diffraction** integral. The quadratic phase factor $\exp[-j\pi\lambda\Delta z(\xi^2 + \eta^2)]$ is the signature of Fresnel diffraction.

</div>
</div>

### Transmitted Field and Angular Plane Wave Spectrum

If we know the amplitude transmittance $t_i(x,y)$ and the incident wave field $u_i(x,y)$, we obviously can calculate the transmitted complex field:



$$
\boxed{u_i^+(x,y) = u_i^-(x,y) \cdot t_i(x,y)}
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>This is our case of interest</div>
</div>

## Complete Example: Tilted Plane Wave Through Circular Aperture

This section provides a complete angular-spectrum analysis of an oblique [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) passing through a circular aperture.

### Setup and Notation

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Notation</div>
<div class="callout-content">

- Transverse coordinate: $\mathbf{r} = (x, y)$
- Spatial frequency: $\mathbf{f} = (f_x, f_y)$
- Wavenumber: $k = n\omega/c_0 = 2\pi/\lambda$
- Direction cosines: $\boldsymbol{\gamma} = (\gamma_x, \gamma_y, \gamma_z)$ with $\gamma_x^2 + \gamma_y^2 + \gamma_z^2 = 1$
- Transverse spatial frequency of tilted plane wave: $\mathbf{f}_0 = \frac{k}{2\pi}(\gamma_x, \gamma_y)$

</div>
</div>

### Step 1: Incident Plane Wave at Object Plane $z = z_0$

A [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) incident obliquely arrives at the object plane with the transverse factor:



$$
u^-(x,y) = A e^{j\phi} e^{jk(\gamma_x x + \gamma_y y)} = A_0 e^{j2\pi \mathbf{f}_0 \cdot \mathbf{r}}
$$



where $A_0 = A e^{j\phi}$ and $\mathbf{r} = (x, y)$.

### Step 2: Aperture Transmittance

Take a circular aperture of radius $a = d/2$. The transmittance is:



$$
t(\mathbf{r}) = \text{circ}\left(\frac{\|\mathbf{r}\|}{a}\right) = \begin{cases} 1, & \|\mathbf{r}\| \leq a \\ 0, & \|\mathbf{r}\| > a \end{cases}
$$



The transmitted field immediately after the aperture is:



$$
u^+(\mathbf{r}) = u^-(\mathbf{r}) \cdot t(\mathbf{r}) = A_0 e^{j2\pi \mathbf{f}_0 \cdot \mathbf{r}} \cdot t(\mathbf{r})
$$



### Step 3: Angular Spectrum Representation

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>2D Fourier Transform Convention</div>
<div class="callout-content">



$$
\mathcal{F}\{g(\mathbf{r})\}(\mathbf{f}) = \iint_{\mathbb{R}^2} g(\mathbf{r}) e^{-j2\pi \mathbf{f} \cdot \mathbf{r}} \, d^2\mathbf{r}
$$




$$
g(\mathbf{r}) = \iint_{\mathbb{R}^2} \mathcal{F}\{g\}(\mathbf{f}) e^{j2\pi \mathbf{f} \cdot \mathbf{r}} \, d^2\mathbf{f}
$$



</div>
</div>

Using the **modulation/shift property**:



$$
\mathcal{F}\{e^{j2\pi \mathbf{f}_0 \cdot \mathbf{r}} \cdot t(\mathbf{r})\}(\mathbf{f}) = T(\mathbf{f} - \mathbf{f}_0)
$$



where $T(\mathbf{f}) = \mathcal{F}\{t\}(\mathbf{f})$ is the aperture's [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/).

Therefore the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) of the transmitted field is:



$$
U^+(\mathbf{f}) = A_0 \, T(\mathbf{f} - \mathbf{f}_0)
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Key Insight</div>
<div class="callout-content">

The plane-wave factor **shifts** the aperture spectrum: the aperture's FT is centered at $\mathbf{f}_0$ (not at the origin).

</div>
</div>

### Step 4: Fourier Transform of Circular Aperture

The 2D FT of a circular aperture of radius $a$ is radially symmetric:



$$
T(\mathbf{f}) = \mathcal{F}\{t\}(\mathbf{f}) = a^2 \frac{J_1(2\pi a \rho)}{\rho}, \quad \rho = \|\mathbf{f}\|
$$



Thus:



$$
U^+(\mathbf{f}) = A_0 \, a^2 \frac{J_1(2\pi a \|\mathbf{f} - \mathbf{f}_0\|)}{\|\mathbf{f} - \mathbf{f}_0\|}
$$



The [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) is the **Airy-like radial profile centered at $\mathbf{f}_0$**.

### Step 5: Free-Space Propagation from $z_0$ to $z_1$

Propagation multiplies each spectral component by the transfer factor:



$$
H(\mathbf{f}; \Delta z) = \exp(jk_z(\mathbf{f}) \Delta z), \quad \Delta z = z_1 - z_0
$$



with:



$$
k_z(\mathbf{f}) = \sqrt{k^2 - (2\pi f_x)^2 - (2\pi f_y)^2}
$$



<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Evanescent Components</div>
<div class="callout-content">

If $|2\pi \mathbf{f}| > k$ then $k_z$ is imaginary → evanescent decay.

</div>
</div>

The propagated [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) is:



$$
U(\mathbf{f}; z_1) = U^+(\mathbf{f}) \cdot H(\mathbf{f}; \Delta z) = A_0 \, T(\mathbf{f} - \mathbf{f}_0) \, e^{jk_z(\mathbf{f}) \Delta z}
$$



### Step 6: Field at Output Plane $z = z_1$

The field is the inverse 2D FT:



$$
u(\mathbf{r}, z_1) = \iint_{\mathbb{R}^2} U(\mathbf{f}; z_1) e^{j2\pi \mathbf{f} \cdot \mathbf{r}} \, d^2\mathbf{f}
$$



Change variable $\mathbf{s} = \mathbf{f} - \mathbf{f}_0$:



$$
u(\mathbf{r}, z_1) = A_0 e^{j2\pi \mathbf{f}_0 \cdot \mathbf{r}} \iint_{\mathbb{R}^2} T(\mathbf{s}) e^{jk_z(\mathbf{s} + \mathbf{f}_0) \Delta z} e^{j2\pi \mathbf{s} \cdot \mathbf{r}} \, d^2\mathbf{s}
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Two Key Observations</div>
<div class="callout-content">

1. The prefactor $e^{j2\pi \mathbf{f}_0 \cdot \mathbf{r}} = e^{jk(\gamma_x x + \gamma_y y)}$ is the **plane-wave tilt preserved** across propagation
2. The integral contains the aperture FT multiplied by propagation phase — different spatial frequencies accumulate different phase, reshaping the transverse profile

</div>
</div>

### Step 7: Special/Limiting Cases

**Case (a): Small aperture** — If $T(\mathbf{s})$ is sharply peaked around $\mathbf{s} = 0$, approximate $k_z(\mathbf{s} + \mathbf{f}_0) \approx k_z(\mathbf{f}_0)$. The plane-wave factor acts almost like a true [eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/).

**Case (b): Fraunhofer (far-field)** — For large $\Delta z$, the field reduces to the FT of the exit pupil at scaled coordinates. The far-field intensity is $|T(\mathbf{f} - \mathbf{f}_0)|^2$ — the **[Airy disk](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/) pattern shifted by incidence angle**.

**Case (c): Evanescent components** — If $\|\mathbf{f} - \mathbf{f}_0\| > k/(2\pi)$, then $k_z$ is imaginary and that component decays as $\exp(-|\text{Im}\, k_z| \Delta z)$. High spatial frequencies (fine details) are attenuated.

### Step 8: Final Expression

<div class="callout callout-success">
<div class="callout-title"><span class="callout-icon">✅</span>Angular Spectrum Formula: Circular Aperture</div>
<div class="callout-content">



$$
u(\mathbf{r}, z_1) = A_0 e^{j2\pi \mathbf{f}_0 \cdot \mathbf{r}} \iint_{\mathbb{R}^2} \left[ a^2 \frac{J_1(2\pi a \|\mathbf{s}\|)}{\|\mathbf{s}\|} \right] e^{jk_z(\mathbf{s} + \mathbf{f}_0) \Delta z} e^{j2\pi \mathbf{s} \cdot \mathbf{r}} \, d^2\mathbf{s}
$$



where $\mathbf{s} = \mathbf{f} - \mathbf{f}_0$.

</div>
</div>

### Physics Summary

<div class="callout callout-abstract">
<div class="callout-title"><span class="callout-icon">📄</span>Key Takeaways</div>
<div class="callout-content">

- A transverse plane-wave factor $e^{jk(\gamma_x x + \gamma_y y)}$ **shifts** the aperture FT: the pattern is centered at $\mathbf{f}_0$
- Propagation **multiplies** each spectral component by $e^{jk_z \Delta z}$: this produces phase changes (and evanescent decay) that reshape the field
- In the **far field**, the pattern is the shifted FT of the aperture — for a circle, that's the **Airy pattern displaced by incidence angle**
- The plane-wave transverse factor is a **carrier**: it survives as $e^{j2\pi \mathbf{f}_0 \cdot \mathbf{r}}$ in the output, but the aperture imprint and propagation phase determine the transverse envelope

</div>
</div>

### Propagation Transfer Function

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

We know that plane waves are eigenfunctions of the free space propagation operator. Thus, each plane wave will propagate from $z_i$ to $z_e$ and still be a plane wave, multiplied by an amount $\lambda = H(\gamma_x, \gamma_y)$

</div>
</div>



$$
= \exp\left\{jk(z_e - z_i)\left[1 - \lambda^2(\xi^2 + \eta^2)\right]^{1/2}\right\}
$$



$\Rightarrow$ Thus, the resultant magnitude and phase of the plane waves at $z_e$ are given by:

## Propagation Condition



$$
\gamma_x^2 + \gamma_y^2 < 1
$$



True only when:


$$
\tilde{U}_i(\xi,\eta) \cdot H(\xi,\eta) = \tilde{U}_e(\xi,\eta) \cdot \exp\left\{jk(z_e - z_i)\left[1 - \lambda^2(\xi^2 + \eta^2)\right]\right\}
$$





$$
\Rightarrow (\lambda\xi)^2 + (\lambda\eta)^2 < 1
$$





$$
\xi^2 + \eta^2 < \frac{1}{\lambda^2}
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

Note: This means that amplitudes of all plane waves is preserved. Only the phase is changed due to path length differences.

</div>
</div>

$\Rightarrow$ Finally, the amplitude distribution at $z_e$ can be calculated by an inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):



$$
u_e(x,y) = \mathcal{F}^{-1}\left\{\tilde{U}_i(\xi,\eta) \cdot H(\xi,\eta)\right\}
$$





$$
= \iint_{-\infty}^{\infty} \tilde{U}_i(\xi,\eta) \exp\left\{jk(z_e - z_i)\left[1 - \lambda^2(\xi^2 + \eta^2)\right]^{1/2}\right\} e^{+j\pi(\xi x + \eta y)} d\xi d\eta
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Free-Space Propagation as an LSI Filter</div>
<div class="callout-content">

This angular spectrum formulation has exactly the same structure as a 1D linear filter:

| Domain | 1D Signal Processing | 2D Optical Propagation |
|--------|---------------------|----------------------|
| Spatial | $f(x) \to h(x) \to g(x) = f * h$ | $u_i(x,y) \to h(x,y) \to u_o(x,y) = u_i * h$ |
| Frequency | $G(\xi) = F(\xi) \cdot H(\xi)$ | $U_o(\xi,\eta) = U_i(\xi,\eta) \cdot H(\xi,\eta)$ |

Free-space propagation is a **linear shift-invariant system** with transfer function $H(\xi,\eta) = \exp\{jk\Delta z[1 - \lambda^2(\xi^2+\eta^2)]^{1/2}\}$. The same convolution/multiplication duality applies.

</div>
</div>
# Diffraction as a Linear Shift-Invariant System



$$
\frac{u_i(x,y)}{\tilde{U}_i(\xi,\eta)} \xrightarrow{\boxed{\text{Free Space Propagation } H(\xi,\eta)}} \frac{u_e(x,y)}{\tilde{U}_e(\xi,\eta) = \tilde{U}_i(x,y) \cdot H(\xi,\eta)}
$$



**[Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) from plane $z_i$ to plane $z_e$**

## Similarity Between 1-dim and 2-dim Fourier Synthesis

**One dim:**


$$
f(t) \rightarrow \boxed{\quad} \rightarrow \text{sinusoid}
$$



**Two dim:**
- No $y$ dependence: $e^{j\pi\gamma_x x}$ gives different phases of the [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/)
- $\gamma_x$ = effective phase change in x direction (equivalent to frequency of complex sinusoid)

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

Note: A single plane wave, measured in the $z_i$ plane looks like a single complex sinusoid in x and y.
This is a little different than 1-dim. Time, a single complex exponential corresponds to propagation, but here it corresponds to angle of travel.

</div>
</div>



$$
\cos(\cos^{-1}(\gamma_x)) = \frac{\lambda}{\lambda_x} = \gamma_x, \quad \text{or} \quad \lambda_x = \frac{\lambda}{\gamma_x} = \frac{\lambda}{\cos\theta}
$$



## Square Wave Aperture (One-dim case)

Now, synthesis of a square aperture is identical to one-dim case:



$$
f(x,y) \xrightarrow{H(x,y)} g(x,y)
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

A plane wave is of infinite extent - luckily, only a finite addition. To the delta in $x$ times $y$ shows a/binomial). This is exactly what a lens does: it form a "rectangle"

</div>
</div>
# Simple Example of Angular Plane Wave Decomposition

## Sine Wave Grating



$$
u_i(x,y) = \cos(2\pi f_0 x)
$$



### Angular plane wave spectrum:



$$
\tilde{U}_i(\xi,\eta) = \iint u_i(x,y) e^{-j\pi(\xi x + \eta y)} \, dx \, dy
$$





$$
= \frac{1}{2}\left[\delta(\xi - f_0) + \delta(\xi + f_0)\right] \delta(\eta)
$$



where $\gamma_x = \lambda\xi$, $\gamma_y = \lambda\eta$

Physically, this corresponds to **2 plane waves** at angles $\cos^{-1}(f_0\lambda)$ and $\cos^{-1}(-f_0\lambda)$ in x direction, and angles $\cos^{-1}(0\lambda)$ in y direction (i.e., perpendicular to y).



$$
\alpha = \cos^{-1}(f_0\lambda) \quad \text{or} \quad \gamma_x = f_0\lambda
$$




$$
\beta = \cos^{-1}(-f_0\lambda) \quad \text{or} \quad \gamma_x = -f_0\lambda
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Coordinate Convention</div>
<div class="callout-content">

In this 2D cross-section, the $y$-axis points out of the page (perpendicular to the diagram). The two plane waves propagate in the $x$-$z$ plane, symmetric about the $z$-axis. Their $k$-vectors have no $y$-component ($\gamma_y = 0$), so $\eta = 0$ in frequency space.

</div>
</div>

## Interference Pattern

But we know from physics I that the interference of two plane waves creates a sinusoidal interference pattern!



$$
\frac{1}{2}e^{jk_x x} + \frac{1}{2}e^{-jk_x x} = \cos(k_x x) = \cos(|k|\gamma_x x)
$$





$$
= \cos\left(\frac{2\pi}{\lambda}(f_0\lambda)x\right) = \cos(2\pi f_0 x)
$$


# Returning to Diffraction Formula

We have:



$$
\tilde{U}_e(\xi,\eta) = \tilde{U}_i(\xi,\eta) \cdot H(\xi,\eta)
$$



where:


$$
\tilde{U}_e(\xi,\eta) = \iint u_e(x,y) e^{-j2\pi(\xi x + \eta y)} \, dx \, dy
$$





$$
\tilde{U}_i(\xi,\eta) = \iint u_i(x,y) e^{-j2\pi(\xi x + \eta y)} \, dx \, dy
$$





$$
H(\xi,\eta) = \exp\left\{jk(z_e - z_i)\left[1 - \lambda^2(\xi^2 + \eta^2)\right]^{1/2}\right\}
$$



where $\gamma_x = \lambda\xi$, $\gamma_y = \lambda\eta$

$\Rightarrow$ We should be able to write this in a [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) form by using the [convolution theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/):



$$
\Rightarrow u_e(x,y) = u_i(x,y) ** \mathcal{F}^{-1}\{H(\xi,\eta)\}
$$



## Fresnel Approximation

This is the **[Fresnel](/notes/areas/electrical_engineering/physical_optics/definitions/fresnel_diffraction/) Approach**. However, to simplify things, we first restrict the angular plane waves to small angles ($\gamma_x \ll 1$, $\gamma_y \ll 1$):



$$
\Rightarrow \lambda^2\xi^2 \ll 1 \quad \text{and} \quad \lambda^2\eta^2 \ll 1
$$



$\therefore$ Using the binomial expansion $(1-a)^{1/2} \approx 1 - \frac{a}{2}$

we have:



$$
H(\xi,\eta) \approx \exp\left\{jk(z_e - z_i)\left[1 - \frac{\lambda^2}{2}(\xi^2 + \eta^2)\right]\right\}
$$





$$
= \exp\{jk(z_e - z_i)\} \exp\{-j\pi\lambda(z_e - z_i)(\xi^2 + \eta^2)\}
$$



We now need to calculate $h(x,y)$ by inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):



$$
\mathcal{F}_\xi^{-1}\mathcal{F}_\eta^{-1}\left\{\exp\left[-j\pi\lambda(z_e - z_i)(\xi^2 + \eta^2)\right]\right\}
$$





$$
= \mathcal{F}_\xi^{-1}\left\{\exp\left[-j\pi\lambda(z_e - z_i)\xi^2\right]\right\} \cdot \mathcal{F}_\eta^{-1}\left\{\exp\left[-j\pi\lambda(z_e - z_i)\eta^2\right]\right\}
$$



But $\exp\left[-j\pi\lambda(z_e - z_i)\xi^2\right] = \text{Gaus}(a\xi)$

where $a = \sqrt{j\lambda(z_e - z_i)}$

and $\text{Gaus}(\xi) = \exp(-\pi\xi^2)$
# Fresnel Diffraction Formula

And $\mathcal{F}^{-1}\{\text{Gaus}(a\xi)\} = \frac{1}{|a|} \text{Gaus}\left(\frac{x}{a}\right)$

Recall Gaussian problem 2.4d: $\mathcal{B}\{e^{-\pi\xi^2}\} = e^{-\pi\xi^2}$



$$
\therefore \mathcal{F}^{-1}\left\{\exp\left[-j\pi\lambda(z_e - z_i)\xi^2\right]\right\}
$$





$$
= \frac{1}{\sqrt{j\lambda(z_e - z_i)}} \exp\left[-\frac{\pi x^2}{j\lambda(z_e - z_i)}\right]
$$



and $\mathcal{F}^{-1}\mathcal{F}^{-1}\left\{\exp\left[-j\pi\lambda(z_e - z_i)(\xi^2 + \eta^2)\right]\right\}$



$$
= \frac{1}{j\lambda(z_e - z_i)} \exp\left[\frac{j\pi(x^2 + y^2)}{\lambda(z_e - z_i)}\right]
$$



Finally, $\mathcal{F}^{-1}\mathcal{F}^{-1}\{H(\xi,\eta)\} = \frac{\exp\{jk(z_e - z_i)\}}{j\lambda(z_e - z_i)} \exp\left[\frac{j\pi(x^2 + y^2)}{\lambda(z_e - z_i)}\right]$

We thus have the [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) form (with $\frac{\pi}{\lambda} = \frac{k}{2}$):



$$
\boxed{u_e(x,y) = u_i(x,y) ** \frac{\exp\{jk(z_e - z_i)\}}{j\lambda(z_e - z_i)} \exp\left[\frac{jk(x^2 + y^2)}{2(z_e - z_i)}\right]}
$$





$$
= \frac{\exp\{jk(z_e - z_i)\}}{j\lambda(z_e - z_i)} \iint u_i(\alpha,\beta) \exp\left\{\frac{jk[(x-\alpha)^2 + (y-\beta)^2]}{2(z_e - z_i)}\right\} d\alpha d\beta
$$



**Fresnel Formula** (Angular Approximation / Fresnel Formula)

---

## Huygens' Principle

*(Tie long awaited)*

Recall from first quarter that Huygens' principle stated that any field distribution could be thought of as a [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) of spherical waves:



$$
= \sum \text{superposition}
$$


# Mathematical Statement of Huygens' Principle



$$
u_e(x_2, y_2) = \iint u_i(x_1, y_1) \frac{\exp(jkr)}{j\lambda r} \, dx_1 dy_1
$$



where $\exp\left(\frac{jkr}{j\lambda r}\right)$ is a spherical wave (multiplied by $\frac{1}{j\lambda}$)

**Source of spherical waves in $x_1, y_1$**



$$
r = \sqrt{(z_e - z_i)^2 + (x_1 - x_2)^2 + (y_1 - y_2)^2}
$$





$$
r = (z_e - z_i)\sqrt{1 + \frac{(x_1 - x_2)^2 + (y_1 - y_2)^2}{(z_e - z_i)^2}}
$$



## Approximations

### (1) Fresnel Approximation
As before, we limit the observations to regions where:


$$
(z_e - z_i) >> |x_1 - x_2| \quad \text{and} \quad (z_e - z_i) >> |y_1 - y_2|
$$



### (2) $\frac{1}{r}$ Approximation
Then the binomial expansion for $r$ gives:



$$
r = (z_e - z_i) + \frac{1}{2(z_e - z_i)}\left[(x_1 - x_2)^2 + (y_1 - y_2)^2\right]
$$



**Use this approximation for exponential**

### (3) We also approximate $r \approx (z_e - z_i)$ in denominator of spherical wave. Reason: $\frac{1}{r} \approx \frac{1}{z_e - z_i}$, but we cannot use $\exp(jkr) \approx \exp(jkz)$ because $k$ may be large and this may cause the exponential to change from +1 to -1.
# Proper Approximation for Huygens' Principle

The proper approximation becomes:



$$
u_e(x_2, y_2) = \iint u_i(x_1, y_1) \frac{\exp\left\{jk\left[(z_e - z_i) + \frac{1}{2(z_e - z_i)}(x_1 - x_2)^2 + (y_1 - y_2)^2\right]\right\}}{j\lambda(z_e - z_i)} \, dx_1 dy_1
$$





$$
\boxed{= \frac{\exp\{jk(z_e - z_i)\}}{j\lambda(z_e - z_i)} \iint u_i(x_1, y_1) \exp\left[\frac{jk}{2(z_e - z_i)}\left((x_1 - x_2)^2 + (y_1 - y_2)^2\right)\right] dx_1 dy_1}
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Term-by-Term Physical Interpretation</div>
<div class="callout-content">

**$u_e(x_2, y_2)$ — Output field.** The complex optical field at the observation plane. Contains both amplitude and phase; intensity is $|u_e|^2$.

**$u_i(x_1, y_1)$ — Input field.** The field in the source/aperture plane. Encodes aperture shape, object transmission, phase masks, etc. Every point $(x_1, y_1)$ acts as a secondary radiator (Huygens).

**$\iint dx_1\, dy_1$ — Superposition.** Every point in the input plane contributes to every point in the output plane. Diffraction is nonlocal — no ray tracing here. The output is the coherent sum of all secondary waves. This is where interference comes from.

**$\exp\{jk(z_e - z_i)\}$ — Carrier phase.** A global phase advance corresponding to plane-wave propagation over distance $z_e - z_i$. Same for all $(x_2, y_2)$. Does not affect intensity, but matters if this field interferes with another.

**$\dfrac{1}{j\lambda(z_e - z_i)}$ — Amplitude scaling.** $1/(z_e - z_i)$: spherical wave spreading (inverse square law for intensity). $1/\lambda$: normalization of the Huygens-Fresnel kernel (arises from $k = 2\pi/\lambda$). $j$: enforces the correct phase convention. Together these ensure energy conservation.

**$\exp\!\left[\dfrac{jk}{2(z_e - z_i)}\left((x_1 - x_2)^2 + (y_1 - y_2)^2\right)\right]$ — Quadratic phase kernel (the heart of Fresnel diffraction).**
- Represents the extra path length from $(x_1, y_1)$ to $(x_2, y_2)$, retained to second order (paraxial approximation)
- Introduces position-dependent phase delays → constructive/destructive interference → diffraction fringes and Fresnel zones
- Quadratic because off-axis rays travel slightly farther: $R \approx (z_e - z_i) + \frac{(x_2 - x_1)^2 + (y_2 - y_1)^2}{2(z_e - z_i)}$
- This is where wave optics departs from ray optics

**Structural meaning:** Propagation = [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) with a quadratic-phase kernel. Free-space propagation is a linear shift-invariant system whose [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) is a chirped spherical wave. This is why lenses cancel quadratic phase, and why Fresnel diffraction becomes Fourier optics in the far field.

**One-line intuition:** Every point in the input plane emits a spherical wave; the output field is the coherent sum of those waves, with phase delays determined by geometry and wavelength.

</div>
</div>

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

Note: This is **exactly** the results obtained from our previous analysis using angular (plane wave decomposition). Thus, the diffraction effect can apparently be described by considering the effect at $z_e$ to be the superposition of spherical waves $\frac{\exp(jkr)}{j\lambda r}$ at $z_i$, weighted by the field distribution at $z_i$. This is **Huygens' Principle**.

</div>
</div>
# Criterion for Validity of Fresnel Approximation

**Homework:** Goodman: 4-5, 4-7; Cathey: 1-3

*(or quadratic form of Huygens' Principle)*

$\Rightarrow$ Recall: Fresnel approximation was good for "small" angular plane waves: $\gamma_x \ll 1$, $\gamma_y \ll 1$

$\Rightarrow$ Specifically, approximations were (for Huygens' development):

## i) $\frac{1}{r} \approx \frac{1}{(z_e - z_i)}$

### ii) $\exp[jkr] \approx \exp\left\{jk\left[(z_e - z_i) + \frac{(x_1 - x_2)^2 + (y_1 - y_2)^2}{2(z_e - z_i)}\right]\right\}$

For i) to be true, we require:


$$
(z_e - z_i) >> |x_1 - x_2|
$$


and


$$
(z_e - z_i) >> |y_1 - y_2|
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

Since $\theta \approx \frac{|x_1 - x_2|}{z_e - z_i}$, requiring $(z_e - z_i) \gg |x_1 - x_2|$ is equivalent to requiring $\theta \ll 1$ — the paraxial (small-angle) condition.

</div>
</div>

For ii) to be true, we require the next term in the binomial expansion to be insignificant:



$$
r = \left[(z_e - z_i)^2 + (x_1 - x_2)^2 + (y_1 - y_2)^2\right]^{1/2} = (z_e - z_i)\left\{1 + \frac{(x_1 - x_2)^2 + (y_1 - y_2)^2}{(z_e - z_i)^2}\right\}^{1/2}
$$





$$
\exp(jkr) = \exp\left\{jk(z_e - z_i)\left[1 + \frac{(x_1 - x_2)^2 + (y_1 - y_2)^2}{2(z_e - z_i)^2} - \frac{[(x_1-x_2)^2 + (y_1-y_2)^2]^2}{8(z_e - z_i)^4} + \cdots\right]\right\}
$$



<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Warning</div>
<div class="callout-content">

The Fresnel approximation keeps only the first two terms (constant + quadratic). For this to be valid, the next term — the fourth-order correction $\frac{[(x_1-x_2)^2 + (y_1-y_2)^2]^2}{8(z_e-z_i)^4}$ — must contribute negligible phase, i.e., its contribution $k(z_e - z_i) \times (\text{fourth-order term})$ must be $\ll 1$ radian. This is quantified by the Fresnel condition below.

</div>
</div>
# Fresnel Condition

In order to neglect third term in expansion, we must have:



$$
\frac{k(z_e - z_i)\left[(x_1 - x_2)^2 + (y_1 - y_2)^2\right]^2}{8(z_e - z_i)^4} \ll 1
$$





$$
\boxed{(z_e - z_i)^3 >> \frac{\pi}{4\lambda}\left[(x_1 - x_2)^2 + (y_1 - y_2)^2\right]^2_{\text{max}}}
$$



**This is a sufficient Fresnel Condition**

(It may not actually be necessary)

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Big-Picture Interpretation: Why the Fresnel Approximation Works</div>
<div class="callout-content">

**What this section proved:** It is okay to replace a spherical wave with a quadratic phase — because the error is small.

The exact distance $R$ between input and output points involves a square root. Factoring out the propagation distance gives $R = (z_e - z_i)\sqrt{1 + \varepsilon}$, where:



$$
\varepsilon = \frac{(x_1 - x_2)^2 + (y_1 - y_2)^2}{(z_e - z_i)^2}
$$



The binomial expansion $(1+\varepsilon)^{1/2} = 1 + \frac{1}{2}\varepsilon - \frac{1}{8}\varepsilon^2 + \cdots$ then gives:



$$
R \approx (z_e - z_i) + \frac{(x_1 - x_2)^2 + (y_1 - y_2)^2}{2(z_e - z_i)} - \frac{\left[(x_1 - x_2)^2 + (y_1 - y_2)^2\right]^2}{8(z_e - z_i)^3} + \cdots
$$



Inside $\exp(jkR)$, each term plays a distinct role:

| Term | Role |
|------|------|
| Constant $(z_e - z_i)$ | Carrier phase |
| Quadratic | Fresnel diffraction kernel |
| Fourth-order and above | Small corrections (dropped) |

**Why "small" means small:** The neglected fourth-order term contributes phase $k(z_e - z_i) \times \varepsilon^2/8$. The Fresnel condition above guarantees this is $\ll 1$ radian — too small to shift interference fringes.

**Physical conditions for $\varepsilon \ll 1$:** Narrow apertures, long propagation distances, small diffraction angles — the paraxial regime.

**Hierarchy of approximations:**

| Approximation | Terms kept | Result |
|---------------|-----------|--------|
| Exact | All terms | Rayleigh–Sommerfeld |
| Fresnel | Up to quadratic | Near-field diffraction |
| Fraunhofer | Linearized phase | Far-field / Fourier transform |

**One-sentence intuition:** You're approximating a sphere by a paraboloid — and the Fresnel condition proves the error is small.

</div>
</div>

## Two Forms for the Fresnel Diffraction Formula

From here on, let $z$ simply be the distance between observation plane and aperture, i.e., $z = (z_e - z_i)$

### Convolution Form



$$
U_2(x,y) = \frac{e^{jkz}}{j\lambda z} \iint U_1(\alpha,\beta)\, \exp\!\left[jk\frac{(x-\alpha)^2 + (y-\beta)^2}{2z}\right] d\alpha\, d\beta
$$





$$
U_2(x,y) = \frac{e^{jkz}}{j\lambda z} \bigl[U_1 * h\bigr](x,y), \quad h(x,y) = \exp\!\left[jk\frac{x^2+y^2}{2z}\right]
$$



**[Transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):**



$$
H(\xi,\eta) = \exp[jkz] \exp[-j\pi\lambda z(\xi^2 + \eta^2)]
$$



By expanding out the quadratic phase in the integral and factoring, we arrive at a second form:

---

### Fourier Transform Form (Quadratic-Phase / Fourier Form)



$$
U_2(x,y) = \frac{e^{jkz}}{j\lambda z} \exp\!\left[jk\frac{x^2+y^2}{2z}\right] \iint U_1(\alpha,\beta)\, \exp\!\left[jk\frac{\alpha^2+\beta^2}{2z}\right] \exp\!\left[-j\frac{2\pi}{\lambda z}(x\alpha+y\beta)\right] d\alpha\, d\beta
$$



Recognizing the remaining exponential as the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) kernel, this can be written compactly as:



$$
U_2(x,y) = \frac{e^{jkz}}{j\lambda z} \exp\!\left[jk\frac{x^2+y^2}{2z}\right] \mathcal{F}\!\left\{U_1(\alpha,\beta)\, \exp\!\left[jk\frac{\alpha^2+\beta^2}{2z}\right]\right\}\Bigg|_{f_x = \frac{x}{\lambda z},\; f_y = \frac{y}{\lambda z}}
$$



where the 2D Fourier transform is:



$$
\mathcal{F}\{g(\alpha,\beta)\}(f_x,f_y) = \iint g(\alpha,\beta)\, e^{-j2\pi(f_x\alpha + f_y\beta)}\, d\alpha\, d\beta
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

The first form writes Fresnel diffraction as a [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) with a quadratic-phase [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) $h(x,y)$, showing free-space propagation is a linear shift-invariant system. The second form factors the quadratic phase to reveal a scaled [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of a chirp-modulated input field. The spatial frequencies $f_x, f_y$ correspond to observation-plane coordinates via $f_x = x/(\lambda z)$, revealing the direct connection between free-space propagation and Fourier optics — and leading directly to the Fraunhofer (far-field) limit.

</div>
</div>
# Fraunhofer Diffraction Formula (Far Field)

Note that this equation can be thought of as some phase factors multiplying the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the aperture transmittance and a quadratic phase factor $\exp\left\{\frac{jk[\alpha^2+\beta^2]}{2z}\right\}$

## Fraunhofer Diffraction Formula (Far Field)

In the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) form of the [Fresnel diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/fresnel_diffraction/) formula, the input field $U_1(\alpha,\beta)$ is multiplied by a quadratic-phase chirp factor $\exp\{jk(\alpha^2+\beta^2)/2z\}$ before being Fourier transformed. This chirp encodes the curvature of the Fresnel kernel — it's what makes near-field diffraction different from a pure Fourier transform.

If the propagation distance $z$ is large enough, the phase variation of this chirp across the entire aperture becomes negligible, and the exponential can be replaced by unity:



$$
\exp\left\{\frac{jk[\alpha^2+\beta^2]}{2z}\right\} \approx 1
$$



This requires:



$$
\frac{k(\alpha^2+\beta^2)}{2z} \ll 1 \quad \text{for all } \alpha, \beta \text{ in the diffracting aperture}
$$





$$
\Rightarrow \boxed{z >> \frac{k(\alpha^2+\beta^2)_{\text{max}}}{2}}
$$



**Fraunhofer Condition**

For an input aperture of radius $a$, the maximum phase variation of the chirp factor is:



$$
\Delta\phi = k\frac{a^2}{2z} = \pi\frac{a^2}{\lambda z}
$$



Requiring $\Delta\phi \ll 1$ gives the equivalent condition:



$$
\boxed{\frac{a^2}{\lambda z} \ll 1}
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

The quantity $a^2/\lambda z$ is the **Fresnel number**. In the small Fresnel number limit, the chirp factor drops out and Fresnel diffraction reduces to Fraunhofer diffraction — the field becomes proportional to the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the input.

</div>
</div>

Under this condition, the quadratic phase term in the **input plane** is negligible, so the Fresnel diffraction equation reduces to:



$$
\boxed{U_2(x,y) = \frac{e^{jkz}}{j\lambda z} \exp\!\left[jk\frac{x^2+y^2}{2z}\right] \iint U_1(\alpha,\beta)\, \exp\!\left[-j\frac{2\pi}{\lambda z}(x\alpha + y\beta)\right] d\alpha\, d\beta}
$$



Recognizing the [Fourier](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) kernel, this may be written as:



$$
U_2(x,y) = \frac{e^{jkz}}{j\lambda z} \exp\!\left[jk\frac{x^2+y^2}{2z}\right] \mathcal{F}\{U_1(\alpha,\beta)\}\bigg|_{f_x = \frac{x}{\lambda z},\; f_y = \frac{y}{\lambda z}}
$$



**[Fraunhofer Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/fraunhofer_diffraction/) Formula**

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

This is the **Fraunhofer approximation** (far-field diffraction). The observation-plane coordinates map directly to spatial frequencies via $f_x = x/(\lambda z)$ and $f_y = y/(\lambda z)$, revealing diffraction as Fourier analysis — the far-field pattern is the Fourier transform of the aperture.

</div>
</div>
# Intensity in Fraunhofer Diffraction

$\Rightarrow$ $u_e(x,y)$ is the complex electric field at plane $z_e$

$\Rightarrow$ Most detectors of light (film, eye, photodiode) are only capable of measuring **power**

$\Rightarrow$ We define the **intensity** (power/unit area) as:



$$
I_e(x,y) = u_e(x,y) \cdot u_e^*(x,y)
$$



$\Rightarrow$ Extremely simple [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) formula in Fraunhofer region:



$$
I_e(x,y) = \left| \frac{\exp(jkz)}{j\lambda z} \exp\left\{\frac{jk(x^2+y^2)}{2z}\right\} \mathcal{F}\{u_i(\alpha,\beta)\}\right|^2
$$





$$
= \frac{1}{(\lambda z)^2} \left| \mathcal{F}\{u_i(\alpha,\beta)\}\bigg|_{\xi=\frac{x}{\lambda z}, \eta=\frac{y}{\lambda z}} \right|^2
$$



Or simply, the **intensity pattern** (as seen by eye, etc.) is the **squared magnitude of the two-dim [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)** (scaled by $\frac{1}{\lambda z}$).



$$
\text{Inverse Square Law}
$$



<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Why Intensity = Squared Fourier Transform</div>
<div class="callout-content">

**Why intensity, not field?** Detectors (film, eye, photodiode) measure power, not phase. Phase information disappears unless you interfere fields. So the measurable quantity is $I = |U|^2$.

**Why the phase terms cancel:** Substituting the Fraunhofer field into $I = U_2 \cdot U_2^*$, the exponential phase factors $e^{jkz}$ and $e^{jk(x^2+y^2)/2z}$ have unit magnitude and cancel in the product, leaving only the magnitude of the Fourier transform.

**The prefactor $1/\lambda^2 z^2$:** This comes from $|1/(j\lambda z)|^2$. The $1/z^2$ is geometric spreading (inverse square law); the $1/\lambda^2$ is the Huygens-Fresnel normalization. It affects brightness, not pattern shape.

**The punchline:** Fraunhofer diffraction intensity is the squared magnitude of the Fourier transform of the aperture field. This is the central result of Fourier optics — aperture shape determines the diffraction pattern:
- Slits → $\mathrm{sinc}^2$
- Gratings → comb spectra
- Circular apertures → [Airy disk](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/)

This is the equation that turns optics into Fourier analysis.

</div>
</div>
# Fraunhofer Condition

The Fraunhofer condition is fairly severe:



$$
z >> \frac{k(\alpha^2 + \beta^2)_{\text{max}}}{2} = \frac{\pi(\alpha^2 + \beta^2)_{\text{max}}}{\lambda}
$$



<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Example</div>
<div class="callout-content">

He-Ne laser (red): $\lambda \approx 6 \times 10^{-7}$ m ($k = \frac{2\pi}{\lambda}$)

Aperture = $2.5 \times 2.5$ cm

$\Rightarrow z >> 1,600$ meters

</div>
</div>

Nevertheless, it is often a useful approximation.

## Transfer Functions Associated with Approximations



$$
H(\xi,\eta) = \exp\left\{jkz\left[1 - \lambda^2(\xi^2+\eta^2)\right]^{1/2}\right\}
$$

 — **No approximation**



$$
H_F(\xi,\eta) \cong \exp\left\{jkz\left[1 - \frac{\lambda^2}{2}(\xi^2+\eta^2)\right]\right\}
$$

 — **Fresnel Approximation**

$H_F(\xi,\eta) \rightarrow$ does not exist, because the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) operator is not shift [invariant](/notes/areas/mathematics/abstract_algebra/definitions/invariant/) and thus has no [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) associated with it.

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Warning</div>
<div class="callout-content">

However, the Fraunhofer region can be thought of as a limit of the Fresnel region, which does have a transfer function associated with Fresnel diffraction (i.e., the Fresnel equations are obviously good in the Fraunhofer region, and the transfer function associated with Fresnel diffraction can be used).

</div>
</div>
# Example of Fraunhofer Diffraction - Microwave Antenna

## Microwave Antenna (Transmitter)

**Setup:**
- $\lambda = 1$ mm
- $d = 1$ meter
- $z = 10$ km

**Question:** How much power will be received by the receiving antenna?

## Equivalent Set-up



$$
u^i(x,y) = A \cdot \text{circ}\left(\frac{r}{d/2}\right)
$$



where $r$ = radius

## Fraunhofer Condition



$$
z >> \frac{k(\alpha^2 + \beta^2)_{\text{max}}}{2} = \frac{\pi r^2}{\lambda}
$$





$$
z >> \frac{\pi(0.5)^2}{10^{-3}} = 750 \text{ m}
$$



$\therefore z = 10$ km is in the Fraunhofer region

## Intensity Pattern



$$
I_e(x,y) = \frac{1}{(\lambda z)^2} \left| \mathcal{F}\mathcal{F}\left\{A \cdot \text{circ}\left(\frac{r}{d/2}\right)\right\}\right|^2_{\xi=\frac{x}{\lambda z}, \eta=\frac{y}{\lambda z}}
$$





$$
= \frac{1}{(\lambda z)^2} \left| \frac{A\pi d^2}{4} \text{somb}\left(\frac{d\rho}{\lambda z}\right) \right|^2
$$



or:



$$
= \frac{1}{(\lambda z)^2} \left| \frac{Ad}{2} \frac{J_1(\pi d\rho/\lambda z)}{\rho/\lambda z} \right|^2
$$



where $\rho = \sqrt{x^2 + y^2}$

# Fraunhofer Diffraction - Airy Pattern

The intensity pattern follows a sombrero function:



$$
\text{somb}\left(\frac{d\rho}{\lambda z}\right) = \frac{2J_1\left(\frac{\pi d\rho}{\lambda z}\right)}{\frac{\pi d\rho}{\lambda z}}
$$



and $J_1(\pi)(1.22) = 0$

$\therefore$ Zero of [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/) is at:



$$
\frac{d\rho_1}{\lambda z} = 1.22
$$





$$
\rho_1 = \frac{(1.22)\lambda z}{d}
$$





$$
= \frac{(1.22)(10^{-3})(10^4)}{1} = 12.2 \text{ m}
$$



## Form of Result

From $\rho = 1.22 \frac{\lambda z}{d}$

and $\frac{\rho}{z} \approx \sin\theta$

we have:



$$
\boxed{\sin\theta = 1.22 \frac{\lambda}{d}}
$$



**Very Important Equation**

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

$\rho_1$ = radius of main lobe

</div>
</div>
# Far Field Diffraction from Square Aperture

For a square aperture, the result is almost the same:



$$
\text{rect}\left(\frac{x'}{d}, \frac{y'}{d}\right) \xrightarrow{z} I \propto \left| d^2 \text{sinc}\left(\frac{dx'}{\lambda z}, \frac{dy'}{\lambda z}\right) \right|^2
$$





$$
\text{sinc}(1) = 0
$$





$$
\Rightarrow \frac{da}{\lambda z} = 1, \text{ or } a = \frac{\lambda z}{d}
$$



But $\frac{a}{z} = \sin\theta$



$$
\therefore \boxed{\sin\theta = \frac{\lambda}{d}}
$$



Thus we see a general result:



$$
\boxed{\sin\theta = K\frac{\lambda}{d}}
$$



**Far Field [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) from an Aperture**

where $K$ is a value close to 1, and is dependent on the shape of the aperture.

| Aperture | K |
|----------|---|
| Square | $K = 1$ |
| Circle | $K = 1.22$ |
# Notice Effect of Rectangular Antennas

## Rectangular Antenna Pattern

An antenna with a rectangular shape such as shown has less broadening of the beam in the horizontal direction ($\theta$) than the vertical direction ($\phi$).



$$
\sin\theta = \frac{\lambda}{d_1}, \quad \sin\phi = \frac{\lambda}{d_2}
$$



$\therefore$ An antenna with a rectangular shape such as above has less broadening of the beam in the horizontal direction ($\theta$) than the vertical direction ($\phi$).

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Radar Application</div>
<div class="callout-content">

Objects for radar antenna to detect are shown in the beam pattern.

</div>
</div>

## Resolution Considerations

Consider a radar antenna that tries to locate an object by rotating with beam "illuminates" object.

Two objects can be distinguished separately only if beam is narrow. A broad antenna has better resolution in horizontal direction than vertical direction.
# Diffraction Grating (Absorption Type)

## Setup

Frequency of grating in $x$ is $\frac{1}{T} = f_0$

The depth of modulation is represented by $m$ where $0 < m \leq 1$.



$$
u_i^-(x,y) = A
$$





$$
t(x,y) = \left[\frac{1}{2} + \frac{m}{2}\cos(2\pi f_0 x)\right] \text{rect}\left(\frac{x}{\ell}\right) \text{rect}\left(\frac{y}{\ell}\right)
$$





$$
\therefore u_i^+(x,y) = A\left[\frac{1}{2} + \frac{m}{2}\cos(2\pi f_0 x)\right] \text{rect}\left(\frac{x}{\ell}\right) \text{rect}\left(\frac{y}{\ell}\right)
$$



## Far Field Calculation

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Delta Functions in the Angular Spectrum</div>
<div class="callout-content">

The transmitted field contains discrete plane wave components (constant term plus two diffracted orders at $\pm f_0$). In frequency space, discrete components appear as **delta functions** — each delta represents a plane wave at that spatial frequency.

The convolution with $\text{sinc}(\ell\xi)\text{sinc}(\ell\eta)$ spreads each delta into a sinc pattern, reflecting the finite aperture size $\ell$. Without the finite aperture, the far-field would consist of three infinitely sharp spots.

</div>
</div>



$$
\mathcal{FF}\{u_i^+(x,y)\} = A\left[\frac{1}{2}\delta(\xi,\eta) + \frac{m}{4}\delta(\xi+f_0,\eta) + \frac{m}{4}\delta(\xi-f_0,\eta)\right] ** \ell^2 \text{sinc}(\ell\xi)\text{sinc}(\ell\eta)
$$





$$
= \frac{A\ell^2}{2}\text{sinc}(\ell\eta)\left[\text{sinc}(\ell\xi) + \frac{m}{2}\text{sinc}(\ell(\xi+f_0)) + \frac{m}{2}\text{sinc}(\ell(\xi-f_0))\right]
$$



## Output Field



$$
u_e(x',y') = \frac{A\ell^2}{j\lambda z}\exp(jkz)\exp\left(j\frac{k(x'^2+y'^2)}{2z}\right)\text{sinc}\left(\frac{\ell y'}{\lambda z}\right)\left\{\text{sinc}\left(\frac{\ell x'}{\lambda z}\right) + \frac{m}{2}\text{sinc}\left[\frac{\ell}{\lambda z}(x'+\lambda z f_0)\right] + \frac{m}{2}\text{sinc}\left[\frac{\ell}{\lambda z}(x'-\lambda z f_0)\right]\right\}
$$



The intensity pattern shows peaks at $x' = 0$, $x' = \pm f_0\lambda z$, with width $\frac{\ell x'}{\lambda z} = 1 \Rightarrow x' = \frac{\lambda z}{\ell}$.
# Diffraction Grating - Resolution Analysis

## Key Observations

**Note:**
1. Distance from origin to first zero of [sinc function](/notes/areas/electrical_engineering/signals_systems/definitions/sinc_function/) $= \frac{\lambda z}{\ell}$
2. Distance to next [sinc function](/notes/areas/electrical_engineering/signals_systems/definitions/sinc_function/) $= f_0\lambda z = \frac{\lambda z}{T}$

Since $f_0 = \frac{1}{T}$:



$$
\therefore \text{If } T << \ell,
$$





$$
\frac{\lambda z}{\ell} << \frac{\lambda z}{T} \text{ and the overlap of sinc functions is small.}
$$



## Intensity Pattern



$$
I_e(x,y) \propto \frac{A^2\ell^4}{4\lambda^2 z^2}\text{sinc}^2\left(\frac{\ell y}{\lambda z}\right)\left\{\text{sinc}^2\left(\frac{\ell x}{\lambda z}\right) + \frac{m^2}{4}\text{sinc}^2\left[\frac{\ell}{\lambda z}(x'+\lambda z f_0)\right] + \frac{m^2}{4}\text{sinc}^2\left[\frac{\ell}{\lambda z}(x'-\lambda z f_0)\right]\right\}
$$



## Diffraction Orders

The position of the $\pm 1$ order components $= f_0\lambda z$

This device can be used to disperse white light into colors.

- The width of each order is $\frac{\lambda z}{\ell}$
- The spatial separation is $f_0\lambda z$



$$
\text{Total number of resolvable wavelengths} = \frac{(f_0\lambda z)}{\lambda z/\ell} = f_0\ell = \frac{\ell}{T}
$$





$$
= \text{number of cycles of sinc function (lines in grating)}
$$



## Spectral Resolution

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

Resolution of a grating is not a function of slit size or line spacing, but only of the **number of lines**.

This is sometimes called the **space-bandwidth product**.

</div>
</div>
# Diffraction Grating (Phase Type)

## Setup



$$
u^-(x,y) = 1
$$





$$
t(x,y) = \exp\left[j\frac{m}{2}\sin(2\pi f_0 x)\right] \text{rect}\left(\frac{x}{\ell}\right) \text{rect}\left(\frac{y}{\ell}\right)
$$





$$
u^+(x,y) = t(x,y)
$$



The phase varies sinusoidally between $+\frac{m}{2}$ and $-\frac{m}{2}$.

## Bessel Function Identity



$$
\exp\left[j\frac{m}{2}\sin(2\pi f_0 x)\right] = \sum_{q=-\infty}^{\infty} J_q\left(\frac{m}{2}\right)\exp(j2\pi q f_0 x)
$$



## Fourier Transform



$$
\therefore \mathcal{FF}\{t(x,y)\} = \ell^2 \text{sinc}(\ell\xi)\text{sinc}(\ell\eta) * \left[\sum_{q=-\infty}^{\infty} J_q\left(\frac{m}{2}\right)\delta(\xi - qf_0, \eta)\right]
$$





$$
= \sum_{q=-\infty}^{\infty} \ell^2 J_q\left(\frac{m}{2}\right)\text{sinc}[\ell(\xi - qf_0)]\text{sinc}(\ell\eta)
$$



## Output Field



$$
\Rightarrow u(x',y') = \frac{\ell^2}{j\lambda z}\exp(jkz)\exp\left[j\frac{k}{2z}(x'^2+y'^2)\right]\sum_{q=-\infty}^{\infty} J_q\left(\frac{m}{2}\right)\text{sinc}\left[\frac{\ell}{\lambda z}(x'-qf_0\lambda z)\right]\text{sinc}\left(\frac{\ell y'}{\lambda z}\right)
$$



Again if $f_0 >> \ell$ (or $T << \ell$), there is little overlap of sinc functions. Then:



$$
I(x',y') \cong \left(\frac{\ell^2}{\lambda z}\right)^2 \sum_{q=-\infty}^{\infty} J_q^2\left(\frac{m}{2}\right)\text{sinc}^2\left[\frac{\ell}{\lambda z}(x'-qf_0\lambda z)\right]\text{sinc}^2\left(\frac{\ell y'}{\lambda z}\right)
$$


# Behavior of $J_q^2\left(\frac{m}{2}\right)$ Terms

## Bessel Function Squared Behavior

The functions $J_q^2\left(\frac{m}{2}\right)$ show characteristic behavior:

- $J_0^2$ starts at 1 and decreases
- Higher order terms $J_1^2, J_2^2, ...$ start at 0 and have peaks at increasing values of $\frac{m}{2}$

## Eliminating Zeroth Order

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Tip</div>
<div class="callout-content">

We can make any of the orders of Bessel become zero by choosing $\frac{m}{2}$ appropriately.

</div>
</div>

**Example:** If we choose $\frac{m}{2} = 2.5$ (or $m = 5$ radians peak-to-peak phase change), $J_0^2(2.5) = 0$, and there is no zeroth order peak.

## Diffraction Pattern

With $m = 8$ radians:
- Note $\frac{m}{2} = 4$ and $J_1(4) \approx 0$
- No first order terms

The resulting [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern shows:
- Orders at positions $q^{th}$, $3^{rd}$, $2^{nd}$, $1^{st}$, $0$, $1^{st}$, $2^{nd}$, $3^{rd}$, $4^{th}$...
- Relative intensities determined by $J_q^2\left(\frac{m}{2}\right)$
# Antennas and Huygens Arrays

## Far Field Diffraction Pattern for Square Antenna

Recall the far field [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern for a single square antenna (width = $d$):



$$
t(x,y) = \text{rect}\left(\frac{x}{d}, \frac{y}{d}\right)
$$





$$
I(\xi_x, \xi_y) = \left(\frac{1}{\lambda z}\right)^2 \left| \iint u_i(x,y) \exp\{-j2\pi(x\xi_x + y\xi_y)\} dx\,dy \right|^2
$$



where $\xi_x$, $\xi_y$ are direction cosines.

If we have a square antenna, this becomes:



$$
I(\xi_x, \xi_y) = I\left(\frac{\cos\theta}{\lambda}, \frac{\cos\phi}{\lambda}\right) = \left(\frac{1}{\lambda z}\right)^2 \left| d^2 \text{sinc}\left(\frac{d\cos\theta}{\lambda}\right) \text{sinc}\left(\frac{d\cos\phi}{\lambda}\right) \right|^2
$$



The intensity pattern shows angular sensitivity in the $\frac{\cos\theta}{\lambda}$ direction.

## Antenna Array

Consider the effect of spacing $M$ antennas a distance $D$ apart ($M$ is odd, $D \geq d$):



$$
t(x,y) = \text{rect}\left(\frac{x}{d}, \frac{y}{d}\right) * \left[\frac{1}{D}\text{comb}\left(\frac{x}{D}\right) \cdot \text{rect}\left(\frac{x}{MD}\right)\right]
$$



This creates a uniform linear array of $M$ antenna elements.
# Antenna Array - Intensity Pattern

## Array Intensity Formula



$$
\Rightarrow I\left(\frac{\cos\theta}{\lambda}, \frac{\cos\phi}{\lambda}\right) = \left(\frac{1}{\lambda z}\right)^2 \left| d^2 \text{sinc}\left(\frac{d\cos\theta}{\lambda}, \frac{d\cos\phi}{\lambda}\right) \right|^2 \cdot \left| \text{comb}\left(\frac{D\cos\theta}{\lambda}\right) * \text{sinc}\left(\frac{MD\cos\theta}{\lambda}\right) \right|^2
$$



The resulting pattern shows:
- Main narrow central lobe (labeled $I$)
- Grating lobes at regular intervals in $\frac{\cos\theta}{\lambda}$

## Grating Lobes

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>Warning</div>
<div class="callout-content">

The central lobe is very narrow $\Rightarrow$ high directivity. However, there are other additional lobes created (called **grating lobes**) in an analogy with optical diffraction gratings.

</div>
</div>

These can cause some confusion in a receiving antenna in determining the actual angle at which a signal was sent.

## Physical Reason for Grating Lobes

Two point sources make two sets of plane waves.

Phases received by antennas of both plane waves are identical.

- Array of Antennas
- Phases measured by antennas of both plane waves are identical
# Antenna Arrays - Main Lobe Condition

## Eliminating Grating Lobes

If we want to ensure that only the main lobe occurs, we require:



$$
\frac{\cos\theta}{\lambda} = \frac{1}{D} \text{ does not exist}
$$





$$
\Rightarrow \cos\theta = \frac{\lambda}{D} > 1 \quad (\Rightarrow \cos\theta \text{ does not exist})
$$





$$
\therefore D < \lambda
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

Or spacing between antennas must be less than a wavelength.

</div>
</div>

## General Case - Linear Array of Arbitrary Antennas

For the general case of a linear array of arbitrary shaped antennas with shape $a(x,y)$ we have:



$$
\Rightarrow t(x,y) = a(x,y) * \left[\text{samp}(x)\right]
$$



where $\text{samp}(x)$ is some [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) function (not necessarily equally spaced delta functions) of finite length.

From the [convolution theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/), we simply have:



$$
I\left(\frac{\cos\theta}{\lambda}, \frac{\cos\phi}{\lambda}\right) = \left| A\left(\frac{\cos\theta}{\lambda}, \frac{\cos\phi}{\lambda}\right) \right|^2 \cdot \left| \mathcal{FF}\{\text{samp}(x)\} \right|^2
$$





$$
= \underbrace{\text{Antenna Factor}}_{\text{Antenna Factor}} \times \underbrace{\text{Array Factor}}_{\text{Array Factor}}
$$



## Array Theorem

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

The array theorem for antennas simply states:

The pattern which results from a linear array of antennas is given by the **product** of the antenna factor (pattern from a single antenna) and the array factor (pattern resulting from antennas considered as point sources).

</div>
</div>
# Array Beam Steering

## Intensity with Direction Cosines

Since we have:



$$
I\left(\frac{\cos\theta'}{\lambda}, \frac{\cos\phi}{\lambda}\right) = \left(\frac{1}{\lambda z}\right)^2 \left| T\mathcal{FF}\{t(x,y)\}\bigg|_{\xi=\frac{\cos\theta}{\lambda}, \eta=\frac{\cos\phi}{\lambda}} \right|^2
$$



And the Fourier shift theorem states:



$$
\mathcal{FF}\{t(x,y)e^{j2\pi\alpha x}\} = T\left(\frac{\cos\theta}{\lambda} - \alpha, \frac{\cos\phi}{\lambda}\right)
$$





$$
= T\left(\frac{\cos\theta - \cos\theta'}{\lambda}, \frac{\cos\phi}{\lambda}\right)
$$



where $\alpha = \frac{\cos\theta'}{\lambda}$

## Phase Delay Beam Steering

Then by simply providing a phase delay from one receiver (or transmitter) to the other, we can steer the beam.

The width of a beam (given by [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/)) is reduced by the overall array size (maximum spatial frequency at the edges) and the angular range (given by maximum angle in which aliasing has not occurred) are independent quantities.

## Phased Array Implementation

```
Phase shifters
    ↓
[α] → [2α] → [3α] → [4α] →  Main lobe direction
         ↘    ↘    ↘    ↘
              (XMT R)
```

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Tip</div>
<div class="callout-content">

Fixed phase delays are often introduced by using varying lengths of coax/transmission lines to antennas.

</div>
</div>

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

If phase is varied electronically, beam can be steered without moving the antennas.

</div>
</div>
# Phased Array Receiving

## Equivalent Large Antenna

In receiving, if we record a sum of all antennas with a given linear phase shift, we have the equivalent of a large antenna pointed at a specific direction.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

When $(x,y)$ values of arriving electromagnetic radiation differ, the relative time delay to the elements of the array is proportional to the relative displacement of the receiving antenna.

</div>
</div>

## Digital Beam Forming

```
        [φ₁]
θ' →  D-[φ₂]→ Σ → record
        [φ₃]
        [φ₄]

Main lobe
pattern angle corresponds
to phase shifts φ₁-φ₄ from e^(j2π cos θ' x), and beam is steered by cos θ
```

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Tip</div>
<div class="callout-content">

If we record all antennas independently, phase shifts can be added later (by a digital computer for example), to steer maximum response in any direction.

</div>
</div>

```
D → [rec] → [φ₁] ↘
D → [rec] → [φ₂] → Σ → result
D → [rec] → [φ₃] ↗
D → [rec] → [φ₄] ↗
```

Where $\phi_1 \to \phi_4$ come from $e^{j\pi\frac{\cos\theta}{\lambda}x}$ and beam is steered by $\cos\theta$.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

We can now analyze energy from different angles by changing $\phi_1$-$\phi_4$ and playing the recording again.

</div>
</div>
# Adaptive Beam Forming and Nulling

## Angular Image of Energy

In this way, an angular image of the energy can be produced:



$$
\text{Signal at angle } \cos\theta_1: \sum_{k=1}^{N} f_k(t) e^{j2\pi \frac{\cos\theta_1}{\lambda} k\Delta}
$$



where:
- $D$ = spacing between antennas
- $N$ = number of antennas

## Adaptive Beam Forming and Nulling

**Goal:** Choose phases that place null on top of noise source



$$
\text{Signal at any angle } \cos\theta_p: \sum_{k=1}^{N} f_k(t) e^{j\pi \frac{\cos\theta_p}{\lambda} k\Delta}
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

This is just a discrete Fourier transform of the signals at the antennas, where the transform is taken in the spatial dimension ($k\Delta$) and results in the angular dimension ($\cos\theta_p$).

</div>
</div>

## System for "Imaging" Sources

Thus, we have a system for "imaging" sources which looks like:

```
Source B at angle θ_B    →  [  ]  → Signal at angle cos θ₁  (Source A) f_A(t)
f_B(t)                   → [FFT] → Signal at angle cos θ₂  (Source B) f_B(t)
Source A at angle θ_A    →  [  ]
f_A(t)
```

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

**Note:** We have just described the equivalent of a lens for RF.

The object is at infinity, and the image occurs at the focal plane (Fourier plane). The lens does its own "FFT".

</div>
</div>
# Two-Dimensional Arrays

## Array Configurations

**Rectangular Array:**
```
o o o o o
o o o o o
o o o o o
o o o o o
o o o o o
```

**Mills Cross (9 antenna dishes):**
```
      o
      o
o  o  o  o  o
      o
      o
```

## Calculation for Mills Cross



$$
\rho(x,y) = \left[\delta(x) \cdot \text{comb}\left(\frac{y}{a}\right) \cdot \text{rect}\left(\frac{y}{5a}\right)\right] ** \text{cyl}\left(\frac{\sqrt{x^2+y^2}}{d}\right) \quad \leftarrow I
$$





$$
+ \left[\text{comb}\left(\frac{x}{a}\right)\delta(y) \cdot \text{rect}\left(\frac{x}{5a}\right)\right] ** \text{cyl}\left(\frac{\sqrt{x^2+y^2}}{d}\right) \quad \leftarrow II
$$





$$
\text{-} \left[\delta(x)\delta(y)\right] ** \text{cyl}\left(\frac{\sqrt{x^2+y^2}}{d}\right) \quad \leftarrow III
$$



## Fourier Transforming



$$
I \Rightarrow \left[5a \cdot \text{comb}\left(\frac{a\cos\phi}{\lambda}\right) * \text{sinc}\left(\frac{5a\cos\phi}{\lambda}\right)\right] \cdot \frac{\pi d^2}{4}\text{somb}\left(d\sqrt{\left(\frac{\cos\theta}{\lambda}\right)^2 + \left(\frac{\cos\phi}{\lambda}\right)^2}\right)
$$





$$
II \Rightarrow \left[5a^2\text{comb}\left(\frac{a\cos\theta}{\lambda}\right) * \text{sinc}\left(\frac{5a\cos\theta}{\lambda}\right)\right] \cdot \frac{\pi d^2}{4}\text{somb}\left(d\sqrt{\left(\frac{\cos\theta}{\lambda}\right)^2 + \left(\frac{\cos\phi}{\lambda}\right)^2}\right)
$$





$$
III \Rightarrow \left[\frac{\pi d^2}{4}\text{somb}\left(d\sqrt{\left(\frac{\cos\theta}{\lambda}\right)^2 + \left(\frac{\cos\phi}{\lambda}\right)^2}\right)\right]
$$


# Mills Cross - Complete Solution

## Combined Result



$$
\therefore I + II - III \Rightarrow \left[5a^2 \text{comb}\left(\frac{a\cos\phi}{\lambda}\right) * \text{sinc}\left(\frac{5a\cos\phi}{\lambda}\right) + 5a^2 \text{comb}\left(\frac{a\cos\theta}{\lambda}\right) * \text{sinc}\left(\frac{5a\cos\theta}{\lambda}\right) - 1\right]
$$





$$
= \left\{5a\sum_{n=-\infty}^{\infty} \text{sinc}\left[5a\left(\frac{\cos\phi}{\lambda} - \frac{n}{a}\right)\right] + 5a\sum_{n=-\infty}^{\infty} \text{sinc}\left[5a\left(\frac{\cos\theta}{\lambda} - \frac{n}{a}\right)\right] - 1\right\}
$$





$$
\cdot \frac{\pi d^2}{4}\text{somb}\left(d\sqrt{\left(\frac{\cos\theta}{\lambda}\right)^2 + \left(\frac{\cos\phi}{\lambda}\right)^2}\right)
$$



## Pattern Analysis

The pattern shows:
- **Antenna factor**: Overall envelope from somb function
- **Array Factor**: Grid of peaks from the cross pattern
- Width of line = $\frac{1}{5a}$

The diagram shows the pattern in $\frac{\cos\theta}{\lambda}$ vs $\frac{\cos\phi}{\lambda}$ space, with the antenna factor providing the overall envelope.

---

# Non-Uniform Arrays

Arrays chosen with random position to reduce sidelobes:

**Regular array** of $N$ radiators:
- Sharp peaks with regular sidelobe pattern
- Predictable grating lobes

**Randomly spaced array** of $N$ radiators:
- Main beam preserved
- Sidelobes reduced and spread out
- No distinct grating lobes
# Mills Cross (Goodman's Notation)

## Configuration

```
        o
        o ↑a
    d ↗ o  o  o  o  o
        o
        o
```

## Calculation



$$
\rho(x,y) = \left[\delta(x) \cdot \text{comb}\left(\frac{y}{a}\right) \cdot \text{rect}\left(\frac{y}{5a}\right)\right] * \text{circ}\left(\frac{\sqrt{x^2+y^2}}{d/2}\right) \quad \leftarrow I
$$





$$
+ \left[\text{comb}\left(\frac{x}{a}\right)\delta(y) \cdot \text{rect}\left(\frac{x}{5a}\right)\right] * \text{circ}\left(\frac{\sqrt{x^2+y^2}}{d/2}\right) \quad \leftarrow II
$$





$$
\text{-} \left[\delta(x)\delta(y)\right] * \text{circ}\left(\frac{\sqrt{x^2+y^2}}{d/2}\right) \quad \leftarrow III
$$



## Fourier Transforming



$$
I: \left\{5a^2 \text{comb}\left(\frac{a\cos\phi}{\lambda}\right) * \text{sinc}\left[\frac{5a\cos\phi}{\lambda}\right]\right\} \cdot \frac{dJ_1(\pi d\rho')}{2\rho'}
$$



where $\rho' = \sqrt{\left(\frac{\cos\theta}{\lambda}\right)^2 + \left(\frac{\cos\phi}{\lambda}\right)^2}$



$$
II: \left\{5a^2 \text{comb}\left[\frac{a\cos\theta}{\lambda}\right] * \text{sinc}\left[\frac{5a\cos\theta}{\lambda}\right]\right\} \cdot \frac{dJ_1(\pi d\rho')}{2\rho'}
$$





$$
III: \left\{\frac{dJ_1(\pi d\rho')}{2\rho'}\right\}
$$





$$
I + II - III \Rightarrow \left\{5a\sum_{n=-\infty}^{\infty}\text{sinc}\left[5a\left(\frac{\cos\phi}{\lambda} - \frac{n}{a}\right)\right] + 5a\sum_{n=-\infty}^{\infty}\text{sinc}\left[5a\left(\frac{\cos\theta}{\lambda} - \frac{n}{a}\right)\right] - 1\right\} \cdot \frac{dJ_1(\pi d\rho')}{2\rho'}
$$


# Mills Cross - Pattern Diagram

## Two-Dimensional Pattern

The Mills Cross produces a characteristic pattern in $\left(\frac{\cos\theta}{\lambda}, \frac{\cos\phi}{\lambda}\right)$ space:

```
              ↑ cos φ/λ
              |
         ─────┼─────  Array Factor
        /  |  |  |  \
       /   |  |  |   \
      (────┼──┼──┼────)──→ cos θ/λ
       \   |  |  |   /
        \  |  |  |  /
         ─────┼─────
              |

     Antenna ↗     ↖ Line width = 1/5a
     Factor
              ←1/a→
```

## Key Features

- **Array Factor**: Grid pattern from the cross arrangement of antennas
- **Antenna Factor**: Circular envelope from individual dish antennas
- **Line width**: $\frac{1}{5a}$ (determined by the total extent of the array)
- **Line spacing**: $\frac{1}{a}$ (determined by the spacing between antennas)

The resulting beam pattern is the product of the array factor (grid) and antenna factor (circular envelope).
# Fourier Transform Property of a Lens

## Setup

Consider a thickness spherical lens:

| Parameter | Value |
|-----------|-------|
| Gaskill | 10-3 |
| Goodman | 5-9 |
| Cathey | 5-9 |

- Maximum thickness = $\Delta_0$
- Index of refraction = $n$
- Thickness at $(x,y)$ = $\Delta(x,y)$

## Phase Delay Through a Lens

Phase delay of wave through a region of refractive index $n$:



$$
\text{Recall } e^{jk'r} \Rightarrow k'r \text{ gives the phase of propagation}
$$





$$
\text{But } k' = \frac{\omega}{c'} = \frac{\omega n}{c_0} \quad \text{since } n = \frac{c_0}{c'} = \frac{\text{free space velocity}}{\text{velocity}}
$$





$$
\therefore \phi = k'r = \frac{\omega n}{c_0} \cdot r = kn \cdot r, \quad \text{where } k = \frac{\omega}{c_0}
$$





$$
\underbrace{\phi}_{\text{phase}}
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

(Free space wavenumber)

$\therefore$ Phase delay suffered by a wave traveling from $U_e$ to $U_i$ is:

</div>
</div>



$$
\phi(x,y) = kn\Delta(x,y) + k[\Delta_0 - \Delta(x,y)]
$$





$$
= \underbrace{k n \Delta(x,y)}_{\text{delay from lens}} + \underbrace{k[\Delta_0 - \Delta(x,y)]}_{\text{delay from free space}}
$$



where $\Delta(x,y)$ is thickness function of lens
# Lens Thickness Function

## Phase-Only Transmittance Function



$$
\Rightarrow t_\ell(x,y) \triangleq e^{j\phi(x,y)} = \exp[jk\Delta_0]\exp[jk(n-1)\Delta(x,y)]
$$



This is a **phase-only function**.

We assume a "thin lens", so that we have the field behind the lens given by:



$$
u^+(x,y) = u^-(x,y)t(x,y) = u^-(x,y)\exp[jk\Delta_0]\exp[jk(n-1)\Delta(x,y)]
$$



## Calculating the Thickness Function $\Delta(x,y)$

Split lens into two parts:

**Convention:** Convex surfaces have positive radii of curvature; concave surfaces have negative radii - for light traveling from left to right.

### Left Half of Lens
- Radius $R_1$
- Center at $R_1 - x_1 - y_1$

### Right Half of Lens
- Radius $-R_2$
- Center at $\sqrt{R_2^2 - x^2 - y^2}$

(Recall $R_2$ is a negative number by convention)



$$
\Rightarrow \Delta(x,y) = \Delta_1(x,y) + \Delta_2(x,y)
$$



**and:**



$$
\Delta_1(x,y) = \Delta_{01} - \left(R_1 - \sqrt{R_1^2 - x^2 - y^2}\right)
$$





$$
= \Delta_{01} - R_1\left(1 - \sqrt{1 - \frac{x^2+y^2}{R_1^2}}\right)
$$





$$
\Delta_2(x,y) = \Delta_{02} - \left(-R_2 - \sqrt{R_2^2 - x^2 - y^2}\right)
$$





$$
= \Delta_{02} - \left(-R_2 + R_2\sqrt{\frac{R_2^2 - x^2 - y^2}{(-R_2)^2}}\right) \leftarrow \text{factor out } -R_2 \text{ and this is a positive number}
$$





$$
= \Delta_{02} + R_2\left(1 - \sqrt{1 - \frac{x^2+y^2}{R_2^2}}\right)
$$


# Lens Thickness Function - Complete Derivation

## Total Thickness Function



$$
\boxed{\Delta(x,y) = \Delta_1(x,y) + \Delta_2(x,y) \approx \Delta_0 - R_1\left(1 - \sqrt{1 - \frac{x^2+y^2}{R_1^2}}\right) + R_2\left(1 - \sqrt{1 - \frac{x^2+y^2}{R_2^2}}\right)}
$$



where $\Delta_0 = \Delta_{01} + \Delta_{02}$

## Paraxial Ray Approximation

Assume deviation from center $(x,y)$ is small, so $x^2 + y^2 << R^2$:



$$
\Rightarrow \sqrt{1 - \frac{x^2+y^2}{R_1^2}} \approx 1 - \frac{x^2+y^2}{2R_1^2}
$$



**and**



$$
\sqrt{1 - \frac{x^2+y^2}{R_2^2}} \approx 1 - \frac{x^2+y^2}{2R_2^2}
$$



(Paraxial rays)

## Approximate Thickness Function

Then we have:



$$
\boxed{\Delta(x,y) = \Delta_0 - R_1\left(\frac{x^2+y^2}{2R_1^2}\right) + R_2\left(\frac{x^2+y^2}{2R_2^2}\right) = \Delta_0 - \frac{x^2+y^2}{2}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)}
$$



## Lens Transmittance Function



$$
\therefore t_\ell(x,y) = \exp[jk\Delta_0]\exp\left[jk(n-1)\left(\Delta_0 - \frac{x^2+y^2}{2}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)\right)\right]
$$





$$
= \exp[jk\Delta_0]\exp\left[jk(n-1)\Delta_0\right]\exp\left[-jk(n-1)\frac{(x^2+y^2)}{2}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)\right]
$$





$$
= \exp[jkn\Delta_0]\exp\left[-jk(n-1)\frac{(x^2+y^2)}{2}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)\right]
$$


# Lens Focal Length and Transmittance Function

## Lens Maker's Formula

Define the focal length of a lens as:



$$
\boxed{\frac{1}{f} \triangleq (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)}
$$



**Lens Maker's Formula**

## Transmittance Function for a Thin Lens

Then we have:



$$
\boxed{t_\ell(x,y) = \exp[jkn\Delta_0]\exp\left[-j\frac{k}{2f}(x^2+y^2)\right]}
$$



**Transmittance Function For a Thin Lens Using The Paraxial Ray Approximation**

## Meaning of Transmittance Function $t_\ell(x,y)$

- $\exp[jkn\Delta_0]$ is a constant phase delay of little interest

- $\exp\left[-j\frac{k}{2f}(x^2+y^2)\right]$ is a quadratic approximation to a converging spherical wave, converging at the point $z = f$.

```
         ← z₂ parabolic
           surface
    ↗  (    )
   (  ( z=f )  → z
    ↘  (    )
   z₁
```

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

The quadratic phase factor represents a parabolic approximation to a spherical wavefront converging to the focal point.

</div>
</div>
# Object Placed Against the Lens

## Setup

```
Normal       ↗            u_f(x',y')
Incidence  [lens]           ↗
Plane    → t_e+t_ℓ(x,y)     z = f
wave A   →
         ↗ p(x,y)
      t_0(x,y)
```



$$
u^-(x,y) = A
$$





$$
p(x,y) = \begin{cases} 1 & \text{inside lens aperture} \\ 0 & \text{outside} \end{cases}
$$





$$
u^+(x,y) = A\,t_0(x,y)\,t_\ell(x,y)\,p(x,y) = A\,t_0(x,y)\,p(x,y)\exp\left[-j\frac{k}{2f}(x^2+y^2)\right]
$$



where we have dropped the constant phase term $t_\ell(x,y)$.

## Field at the Focal Plane

To calculate the field at $z = f$ we use the [Fresnel diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/fresnel_diffraction/) formula:



$$
u_f(x',y')\bigg|_{z_e=f} = \underbrace{\frac{\exp\{jkf\}}{j\lambda f}}_{z_e=f} \exp\left\{j\frac{k(x'^2+y'^2)}{2f}\right\} \iint u^+(x,y)\exp\left\{j\frac{k(x^2+y^2)}{2f}\right\} \exp\left\{-j\frac{2\pi}{\lambda f}(xx'+yy')\right\} dx\,dy
$$



([Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) Form)

## Substituting for $u^+(x,y)$:



$$
u_f(x',y')\bigg|_{z_e=f} = \frac{\exp\left\{j\frac{k(x'^2+y'^2)}{2f}\right\}}{j\lambda f} \iint A\,t_0(x,y)\,p(x,y)\exp\left\{-j\frac{k}{2f}(x^2+y^2)\right\}\exp\left\{j\frac{k(x^2+y^2)}{2f}\right\} \exp\left\{-j\frac{2\pi}{\lambda f}(xx'+yy')\right\} dx\,dy
$$





$$
= A\frac{\exp\left\{jk\frac{(x'^2+y'^2)}{2f}\right\}}{j\lambda f} \iint_{-\infty}^{\infty} t_0(x,y)\,p(x,y)\exp\left\{-j\frac{2\pi}{\lambda f}(xx'+yy')\right\} dx\,dy
$$


# Lens as Fourier Transform System

## Simplified Result

If the object $t_0(x,y)$ is smaller than the lens aperture, we can neglect $p(x,y)$. Then:



$$
u_f(x',y')\bigg|_{z_e=f} = A\frac{\exp\left\{jk\frac{(x'^2+y'^2)}{2f}\right\}}{j\lambda f} \mathcal{FF}\{t_0(x,y)\}\bigg|_{\xi=\frac{x'}{\lambda f}, \eta=\frac{y'}{\lambda f}}
$$



If we measure the intensity at $z_0 = f$ we have:



$$
I_f(x',y')\bigg|_{z=f} = u_e u_e^* = \frac{A^2}{\lambda^2 f^2}\left|\mathcal{FF}\{t_0(x,y)\}\right|^2_{\xi=\frac{x'}{\lambda f}, \eta=\frac{y'}{\lambda f}}
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

**This is the Fourier Power Spectrum**

The intensity in the back focal plane is directly proportional to the Fourier power spectrum of the transparency $t_0(x,y)$.

</div>
</div>

---

## Object Placed in Front of the Lens

(at distance $d$)

```
      d_0
    ↗    ↖← f →↗ y'
  (      )      x'
t_0(x,y)
```

- **Object:** $t_0(x,y)$
- **Angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) spectrum of object:** $\mathcal{FF}\{At_0(x,y)\} = F(\xi,\eta)$



$$
\Rightarrow \text{We can calculate plane wave spectrum at lens by multiplying by Fresnel operator to transfer} \begin{matrix} \text{from} \\ \xi = \frac{x}{\lambda} \\ \eta = \frac{y}{\lambda} \end{matrix}
$$


# Object in Front of Lens - Field Calculation

## Fresnel Transfer to Lens



$$
\therefore F(\xi,\eta) = \left[F_0(\xi,\eta) \cdot \exp\left\{jkd_0\left[1 - \frac{\lambda^2}{2}(\xi^2+\eta^2)\right]\right\}\right]
$$





$$
= F_0(\xi,\eta) \cdot \exp[-j\pi\lambda d_0(\xi^2+\eta^2)]
$$



where we leave out $\exp[jkd_0]$ term since it is a constant.

## Field at Focal Plane

From the object against the lens calculation, we have:



$$
u_f(x',y')\bigg|_{\substack{\text{Field at focal} \\ \text{pt. at lens}}} = \exp\left[j\frac{k}{2f}(x'^2+y'^2)\right] \cdot \frac{\mathcal{FF}\{At_0(x,y)\}}{j\lambda f}\bigg|_{\xi=\frac{x'}{\lambda f}, \eta=\frac{y'}{\lambda f}}
$$





$$
= \frac{\exp\left[j\frac{k}{2f}(x'^2+y'^2)\right]}{j\lambda f} F_0\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)
$$



where $F_0$ is the angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) spectrum.



$$
\therefore u_f(x',y') = \frac{\exp\left[j\frac{k}{2f}(x'^2+y'^2)\right]}{j\lambda f} \exp\left[-j\pi\lambda d_0\left(\frac{x'^2+y'^2}{\lambda^2 f^2}\right)\right] F_0\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)
$$





$$
= \frac{1}{j\lambda f}\exp\left[j\frac{k}{2f}\left(1 - \frac{d_0}{f}\right)(x'^2+y'^2)\right] F_0\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)
$$





$$
\Rightarrow u_f(x',y') = \frac{A}{j\lambda f}\exp\left[j\frac{k}{2f}\left(1 - \frac{d_0}{f}\right)(x'^2+y'^2)\right] \iint t_0(x,y)\exp\left[j\frac{2\pi}{\lambda f}(xx'+yy')\right] dx\,dy
$$



## Special Case: $f = d_0$

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

**Note:** If $f = d_0$ we have:



$$
u_f(x',y') = \frac{A}{j\lambda f}\iint t_0(x,y)\exp\left[-j\frac{2\pi}{\lambda f}(xx'+yy')\right] dx\,dy
$$



$\Rightarrow$ **Exactly the Fourier Transform**

Transform variables: $x \to x$, $y \to z$, $\frac{x'}{\lambda f} \to \xi$, $\frac{y'}{\lambda f} \to \eta$

</div>
</div>
# Lenses and Fourier Transforms

## Fourier Transform Pairs

```
    1                              δ(x,y)
    ↓     [lens]                    ↓     [lens]
   ←f→    δ(x,y)                   ←f→      1

𝓕{1} = δ(x,y)     Fourier Transform     𝓕{δ(x,y)} = 1
                       Pairs
```

## Shift Theorem

```
       y
    x ↙  h ↘  f
         δ(x-h)  φ
```



$$
\mathcal{F}\{\delta(x-h)\}\bigg|_{\xi=\frac{x'}{\lambda f}} = 1 \cdot \exp[-j2\pi h\xi]
$$





$$
= \exp\left[-j2\pi h\frac{x'}{\lambda f}\right]
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

Note however that this is just a **plane wave**, since a plane wave can be written as:



$$
\exp\left[-j2\pi\frac{\cos\theta}{\lambda}x'\right] = \exp\left[-j2\pi\frac{\sin\phi}{\lambda}x'\right]
$$



</div>
</div>



$$
\therefore \sin\phi = \frac{h}{f} \approx \phi \leftarrow \text{Propagation angle of plane wave}
$$



## Connection to Geometrical Optics

From geometrical optics, we note that the ray parallel to the optical axis must be directed through the back focal point.

Hence, we see immediately that $\tan\phi = \frac{h}{f} \approx \phi$.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

This result is identical to Fourier optics approach in the paraxial approximation.

</div>
</div>
# Spherical Wave and Imaging Formula

## Setup

```
         ↗x
      (  )f(  )     x'
    ←x→     f    →x'←
      d₀
```

## Spherical Wave in Focal Plane



$$
\exp\left[-j\frac{\pi r'^2}{\lambda R}\right] = \exp\left[-j\frac{\pi r'^2}{\lambda x'}\right]
$$



where $r' = \sqrt{x'^2 + y'^2}$

## Imaging Formula

Use imaging formulae to locate focal point:



$$
\frac{1}{d_0} + \frac{1}{d_i} = \frac{1}{f}
$$



**or:** $\quad xx' = f^2$ (Newtonian imaging formula)



$$
\therefore x' = \frac{f^2}{x} = R \quad (x = d_0 - f, \quad x' = d_i - f)
$$



## Spherical Wave Expression

And spherical wave becomes:



$$
\exp\left[-j\frac{\pi r'^2 x}{\lambda f^2}\right]
$$





$$
= \exp\left[-j\frac{\pi r'^2(d_0 - f)}{\lambda f \cdot f}\right]
$$





$$
= \exp\left[+j\frac{\pi r'^2}{\lambda f}\left(1 - \frac{d_0}{f}\right)\right] = \exp\left[j\frac{k}{2f}\left(1 - \frac{d_0}{f}\right)(x'^2+y'^2)\right]
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

**Note:** This is exactly the quadratic phase term predicted for an object "d" in front of a lens, observed in back focal plane:



$$
u(x',y') = \frac{A}{j\lambda f}\exp\left[j\frac{k}{2f}\left(1 - \frac{d_0}{f}\right)(x'^2+y'^2)\right]
$$





$$
\times \iint t_0(x,y)\exp\left[-j\frac{2\pi}{\lambda f}(xx'+yy')\right] dx\,dy
$$



↑ focal plane coordinates, ↑ object plane coordinates

</div>
</div>
# Heuristic Explanation of F.T. Property of Lens

## Physical Interpretation

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Tip</div>
<div class="callout-content">

The Fourier Transform property can be thought of as simply:

**Fraunhofer diffraction at infinity** followed by an **imaging system** to image light from $\infty$ to a finite observation plane.

</div>
</div>

## Limiting Case

Of course,



$$
\frac{1}{d_0} + \frac{1}{d_i} = \frac{1}{f}
$$



So if $d_0 = \infty$:
- $d_i = f$
- The Fraunhofer pattern at $\infty$ is reimaged at the back focal plane of the lens.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

This explains why the Fourier transform appears at the back focal plane: the lens images the far-field (Fraunhofer) diffraction pattern from infinity to the focal plane.

</div>
</div>
# Power Spectrum Analysis

## Example: Particle Size Detection

Consider two particles (circles) at points $(a,b)$ and $(c,d)$.

```
  y↑
   |  ⊚(c,d)
   | ⊚(a,b)
   +────────→ x
            λ
```

## Fourier Power Spectrum

Fourier power spectrum gives by:



$$
\left| \frac{\alpha J_1(2\pi\alpha\sqrt{f_x^2+f_y^2})}{\sqrt{f_x^2+f_y^2}} e^{j\pi(af_x+bf_y)} + \frac{\alpha J_1(2\pi\alpha\sqrt{f_x^2+f_y^2})}{\sqrt{f_x^2+f_y^2}} e^{j\pi(cf_x+df_y)} \right|^2
$$





$$
= 2\left(\frac{\alpha J_1(2\pi\alpha\sqrt{f_x^2+f_y^2})}{\sqrt{f_x^2+f_y^2}}\right)^2 + 2\left(\frac{\alpha J_1(2\pi\alpha\sqrt{f_x^2+f_y^2})}{\sqrt{f_x^2+f_y^2}}\right) \cos(2\pi[(a-c)f_x + (b-d)f_y])
$$





$$
= \underbrace{\text{independent of particle position}}_{\text{of particle position}} + \underbrace{\text{sum of random cosines}}_{\Rightarrow \text{noise}}
$$



## Distribution Vector

If scene consists of:
- $N_1$ particles of size $d_1$
- $N_2$ of size $d_2$
- ...
- $N_L$ of size $d_L$

We can express this answer by a distribution vector:



$$
\underline{N} = (N_1, \cdots, N_L)^T
$$


# Particle Size Distribution - Matrix Formulation

## Total Power Spectrum

If $G_i(f_x)$, $i = 1, L$ is the [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern produced by a single particle of size $d_i$, total power spectrum is:



$$
H(f_x) = \sum_{i=1}^{L} N_i G_i(f_x) + \eta(f_x)
$$





$$
\underbrace{\eta}_{\text{noise}}
$$



## Matrix Notation

Sample $f_x$ at discrete frequencies $f_{x_1}, f_{x_2}, \ldots, f_{x_N}$



$$
\Rightarrow \underline{H} = \underline{\underline{G}}\underline{N} + \underline{\eta} \quad \leftarrow \text{(Shaw Stark, 177, 178)}
$$



## Solution Methods

1. Filter result to remove $\underline{\eta}$
2. Invert by pseudoinverse to solve for $\underline{N}$



$$
\underline{H} = \underline{\underline{G}}\underline{N}
$$



$\underline{\underline{G}}$ is not square and has no inverse



$$
\underline{\underline{G}}^+\underline{H} = (\underline{\underline{G}}^+\underline{\underline{G}})\underline{N}
$$





$$
(\underline{\underline{G}}^+\underline{\underline{G}})^{-1}\underline{\underline{G}}^+\underline{H} = \underline{N}_{LS}
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

(Shaw Stark, pg 177-178)

This gives the **Least Squares** solution for the particle size distribution.

</div>
</div>
# Statistical Pattern Recognition

## Feature Selection

**Goal:** We desire to choose a small number of features that are important for pattern recognition.

```
      ┌─────────┐     ┌──────────────┐
  N   │  Image  │     │   Feature    │    Features:
 ───► │         │────►│   Selector   │───► ∧ ∧  Ears (Number)
      │         │     │              │     ≋ ≋  Whiskers (Length)
      └─────────┘     └──────────────┘     ⌒   Tail (Length)
       N² data pts.                        Features (3)
```

## Linear Transforms for Feature Extraction

Can we use linear transforms to extract features?

```
         ┌────────────┐  ┌───────────────┐
  f(x,y) │   Linear   │  │Dimensionality │  F'(u,v)
 ───────►│  Transform │─►│  Reduction    │────────►
         │   F̂(u,v)  │  │               │  M data pts
 N² data │            │  │               │  M << N²
   pts   └────────────┘  └───────────────┘
              ↑
         Unitary
        Transforms
         Preserve
          Energy
```

## Dimensionality Reduction Example

**Example of dimensionality reduction:** Choose M data pts. with highest values.
# Optimization of Linear Transform

## Objective

Choose transform that minimizes the **mean-square error** when M features are used to regenerate (approx.) original image pts.

```
  F'(u,v)  ┌─────────┐  f'(x,y)
 ─────────►│ Inverse │─────────►
M features │ Linear  │ M data pts.
           │Transform│
           └─────────┘
```

## Mean Square Error (MSE)



$$
\text{MSE} = \left\langle \left| f'(x,y) - f(x,y) \right|^2 \right\rangle
$$





$$
\underbrace{f'(x,y)}_{\substack{\text{Reconstructed} \\ \text{image from} \\ \text{M features}}} \quad \underbrace{f(x,y)}_{\substack{\text{Original} \\ \text{Image}}}
$$



## Karhunen-Loève Transform

Linear Transform that minimizes MSE:



$$
\rightarrow \text{Karhunen-Loève Transform}
$$



(sometimes called **Hotelling Transform** or **Principal Component Analysis**)

## Properties

- K-L transform [basis](/notes/areas/mathematics/linear_algebra/definitions/basis/) functions depend on **statistics** of image
- [Basis](/notes/areas/mathematics/linear_algebra/definitions/basis/) functions are given by the **eigenvectors** of the **autocorrelation matrix** of the statistical process

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

If statistics are:
- Large SBP ($N^2 >> 1$)
- **Stationary** (Independent of position)

Then basis functions become **complex exponentials**

And linear transform is **Fourier Transform**

</div>
</div>
# Fourier Transform as Feature Extractor

## Examples (Shaw Stark, pg. 172)

Applications where [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) is useful:
- Handwriting
- Printed matter
- Homogeneous aerosols
- Forests, crops (maybe)
- Targets with equal probability of occurring anywhere in the image

## Conclusion

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

Fourier Transform may be useful as a feature extractor when:

- Location is **unknown** or **unimportant**
- Important information is **delocalized** rather than localized (global rather than local) e.g. textures
- SBP is large and statistics are **stationary**

</div>
</div>

## Examples Where F.T. is Useful

- Handwriting
- Train tracks, orchards
- Aerosol detection

---

# Translational Invariance of Fourier Power Spectrum

```
  f(x,y)  ──────►  F.T.  ──────►  | |²  ──────► |F(f_x,f_y)|² ←─┐
                                                              │ Power
  f(x-a,y-b)      F(f_x,f_y)exp[j2π(af_x+bf_y)]  |F(f_x,f_y)|²←─┤ Spectrum
                                                              │ Does
                                                              │ Not
                                                              └─ Change
```

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

A shift in position only adds a phase factor to the Fourier transform, which disappears when taking the magnitude squared.

</div>
</div>
# Variations on Fourier Power Spectrum Sampling

## Wedge-Ring Detector

(Shaw Stark, pg 163)

```
    ╱╲
   ╱  ╲
  ╱ ┌──┐╲
 ╱  │  │ ╲
╱   └──┘  ╲
```

The wedge-ring detector samples the Fourier plane in polar coordinates, providing:
- Rings for radial (frequency magnitude) information
- Wedges for angular (orientation) information

## Key Properties

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

- Wedges are **scale invariant**
- Rings are **rotationally invariant**
- F.T. of real object is **Hermitian** so left half is same as right half

</div>
</div>

Thus, we can sample only half the transform without losing information.

(Shaw Stark, pg. 168)
# Variations on Fourier Power Spectrum Sampling (Cont.)

## Log-Polar Coordinate Distortion

```
         ┌───────────┐    ┌──────────┐
  f(r,θ) │ Log-polar │    │ Fourier  │     | |²
 ────────►│Coordinate │───►│Transform │────►
         │Distortion │    │          │
         └───────────┘    └──────────┘
              ↓               θ
         ┌────┴────┐          ↓
         │ log(r)  │        log(r)
         └─────────┘
```

## Coordinate Transformation

**Note:** $f(ar, \theta + \theta_0)$ becomes:



$$
f(\log r + \log a, \theta + \theta_0)
$$




$$
\underbrace{\log r + \log a}_{x\text{-axis}} \quad \underbrace{\theta + \theta_0}_{y\text{-axis}}
$$





$$
\Rightarrow
$$

 Scale and rotation have been converted into an **x-axis** & **y-axis shift**

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

$\therefore$ Since Fourier power spectrum is invariant to shifts in $x$ & $y$, the original object can change scale & orientation without affecting feature.

</div>
</div>

## Mellin Transform

- Transform in $\log(r)$ direction is a **Mellin transform**
- Features are **no longer [invariant](/notes/areas/mathematics/abstract_algebra/definitions/invariant/)** to translation

(Shaw Stark, pg. 175 & 174)
# Complete Invariance: Position, Scale, and Orientation

## How to Include All Invariances?

Combining position invariance (as well as scale and orientation):

```
Original   ┌─────────┐      ┌───────────┐   ┌─────────┐
 Object    │ Fourier │  | |²│ Log-polar │   │ Fourier │  | |²   Feature
──────────►│Transform│─────►│Coordinate │──►│Transform│──────►
   to      │         │      │Distortion │   │         │
 Detect    └─────────┘      └───────────┘   └─────────┘
```

## Invariance Properties

1. **Translational Invariance**: First [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) + magnitude squared removes position dependence

2. **Scale & Rotation Invariance**:
   - Power spectrum will **inversely scale** with object
   - Power spectrum will **rotate directly** as object rotates
   - Log-polar distortion converts these to shifts
   - Second [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) + magnitude squared removes scale and rotation dependence

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Tip</div>
<div class="callout-content">

This cascade of transforms provides features that are invariant to:
- Translation (position)
- Scale (size)
- Rotation (orientation)

Making it ideal for object recognition regardless of where, how big, or how oriented the object appears.

</div>
</div>
# Telecentric Imaging System

## Setup

```
Object          y₂              Image
  y₁         ↗  x₂           y₃↗
   ↗x₁      ╱    ╲             ╱ x₃
   ╲       ╱      ╲           ╱
    ╲─────╱────────╲─────────╱
      f₁      f₁       f₂      f₂

   └──────────┘    └──────────┘
   This stage produces    This stage produces
   an exact Fourier       an exact Fourier
   Transform (forward)    Transform (forward)
```

## Field at Each Plane

Consider:
1. $t(x,y)$ in the object plane $(x_1, y_1)$
2. [Plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) illumination of object $A$



$$
\Rightarrow u_1(x_1, y_1) = At(x,y)
$$



From previous development, we know that at focal plane of first lens:



$$
u_2(x_2, y_2) = \frac{A}{j\lambda f_1} \mathcal{FF}\{t(x,y)\}\bigg|_{\xi=\frac{x_2}{\lambda f_1}, \eta=\frac{y_2}{\lambda f_1}}
$$





$$
= \frac{A}{j\lambda f_1} T\left(\frac{x_2}{\lambda f_1}, \frac{y_2}{\lambda f_1}\right)
$$



where $T\left(\frac{x_2}{\lambda f_1}, \frac{y_2}{\lambda f_1}\right) = \mathcal{FF}\{t(x,y)\}$

## Field at Output Plane

We can equivalently calculate distribution in $(x_3, y_3)$ plane with same formula:



$$
u_3(x_3, y_3) = \left(\frac{A}{j\lambda f_1}\right)\left(\frac{1}{j\lambda f_2}\right) \iint T\left(\frac{x_2}{\lambda f_1}, \frac{y_2}{\lambda f_1}\right) \exp\left[-j\frac{2\pi}{\lambda f_2}(x_2 y_3 + y_2 y_3)\right] dx_2 dy_2
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

- Need inverse transform to return to $u_1$
- $T$ is function of $\frac{x_2}{\lambda f_1}$ and exp is function of $\frac{x_2}{\lambda f_2}$

</div>
</div>
# Telecentric Imaging System - Magnification

## Variable Substitution



$$
\Rightarrow i) \text{ Let } x_3 = -(-x_3) \text{ and } y_3 = -(-y_3) \text{ in exponential}
$$





$$
ii) \text{ Let } x_2 = f_1\left(\frac{x_2}{f_1}\right), \quad dx_2 = \lambda f_1 d\left(\frac{x_2}{\lambda f_1}\right), \quad y_2 = f_1\left(\frac{y_2}{f_1}\right) \text{ and } dy_2 = \lambda f_1 d\left(\frac{y_2}{\lambda f_1}\right)
$$



Then:



$$
u_3(x_3, y_3) = \frac{Af_1}{f_2} \iint T\left(\frac{x_2}{\lambda f_1}, \frac{y_2}{\lambda f_1}\right) \exp\left\{j2\pi f_1\left(\frac{x_2}{\lambda f_1}\right) + (-y_3)\frac{f_1}{f_2}\left(\frac{x_2}{\lambda f_1}\right)\right\} d\left\{\frac{x_2}{\lambda f_1}\right\} d\left\{\frac{y_2}{\lambda f_1}\right\}
$$





$$
= A\frac{f_1}{f_2} u_1\left(\frac{-f_1 x_3}{f_2}, \frac{-f_1 y_3}{f_2}\right)
$$



## Magnification

Define a magnification $M = f_2/f_1$

Then:



$$
u_3(x_3, y_3) = \frac{A}{M} u_1\left(\frac{-x_3}{M}, \frac{-y_3}{M}\right)
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

**Notes:**
1. Intensity reduces by $M^2$ because area increases by $M^2$ - This is because a lens can only produce a **forward** Fourier transform, so we have $\mathcal{FF}\{\mathcal{FF}\{t(x,y)\}\} = t(-x,-y)$
2. We can adjust $M$ by changing focal lengths. In particular, if $f_1 = f_2$, $M = 1$. This is a **1:1 imaging system**.

</div>
</div>

## Motion of Object & Image Planes

```
      ↑           ↑
     x₀          x_i
  ⟺  ╱ ╲    ╱ ╲  ⟺
    ←f→ ←f→
```



$$
x_i = x_o \text{ when } M = 1
$$




$$
x_i = M^2 x_o \text{ in general}
$$


# Single Lens Imaging

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Tip</div>
<div class="callout-content">

**Homework Problems:** Goodman: 6-1, 6-3, Heskett

</div>
</div>

## Impulse Response Formulation

Every [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/), we can state the response of a linear system as the sum of impulse responses at point sources:



$$
u_i(x_i, y_i) = \iint h(x_i, y_i; x_o, y_o) u_o(x_o, y_o) dx_o dy_o
$$



where $h$ is the response of the system to a point source at $x_o, y_o$

```
      u_o  u_o'         u_i
       ╲   ╱             │
       (  │  )           │
        ╲ │ ╱            │
    ←d_o→│←───d_i────→
```

## Image Formation

For image formation, on impulse:



$$
h(x_i, y_i; x_o, y_o) = K\delta(x_i \pm Mx_o, y_i \pm My_o), \quad M = \frac{1}{\text{magnification}}
$$



Consider a point source at $(x_o, y_o)$:



$$
\Rightarrow \text{Wave at lens is a spherical wave}
$$





$$
\text{+ with paraxial approx. is written as:}
$$





$$
u_\ell(x,y) = \frac{1}{j\lambda d_o} \exp\left\{j\frac{k}{2d_o}[(x-x_o)^2 + (y-y_o)^2]\right\}
$$



## After Passing Through the Lens



$$
u_\ell'(x,y) = u_\ell(x,y) \cdot p(x,y) \exp\left[-j\frac{k}{2f}(x^2+y^2)\right]
$$





$$
p = \text{pupil function}
$$





$$
\underbrace{\quad}_{\text{transmittance of thin lens}}
$$



Using [Fresnel diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/fresnel_diffraction/) from $u_\ell'$ to $u_i$:



$$
\text{Result} \Rightarrow h(x_i, y_i; x_o, y_o) = \frac{1}{j\lambda d_i} \iint u_\ell'(x,y) \exp\left\{j\frac{k}{2d_i}[(x_i-x)^2 + (y_i-y)^2]\right\} dx\,dy
$$


# Single Lens Imaging - Impulse Response

## Combining Terms



$$
h(x_i, y_i; x_o, y_o) = \frac{1}{\lambda^2 d_o d_i} \exp\left[j\frac{k}{2d_i}(x_i^2+y_i^2)\right] \underbrace{\exp\left[j\frac{k}{2d_o}(x_o^2+y_o^2)\right]}_{\text{small object}}
$$





$$
\cdot \iint p(x,y) \exp\left[j\frac{k}{2}\left(\frac{1}{d_o} + \frac{1}{d_i} - \frac{1}{f}\right)(x^2+y^2)\right]
$$





$$
\cdot \exp\left\{-jk\left[\left(\frac{x_o}{d_o} + \frac{x_i}{d_i}\right)x + \left(\frac{y_o}{d_o} + \frac{y_i}{d_i}\right)y\right]\right\} dx\,dy
$$



## Simplifications

1. Since we are normally interested in image intensity, we can ignore $\exp\left[j\frac{k}{2d_i}(x_i^2+y_i^2)\right]$

2. $\exp\left[j\frac{k}{2d_o}(x^2+y^2)\right]$ cannot be ignored, since the [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) integral is taken over $x_o$ & $y_o$. However, if we are interested in an **imaging condition**, the light at $x_i, y_i$ must come from a small region of the object.

```
    (x_o,y_o)╱────────────╲
            ╱              ╲
           (                )──→ (x_i, y_i)
```

## Small Region Approximation

If, within this small region, the phase does not change much, we can let:



$$
\exp\left[j\frac{k}{2d_o}(x_o^2+y_o^2)\right] \cong \exp\left[j\frac{k}{2d_o}\left(\frac{x_i^2+y_i^2}{M^2}\right)\right]
$$



and the image plane phase can again be dropped.
# Single Lens Imaging - Impulse Response (Continued)

## Simplified Expression

We then have:



$$
h(x_i, y_i; x_o, y_o) = \frac{1}{\lambda^2 d_o d_i} \iint p(x,y) \exp\left[j\frac{k}{2}\left(\frac{1}{d_o} + \frac{1}{d_i} - \frac{1}{f}\right)(x^2+y^2)\right]
$$





$$
\cdot \exp\left\{-jk\left[\left(\frac{x_o}{d_o} + \frac{x_i}{d_i}\right)x + \left(\frac{y_o}{d_o} + \frac{y_i}{d_i}\right)y\right]\right\} dx\,dy
$$



Finally, we restrict ourselves to the **image plane**:



$$
\boxed{\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}}
$$


**Lens Law**

## Space-Invariant Form

Then:



$$
h(x_i, y_i; x_o, y_o) = K \iint p(x,y) \exp\left\{-jk\left[\left(\frac{x_o}{d_o} + \frac{x_i}{d_i}\right)x + \left(\frac{y_o}{d_o} + \frac{y_i}{d_i}\right)y\right]\right\} dx\,dy
$$



where $K = \frac{1}{\lambda^2 d_o d_i}$ and $M = \frac{-d_i}{d_o}$



$$
\Rightarrow h(x_i, y_i; x_o, y_o) = K \iint p(x,y) \exp\left\{j\frac{2\pi}{\lambda d_i}[(x_i - Mx_o)x + (y_i - My_o)y]\right\} dx\,dy
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

Impulse response is given by the F.T. of the pupil function, centered on image coordinates $x_i = -Mx_o$, $y_i = -My_o$.

</div>
</div>

## Change of Variables

Let $\tilde{x} = \frac{x}{\lambda d_i}$, $\tilde{y} = \frac{y}{\lambda d_i}$, $\tilde{x}_o = Mx_o$, $\tilde{y}_o = My_o$



$$
\rightarrow \boxed{h(x_i - \tilde{x}_o, y_i - \tilde{y}_o) = K\lambda^2 d_i^2 \iint p(\lambda d_i \tilde{x}, \lambda d_i \tilde{y}) \exp\left\{-j2\pi[(x_i - \tilde{x}_o)\tilde{x} + (y_i - \tilde{y}_o)\tilde{y}]\right\} d\tilde{x}\,d\tilde{y}}
$$



**(Space [Invariant](/notes/areas/mathematics/abstract_algebra/definitions/invariant/) Form)**

Finally, let $\tilde{h} = \frac{1}{K\lambda^2 d_i^2} h$

and:



$$
u_g(\tilde{x}_o, \tilde{y}_o) = K\frac{\lambda^2 d_i^2}{M^2} u_o\left(\frac{-\tilde{x}_o}{M}, \frac{-\tilde{y}_o}{M}\right)
$$





$$
\underbrace{\quad}_{\text{Modified object}} \quad \underbrace{\frac{1}{M}}_{\text{Geometric Optics Expression for Object}}
$$


# Coherent Transfer Function (CTF)

## Linear Shift-Invariant Superposition

Then the original [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) integral becomes:



$$
u_i(x_i, y_i) = \iint \tilde{h}(x_i - \tilde{x}_o, y_i - \tilde{y}_o) u_g(\tilde{x}_o, \tilde{y}_o) d\tilde{x}_o d\tilde{y}_o
$$





$$
\text{where } \tilde{h}(x_i, y_i) = \iint p(\lambda d_i \tilde{x}, \lambda d_i \tilde{y}) \exp[-j2\pi(\tilde{x}x_i + \tilde{y}y_i)] d\tilde{x}\,d\tilde{y}
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

**True for coherent light.**
Image/amplitude distribution.

</div>
</div>

## What is the Transfer Function of the Lens?

Define frequency spectra of input & output:
- Note: Goodman notation $f_x = \xi$, $f_y = \eta$

**Input:**


$$
G_g(f_x, f_y) = \iint u_g(\tilde{x}_o, \tilde{y}_o) \exp[-j2\pi(f_x \tilde{x}_o + f_y \tilde{y}_o)] d\tilde{x}_o d\tilde{y}_o
$$



**Output:**


$$
G_i(f_x, f_y) = \iint u_i(x_i, y_i) \exp[-j2\pi(f_x x_i + f_y y_i)] dx_i dy_i
$$



## Space-Invariant Transfer Function



$$
H(f_x, f_y) = \iint \tilde{h}(x_i, y_i) \exp[-j2\pi(f_x x_i + f_y y_i)] dx_i dy_i
$$



From the [convolution theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/), we have:



$$
G_i(f_x, f_y) = H(f_x, f_y) \cdot G_g(f_x, f_y)
$$





$$
H(f_x, f_y) = \text{coherent transfer function (CTF)}
$$



## CTF and Pupil Function



$$
\text{Recall: } \boxed{H(f_x, f_y) = \mathcal{FF}\{\tilde{h}(x_i, y_i)\} = \mathcal{FF}\{\mathcal{FF}^{-1}\{p(\lambda d_i \tilde{x}, \lambda d_i \tilde{y})\}\}}
$$





$$
= p(-\lambda d_i f_x, -\lambda d_i f_y)
$$





$$
\therefore \boxed{\text{CTF} = \text{Pupil function in inverted coordinates}}
$$


# Example: Circular Lens Aperture

## Lens of Diameter $\ell$



$$
\Rightarrow p(x,y) = \text{circ}\left(\frac{\sqrt{x^2+y^2}}{\ell/2}\right)
$$





$$
\Rightarrow H(f_x, f_y) = \text{circ}\left(\frac{\sqrt{f_x^2+f_y^2}}{1/(2\lambda d_i)}\right) = \begin{cases} 1 & 0 < \sqrt{f_x^2+f_y^2} < \frac{1}{2\lambda d_i} \\ \frac{1}{2} & \sqrt{\quad} = \frac{1}{2\lambda d_i} \\ 0 & \sqrt{\quad} > \frac{1}{2\lambda d_i} \end{cases}
$$



## Transfer Function Shape

```
        ┌─────────────┐
        │             │     $\sin\theta = \frac{\ell}{d}$ role:
        │             │     (used backwards) ↙
    ────┴──────┬──────┴────    f = 1/λ
              │
         ──►  │  ◄── at θ = λf_x
        1/2λd_i
              = cutoff
```



$$
\Rightarrow f_x = \frac{1}{2\lambda d_i}
$$



## Physical Interpretation

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Note</div>
<div class="callout-content">

**Note:** If the aperture acts like a filter, thus no high freq. info. passes through the edges and low freq. through the center.

</div>
</div>



$$
\Rightarrow
$$

 **Physical Interpretation:**

```
      ┌─────────────┐
      │   ←─d_i─→  │
      │      ╲     │
      │       ╲    │
      └────────╲───┘
            Huygens
            Sources
```

- Each Huygens source will interfere with any other source to form a grating $d_i$ away from lens
- Each grating is a spatial frequency component of the image
- Largest spatial frequency is formed from Huygens sources which are farthest from each other
# Maximum Spatial Frequency and Numerical Aperture

## Two Point Sources

Consider two point sources at $x = \ell/2$ and $x = -\ell/2$:

```
  ℓ┌─────────────┐
   │      d_i    │θ
   │    ╲   ╱    │
  ─┴─────┴─────┴─
```

## Interference Pattern



$$
A = e^{j\left(2\pi\alpha x + \frac{x\ell\alpha\xi}{2d_i}\right)} + e^{j\left(-2\pi\alpha x + \frac{x\ell\alpha\xi}{2d_i}\right)}, \quad \alpha = \frac{\sin\theta}{\lambda}, \quad \cos\theta \approx \frac{\ell/2}{d_i}
$$



Ignoring the spherical wave term gives:



$$
A = e^{j(2\pi\alpha x)} + e^{-j2\pi\alpha x} = 2\cos(2\pi\alpha x)
$$





$$
\Rightarrow \boxed{\text{Highest spatial freq. in image} = \alpha = \frac{\ell\sin\theta}{\lambda} = \frac{\ell}{2\lambda d_i}}
$$



## Numerical Aperture

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Important</div>
<div class="callout-content">

**Note:** $\lambda_{eff}$ and wavelength are the only important parameters:



$$
\alpha_{max} = f_{max} = \frac{\sin\theta}{\lambda_{eff}} = \frac{n\sin\theta}{\lambda_0} = \frac{NA}{\lambda_0}
$$



(This is the freq. cutoff in free space calculation)

</div>
</div>



$$
\underbrace{\lambda_{eff}}_{\substack{\text{effective} \\ \text{wavelength in} \\ \text{medium}}}
$$





$$
\boxed{NA = n\sin\theta = \text{numerical aperture}}
$$


# Note: Physical Significance (Object Space Resolution)

## Object Space Resolution



$$
\left(f_{\max}\right)_{obj} = \frac{1}{2\lambda d_o} = \frac{NA}{\lambda}
$$





$$
\text{Resolution} = \frac{1}{f_{\max}} = \frac{1}{(NA)}
$$



**Illuminate with a pencil beam** at Grating of freq. $f_x$

See smaller features if:
- $\lambda$ small
- NA large ($NA \leq 1$ in air → $(res)_{min} = \lambda$)

---

## Sinusoidal Diffraction Grating

A sinusoidal [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) grating (freq $f_o$) will diffract a pencil beam into 2 beams.

- If too high, both beams miss the lens, and no light passes through
- At some critical angle $\tan \theta = \frac{1}{2d_o}$, the two pencil beams just enter, and interference occurs in the output to generate a sinusoid

Since the angle is related to the grating freq by:


$$
\sin \theta = \lambda f_x
$$



(note, this is just $\sin \theta = \frac{\lambda}{d}$, where $d = \frac{1}{f_x}$)

We have:


$$
\sin \theta_{\max} = (\lambda f_x)_{\max} \approx \tan \theta_{\max} = \frac{1}{2d_o}
$$





$$
\therefore \boxed{(f_x)_{\max} = \frac{1}{2\lambda d_o}}
$$



---

## Notes

- High spatial frequencies pass through the edge of the lens, and low spatial frequencies through the center
- $(NA)_{object side} = n \sin \theta$ and $f_{\max} = \frac{NA}{\lambda}$
- A specific spatial freq. goes through a specific part of the lens
# Coherence

**Midterm: Next Monday**

## Types of Coherence

1. Temporal [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) (longitudinal)
2. Spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) (transversal)

---

## A. Temporal Coherence

[Diagram showing wave oscillation u(t) between times $t_2$ and $t_1$]

→ Degree of correlation between $t_1$ & $t_2$

→ $\langle u(t_1) u^*(t_2) \rangle$ ← Time average



$$
\langle u(t_1) u^*(t_2) \rangle = \frac{1}{T} \int_0^T u(t+t_1) u^*(t+t_2) dt
$$



If statistics are stationary, we can write the time average as:



$$
\langle u(t_1) u^*(t_2) \rangle = \lim_{T \to \infty} \frac{1}{T} \int_0^T u(t) u(t+\tau) dt, \quad \tau = t_2 - t_1
$$



**Examples of high temporal [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/):**
- Pure monochromatic source such as a single mode highly filtered white light
- Possibly low spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/)

---

## B. Spatial Coherence

[Diagram showing two points with rays]

**Degree of correlation between $x_1$ & $x_2$**



$$
\langle u(x_1) u^*(x_1) \rangle
$$

 ← time average



$$
\Rightarrow |\langle u(x_1) u^*(x_2) \rangle| = 1
$$

 → perfect spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/)

If diffuse states $e^{i\phi(t)}$ ← function of time, and [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) is destroyed.

**Examples of high spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/):**
1. Star (low temporal [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/))
2. Arc lamp (low-medium temporal coh.)
3. Gas laser (high temporal coh.)

---

## C. Mutual Coherence Function



$$
\Gamma(x_1, x_2, \tau) = \Gamma_{12}(\tau) = \langle u(x_1, t+\tau) u^*(x_2, t) \rangle
$$



Cross correlation between waves at two different points and two different times.

---

## Detailed Analysis

**Note:** This does not imply that high spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) means a [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) illumination.

**Example:**
[Diagram showing diffuser creating spreading light]

**Consider** $\langle u(x_1) u^*(x_2) \rangle$



$$
u(x_1) = e^{i(\omega t + \phi_1)}
$$




$$
u(x_2) = e^{i(\omega t + \phi_2)}
$$



Note: phases are not changing in time.



$$
\langle u(x_1) u^*(x_2) \rangle = \frac{1}{T} \int_0^T e^{i(\phi_1 - \phi_2)} dt = e^{i(\phi_1 - \phi_2)} \frac{1}{T} \int_0^T dt
$$





$$
\Rightarrow |\langle u(x_1) u^*(x_2) \rangle| = 1
$$

 → Perfect spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/)
# Mutual Coherence Function and Fringe Visibility


## ★★ Interference

**Time-Average Intensity of two light fields $E_1$ & $E_2$ (at 2 places and 2 times)**



$$
I = \langle (E_1 + E_2) \cdot (E_1^* + E_2^*) \rangle
$$





$$
= \langle |E_1|^2 \rangle + \langle |E_2|^2 \rangle + 2\text{Re}\langle E_1 \cdot E_2^* \rangle
$$





$$
= I_1 + I_2 + 2\text{Re}\langle E_1 E_2^* \rangle
$$



where $I_1 = \langle |E_1|^2 \rangle$, and $I_2 = \langle |E_2|^2 \rangle$

---

## Defining Mutual Coherence

We can define the mutual [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) as:



$$
\Gamma_{12}(\tau) = \langle E_1(t) E_2^*(t+\tau) \rangle
$$





$$
\gamma_{12}(\tau) = \frac{\Gamma_{12}(\tau)}{\sqrt{\Gamma_{11}(0) \Gamma_{22}(0)}} = \frac{\Gamma_{12}(\tau)}{\sqrt{I_1 I_2}}
$$



[Diagram showing interference pattern with spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) notation]

What is spatial coh. in this plane of pts $x_1$ & $x_2$?

$\Gamma_{12}(\tau=0)$



$$
\therefore I = I_1 + I_2 + 2\text{Re}\{\Gamma_{12}(\tau)\}, \quad \text{where } \tau = \text{time difference}
$$



---

## Define Degree of Coherence



$$
\gamma_{12}(\tau) = \frac{\Gamma_{12}(\tau)}{\sqrt{\Gamma_{11}(0)\Gamma_{22}(0)}} = \frac{\Gamma_{12}(\tau)}{\sqrt{I_1 I_2}}
$$





$$
\therefore I = I_1 + I_2 + 2\sqrt{I_1 I_2} \text{Re}\{\gamma_{12}(\tau)\}
$$





$$
= I_1 + I_2 + 2\sqrt{I_1 I_2}|\gamma_{12}(\tau)|\cos[\alpha_{12}(\tau) + \delta]
$$



where $|\gamma|$ ranges from $0 \to 1$ ← totally coherent
$\alpha_{12}(\tau) + \delta = \arg\{\gamma_{12}(\tau)\}$

- If $|\gamma| = 1$, waves add in amplitude
- If $|\gamma| = 0$, waves add in intensity



$$
\Rightarrow I_{\max} = I_1 + I_2 + 2\sqrt{I_1 I_2}|\gamma_{12}|
$$




$$
I_{\min} = I_1 + I_2 - 2\sqrt{I_1 I_2}|\gamma_{12}|
$$





$$
\boxed{\gamma^2 = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} = \frac{2\sqrt{I_1 I_2}|\gamma_{12}|}{I_1 + I_2}}
$$

 → **Visibility**

(Note similarity to standing wave ratio)
# Visibility and Coherence



$$
\rightarrow \text{If } I_1 = I_2 \text{ we have}
$$





$$
\boxed{\gamma = |\gamma_{12}|}
$$





$$
\therefore \text{Complete coherence} \Rightarrow \text{visibility} = 1
$$




$$
\text{Complete incoherence} \Rightarrow \text{visibility} = 0
$$



---

## D. Relation Between Temporal Coherence & Spectrum

**Note:**


$$
\langle u(t) u^*(t+\tau) \rangle = \lim_{T \to \infty} \frac{1}{T} \int_0^T u(t) u^*(t+\tau) dt
$$




$$
= u(t) * u^*(t) \leftarrow \text{autocorrelation}
$$



**Wiener-Khinchin Theorem** ⇒


$$
\mathcal{F}\{u(t) * u^*(t)\} = \tilde{U}(\omega) \cdot \tilde{U}^*(\omega) = |U(\omega)|^2
$$


→ Spectral Power Density

⇒ Thus, the temporal [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) part of the mutual [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) function is F.T. related to the bandwidth of the source ⇒

---

## Examples:

| Source | Spectrum | $|\gamma_{11}(\tau)|$ |
|--------|----------|----------------------|
| "Perfect" Laser (single freq.) | [Delta function at 5000 Å] | [Constant = 1] |
| Discharge Tube (Low pressure) | [Peak at $\Delta\lambda \approx 1$ Å] | [Decaying curve, $2.3 \times 10^{-12}$ sec] |
# Coherence Time and Length

## Multi-Mode Lasers

| Source | Spectrum | R(τ) | $|\gamma_{11}(\tau)|$ |
|--------|----------|------|----------------------|
| Two modes | [Two peaks separated by δf] | [Oscillating] | [Envelope with period ← δf →] |
| Many modes | [Multiple peaks at δf₁, δf₂] | [Autocorrelation pattern] | [Decaying envelope with periods 1/δf₁, 1/δf₂] |

---

## ★ Coherence Time



$$
\boxed{\langle \tau_o \rangle = \frac{1}{\Delta f}}
$$



Since:
[Spectrum diagram] → [Coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) function with $\tau_o = \frac{1}{\Delta f}$]

⇒ Time delay when fringes no longer form



$$
\Delta \tau = t_2 - t_1
$$



If $\Delta \tau > \tau_o$, no fringes → **[Holography](/notes/areas/electrical_engineering/physical_optics/definitions/holography/)**

---

## ★ Coherence Length



$$
l_c = c\langle \tau_o \rangle = \frac{c}{\Delta f}
$$



In terms of wavelengths, we have:



$$
\boxed{l_c = \frac{\lambda^2}{\Delta \lambda}}
$$



Since:


$$
\frac{\Delta f}{f} = \frac{\Delta \lambda}{\lambda}
$$




$$
\frac{c}{\Delta f} = \frac{\bar{c}\lambda}{\bar{f}\Delta \lambda}
$$



And:


$$
f = \frac{c}{\lambda}
$$




$$
\frac{df}{d\lambda} = -\frac{c}{\lambda^2}
$$




$$
\Rightarrow \Delta f = -\frac{c}{\lambda^2}\Delta \lambda
$$



---

## Example: Coherence length of white light detectable by the eye



$$
\lambda = 5500 \text{ Å}
$$




$$
\lambda_{\min} = 4000 \text{ Å}
$$




$$
\lambda_{\max} = 7000 \text{ Å}
$$





$$
\Rightarrow l_c = \frac{\lambda^2}{\Delta \lambda} = \left(\frac{\lambda}{\Delta \lambda}\right)\lambda \approx 3\lambda
$$


# Measurement of Temporal Coherence

## → Measurement of Temporal Coherence

### Michelson Interferometer

[Diagram showing Michelson interferometer with beam splitter (B.S.), two arms l₁ and l₂]



$$
\tau = \frac{l_2 - l_1}{c}
$$



**Note:** By adjusting $l_1$ w.r.t. $l_2$, any time can be correlated with any other. The fields are compared at the same point in space.

---

## Output of Michelson at a Single Point



$$
I(\tau) = \lim_{T \to \infty} \frac{1}{T} \int_0^T |E(t) + E(t+\tau)|^2 dt
$$





$$
= 2I_o + 2\text{Re}\{\Gamma_{11}(\tau)\}
$$

 (See previous derivation on pg. 3-3)

where $\tau = \frac{l_2 - l_1}{c}$

**Derivation:**


$$
I(\tau) = \frac{1}{T}\int_0^T |E(t) + E(t+\tau)|^2 dt
$$




$$
= \frac{1}{T}\left(\int_0^T |E(t)|dt + \frac{1}{T}\int_0^T |E(t+\tau)|dt\right)
$$




$$
+ \frac{1}{T}\int_0^T E(t)\bar{E}(t+\tau)dt + \frac{1}{T}\int_0^T E^*(t)E(t+\tau)dt
$$




$$
= I_o + 2\text{Re}\left\{\frac{1}{T}\int_0^T E(t)E^*(t+\tau)dt\right\}
$$



where $\tau = \frac{l_2 - l_1}{c}$



$$
= 2I_o + 2\text{Re}\{\Gamma_{11}^{Autocorrelation}\}
$$



Thus, by moving one arm w.r.t. the other, we can obtain $\Gamma_{11}(\tau)$.

⇒ Since $\Gamma_{11}(\tau)$ is F.T. related to the spectrum of the source, we can measure $\Gamma_{11}(\tau)$ with this device and perform FFT to compute spectrum.

### ★ Fourier Transform Spectrometer
# Fourier Spectrometer Advantages and Limitations

## ★ Advantages to Fourier Spectrometer

- **All wavelengths are multiplexed onto a single detector** - Use to be important in astronomy. Now used in IR (FTIR)

- **High resolution possible with large instrument**

- **Angular acceptance is higher**

---

## ★ Limitations

- **Resolution determined by:**
  - A. Stability of large interferometers
  - B. SNR of detector measuring small correlations on a large bias

from very narrow lines
# Spatial Coherence


[Diagram showing source with points x', x" projecting through lens to measurement plane]

- [Coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) measured in this plane
- **Note:** Incoherent source can become coherent through propagation



$$
\Gamma_{12}(0) = \text{measure of spatial coherence}
$$



⇒ $r_1 = r_2$, we can vary $d$ until no fringes form. This is the **[coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) width**.

---

## ★ Effect of Source Size on Spatial Coherence

Consider fringes made by each point of an extended completely incoherent source and superimpose the result.

**For a single point on S**, we have a fringe pattern at P:



$$
I(P) = I_1(P) + I_2(P) + 2\sqrt{I_1(P)}\sqrt{I_2(P)}\cos\left[\bar{k}\left(\frac{d}{R}\right)x + \bar{k}\left(\frac{d}{r}\right)x''\right]
$$



where $\bar{k} = \frac{2\pi}{\lambda}$

**Geometry:**
- $r_2 = \sqrt{r^2 + (\frac{d}{2} + x'')^2}$
- $r_1 = \sqrt{r^2 + (\frac{d}{2} - x'')^2}$
- $|r_2 - r_1| = \sqrt{r^2 + (\frac{d}{2} + x'')^2} - \sqrt{r^2 + (\frac{d}{2} - x'')^2}$



$$
= r\sqrt{1 + \frac{(\frac{d}{2} + x'')^2}{r^2}} - r\sqrt{1 + \frac{(\frac{d}{2} - x'')^2}{r^2}}
$$





$$
\approx \frac{r}{2}\left(1 + \frac{(\frac{d}{2} + x'')^2}{2r^2} - 1 - \frac{(\frac{d}{2} - x'')^2}{2r^2}\right)
$$





$$
= \frac{1}{2r^2}\left((\frac{d}{2} + x'')^2 - (\frac{d}{2} - x'')^2\right)
$$





$$
= \frac{1}{2r}\left((\frac{d}{2})^2 + dx'' + x''^2 - (\frac{d}{2})^2 + dx'' - x''^2\right)
$$





$$
= \frac{dx''}{r}
$$



- Phase difference from s to top and bottom holes
- Phase difference from p to top and bottom holes

$\cos(a+b) = \cos(a)\cos(b) - \sin(a)\sin(b)$

When extended source is represented by many point sources:



$$
I(P) = I_1(P) + I_2(P) + 2\sqrt{I_1(P)}\sqrt{I_2(P)}\int_{-S/2}^{S/2}\cos\left[\bar{k}\left(\frac{d}{R}\right)x + \bar{k}\left(\frac{d}{r}\right)x''\right]dx''
$$





$$
= I_1(P) + I_2(P) + 2S\sqrt{I_1(P)}\sqrt{I_2(P)}\text{sinc}\left[\left(\frac{d}{\lambda R}\right)S\right]\cos\left[\bar{k}\left(\frac{d}{R}\right)x\right]
$$


# Spatial Coherence and Grating Shift

## Note:



$$
\cos\left(\bar{k}\left(\frac{d}{R}\right)x + \bar{k}\left(\frac{d}{r}\right)x''\right)
$$



- Phase shift φ (in radians)
- Grating freq. (in radians)

---

## ⇒ When two different point sources are used, gratings are shifted by an amount (distance along source):



$$
\bar{k}\left(\frac{d}{R}\right)x \cdot \left(\frac{r}{\bar{k}d}\right) = \frac{xr}{R}
$$



| Term | Description |
|------|-------------|
| Phase shift in radians φ | |
| Period of grating (for 2π radians) | ⇒ Physical grating shift for φ phase shift |

---

## Diagram

[Diagram showing two source points S₁ and S₂ separated by distance d, at distance R from measurement point, with shift = xr/R indicated]

- ← cannot to period of entire fringe →

---

## Condition for Negligible Degradation

If $\frac{xr}{R} \ll \frac{b}{2\pi} \cdot \frac{r}{\bar{k}d}$

shift ↓ ← Period (through one radium)

or $d \ll \frac{2\pi R}{kx} = \frac{R\lambda}{\pi x}$



$$
\frac{d}{R} \ll \frac{d}{\lambda}
$$



For negligible degradation of fringe pattern:
⇒ simply require phase shift $\phi \ll \pi$ ⇒ $\bar{k}\left(\frac{d}{r}\right)x \ll \pi$



$$
\Rightarrow d \ll \frac{\lambda R}{2x}
$$



For maximum x separation, $x_{\max} = S/2$: $\left[\text{sinc}\left(\frac{dS}{\lambda R}\right)\right]$
# Van Cittert-Zernike Theorem

## Fringe Visibility Condition

**Notice:** Fringes vanish if $d = \frac{\bar{\lambda}R}{S}$

or $\boxed{d = \frac{\bar{\lambda}}{\theta_s}}$ where $\theta_s = \frac{S}{R}$ = angular size of source

**Note:** From Fourier aperture produces: $\propto \frac{b}{\bar{\lambda}}$, $\sin\theta \approx \theta = \frac{\lambda}{b} = \tan\frac{\lambda}{b}$

$\therefore b \approx \frac{R\bar{\lambda}}{S}$, exactly like above spatial [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) eqn.

---

## Generalization: Van Cittert-Zernike Theorem

**Distances from $P_1$ & $P_2$ meas. pts. to source**



$$
\text{Spatial Coherence} \Rightarrow \gamma_{12}(0) = \frac{\int_S I(x_s, y_s) e^{i\bar{k}(R_1-R_2)} dS}{\int I(x_s, y_s) dS}
$$



where [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) function $\gamma = \frac{\Gamma_{12}(0)}{\sqrt{\Gamma_{11}(0)\Gamma_{22}(0)}}$

**Same mathematics as diff pattern of coherent wave converging on $P_1$ after passing through transparency having amplitude transmittance proportional to intensity distribution of incoherent source.**

$I(x_s, y_s)$ at $P_1$

**Note:** $\bar{k}(R_1-R_2)$ is the phase shift of the cosine fringe pattern.

---

This is exactly like the [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) equation

⇒ If $P_1$ & $P_2$ are close to the axis & far from source, we have an equation like [Fraunhofer diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/fraunhofer_diffraction/)

and hence $I(x_s, y_s)$ and $\gamma_{12}(0)$ are [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) related.

---

## Example: Measure the size of Betelgeuse (red giant)

[Diagram showing light from star passing through Michelson Stellar Interferometer with separation d]

## Measuring Stellar Angular Size

Assuming star is round, we have $\gamma_{12}(0)$ given as the F.T. of a circle ⇒

[Graph showing $\gamma_{12}(0)$ vs P with width of [coherence](/notes/areas/electrical_engineering/physical_optics/definitions/coherence/) area marked, showing $J_1(anl)$ behavior starting at 1 and decreasing to first zero at 1.22]



$$
\Rightarrow d_w = \frac{1.22\bar{\lambda}}{\theta_s} \leftarrow \text{Fringe disappear}
$$



First zero of fringe visibility ← Angular size of source

Measurement: $d_w = 2.6$ meters



$$
\Rightarrow \theta_s = \frac{1.22\bar{\lambda}}{d_w} = 0.047 \text{ sec of arc}
$$



From known distance ⇒ diameter is 280 times that of the sun — **Red Giant**

---

## Notes:

- Michelson in principle could also measure phase info. of $\gamma_{12}(0)$ and hence an inverse FT would reconstruct the intensity.

- Atmospheric turbulence prevents this from happening in practice. Hence, Michelson measured short-term visibility magnitude only

- Various techniques can be used to recover phase info in presence of random fluctuations ⇒ Speckle interferometry, speckle masking (triple product correlation), and phase retrieval (Gerschberg-Saxton algorithm)
# Page 106

[This page appears to be blank or contains minimal content]
# Incoherent Case: Optical Transfer Function

## Optical Transfer Function (OTF)

★ Modulation Transfer Ftn. (MTF) is the modulus of OTF

[Block diagram showing: $A_1 + A_2$ → [1] → $\mathcal{F}\{A_1\} + \mathcal{F}\{A_2\}$]

System is linear for general amplitude ftn.

---

## Consider a case where $A_1$ & $A_2$ contain phase terms which are random functions of time

[Diagram showing optical system with random phase terms $\delta(x-x_1)e^{i\phi_1(t)}$, $\delta(x-x_2)e^{i\phi_2(t)}$, $h(x-x_1)e^{i\phi_1(t)}$, $h(x-x_2)e^{i\phi_2(t)}$]



$$
A = h(x-x_1)e^{i\phi_1(t)} + h(x-x_2)e^{i\phi_2(t)}
$$



**Average Intensity is the directly observable quantity:**



$$
\langle I \rangle = \frac{1}{T}\int_0^T \left|h(x-x_1)e^{i\phi_1(t)} + h(x-x_2)e^{i\phi_2(t)}\right|^2 dt
$$





$$
= \frac{1}{T}\int_0^T |h(x-x_1)|^2 dt + \frac{1}{T}\int_0^T |h(x-x_2)|^2 dt + \frac{1}{T}\int_0^T h(x-x_1)h^*(x-x_2)e^{i(\phi_1-\phi_2)} dt
$$




$$
+ \frac{1}{T}\int_0^T h^*(x-x_1)h(x-x_2)e^{-i(\phi_1-\phi_2)} dt
$$


# Incoherent Imaging

## Incoherent Case Analysis

If $\phi_1$ and $\phi_2$ are uncorrelated and uniformly distributed from 0 to $2\pi$, then:



$$
\frac{1}{T}\int_0^T e^{i(\phi_1-\phi_2)} dt = 0
$$



and



$$
\langle I \rangle = \langle |h(x-x_1)|^2 \rangle + \langle |h(x-x_2)|^2 \rangle
$$





$$
\therefore \text{System is linear in intensity with impulse response}
$$





$$
\langle |h(x)|^2 \rangle
$$



---

## Coherent vs Incoherent Case

**Coherent case:**
- $\langle E_1 \rangle = 0$
- $\langle E_2 \rangle = 0$  (only)
- $\langle E_1 + E_2 \rangle = 0$  (known)
- $\langle E_1 E_2^* \rangle = $ (statistics passes)
- $\langle |E|^2 \rangle + \langle |E|^2 \rangle$
- $= \langle E_1 \rangle * \langle E_2 \rangle$  zero fractions
- $= I_1 + I_2$

$\therefore$ Incoherent light is linear in intensity

---

## Transfer Functions

We must use an intensity [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) $I(x, y)$:

**[Impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) is** $|h(x, y)|^2$ and every thing is coherent from a pt. source. Every thing is coherent from a pt. source.



$$
G_q(f_x, f_y) = K \iint |h(x_i - \bar{x}_o, y_i - \bar{y}_o)|^2 I_g(\bar{x}, \bar{y}) d\bar{x}_o d\bar{y}_i
$$



[Diagram showing optical system]

If we define normalized frequencies: ("Normalize to zero-frequency" values)



$$
G_q(f_x, f_y) = \iint I_g(\bar{x}_o, \bar{y}_o) \exp[-j2\pi(f_x\bar{x}_o + f_y\bar{y}_o)] d\bar{x}_o d\bar{y}_i
$$





$$
\iint I_g(\bar{x}_o, \bar{y}_o) d\bar{x}_o d\bar{y}_i
$$





$$
G_i(f_x, f_y) = \iint I_i(x_i, y_i) \exp[-j2\pi(f_x x_i + f_y y_i)] dx_i dy_i
$$





$$
\iint I_i(x_i, y_i) dx_i dy_i
$$


# Optical Transfer Function



$$
\mathcal{H}(f_x, f_y) = \frac{\iint |\tilde{h}(x_i, y_i)|^2 \exp[-j2\pi(f_x x_i + f_y y_i)] dx_i dy_i}{\iint |h(x_i, y_i)|^2 dx_i dy_i}
$$



---

## Then



$$
G_i(f_x, f_y) = \mathcal{H}(f_x, f_y) \cdot G_g(f_x, f_y)
$$



Where:
- $\mathcal{H}$ = **[optical transfer function](/notes/areas/electrical_engineering/physical_optics/definitions/optical_transfer_function/) (OTF)**
- $|\mathcal{H}|$ = **modulation [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) (MTF)**

---

## Note:



$$
\mathcal{H}(f_x, f_y) = \frac{\mathcal{F}\{|\tilde{h}(x_i, y_i)|^2\}}{\mathcal{F}\{|\tilde{h}(x_i, y_i)|^2\}|_{f_x=0, f_y=0}}
$$



From the autocorrelation theorem (Wiener-Khinchin):



$$
\mathcal{F}\{|\tilde{h}(x_i, y_i)|^2\} = H(f_x, f_y) \circledast H^*(f_x, f_y)
$$





$$
\therefore \mathcal{H}(f_x, f_y) = \frac{H(f_x, f_y) \circledast H^*(f_x, f_y)}{(H(f_x, f_y) \circledast H^*(f_x, f_y))|_{f_x=0, f_y=0}}
$$



---

## Properties:

1. $\mathcal{H}(0, 0) = 1$

2. Fourier of a real ftn. ⟹ $2 \cdot \mathcal{H}(-f_x, -f_y) = \mathcal{H}^*(f_x, f_y)$

3. Schwarz inequality ⟹ $|\mathcal{H}(f_x, f_y)| \leq |\mathcal{H}(0, 0)|$
# CTF and OTF Examples

## Examples:

Consider the CTF and OTF of a system with a square pupil:

[Diagram of square pupil with dimensions ← l →, ↑ l ↓]

---

## Coherent Transfer Function (CTF):



$$
H(f_x, f_y) = \text{rect}\left(\frac{\lambda d_i f_x}{l}\right) \text{rect}\left(\frac{\lambda d_i f_y}{l}\right)
$$

 — **Coherent Limit**

---

## Optical Transfer Function (OTF):



$$
\mathcal{H}(f_x, f_y) = H(f_x, f_y) \circledast H(f_x, f_y)
$$

 — **Incoherent Limit**



$$
= \left[\text{rect}\left(\frac{\lambda d_i f_x}{l}\right) \circledast \text{rect}\left(\frac{\lambda d_i f_x}{l}\right)\right]\left[\text{rect}\left(\frac{\lambda d_i f_y}{l}\right) \circledast \text{rect}\left(\frac{\lambda d_i f_y}{l}\right)\right]
$$





$$
= \text{tri}\left(\frac{\lambda d_i f_x}{l}\right) \text{tri}\left(\frac{\lambda d_i f_y}{l}\right)
$$



---

[Graph showing CTF (rectangular) and OTF (triangular) curves plotted against $f_x$, with cutoff frequencies marked at $-\frac{1}{\lambda d_i}$, $-\frac{1}{2\lambda d_i}$, $\frac{1}{2\lambda d_i}$, $\frac{1}{\lambda d_i}$]

---

⇒ An incoherent system has a cut-off at twice the freq. of a coherent system. However, this does not really mean it has twice the resolving power.

**Two F numbers:** A given distance range in two constraints: similarity to a certain spatial freq. in an incoherent system, propagated at this distance within the lines on wave. The number of points in biological equal threshold of finding a
# Physical Interpretation of OTF

## Physical Interpretation:

[Diagram showing rotating diffuser with cone of plane waves passing through grating, creating Huygens sources]

- For this freq, the 2 pencil beams are shifted in angle depending on the illumination angle

- Grating is formed by any two pairs of Huygens sources that are spaced by a distance ($f_x \cdot \lambda d_i$)

- For low spatial frequencies, there are more pairs than at high frequencies (& thus large separations)

- **Two Finger rule:**

[Diagram showing circular aperture with two points marked × ×, and chord transform illustration]

**MTF is proportional to the number of locations two points occur at a specific separation and orientation ⇒ correlation**

- Note redundancy in incoherent system which gives rise to noise suppression (coherent noise).
# Pupil Shapes of Mammals

## Pupil Shapes of Mammals:

| Animal | Pupil Shape | MTF |
|--------|-------------|-----|
| Horse & goat | [Horizontal rectangular pupil] | [MTF graph showing vert/horiz curves, higher horizontal resolution] |
| Domestic cat | [Vertical slit pupil] | [MTF graph showing vert/horiz curves, higher vertical resolution] |
| Humans | [Circular pupil] | [MTF graph showing symmetric response] |
# Generalized Pupil Function

## I. Generalized Pupil Function

[Diagram showing [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) limited system with pupil function P(x,y)]

**[Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) limited system**
⇒ [Impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) = F.T. of pupil function (aperture)

---

## Aberrations

→ Aberrations are phase errors in optical system
→ If phase error at exit pupil is $kW(x,y)$, $k = 2\pi/\lambda$

We define a **generalized pupil function**:



$$
\boxed{P(x,y) = P(x,y) \exp[jkW(x,y)]}
$$



---

## Coherent Case

$\therefore$ [Impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) is F.T. of $\mathbb{P}(x,y)$

We also have the coherent [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) = generalized pupil ftn.



$$
H(f_x, f_y) = \mathbb{P}(\lambda d_i f_x, \lambda d_i f_y)
$$





$$
= P(\lambda d_i f_x, \lambda d_i f_y) \exp[jkW(\lambda d_i f_x, \lambda d_i f_y)]
$$



$\therefore$ Effect of aberrations is simply to apply phase distortions to the pass band. It does not affect the band limit.
# Incoherent Case OTF with Aberrations

## Incoherent Case



$$
\mathcal{H}(f_x, f_y) = \frac{\mathbb{P}(\lambda d_i f_x, \lambda d_i f_y) \circledast \mathbb{P}^*(\lambda d_i f_x, \lambda d_i f_y)}{(\mathbb{P}(\lambda d_i f_x, \lambda d_i f_y) \circledast \mathbb{P}^*(\lambda d_i f_x, \lambda d_i f_y))|_{f_x=0, f_y=0}}
$$



→ In general, aberrations lower the contrast of a certain spatial frequency
# Aberrations and OTF

## Examples:

[Diagram showing CTF (rectangular) and OTF (triangular) curves]

---

## Aberrations and Their Effect on the OTF

### Focusing Error (Square lens of width l)

Recall imaging relation: $\frac{1}{d_i} + \frac{1}{d_o} - \frac{1}{f} = 0$

Focusing error: $\frac{1}{d_i} + \frac{1}{d_o} - \frac{1}{f} = \epsilon$

Then, we have an extra term in the pupil function:

**Recall:** Point spread ftn for single lens imaging:


$$
h(x_o, y_o) = \frac{1}{\lambda d_o d_i}
$$




$$
\mathcal{F}\{P_{\text{pupil}} \cdot \exp[i\frac{k}{2}(\frac{1}{d_o} + \frac{1}{d_i})(x^2+y^2)]\}
$$




$$
= \exp[ik(\frac{1}{2d_o} + \frac{1}{2d_i})x \times (\frac{x_o}{d_o} + \frac{x_i}{d_i})]
$$





$$
P(x,y) \exp\left[jk\epsilon\frac{(x^2+y^2)}{2}\right]
$$



and $W = \frac{\epsilon l^2}{8}$ where W is the maximum path length error along x or y axis.



$$
\mathcal{H}(f_x, f_y) = \Lambda\left(\frac{f_x}{2f_o}\right)\Lambda\left(\frac{f_y}{2f_o}\right)
$$





$$
\times \text{sinc}\left[\frac{8W}{\lambda}\left(\frac{f_x}{2f_o}\right)\left(1-\frac{|f_x|}{2f_o}\right)\right] \text{sinc}\left[\frac{8W}{\lambda}\left(\frac{f_y}{2f_o}\right)\left(1-\frac{|f_y|}{2f_o}\right)\right]
$$



[Diagram showing lens with dimension l]

$x = \frac{l}{2}$, $\epsilon\frac{(x^2+y^2)}{2} = \epsilon\frac{l^2}{8}$

Note: $W = 0$ ⇒ [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) limit

$f_o = \frac{l}{2\lambda d_i}$ ← lens diameter

[Graph showing OTF curves for W=λ, W=λ/4, and W=0 ([diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) limit), with contrast reversal indicated]
# Aberration Function Effects

## Aberration Function

[Diagram showing pupil with different zones (a), (b) having phases $e^{j\phi_a}$, $e^{j\phi_b}$ and their contribution to aberration function, with arrows indicating "from (a)" and "from (b)"]

⇒ Frequency is not represented

**Aberration Ftn**

---

## Notes:

1. If complete cancellation of a freq. requires a $\lambda/2$ error

2. Contrast reversal requires > $\lambda/2$ error.
# Coherent Imaging Effects

## II. Coherent Imaging Effects

1. Ringing
2. Speckle

---

## A. Ringing of a Knife Edge (Coherent)



$$
I_{im}(x') = \left|\int_{-\infty}^{\infty} \sqrt{I_{ob}(x)} \cdot K\left(\frac{x'}{q} + \frac{x}{p}\right) dx\right|^2
$$



where:
- $I_{ob}(x)$ = object intensity (assume no phase component)
- $K\left(\frac{x'}{q}\right)$ = amplitude [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) of the lens
- $p$ = object distance
- $q$ = image distance

---

## Consider a square aperture of size "2a"

**Amplitude [Impulse Response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/):**


$$
K\left(\frac{x'}{q}\right) = \text{sinc}\left(ka\frac{x'}{q}\right), \quad k = \frac{2\pi}{\lambda}
$$



and


$$
I_{im}(x') = \left|\int_{-\infty}^{\infty} \sqrt{I_{ob}(x)} \text{sinc}\left[ka\left(\frac{x'}{q} + \frac{x}{p}\right)\right] dx\right|^2
$$



---

## Consider a Knife Edge Object



$$
\Rightarrow I_{ob}(\bar{x}) = \begin{cases} 1 & x > 0 \\ 0 & x < 0 \end{cases} = \text{step}(x)
$$





$$
I_{im}(x') = \left|\int_{-\infty}^{\infty} \text{step}(x) \text{sinc}\left[ka\left(\frac{x'}{q} + \frac{x}{p}\right)\right] dx\right|^2
$$





$$
= \left|\int_0^{\infty} \text{sinc}\left[ka\left(\frac{x'}{q} + \frac{x}{p}\right)\right] dx\right|^2
$$





$$
= \left[\frac{1}{2} - \frac{1}{\pi} Si\left(\frac{kax'}{q}\right)\right]^2
$$



## Sine Integral Function

where: $Si(\theta) = \int_0^{\theta} \frac{\sin\theta}{\theta} d\theta$ = **sine integral function**

---

## Physical Meaning (Coherent Case):

[Graph showing oscillating response with overshoot, then settling to steady state]

⇒ [Graph showing coherent edge response with ringing/oscillations]

---

## Incoherent Case



$$
I_{im}(x') = \int_{-\infty}^{\infty} I_{ob}(x) \cdot K\left(\frac{x'}{q} + \frac{x}{p}\right) K^*\left(\frac{x'}{q} + \frac{x}{p}\right) dx
$$



**Intensity [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) of square aperture (size "2a"):**



$$
\left|K\left(\frac{x'}{q}\right)\right|^2 = \text{sinc}^2(kax'/q)
$$





$$
\Rightarrow I_{im}(x') = \frac{1}{2} - \frac{1}{\pi}\left[Si\left(\frac{2kax'}{q}\right) - \frac{1 - \cos^2\left(\frac{kax'}{q}\right)}{kax'/q}\right]
$$



---

## Physical Meaning (Incoherent):

**Comparison between coh. & incoh.**

[Graph showing step input → smooth monotonic response (incoherent)]

[Graph showing comparison with coherent response showing oscillations vs incoherent smooth response, with marking at $-\frac{1}{2}$ in amplitude and $= \frac{1}{4}$ in intensity]

**Ref:** Considine, P.S., JOSA **56**, 1001, (1966)
# Speckle

## B. Speckle

**(Viewpoint #1: Angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) spectrum)**

(Not just for laser light, but radar & sonar as well)

**Coherent light reflects off of a "rough" white surface**

"Rough" means surface varies in height by several wavelengths. Since screen is white, no amplitude modulation of illumination occurs.

[Diagram showing rough surface with incident light creating scattered waves]

At the plane, we have the original illum. $A(x,y)$ times a random phase $e^{j\phi(x,y)}$ due to the surface

→ We can decompose the amplitude at the surface into an angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) spectrum. Thus, at this surface, all plane waves add together in such a way as to create a uniform amplitude function

→ If an optical system can capture all the plane waves and recombine them into an image, a uniform amplitude function results

[Diagram showing optical system capturing and recombining plane waves, with speckle pattern in image]

**Image contains exactly the same set of plane waves as the object ⇒ uniform amplitude phase function**
# Speckle Formation


→ We can think of each point of the image (or object) as being a summation of many plane waves of random phases. Since light is coherent, plane waves add in amplitude as phasors.

[Diagram showing phasor addition with unit circle, indicating "Every point in image is composed of a sum of phasors which always add up to 1"]

→ Now consider an optical system which had a small aperture so that some of the plane waves were not passed through.

[Diagram showing optical system with aperture blocking some plane waves]

**Histogram of speckle:**


$$
p(I) = \frac{\exp(-I/I_o)}{I_o}
$$



where $I_o = \langle I \rangle$ = mean intensity

[Graph showing histogram of speckle intensity - exponential decay curve from peak at 0, with marking showing "constant amplitude" and "from only 3 plane waves mixed" at points, and "Unit Circle" marker]

**Phasor Diagram**

The amplitude is no longer a constant, but rather is a random value which changes with every point on surface.

This is **speckle**. Since the human eye captures only a very small angle of plane waves, speckle is usually seen with any diffuse object (diffuse means "rough" is scattered into a wide angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) excitation).

## Speckle Statistics

→ We can think of each point of the image (or object) as being a summation of many plane waves of random phases. Since light is coherent, plane waves add in amplitude as phasors.

[Phasor diagram showing unit circle with multiple vectors adding to result]

**Every point in image is composed of a sum of phasors which always add up to 1**

---

→ Now consider an optical system which had a small aperture so that some of the plane waves were not passed through.

[Diagram showing angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) spectrum with limited aperture]

**Histogram of speckle:**



$$
p(I) = \frac{\exp(-I/I_o)}{I_o}
$$



where $I_o = \langle I \rangle$ = mean intensity

[Histogram showing exponential decay of intensity probability, with annotations:
- "constant amplitude from only 3 plane waves mixed"
- Unit circle diagram showing phasor addition]

**Phasor Diagram**

The amplitude is no longer a constant, but rather is a random value which changes with every point on surface.

This is **speckle**. Since the human eye captures only a very small angle of plane waves, speckle is usually seen with any diffuse object (diffuse means "rough" is scattered into a wide angular [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) excitation).

## Speckle (Viewpoint #2: Impulse response of optical system)

→ The [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) of an imaging system (sometimes called its point-spread function) is given by the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the aperture: $\mathcal{F}\{P(\lambda d_i \bar{x}, \lambda d_i \bar{y})\}$

Thus, if the aperture is a circle, the [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) is $\text{somb}(\rho)$

[Diagram showing phase front $e^{i\phi_o}$ passing through aperture, creating $\text{somb}(r) \propto \frac{J_1(ar\bar{s})}{s}$]

→ A rough surface now consists of many points, each with its own random phase. This gives rise to many $\text{somb}(r)$ ftns., each with random phase.

[Diagram showing overlapping somb functions]

When somb ftns overlap, amplitudes = sum. However, due to the random phase of each, this sum can either add or subtract. Thus, overlap points are not uniform, and result in **speckle**

### Notes:
★ 1) As lens gets larger (better resolution) size of speckle gets smaller
2) Size of speckle is ≈ [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) limit of lens
# Apodization

## Apodization - What is it?

[Diagram showing aperture with tapered edges] ↔ [Corresponding F.T. pattern]

**A - pod** ← eq: podiatrist, pseudopod
↑     ↑
no   feet  ⇒ To cut off or remove the feet

This is like an F.T. system, except that the aperture has been passed up to the lens plane.

**Apodization is the shaping of the aperture of an optical system to control side lobes (or sometimes enhance them to provide improved resolution).**

---

## → Consider a typical astronomy problem:

Resolve a double star system where one star is $10^2$ times brighter than the other:

[Diagram showing bright star and dark companion with [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) patterns, showing side lobes at $-\frac{2}{\lambda}$ and $\frac{2}{\lambda}$]

- We desire to reduce the side lobes as much as possible

**Amplitude:** $\text{rect}\left(\frac{x}{a}\right) \xrightarrow{\mathcal{F}} a\,\text{sinc}(au)$

**Intensity:** $I(u) = |a\,\text{sinc}(au)|^2 \propto \frac{1}{u^2}$ ← Spatial freq = sinθ

$I(u) \sim \frac{1}{u^2}$

---

## Try using an amplitude mask with a (near coherent) triangular shading (Bartlett window)

[Diagram showing triangular aperture function with width a]

**Amplitude [Impulse Response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/):**


$$
\mathcal{F}\left\{\text{tri}\left(\frac{x}{a}\right)\right\} = \mathcal{F}\left\{\text{rect}\left(\frac{2x}{a}\right) \circledast \text{rect}\left(\frac{2x}{a}\right)\right\} = \left(\frac{a}{2}\right)^2 \text{sinc}^2\left(\frac{au}{2}\right)
$$



where $\text{tri}(x) = \begin{cases} 1-|x| & |x| \leq 1 \\ 0 & \text{else} \end{cases}$

$I(u)$ — Intensity impulse: $I(u) = \left(\frac{a}{2}\right)^4 \text{sinc}^4\left(\frac{au}{2}\right)$

$\propto \frac{1}{u^4}$

**Note:** Main lobe is increased by 2× because some high spatial freq's removed.

[Graph comparing intensity responses, showing $\frac{1}{u^2}$ vs $\frac{1}{u^4}$ decay]
# Apodization - Parzen Window

## Try Parzen Window



$$
\mathcal{F}\left\{\text{tri}\left(\frac{ux}{a}\right) \circledast \text{tri}\left(\frac{ux}{a}\right)\right\}
$$



Choose half size so autocorrelation fits in same space



$$
\mathcal{F}\left\{\text{tri}\left(\frac{ux}{a}\right) \circledast \text{tri}\left(\frac{ux}{a}\right)\right\} = \left(\frac{a}{4}\right)^4 \text{sinc}^4\left(\frac{au}{4}\right)
$$



[Diagram showing Parzen window shape]
- 1st zero at $\frac{4}{a}$

⇒ Intensity fall off: $\propto \frac{1}{u^8}$

**Note:** As window gets "smoother", side lobes decrease faster.

[Note: [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) represents a low-pass filter operation (in the case), reducing the high spatial freq's and hence the sidelobes]

---

## Theorem:

The asymptotic behavior of a F.T. is given by the order of the discontinuity in the aperture.

| Discontinuity | Fourier |
|---------------|---------|
| ⌐⌐ ← Discontinuous in 0th derivation | ⇒ $\frac{1}{x}$ ← Spectr |
| /\ " " 1st derivation | ⇒ $\left(\frac{1}{x}\right)^2$ |

In general, if the discontinuity is of order n, the side lobes fall off as $\left(\frac{1}{x^{(n+1)}}\right)^2$

---

## Note:

**Central limit theorem** states that in general, if we convolve something enough times, we end up with a Gaussian:



$$
g(x) \circledast g_2(x) \circledast g_3(x) \circledast \cdots \to \text{Gauss}(x)
$$



This function is continuous in all derivatives (but also is ∞ in extent), has no sidelobes, and falls off faster than a power series ($e^{-x^2}$)

- Gaussian apertures can be created by evaporating onto a substrate using a spinning aperture that looks like: [spiral diagram]

or

Absorber: $e^{-x^2}$
But $\frac{ar}{2} r^2$
⇒ $t(r) = e^{-\alpha r^2}$
# FFT Windows and Mask Apodizers

## Note similarity to FFT Windows

- Bartlett - Triangular
- Blackman
- Hamming
- Hanning - Raised cosine
- Kaiser Bessel
- Parzen

---

## Mask Apodizers

It is often difficult to shade a large telescope mirror with a variable density apodizer. Hence, rectangular masks are sometimes used.

[Diagram showing telescope mirror with square apodizer]



$$
\text{rect}(x)\text{rect}(y) \xrightarrow{\mathcal{F}} A = \frac{\sin(\pi x)\sin(\pi y)}{\pi^2 xy}
$$





$$
I \propto \frac{\sin^2(\pi x)\sin^2(\pi y)}{x^2 y^2}
$$





$$
I_{(x\text{-axis})} \sim \frac{1}{x^2}
$$





$$
I_{(y\text{-axis})} \sim \frac{1}{y^2}
$$





$$
I_{(45° \text{ axis})} \sim \frac{1}{r^4}
$$



[Diagram showing circular aperture]



$$
\text{circ}(r) \xrightarrow{\mathcal{F}} A = \frac{J_1(2\pi r)}{r}, \quad I = \frac{J_1^2(2\pi r)}{r^2}
$$



For large r, $J_1(r) \sim \frac{1}{\sqrt{r}}$



$$
\Rightarrow I \sim \frac{1}{r^3}
$$


# Blocking Aperture Apodizers

## Note:

This apodizer redistributes the $\frac{1}{r^3}$ sidelobes of a circle (which are uniformly distributed in angle) into $\frac{1}{r^2}$ and $\frac{1}{r^4}$ regions (x-axis/y-axis and 45°). It is of course only useful if observation is to be only along a line (e.g., double stars), and the orientation is known.

[Diagram showing square aperture pattern with low sidelobes from square aperture ($\frac{1}{r^4}$) marked]

---

## Blocking Aperture "Apodizers"

### Circular Blocks:

[Two diagrams showing circular apertures with central obscuration]



$$
g(r, \theta) = \text{circ}\left(\frac{r}{r_1}\right) - \text{circ}\left(\frac{r}{r_2}\right)
$$





$$
f(r, \theta) = \text{circ}\left(\frac{r}{r_1}\right)
$$





$$
G(\rho) = 2\pi \int_0^{\infty} g(r') J_o(2\pi\rho r') r' dr' = \mathcal{H}\{g(r)\}
$$



([Hankel Transform](/notes/areas/electrical_engineering/physical_optics/definitions/hankel_transform/))
# Hankel Transform Examples

## Hankel Transform



$$
\mathcal{H}\left\{\text{circ}\left(\frac{r}{r_1}\right)\right\} = r_1 \frac{J_1(2\pi r_1 \rho)}{\rho}
$$





$$
\mathcal{H}\left\{\text{circ}\left(\frac{r}{r_1}\right) - \text{circ}\left(\frac{r}{r_2}\right)\right\} = r_1 \frac{J_1(2\pi r_1 \rho)}{\rho} - r_2 \frac{J_1(2\pi r_2 \rho)}{\rho}
$$



---

## Notice what happens in the limit $r_2 \to r_1$:



$$
f(r, \theta) = \delta(r - r_1) \leftarrow \text{Thin ring}
$$



[Diagram showing thin ring aperture]



$$
\mathcal{H}\{\delta(r - r_1)\} = 2\pi \int \delta(r' - r_1) J_o(2\pi\rho r') r' dr'
$$





$$
= 2\pi r_1 J_o(2\pi r_1 \rho)
$$



[Graph showing $J_1(\rho)$ with oscillations, and $J_o(\rho)$ below it]

**Note:**
- Main lobe decreases!
- Side lobes increase



$$
|J_1(\rho)/\rho|^2 \sim \frac{1}{\rho^3}
$$





$$
|J_o(\rho)|^2 \sim \frac{1}{\rho}
$$



(Recall: $J_n(x) \sim \sqrt{\frac{2}{\pi x}} \cos\left(x - \frac{n\pi}{2} - \frac{\pi}{4}\right)$ for large x)
# Wavefront Modulation - Film

## Wavefront Modulation

### Film:

[Diagram showing film structure with protective layer, emulsion (gelatin), base (plastic, glass), and film grains (Silver Halide)]

- Photon is incident on film grain
- Electron is promoted to conduction band and gets trapped in crystal dislocation
- Electron electrostatically attracts silver ions to form metallic silver site (Unstable)
- If this process is repeated within a few seconds, a two-atom unit is formed (stable).

**Reciprocity** { **Silver**

**Chemical development converts the entire grain (~10⁹ atoms) to silver if it has been exposed**

**Photographic gain (10⁹)**

**Stability** { Development will not take place if there are less than a threshold number (~4) of silver atoms.

- Fixing removes excess silver halide (which will eventually turn to silver)

(Show film grain pictures in Cathey)
# Film Characteristics (B&W Film)


## Wavelength Sensitivity

Silver halide will only form an electron-hole pair for $\lambda \leq 0.5\mu m$ (green, blue, violet)

⇒ To achieve a panchromatic response (B&W film), sensitizing dyes must be added.

---

### Exposure



$$
E(x, y) = I(x, y) \cdot T \quad (mJ/cm^2)
$$



(Total # of photons per cm²)

**Intensity** × **Time**

---

### Reciprocity

Simply implies film is affected by exposure only. Decrease in intensity can be compensated for by increase in time, etc.

---

### Intensity Transmittance



$$
T(x, y) = \text{local average}\left\{\frac{I_{\text{trans at }(x,y)}}{I_{\text{inc at }(x,y)}}\right\}
$$



---

### Density



$$
D = \log_{10}\left(\frac{1}{T}\right)
$$



**Note:** Transmittances **multiply**, but densities **add**

[Diagram showing three filters with transmittances $t_1$, $t_2$, $t_3$ and densities $D_1$, $D_2$, $D_3$]



$$
t_t = t_1 \cdot t_2 \cdot t_3
$$





$$
D_t = D_1 + D_2 + D_3
$$


# H-D Curve for Film


[Graph showing Density vs log E (Exposure) with slope = γ marked on linear region]

## For linear region of H-D curve:



$$
D = \gamma_n \log_{10} E - D_o = \gamma_n \log(IT) - D_o
$$



where γₙ = slope for Negative film

### Recall definition of density:



$$
D = \log_{10}\left(\frac{1}{T_n}\right)
$$



← Intensity transmittance



$$
\Rightarrow \log(T_n) = -\gamma_n \log(IT) + D_o
$$



or



$$
T_n = 10^{D_o}(IT)^{-\gamma_n} = K \cdot I^{-\gamma_n}
$$



← **positive constant**

---

**Note:** Because $\gamma_n$ is positive, this relation is never linear. However, with two photographic steps, we can achieve:



$$
T_p = K_p I^{-\gamma_p}, \quad \text{where } \gamma_p = -\gamma_{n_1}\gamma_{n_2}
$$



is a negative number

Thus, if $\gamma_p = 1$, relationship is **linear in int.**
# MTF of Film


## Simple Model of Film:

[Block diagram: E → Linear System → E' → Nonlinear Response (H&D eqn) → D]

**What is MTF of linear system**

---

### Exposure Pattern:



$$
E = E_o + E_1 \cos(2\pi f x)
$$



### Modulation def:



$$
M_i = \frac{E_1}{E_o}
$$



(Peak variation to background exposure)

---

From film, measure density variation, and infer log (exposure) through H&D curve

[Graph showing D vs log E with measured density and effective (log of) exposure marked]



$$
\therefore M(f) = \frac{M_{\text{eff}}(f)}{M_i(f)}
$$



(Show MTF of real film in Cathey)
# Spatial Light Modulators


## Liquid Crystals

(Show Goodman pg 168)

- Mechanical properties of liquids
- Optical properties of solids
- Ordering takes place along some planes but not others

**Nematic:** Ordering in one dimension only (all molecules are pointed in same direction)

**Smectic:** Ordering is in two dimensions. Randomness only within single layer.

**Cholesteric:** Molecules form long helical chains that are aligned in one dimension only. (Liquid crystal thermometers)

[Diagram showing helical structure with pitch ≈ λ₀ → white light reflects at ★ pitch ftn of temp.]

---

## ★ Consider Nematic Liquid Crystals Only (Twisted Nematic)

- Alignment performed by grooving substrate with polishing cloth.

[Diagram showing grooves with L.C. molecules aligned, showing 90° twist]
# Properties of Twisted Nematics

## ★ Properties of Twisted Nematics

### 1) Birefringence
(Light of one linear polarization state travels at a different velocity than the other: elliptic polarization results)

### 2) Optical Rotatory Power (Optical Activity)
(Light of one circular polarization state travels at a different velocity than the other: Linear polarization is simply rotated).

- This occurs in twisted nematics because the polarization state follows the twist, induced.

### 3) Large dipole moment along molecule axis

---

## ★ Operation of LCD (Displays)

- Ignore birefringence effects

[Diagram showing LCD operation in OFF state:
- Light → Polarizer → LC with 90° twist → polarization rotates → polarizer → off state]

[Diagram showing LCD operation in ON state:
- Light → Polarizer → Transp. Electrode → Electric Field → Transp. Electrodes → polarization unchanged → polarizer → Light ON state]
# Optical SLM (Hybrid Field Effect)

## Electrical-to-Optical SLM

Can be fabricated by matrix-addressing liquid crystal

---

## ★ Optical-to-Optical SLM (Hybrid-Field-Effect)

[Detailed diagram showing:
- Alignment layer with light blocking layer
- Photosensor (CdS, etc.)
- Pol., B.S.
- Input/Read
- L.C.
- Glass substrate (fiber-optic face plate)
- Mirror/ITO (trans. conductor)
- A-C field
- Write Light (Incoherent Image)]

- Crystal is twisted nematic with 45° twist
- Optical rotatory power is cancelled by reflection
- Light incident from write side causes resistance of photoconductor to reduce (bright parts of image)
- Voltage falls across L.C. and causes molecules to rotate. Speed increases since stress.
- Birefringence is maximized by a partial rotation of the molecules. If thickness is chosen to result in half-wave plate, polarization is rotated from trans, want to heriz (or vice versa).
# SLM Uses

## Uses:

1) **Incoherent-to-coherent light conversion**

2) **Wavelength conversion** ($\lambda_1 \to \lambda_2$)

3) **Optical amplification of image** (projection TV)

---

## Speed:

$\sim \frac{1}{30}$ sec cycle time for nematics

Somewhat faster for ferroelectric L.C.'s
# Acoustooptic Effect (12.7)

## Acoustooptic Effect

[Diagram showing:
- Absorber (Matched impedance)
- Travelling Acoustic Wave
- Acoustooptic Device (H₂O, TeO₂, Glass, SiO₂ (Quartz), etc.)
- Transducer
- hν input]

---

## AO Effect:

→ Transducer produces an acoustical wave in material

→ Acoustic compression & rarefaction produces small index of refraction change.

→ Light sees a travelling phase grating with period ($\sim 10^5$ cm/sec)



$$
\Lambda = \frac{V_s}{f} \leftarrow \text{Speed of acoustic propagation in material } (\sim 10^5 \text{ cm/sec})
$$



For Acoustic f up to 100 MHz ⇒ sinθ = 0.003 ($\lambda = 0.5\mu m$)



$$
\Lambda = \frac{V_s}{f} \approx 10\mu m
$$



⇒ $\Lambda \approx 10\mu m$

$\sin\theta = \frac{\lambda}{\Lambda}$ ⇒ θ ≈ 3° ($\lambda = 5\mu m$)

---

## → Interaction of Light and Thick Phase Grating

### Bragg Condition:

[Diagram showing Bragg [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) geometry with angles θᵢ, θᵣ and grating spacing Λ]

- Acoustic waves look like mirrors with very small reflectances due to index discontinuity.
- Prime indicates inside material

★ $\theta_i = \theta_r$ because of law of reflection at "mirror"

★ For all reflections to add in-phase:



$$
AO + \overline{OB} = m(\lambda_n) \leftarrow \text{Integer}
$$





$$
\Rightarrow \boxed{2\Lambda\sin\theta = m(\lambda/n)}
$$

 — **Bragg Condition (inside substrate)**

By Snell's laws: $\sin\theta = n\sin\theta'$ ⇒ $\boxed{2\Lambda\sin\theta = m\lambda}$ — Bragg condition (outside)
# Bragg Condition Notes

## Note:

1) Bragg condition true only for "thick" gratings

2) Only one [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) order (plus zero order from unreflected light) is produced

3) [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) order occurs only at specific input angles (Bragg condition)

---

## → What happens when grating is finite thickness?

[Diagram showing finite thickness grating with length L]

**Recall:** Gaussian confined in space bc ω₀ exists of plane waves: given by $\theta = \frac{\lambda}{\pi\omega_o}$

[Diagram showing [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) with K(θ) showing main lobe and side lobes at $\frac{\lambda}{L}$]

Acoustic wave of finite extent can be expressed as an [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) of infinite extent plane waves ([Angular Spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) Decomposition)

---

## ★ Several specific acoustic plane waves may satisfy Bragg equation

[Diagram showing multiple [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) orders at angles with:
- Off-axis "Acoustic plane" wave due to finite extent of transducer
- Acoustic → "plane" wave component
- Orders: 0, +1, +2 marked
- Angles: -2α, -α, α, 2α]



$$
2\Lambda\sin\theta = m\lambda
$$




$$
\sin\theta = m\left(\frac{\lambda}{2\Lambda}\right)
$$




$$
\Rightarrow \theta_B \approx \frac{m\lambda}{2\Lambda}
$$



Let $\alpha = \frac{\lambda}{2\Lambda}$ = Primary Bragg angle

— High order Bragg angles = mα
# Angular Plane Wave Spectrum (68)

## Angular Plane Wave Spectrum of Finite Acoustic Transducer

[Diagram showing possible Bragg angles (components of acoustic wave that satisfy Bragg condition) with:
- Peaks at -3α, -2α, -α, 0, α, 2α, +3 positions
- Light wave vectors at angles
- Transducer of width L shown]



$$
\alpha = \frac{\lambda}{2\Lambda}
$$



---

## Number of diffraction orders under main lobe of sinc ftn. (strong orders)



$$
N \approx \frac{2\left(\frac{\lambda}{L}\right)}{\frac{\lambda}{2\Lambda}} = \frac{4\Lambda^2}{\lambda L}
$$



(Not counting undiffracted order)

---

## Define Q parameter:



$$
\boxed{Q = \frac{2\pi\lambda L}{\Lambda^2}}
$$

 ← Inversely related to number of [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) orders present



$$
\Rightarrow Q \cdot N = (2\pi\lambda L / \Lambda^2)(4\Lambda^2 / \lambda L) = 8\pi
$$



---

### 1) $Q \gg 8\pi$ ⇒ Single diffraction order present (+ zero order) { **Bragg region**

### 2) $Q \ll 8\pi$ ⇒ Many orders present { **Raman-Nath** or **Debye-Sears region**
# Thin Grating (Raman-Nath)


[Diagram showing thin grating with thickness d ≪ λ]



$$
t(x, y) = \exp\left[i m \sin\left(\frac{2\pi}{\Lambda}x\right)\right], \quad m = \text{modulation index}
$$





$$
= \sum_{g=-\infty}^{\infty} J_g\left(\frac{m}{2}\right) \exp\left(i2\pi g\frac{x}{\Lambda}\right)
$$



↑ gth order Bessel ftn



$$
\mathcal{F}\{t(x,y)\} = \sum_{g=-\infty}^{\infty} J_g\left(\frac{m}{2}\right) \delta\left(\frac{\sin\theta}{\lambda} - \frac{g}{\Lambda}\right)
$$



where $\theta_o = \lambda/\Lambda$

[Graph showing $J_o(m/2)$, $J_1(m/2)$, $J_2(m/2)$ vs θ at positions θₒ, 2θₒ]

[Graph showing [Bessel Function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/) Behavior with $J_o$, $J_1$, $J_2$ curves vs m]

**Note:** At certain modulation index m, the zero order can disappear.

Decrease of intensity at higher orders as order of Bessel ftn. increases

---

## Amplitude modulation:



$$
u(t) = m(t)\cos(\omega t)
$$



Freq. mod.: ← Note: This changes the [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) angle



$$
u(t) = \cos((\omega + m\Omega)t)
$$

 ⇒ Scanner
# Particle Interaction Picture


## Photon:
- Energy = $\hbar\omega$
- Momentum = $\hbar \vec{k}$

## Phonon:
- Energy = $\hbar\omega_s$
- Momentum = $\hbar \vec{k}_s$

---

## Photon-Phonon Collision:

[Diagram showing k-vector triangle with:
- $\vec{k}_d$ (diffracted)
- $-\theta$
- $\vec{k}_s$ (scattered)
- $\vec{k}_i$ (incident)
- Conservation of Momentum notation]

**From picture:**


$$
k_s = 2k_d\sin\theta
$$



($|\vec{k}_d| \approx |\vec{k}_i|$ since $\omega_d = \omega_i + \omega_s \approx \omega_i$ and $|k| = \frac{\omega}{c}$)



$$
\Rightarrow 2\Lambda\sin\theta = (\Lambda/n)
$$



(m₁ corresponds to multiple phonon interactions) — **Bragg Law**

---

## Multiple Phonon Collisions

[Diagram showing multiple phonon interactions with:
- Acoustic wave at new angle due to spread of plane waves from finite acoustic aperture (Second Phonon)
- $|k_1| \approx |k_i| \approx |k_2|$
- Light vectors in a circle
- Acoustic wave at original Bragg angle (First phonon)]

⇒ Angle of phonon k vector corresponds to direction of propagation of acoustic wave
# Frequency Shift

## Also notice: Conservation of energy implies



$$
\hbar\omega_i + \hbar\omega_s = \hbar\omega_d
$$





$$
\Rightarrow \omega_d = \omega_i + \omega_s
$$



**Freq. of light has been shifted by sound freq.**

---

## ★ Physical Interpretation of Frequency Shift

### 1) Doppler Shift:

[Diagram showing acoustic wave ωs, travelling at velocity Vs with angle θ]



$$
\omega_d - \omega_i + \omega_s
$$





$$
\Delta\omega = 2\omega \frac{V_s}{c/n} \cdot \frac{\omega_i}{c/n}
$$

 ← velocity parallel to light

↑ Reflected wave

{Recall doppler shift given by $\omega_2 = \omega_1(1 - v_z/c_{/n})$ for source moving ⇒ $\omega_2 - \omega_i = \Delta\omega = \frac{\omega_i v_z}{c_m}$}

But $V_{\parallel} = V_s \cdot \sin\theta$ ⇒ $\Delta\omega = 2\omega\frac{V_s\sin\theta}{c/n}$

Also from Bragg Condition inside material:


$$
\sin\theta = \frac{m\lambda/n}{2\Lambda}
$$

 ← ($2\Lambda\sin\theta = (m\frac{\lambda}{n})$)

Bragg Condition.



$$
\Rightarrow \Delta\omega = \frac{2\omega V_s \cdot m\lambda/n}{2\Lambda \cdot c/n} = m\frac{2\pi V_s}{\Lambda} = m\omega_s
$$

 ← **Freq. shift = Acoustic wavelength = Acoustic Freq.**

(Higher order harmonics for higher [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) orders)

---

### 2) Moving Grating (thin)

[Diagram showing grating moving at velocity Vs with [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) order produced at $\sin\theta = \frac{\lambda}{\Lambda}$]

★ **Shift theorem:** $f(x) \overset{\mathcal{F}}{\longleftrightarrow} F(u)$ : $f(x-\alpha) \overset{\mathcal{F}}{\longleftrightarrow} F(u)e^{-j2\pi\alpha u}$

Shift by one acoustic period and observe phase at $\sin\theta = \frac{1}{\Lambda}$

⇒ $\alpha = \Lambda$, $u = \frac{\sin\theta}{\lambda} = \frac{1}{\Lambda}$



$$
\therefore f(x-\Lambda) \overset{\mathcal{F}}{\longleftrightarrow} F(u)e^{-j2\pi(\Lambda)(\frac{1}{\Lambda})} = F(u)e^{-j2\pi}
$$



↑ 2π phase shift
# Frequency Shift Summary (70)

## ★ When grating is shifted one acoustic wavelength, phase shifts by $2\pi$ = 1 cycle



$$
\text{Acoustic frequency}
$$



⇒ Travelling wave shifts grating $V_s$ wavelengths/sec



$$
\therefore \text{Phase of diffracted light shifts } \frac{V_s \text{ cycles}}{\text{sec}} / 2\pi
$$



⇒ **Frequency shift of $V_s$**
# On-axis Kinoforms


- Phase-only structures
- Phase functions are recorded modulo $2\pi$

## Examples:

| Conventional Element | Kinoform Equivalent |
|---------------------|---------------------|
| Prism [linear phase ramp with period λ] | [Sawtooth pattern with period $\frac{1}{T}\lambda$] |
| Conventional Element ↓ | Kinoform Equivalent ↓ |
| Lens [parabolic phase] | Kinoform Lens [wrapped phase pattern] |

---

## Consider a simple blazed grating

[Diagram showing blazed grating with incident light λ, orders m=-2, m=-1, m=0, m=1, m=2, angle θ, and period |d|←]
# Blazed Grating Analysis



$$
t(x) = \sum_{m=-\infty}^{\infty} \delta(x - mT) * \text{rect}\left(\frac{x}{T}\right) \exp(j2\pi\beta x)
$$



where $\beta = \frac{(n-1)d}{\lambda T}$

[Diagram showing phase profile with $\Delta\phi_{total} = (k' - k)\Delta h = \frac{2\pi(n-1)\Delta h}{\lambda}$]

$\Delta h = \frac{\alpha(\Delta x)}{T}$



$$
\Rightarrow \text{Far-field amplitude given by}
$$





$$
F(u) = \sum_{m=-\infty}^{\infty} \delta\left(u - \frac{m}{T}\right) \cdot \frac{\sin(\pi T(\beta - u))}{\pi T(\beta - u)}
$$



where: $u = \frac{\sin\theta}{\lambda}$

↑ [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) orders

$\beta = \frac{1}{2\pi} \frac{\partial\phi}{\partial x} = \frac{(n-1)d}{\lambda T}$

$= \frac{(n-1)d\Delta x}{T\lambda\Delta x}$

$= \frac{(n-1)d}{\lambda T}$

---

## ⇒ Intensity of mth diffraction order ($u = \frac{m}{T}$)



$$
\eta_m = |\alpha_m|^2 = \left|\frac{\sin(\pi T(\beta - \frac{m}{T}))}{\pi T(\beta - \frac{m}{T})}\right|^2
$$



We are usually interested in the first [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) order $(m=1)$



$$
\eta_1 = \left|\frac{\sin(\pi(\beta T - 1))}{\pi(\beta T - 1)}\right|^2
$$





$$
\therefore \eta_1 = 1 \quad \text{when } \beta = \frac{1}{T}
$$

 ⇒ Blaze goes from 0 to $2\pi$



$$
\exp\{j2\pi\beta x\} = \exp\left\{j2\pi\frac{x}{T}\right\}\bigg|_{x=0 \to T}
$$



**Also:** If $\beta = \frac{1}{T}$, $\frac{1}{nT} = \frac{(n-1)d}{\lambda T}$ ⇒ $d = \frac{\lambda}{n-1}$
# Blazed Grating Wavelength Dependence

## Note:

- Blazed grating is only 100% efficient for a single wavelength $\lambda_o$. (Let $d = \frac{\lambda_o}{n-1}$)

- For another wavelength $\lambda$, we have



$$
\beta = \frac{(n-1)d}{\lambda T} = \frac{\lambda_o}{\lambda T}
$$



(Recall $d = \frac{\lambda_o}{n-1}$ for max. efficiency)

and



$$
\eta_1 = \left|\frac{\sin\left(\pi\left(\frac{\lambda_o}{\lambda} - 1\right)\right)}{\pi\left(\frac{\lambda_o}{\lambda} - 1\right)}\right|^2
$$



[Graph showing efficiency $\eta_1$ vs wavelength $\lambda$, with peak of 1.0 at $\lambda_o$, dropping to ~0.5 at $0.5\lambda_o$ and $1.5\lambda_o$, approaching 0 at $2\lambda_o$]

- Efficiency reduced at other wavelengths
- Residual light occurs as higher orders, often adding a background haze (similar to scatter, but deterministic)
# Arbitrary Phase Profiles


Consider an arbitrary phase function

[Graph showing smooth phase function $\phi(x)$ vs x]

→ [Graph showing wrapped phase $\phi'(x)$ with discontinuities at $\pm\frac{1}{2}$, ranging between $-\frac{1}{2}$ and $\frac{1}{2}$]



$$
t_c(x) = \exp[j2\pi\phi(x)]
$$





$$
t_d = \exp[j2\pi\phi'(x)]
$$



where $\phi'(x) = |\phi(x)|_{\text{mod } \alpha}$

---

## ★ How do we analyze this structure?

- Use nonlinear (limiter) analysis

- Plot diffractive phase $\phi'(x)$ as a function of refractive phase $\phi(k)$

[Graph showing sawtooth relationship between $\phi'(x)$ and $\phi(x)$, with slopes at -1.5, -0.5, 0.5, 1.0, 1.5]

**Note:** Phase ranges from $-\frac{1}{2}$ to $\frac{1}{2}$ for generality

---

**Note:** $\phi'(x)$ is periodic in $\phi(x)$ with period = 1

⇒ $\exp[j2\pi\phi'(x)]$ is also periodic in $\phi(x)$

⇒ we can write this as a generalized [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)
# Fourier Analysis of Kinoforms



$$
\exp[j2\pi\phi'(x)] = \sum_{m=-\infty}^{\infty} C_m \exp[j2\pi m\phi(x)]
$$



↑ Transform variable is a function instead of a single variable.

---

## Solve for $C_m$ coefficients:



$$
C_m = \int_{-1/2}^{1/2} \exp[j2\pi\phi'(x)] \exp[-j2\pi m\phi(x)] \cdot d\phi(x)
$$



But $\phi'(x) = \alpha\phi(x)$ in the region $(-1/2, 1/2)$



$$
\therefore C_m = \int_{-1/2}^{1/2} \exp[j2\pi(\alpha - m)\phi(x)] \, d\phi(x)
$$





$$
= \frac{\sin(\pi(\alpha - m))}{\pi(\alpha - m)}
$$



---



$$
\Rightarrow \text{If } \alpha = 1, \text{ then } C_1 = 1 \text{ and } C_m = 0 \text{ for } m \neq 1
$$



If $\alpha \neq 1$, then additional orders exist.

---

## Note:

- For **blazed grating**, these orders are plane waves (of varying angle)

- For **Fresnel zone plate**, these orders are spherical waves (of varying ROC)

- For **arbitrary profile**, these orders are more complex wavefronts given by:



$$
\sum_{m=-\infty}^{\infty} C_m \exp[j2\pi m\phi(x)]
$$


# Binary Optics Fabrication


- Use microelectronics tools to fabricate step-wise approximation to desired profile

## Process Steps:

**(1)** [Expose pattern on resist layer on substrate]

**(2)** [Etch ($\frac{\lambda}{4}$) to create steps] ← P.R.

**(3)** [Expose second pattern]

**(4)** [Etch ($\frac{\lambda}{2}$) to create finer steps]

**(5)** [Result: Multi-level staircase pattern]

---

**Note:** N masks generate $2^N$ phase levels.
# Diffraction Efficiency of Step-Wise Phase Pattern

## ★ Diffraction Efficiency of Step-Wise Phase Pattern:

- Multi-level structure can be considered as the desired profile minus an error:

### Example:

[Diagram showing: N-levels continuous phase profile + off-set phase → Error → Desired minus sawtooth error pattern with period $\frac{\alpha}{N}$ and amplitude $\frac{1}{T}$, $\frac{2\pi}{N}$]



$$
t(x) = \exp\left(j2\pi\frac{x}{\alpha}\right) \cdot \left\{\left[\exp\left(-j2\pi\frac{x}{\alpha}\right) \cdot \text{rect}\left(\frac{Nx}{\alpha}\right)\right] * \frac{N}{\alpha}\text{comb}\left(\frac{Nx}{\alpha}\right)\right\}
$$



---

## Fourier transforming: (Angular plane wave spectrum where $u = \frac{\cos\theta}{\lambda}$)



$$
T(u) = \delta\left(u - \frac{1}{\alpha}\right) * \frac{\alpha}{N}\left\{\left[\delta\left(u + \frac{1}{\alpha}\right) * \text{sinc}\left(\frac{\alpha u}{N}\right)\right] \cdot \text{comb}\left(\frac{\alpha u}{N}\right)\right\}
$$





$$
= \delta\left(u - \frac{1}{\alpha}\right) * \left[\text{sinc}\left(\frac{\alpha u + 1}{N}\right) \cdot \sum_{n=-\infty}^{\infty} \delta\left(u - \frac{nN}{\alpha}\right)\right]
$$





$$
= \text{sinc}\left(\frac{u\alpha}{N}\right) \cdot \sum_{n=-\infty}^{\infty} \delta\left(u - \frac{nN+1}{\alpha}\right)
$$



---

## Inverse Transforming:



$$
\int_{-\infty}^{\infty} \text{sinc}\left(\frac{u\alpha}{N}\right) \sum_{n=-\infty}^{\infty} \delta\left(u - \frac{nN+1}{\alpha}\right) \exp(j2\pi ux) \, du
$$





$$
= \sum_{n=-\infty}^{\infty} \text{sinc}\left(\frac{nN+1}{N}\right) \exp\left(j2\pi\left(\frac{nN+1}{\alpha}\right)x\right)
$$



↑ Amplitude of plane-wave component

plane waves at angle $\frac{\sin\theta}{\lambda} = \frac{nN+1}{\alpha}$

↑ Integer # of phase levels

↑ 2 period
# Step-Wise Phase Efficiency

## Consider case where n = 0 (Diffraction component from error term)

[Diagram showing staircase approximation with n=0 marked, height λ]

**[Plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) component:** $\exp\left[j2\pi\frac{x}{\alpha}\right]$

**[Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) Efficiency:** $\eta = \left|\text{sinc}\left(\frac{1}{N}\right)\right|^2$

(true binary phase grating)

---

## Efficiency values:

| N | η |
|---|---|
| N = 2 (true binary phase grating) | η = 40.5% |
| N = 4 | η = 81% |
| N = 8 | η = 95% |
| N = 16 | η = 98.7% |
# Simple Spatial Filtering (Amplitude-only Filters) (30)

## Simple Spatial Filtering: (Amplitude-only Filters)

### Recall Optical set-up for spatial filtering:

[Diagram showing optical system with planes P1, P2, P3, focal lengths f between each]



$$
A \to f(x,y) \xrightarrow{H(x',y')} g(x,y) = f(x,y) * h(x,y)
$$



where: $h(x,y) = \mathcal{F}\mathcal{F}\{H(x,y)\}$

---

## Abbe-Porter Experiment:



$$
f(x,y) = \text{Ronchi ruling}
$$

 [Grid pattern with period a]

(gratings are 2 freq of filter)



$$
\Rightarrow f(x,y) = \left\{\left[\frac{1}{b}\text{comb}\left(\frac{x}{b}\right) \cdot \delta(y)\right] * \text{rect}\left(\frac{x}{a}\right)\right\} * \left\{\left[\frac{1}{b}\text{comb}\left(\frac{x}{b}\right) \cdot \delta(x)\right] * \text{rect}\left(\frac{y}{a}\right)\right\}
$$





$$
H(x',y') = \text{rect}\left(\frac{x'}{\epsilon}\right)\text{rect}\left(\frac{y'}{\epsilon}\right)
$$



[Diagram showing square filter with dimensions $\frac{1}{\epsilon} \times 2$, labeled "Two types of filter"]

---

## In plane P2, (ignoring constant phase factors and attenuation)



$$
F(x', y') = \mathcal{F}\mathcal{F}\{f(x,y)\}\bigg|_{z=\frac{x'}{\lambda f}, \eta=\frac{y'}{\lambda f}}
$$





$$
= \left[\text{comb}(bz) \cdot a\,\text{sinc}(az)\delta(\eta)\right] * \left[\text{comb}(b\eta) \cdot a\,\text{sinc}(a\eta) \cdot \delta(z)\right]
$$





$$
= \left[\text{comb}\left(\frac{bx'}{\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ax'}{\lambda f}\right)\delta\left(\frac{y'}{\lambda f}\right)\right] * \left[\text{comb}\left(\frac{by'}{\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ay'}{\lambda f}\right)\delta\left(\frac{x'}{\lambda f}\right)\right]
$$


# Simple Spatial Filtering Continued




$$
H(x',y') \cdot F(x',y') = \left[\text{comb}\left(\frac{bx'}{\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ax'}{\lambda f}\right) \cdot \delta\left(\frac{y'}{\lambda f}\right)\right] * \left[\text{comb}\left(\frac{by'}{\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ay'}{\lambda f}\right) \cdot \delta\left(\frac{x'}{\lambda f}\right)\right]
$$



**Use a spatial filter:** $H(x',y') = \text{rect}\left(\frac{x'}{c}\right)\text{rect}\left(\frac{y'}{d}\right)$

---

## Case 1

Let: $c = N\frac{\lambda f}{b}$, where $N >> 1$

$d = \frac{\lambda f}{b}$

[Diagram showing filter passing N harmonics in x, 1 in y]



$$
\therefore H(x',y') \cdot F(x',y') \cong \text{comb}\left(\frac{bx'}{\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ax'}{\lambda f}\right) \cdot \delta(y')
$$



**Image in P₃:**



$$
\Rightarrow g(x,y) = \mathcal{F}^{-1}\mathcal{F}^{-1}\{H(x',y') \cdot F(x',y')\}
$$





$$
= \frac{1}{a}\left[\text{comb}\left(\frac{x}{b}\right) \cdot \delta(y)\right] ** \text{rect}\left(\frac{x}{a}\right)
$$



[Diagram showing output with horizontal lines - "Neglect all constants, Horizontal lines have been removed"]

---

## Case 2

Let $c = \frac{\lambda f}{b}$, $d = N\frac{\lambda f}{b}$ where $N >> 1$

[Diagram showing filter passing 1 harmonic in x, N in y]



$$
H(x',y') \cdot F(x',y') \cong \text{comb}\left(\frac{by'}{\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ay'}{\lambda f}\right) \cdot \delta\left(\frac{x'}{\lambda f}\right)
$$





$$
\Rightarrow g(x,y) = \mathcal{F}^{-1}\mathcal{F}^{-1}\{H(x',y') \cdot F(x',y')\} = \left[\text{comb}\left(-\frac{y}{b}\right) \cdot \delta(x)\right] ** \text{rect}\left(\frac{y}{a}\right)
$$



**Vertical lines have been removed.**
# Additional Filters in Abbe-Porter Experiment

## Additional filters of interest in Abbe-Porter Experiment

### Case I

Let $c = \frac{3\lambda f}{b}$, $d = \lambda f$

[Diagram showing filter with width c passing 3 orders]



$$
\Rightarrow H(x',y') \cdot F(x',y') =
$$





$$
\left[\text{comb}\left(\frac{bx'}{\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ax'}{\lambda f}\right) \cdot \delta\left(\frac{y'}{\lambda f}\right) \cdot \text{rect}\left(\frac{bx'}{3\lambda f}\right)\right]
$$





$$
= \frac{\lambda f}{b} \sum_{n=-\infty}^{\infty} \delta\left(x' - \frac{\lambda f}{b}n\right) \cdot \text{rect}\left(\frac{bx'}{3\lambda f}\right) \cdot a\,\text{sinc}\left(\frac{ax'}{\lambda f}\right) \cdot \delta\left(\frac{y'}{\lambda f}\right)
$$



Only lets through $-1, 0, +1$ orders



$$
= \left(\frac{a\lambda f}{b}\right)\left[\delta(x') + \delta\left(x' - \frac{\lambda f}{b}\right) + \delta\left(x' + \frac{\lambda f}{b}\right)\right] \cdot \text{sinc}\left(\frac{ax'}{\lambda f}\right)\delta\left(\frac{y'}{\lambda f}\right)
$$





$$
= \left(\frac{a\lambda f}{b}\right)\left[\delta(x') + \delta\left(x' - \frac{\lambda f}{b}\right)\text{sinc}\left(\frac{a}{b}\right) + \delta\left(x' + \frac{\lambda f}{b}\right)\text{sinc}\left(\frac{a}{b}\right)\right]\delta\left(\frac{y'}{\lambda f}\right)
$$



---

## Image (neglecting constants) is given by:



$$
\mathcal{F}^{-1}\mathcal{F}^{-1}\{H(x',y') \cdot F(x',y')\}
$$





$$
= 1 + 2\,\text{sinc}\left(\frac{a}{b}\right)\cos\left(\frac{2\pi}{b}x\right)
$$



**Raised cosine:**
- i) frequency $\frac{1}{b}$ $\Rightarrow$ period = b
- ii) amplitude $2\,\text{sinc}\left(\frac{a}{b}\right)$

[Diagram showing raised cosine waveform g(x,0) with period b]

[Diagram showing 2D output pattern with vertical stripes]
# High-Pass Filtering

## Case II: Consider a spatial filter shaped like:

[Diagram showing square blocking filter at center, same as case 1 except that F(0,0) is also removed]

Also assume $a \approx b$ (i.e. thin line)

[Diagram showing function f(x,y) with varying values around average value]



$$
\rightarrow \text{Recall } F(0,0) = \iint f(x,y) e^{-j2\pi(x \cdot 2 + y \cdot \eta)} dx\,dy \bigg|_{z=0,\eta=0}
$$





$$
= \iint f(x,y)\,dx\,dy = \text{average value of } f(x,y)
$$





$$
\rightarrow \text{By removing } F(0,0), \text{ we subtract the average value of } f(x,y)
$$


from the original $f(x,y)$. Hence, we have:

[Diagram showing f(x,y) - f̄(x,y) with values oscillating around zero]



$$
\rightarrow \text{The intensity is actually observed, and } I = |f(x,y) - \overline{f(x,y)}|^2
$$



[Diagram showing I(x,y) with squared values]

**Thus, the resultant image is a contrast reversed version of the original!**
# Applications of Spatial Filters

## ★★ Applications of Spatial Filters

### ★ High Pass, Low Pass, and Differentiation Filters

**High Pass [Transfer Function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):**

[Diagram showing 1D [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) t(ξ) with rectangular passband, labeled "one dim"]

[Diagram showing 2D circular high-pass filter with hole in center, labeled "two-dim"]

---

**Low Pass [Transfer Function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):**

[Diagram showing 1D [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) t(ξ) with rectangular passband centered at origin, labeled "one-dim"]

[Diagram showing 2D circular low-pass filter (filled circle), labeled "two-dim"]

---

### Differentiation:



$$
g(x,y) = \frac{\partial f(x,y)}{\partial x}
$$



**Recall:** $\mathcal{F}\left\{\frac{\partial f(x,y)}{\partial x}\right\} = j2\pi\xi \cdot F(\xi,\eta)$



$$
\therefore H(\xi,\eta) = j2\pi\xi \rightarrow \xi
$$



[Diagram showing 1D [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) t(ξ) = ξ (linear ramp), labeled "one dim"]

[Diagram showing 2D differentiation filter with phase variation φ = π on left half, φ = 0 on right half, labeled "two-dim filter (differentiation in one-dimension)"]
# Another Application of Spatial Filters

## ★★ Another Application of Spatial Filters

### ★ Raster-Line Removal

[Diagram showing TV/monitor screen with scan lines]

- Two-dim pictures are encoded on a one-dim time signal for transmission.
- This encoding involves [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) the picture in the vertical direction.

[Diagram showing video signal f(t) with line 1, line 2, line 3 marked, labeled "525 of these lines = 1 frame and occurs every 1/30 sec."]



$$
\rightarrow
$$

 The reconstructed image is thus a sampled image in the y (vertical) direction



$$
g_s(x,y) = g(x,y) \cdot \frac{1}{\gamma}\text{comb}\left(\frac{y}{\gamma}\right)
$$



where:
- $\gamma$ = [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) interval
- $g(x,y)$ = original picture
- $g_s(x,y)$ = sampled picture



$$
\Rightarrow
$$

 Spectrum of sampled picture: $G_s(\xi,\eta) = G(\xi,\eta) * \text{comb}(\gamma\eta)$

[Diagram showing G(ξη) spectrum with triangle shape] $\rightarrow$ [Diagram showing Gs(ξ,η) with replicated spectra at intervals 1/γ]
# Whittaker-Shannon Reconstruction and Half-Tone Printing

## Using an optical system to perform Whittaker-Shannon reconstruction:



$$
G(\xi,\eta) = G_s(\xi,\eta) \cdot \text{rect}(\gamma\xi)
$$



[Diagram showing optical system: Sampled (Raster scanned) Object in → Low pass filter → Continuous Image Out]



$$
\rightarrow
$$

 This is a low-pass filter in η direction, as required by Whittaker-Shannon theorem.

---

## Half-Tone Method of Picture Printing

[Diagram showing original grayscale image with varying intensities] → [Diagram showing × (Thru) operator] → [Diagram showing half-tone pattern with dots of varying sizes]

**Original gray scale image** → **Half tone**

[Diagram showing exposure vs density curve with clip level for film]

(i.e., if exposure is > clip, film is opaque, unit is clear. Unit 21 M is a dot, film is then a screen)

**Result f(x,y):**

[Diagram showing F(ξ,η) spectrum] → [Diagram showing output with note about low pass filter]



$$
\Rightarrow
$$

 Human eye acts as a low pass filter - only 1st lobe image is perceived. Continuous gray scale image has been passed.
# Phase Contrast Methods

## ★ Phase Contrast Methods (observing phase-only functions)

**Consider a general object transmittance:**



$$
A(x,y) = A(x,y) \cdot \text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)
$$



**Define an average picture transmittance:**



$$
A_{\text{ave}}(x,y) = \frac{1}{\ell^2} \iint_{-\ell/2}^{\ell/2} A(x,y)\,dx\,dy \cdot \text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)
$$





$$
= \bar{A} \cdot \text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right) \quad \text{where } \bar{A} = \frac{1}{\ell^2}\iint_{-\ell/2}^{\ell/2} A(x,y)\,dx\,dy
$$



We can define the picture as:



$$
A(x,y) = A_{\text{ave}}(x,y) + A(x,y) - A_{\text{ave}}(x,y)
$$



We now have a spectrum in two parts:



$$
\mathcal{F}\mathcal{F}\{A(x,y)\} = \mathcal{F}\mathcal{F}\{A_{\text{ave}}(x,y)\} + \mathcal{F}\mathcal{F}\{A(x,y) - A_{\text{ave}}(x,y)\}
$$





$$
= \iint \bar{A}\,\text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)\exp(-i2\pi(x\xi + y\eta))\,dx\,dy
$$





$$
+ \iint (A(x,y) - \bar{A})\text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)\exp(-i2\pi(x\xi + y\eta))\,dx\,dy
$$





$$
= U_0(\xi,\eta) + U_1(\xi,\eta)
$$



---

**Now,** $U_0(\xi,\eta) = \bar{A}\ell^2\,\text{sinc}(\ell\xi)\,\text{sinc}(\ell\eta)$



$$
= \left(\iint A(x,y)\,dx\,dy\right)\text{sinc}(\ell\xi)\,\text{sinc}(\ell\eta)
$$





$$
U_1(\xi,\eta) = \iint A(x,y)\,\text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)\exp(-i2\pi(x\xi + y\eta))\,dx\,dy
$$





$$
\text{-} \bar{A}\iint\text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)\exp(-i2\pi(x\xi + y\eta))\,dx\,dy
$$





$$
\Rightarrow U_1(0,0) = \iint A(x,y)\,\text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)\,dx\,dy - \bar{A}\iint\text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)\,dx\,dy = \bar{A}\ell^2 - \bar{A}\ell^2 = 0
$$


# Phase Contrast Methods Continued

## Note:



$$
\lim_{\ell \to \infty} U_0(\xi,\eta) = \bar{A} \lim_{\ell \to \infty} \ell\,\text{sinc}(\ell\xi) \cdot \lim_{\ell \to \infty} \ell\,\text{sinc}(\ell\eta)
$$





$$
= \bar{A}\,\delta(\xi,\eta)
$$



Also we have shown that for any $\ell$,



$$
U_1(0,0) = 0
$$



[Diagram showing U₁(ξ,η) and U₀(ξ,η) as separate components in frequency domain]

We now make a filter which is located only in the $\xi = 0, \eta = 0$ region of the transform, with transmittance $F(\xi,\eta) = ae^{i\alpha}$



$$
\therefore U'(\xi,\eta) = U_0(\xi,\eta)F(\xi,\eta) + U_1(\xi,\eta)
$$



---

## Image created is proportional to $\mathcal{F}^{-1}\mathcal{F}^{-1}\{U'(\xi,\eta)\}$



$$
\mathcal{F}^{-1}\mathcal{F}^{-1}\{U_0(\xi,\eta)F(\xi,\eta)\} = ae^{i\alpha}\mathcal{F}^{-1}\mathcal{F}^{-1}\{U_0(\xi,\eta)\}
$$





$$
= ae^{i\alpha}A_{\text{ave}}(x,y)
$$



**Image** $\Rightarrow$ $P(x',y') = \mathcal{F}^{-1}\mathcal{F}^{-1}\{U'(\xi,\eta)\} = ae^{i\alpha}A_{\text{ave}}(x',y') + A(x',y') - A_{\text{ave}}(x',y')$
(coordinates)

---

## Consider phase object with small modulation:



$$
A(x,y) = e^{i\phi(x,y)}, \quad \phi(x,y) << 1
$$





$$
\therefore A_{\text{ave}}(x,y) = \frac{1}{\ell^2}\iint_{-\ell/2}^{\ell/2} A(x,y)\,dx\,dy \cdot \text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)
$$





$$
\approx 1 \cdot \text{rect}\left(\frac{x}{\ell}\right)\text{rect}\left(\frac{y}{\ell}\right)
$$


# Phase Contrast - Dark Ground Technique

## Then image amplitude becomes:



$$
P(x',y') \cong \left[ae^{i\alpha} + A(x',y') - 1\right]\text{rect}\left(\frac{x'}{\ell},\frac{y'}{\ell}\right)
$$



and image intensity becomes (neglecting finite size from here on):



$$
I(x',y') = |P(x',y')|^2 = |ae^{i\alpha} + A(x',y') - 1|^2
$$



**Substituting for** $A(x',y') = e^{i\phi(x',y')}$:



$$
\boxed{I(x',y') = |ae^{i\alpha} + e^{i\phi(x',y')} - 1|^2}
$$





$$
= a^2 + 2\left[1 + a\cos(\alpha - \phi(x',y')) - a\cos(\alpha) - \cos(\phi(x',y'))\right]
$$



---

## ★ Method 1 - Dark Ground Technique

**Homework:**
Due 22:Apr:81
Cathey: 7-2, 7-3, 7-4

**Filter:** $F(\xi,\eta) = ae^{i\alpha}$, where $a = 0$, $\alpha = 0$

(black spot) [Diagram showing small black spot at center blocking F(ξ,η)]



$$
\Rightarrow I(x',y') = 2\left[1 - \cos\phi(x',y')\right]
$$



For small angles $\phi(x',y') << 1$: $\cos\phi(x',y') \approx 1 - \frac{\phi^2(x',y')}{2}$



$$
\therefore I(x',y') \approx 2\left[1 - 1 + \frac{\phi^2(x',y')}{2}\right] = \phi^2(x',y')
$$



$e^{i\phi(x,y)} \approx 1 + j\phi(x,y)$

Remove constant term: $\Rightarrow$ Intensity is proportional to square of phase variation

[Diagram showing phase input with linear variation] $\cong$ [Diagram showing I = A² with parabolic intensity] $\rightarrow$ [Diagram showing one-sided intensity result $A \propto \phi(x,y)$]



$$
I = A^2 \qquad I + A^2 = (\phi(x,y))^2
$$


# Phase Contrast - Zernike Methods

## Method 2: Positive Phase Contrast (Zernike)

**Filter:** $F(\xi,\eta) = ae^{i\alpha}$, where $a = 1$, $\alpha = \pi/2$

[Diagram showing filter with dielectric to retard phase by π/2]



$$
\Rightarrow I(x',y') = 1 + 2\left[1 + \cos\left(\frac{\pi}{2} - \phi(x',y')\right) - \cos\left(\frac{\pi}{2}\right) - \cos(\phi(x',y'))\right]
$$



If $\phi(x',y') << 1$:

Then $\cos\phi(x',y') \approx 1$

$\cos\left(\frac{\pi}{2} - \phi(x',y')\right) = \sin(\phi(x',y')) \approx \phi(x',y')$

$\cos\left(\frac{\pi}{2}\right) = 0$

and $\boxed{I(x',y') \approx 1 + 2\phi(x',y')}$

$e^{j\phi(x,y)} \cong 1 + j\phi(x,y)$

Shift constant term by $\pi/2$

$I = |j + j\phi(x,y)|^2$

$= |j + 2\phi(x,y) + \phi^2(x,y)|$

$\approx 1 + 2\phi(x,y)$



$$
\Rightarrow
$$

 **Intensity is linearly proportional to phase variation**

[Diagram showing phase input] [Diagram showing intensity output with linear relationship: $I = (1+\phi(x,y))^2 \approx 1 + 2\phi + \phi^2 \approx 1 + 2\phi$]

---

## Method 3: Negative Phase Contrast



$$
F(\xi,\eta) = ae^{i\alpha}, \quad a = 1, \quad \alpha = \frac{3\pi}{2}
$$



Then $I(x',y') = 1 + 2\left[1 + \cos\left[\frac{3\pi}{2} - \phi(x',y')\right] - \cos\left(\frac{3\pi}{2}\right) - \cos(\phi(x',y'))\right]$

Again, $\phi(x',y') << 1$

$\Rightarrow \cos\phi(x',y') \approx 1$

$\cos\left(\frac{3\pi}{2} - \phi(x',y')\right) = -\sin(\phi(x',y')) = -\phi(x',y')$

$\cos\left(\frac{3\pi}{2}\right) = 0$

and $\boxed{I(x',y') \cong 1 - 2\phi(x',y')}$

[Diagram showing phase input] [Diagram showing inverted intensity output: $I = (1-\phi(x,y))^2 \approx 1 - 2\phi + \phi^2 \approx 1 - 2\phi$]
# Phase Contrast - Schlieren Method

## Method 4

### ★ Schlieren Method (knife edge method)

[Diagram showing four different intensity distributions as knife edge cuts off different portions of light]

**Recall:** $\text{sgn}(\xi) = \begin{cases} 1 & \xi > 0 \\ 0 & \xi = 0 \\ -1 & \xi < 0 \end{cases}$

Similar to Heaviside Step Function.

**Filter:** $H(\xi,\eta) = \frac{1}{2}(1 + \text{sgn}(\xi))$

**Input:** $f(x,y) = e^{j\phi(x,y)}$

Small angle approx: $f(x,y) \approx 1 + j\phi(x,y)$



$$
\Rightarrow F(\xi,\eta) = \delta(\xi,\eta) + j\,\Phi(\xi,\eta)
$$



where $\Phi(\xi,\eta) = \mathcal{F}\mathcal{F}\{\phi(x,y)\}$

---

## Note:

If the knife edge is adjusted to completely remove the zero freq. $\delta(\xi,\eta)$, then the result is



$$
F(\xi,\eta) \cdot H(\xi,\eta) = \frac{1}{2}(1 + \text{sgn}(\xi)) \cdot j\,\Phi(\xi,\eta)
$$





$$
\mathcal{F}^{-1}\{F(\xi,\eta) \cdot H(\xi,\eta)\} = \frac{1}{2}\left(\delta(x,y) + \frac{j}{\pi x}\delta(y)\right) ** j\,\phi(x,y)
$$





$$
= \frac{j}{2}\left[\phi(x,y) + \frac{j}{\pi}\int\frac{\phi(\alpha,y)}{x-\alpha}\,d\alpha\right]
$$





$$
= \frac{j}{2}\left[\phi(x,y) + j\,H_x\{\phi(x,y)\}\right]
$$



where $H_x\{\phi(x,y)\} = \frac{1}{\pi}\int\frac{\phi(\alpha,y)}{x-\alpha}\,d\alpha$



$$
= \underline{\text{One-Dim Hilbert Transform}}
$$


# Complex Spatial Filters


**Recall telecentric system:**

[Diagram showing optical system with planes P1, P2, P3 and focal lengths f]



$$
f(x,y) \xrightarrow{H(\xi,\eta)} g(x,y)
$$





$$
\rightarrow
$$

 The [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) $H(\xi,\eta)$ is physically present in plane P2.



$$
\rightarrow
$$

 If we use film to record $H(\xi,\eta)$, then



$$
t(x,y) = H(x',y') \rightarrow \text{positive real}
$$





$$
\rightarrow
$$

 To perform **convolutions** $\mathcal{F}$ correlations, we require

**[convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)** $\rightarrow$ $g(x,y) = f(x,y) * h(x,y)$ — [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)

or $G(\xi,\eta) = F(\xi,\eta) \cdot H(\xi,\eta)$

where $H(\xi,\eta) = \mathcal{F}\mathcal{F}\{h(x,y)\}$

**correlation** $\rightarrow$ and $g(x,y) = f(x,y) \star h^*(x,y) = f(x,y) * h^*(-x,-y)$ — correlation

or $G(\xi,\eta) = F(\xi,\eta) \cdot H^*(\xi,\eta)$

where $H^*(\xi,\eta) = \mathcal{F}\mathcal{F}\{h^*(-x,-y)\}$

---

★ This means we have to make a filter with transmittance:



$$
t(x',y') = H(x',y') = \mathcal{F}\mathcal{F}\{h(x,y)\}
$$



or $t(x',y') = H^*(x',y') = \mathcal{F}\mathcal{F}\{h^*(-x,-y)\}$
# Vander Lugt Filters



$$
\rightarrow
$$

 But we know that $H(x',y')$ is real only if $h(x,y)$ is even.



$$
\rightarrow
$$

 Since this is not usually the case, we conclude $H(x',y')$ is in general complex.

**Homework:** Cathey 7-6, 7-11, 7-14, Goodman 7-7

---

## Vander Lugt Filters

[Diagram showing recording geometry with P1 and P2 planes, object wave h(x,y), and reference [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) at angle θ]

**Recording geometry:**



$$
\rightarrow
$$

 Form optical [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of $h(x,y)$ in P2 $\Rightarrow$ $H\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)$



$$
\rightarrow
$$

 Add off-axis reference wave at angle $\theta$, $\Rightarrow e^{-j2\pi\alpha x'}$, where $\alpha = \frac{\sin\theta}{\lambda}$



$$
\therefore U(x',y') = H\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right) + e^{-j2\pi\alpha x'}
$$





$$
\rightarrow
$$

 Film responds to the intensity. Therefore



$$
t(x',y') \propto I(x',y') = \left|H\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right) + e^{-j2\pi\alpha x'}\right|^2
$$





$$
= \left|H\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)\right|^2 + 1 + H\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)e^{j2\pi\alpha x'} + H^*\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)e^{-j2\pi\alpha x'}
$$



**Note:** Although we recorded the intensity, we still have the complex function $H(x',y')$ recorded. However, we also had to record $H^*(x',y')$ to cancel out all phase terms.
# Vander Lugt Filter Impulse Response

## Calculate impulse response of this filter: $v(x,y)$

(Neglect all constants)

[Diagram showing [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) input going through filter with spectrum components, set up to observe [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)]



$$
t(x',y')
$$


(proportional to [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/))



$$
v(x,y) = \mathcal{F}^{-1}\mathcal{F}^{-1}\left\{t\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)\right\}\bigg|_{x=-\frac{x'}{\lambda f}, y=-\frac{y'}{\lambda f}} = \mathcal{F}^{-1}\mathcal{F}^{-1}\left\{H\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)H^*\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right) + 1 + H\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)e^{j2\pi\alpha x'} + H^*\left(\frac{x'}{\lambda f}, \frac{y'}{\lambda f}\right)e^{-j2\pi\alpha x'}\right\}
$$





$$
= h(x,y) ** h^*(-x,-y) + \delta\left(\frac{x}{\lambda f}, \frac{y}{\lambda f}\right) + h(x,y) * \delta\left(\frac{x+\alpha}{\lambda f}\right) + h^*(-x,-y) * \delta\left(\frac{x-\alpha}{\lambda f}\right)
$$



**But recall:**
$\delta\left(\frac{x}{a}+\alpha\right) = |a|\delta(x+a\alpha)$
$= \lambda f\,\delta(x+\alpha\lambda f) * \delta(y+\alpha \cdot nothing)$
since $\alpha = +a \cdot 0/\lambda$



$$
= h(x,y) ** h^*(x,y) + \delta(x,y) + h(x,y) * \delta(x+f\sin\theta) + h^*(-x,-y) * \delta(x-f\sin\theta)
$$



---

★ **Note:** $h^*(x-f\sin\theta, -y)$ and $h(x+f\sin\theta, y)$ are physically separated from each other two terms.

(See above diagram)

Thus, we have recorded a filter whose [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) is $h(x,y)$ (or $h^*(-x,-y)$).

---

**Remember:** Cathey 7-2: [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/)
problem 1: image

We have a filter: Using the Vander Lugt Filter to Perform Correlation

[Diagram showing optical system with P1, P2, P3 planes: Unit Amplitude [Plane Wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) → Input f(x,y) → Vander Lugt Filter t(x',y') → Output g(x,y)]
# Vander Lugt Filter Output



$$
g(x,y) = f(x,y) ** v(x,y)
$$



where $v(x,y) = \mathcal{F}^{-1}\mathcal{F}^{-1}\{t(x',y')\}$ and was previously calculated.



$$
\Rightarrow g(x,y) = f(x,y) ** h(x,y) ** h^*(x,y)
$$





$$
+ f(x,y) ** \delta(x,y)
$$





$$
+ f(x,y) ** h(x+f\sin\theta, y)
$$





$$
+ f(x,y) ** h^*(-x-f\sin\theta, -y)
$$





$$
= f(x,y) ** \left[h(x,y) ** h^*(x,y)\right] \quad \text{(garbage)}
$$





$$
+ f(x,y) \quad \text{(input image)}
$$





$$
+ f(x,y) ** h(x+f\sin\theta, y) \quad \text{(convolution, centered at } x = -f\sin\theta\text{)}
$$





$$
+ f(x,y) ** h^*(x-f\sin\theta, y) \quad \text{(correlation, centered at } x = +f\sin\theta\text{)}
$$



[Diagram showing output plane with separated terms: f(x,y)**h(x,y) at center, f(x,y) term, f(x,y)**h*(x,y) correlation term at x=+fsinθ, with garbage/autocorrelation terms between]

---

## ★ Angle requirement for θ:

**Consider:**
1) Maximum width of $f(x,y) \rightarrow W_f$ (in x direction)
2) Maximum width of $h(x,y) \rightarrow W_h$ (in x direction)



$$
\rightarrow
$$

 We know: Maximum width of a [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) (or correlation) of two functions = sum of individual maximum widths



$$
\Rightarrow
$$

 1) Max width of $f(x,y) ** [h(x,y) ** h^*(x,y)] = W_f + 2W_h$
2) Max width of $f(x,y) = W_f$
3) Max width of $f(x,y) ** h(x,y) = W_f + W_h$
4) Max width of $f(x,y) ** h^*(x,y) = W_f + W_h$
# Vander Lugt Filter - Angle Requirements

[Diagram showing three terms with widths: $W_f + 2W_h$, $W_f$, $W_f + W_h$ separated by spacing $f\sin\theta$]

**Requirement for no overlap:**



$$
f\sin\theta \geq \frac{W_f + 2W_h}{2} + \frac{W_f + W_h}{2}
$$



or $\sin\theta \geq \frac{3}{2}\frac{W_h}{f} + \frac{W_f}{\underbrace{f}_{\text{focal length of lens}}}$

For small angles, we have the simple result:



$$
\boxed{\theta \geq \frac{3}{2}\frac{W_h}{f} + \frac{W_f}{f}}
$$



---

## ★ The Vander Lugt Filter Described In Terms of Superposition of Gratings

**General Input Response:**



$$
\rightarrow
$$

 Consider a complex function $|h(x,y)|e^{j\phi_h(x,y)}$ composed of the sum of point sources: $\iint |h(\alpha,\beta)|e^{j\phi_h(\alpha,\beta)}\delta(x-\alpha, y-\beta)\,d\alpha\,d\beta$



$$
\rightarrow
$$

 We study the result of recording a single point source $\delta(x-\alpha, y-\beta)$ with strength $|h(\alpha,\beta)|e^{j\phi_h(\alpha,\beta)}$



$$
\Rightarrow h(x,y)$ is a simple linear superposition of this result.

[Diagram showing P1 with point source $|h(\alpha,\beta)|e^{j\phi_h(\alpha,\beta)}\delta(x-\alpha,0)$ and P2 with reference plane wave $e^{j2\pi\alpha x'}$, labeled "Recording Geometry"]
# Vander Lugt Filter - Two Plane Wave Interference

## Note: We have in P2 the interference of two plane waves:
$$

t(x',y') \propto I(x',y') = \left|e^{-j2\pi\alpha x'} + |h(\alpha,0)|e^{j\phi_h(\alpha,0)}e^{-j2\pi\alpha x'/\lambda f}\right|^2

$$

$$

= 1 + |h(\alpha,0)|^2 + |h(\alpha,0)|e^{-j2\pi\alpha x'}e^{-j\phi_h(\alpha,0)}e^{+j2\pi\alpha x'/\lambda f}

$$

$$

+ |h(\alpha,0)|e^{j2\pi\alpha x'}e^{j\phi_h(\alpha,0)}e^{-j2\pi\alpha x'/\lambda f}

$$

$$

= 1 + |h(\alpha,0)|^2 + 2|h(\alpha,0)|\cos\left(2\pi\left(\alpha - \frac{\alpha}{\lambda f}\right)x' + \phi_h(\alpha,0)\right)

$$

$$

\underbrace{\qquad}_{\text{bias}} \quad \underbrace{\qquad}_{AM} \quad \underbrace{\qquad}_{\text{carrier}} \quad \underbrace{\qquad}_{\phi M}

$$

$$

\underbrace{\qquad}_{FM}

$$
\text{-}--

## Result for single pt:

[Graph showing oscillating function $t(x',y')$ with DC bias level marked]

1) **Amplitude of $h(x,y)$ at pt $(\alpha,0)$**, $|h(\alpha,0)|$, controls amplitude modulation of carrier (or depth of modulating grating)

2) **Phase of $h(x,y)$ at pt $(\alpha,0)$**, $e^{j\phi_h(\alpha,0)}$, controls shift of carrier or phase modulation

3) **Location of pt $(\alpha,0)$**: controls frequency modulation. Notice: If $\alpha = 0$, carrier is $\cos(2\pi\alpha x' + \phi) \Rightarrow freq = \alpha$. If $\alpha \neq 0$, carrier is $\cos\left(2\pi\left(\alpha - \frac{\alpha}{\lambda f}\right)x' + \phi\right) \Rightarrow freq = \alpha - \frac{\alpha}{\lambda f}$.
$$

\rightarrow

$$
Now general $h(x,y)$ is simply a superposition of many modulated gratings
# Optical Interpretation of Matched Filtering

## Optical Interpretation of Matched Filtering Operation

**Recall:** Frequency domain description of $f(x,y) ** h(x,y)$

and $f(x,y) ** h^*(x,y)$
$$

F(\xi,\eta) \cdot H(\xi,\eta) \quad \text{([convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/))}

$$

$$

F(\xi,\eta) \cdot H^*(\xi,\eta) \quad \text{(correlation)}

$$
[Diagram showing optical system: Plane wave → f(x,y)=h(x,y) Input → Filter with H(ξ,η) and spectrum showing lines of constant phase, diffraction from input, H(ξ,η)·H*(ξ,η) removes phase component → Correlation point output]

**Matched Filter when $f(x,y) = h(x,y)$**
$$

\Rightarrow g(x,y) = h(x,y) ** h^*(x,y)

$$
\text{-}--

**Notice:**

1) **Effect of filter $H^*(\xi,\eta)$** is to straighten out the lines of constant phase. These constant phase fronts are focused by last lens to a bright spot.

2) **Effect of filter $H(\xi,\eta)$** (convolution) is to generate $H(\xi,\eta) \cdot H(\xi,\eta)$ which contains phase variation (not cancelled by $H^*(\xi,\eta)$). Thus, final lens does not focus this field to a bright spot. Thus, convolution is not useful for detecting patterns.
# Signal Detection

## Signal Detection: (type of pattern recognition)
$$

\rightarrow

$$
Say we have a signal $S(x)$ to be detected and N signals $n_1(x), n_2(x), \ldots n_N(x)$ which could be present instead of $S(x)$.
$$

\rightarrow

$$
We would like to design a filter

[Diagram showing: S(x), n_1(x), n_2(x), ... n_N(x) → h(x) → signal to allow detection of S(x)]

\text{-}--

## ★ Imagine the problem of character recognition

**Characters:** A, B, C, D → [Detect A]

One obvious way to detect character A is to make a mask of A and place it over each input character,

[Images of characters A, B, C overlaid with mask]

and add up the common areas. Since all areas are common in the A-A match, but not all are common for the A-B and A-C match, the Total common area will be largest for A-A. Thus the largest number in this procedure detects the letter A. (Assuming all letters have equal total area)
# Template Matching
$$

\Rightarrow \int_{-\infty}^{\infty}|S(x)|^2\,d\alpha = \int_{-\infty}^{\infty}|n_i(x)|^2\,d\alpha = K

$$
(We shall eliminate this constraint later by proper normalization)

\text{-}--

## ★ This procedure is called Template Matching for obvious reasons

**Mathematically, we can write**
$$

\sigma = \iint f(x,y) \cdot \underbrace{R^*}_{g}(x,y)\,dx\,dy \quad \xleftarrow{\text{input pattern "A" or "B" or...}} \xleftarrow{\text{test pattern "A"}} \quad \text{Template match ([Inner product](/notes/areas/mathematics/functional_analysis/definitions/inner_product/))}

$$
We simply measure the value of $\sigma$ to see if it is large enough.

[Diagram showing: Input f(x,y) → Template Match → Threshold σ ≥ σ₀? → 1 = yes, 0 = No]

\text{-}--

## Template Match observed in Function Space:

**Recall function space:** $f(x) = \{f(x_1), f(x_2), \ldots, f(x_3), \ldots\}$

N dimensional vector
$$

\rightarrow

$$
$f(x)$ is a single point (vector) in N-dim space
$$

\rightarrow

$$
$h(x)$ is another vector
$$

\rightarrow

$$
Condition that $\int_{-\infty}^{\infty}|f(x)|^2\,dx = \int_{-\infty}^{\infty}|h(x)|^2\,dx$
$$

\Rightarrow f^* \cdot f = h^* \cdot h \Rightarrow \text{vector lengths are the same}

$$
# Function Space and Template Match

## In function space we have:

[Diagram showing vectors f and k* in N-dimensional space with axes x₁, x₂, x₃]
$$

f \cdot k^*

$$
\text{-}--

## ★ It is now clear that the Template match of two functions (inner product of two vectors) simply calculates the projection of f onto k.

Thus, we compare two functions by their proximity in function space.

\text{-}--

## ★ How do we design a filter to perform this inner product?
$$

\rightarrow

$$
Consider a filter with impulse response
$$

h(x,y) = k^*(-x,-y) \quad \text{(Matched Filter)}

$$
[Diagram showing: f(x,y) → [h(x,y)] → g(x,y)]
$$

g(x,y) = f(x,y) ** k^*(-x,-y)

$$

$$

= \iint f(\alpha,\beta) \cdot k^*(\alpha-x, \beta-y)\,d\alpha\,d\beta

$$

$$

= \mathcal{X}_{fk}(x,y) \quad \underline{\text{Cross Correlation}}

$$
# Cross Correlation and Inner Product

## Note:
$$

\mathcal{X}_{fk}(0,0) = \iint f(\alpha,\beta) \cdot k^*(\alpha,\beta)\,d\alpha\,d\beta = \sigma

$$
(Desired Inner Product)
$$

\therefore

$$
We simply use a filter with impulse response $k^*(-x,-y)$ and observe the output at $g(0,0)$.

\text{-}--

**Note:** If $f = k$ (pattern match) then output of filter
$$

\mathcal{X}_{ff}(x,y)

$$
is the autocorrelation of $f(x,y)$.
$$

\rightarrow

$$
We have shown that
$$

\mathcal{X}_{ff}(0,0) \geq \mathcal{X}_{ff}(x,y)

$$
(Autocorrelation has a maximum value at center)

We can also show that
$$

\mathcal{X}_{fk}(0,0) \geq \mathcal{X}_{fk}(x,y)

$$
(Cross correlation)

since in signal space, this corresponds to computing inner product of f with all other vectors k compared to k(x,y) and shifted versions: k(x-x', y-y')

[Diagram showing vectors k(x,y), f(x,y), k(x-x',y'), h(x-x',y') in function space]
# Matched Filter for Pattern Detection

## ★ It is natural to ask what center values $g(a,b) = \mathcal{X}_{fk}(a,b)$ correspond to in the above pattern recognition system.
$$

\rightarrow g(a,b) = \mathcal{X}_{fk}(a,b) = \iint f(\alpha,\beta) \cdot k^*(\alpha-a, \beta-b)\,d\alpha\,d\beta

$$

$$

\rightarrow

$$
Recall $k(\alpha,\beta)$ was the function describing the pattern "A"
$$

\rightarrow

$$
Thus $\mathcal{X}_{fk}(a,b)$ is the inner product between input $f(\alpha,\beta)$ and a shifted pattern "A", described by $k(\alpha-a, \beta-b)$
$$

\rightarrow

$$
Thus $\mathcal{X}_{fk}(a,b)$ tests for the presence of "A" shifted by an amount $(a,b)$.

\text{-}--

## ★ This type of filter is called a Matched Filter

## ★ Transfer function of matched filter:
$$

h(x,y) = k^*(-x,-y) \quad \text{([impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/))}

$$

$$

\Rightarrow H(\xi,\eta) = \mathcal{F}\{k^*(-x,-y)\} = K^*(\xi,\eta)

$$

$$

\rightarrow

$$
Thus, matched filter can be viewed as

[Diagram showing: F(ξ,η) → [K*(ξ,η)] → G(ξ,η)]
$$

G(\xi,\eta) = F(\xi,\eta) \cdot K^*(\xi,\eta) \leftarrow \text{Product of F.T.}

$$
and when input matches filter, $G(\xi,\eta) = |K(\xi,\eta)|^2$

↳ $F(\xi,\eta) = K(\xi,\eta)$
# Character Recognition Machine

## Application 1 ←

### Character Recognition Machine

**Problem:** Detect all the letters of the alphabet

**Solution:** Use a bank of Vander Lugt filters

[Diagram showing parallel matched filter bank architecture:
\text{-} Input g(x,y) splits to multiple paths
\text{-} Each path has filter H₁*, H₂*, H₃*, H₄*, H₅* etc.
\text{-} Each filter output goes through integrator (∫)
\text{-} Outputs are normalized by √(∬|h₁|²dxdy), √(∬|h₂|²dxdy), etc.
\text{-} Final outputs go to comparator]

Letter "A": $h_1(x,y) \rightarrow$ Matched filter is $H_1^*(\xi,\eta)$

Letter "B": $h_2(x,y) \rightarrow$ " " $H_2^*(\xi,\eta)$

⋮

\text{-}--

## ★ Trouble with using outputs of matched filters directly:

Filter for "F" cannot tell the difference between "E" and "F"

[Images showing letters F filter, E input, F input]

Inner product (template match) is the same for both inputs.
# Matched Filter Normalization

## Solution to Trouble:

Normalize all outputs by $\sqrt{\iint |h_i(x,y)|^2\,dx\,dy}$

Then, largest output corresponds to input
$$

\rightarrow

$$
Proof of normalization solution:

### ★ Peak Intensity of correctly matched filter

$h_k$ = input
$h_k^*$ = filter impulse response
$$

|U_k|^2 = \left[\iint |h_k|^2\,dx\,dy\right]^2 \xleftarrow{\text{because intensity is measured}}

$$

$$

\iint |h_k|^2\,dx\,dy \leftarrow \text{Normalization}

$$

$$

= \iint |h_k|^2\,dx\,dy

$$
\text{-}--

### ★ Peak of incorrectly matched filter (intensity) $|U_n|^2$, $(n \neq k)$

$h_k$ = input
$h_n^*$ = filter impulse response
$$

|U_n|^2 = \frac{\left|\iint h_k h_n^*\,dx\,dy\right|^2}{\iint |h_n|^2\,dx\,dy} \leftarrow \text{Normalization}

$$
\text{-}--

## From Schwarz inequality:
$$

\left|\iint h_k h_n^*\,dx\,dy\right|^2 \leq \iint |h_k|^2\,dx\,dy \cdot \iint |h_n|^2\,dx\,dy

$$
To see this inequality is true, remember vector space interpretation of inner product: $\iint h_k h_n^*\,dx\,dy = h_k \cdot h_n$ (vectors)

We know $h_k \cdot h_n = \|h_k\| \|h_n\| \cos\theta$

Since $-1 < \cos\theta < 1$, we have $\|h_k \cdot h_n\|^2 = \|h_k\|^2 \|h_n\|^2 \cos^2\theta$
$$

\leq \|h_k\|^2 \|h_n\|^2

$$
# Matched Filter Proof
$$

\therefore |U_n|^2 = \frac{\left|\iint h_k h_n^*\,dx\,dy\right|^2}{\iint |h_n|^2\,dx\,dy} \leq \frac{\iint |h_k|^2\,dx\,dy \cdot \iint |h_n|^2\,dx\,dy}{\iint |h_n|^2\,dx\,dy}

$$

$$

= \iint |h_k|^2\,dx\,dy = |U_k|^2

$$
or $|U_n|^2 \leq |U_k|^2$
$$

\rightarrow

$$
We also know that the equality only holds if
$$

h_n(x,y) = K \cdot h_k(x,y)

$$

$$

\underbrace{\qquad}_{\text{filter}} \quad \underbrace{\qquad}_{\text{input}}

$$

$$

\therefore

$$
All filter outputs $|U_n|^2$ are less than the proper filter output $|U_k|^2$, and selection can be based on the highest value.

\text{-}--

## Problems with matched filtering techniques:

1. Rotation sensitive
2. Scale sensitive (size change)
3. Statistical variation sensitivity
# Inverse Spatial Filtering

## Application 2 ←

### Inverse Spatial Filtering

## ★ Consider the problem of image blur

[Diagram showing: object with dimension d₀ → blurred arrow → blurred image g(x,y) with dimension d_i, Exposure time = Δt]
$$

f(x,y) \xrightarrow{h(x,y)/H(\xi,\eta)} g(x,y)

$$
**Equivalent linear system**

\text{-}--

## ★ Blurring operation can be expressed as a filtering by **[LSI](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/)** filter with **[impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** $h(x,y)$.
$$

\rightarrow

$$
**[Impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/)** (response to a point object) is
$$

h(x,y) = \text{rect}\left(\frac{x}{v\Delta t}\right)\delta(y)

$$
since streak in x direction is $v\Delta t$ long.
$$

\therefore H(\xi,\eta) = v\Delta t\,\text{sinc}(v\Delta t\,\xi)

$$
# Inverse Filtering Analysis

[Diagram showing sinc function with first zero at 1/vΔt on ξ axis]

**Note:**
1. Blurring is a low pass type filter
2. Sinusoids with freq $n\left(\frac{1}{v\Delta t}\right)$ are completely blocked.

[Diagram showing: vΔt width → blur distance]

This is because the blur averages over exactly one cycle (or n cycles for $\frac{n}{v\Delta t}$) of this sinusoid, so it looks like a constant.
$$

\Rightarrow

$$
We can restore $F(\xi,\eta)$ (and hence unblurred picture $f(x,y)$) by a filter with transfer function
$$

\frac{H^*(\xi,\eta)}{|H(\xi,\eta)|^2} \quad \text{sinc}

$$

$$

G(\xi,\eta) = F(\xi,\eta) \cdot H(\xi,\eta) \quad \text{(distorted)}

$$
and so $F(\xi,\eta) = \underbrace{F(\xi,\eta) \cdot H(\xi,\eta)}_{\text{input}} \cdot \left[\frac{H^*(\xi,\eta)}{|H(\xi,\eta)|^2}\right] \quad \text{(restored)}$
# Generating the Inverse Filter

We would like to generate this filter:
$$

\frac{H^*(\xi,\eta)}{|H(\xi,\eta)|^2}

$$
**Part 1:** $H^*(\xi,\eta) \cdot \frac{1}{|H(\xi,\eta)|^2}$ **Part 2**

\text{-}--

## Part 1:

[Diagram showing optical setup with two focal lengths f, input h(x,y), impulse response = rect(x/vΔt), and output showing $H(\xi,\eta) + e^{-j2\pi\alpha x}$ with reference wave]
$$

I(\xi,\eta) = |H(\xi,\eta)|^2 + 1 + H(\xi,\eta)e^{j2\pi\alpha x} + H^*(\xi,\eta)e^{-j2\pi\alpha x}

$$

$$

\underbrace{\qquad}_{\text{part 1 on carrier}}

$$
\text{-}--

## Part 2:

[Diagram showing h(x,y) input with no reference wave]
$$

I = |H(\xi,\eta)|^2

$$

$$

t(\xi,\eta) = \left[|H(\xi,\eta)|^2\right]^{-\gamma} \xleftarrow{\text{Negative film response}}

$$

$$

= |H(\xi,\eta)|^{-2}

$$
# Inverse Filtering - Restored Image

By placing these two filters in contact with one another, we have
$$

\frac{H^*(\xi,\eta)}{|H(\xi,\eta)|^2}

$$
Now, using an optical correlator

(which is just our basic telecentric imaging system)

[Diagram showing optical system: blurred object → lenses → filter $\frac{H^*(\xi,\eta)e^{-j2\pi\alpha x}}{|H(\xi,\eta)|^2}$ + other terms → restored image at $f\sin\theta$]
# Fresnel Zones and the Fresnel Zone Plate


Consider light (plane wave, monochromatic) illuminating a screen:

[Diagram showing plane wave illuminating screen with point P at distance R, showing zones a, b, c, d with radii r₁, r₂, etc., and path lengths R+λ/2, R+2λ/2, etc.]

[Diagram showing concentric Fresnel Zones viewed from point P]

\text{-}--

## Compute radius of zones:

Right Triangle ΔPOa gives:
$$

r_1^2 + R^2 = \left(R + \frac{\lambda}{2}\right)^2 = R^2 + R\lambda + \left(\frac{\lambda}{2}\right)^2

$$

$$

\Rightarrow r_1^2 = R\lambda + \left(\frac{\lambda}{2}\right)^2

$$
Since $R >> \lambda$
$$

\Rightarrow r_1^2 \cong R\lambda, \quad r_1 = \sqrt{R\lambda}

$$
# Fresnel Zone Calculations

## Example:

Let $R = 50$ cm

$\lambda = 0.5\,\mu$m
$$

r_1 = \sqrt{50 \times 5 \times 10^{-5}}\,\text{cm} = 0.5\,\text{mm}

$$
By the same method, we have:
$$

r_2 = \sqrt{2R\lambda} = \sqrt{2}\,r_1

$$

$$

r_3 = \sqrt{3R\lambda} = \sqrt{3}\,r_1, \quad \text{etc.}

$$
\text{-}--

## Phase
$$

\rightarrow

$$
We approximate a zone as being constant phase.
$$

\rightarrow

$$
Thus, if zone 1 has a certain phase, zone 2 is $\pi$ out of phase, zone 3 is $2\pi$ out, or in phase, etc.

\text{-}--

## Amplitude

Amplitude is proportional to the area of zone.

\text{-} Area of central zone = $\pi r_1^2$
\text{-} Area of second zone = $\pi r_2^2 - \pi r_1^2 = \pi(2r_1^2 - r_1^2) = \pi r_1^2$
\text{-} Area of 3rd zone = $\pi r_3^2 - \pi r_2^2 = \pi(3r_1^2 - 2r_1^2) = \pi r_1^2$

etc.

**Thus, all zones are of equal strength**

\text{-}--

## Superposition:

Amplitude at P is given by sum of zones.

(Larger zones contribute slightly less due to larger distance and angle - ignore this)
# Fresnel Zone Superposition

## Result at P is
$$

E = E_1 - E_2 + E_3 - \ldots

$$
($E_n$ is amplitude from $n^{th}$ zone)

We can replace the value of a zone by the mean of the zone in front and behind:
$$

\Rightarrow E_n = \frac{E_{n+1} + E_{n-1}}{2}

$$

$$

\Rightarrow \text{Thus} \quad E = \frac{E_1}{2} + \left(\frac{E_1}{2} - E_2 + \frac{E_3}{2}\right) + \left(\frac{E_3}{2} - E_4 + \frac{E_5}{2}\right) + \ldots

$$

$$

\underbrace{\qquad}_{0} \quad \underbrace{\qquad}_{0}

$$
From above expression

However, if a circular aperture is used so that only the first zone is exposed,
$$

E = E_1

$$
(amplitude is twice as great).

\text{-}--

If 2 zones are exposed,
$$

E = E_1 - E_2 \approx 0

$$
(dark spot in center)
$$

\rightarrow

$$
(See 3a) ←

\text{-}--

## Zone plate

Block all regions with $-\pi$ phase.

Thus, point P adds all light in phase and is very bright.
# Fresnel Diffraction Integral for Zone Plate

## Recall solution to on-axis Fresnel Transform of circle:

[Diagram showing circular aperture with radius r₀, finding intensity on-axis]
$$

U_0(x,y) = \text{circ}\left(\frac{\sqrt{x^2+y^2}}{r_0}\right)

$$
**Fresnel diffraction integral gives:**
$$

U(0,0,z) = \exp\left[j\frac{2\pi}{\lambda}z\right] \iint \text{circ}\left(\frac{r}{r_0}\right) \exp\left[j\frac{\pi}{\lambda z}r^2\right] r\,dr\,d\theta

$$

$$

= \frac{2\pi\exp\left[j\frac{2\pi}{\lambda}z\right]}{j\lambda z} \exp\left[j\frac{\pi}{\lambda z}r^2\right] \frac{z\lambda}{j2\pi}\bigg|_0^{r_0}

$$

$$

= -2j\exp\left[j\frac{2\pi}{\lambda}z\right] \exp\left[j\frac{\pi r_0^2}{2\lambda z}\right] \sin\left[\frac{\pi r_0^2}{2\lambda z}\right]

$$

$$

\Rightarrow I(0,0,z) = 4\sin^2\left[\frac{\pi r_0^2}{2\lambda z}\right]

$$
[Graph showing I(0,0,z) vs z with oscillations, peaks at $\frac{\pi r_0^2}{2\lambda z} = 2\pi$ and $\frac{\pi r_0^2}{2\lambda z} = \pi$]

[Diagram showing Zone 2 and Zone 1 regions]
$$

z = \frac{r_0^2}{2\lambda}

$$
This is "R" in our current development
$$

\boxed{r_0 = \sqrt{nR\lambda}}

$$
Formula for size of $n^{th}$ Fresnel zone
$$

\frac{r_0^2}{n\lambda} = R

$$
$n = 2 \Rightarrow$ Two Fresnel Zones

## Zone Plate

[Diagram showing zone plate with concentric rings: φ=0 outer ring, φ=π, φ=0, φ=π, φ=0 at center, with radii r₁, r₂, r₃ marked]
$$

\begin{cases} r_1 = \sqrt{R\lambda}, & R = \text{distance from plate to screen} \\ r_n = \sqrt{n}\,r_1 \end{cases}

$$
\text{-}--

[Diagram showing zone plate with observation point P at distance R, and markings at ξ/3 and ξ/2]

**Consider Fresnel Zones from distances $\frac{R}{2}$, $\frac{R}{3}$, etc.**

P at $\frac{R}{2}$ $\Rightarrow$ $r_1' = \sqrt{\frac{R}{2}\lambda} = \frac{1}{\sqrt{2}}r_1$

P'' at $\frac{R}{3}$ $\Rightarrow$ $r_1'' = \sqrt{\frac{R}{3}\lambda} = \frac{1}{\sqrt{3}}r_1$
# Fresnel Zone Plate Focal Points
$$

\therefore P' = \frac{R}{2} \Rightarrow

$$
[Diagram showing zone plate at P' = R/2 with zones marked: φ=2, φ=s₁, φ=0, φ=π, φ=π, where r₁' = 1/√2 r₁ and r₂' = r₁]

\text{-} Original Zone plate

**Contributions from $\phi = 0$ and $\phi = \pi$**
$$

\Rightarrow

$$
**Dark spot.**

\text{-}--

## P'' ⇒ R/3

[Diagram showing zone plate at P'' = R/3 with zones 1 and 2 canceling, zones 4-6 blocked, zones 7&8 cancel, zone 1 is a not positive phase, etc.]

\text{-} Zone 1 and zone 2 cancel
\text{-} but zone 3 leaves a net positive phase. Zones 4-6 are blocked. Zone 7 & 8 cancel, Zone 1 is a not positive phase, etc.
$$

\Rightarrow

$$
**Light spot**
$$

\therefore

$$
Foci @ $\frac{1}{n}R$

but $n =$ even $\Rightarrow$ dark spot

$n =$ odd $\Rightarrow$ light spot
# On-Axis Hologram as a Fresnel Zone Plate
$$

\rightarrow

$$
Consider an object as consisting of a large number of point sources
$$

\rightarrow

$$
A single pt. source of strength A is a spherical wave:
$$

U_0 = \frac{A_0}{r}\exp(jkr), \quad r = \sqrt{x^2 + y^2 + z^2}

$$
[Diagram showing point source creating spherical wave with $U_0 = \frac{A_0}{r}\exp(jkr)$]

If $z >> \sqrt{x^2+y^2}$, $r \approx z_0\left(1 + \frac{x^2+y^2}{2z_0^2}\right)$

and $U_0 = \frac{A_0}{z_0}\exp(jkz_0)\exp\left(j\frac{k}{2z_0}(x^2+y^2)\right)$
$$

\rightarrow

$$
Add reference plane wave: $U_R = A_R\exp(jkz_0)$
$$

\rightarrow

$$
Transmittance of film becomes (proportional to intensity)
$$

t(x,y) = I(x,y) = |U_R + U_0|^2 = |U_R|^2 + |U_0|^2 + U_R^*U_0 + U_RU_0^*

$$

$$

= A_R^2 + \left(\frac{A_0}{z_0}\right)^2 + \frac{A_RA_0}{z_0}\left[\exp\left\{j\frac{k}{2z_0}(x^2+y^2)\right\} + \exp\left\{-j\frac{k}{2z_0}(x^2+y^2)\right\}\right]

$$

$$

= A_R^2 + \left(\frac{A_0}{z_0}\right)^2 + \frac{2A_RA_0}{z_0}\cos\left(\frac{k}{2z_0}(x^2+y^2)\right)

$$
# Continuous Zone Plate and Hologram Lenses

**Note:** $t(x,y) \propto \cos\left(\frac{k}{2z_0}(x^2+y^2)\right)$ is a continuous zone plate
$$

\left[t'(x,y) = \left[\text{step}\left(\cos\frac{k}{2z_0}(x^2+y^2)\right)\right] \text{ is an actual zone plate}\right]

$$

$$

\text{step}(x) = \begin{cases} 1, & x > 0 \\ 0, & x \leq 0 \end{cases}

$$

$$

\therefore

$$
If we illuminate $t(x,y)$ with a plane wave, we expect a bright point to occur at $z_0$

[Diagram showing continuous zone plate illuminated by plane wave, creating bright point at z₀]

\text{-}--

## ★ Consider the hologram as Superposition of 8 lenses

We have $t(x,y) = A_R^2 + \left(\frac{A_0}{z_0}\right)^2 + \frac{A_RA_0}{z_0}\left[\exp\left\{j\frac{k}{2z_0}(x^2+y^2)\right\} + \exp\left\{-\frac{jk}{2z_0}(x^2+y^2)\right\}\right]$

Recall: transmittance function of a lens:
$$

t(x,y) = \exp\left[-j\frac{k}{2f}(x^2+y^2)\right]

$$
$f$ = focal length of lens
$$

\therefore t(x,y) = \left\{A_R^2 + \left(\frac{A_0}{z_0}\right)^2\right\} \cdot (\text{lens of } \infty \text{ focal length})

$$

$$

+ \left\{\frac{A_RA_0}{z_0}\right\} \cdot (\text{lens of focal length } -z_0)

$$

$$

+ \left\{\frac{A_RA_0}{z_0}\right\} \cdot (\text{lens of focal length } +z_0)

$$
# General Holographic Imaging

[Diagram showing plane wave passing through object with multiple lenses (lens f₁-z₁, lens f₂-∞, lens f₃+∞)]

**Transmittance same as 3 lenses** → {0, I, 0}

**General Object + plane wave**

[Diagram showing plane wave illuminating general object creating superposition of zone plates]

Sum of point sources

— See 6(a —

\text{-}--

## ★ General Treatment of Holography
$$

\rightarrow

$$
Consider a one-lens imaging system:

[Diagram showing holographic imaging system with object (only care about intensity), information about object is contained in this plane, also contained in this plane since we see an image, and observation plane noting "Care about intensity and phase"]

This implies that the information is contained in all intermediate planes, although it may not be recognizably
# Three-Dimensional Nature of Holograms

## Three-dimensional nature:

**Record:**

[Diagram showing object with points A, B, C being recorded as hologram plate with concentric rings for each point]

\text{-} Each point source forms its own zone plate.
\text{-} Focal length of zone plate is given by distance between object and hologram plate

\text{-}--

**Play back:**

[Diagram showing plane wave illuminating hologram, with observe points A, B, C visible - Negative Focal Pts. "Virtual Image"]

[Diagram showing plane wave illuminating hologram, with observe points showing Positive Focal Pts. "Real Image"]

\text{-}--

**Note:** Real image is pseudoscopic, i.e., it goes out where original object went in, & vice versa. It looks like a death mask.
# Recording Phase Information

## Consider recording this wave front:

[Diagram showing reference wave and object wave interfering at film, with indicatrices representing complex numbers]
$$

\rightarrow

$$
Wave at film from object: $\hat{a}(x,y) = |a(x,y)|\exp[-j\phi(x,y)]$

## ★ → How do we record phase?

**Recall technique of interferometry in radio:**

**Technique 1** (base banding):
$$

\rightarrow

$$
Original signal $f_1(t) = \cos(\omega_1 t + \phi(t))$
$$

\rightarrow

$$
Add reference signal (local oscillator) $f_{\text{ref}}(t) = \cos(\omega_1 t)$
$$

\rightarrow

$$
Mix sum through non-linear mixer

**Recall:** $\cos(\alpha)\cos(\beta) = \frac{1}{2}[\cos(\alpha-\beta)+\cos(\alpha+\beta)]$
$$

|f_1(t) + f_2(t)|^2 = |\cos(\omega_1 t + \phi(t)) + \cos(\omega_1 t)|^2

$$

$$

= \cos^2(\omega_1 t + \phi(t)) + \cos^2(\omega_1 t) + 2\cos(\omega_1 t + \phi(t))\cos(\omega_1 t)

$$

$$

= \cos^2(\omega_1 t + \phi(t)) + \cos^2(\omega_1 t) + \cos(2\omega_1 t + \phi(t)) + \cos(\phi(t))

$$

$$

\rightarrow

$$
Low pass result with cutoff $< \omega_1$
$$

\text{L.P.}\{|f_1(t) + f_2(t)|^2\} = K + \cos(\phi(t))

$$

$$

\underbrace{\text{constant}}_{\text{result}}

$$
\text{-}--

**Technique 2** (heterodyning):
$$

\rightarrow

$$
Original signal: $f_1(t) = \cos(\omega_1 t + \phi(t))$
$$

\rightarrow

$$
Add ref signal of different freq and known but not constant phase: $f_2(t) = \cos(\omega_2 t + \psi(t))$
# Heterodyning Analysis

## Mix:
$$

\Rightarrow |f_1(t) + f_2(t)|^2 = |\cos(\omega_1 t + \phi(t)) + \cos(\omega_2 t + \psi(t))|^2

$$

$$

= \cos^2(\omega_1 t + \phi(t)) + \cos^2(\omega_2 t + \psi(t)) + 2\cos(\omega_1 t + \phi(t))\cos(\omega_2 t + \psi(t))

$$
**Recall:**
$\cos^2(\omega t) = \frac{1}{2} + \frac{1}{2}\cos(2\omega t)$
$$

= \cos^2(\omega_1 t + \phi(t)) + \cos^2(\omega_2 t + \psi(t)) + \cos((\omega_1 + \omega_2)t + \phi(t) + \psi(t))

$$

$$

+ \cos((\omega_1 - \omega_2)t + \phi(t) - \psi(t))

$$
\text{-}--

## Band pass:
$$

\Rightarrow \text{B.P.}\{|f_1(t) + f_2(t)|^2\} = \cos((\omega_1 - \omega_2)t + \phi(t) - \psi(t))

$$

$$

\underbrace{\qquad}_{\text{Band-pass}}

$$

$$

\underbrace{\qquad}_{\text{i.f.}}

$$

$$

\underbrace{\qquad}_{\text{frequency}}

$$
(i.f. = intermediate frequency)

High-freq. cut-off: $\omega_{c_1} < \omega_1$ or $\omega_2$

Low-freq. cut-off: $\omega_{c_2} > $ d.c.

**Note:** No d.c. term

\text{-}--

## ★ We use the exact same technique for a hologram, except that we substitute spatial frequency for temporal frequency

[Diagram showing frequency components at 0, $\omega_{c_1}$, $\omega_1$, $2\omega_1$, and $\omega_1 - \omega_2$]

**Recall:** Plane waves at different angles represent signals at different spatial frequencies:
$$

f(x,y) = e^{-j2\pi\alpha x} \quad \quad \alpha = \text{spatial freq} = \frac{\sin\theta}{\lambda}

$$

$$

\rightarrow

$$
Now, let object wave be $|a(x,y)|\exp[-j\phi(x,y)] = \hat{a}(x,y)$
$$

\rightarrow

$$
Let reference wave be $|A(x,y)|\exp[-j\psi(x,y)] = \hat{A}(x,y)$
$$

\rightarrow

$$
Mix: $I(x,y) = |A(x,y)|^2 + |a(x,y)|^2 + 2A(x,y)a(x,y)\cos(\psi(x,y) - \phi(x,y))$
$$

\underbrace{\qquad}_{\text{phase is preserved}}

$$
# Hologram Transmittance and Reconstruction

**Transmittance is linearly proportional to intensity**

**Assume:** i) $t(x,y) = \beta'(I(x,y))$

ii) Reference wave is constant amplitude $\Rightarrow |A(x,y)|^2 \cong |A|^2$
$$

\therefore t(x,y) = t_0 + \beta'\left[|a|^2 + \hat{A}^*\hat{a} + \hat{A}\hat{a}^*\right]

$$

$$

\underbrace{\text{Transmittance of hologram}}_{}

$$

$$

\underbrace{\beta'|A|^2 = \text{bias (constant)}}_{}

$$
\text{-}--

## Reconstruction:

Let reconstruction wave = $\hat{B}(x,y)$

[Diagram showing $\hat{B}(x,y)$ passing through $t(x,y)$]
$$

\hat{B}(x,y) \cdot t(x,y) = t_0\hat{B} + \beta'\hat{a}\hat{a}^*\hat{B} + \beta'\hat{A}^*\hat{B}\hat{a} + \beta'\hat{A}\hat{B}\hat{a}^*

$$

$$

\underbrace{\quad}_{U_1} \quad \underbrace{\quad}_{U_2} \quad \underbrace{\quad}_{U_3} \quad \underbrace{\quad}_{U_4}

$$
(off-axis correlation must be performed)

\text{-}--

## Case 1: Let $\hat{B}(x,y) = \hat{A}(x,y)$

(Reconstruction wave is equal to reference wave)

Then $U_3$ becomes: $\beta'\hat{A}^*\hat{B}\hat{a} = \beta'\hat{A}^*\hat{A}\hat{a}$
$$

= \beta'(|A|^2\hat{a}(x,y))

$$

$$

\Rightarrow \boxed{\text{original object wave } \hat{a}(x,y) \text{ is recovered.}}

$$
# Hologram Reconstruction - Case 2

## Case 2: Let $\hat{B}(x,y) = \hat{A}^*(x,y)$

(Record wave is complex conj. of ref wave)

Then $U_4$ becomes: $\beta'\hat{A}\hat{B}\hat{a}^* = \beta'\hat{A}\hat{A}^*\hat{a}^*$
$$

= \beta'|A|^2\hat{a}^*

$$

$$

\underbrace{\qquad}_{\text{constant}}

$$

$$

\boxed{\text{comp conj. of object wave } \hat{a}^*(x,y) \text{ is recovered}}

$$
\text{-}--

## ★ Image Formation

**Consider image of a point source:**

[Diagram showing ref wave A(x,y) illuminating point object $\hat{a}(x,y)$ at distance $z_0$ from film, creating hologram recording]
$$

\therefore \hat{a}(x,y) = \hat{a}_0\exp\left[jk\sqrt{z_0^2 + (x-x_0)^2 + (y-y_0)^2}\right]

$$
↑ object wave — ↑ diverging spherical wave located at $(x_0, y_0, z_0)$

\text{-}--

## Case 1 illumination: $\hat{B} = \hat{A}$
$$

\Rightarrow U_3(x,y) = \beta'|A|^2\hat{a}_0\exp\left[jk\sqrt{z_0^2 + (x-x_0)^2 + (y-y_0)^2}\right]

$$

$$

\Rightarrow

$$
Diverging plane wave, with apparent center at $(x_0, y_0, 0)$
# Virtual and Real Images

[Diagram showing ref $\hat{A}(x,y)$ wave passing through hologram creating virtual image at $z_0$]

\text{-}--

## Case 2 illumination: $\hat{B} = \hat{A}^*$
$$

\Rightarrow U_4(x,y) = \beta'|A|^2\hat{a}^*

$$

$$

= \beta'|A|^2\hat{a}_0^*\exp\left[-jk\sqrt{z_0^2 + (x-x_0)^2 + (y-y_0)^2}\right]

$$

$$

\Rightarrow

$$
Converging spherical wave, converges at pt. $(x_0, y_0, z_0)$

[Diagram showing converging wave creating real image]

**Note:**

[Diagram comparing original object view vs pseudoscopic real image view - "death mask"]

\text{-}--

## Separation of Undesirable Terms (off-axis hologram)
$$

\rightarrow

$$
Use Technique 2 in interferometry (pg. 62), heterodyning, so info is contained on a carrier (or i.f. frequency)
$$

\rightarrow

$$
Recall: Heterodyning requires using a reference signal (local oscillator) which is a different freq. than the object signal
$$

\Rightarrow

$$
different spatial freq $\Rightarrow$ different angle
# Off-Axis Hologram Recording

[Diagram showing reference wave $\hat{A}(x,y) = A\exp[-j2\pi\alpha y]$, $\alpha = \frac{\sin\theta}{\lambda}$ at angle to film, with object wave $\hat{a}(x,y)$]

**Amplitude at film:** $U(x,y) = A\exp[-j2\pi\alpha y] + \hat{a}(x,y)$, $\alpha = \frac{\sin\theta}{\lambda}$

**Intensity at film:** $I(x,y) = A^2 + |\hat{a}(x,y)|^2 + A\hat{a}(x,y)\exp[j2\pi\alpha y]$
$$

+ A\hat{a}^*(x,y)\exp[-j2\pi\alpha y]

$$
\text{-}--

## ★ Notice: If we write object as $\hat{a}(x,y) = |a(x,y)|\exp[-j\phi(x,y)]$

We have intensity:
$$

I(x,y) = A^2 + |a(x,y)|^2 + 2A|a(x,y)|\cos[2\pi\alpha y - \phi(x,y)]

$$

$$

\underbrace{\qquad}_{\text{amplitude modulation}} \quad \underbrace{\qquad}_{\text{carrier}} \quad \underbrace{\qquad}_{\text{phase modulation}}

$$

$$

\Rightarrow

$$
This is identical to heterodyning, where
$$

(\omega_1 - \omega_2) = \text{i.f.} = 2\pi\alpha_y

$$

$$

\underbrace{\text{temporal analog}}_{}

$$

$$

\underbrace{\text{spatial}}_{}

$$

$$

\psi = 0

$$
because plane wave is local osc.
$$

\Rightarrow

$$
local osc. is pure cosωt with no $\psi(t)$ component
# Reconstruction of Off-Axis Holograms
$$

\underset{\text{screen film}}{t(x,y)} = t_0 + \beta'\left[|a|^2 + A\hat{a}(x,y)\exp[j2\pi\alpha y] + A\hat{a}^*(x,y)\exp[-j2\pi\alpha y]\right]

$$

$$

\underbrace{\quad}_{t_1} \quad \underbrace{\quad}_{t_2} \quad \underbrace{\quad}_{t_3} \quad \underbrace{\quad}_{t_4}

$$
$\beta'$ = constant related to Film Transmittance

where $t_0 = \beta'A^2$
$$

\rightarrow

$$
Assume reconstruction illumination is a normally incident plane wave:
$$

B(x,y) = B

$$
**Then:**
\text{-} $U_1(x,y) = t_0 B$
\text{-} $U_2(x,y) = \beta'B|a(x,y)|^2$
\text{-} $U_3(x,y) = \beta'BA\hat{a}(x,y)\exp[j2\pi\alpha y]$
\text{-} $U_4(x,y) = \beta'BA\hat{a}^*(x,y)\exp[-j2\pi\alpha y]$

\text{-}--

## ★ Notice:

\text{-} $U_1 \Rightarrow$ proportional to on-axis plane wave
\text{-} $U_2 \Rightarrow$ garbage, also centered on-axis
\text{-} $U_3 \Rightarrow$ proportional to object wave $\hat{a}(x,y)$ times a linear phase factor $\exp[j2\pi\alpha y]$. This is equivalent to tilting the object wave $\hat{a}(x,y)$ by angle $\theta$.
\text{-} $U_4 \Rightarrow$ proportional to complex conj. of object wave $\hat{a}^*(x,y)$ times linear phase factor $\exp[-j2\pi\alpha y] \Rightarrow$ tilt is in $-\theta$ direction.
# Reflection Holograms and Multiplex Holograms

## Reflection Holograms

[Diagram showing object wave and ref wave entering from opposite sides of thick film with λ/2 spacing between layers, creating Bragg stack]

**Play back:**

[Diagram showing Bragg stack reflecting proper wavelength λ]

Bragg stack selects proper wavelength λ. Thus, it can work in white light.

\text{-}--

## Multiplex Holograms

[Diagram showing object being spun while conventional photograph taken at many angles]

[Diagram showing single photograph #1 being recorded as thin hologram with object wave, ref wave at angles #2, #3, #4]

[Diagram showing cylindrical hologram playback with View 1 (Photo 1-m) and View 2 (Window m+1→n)]
# Holographic Laser Cavities

## Holographic Laser Cavities:

[Diagram showing laser cavity with diffractive optic mirror 1 (T = Mode), mirror 2 (diffractive optic), and transmittance functions $t_1(x',y')$ and $t_2(x',y')$]

Let $a(x,y)$ be complex field of desired mode at mirror 1:
$$

\hat{a}(x,y) = \iint A(u,v)\exp[-j2\pi(xu+yv)]\,du\,dv \quad \text{([Plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) expansion)}

$$
At Mirror 2:
$$

\hat{b}(x',y') = \iint A(u,v)\exp[-j2\pi(xu+yv)]\exp\left[jkl\left[1-(\lambda u)^2-(\lambda v)^2\right]^{1/2}\right]\,du\,dv

$$

$$

\underbrace{\qquad}_{\text{free-space propagator}}

$$
\text{-}--

Let $t_2(x',y') = \frac{\hat{b}^*(x',y')}{\hat{b}(x',y')}$ (All-phase function)

Then $\hat{b}(x',y') \cdot t_2(x',y') = \hat{b}^*(x',y')$
$$

= \iint A^*(u,v)\exp[-j2\pi(xu+yv)] \times \exp\left\{-jkl\left[1-(\lambda u)^2-(\lambda v)^2\right]^{1/2}\right\}\,du\,dv

$$
Prop back to mirror 1:
$$

\Rightarrow \iint A^*(u,v)\exp[-j2\pi(xu+yv)]\,du\,dv = a^*(x,y).

$$
If we let $t_1(x,y) = \frac{a(x,y)}{a^*(x,y)}$, we have

the final field regenerating the original field $a(x,y)$
$$

\Rightarrow

$$
**Laser Mode**
# Essentials of Holography


**Recording:**

Obj wave: $a(x,y)$

Ref wave: $b(x,y)$
$$

I(x,y) = |a(x,y) + b(x,y)|^2 = |b(x,y)|^2 + |a(x,y)|^2

$$

$$

+ a(x,y)b^*(x,y) + a^*(x,y)b(x,y) \propto t(x,y)

$$

$$

\underbrace{\qquad}_{\text{trans. of hologram}}

$$
\text{-}--

**Play back:**

Play back wave = $C(x,y)$
$$

A(x,y) = C(x,y) \cdot t(x,y)

$$

$$

= C(x,y)|b(x,y)|^2 + C(x,y)|a(x,y)|^2 + C(x,y)a(x,y)b^*(x,y)

$$

$$

+ C(x,y)a^*(x,y)b(x,y)

$$
\text{-}--

## Special Case: $b = e^{-j2\pi\alpha x}$, $c = e^{-j2\pi dx}$

($b = c$)
$$

A \propto \underbrace{e^{-j2\pi\alpha x}}_{t_1} + \underbrace{|a(x,y)|^2 e^{-j2\pi\alpha x}}_{t_2} + \underbrace{a(x,y)}_{t_3} + \underbrace{a^*(x,y)e^{-j2\pi(2\alpha)x}}_{t_4}

$$
[Diagram showing recording geometry with object wave and reference wave at angle]

[Diagram showing playback geometry with reconstructed waves $t_1$, $t_2$, $t_3$, $t_4$ separating at different angles]
# Special Case Hologram

## Special Case: $b = e^{-j2\pi\alpha x}$, $c = 1$
$$

A \propto \underbrace{1}_{t_1} + \underbrace{|a(x,y)|^2}_{t_2} + \underbrace{a(x,y)e^{j2\pi\alpha x}}_{t_3} + \underbrace{a^*(x,y)e^{-j2\pi\alpha x}}_{t_4}

$$
[Diagram showing recording geometry with reference wave b at angle to film and object wave c]

[Diagram showing playback geometry with hologram producing four terms: $t_1$, $t_2$ on-axis, $t_3$ (Virtual), $t_4$ (Real)]

\text{-}--

**Record** → **Playback**

[Diagram showing spectral components in frequency domain]

\text{-} $t_4$ at $-\alpha$
\text{-} $t_1$, $t_2$ centered at origin
\text{-} $t_3$ centered at $\alpha$ (contains $\mathscr{F}\{a(x,y)\}$)
\text{-} Recover info at $f_x$
$$

\text{Hologram} = t_1 + t_2 + a \cdot (\text{carrier}) + a^* \cdot (\text{carrier})

$$
# Minimum Reference Wave Angle

[Diagram showing hologram reconstruction with plane wave illumination B, producing $U_3$ (Virtual Image), $U_1$, and $U_4$ (Real Image)]

\text{-}--

## ★★ Minimum Reference Wave Angle

$\Rightarrow$ Find minimum carrier frequency "$\alpha$" so that spectra of $t_3$ and $t_4$ do not overlap each other or $t_1$, $t_2$.

(This is very similar to the sampling theorem)

[Diagram showing spectral components: $\mathscr{F}\{a\}$, $\mathscr{F}\{a^*\}$, and $t_3$]

[Diagram showing hologram spectrum with labeled components]
$$

\text{hologram} = t_1 + t_2 + \hat{a} \cdot \text{carrier} + \hat{a}^* \cdot (-\text{carrier})

$$
$\Rightarrow$ We could recover $\hat{a}$'s carrier by Fourier transforming $t(x,y)$ and spatial filtering, assuming $\mathscr{F}\{\hat{a}\}$'s carriers does not overlap any other spectral components.

\text{-}--

**Define:**
$$

G_1(\xi,\eta) = \mathscr{F}\mathscr{F}\{t_1(x,y)\} = t_0\,\delta(\xi,\eta)

$$

$$

G_2(\xi,\eta) = \mathscr{F}\mathscr{F}\{t_2(x,y)\} = \beta' G_a(\xi,\eta) * G_a(\xi,\eta)

$$
where $G_a(\xi,\eta) = \mathscr{F}\mathscr{F}\{\hat{a}(x,y)\}$
$$

G_3(\xi,\eta) = \mathscr{F}\mathscr{F}\{t_3(x,y)\} = \beta' A\,G_a(\xi,\eta-\alpha)

$$
and
$$

G_4(\xi,\eta) = \mathscr{F}\mathscr{F}\{t_4(x,y)\} = \beta' A\,G_a^*(-\xi,-\eta-\alpha)

$$
# Fourier Transform of Hologram

**Note:** $G_a(\xi,\eta)$ is the Fourier transform of $\hat{a}(x,y)$

[Diagram showing object wave evaluated at hologram plane]

$\hat{a}(x,y)$ is the object wave evaluated at hologram plane.

$\Rightarrow$ Actual object distribution and distribution at hologram $\hat{a}(x,y)$ are related by free space diffraction (Fresnel diffraction formula)

$\Rightarrow$ This means F.T. of $\hat{a}(x,y)$ = F.T. of object times free space transfer function
$$

H(\xi,\eta) = \exp\left\{jkz_0\left[1-\lambda^2(\xi^2+\eta^2)\right]^{1/2}\right\}

$$
$\Rightarrow$ $\therefore$ The diffraction from object to hologram just changes the phase of the Fourier components, and hence the bandwidth of $\hat{a}(x,y)$ (at hologram) is the same as the bandwidth of the object.

$\Rightarrow$ Set this bandwidth be $B$

[Diagram showing $|G_a|$ with bandwidth $B$ centered at origin - "Transform of object"]

[Diagram showing $|G_1|$ spike, convolved with $|G_2|$ of width $2B$, and $|G_3|$ with bandwidth $B$ - "Transform of hologram transmittance"]
# Separation Requirement and Minimum Angle

$\Rightarrow$ For separation, we require
$$

\alpha \geq 3B

$$
or since $\alpha = \frac{\sin\theta}{\lambda}$, $\sin\theta \geq 3B\lambda$
$$

\Rightarrow \boxed{\theta_{\min} = \arcsin(3B\lambda)}

$$
**Minimum Reference Angle**

\text{-}--

## Example:

[Diagram showing reference wave at angle to hologram, with object (Beethoven) to the left]

Bandwidth of object = highest freq = $\frac{1}{\text{smallest change}}$

Assume smallest variation = $10\mu$
$$

\Rightarrow B = \frac{1}{10\mu} = 100 \text{ /mm}

$$

$$

\boxed{\theta_{\min} = \arcsin\left(3(100)(0.5 \times 10^{-3})\right) = 9°}

$$

$$

\boxed{\text{Carrier frequency } \alpha = 3B = 300 \text{ lines/mm}}

$$
\text{-}--

**★ Note:** This means very high resolution film (300 lines/mm is a lot!) must be used. Such film does exist. Kodak 649F has a resolution of 1500-2000 lines/mm (and an ASA of 0.06!). Note also that motion more than a fraction of a carrier period ($3\mu$ in above example) during exposure will wash out carrier $\Rightarrow$ no hologram.
# Holographic Image Formation and Magnification


[Diagram showing optical setup with:
\text{-} Reference wave at angle
\text{-} Object at distance $d_1$ from hologram
\text{-} Point $e_v$ on object
\text{-} Hologram plane
\text{-} Image plane at $(x_2, y_2)$
\text{-} Final observation point at $\phi_1$ and coordinates $(x_3, y_3)$]

$\Rightarrow$ Consider a diffuse object such as a statue, so the light reflecting off the object is
$$

\boxed{\text{This is the object}} \Rightarrow U_1(x_1,y_1) = |A(x_1,y_1)|e^{j\psi(x_1,y_1)} \leftarrow \text{Random phase}

$$
$\Rightarrow$ Reference beam is produced by a point source off-axis, and $\rho_v$ away. Hence in the hologram plane the reference produces:
$$

\boxed{\text{Reference Beam}} \quad U_2(x_2,y_2) = V_0 \exp\left[jk_1\left(x_2\sin\phi + \frac{x_2^2+y_2^2}{2\rho_v}\right)\right]

$$
**Notice:** i) $k_1 \Rightarrow$ recording wavelength

ii) If $\rho_v \to \infty$, we have the usual off-axis plane wave $\exp(j2\pi\alpha x_2)$, $\alpha = \frac{\sin\phi}{\lambda}$

$\Rightarrow$ To calculate the light field created by the object at the hologram, we use the Fresnel diffraction formula:
$$

\boxed{\text{Object Beam}} \quad U_2(x_2,y_2) = \frac{\exp(jk_1d_1)}{j\lambda_1 d_1} h_1(x_2,y_2;d_1)

$$

$$

\iint U_1(x_1,y_1) h_1(x_1,y_1;d_1) \exp\left[-jk_1 \frac{(x_1x_2+y_1y_2)}{d_1}\right] dx_1 dy_1

$$
where: $h_1(x_1,y;d) = \exp\left[jk_1\frac{(x^2+y^2)}{2d}\right]$ ← secondary wavelet
# Hologram Interference and Transmittance

Recall that interference gives an intensity (and thus transmittance of hologram) which is in 4 parts:
$$

\begin{cases} a = \text{obj} \\ A = \text{ref} \end{cases} \quad I = |a+A|^2 = |A|^2 + |a|^2 + aA^* + a^*A

$$

$$

\underbrace{\qquad}_{\text{primary}} \quad \underbrace{\qquad}_{\text{secondary}}

$$
1. We define 3rd term as the **primary wave** since it contains the object "$a(x,y)$"

2. We define 4th term as the **secondary wave** since it contains the conjugate of the object $a^*(x,y)$

$\Rightarrow$ Now consider only the primary wave term resulting from containing $U_2(x_2,y_2)$ and $V_2(x_2,y_2)$ (i.e. $UV^*$)
$$

\boxed{t(x_2,y_2) = U(x_2,y_2)V^*(x_2,y_2) = V_0 U_2(x_2,y_2) \exp\left[-jk_1\left(x_2\sin\phi + \frac{x_2^2+y_2^2}{2\rho_v}\right)\right]}

$$
$\Rightarrow$ Now illuminate the hologram with another off-axis spherical wave of wavelength $\lambda_2$ (amount to $\lambda_2$)
$$

\boxed{W(x_2,y_2) = W_0 \exp\left[jk_2\left(x_2\sin\psi + \frac{x_2^2+y_2^2}{2\rho_w}\right)\right]} \quad \boxed{\text{Read out beam}}

$$
$\Rightarrow$ After passing through hologram and propagating a distance $d$:
$$

U_3(x_3,y_3) = V_0 W_0 \frac{\exp(jk_2d_2)}{j\lambda_2 d_2} h_2(x_3,y_3;d_2)

$$
← Fresnel diffraction formula
$$

\times \iint U_2(x_2,y_2) h_1(x_2,y_2;-\rho_v) \exp[-jk_1 x_2 \sin\phi]

$$

$$

\times h_2(x_2,y_2;\rho_w) \exp[jk_2 x_2 \sin\psi] h_2(x_2,y_2;d_2)

$$
← more Fresnel formulas
$$

\times \exp\left[-jk_2 \frac{(x_2x_3+y_2y_3)}{d_2}\right] dx_2 dy_2

$$
← diff. formula
# Focusing Condition

$\Rightarrow$ Substituting for $U_2(x_2,y_2)$ yields:
$$

U_3(x_3,y_3) = -V_0 W_0 \frac{\exp[j(k_1d_1+k_2d_2)]}{\lambda_1\lambda_2 d_1 d_2} h_2(x_3,y_3;d_2)

$$

$$

\times \iint \exp\left\{j\pi(x_2^2+y_2^2)\left[\frac{1}{\lambda_2 d_2} + \frac{1}{\lambda_2 d_1} - \frac{1}{\lambda_1\rho_v} + \frac{1}{\lambda_2\rho_w}\right]\right\}

$$

$$

\times \exp\left[j2\pi x_2\left(\frac{\sin\psi}{\lambda_2} - \frac{\sin\phi}{\lambda_1}\right)\right] \exp\left[-\frac{k_2(x_2x_3+y_2y_3)}{d_2}\right]

$$

$$

\times \iint U_1(x_1,y_1) h_1(x_1,y_1;d_1) \exp\left[-\frac{j2\pi}{\lambda_1}(x_1x_2+y_1y_2)\right] dx_1 dy_1 dx_2 dy_2

$$
$\Rightarrow$ Reverse the order of integration, and drop minor sign and $\exp[j(k_1d_1+k_2d_2)]$
$$

U_3(x_3,y_3) = \frac{V_0 W_0}{\lambda_1\lambda_2 d_1 d_2} h_2(x_3,y_3;d_2) \iint U_1(x_1,y_1) h_1(x_1,y_1;d_1)

$$

$$

\times \iint \exp\left\{j\pi(x_2^2+y_2^2)\left[\frac{1}{\lambda_2 d_2} + \frac{1}{\lambda_2 d_1} - \frac{1}{\lambda_1\rho_v} + \frac{1}{\lambda_2\rho_w}\right]\right\}

$$

$$

\times \exp\left[-j2\pi x_2\left(\frac{\sin\phi}{\lambda_1} - \frac{\sin\psi}{\lambda_2} + \frac{x_1}{\lambda_1 d_1} + \frac{x_3}{\lambda_2 d_2}\right)\right]

$$

$$

\times \exp\left[-j2\pi y_2\left(\frac{y_1}{\lambda_1 d_1} + \frac{y_3}{\lambda_2 d_2}\right)\right] dx_2 dy_2 dx_1 dy_1

$$
\text{-}--
$$

\boxed{\text{Focusing Condition}: \quad \frac{1}{\lambda_1 d_1} + \frac{1}{\lambda_2 d_2} - \frac{1}{\lambda_1\rho_v} + \frac{1}{\lambda_2\rho_w} = 0}

$$
We shall show that if $d_1$ (object distance) and $d_2$ (image distance) satisfy this condition, the above expression reduces to an image.
$$

\Rightarrow

$$
With this condition applied, inner integral becomes
$$

\iint \exp\left[-j2\pi x_2\left(\frac{\sin\phi}{\lambda_1} - \frac{\sin\psi}{\lambda_2} + \frac{x_1}{\lambda_1 d_1} + \frac{x_3}{\lambda_2 d_2}\right)\right] \exp\left[-j2\pi y_2\left(\frac{y_1}{\lambda_1 d_1} + \frac{y_3}{\lambda_2 d_2}\right)\right] dx_2 dy_2

$$

$$

= \iint \exp\left[-j2\pi(x_2\xi + y_2\eta)\right] dx_2 dy_2, \quad \text{where} \quad \xi = \left(\frac{\sin\phi}{\lambda_1} - \frac{\sin\psi}{\lambda_2} + \frac{x_1}{\lambda_1 d_1} + \frac{x_3}{\lambda_2 d_2}\right)

$$

$$

\eta = \left(\frac{y_1}{\lambda_1 d_1} + \frac{y_3}{\lambda_2 d_2}\right)

$$
# Total Integral and Magnification

But this is just the Fourier transform of unity.

$\Rightarrow$ Hence, $\displaystyle\iint \exp[-j2\pi(x_2\xi + y_2\eta)] dx_2 dy_2 = \delta(\xi,\eta)$
$$

= \delta\left(\frac{\sin\phi}{\lambda_1} - \frac{\sin\psi}{\lambda_2} + \frac{x_1}{\lambda_1 d_1} + \frac{x_3}{\lambda_2 d_2}\right) \delta\left(\frac{y_1}{\lambda_1 d_1} + \frac{y_3}{\lambda_2 d_2}\right)

$$
and the **total integral** becomes:
$$

U_3(x_3,y_3) = \frac{V_0 W_0}{\lambda_1\lambda_2 d_1 d_2} h_2(x_3,y_3;d_2) \iint U_1(x_1,y_1) h_1(x_1,y_1;d_1) \,\delta\left(\frac{\sin\phi}{\lambda_1} - \frac{\sin\psi}{\lambda_2} + \frac{x_1}{\lambda_1 d_1} + \frac{x_3}{\lambda_2 d_2}\right)

$$

$$

\times \delta\left(\frac{y_1}{\lambda_1 d_1} + \frac{y_3}{\lambda_2 d_2}\right) dx_1 dy_1

$$

$$

= \frac{\lambda_1 d_1}{\lambda_2 d_2} V_0 W_0 h_2(x_3,y_3;d_2) \iint U_1(x_1,y_1) h_1(x_1,y_1;d_1)

$$

$$

\times \delta\left(x_1 + \frac{\lambda_1 d_1}{\lambda_2 d_2}x_3 + d_1\sin\phi - \frac{\lambda_1 d_1}{\lambda_2}\sin\psi\right) \delta\left(y_1 + \frac{\lambda_1 d_1}{\lambda_2 d_2}y_3\right) dx_1 dy_1

$$
\text{-}--

**Define magnification** (x-y plane) as
$$

M = \frac{\lambda_2 d_2}{\lambda_1 d_1}

$$
Then
$$

\boxed{U_3(x_3,y_3) = \frac{V_0 W_0}{M} h_2(x_3,y_3;d_2) \, U_1\left(-\frac{x_3}{M} - d_1\sin\phi + d_2\sin\psi, -\frac{y_3}{M}\right)}

$$

$$

\times h_1\left(-\frac{x_3}{M} - d_1\sin\phi + \frac{d_2\sin\psi}{M}, -\frac{y_3}{M}; d_1\right)

$$
$\Rightarrow$ We see that a scaled version of $U_1$ results, and that it is shifted by an amount $-d_1\sin\phi + d_2\frac{\sin\psi}{M}$.

$\Rightarrow$ There are also 2 quadratic phase factors $h_2$ & $h_1$.
# Magnification: Transverse and Longitudinal

## Magnification (Transverses and Longitudinal)

$\Rightarrow$ We defined transverse mag as: $M = \frac{\lambda_2 d_2}{\lambda_1 d_1}$ ← Looks like mag is linearly prop. to ratio of wavelengths.

**★** However, $d_2/d_1$ is a function of wavelength

$\Rightarrow$ From focusing condition (primary wave)
$$

d_2 = \left(-\frac{1}{\rho_w} + \frac{\lambda_2}{\lambda_1\rho_v} - \frac{\lambda_2}{\lambda_1 d_1}\right)^{-1}

$$
(Image reconstruction / Distance for primary wave)

$\Rightarrow$ If we perform the same analysis for secondary wave
$$

d_2 = \left(-\frac{1}{\rho_w} - \frac{\lambda_2}{\lambda_1\rho_v} + \frac{\lambda_2}{\lambda_1 d_1}\right)^{-1}

$$
(Image reconstruction / Distance for secondary wave)

If $d_2$ is negative (behind hologram), we have a virtual image.

If $d_2$ is positive (in front of hologram), image is real.

**★** $\Rightarrow$ We see from above that either primary or secondary image can be either virtual or real, depending on $\lambda_1$, $\lambda_2$, $\rho_w$, $\rho_v$, $d_1$.

**Notice:** If $\lambda_1 = \lambda_2$ and $\rho_w = \rho_v$ (and $\phi = \psi$) $d_2$ must be $d_1$ for $M = +1$ and indicates that:
$$

d_2 = -d_1 \quad (\text{primary wave}) \Rightarrow \text{virtual image}

$$
and $M = -1 \Rightarrow |U_3(x_3,y_3)|^2 = |U_1(x_3-d_1\sin\phi, y_3)|^2$
$$

d_2 = \left(\frac{1}{d_1} - \frac{2}{\rho_w}\right)^{-1}

$$
(secondary wave)

$\Rightarrow$ In this case, primary wave forms an image just like the original (only shifted) and on the opposite side of the viewer

$\Rightarrow$ Secondary image however depends on $d_1$ and $\rho_w$.

When $\rho_w = \infty$ (plane wave), $d_2 = d_1$ (real image), and $M = 1$
# Magnification as a Function of Object Distance

## Magnification as a function of object distance:

Recall: $M = \frac{\lambda_2 d_2}{\lambda_1 d_1}$

and
$$

d_2 = \left(-\frac{1}{\rho_w} + \frac{\lambda_2}{\lambda_1\rho_v} - \frac{\lambda_2}{\lambda_1 d_1}\right)^{-1}

$$
(primary wave)
$$

d_2 = \left(-\frac{1}{\rho_w} - \frac{\lambda_2}{\lambda_1\rho_v} + \frac{\lambda_2}{\lambda_1 d_1}\right)^{-1}

$$
(secondary wave)
$$

\Rightarrow \boxed{M_{\pm} = \left(-\frac{\lambda_1 d_1}{\lambda_2\rho_w} \pm \frac{d_1}{\rho_v} + 1\right)^{-1}} \begin{array}{l} \leftarrow \text{primary} \\ \leftarrow \text{secondary} \end{array} \quad \boxed{\text{Transverse Magnification}}

$$
\text{-}--

**★** We can calculate **longitudinal magnification** by change in image distance vs. change in object distance:
$$

M_{\text{long}} = \frac{d(d_2)}{d(d_1)}, \quad \text{where } d_2 = \frac{1}{\left(-\frac{1}{\rho_w} \pm \frac{\lambda_2}{\lambda_1\rho_v} - \frac{\lambda_2}{\lambda_1 d_1}\right)}

$$

$$

\Rightarrow M_{\text{long}} = \frac{d(d_2)}{d(d_1)} = \pm \frac{\lambda_2}{\lambda_1} \frac{d\left(\frac{1}{d_1}\right)}{d(d_1)} \cdot \frac{1}{\left(-\frac{1}{\rho_w} \pm \frac{\lambda_2}{\lambda_1\rho_v} - \frac{\lambda_2}{\lambda_1 d_1}\right)^2} = \pm \frac{\lambda_2}{\lambda_1}\left[\frac{1}{d_1^2}\right] \cdot \frac{1}{\left(-\frac{1}{\rho_w} \pm \frac{\lambda_2}{\lambda_1\rho_v} - \frac{\lambda_2}{\lambda_1 d_1}\right)^2}

$$

$$

= \pm \frac{\lambda_2}{\lambda_1} \cdot \frac{\left(\frac{\lambda_1}{\lambda_2}\right)^2}{\left(-\frac{d_1\lambda_1}{\lambda_2\rho_w} \pm \frac{d_1}{\rho_v} + 1\right)^2}

$$

$$

= \frac{\pm\lambda_1}{\lambda_2} \cdot \frac{1}{\left(-\frac{\lambda_1 d}{\lambda_2\rho_w} \pm \frac{d_1}{\rho_v} + 1\right)^2} = \pm \frac{\lambda_1}{\lambda_2} M_{\pm}^2

$$
\text{-}--

**Note:** It is possible to have significantly different transverse and longitudinal magnifications.
# Magnification Example and Interferometry Application

## Example: Plane wave read-out: $\rho_w = \infty$
$$

\Rightarrow M_{\pm} = \left(\pm\frac{d_1}{\rho_v} + 1\right)^{-1} \leq 2 \text{ not a function of } \lambda_1/\lambda_2

$$
But $M_{\text{long}} = \pm \frac{\lambda_1}{\lambda_2} M_{\pm}^2 = \pm \frac{\lambda_1}{\lambda_2}\left(\pm\frac{d_1}{\rho_v} + 1\right)^{-2}$

$\therefore$ A large difference in wavelength $\frac{\lambda_1}{\lambda_2}$ has no effect on transverse mag., and a great effect on longitudinal mag. This causes **severe distortions**.

\text{-}--

## ★ Applications

### Interferometry:

[Diagram of interference measurement setup]

\text{-} Interferometer coherent beams (add amplitudes). Phase imbalance in one beam are observed as optical variations of the sum (of the sum in the form of intensity)

$\Rightarrow$ How can we interpret two beams which occur at different times?

(For example the two beams may come from the same object, see before a stress is placed on the object, and after the stress)
# Holographic Interferometry

$\Rightarrow$ Using holography, record a multiple exposure (2 exposures in the obvious example)
$$

E = \sum_{k=1}^{N} T_k I_k

$$
$T_k$ are exposure times, $I_k$ are intensities of different holograms
$$

\Rightarrow I_k = |A(x,y) + a_k(x,y)|^2

$$

$$

\uparrow \text{Fixed reference} \quad \uparrow \text{Many objects}

$$

$$

\Rightarrow E = \sum_{k=1}^{N} T_k |A|^2 + \sum_{k=1}^{N} T_k |a_k|^2

$$

$$

+ \sum_{k=1}^{N} T_k A^* a_k + \sum_{k=1}^{N} T_k A a_k^*

$$

$$

\underbrace{\qquad}_{\text{important term}} \quad \underbrace{\qquad}_{\text{important term}}

$$
3rd term gives transmittance:
$$

t_3 = \beta \sum_{k=1}^{N} T_k A^* a_k

$$
4th term: $t_4 = \beta \sum_{k=1}^{N} T_k A a_k^*$

If we illuminate 3rd term with $A$, we reconstruct
$$

U_3 = \beta \sum_{k=1}^{N} T_k |A|^* A | a_k = \beta |A|^2 \sum_{k=1}^{N} T_k a_k

$$

$$

\underbrace{\qquad}_{N \text{ virtual images superimposed, and thus interfere.}}

$$
\text{-}--

**Example:** Observing heat distribution

[Diagram showing metal block with reference wave, object wave through heated zone, and resulting interference pattern going to eye]

$\Rightarrow$ Perform double exposure - Once with hot plate off, once with plate on.
# Non-Destructive Testing and Aberration Correction

## Reconstruction:

[Diagram showing hologram with read-out beam producing interference pattern going to eye]

\text{-}--

**Example:** Non-destructive testing - How can we predict whether a mechanical component is going to fail at high stress without actually applying the full stress?

$\Rightarrow$ **Solution:** Apply small stress and observe strain using holographic interferometry

[Diagram showing automobile tire with marked lines]

\text{-} Apply small amount of air in between exposures, and observe interference. Many interference lines near large strain $\Rightarrow$ weak spot in tire.

\text{-}--

## Aberration Correction

**Method 1:** (Image Coding)

[Diagram showing recording geometry with illumination through aberrating medium onto object, with reference wave hitting film]

**Recording Geometry**
# Aberration Correction Methods

$\Rightarrow$ Let object wave (undistorted) at aberrating medium $= U_1(x,y)$

$\Rightarrow$ Aberration introduces phase shifts of $\exp[jW(x,y)]$ so resultant object wave at aberration is $U_1(x,y)\exp[jW(x,y)]$

$\Rightarrow$ Hologram records this wave and the complex conjugate

$\Rightarrow$ **Play back:** (use conjugate read-out beam $A^*$) $\Rightarrow$ conjugate real image

$\Rightarrow$ term 4: $|A^*A| a^* \Rightarrow |A|^2 U_1^*(x,y) \exp[-jW(x,y)]$

occurs at aberration plate d in front of hologram

[Diagram showing play back geometry with read out beam from $A^*$ (conjugate of reference beam), same aberrating medium, real image of object]

$\therefore$ After passing through the same aberrating medium,

we have $|A|^2 U_1^*(x,y) \exp[-jW(x,y)] \exp[jW(x,y)]$
$$

\underbrace{\qquad}_{\text{real image}} \quad \underbrace{\qquad}_{\text{Aberration plate}}

$$

$$

= |A|^2 U_1^*(x,y) \leftarrow

$$
Produces undistorted real image.

This technique has obvious applications in cryptography. Hologram is coded message. Aberration plate is the code.
# Compensation Plate Method

## Method 2: (Compensation plate)

$\Rightarrow$ Record the impulse response of the aberration:

[Diagram showing point source with spherical waves passing through aberrating medium onto film]
$$

\Rightarrow \text{Object wave} = a = \exp[jW(x,y)]

$$

$$

\underbrace{\qquad}_{\text{aberration function}}

$$

$$

\text{Reference wave} = A = \exp[j2\pi\alpha y] \leftarrow \text{[plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/)}

$$
$\Rightarrow$ If we use a read-out of $a$, we generate $A \Rightarrow$ playback

[Diagram showing general object passing through aberrating medium hitting film, then plane wave output]

$\therefore$ Every point on object produces an aberrated spherical wave at the hologram. The component $a^*$ on the hologram can remove this aberration and produces a plane wave with angle proportional to the original point location. This angles are conjugate at a lens.
# Lens Aberration Compensation

## Application: Lens aberration compensation

### Method 3: (Atmospheric compensation)

[Diagram showing point reference source, object passing through aberrating medium onto film]

$\Rightarrow$ Assume aberrating medium is just in front of film
$$

\Rightarrow \text{object wave: } a(x,y)\exp[jW(x,y)]

$$

$$

\text{reference wave: } A(x,y)\exp[jW(x,y)]

$$

$$

\Rightarrow \text{Hologram} \propto I = |a(x,y)\exp[jW(x,y)] + A(x,y)\exp[jW(x,y)]|^2

$$

$$

= |a(x,y)|^2 + |A(x,y)|^2 + a(x,y)A^*(x,y) + a^*(x,y)A(x,y)

$$
$\therefore$ Aberration function $\exp[jW(x,y)]$ has not been recorded!

$\Rightarrow$ Reconstruction with wave $A \Rightarrow$ 3rd term $\Rightarrow$
$$

\Rightarrow |A^*A| \, a(x,y)

$$
reconstructs original object

(Show Goodman, p9267)

\text{-}--

## Holographic data storage:

[Diagram showing object being recorded as hologram, then F.T. hologram shown going to F.T. into about 1 bit - Note: in F.T. hologram, is stored everywhere in plane.]

$\Rightarrow$ Photorefractive crystals act as real-time storage (3-dim storage).
# Photorefractive Effect


[Diagram showing reference wave and object wave entering BaTiO₃ Crystal]

\text{-}--

**I** [Graph showing interference pattern - sinusoidal intensity variation with x]

Interference pattern generates photo-excited carriers

\text{-}--

**S** [Graph showing charge distribution with + and - regions]

Free carriers migrate to dark regions, creating spatial charge distribution

\text{-}--

**Δn** [Graph showing refractive index variation]

Linear electrooptic effect produces volume phase grating proportional to electric field.
# Holographic Association and Memory

## Association

[Diagram showing associative memory network:
\text{-} Input $(1,2,3,4)$ maps to output $(a,b,c,d)$
\text{-} Input $(26,25,24,23)$ maps to output $(10,5,2,6)$
\text{-} Input $(x,\beta,\gamma,\delta)$ maps to output $(z,\gamma,x,\omega)$]

Given $(1,2,3,4) \rightarrow$ Retrieve $(a,b,c,d)$

Given $(z,\gamma,x,\omega) \rightarrow$ Retrieve $(26,25,24,23)$

\text{-}--

[Diagram showing two beams A and B interfering]
$$

t \propto |A|^2 + |B|^2 + AB^* + BA^*

$$

$$

\qquad\qquad\qquad \text{I} \quad \text{II} \quad \text{III} \quad \text{IV}

$$
Illuminate with B: $\text{III} \Rightarrow |B|^2 A \rightarrow \tilde{} \, A$ wavefront
$$

\underbrace{\qquad}_{\text{Flat phase}}

$$
Illuminate with A: $\text{IV} \Rightarrow |A|^2 B \rightarrow \tilde{} \, B$ wavefront
$$

\underbrace{\qquad}_{\text{Flat phase}}

$$
\text{-}--

**Partial data retrieval:** (Recall: A small part of a hologram can reproduce the entire image)
$$

(1,2,3,?) \longrightarrow (a,b,c,d) + \text{noise}$$

An incomplete ref wave can regenerate a complete object wave with additional noise

$\Rightarrow$ Possible model for **biological memory**.
