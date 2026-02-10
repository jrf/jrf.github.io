---
title: "Physical Optics Homework"
---

# EE5621 Homework Explanations

This document provides detailed explanations for homework problems from EE5621: Physical Optics, based on Goodman's *Introduction to Fourier Optics*.

---

# Homework 1: Fourier Analysis Foundations

## What is the Fourier Transform?

The **[Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)** is a **map** that takes a function in one domain and produces a function in another domain:



$$
\mathcal{F}: f(x) \mapsto F(\nu)
$$



Concretely, the map is defined by this integral:



$$
F(\nu) = \int_{-\infty}^{\infty} f(x) \, e^{-j2\pi \nu x} \, dx
$$



| | Input | Output |
|---|-------|--------|
| **Forward transform** $\mathcal{F}$ | $f(x)$ — function of position/time | $F(\nu)$ — function of frequency |
| **Inverse transform** $\mathcal{F}^{-1}$ | $F(\nu)$ — function of frequency | $f(x)$ — function of position/time |

The two domains describe the **same underlying object** — just from different perspectives:

| Domain | What it shows | Axes |
|--------|---------------|------|
| **Spatial/Time** | Value at each location/moment | Position $x$ or time $t$ |
| **Frequency** | Amount of each sinusoidal component | Frequency $\nu$ or $f$ |

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>The core idea</div>
<div class="callout-content">

Any function can be written as a sum of sinusoids at different frequencies. The Fourier transform tells you **which frequencies are present** and **how much of each**.

The inverse transform reconstructs the original by adding up all the sinusoidal components:



$$
f(x) = \int_{-\infty}^{\infty} F(\nu) \, e^{+j2\pi \nu x} \, d\nu
$$



This is why the transform is **lossless** — no information is lost, just rearranged.

</div>
</div>

**Why do we care?**

1. **Simplifies [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)**: [Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) in the spatial domain becomes multiplication in the frequency domain. Filtering an image is just multiplying spectra.

2. **Reveals hidden structure**: Periodic patterns that are hard to see spatially become obvious peaks in the frequency domain.

3. **Connects to physics**: [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/), interference, and imaging are naturally described in terms of spatial frequencies. A lens performs an optical [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/).

4. **Enables efficient computation**: The Fast [Fourier Transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) (FFT) makes frequency analysis computationally practical.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Analogy: A musical chord</div>
<div class="callout-content">

A chord played on a piano is a complex pressure wave over time — hard to analyze directly. But the Fourier transform reveals discrete peaks at the frequencies of each note (e.g., 262 Hz, 330 Hz, 392 Hz for a C major chord). The frequency domain separates what the time domain mixes together.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Key properties to keep in mind</div>
<div class="callout-content">

- **Lossless**: The transform contains exactly the same information as the original — just rearranged
- **Invertible**: You can always get back to the original via the inverse transform
- **Linear**: The transform of a sum is the sum of the transforms
- **Reciprocal**: Wide in space → narrow in frequency (and vice versa)

</div>
</div>

<div class="callout callout-abstract">
<div class="callout-title"><span class="callout-icon">📄</span>Mathematical structure: The transform is a bijection</div>
<div class="callout-content">

On appropriate function spaces, $\mathcal{F}$ is a **bijection** (one-to-one and onto):

| Property | Meaning | Why it holds |
|----------|---------|--------------|
| **Injective** | Different functions → different transforms | Inverse exists: $\mathcal{F}\{f\} = \mathcal{F}\{g\} \Rightarrow f = g$ |
| **Surjective** | Every valid spectrum is a transform of something | Inverse produces that something |

On $L^2(\mathbb{R})$ (square-integrable functions), the Fourier transform is a **unitary isomorphism** — a bijection that also preserves inner products:



$$
\langle f, g \rangle = \langle \mathcal{F}\{f\}, \mathcal{F}\{g\} \rangle
$$



This is the **[Plancherel theorem](/notes/areas/mathematics/functional_analysis/definitions/plancherel_theorem/)**. It means the transform preserves "energy" (norms) and "similarity" (inner products) between functions — the two domains are not just equivalent in information, but equivalent in *structure*.

</div>
</div>

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Definitions</div>
<div class="callout-content">

**[Bijection](/notes/areas/mathematics/set_theory/definitions/bijection/)**: A function that is both injective and surjective — a perfect one-to-one pairing between two sets.

**[Injective](/notes/areas/mathematics/set_theory/definitions/injection/)** (one-to-one): $f(a) = f(b) \Rightarrow a = b$. No two inputs share the same output.

**[Surjective](/notes/areas/mathematics/set_theory/definitions/surjection/)** (onto): For every $y$ in the codomain, there exists an $x$ such that $f(x) = y$. Every output is reachable.

**[$L^2(\mathbb{R})$](/notes/areas/mathematics/functional_analysis/definitions/lp_space/)**: The space of square-integrable functions — functions where $\int |f(x)|^2 \, dx < \infty$. These are functions with finite "energy."

**[Inner product](/notes/areas/mathematics/functional_analysis/definitions/inner_product/)**: A generalization of the dot product to functions: $\langle f, g \rangle = \int f(x) \overline{g(x)} \, dx$. Measures "similarity" between functions.

**[Norm](/notes/areas/mathematics/functional_analysis/definitions/norm/)**: The "size" or "energy" of a function: $\|f\| = \sqrt{\langle f, f \rangle} = \sqrt{\int |f(x)|^2 \, dx}$.

**[Unitary](/notes/areas/mathematics/linear_algebra/definitions/unitary_operator/)**: A transformation that preserves inner products (and hence norms). Rotations are unitary; stretching is not.

**[Isomorphism](/notes/areas/mathematics/abstract_algebra/definitions/isomorphism/)**: A bijection that preserves structure. A unitary isomorphism preserves both the pairing (bijection) and the geometry (inner products).

</div>
</div>

---

## Fourier Transforms in Optical Imaging

In imaging, the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) maps from the **spatial domain** (brightness at each location) to the **spatial frequency domain** (how much of each grating pattern is present):



$$
\mathcal{F}: f(x, y) \mapsto F(\nu_x, \nu_y)
$$



### What Does the Frequency Domain Mean for an Image?

Each point $(\nu_x, \nu_y)$ in the frequency domain represents a specific 2D sinusoidal grating — stripes at a particular spacing and orientation. The value $F(\nu_x, \nu_y)$ tells you the amplitude and phase of that pattern in the image.

| Feature in image | Location in frequency domain |
|------------------|------------------------------|
| Uniform regions, slow gradients | Near origin (low $\nu_x$, $\nu_y$) |
| Edges, fine textures, sharp details | Far from origin (high $\nu_x$, $\nu_y$) |
| Vertical stripes/edges | Along the $\nu_x$ axis |
| Horizontal stripes/edges | Along the $\nu_y$ axis |
| Periodic textures (fabric, bricks) | Discrete peaks at the texture's frequency |

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Reading an image's spectrum</div>
<div class="callout-content">

A photograph of a picket fence would show:
- A bright region near the origin (overall brightness)
- Peaks along the $\nu_x$ axis at the fence's stripe frequency (vertical slats)
- Diffuse energy at high frequencies (wood grain, edges)

</div>
</div>

### Why Lenses Perform Fourier Transforms

This isn't just mathematical convenience — **light physically computes Fourier transforms** through [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/).

When coherent light passes through an object and then through a lens:

1. The object modulates the light's amplitude/phase at each point $(x, y)$
2. [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) causes each point to spread into waves traveling in all directions
3. The lens focuses waves traveling in the same direction to the same point
4. At the back focal plane, the light distribution is the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the object

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>The optical Fourier transform</div>
<div class="callout-content">

Place a transparency at the front focal plane of a lens. The light intensity at the back focal plane is $|F(\nu_x, \nu_y)|^2$ — the power spectrum of the transparency.

The spatial frequency $(\nu_x, \nu_y)$ maps to position in the focal plane:


$$
x' = \lambda f \nu_x, \quad y' = \lambda f \nu_y
$$


where $\lambda$ is wavelength and $f$ is focal length.

</div>
</div>

This is why Fourier optics is so powerful: the mathematics directly describes what light does. [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) *is* Fourier transformation.

### Filtering in the Frequency Domain

Since the frequency domain separates image features by their spatial scale, we can selectively modify them:

| Operation | Frequency domain action | Effect |
|-----------|------------------------|--------|
| **Blur** | Multiply by low-pass filter (attenuate high $\nu$) | Removes fine detail, smooths edges |
| **Sharpen** | Boost high frequencies | Enhances edges, amplifies noise |
| **Remove periodic noise** | Zero out specific frequency peaks | Eliminates repeating patterns |
| **Edge detection** | High-pass filter (attenuate low $\nu$) | Keeps only rapid variations |

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Optical filtering</div>
<div class="callout-content">

In an optical system, you can physically place a mask at the Fourier plane (back focal plane of the first lens). A second lens then performs the inverse transform, producing the filtered image.

- **Circular aperture** → low-pass filter → blurred image
- **Opaque dot at center** → high-pass filter → edge-enhanced image
- **Slit** → directional filter → enhances features in one orientation

</div>
</div>

### The Complete Imaging Pipeline

A coherent optical imaging system performs:



$$
\text{Object } f(x,y) \xrightarrow{\text{Lens 1}} \text{Spectrum } F(\nu_x, \nu_y) \xrightarrow{\times H(\nu_x,\nu_y)} \text{Filtered spectrum} \xrightarrow{\text{Lens 2}} \text{Image } g(x,y)
$$



where $H(\nu_x, \nu_y)$ is the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) of any filtering or apertures in the system.

This is why understanding Fourier transforms is essential for optics: every lens, aperture, and optical element can be understood as an operation in the frequency domain.

---

## Problem 1: Properties of Delta Functions (Goodman 2.1)

The **[Dirac delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/)** $\delta(x)$ is not a function in the traditional sense — it's a *distribution* or *generalized function*. It's defined by its behavior under integration:



$$
\int_{-\infty}^{\infty} f(x) \delta(x - x_0) \, dx = f(x_0)
$$



This is called the **sifting property**: the delta "picks out" the value of $f$ at the location of the spike.

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Key properties to remember</div>
<div class="callout-content">

- $\delta(x) = 0$ for $x \neq 0$
- $\int_{-\infty}^{\infty} \delta(x) \, dx = 1$
- It's infinitely tall and infinitely narrow, but with unit area

</div>
</div>

---

### Part (a): Scaling the 2D Delta Function



$$
\delta(ax, by) = \frac{1}{|ab|} \delta(x, y)
$$



**What this means:** When you "squeeze" the coordinates by factors $a$ and $b$, the delta function must compensate to maintain unit volume under the integral.

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Physical intuition</div>
<div class="callout-content">

Think of the delta as a very narrow, tall spike. If you compress the $x$-axis by a factor of $a$, the spike gets $|a|$ times narrower. To keep the total "mass" (integral) equal to 1, the spike must get $|a|$ times taller. The factor $1/|ab|$ accounts for compression in both dimensions.

</div>
</div>

**The derivation uses two facts:**

1. **1D scaling property:** $\delta(cx) = \frac{1}{|c|} \delta(x)$

2. **Separability:** The 2D delta is the product of two 1D deltas:
   

$$
\delta(x, y) = \delta(x) \cdot \delta(y)
$$



Combining these:


$$
\delta(ax, by) = \delta(ax) \cdot \delta(by) = \frac{1}{|a|}\delta(x) \cdot \frac{1}{|b|}\delta(y) = \frac{1}{|ab|}\delta(x,y)
$$



---

### Part (b): The Dirac Comb (Shah Function)



$$
\text{comb}(ax) \cdot \text{comb}(by) = \frac{1}{|ab|} \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} \delta\left(x - \frac{n}{a}, y - \frac{m}{b}\right)
$$



**What is the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/)?**

The [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) is an infinite train of equally-spaced [delta functions](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/):


$$
\text{comb}(x) = \sum_{n=-\infty}^{\infty} \delta(x - n)
$$



It's also called the **Shah function** (denoted Ш) because it looks like a row of spikes at every integer.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Why is this important?</div>
<div class="callout-content">

The [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) is fundamental to **[sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) theory**. Multiplying a continuous signal by a [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) gives you samples at regular intervals. This is how we mathematically model analog-to-digital conversion.

</div>
</div>

**The scaling effect:**

When you write $\text{comb}(ax)$, you're changing the spacing between spikes:
- If $a > 1$: spikes are closer together (spacing = $1/a$)
- If $a < 1$: spikes are farther apart (spacing = $1/a$)

The $1/|ab|$ factor in front compensates for the changed density of spikes to preserve normalization.

---

## Problem 2: Fourier Transform Relations (Goodman 2.2)

These problems establish fundamental transform pairs that appear repeatedly in optics and signal processing.

---

### Part (a): Rectangle to Sinc



$$
\mathcal{F}\{\text{rect}(x) \cdot \text{rect}(y)\} = \text{sinc}(f_X) \cdot \text{sinc}(f_Y)
$$



**The rectangle function:**


$$
\text{rect}(x) = \begin{cases} 1 & |x| < 1/2 \\ 0 & |x| > 1/2 \end{cases}
$$



It's a "top hat" or "boxcar" function — constant over a unit interval, zero elsewhere.

**The [sinc function](/notes/areas/electrical_engineering/signals_systems/definitions/sinc_function/):**


$$
\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}
$$



This oscillating function with decaying envelope is ubiquitous in signal processing.

**Why does rect transform to sinc?**

Computing the 1D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) directly:


$$
\mathcal{F}\{\text{rect}(x)\} = \int_{-1/2}^{1/2} e^{-j2\pi f_X x} \, dx = \frac{e^{-j\pi f_X} - e^{j\pi f_X}}{-j2\pi f_X} = \frac{\sin(\pi f_X)}{\pi f_X} = \text{sinc}(f_X)
$$



**The key concept: Separability**

When a 2D function can be written as $g(x,y) = g_1(x) \cdot g_2(y)$, its 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) factors:


$$
\mathcal{F}\{g_1(x) \cdot g_2(y)\} = G_1(f_X) \cdot G_2(f_Y)
$$



This dramatically simplifies 2D transform calculations — you can do two 1D transforms instead of one 2D integral.

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Physical interpretation in optics</div>
<div class="callout-content">

A rectangular aperture (like a slit) produces a sinc-shaped diffraction pattern. The rect-sinc transform pair is the mathematical foundation of **[Fraunhofer diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/fraunhofer_diffraction/)**.

</div>
</div>

---

### Part (b): Triangle to Sinc-Squared



$$
\mathcal{F}\{\Lambda(x) \cdot \Lambda(y)\} = \text{sinc}^2(f_X) \cdot \text{sinc}^2(f_Y)
$$



**The triangle function:**


$$
\Lambda(x) = \begin{cases} 1 - |x| & |x| < 1 \\ 0 & |x| \geq 1 \end{cases}
$$



It's a tent-shaped function that rises linearly from 0 to 1 and back down.

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>The key insight: Triangle = Rectangle ∗ Rectangle</div>
<div class="callout-content">

The triangle function is the **[convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/)** of a rectangle with itself:


$$
\Lambda(x) = \text{rect}(x) * \text{rect}(x)
$$


To see why: when you slide one rectangle past another and measure their overlap area, you get a triangle.

</div>
</div>

**Using the [Convolution Theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/):**

One of the most powerful results in Fourier analysis:


$$
\mathcal{F}\{f * g\} = F \cdot G
$$



[Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) in the spatial domain becomes multiplication in the frequency domain.

Therefore:


$$
\mathcal{F}\{\Lambda(x)\} = \mathcal{F}\{\text{rect} * \text{rect}\} = \text{sinc}(f_X) \cdot \text{sinc}(f_X) = \text{sinc}^2(f_X)
$$



**Physical interpretation:**

The sinc² intensity pattern (called the **[Airy pattern](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/)** for circular apertures) describes the [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern from many optical elements.

---

### Part (c): Constant to Delta



$$
\mathcal{F}\{1\} = \delta(f_X, f_Y)
$$



**What this means:**

A constant signal (same value everywhere in space) transforms to a single spike at the origin in frequency space.

**Physical intuition:**

- A constant has **no spatial variation** — it's completely "flat"
- The only frequency component is **zero frequency** (DC)
- Hence all the spectral energy is concentrated at $f_X = f_Y = 0$

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>The dual relationship</div>
<div class="callout-content">

By the inverse Fourier transform symmetry:


$$
\mathcal{F}\{\delta(x,y)\} = 1
$$


A point source (delta in space) contains **all frequencies equally** — it has a flat, constant spectrum.

This duality — constant ↔ delta — is fundamental to understanding both [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) and [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/).

</div>
</div>

---

## Problem 3: Fourier-Bessel Transform (Goodman 2.6)

The **[Fourier-Bessel transform](/notes/areas/electrical_engineering/physical_optics/definitions/hankel_transform/)** (also called the **[Hankel transform](/notes/areas/electrical_engineering/physical_optics/definitions/hankel_transform/)**) is the natural transform for functions with **circular symmetry**. Instead of complex exponentials, it uses [Bessel functions](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/) as its [basis](/notes/areas/mathematics/linear_algebra/definitions/basis/).

**Definition:**


$$
G(\rho) = 2\pi \int_0^{\infty} r \, g_R(r) \, J_0(2\pi r \rho) \, dr
$$



where:
- $r = \sqrt{x^2 + y^2}$ is the radial coordinate
- $\rho = \sqrt{f_X^2 + f_Y^2}$ is the radial frequency
- $J_0$ is the **zeroth-order [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/) of the first kind**

**Why Bessel functions?**

When you have circular symmetry and write the 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) in polar coordinates, the angular integration yields a [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/). It's the natural "building block" for radially symmetric functions, just as $e^{j\omega t}$ is for 1D signals.

---

### Part (a): Delta Ring



$$
\mathcal{B}\{\delta(r - r_0)\} = 2\pi r_0 J_0(2\pi r_0 \rho)
$$



**What is $\delta(r - r_0)$?**

This is a **delta ring** — all the "mass" concentrated on a circle of radius $r_0$. Imagine an infinitely thin, infinitely bright ring.

**The calculation:**

Substituting into the Fourier-Bessel definition:


$$
G(\rho) = 2\pi \int_0^{\infty} r \, \delta(r - r_0) \, J_0(2\pi r \rho) \, dr
$$



The sifting property picks out $r = r_0$:


$$
G(\rho) = 2\pi \cdot r_0 \cdot J_0(2\pi r_0 \rho)
$$



**Physical meaning:**

A ring source produces an oscillating [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern described by $J_0$. The spacing of the oscillations depends on the ring radius $r_0$.

---

### Part (b): Annular Region

For $g_R(r) = 1$ when $a \leq r \leq 1$ (and 0 otherwise):



$$
\mathcal{B}\{g_R(r)\} = \frac{J_1(2\pi\rho) - a J_1(2\pi a \rho)}{\rho}
$$



**What is this function?**

An **annulus** or "washer" — a disk with a hole in the center. It's 1 between radii $a$ and 1, and 0 elsewhere.

**The key Bessel identity:**

The solution uses the integration formula derived from:


$$
\frac{d}{dx}[x J_1(x)] = x J_0(x)
$$



This is analogous to how $\frac{d}{dx}[\sin x] = \cos x$ helps with trigonometric integrals.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Physical application</div>
<div class="callout-content">

Annular apertures are common in optics (e.g., reflecting telescopes with central obstructions). This transform tells you the resulting diffraction pattern.

</div>
</div>

---

### Part (c): Scaling Property



$$
\mathcal{B}\{g_R(ar)\} = \frac{1}{a^2} G\left(\frac{\rho}{a}\right)
$$



**The similarity theorem for radial functions:**

Compressing the spatial function by factor $a$ (making it smaller):
- Expands the frequency spectrum by factor $a$ (spreads it out)
- Reduces the amplitude by factor $1/a^2$

**Why $1/a^2$ instead of $1/a$?**

In 1D, the scaling factor is $1/|a|$. In 2D with circular symmetry, you're scaling in two dimensions, so it's $1/a^2$.

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Physical intuition</div>
<div class="callout-content">

A smaller aperture produces a wider diffraction pattern (and vice versa). This is the fundamental tradeoff between spatial resolution and frequency bandwidth.

</div>
</div>

---

### Part (d): Gaussian Eigenfunction



$$
\mathcal{B}\{e^{-\pi r^2}\} = e^{-\pi \rho^2}
$$



<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>The Gaussian is its own Fourier transform!</div>
<div class="callout-content">

The Gaussian function $e^{-\pi r^2}$ is an **eigenfunction** of the Fourier transform with eigenvalue 1. It transforms into itself.

Most functions look completely different after Fourier transformation. The Gaussian is special — it's perfectly balanced between spatial and frequency localization.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>The uncertainty principle connection</div>
<div class="callout-content">

The Gaussian achieves the theoretical minimum of the **[uncertainty principle](/notes/areas/electrical_engineering/physical_optics/definitions/uncertainty_principle/)**:


$$
\Delta x \cdot \Delta f \geq \frac{1}{4\pi}
$$


It's as localized as possible in *both* space and frequency simultaneously.

</div>
</div>

**Derivation sketch:**

1. The 2D Gaussian is separable: $e^{-\pi(x^2+y^2)} = e^{-\pi x^2} \cdot e^{-\pi y^2}$
2. For 1D: complete the square in the exponent of the Fourier integral
3. The resulting integral evaluates to another Gaussian
4. The 2D result follows by separability

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Physical significance</div>
<div class="callout-content">

[Gaussian beams](/notes/areas/electrical_engineering/physical_optics/definitions/gaussian_beam/) (like laser beams) maintain their Gaussian profile as they propagate and diffract — a consequence of this self-transform property.

</div>
</div>

---

## Problem 4: Bessel Functions as Eigenfunctions

**The claim:**

$J_0(2\pi\rho_0 r)$ is an [eigenfunction](/notes/areas/mathematics/linear_algebra/definitions/eigenfunction/) of any [linear shift-invariant](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/) (LSI) system with circularly symmetric [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/).

**What does this mean?**

When you input $J_0(2\pi\rho_0 r)$ to such a system, the output is the *same function* scaled by a constant:


$$
\text{output} = H(\rho_0) \cdot J_0(2\pi\rho_0 r)
$$



The function passes through unchanged in shape — only its amplitude is modified.

**Why is this true?**

The key insight connects to Problem 3(a):

1. From 3(a): $\mathcal{B}\{\delta(r-r_0)\} = 2\pi r_0 J_0(2\pi r_0 \rho)$

2. The Fourier-Bessel transform is **self-reciprocal** (symmetric), so:
   

$$
\mathcal{B}\{J_0(2\pi\rho_0 r)\} = \frac{1}{2\pi\rho_0}\delta(\rho - \rho_0)
$$



3. The [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/) transforms to a **delta ring in frequency space**

4. For an LSI system, output = input × [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) (in frequency domain):
   

$$
G_{\text{out}}(\rho) = H(\rho) \cdot \frac{1}{2\pi\rho_0}\delta(\rho - \rho_0) = \frac{H(\rho_0)}{2\pi\rho_0}\delta(\rho - \rho_0)
$$



5. Transforming back: the output is $H(\rho_0) \cdot J_0(2\pi\rho_0 r)$

**The [eigenvalue](/notes/areas/mathematics/linear_algebra/definitions/eigenvalue/):**



$$
\lambda = H(\rho_0) = \mathcal{B}\{h_R(r)\}\big|_{\rho = \rho_0}
$$



The [eigenvalue](/notes/areas/mathematics/linear_algebra/definitions/eigenvalue/) is the [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) evaluated at the spatial frequency $\rho_0$.

**Physical interpretation:**

Just as complex exponentials $e^{j2\pi fx}$ are eigenfunctions of 1D [LTI systems](/notes/areas/electrical_engineering/signals_systems/definitions/linear_shift-invariant_system/), Bessel functions are eigenfunctions of circularly symmetric 2D systems. They're the "natural modes" of such systems.

---

## Problem 5: The Fourier Transform as a System

This problem asks us to analyze the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) itself as if it were a signal processing system.

---

### Part (a): Is it Linear?

**Yes, the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) is linear.**

A system is linear if it satisfies **[superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/)**:


$$
\mathcal{F}\{a g_1 + b g_2\} = a \mathcal{F}\{g_1\} + b \mathcal{F}\{g_2\}
$$



**Proof:**

Starting from the definition:


$$
\mathcal{F}\{ag_1 + bg_2\} = \iint [ag_1(x,y) + bg_2(x,y)] e^{-j2\pi(f_X x + f_Y y)} \, dx\,dy
$$



By linearity of integration:


$$
= a \iint g_1 e^{-j2\pi(f_X x + f_Y y)} dx\,dy + b \iint g_2 e^{-j2\pi(f_X x + f_Y y)} dx\,dy
$$




$$
= a\mathcal{F}\{g_1\} + b\mathcal{F}\{g_2\}
$$



---

### Part (b): Does it Have a Transfer Function?

**No, the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) system does not have a [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/).**

**Why not?**

A [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) exists only for systems that are both:
1. Linear ✓ (proven above)
2. Shift-[invariant](/notes/areas/mathematics/abstract_algebra/definitions/invariant/) ✗

<div class="callout callout-warning">
<div class="callout-title"><span class="callout-icon">⚠️</span>The Fourier transform is NOT shift-invariant</div>
<div class="callout-content">

For shift-invariance, shifting the input should shift the output by the same amount:


$$
g(x - x_0) \rightarrow G(f_X - f_{X,0}) \quad \text{(would be shift-invariant)}
$$



But the **shift theorem** tells us what actually happens:


$$
\mathcal{F}\{g(x - x_0)\} = G(f_X) \cdot e^{-j2\pi x_0 f_X}
$$



A shift in the spatial domain produces a **phase modulation** in the frequency domain, not a shift!

</div>
</div>

**Physical intuition:**

The [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) converts between fundamentally different representations (space ↔ frequency). A translation in one domain can't map to a translation in the other because they represent different physical quantities.

**Consequence:**

Without shift-invariance, there's no [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) relationship, and thus no [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/) or [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/). Each input must be analyzed directly through the transform integral.

---

## Homework 1 Summary

| Problem | Core Concept |
|---------|--------------|
| 1 | [Delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) scaling and the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) for [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) |
| 2 | Fundamental transform pairs: rect↔sinc, separability |
| 3 | [Fourier-Bessel transform](/notes/areas/electrical_engineering/physical_optics/definitions/hankel_transform/) for circular symmetry |
| 4 | Bessel functions as eigenfunctions of radially symmetric systems |
| 5 | Linearity vs. shift-invariance; when transfer functions exist |

---

# Homework 2: Computed Tomography and the Projection-Slice Theorem

## Problem 1: X-ray Projections and the Projection-Slice Theorem

> Consider the three-dimensional object shown in the figure below. A two-dimensional slice of this object is illuminated with a line source of x-rays, and a linear detector array is placed behind the object. The x-rays are attenuated by the material in the path of the beam; the denser the material, the less intense the beam. Assume the signal produced at a single detector in the array is equal to the integral of the density along the beam direction.
>
> ![Problem 1 figure](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/pr1.png)

This problem introduces the mathematical foundation of **[Computed Tomography](/notes/areas/electrical_engineering/physical_optics/definitions/computed_tomography/) (CT) imaging**.

---

## The Physical Setup

Imagine a 3D object (like a human body). We take a 2D cross-sectional slice at some height $z_0$. This slice has a density distribution $f(x, y)$ — different tissues (bone, muscle, air) have different densities.

**The x-ray imaging process:**

1. A line source emits parallel x-ray beams along the $x$-direction
2. The beams pass through the object and are **attenuated** (weakened) by the material
3. Denser material absorbs more x-rays → weaker signal reaches the detector
4. A linear detector array on the other side measures what comes through

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Key assumption</div>
<div class="callout-content">

The detector signal equals the **line integral** of density along the beam path. This is the [Beer-Lambert law](/notes/areas/electrical_engineering/physical_optics/definitions/beer_lambert_law/) in action — attenuation accumulates as the beam travels through material.

</div>
</div>

**What is $f(x, y)$?**

$f(x, y)$ is the **density distribution of the cross-sectional slice** — it's what's actually inside the object at each point $(x, y)$. Different tissues have different densities (bone is dense, muscle is medium, air is sparse). The function $f(x, y)$ assigns a density value to every point in the slice. **It's the unknown we want to reconstruct.**

| Symbol | What it is | Known or unknown? |
|--------|------------|-------------------|
| $f(x,y)$ | Internal density at point $(x,y)$ | **Unknown** — can't see inside |
| $p(y)$ | Detector signal at position $y$ | **Measured** — from part (a) |

We [measure](/notes/areas/mathematics/measure_theory/definitions/measure/) $p(y)$. We want $f(x,y)$. The [projection-slice theorem](/notes/areas/electrical_engineering/physical_optics/definitions/projection_slice_theorem/) tells us how to invert this relationship.

---

## Part (a): What does a single projection measure?

> What is the one-dimensional signal received by the detector array for an object cross-section $f(x, y)$ located at $z_0$ when the beam is projected along the $x$-axis as in the figure? Assume the array is a continuous function of $y$.

Consider one detector element sitting at position $y$ on the detector array. The x-ray beam traveling to this detector passes through all points $(x, y)$ for $x \in (-\infty, \infty)$ at that fixed $y$ value.

![X-ray projection diagram](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/projection_diagram.svg)

The signal received is the sum (integral) of all the density values along that line:



$$
p(y) = \int_{-\infty}^{\infty} f(x, y) \, dx
$$



**Interpretation:**
- For each $y$ position, we're "collapsing" all the information along the $x$-direction into a single number
- The result $p(y)$ is a 1D function — it's the **projection** or **shadow** of the 2D object onto the $y$-axis
- This operation is called the **[Radon transform](/notes/areas/electrical_engineering/physical_optics/definitions/radon_transform/)**

**Example:** If there's a dense bone at some $(x_0, y_0)$, the projection $p(y_0)$ will have a higher value than if there were only soft tissue along that line.

**Note on continuous vs. discrete detectors:**

In the mathematical model, the detector is **continuous** — infinitely many beams with infinitesimal spacing. The problem even says "Assume the array is a continuous function of $y$."

In a real CT scanner, detector elements are discrete (maybe 1000+ elements across), so there's finite spacing. This introduces [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) considerations, but the theory treats it as continuous.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Sampling considerations in practice</div>
<div class="callout-content">

1. **[Nyquist sampling](/notes/areas/electrical_engineering/physical_optics/definitions/nyquist_criterion/) / Aliasing** — To faithfully capture a signal, you must sample at least twice per cycle of the highest frequency present. If detectors are spaced too far apart, fine details "fold back" and masquerade as lower frequencies (aliasing), showing up as false patterns or streaks.

2. **Resolution limit** — Detector spacing sets a hard limit on the finest detail you can resolve. If detectors are 0.5mm apart, you can't distinguish features smaller than ~0.5mm.

3. **Number of projection angles** — Similar sampling logic applies to how many angles you need. Too few angles → streak artifacts radiating from sharp edges. Rule of thumb: you need roughly as many projection angles as detector elements.

4. **Interpolation** — The projection-slice theorem fills in radial lines in Fourier space, but the inverse FFT needs data on a Cartesian grid. Interpolating from radial to Cartesian introduces small errors.

</div>
</div>

---

## Spatial vs. Frequency Domain: The Interplay

Before diving into the theorem, it helps to understand the relationship between spatial and frequency representations.

**Spatial domain** — the "normal" view of an image or signal. Each point $(x, y)$ has a value $f(x, y)$ representing intensity, density, etc. This is what you see when you look at a photograph.

**Frequency domain** — a completely different representation of the *same* information. Each point $(\nu_x, \nu_y)$ tells you the amplitude and phase of a sinusoidal wave at that frequency.

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Key insight</div>
<div class="callout-content">

These two representations contain *identical* information. The [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) is a lossless, reversible mapping between them.

</div>
</div>

| Spatial Domain | Frequency Domain |
|----------------|------------------|
| Position $(x, y)$ | Frequency $(\nu_x, \nu_y)$ |
| Sharp edges, fine details | High frequencies (far from origin) |
| Smooth regions, gradual changes | Low frequencies (near origin) |
| Localized features | Spread across many frequencies |
| Periodic patterns | Concentrated at specific frequencies |

**Intuitive examples:**

1. **A sharp edge** (like a boundary between black and white) requires many high-frequency sinusoids to represent — that's why edges appear as energy far from the origin in the frequency domain.

2. **A smooth gradient** only needs low frequencies — the energy stays near the origin.

3. **A periodic grating** (stripes) appears as two bright dots in the frequency domain at $\pm$ the stripe frequency.

**Why this matters for CT:**

The projection-slice theorem exploits this duality. Instead of measuring $f(x,y)$ directly (which we can't do — we can't see inside the body), we [measure](/notes/areas/mathematics/measure_theory/definitions/measure/) projections $p(y)$. Each projection gives us a *slice* of $F(\nu_x, \nu_y)$. Collect enough slices → reconstruct the full frequency domain → inverse transform → recover the spatial image.

---

## Part (b): The Projection-Slice Theorem

> How is the one-dimensional Fourier transform of this distribution related to the two-dimensional Fourier transform of the cross-section $f(x,y)$? (Hint: Consider the two-dimensional Fourier transform along a particular line). This relationship is called the projection-slice theorem.

This is the **key insight** that makes CT reconstruction possible.

**Question:** How does the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the projection $p(y)$ relate to the 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of $f(x,y)$?

**The 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the object:**


$$
F(\nu_x, \nu_y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, e^{-j2\pi(\nu_x x + \nu_y y)} \, dx \, dy
$$



Breaking this down:

- $f(x, y)$ — the original 2D image/object (spatial domain)
- $F(\nu_x, \nu_y)$ — the transformed result (frequency domain)
- $\nu_x, \nu_y$ — spatial frequencies (cycles per unit length in x and y directions)
- $e^{-j2\pi(\nu_x x + \nu_y y)}$ — a 2D sinusoidal wave (explained below)

The double integral multiplies the image by each possible 2D wave and integrates over all space, measuring "how much" of that frequency is present. Think of it as decomposing the image into a sum of 2D sinusoidal gratings at different orientations and spacings.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>What does "cycles per unit length" mean?</div>
<div class="callout-content">

**Temporal frequency** (familiar from audio/radio) measures oscillations per unit *time*. The wave $\cos(2\pi f t)$ oscillates $f$ times per second as time $t$ progresses.

| Temporal frequency | Meaning | Example |
|-------------------|---------|---------|
| 440 Hz | 440 cycles/second | Concert A note |
| 60 Hz | 60 cycles/second | US power line hum |
| 2.4 GHz | 2.4 billion cycles/second | WiFi signal |

**Spatial frequency** is the same idea, but for *space* instead of time. The wave $\cos(2\pi \nu_x x)$ oscillates $\nu_x$ times per unit length as you move in $x$.

| Spatial frequency | Wavelength | What it looks like |
|-------------------|------------|-------------------|
| 1 cycle/cm | 1 cm | Wide stripes, 1 cm apart |
| 5 cycles/cm | 0.2 cm (2 mm) | Fine stripes, 2 mm apart |
| 10 cycles/cm | 0.1 cm (1 mm) | Very fine stripes, 1 mm apart |

**The temporal ↔ spatial analogy:**

| Temporal (time domain) | Spatial (space domain) |
|------------------------|------------------------|
| Time $t$ (seconds) | Position $x$ (meters) |
| Frequency $f$ (Hz = cycles/sec) | Spatial frequency $\nu_x$ (cycles/m) |
| Period $T = 1/f$ (seconds) | Wavelength $\lambda = 1/\nu_x$ (meters) |
| Higher $f$ = faster oscillation | Higher $\nu_x$ = finer detail |

The "unit" depends on your coordinate system. If $x$ is in meters, then $\nu_x$ is in cycles/meter. If $x$ is in millimeters, then $\nu_x$ is in cycles/mm.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Frequency domain: temporal vs. spatial</div>
<div class="callout-content">

The "frequency domain" is always the dual representation showing which sinusoidal building blocks make up your signal.

**Temporal (1D signals like audio):**



$$
F(f) = \int_{-\infty}^{\infty} f(t) \, e^{-j2\pi f t} \, dt
$$



| Time domain | Frequency domain |
|-------------|------------------|
| Signal $f(t)$ | Spectrum $F(f)$ |
| Horizontal axis: time (seconds) | Horizontal axis: frequency (Hz) |
| Shows amplitude at each moment | Shows amplitude at each frequency |

*Example:* A musical chord is complex in time, but in the frequency domain you see distinct peaks at each note's frequency.

**Spatial (2D images):**



$$
F(\nu_x, \nu_y) = \iint f(x,y) \, e^{-j2\pi(\nu_x x + \nu_y y)} \, dx\, dy
$$



| Spatial domain | Frequency domain |
|----------------|------------------|
| Image $f(x, y)$ | Spectrum $F(\nu_x, \nu_y)$ |
| Axes: position (meters) | Axes: spatial frequency (cycles/m) |
| Shows brightness at each location | Shows amplitude at each spatial frequency |

*Example:* A peak at $(\nu_x, \nu_y) = (5, 0)$ means "the image contains vertical stripes at 5 cycles/unit."

</div>
</div>

<div class="callout callout-question">
<div class="callout-title"><span class="callout-icon">❓</span>What is the Fourier transform actually computing?</div>
<div class="callout-content">

At each point $(\nu_x, \nu_y)$, the transform asks: *"How much of the sinusoidal wave with this specific frequency and orientation is present in the image?"*

The integral computes the **correlation** between your image $f(x,y)$ and a specific 2D sinusoidal wave. If the image contains that frequency component, the result is large; if not, it's small.

**How to read the frequency domain:**

| Location in $(\nu_x, \nu_y)$ plane | What it measures |
|-----------------------------------|------------------|
| Origin $(0, 0)$ | DC component — the average brightness |
| Along $\nu_x$ axis ($\nu_y = 0$) | Vertical stripe content at various spacings |
| Along $\nu_y$ axis ($\nu_x = 0$) | Horizontal stripe content at various spacings |
| Far from origin | Fine detail (rapid spatial variation) |
| Near origin | Coarse structure (slow spatial variation) |

**Example:** If your image contains vertical stripes spaced 1 cm apart, there will be a peak at $\nu_x = 1$ cycle/cm, $\nu_y = 0$. The transform "found" that frequency component.

**The inverse transform reconstructs the image:**


$$
f(x,y) = \iint F(\nu_x, \nu_y) \, e^{+j2\pi(\nu_x x + \nu_y y)} \, d\nu_x\, d\nu_y
$$


This says: "Add up all the sinusoidal waves, weighted by how much of each is present." The image is literally a sum of 2D gratings at different frequencies and orientations.

</div>
</div>

**Understanding the exponential term $e^{-j2\pi(\nu_x x + \nu_y y)}$:**

| Piece | What it is |
|-------|------------|
| $e$ | Euler's number (≈ 2.718) |
| $j$ | Imaginary unit ($j = \sqrt{-1}$) |
| $2\pi$ | Converts from "cycles" to "radians" (one cycle = $2\pi$ radians) |
| $\nu_x, \nu_y$ | Spatial frequencies — cycles per unit length in each direction |
| $\nu_x x + \nu_y y$ | Total phase at position $(x, y)$ — a dot product |

Using [Euler's formula](/notes/areas/mathematics/complex_analysis/definitions/eulers_formula/): $e^{-j\theta} = \cos(\theta) - j\sin(\theta)$

This is a **2D sinusoidal wave** oscillating in the direction $(\nu_x, \nu_y)$. The wave is constant along lines where $\nu_x x + \nu_y y = \text{constant}$ and oscillates perpendicular to them. Why complex? Using $e^{j\theta}$ captures both amplitude and phase in one number, making the math cleaner.

| $\nu_x$ | $\nu_y$ | Pattern |
|---------|---------|---------|
| High | 0 | Vertical stripes |
| 0 | High | Horizontal stripes |
| High | High | Diagonal fine pattern |
| Low | Low | Slowly varying, smooth |

**Why do different frequencies produce different patterns?**

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Geometric Intuition</div>
<div class="callout-content">

The equation $\nu_x x + \nu_y y = \text{constant}$ defines a straight line in the $(x, y)$ plane. The wave is constant along these lines and oscillates perpendicular to them.

</div>
</div>

- **When $\nu_y = 0$:** The phase becomes $\nu_x x$, which only depends on $x$. Lines of constant phase are vertical lines ($x = \text{const}$). The wave oscillates as you move horizontally (in $x$), creating **vertical stripes**.

- **When $\nu_x = 0$:** The phase becomes $\nu_y y$, which only depends on $y$. Lines of constant phase are horizontal lines ($y = \text{const}$). The wave oscillates as you move vertically (in $y$), creating **horizontal stripes**.

- **When both are nonzero:** Lines of constant phase are tilted at angle $\theta = \arctan(\nu_x / \nu_y)$ from horizontal. The wave oscillates perpendicular to this direction. If $\nu_x = \nu_y$, the lines are at 45°, and you get **diagonal stripes**. When both frequencies are high, the stripes are closely spaced.

- **Low frequencies:** Large wavelengths mean slow spatial variation — the pattern changes gradually across space, appearing smooth or like a gentle gradient.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Walking through a wave field</div>
<div class="callout-content">

Imagine standing in a field of vertical stripes ($\nu_y = 0$). If you walk horizontally, you pass through bright-dark-bright cycles. But if you walk vertically, the intensity doesn't change — you're moving along a line of constant phase.

</div>
</div>

<div class="callout callout-info">
<div class="callout-title"><span class="callout-icon">ℹ️</span>Two parameters control the pattern</div>
<div class="callout-content">

- **Magnitude** $\sqrt{\nu_x^2 + \nu_y^2}$ determines the spacing: higher = finer features
- **Ratio** $\nu_y / \nu_x$ determines the orientation of the stripes

</div>
</div>

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Animated visualization: Direction of oscillation</div>
<div class="callout-content">

Watch how each pattern oscillates in the direction perpendicular to its stripes:

![Spatial frequency animation](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/spatial_frequency_animation.svg)

**Key insight:** The wave is constant along lines where $\nu_x x + \nu_y y = \text{constant}$. These lines run parallel to the stripes. The wave oscillates perpendicular to them.

| Condition | Stripes | Oscillation |
|-----------|---------|-------------|
| $\nu_y = 0$ | Vertical | Horizontal |
| $\nu_x = 0$ | Horizontal | Vertical |
| Both $\neq 0$ | Diagonal | Diagonal |

**Why do the stripes look "blurry"?** The patterns show sinusoidal waves, not sharp stripes. A pure sinusoid like $\cos(2\pi \nu_x x)$ varies smoothly. Sharp-edged stripes (a square wave) would contain multiple frequencies — the smooth gradient correctly represents a *single* spatial frequency.

</div>
</div>


**The 1D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the projection:**


$$
P(\nu_y) = \int_{-\infty}^{\infty} p(y) \, e^{-j2\pi \nu_y y} \, dy
$$



Breaking this down:

- $p(y)$ — the 1D projection signal from the detector array
- $P(\nu_y)$ — the transformed result (frequency domain)
- $\nu_y$ — spatial frequency along the $y$-direction (how many cycles per unit length as you move in $y$; e.g., $\nu_y = 5$ cycles/cm means 5 oscillations per cm, wavelength = 0.2 cm)
- $e^{-j2\pi \nu_y y}$ — a 1D sinusoidal wave at frequency $\nu_y$

This integral decomposes the projection into its frequency components — how much of each sinusoidal frequency is present in the 1D signal.

**Derivation:** Substitute $p(y) = \int f(x,y) \, dx$ into the 1D transform:



$$
P(\nu_y) = \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} f(x, y) \, dx \right] e^{-j2\pi \nu_y y} \, dy
$$



Since $e^{-j2\pi \nu_y y}$ doesn't depend on $x$, we can pull it inside the inner integral (constants pass through integrals). This gives us a single double integral:



$$
P(\nu_y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, e^{-j2\pi \nu_y y} \, dx \, dy
$$



<div class="callout callout-question">
<div class="callout-title"><span class="callout-icon">❓</span>Why $\nu_x = 0$?</div>
<div class="callout-content">

We don't *choose* this — it's a consequence of the projection. When we integrate $f(x,y)$ along $x$, we sum over all $x$ values, destroying all information about how $f$ varies in $x$. Variations in $x$ correspond to non-zero $\nu_x$ frequencies, but integrating over $x$ averages out all those oscillations — they cancel to zero. Only the $\nu_x = 0$ component survives.

By collapsing the $x$ dimension, we lose access to any $\nu_x \neq 0$ information. That's why we only get a *slice* of the 2D Fourier transform, not the whole thing — and why you need multiple projection angles.

</div>
</div>

**Where does "$0 \cdot x$" come from?** Compare this to the 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):



$$
F(\nu_x, \nu_y) = \int \int f(x,y) \, e^{-j2\pi(\nu_x x + \nu_y y)} \, dx \, dy
$$



If we set $\nu_x = 0$, we get $e^{-j2\pi(0 \cdot x + \nu_y y)} = e^{-j2\pi \nu_y y}$ — exactly what we have! So we write the "$0 \cdot x$" to make the pattern match obvious:



$$
P(\nu_y) = \int \int f(x, y) \, e^{-j2\pi(0 \cdot x + \nu_y \cdot y)} \, dx \, dy = F(0, \nu_y)
$$



Notice that this is exactly $F(\nu_x, \nu_y)$ evaluated at $\nu_x = 0$:



$$
\boxed{P(\nu_y) = F(0, \nu_y)}
$$



<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>The Projection-Slice Theorem</div>
<div class="callout-content">

The 1D Fourier transform of a projection equals a 1D "slice" through the 2D Fourier transform of the object, passing through the origin, perpendicular to the projection direction.

— [Projection-Slice Theorem](/notes/areas/electrical_engineering/physical_optics/definitions/projection_slice_theorem/)

</div>
</div>

**Visually:**
- The object $f(x,y)$ lives in the spatial domain (x-y plane)
- Its 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) $F(\nu_x, \nu_y)$ lives in the frequency domain ($\nu_x$-$\nu_y$ plane)
- A projection along $x$ gives you the **vertical line** $\nu_x = 0$ in the frequency domain

---

## Part (c): Reconstructing the Full Image

> Locate the region of the Fourier transform plane $\mathcal{F}\{f(x, y)\}$ which can be recovered from projecting a line of x-rays down the x-axis from part (b). What region can be recovered from a $y$-axis projection? Can you describe a technique for recovering the entire cross-sectional image $f(x,y)$ from many projections? If you can, you have just invented a method of computer tomography.

**What do we get from each projection?**

| Projection Direction | Spatial Result | Frequency Slice |
|---------------------|----------------|-----------------|
| Along $x$-axis | $p(y) = \int f \, dx$ | Vertical line: $F(0, \nu_y)$ |
| Along $y$-axis | $q(x) = \int f \, dy$ | Horizontal line: $F(\nu_x, 0)$ |
| At angle $\theta$ | projection at angle $\theta$ | Radial line at angle $\theta$ through origin |

**Connection to spatial frequency patterns:**

A projection "sees" variations **perpendicular** to its direction, but is blind to variations **parallel** to it:

| Pattern | Dominant frequencies | Captured by $x$-projection? | Captured by $y$-projection? |
|---------|---------------------|----------------------------|----------------------------|
| Vertical stripes | High $\nu_x$, low $\nu_y$ | No (need $\nu_x \neq 0$) | Yes |
| Horizontal stripes | Low $\nu_x$, high $\nu_y$ | Yes | No (need $\nu_y \neq 0$) |
| Diagonal/checkerboard | High $\nu_x$ and $\nu_y$ | Partially | Partially |
| Smooth gradient | Low both | Yes | Yes |

This is why you need projections from many angles — each one captures a different slice of the frequency content.

**The reconstruction idea:**

With just two projections (along $x$ and $y$), you only know two lines in the Fourier domain — that's not enough to reconstruct the image.

But if you take **many projections at different angles** $\theta \in [0, \pi)$:

1. Each projection gives you one radial "spoke" through the origin in the Fourier domain
2. With enough projections, you fill in the entire 2D Fourier plane
3. Apply the **inverse 2D Fourier transform** to recover $f(x,y)$

**This is [Computed Tomography](/notes/areas/electrical_engineering/physical_optics/definitions/computed_tomography/)!**

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Practical considerations</div>
<div class="callout-content">

- The radial sampling is dense near the origin but sparse far from it
- This non-uniform sampling requires compensation → the **ramp filter** (high-pass filter that boosts high frequencies)
- The algorithm used clinically is **[filtered back-projection](/notes/areas/electrical_engineering/physical_optics/definitions/filtered_back_projection/)**: filter each projection, then "smear" it back across the image at its original angle, accumulating contributions from all angles

</div>
</div>

---

## Problem 2: Equivalent Area and Equivalent Bandwidth (Goodman 2.5)

> The "equivalent area" $\Delta_{xy}$ of a function $g(x, y)$ can be defined by
>
> 

$$
\Delta_{xy} = \frac{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \, dx \, dy}{g(0, 0)},
$$


>
> while the "equivalent bandwidth" $\Delta_{f_x f_y}$ of $g$ is defined in terms of its transform $G$ by
>
> 

$$
\Delta_{f_x f_y} = \frac{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} G(f_x, f_y) \, df_x \, df_y}{G(0, 0)}.
$$


>
> Show that $\Delta_{xy} \cdot \Delta_{f_x f_y} = 1$.

This problem reveals a beautiful reciprocal relationship between a function's spatial extent and its frequency content — a manifestation of the [uncertainty principle](/notes/areas/electrical_engineering/physical_optics/definitions/uncertainty_principle/).

---

### The Definitions

**Equivalent area** of a function $g(x, y)$:



$$
\Delta_{xy} = \frac{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \, dx \, dy}{g(0, 0)}
$$



**Equivalent bandwidth** of its [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) $G(f_x, f_y)$:



$$
\Delta_{f_x f_y} = \frac{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} G(f_x, f_y) \, df_x \, df_y}{G(0, 0)}
$$



**Notation convention:** Lowercase $g$ denotes the spatial domain function; uppercase $G$ denotes its [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) (frequency domain). This is standard: the transform of $g$ is $G$, the transform of $f$ is $F$, etc.

---

### What Do These Quantities Mean?

**Equivalent area** $\Delta_{xy}$:
- The numerator is the total "volume" under the function $g(x,y)$
- Dividing by $g(0,0)$ (the value at the origin) converts volume → area:
  - Think of $g(x,y)$ as a height above the $(x,y)$ plane
  - $\int \int g \, dx\,dy$ = volume under the surface $z = g(x,y)$
  - $g(0,0)$ = height at the origin
  - Dividing: volume / height = area

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Clarification on integrals</div>
<div class="callout-content">

*What you integrate over* (the domain):
- Single integral: over a line (1D)
- Double integral: over a surface (2D)
- Triple integral: over a volume (3D)

*What the result represents* (depends on the integrand):
- $\int \int 1 \, dx\,dy$ = area of the region
- $\int \int g(x,y) \, dx\,dy$ = volume under the surface $z = g(x,y)$
- $\int \int \int 1 \, dx\,dy\,dz$ = volume of the region
- $\int \int \int \rho(x,y,z) \, dx\,dy\,dz$ = mass (if $\rho$ is density)

A double integral integrates *over* a 2D region, but when the integrand is a "height" function, the result is a 3D volume.

</div>
</div>
- Result: the area of a rectangle with height $g(0,0)$ that has the same volume as $g$
- **Intuition**: How "spread out" is the function in space?
- **Note**: This definition assumes $g$ is centered at the origin. For symmetric functions like Gaussians, the origin is also the peak — but that's not guaranteed in general.

**Equivalent bandwidth** $\Delta_{f_x f_y}$:
- Same idea, but for the spectrum $G(f_x, f_y)$
- **Intuition**: How "spread out" is the function in frequency?

| Quantity | Domain | Measures |
|----------|--------|----------|
| $\Delta_{xy}$ | Spatial | Effective spatial extent |
| $\Delta_{f_x f_y}$ | Frequency | Effective frequency extent |

**Geometric interpretation:**

![Equivalent width diagram](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/equivalent_width_diagram.svg)

The equivalent width $\Delta_x$ (or area $\Delta_{xy}$ in 2D) answers the question: *What size rectangle, with height equal to the peak value, has the same area/volume as the original function?*

---

### The Proof

**Goal:** Show that $\Delta_{xy} \cdot \Delta_{f_x f_y} = 1$

**Step 1: Use the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) at the origin**

Look at the definition of $\Delta_{xy}$:



$$
\Delta_{xy} = \frac{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x,y) \, dx \, dy}{g(0,0)}
$$



The numerator is the integral of $g$ over all space. We need to relate this to the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) $G$. The question is: *does this integral appear anywhere in the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)?*

Start with the definition of the 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):



$$
G(f_x, f_y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \, e^{-j2\pi(f_x x + f_y y)} \, dx \, dy
$$



The trick is to evaluate this at the origin of the frequency domain ($f_x = 0$, $f_y = 0$), because this makes the exponential disappear:



$$
G(0, 0) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \, e^{-j2\pi(0 \cdot x + 0 \cdot y)} \, dx \, dy
$$



The exponent becomes zero:


$$
e^{-j2\pi(0 \cdot x + 0 \cdot y)} = e^{0} = 1
$$



So the exponential simply disappears, leaving:



$$
G(0, 0) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \, dx \, dy
$$



This is exactly the numerator of $\Delta_{xy}$! So we can write:



$$
\Delta_{xy} = \frac{G(0,0)}{g(0,0)}
$$



**Physical meaning:** The value of the spectrum at zero frequency (the "[DC component](/notes/areas/electrical_engineering/signals_systems/definitions/dc_component/)") equals the total integral of the function over all space. This makes intuitive sense: the zero-frequency component represents the average or total "mass" of the signal, with no oscillation.

**Step 2: Use the inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) at the origin**

Now look at the definition of $\Delta_{f_x f_y}$:



$$
\Delta_{f_x f_y} = \frac{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} G(f_x, f_y) \, df_x \, df_y}{G(0,0)}
$$



The numerator is the integral of $G$ over all frequencies. We need to relate this to the spatial function $g$. The question is: *does this integral appear anywhere in the inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/)?*

Start with the definition of the inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):



$$
g(x, y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} G(f_x, f_y) \, e^{j2\pi(f_x x + f_y y)} \, df_x \, df_y
$$



The trick is to evaluate this at the origin of the spatial domain ($x = 0$, $y = 0$), because this makes the exponential disappear:



$$
g(0, 0) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} G(f_x, f_y) \, e^{j2\pi(0 \cdot f_x + 0 \cdot f_y)} \, df_x \, df_y
$$



The exponent becomes zero:


$$
e^{j2\pi(0 \cdot f_x + 0 \cdot f_y)} = e^{0} = 1
$$



So the exponential simply disappears, leaving:



$$
g(0, 0) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} G(f_x, f_y) \, df_x \, df_y
$$



This is exactly the numerator of $\Delta_{f_x f_y}$! So we can write:



$$
\Delta_{f_x f_y} = \frac{g(0,0)}{G(0,0)}
$$



**Physical meaning:** The value of the spatial function at the origin equals the total integral of the spectrum over all frequencies. This is the "dual" of Step 1 — the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) and its inverse have symmetric properties.

**Step 3: Substitute into the definitions**

From Step 1:


$$
\Delta_{xy} = \frac{\int \int g(x,y) \, dx \, dy}{g(0,0)} = \frac{G(0,0)}{g(0,0)}
$$



From Step 2:


$$
\Delta_{f_x f_y} = \frac{\int \int G(f_x, f_y) \, df_x \, df_y}{G(0,0)} = \frac{g(0,0)}{G(0,0)}
$$



**Step 4: Multiply**



$$
\Delta_{xy} \cdot \Delta_{f_x f_y} = \frac{G(0,0)}{g(0,0)} \cdot \frac{g(0,0)}{G(0,0)} = 1
$$





$$
\boxed{\Delta_{xy} \cdot \Delta_{f_x f_y} = 1}
$$



---

### Physical Interpretation

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Uncertainty Principle for Fourier Pairs</div>
<div class="callout-content">

A function cannot be simultaneously compact in both space and frequency.

**What does "compact" mean here?** Not the topological definition (closed and bounded). Here "compact" is used informally to mean *localized* — most of the function's energy is concentrated in a small region. A narrow spike is localized; a broad, spread-out hump is not.

**Why can't a function be compact in both domains?** The Fourier transform decomposes a function into sinusoidal waves. Consider what it takes to build different shapes:

- **To build a narrow spike** (localized in space), you need waves of *many* different frequencies. A single sinusoid extends forever — it oscillates from $-\infty$ to $+\infty$. To get waves to cancel everywhere *except* at one spot, you need contributions from all frequencies, carefully tuned to destructively interfere everywhere else. More frequencies → wider spread in the frequency domain.

- **To build a pure sinusoid** (localized in frequency), the wave must extend forever in space. A sinusoid that stops abruptly isn't a pure frequency anymore — the sharp cutoff introduces new frequency components (this is why truncating a signal causes spectral leakage).

**Intuitive analogy:** A short "click" sound contains all frequencies — it's a burst of white noise. A sustained pure tone (like a tuning fork) has a narrow frequency spectrum but lasts a long time. You can't have a sound that's both instantaneous *and* a pure pitch.

**The mathematical reason:** We just proved that $\Delta_{xy} \cdot \Delta_{f_x f_y} = 1$. If you shrink one factor, the other must grow. This isn't a measurement limitation — it's a fundamental property of the Fourier transform itself.

</div>
</div>

| If a function is... | Then its spectrum is... |
|---------------------|------------------------|
| Narrow in space (small $\Delta_{xy}$) | Wide in frequency (large $\Delta_{f_x f_y}$) |
| Wide in space (large $\Delta_{xy}$) | Narrow in frequency (small $\Delta_{f_x f_y}$) |

**Examples:**

1. **[Gaussian](/notes/areas/mathematics/probability/definitions/gaussian_distribution/)**: $g(x) = e^{-\pi x^2}$ transforms to $G(f) = e^{-\pi f^2}$
   - Both have the same shape — the Gaussian is "balanced" between domains
   - This is why Gaussians achieve the minimum uncertainty product

2. **Rectangle**: $\text{rect}(x)$ transforms to $\text{sinc}(f)$
   - Compact in space → infinite extent in frequency (though decaying)

3. **Delta function**: $\delta(x)$ transforms to $1$ (constant)
   - Infinitely narrow in space → infinitely wide (flat) in frequency

---

### Connection to Optics

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Uncertainty principle in optical systems</div>
<div class="callout-content">

- **Aperture size vs. angular resolution**: A larger aperture (spatial extent) produces a narrower [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern (smaller angular bandwidth)
- **Pulse duration vs. spectral width**: Short laser pulses require broad spectral bandwidth
- **Coherence length vs. spectral purity**: A spectrally narrow source has long coherence length

</div>
</div>

---

## Problem 3: Periodic Functions and the Comb Function (Goodman 2.11/2.13)

> 

$$
p(x, y) = g(x, y) * \left[ \text{comb}\left(\frac{x}{X}\right) \text{comb}\left(\frac{y}{Y}\right) \right]
$$


>
> defines a periodic function, with period $X$ in the $x$ direction and period $Y$ in the $y$ direction.

This problem explores how periodic functions arise from [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) with the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/), and how their Fourier transforms become discrete.

---

### The Setup

We're given a function defined as:



$$
p(x, y) = g(x, y) * \left[ \text{comb}\left(\frac{x}{X}\right) \text{comb}\left(\frac{y}{Y}\right) \right]
$$



with period 𝑋 in the 𝑥 direction and period 𝑌 in the 𝑦 direction, and where $*$ denotes [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/).

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>What does "period X in the x direction" mean?</div>
<div class="callout-content">

The function $p(x, y)$ repeats itself:
- Every **X units** along the x-axis: $p(x + X, y) = p(x, y)$
- Every **Y units** along the y-axis: $p(x, y + Y) = p(x, y)$

Think of it like wallpaper—$g$ is the pattern, and $X \times Y$ is the tile size. The convolution stamps copies of $g$ at every point $(nX, mY)$ for all integers $n, m$.

![Periodic tiling diagram](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/periodic_tiling.svg)

*(The blue blob is just an arbitrary example of $g(x,y)$—it could be a Gaussian, a rectangle, or any other function.)*

</div>
</div>

**What does this create?**

The [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) is an infinite train of [delta functions](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/):



$$
\text{comb}(x) = \sum_{n=-\infty}^{\infty} \delta(x - n)
$$



Convolving any function $g$ with a delta function at position $x_0$ produces a copy of $g$ shifted to that position:



$$
g(x) * \delta(x - x_0) = g(x - x_0)
$$



Therefore, convolving with the 2D [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) creates **infinite copies of $g$** at every point $(nX, mY)$ for all integers $n, m$. The result is a doubly-periodic function with period $X$ in $x$ and period $Y$ in $y$.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Physical interpretation</div>
<div class="callout-content">

This is exactly what happens when you tile a floor with identical tiles, or when you create a crystal lattice in solid-state physics. The [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) is the mathematical tool for describing periodic replication.

</div>
</div>

---

### Part (a): Fourier Transform of a Periodic Function

> Show that the Fourier transform of $p$ can be written
>
> 

$$
P(f_x, f_y) = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} G\left(\frac{n}{X}, \frac{m}{Y}\right) \delta\left(f_x - \frac{n}{X}, f_y - \frac{m}{Y}\right)
$$


>
> where $G$ is the Fourier transform of $g$.

**Goal:** Show that



$$
P(f_x, f_y) = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} G\left(\frac{n}{X}, \frac{m}{Y}\right) \delta\left(f_x - \frac{n}{X}, f_y - \frac{m}{Y}\right)
$$



where $G$ is the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of $g$.

---

**Step 1: Define the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/)**



$$
\text{comb}(x) = \sum_{n=-\infty}^{\infty} \delta(x - n)
$$



**Step 2: Scale the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/)**

Substituting $x/X$ into the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) definition:



$$
\text{comb}\left(\frac{x}{X}\right) = \sum_{n=-\infty}^{\infty} \delta\left(\frac{x}{X} - n\right)
$$



Rewrite each delta's argument: $\displaystyle\frac{x}{X} - n = \frac{x - nX}{X} = \frac{1}{X}(x - nX)$

Apply the scaling property $\delta(u/a) = |a| \delta(u)$ with $u = x - nX$ and $a = X$:



$$
\delta\left(\frac{x - nX}{X}\right) = |X| \delta(x - nX)
$$



Therefore (assuming $X > 0$):



$$
\text{comb}\left(\frac{x}{X}\right) = \sum_{n=-\infty}^{\infty} X \delta(x - nX) = X \sum_{n=-\infty}^{\infty} \delta(x - nX)
$$



**Step 3: [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/)**

The [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) is its own [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/): $\mathcal{F}\{\text{comb}(x)\} = \text{comb}(f)$.

The [scaling theorem](/notes/areas/electrical_engineering/signals_systems/definitions/fourier_scaling_property/) states: if $\mathcal{F}\{g(x)\} = G(f)$, then $\mathcal{F}\{g(ax)\} = \frac{1}{|a|} G\left(\frac{f}{a}\right)$.

Here $\text{comb}(x/X) = \text{comb}\left(\frac{1}{X} \cdot x\right)$, so $a = \frac{1}{X}$:



$$
\mathcal{F}\left\{\text{comb}\left(\frac{1}{X} \cdot x\right)\right\} = \frac{1}{|1/X|} \cdot \text{comb}\left(\frac{f_x}{1/X}\right) = |X| \cdot \text{comb}(Xf_x)
$$



Expand the comb: $\text{comb}(Xf_x) = \sum_n \delta(Xf_x - n)$

Apply delta scaling to each term:



$$
\delta(Xf_x - n) = \delta\left(X\left(f_x - \frac{n}{X}\right)\right) = \frac{1}{|X|}\delta\left(f_x - \frac{n}{X}\right)
$$



The $|X|$ and $\frac{1}{|X|}$ cancel:



$$
\mathcal{F}\left\{\text{comb}\left(\frac{x}{X}\right)\right\} = |X| \cdot \sum_n \frac{1}{|X|}\delta\left(f_x - \frac{n}{X}\right) = \sum_{n=-\infty}^{\infty} \delta\left(f_x - \frac{n}{X}\right)
$$



**Step 4: Extend to 2D**

For the separable 2D [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/):



$$
\mathcal{F}\left\{\text{comb}\left(\frac{x}{X}\right) \text{comb}\left(\frac{y}{Y}\right)\right\} = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} \delta\left(f_x - \frac{n}{X}\right) \delta\left(f_y - \frac{m}{Y}\right)
$$



**Step 5: Apply the [convolution theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/)**

[Convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) in space becomes multiplication in frequency:



$$
P(f_x, f_y) = G(f_x, f_y) \cdot \sum_{n,m} \delta\left(f_x - \frac{n}{X}, f_y - \frac{m}{Y}\right)
$$



**Step 6: Apply the sifting property**

Multiplying $G$ by a delta evaluates $G$ at the delta's location:



$$
\boxed{P(f_x, f_y) = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} G\left(\frac{n}{X}, \frac{m}{Y}\right) \delta\left(f_x - \frac{n}{X}, f_y - \frac{m}{Y}\right)}
$$



---

### Physical Interpretation

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Periodic functions have discrete spectra</div>
<div class="callout-content">

The Fourier transform of a periodic function is not a continuous function — it's a sum of weighted delta functions at discrete frequencies. Each delta's amplitude $G(n/X, m/Y)$ is the Fourier coefficient at that harmonic.

</div>
</div>

| Spatial Domain | Frequency Domain |
|----------------|------------------|
| Periodic with period $(X, Y)$ | Discrete with spacing $(1/X, 1/Y)$ |
| Continuous (smooth tile) | Discrete (isolated spikes) |
| Infinite extent (repeats forever) | Finite number of significant harmonics |

This is the 2D version of the [Fourier series](/notes/areas/mathematics/functional_analysis/definitions/fourier_series/): periodic functions can be represented as sums of harmonics, and the transform reveals which harmonics are present.

---

### Deep Dive: Delta Function Scaling

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Why does $\delta(x/X) = X \delta(x)$?</div>
<div class="callout-content">

**The gotcha:** You must apply the scaling property to the *entire* argument of the delta.

**Start from one term:**


$$
\delta\left(\frac{x}{X}-n\right)
$$



**Rewrite** so it looks like a constant times $(x - \text{something})$:


$$
\frac{x}{X}-n=\frac{x-nX}{X} = \frac{1}{X}(x-nX)
$$



**Apply the scaling rule** $\delta(c \cdot u)=\frac{1}{|c|}\delta(u)$:

Here $u=x-nX$ and $c=\frac{1}{X}$, so:


$$
\delta\left(\frac{1}{X}(x-nX)\right) = \frac{1}{|1/X|}\delta(x-nX) = |X|\delta(x-nX)
$$



**Sum over $n$:**


$$
\text{comb}\left(\frac{x}{X}\right) = \sum_{n=-\infty}^{\infty}\delta\left(\frac{x}{X}-n\right) = |X|\sum_{n=-\infty}^{\infty}\delta(x-nX)
$$



**But why is $X$ multiplying, not dividing?**

The scaling property comes from the **Jacobian** in the defining integral.

The delta function is defined by: $\int_{-\infty}^{\infty} f(x) \delta(x) \, dx = f(0)$

For $\delta(x/X)$, substitute $u = x/X$, so $dx = X \, du$:


$$
\int_{-\infty}^{\infty} f(x) \delta(x/X) \, dx = \int_{-\infty}^{\infty} f(uX) \delta(u) \cdot X \, du = X \cdot f(0)
$$



For this to equal $\int f(x) \cdot [?] \, dx$, we need $[?] = X \delta(x)$.

**The $X$ comes from $dx = X \, du$.** Stretching the argument stretches the integration measure, and that factor gets absorbed into the delta function.

</div>
</div>

---

### Part (b): Specific Example

> Sketch the function $p(x, y)$ when
>
> 

$$
g(x, y) = \text{rect}\left(\frac{2x}{X}\right) \text{rect}\left(\frac{2y}{Y}\right)
$$


>
> and find the corresponding Fourier transform $P(f_x, f_y)$.

**Given:** $g(x, y) = \text{rect}\left(\frac{2x}{X}\right) \text{rect}\left(\frac{2y}{Y}\right)$

This is a rectangle centered at the origin with width $X/2$ and height $Y/2$ — exactly one quarter of the unit cell area.

**The periodic function $p(x, y)$:**

Convolving with the [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) creates copies at every $(nX, mY)$. The result is a grid of rectangles, each of size $\frac{X}{2} \times \frac{Y}{2}$, with centers separated by $X$ and $Y$.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Visualization</div>
<div class="callout-content">

Imagine a checkerboard where each square is $X \times Y$, but only the bottom-left quarter of each square is filled in. This creates a pattern with 50% duty cycle in each dimension — 25% overall fill factor.

</div>
</div>

![Periodic array of rectangles p(x,y)](/images/notes/Areas/electrical_engineering/Physical_Optics/books/Introduction_to_Physical_Optics/images/periodic_rectangles_3b.svg)

**Finding $G(f_x, f_y)$:**

The rectangle function transforms to a sinc:



$$
\mathcal{F}\{\text{rect}(x)\} = \text{sinc}(f)
$$



With scaling:



$$
\mathcal{F}\left\{\text{rect}\left(\frac{2x}{X}\right)\right\} = \frac{X}{2} \text{sinc}\left(\frac{X f_x}{2}\right)
$$



For the separable 2D case:



$$
G(f_x, f_y) = \frac{X}{2} \text{sinc}\left(\frac{X f_x}{2}\right) \cdot \frac{Y}{2} \text{sinc}\left(\frac{Y f_y}{2}\right) = \frac{XY}{4} \text{sinc}\left(\frac{X f_x}{2}\right) \text{sinc}\left(\frac{Y f_y}{2}\right)
$$



**The transform $P(f_x, f_y)$:**

Using the result from part (a):



$$
P(f_x, f_y) = \frac{XY}{4} \sum_{n,m} \text{sinc}\left(\frac{n}{2}\right) \text{sinc}\left(\frac{m}{2}\right) \delta\left(f_x - \frac{n}{X}, f_y - \frac{m}{Y}\right)
$$



**Which harmonics survive?**

The [sinc function](/notes/areas/electrical_engineering/signals_systems/definitions/sinc_function/) has zeros at nonzero integers:



$$
\text{sinc}(k) = 0 \quad \text{for } k = \pm 1, \pm 2, \pm 3, \ldots
$$



But $\text{sinc}(n/2)$ is zero only when $n/2$ is a nonzero integer, i.e., when $n$ is an even nonzero integer ($n = \pm 2, \pm 4, \ldots$).

| $n$ | $\text{sinc}(n/2)$ |
|-----|-------------------|
| 0 | 1 |
| $\pm 1$ | $2/\pi \approx 0.637$ |
| $\pm 2$ | 0 |
| $\pm 3$ | $-2/(3\pi) \approx -0.212$ |
| $\pm 4$ | 0 |

Only **odd harmonics** (and the DC term) have nonzero coefficients. This is characteristic of a 50% duty cycle pattern.

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>Connection to signal processing</div>
<div class="callout-content">

This is the same reason that a 50% duty cycle square wave in 1D contains only odd harmonics. The symmetry of the pattern causes even harmonics to cancel.

</div>
</div>

---

## Problem 4: The Equivalent Object Theorem (Goodman 2.13/2.15)

> The input to a certain imaging system is an _object_ complex field distribution $U_o(x, y)$ of unlimited spatial frequency content, while the output of the system is an _image_ field distribution $U_i(x, y)$. The imaging system can be assumed to act as a linear, invariant lowpass filter with a transfer function that is identically zero outside the region $|f_x| \leq B_X / 2, |f_y| \leq B_Y / 2$ in the frequency domain. Show that there exists an "equivalent" object $U_o'(x, y)$ consisting of a rectangular array of point sources that produces exactly the same image $U_i$ as does the true object $U_o$, and that the field distribution across the equivalent object can be written
>
> 

$$
U_o'(x, y) = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} \left[ \int_{\xi=-\infty}^{\infty} \int_{\eta=-\infty}^{\infty} U_o(\xi, \eta) \, \text{sinc}(n - B_X \xi) \, \text{sinc}(m - B_Y \eta) \, d\xi \, d\eta \right] \delta\left(x - \frac{n}{B_X}, y - \frac{m}{B_Y}\right).
$$



This problem proves a remarkable result: for any bandlimited imaging system, there exists an equivalent object made entirely of point sources that produces exactly the same image.

---

### The Setup

**The imaging system:**
- Input: object field $U_o(x, y)$ with unlimited spatial frequency content
- Output: image field $U_i(x, y)$
- The system acts as a **lowpass filter** with cutoff frequencies $B_X/2$ and $B_Y/2$
- [Transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/): $H(f_x, f_y) = 1$ inside the passband, $0$ outside

**The claim:** There exists an equivalent object $U_o'(x, y)$ consisting entirely of point sources (delta functions) on a rectangular grid that produces exactly the same image.

---

### Why Does This Work?

<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>The key insight</div>
<div class="callout-content">

The imaging system only "sees" frequencies within its passband. Any two objects with identical frequency content inside the passband will produce identical images — differences outside the passband are invisible to the system.

</div>
</div>

This is analogous to how two audio signals that differ only in ultrasonic frequencies will sound identical through speakers that can't reproduce ultrasonics.

---

### The Derivation

**Step 1: Express the image in terms of bandlimited content**

The image is determined by convolving the object spectrum with the system's [transfer function](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/):



$$
U_i(x, y) = \mathcal{F}^{-1}\{H(f_x, f_y) \cdot \mathcal{U}_o(f_x, f_y)\}
$$



Since $H$ is zero outside the passband, only the portion of $\mathcal{U}_o$ inside the region $|f_x| \leq B_X/2$, $|f_y| \leq B_Y/2$ contributes to the image.

Define the bandlimited spectrum:



$$
\tilde{\mathcal{U}}_o(f_x, f_y) = \begin{cases} \mathcal{U}_o(f_x, f_y) & |f_x| \leq B_X/2 \text{ and } |f_y| \leq B_Y/2 \\ 0 & \text{otherwise} \end{cases}
$$



**Step 2: Represent the bandlimited spectrum as a [Fourier series](/notes/areas/mathematics/functional_analysis/definitions/fourier_series/)**

Since $\tilde{\mathcal{U}}_o$ is nonzero only within a finite rectangle, we can expand it as a [Fourier series](/notes/areas/mathematics/functional_analysis/definitions/fourier_series/) over that region:



$$
\tilde{\mathcal{U}}_o(f_x, f_y) = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} c_{nm} \, e^{j2\pi\left(\frac{n f_x}{B_X} + \frac{m f_y}{B_Y}\right)}
$$



The coefficients are:



$$
c_{nm} = \frac{1}{B_X B_Y} \int_{-B_X/2}^{B_X/2} \int_{-B_Y/2}^{B_Y/2} \tilde{\mathcal{U}}_o(f_x, f_y) \, e^{-j2\pi\left(\frac{n f_x}{B_X} + \frac{m f_y}{B_Y}\right)} df_x \, df_y
$$



**Step 3: Relate coefficients to spatial integrals**

This coefficient integral can be rewritten using the [convolution theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/). The result involves the original object convolved with sinc functions:



$$
c_{nm} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} U_o(\xi, \eta) \, \text{sinc}(n - B_X \xi) \, \text{sinc}(m - B_Y \eta) \, d\xi \, d\eta
$$



<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>What is this integral computing?</div>
<div class="callout-content">

This is the **projection** of the original object onto a 2D sinc basis function centered at the grid point $(n/B_X, m/B_Y)$. The sinc functions act as interpolation kernels, measuring how much the object contributes to each sample point.

</div>
</div>

**Step 4: Construct the equivalent object**

The inverse [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of $e^{j2\pi(f_x n/B_X + f_y m/B_Y)}$ is a delta function at position $(n/B_X, m/B_Y)$.

Therefore, the equivalent object is:



$$
\boxed{U_o'(x, y) = \sum_{n=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} U_o(\xi, \eta) \, \text{sinc}(n - B_X \xi) \, \text{sinc}(m - B_Y \eta) \, d\xi \, d\eta \right] \delta\left(x - \frac{n}{B_X}, y - \frac{m}{B_Y}\right)}
$$



---

### Physical Interpretation

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Point source representation</div>
<div class="callout-content">

The equivalent object is a **rectangular array of point sources** located at positions $(n/B_X, m/B_Y)$. The amplitude of each point source is determined by the sinc-weighted integral of the original object — essentially a "smart" sampling that accounts for the system's bandwidth.

</div>
</div>

| Property | Equivalent Object |
|----------|-------------------|
| Structure | Grid of point sources (delta functions) |
| Grid spacing | $1/B_X$ in $x$, $1/B_Y$ in $y$ |
| Amplitudes | Sinc-weighted integrals of $U_o$ |
| Image produced | Identical to original object |

**Why does the spacing matter?**

The grid spacing is $1/B_X$ and $1/B_Y$ — exactly the [Nyquist sampling](/notes/areas/electrical_engineering/physical_optics/definitions/nyquist_criterion/) intervals for a signal bandlimited to $B_X/2$ and $B_Y/2$. This is no coincidence: the [sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) theorem tells us that a bandlimited signal is completely determined by samples at the Nyquist rate.

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Application: Holography and optical processing</div>
<div class="callout-content">

This theorem justifies representing continuous objects as discrete arrays of point sources in computational optics. It's fundamental to understanding resolution limits, sampling requirements, and the connection between continuous and discrete representations in imaging.

</div>
</div>

---

## Problem 5: Angular Spectrum of Apertures (Goodman 3.5)

> Assuming unit-amplitude normally incident plane-wave illumination, find the angular spectrum of

This problem introduces the **[angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) representation** — a powerful method for analyzing [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) by decomposing a wavefront into plane waves traveling in different directions.

---

### Background: The Angular Spectrum

When a [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) illuminates an aperture, the field immediately after the aperture is:



$$
U(x, y, 0) = t(x, y)
$$



where $t(x, y)$ is the **transmission function** of the aperture.

The **[angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/)** is simply the 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of this field:



$$
A(f_x, f_y) = \mathcal{F}\{U(x, y, 0)\} = \mathcal{F}\{t(x, y)\}
$$



<div class="callout callout-tip">
<div class="callout-title"><span class="callout-icon">💡</span>Physical meaning</div>
<div class="callout-content">

Each point $(f_x, f_y)$ in the angular spectrum represents a plane wave traveling in a specific direction. The spatial frequencies relate to propagation angles by:


$$
\sin\theta_x = \lambda f_x, \quad \sin\theta_y = \lambda f_y
$$


where $\lambda$ is the wavelength. Higher spatial frequencies correspond to plane waves traveling at larger angles from the optical axis.

</div>
</div>

---

### Part (a): Circular Aperture

> A circular aperture of diameter $d$.

**The aperture:** A circular opening of diameter $d$.

**Transmission function:**



$$
t(x, y) = \text{circ}\left(\frac{2r}{d}\right)
$$



where $r = \sqrt{x^2 + y^2}$ and the circ function is defined as:



$$
\text{circ}(\rho) = \begin{cases} 1 & \rho \leq 1 \\ 0 & \rho > 1 \end{cases}
$$



**Finding the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/):**

For circularly symmetric functions, the 2D [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) reduces to the [Fourier-Bessel (Hankel) transform](/notes/areas/electrical_engineering/physical_optics/definitions/hankel_transform/):



$$
A(\rho_f) = 2\pi \int_0^{\infty} r \, t(r) \, J_0(2\pi r \rho_f) \, dr
$$



where $\rho_f = \sqrt{f_x^2 + f_y^2}$ is the radial spatial frequency.

For the circ function, the standard transform pair (Goodman Table 2.1) gives:



$$
\mathcal{F}\left\{\text{circ}\left(\frac{r}{a}\right)\right\} = \pi a^2 \frac{2J_1(2\pi a \rho_f)}{2\pi a \rho_f}
$$



With $a = d/2$ (the radius):



$$
A(f_x, f_y) = \frac{\pi d^2}{4} \cdot \frac{2J_1(\pi d \rho_f)}{\pi d \rho_f}
$$



This can be written more compactly using the **jinc function**:



$$
\text{jinc}(x) = \frac{2J_1(\pi x)}{\pi x}
$$



Therefore:



$$
\boxed{A(f_x, f_y) = \frac{\pi d^2}{4} \, \text{jinc}(d\rho_f)}
$$



where $\rho_f = \sqrt{f_x^2 + f_y^2}$.

---

### Properties of the Result

<div class="callout callout-note">
<div class="callout-title"><span class="callout-icon">📝</span>The jinc function</div>
<div class="callout-content">

The jinc function is the circularly symmetric analog of the sinc function:

| Property | sinc (1D) | jinc (2D circular) |
|----------|-----------|-------------------|
| Definition | $\frac{\sin(\pi x)}{\pi x}$ | $\frac{2J_1(\pi x)}{\pi x}$ |
| First zero | $x = 1$ | $x \approx 1.22$ |
| Shape | Oscillating, decaying | Oscillating, decaying |
| Transform pair | rect ↔ sinc | circ ↔ jinc |

The jinc function has a central peak and concentric rings of decreasing amplitude — this is the famous **[Airy pattern](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/)**.

</div>
</div>

**Physical interpretation:**

The [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) tells us how the light from the aperture is distributed among different propagation directions:

- **Central peak:** Most energy travels straight through (low spatial frequencies, small angles)
- **Rings:** Some energy diffracts to larger angles (higher spatial frequencies)
- **Zeros:** At certain angles, there's complete destructive interference

The first zero occurs at $\rho_f = 1.22/d$, which corresponds to the angle $\theta = \arcsin(1.22\lambda/d)$ — the **[Rayleigh criterion](/notes/areas/electrical_engineering/physical_optics/definitions/rayleigh_criterion/)** for resolution.

---

### Part (b): Circular Opaque Disk

> A circular opaque disk of diameter $d$.

**The obstacle:** A circular opaque disk of diameter $d$.

**Transmission function:**



$$
t(x, y) = 1 - \text{circ}\left(\frac{2r}{d}\right)
$$



This is the **complement** of the circular aperture — transparent everywhere except within the disk.

**Finding the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/):**

By linearity of the [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/):



$$
A_{\text{disk}}(f_x, f_y) = \mathcal{F}\{1\} - \mathcal{F}\left\{\text{circ}\left(\frac{2r}{d}\right)\right\}
$$



The [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of a constant is a delta function at the origin:



$$
\mathcal{F}\{1\} = \delta(f_x, f_y)
$$



Therefore:



$$
\boxed{A_{\text{disk}}(f_x, f_y) = \delta(f_x, f_y) - \frac{\pi d^2}{4} \, \text{jinc}(d\rho_f)}
$$



---

### Babinet's Principle

<div class="callout callout-important">
<div class="callout-title"><span class="callout-icon">❗</span>Babinet's Principle</div>
<div class="callout-content">

The diffracted fields from complementary screens (aperture and its complement) differ only by the unobstructed plane wave:



$$
A_{\text{disk}} = A_{\text{unobstructed}} - A_{\text{aperture}}
$$



Or equivalently:



$$
A_{\text{aperture}} + A_{\text{disk}} = A_{\text{unobstructed}}
$$



</div>
</div>

**Physical interpretation:**

| Component | What it represents |
|-----------|--------------------|
| $\delta(f_x, f_y)$ | The unobstructed [plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) — light that would pass if nothing were there |
| $-\frac{\pi d^2}{4} \text{jinc}(d\rho_f)$ | The diffracted wave — light removed by the disk |

**Remarkable consequence:**

Except for the central delta function (the [DC component](/notes/areas/electrical_engineering/signals_systems/definitions/dc_component/), representing the undiffracted beam), the [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) of the opaque disk has the **same magnitude** as that of the circular aperture — they differ only in sign!

This means:
- The **[diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) patterns** (intensity distributions) are identical away from the center
- An opaque disk and a circular aperture of the same size produce the same fringe pattern
- Only the on-axis intensity differs (the disk blocks the direct beam; the aperture transmits it)

<div class="callout callout-example">
<div class="callout-title"><span class="callout-icon">📋</span>Poisson's spot (Arago spot)</div>
<div class="callout-content">

Babinet's principle explains a famous phenomenon: a bright spot appears at the center of the shadow of a circular disk. The diffracted waves from the disk's edge constructively interfere at the center, creating a bright spot where you might expect darkness. This was predicted by Poisson (who thought it disproved the wave theory of light) and experimentally confirmed by Arago — actually supporting the wave theory!

</div>
</div>

---

## Homework 2 Summary

| Problem | Key Concept |
|---------|-------------|
| 1(a) | A projection is a line integral — it collapses one dimension |
| 1(b) | [Projection-slice theorem](/notes/areas/electrical_engineering/physical_optics/definitions/projection_slice_theorem/): 1D FT of projection = slice of 2D FT |
| 1(c) | Many projections at different angles → fill Fourier space → inverse FT recovers image |
| 2 | Equivalent area × equivalent bandwidth = 1 ([uncertainty principle](/notes/areas/electrical_engineering/physical_optics/definitions/uncertainty_principle/)) |
| 3 | Periodic functions have discrete spectra; [Dirac comb](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) creates periodicity |
| 4 | Bandlimited systems can replace continuous objects with point source arrays |
| 5 | [Angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) method; circ ↔ jinc transform; Babinet's principle |

This elegant mathematical relationship — that projections in real space correspond to slices in Fourier space — is why CT scanners rotate around the patient, acquiring projections from many angles to reconstruct the internal structure. The area-bandwidth product of Problem 2 quantifies the fundamental tradeoff between spatial and spectral localization. The [angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) representation of Problem 6 provides the foundation for understanding [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) from arbitrary apertures.

---

# Key Concepts Index

These mathematical tools form the foundation for analyzing optical systems, [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/), and imaging:

- [Dirac delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) — Impulse functions and sifting property
- [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) — Spatial ↔ frequency domain conversion
- [Convolution theorem](/notes/areas/electrical_engineering/signals_systems/definitions/convolution_theorem/) — Multiplication ↔ [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) duality
- [Fourier-Bessel transform](/notes/areas/electrical_engineering/physical_optics/definitions/hankel_transform/) — For circularly symmetric functions
- [Bessel functions](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/) — Natural [basis](/notes/areas/mathematics/linear_algebra/definitions/basis/) for radial symmetry
- [Radon transform](/notes/areas/electrical_engineering/physical_optics/definitions/radon_transform/) — Line integrals (projections)
- [Projection-slice theorem](/notes/areas/electrical_engineering/physical_optics/definitions/projection_slice_theorem/) — Foundation of CT imaging
- [Computed tomography](/notes/areas/electrical_engineering/physical_optics/definitions/computed_tomography/) — Medical imaging from projections
- [Angular spectrum](/notes/areas/electrical_engineering/physical_optics/definitions/angular_spectrum/) — [Plane wave](/notes/areas/electrical_engineering/physical_optics/definitions/plane_wave/) decomposition of diffracted fields
- [Airy pattern](/notes/areas/electrical_engineering/physical_optics/definitions/airy_disk/) — [Diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) pattern of circular aperture (jinc function)
- [Babinet's principle](/notes/areas/electrical_engineering/physical_optics/definitions/babinet_principle/) — Complementary screens produce related [diffraction](/notes/areas/electrical_engineering/physical_optics/definitions/diffraction/) patterns
- [Nyquist sampling](/notes/areas/electrical_engineering/physical_optics/definitions/nyquist_criterion/) — [Sampling](/notes/areas/electrical_engineering/signals_systems/definitions/sampling/) rate for bandlimited signals
- [Sinc function](/notes/areas/electrical_engineering/signals_systems/definitions/sinc_function/) — [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) of rectangle; ideal interpolation kernel
- [Rayleigh criterion](/notes/areas/electrical_engineering/physical_optics/definitions/rayleigh_criterion/) — Resolution limit for optical systems
- [Scaling property](/notes/areas/electrical_engineering/signals_systems/definitions/fourier_scaling_property/) — Narrow in space ↔ wide in frequency
