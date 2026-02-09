---
title: "Introduction to Physical Optics"
---

2.1 Fourier Analysis in Two Dimensions

2.1.1 Definition and Existence Conditions

The [Fourier spectrum](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) (or frequency spectrum) of a two-dimensional, complex-valued function
g(x,y) is defined by



$$
G(f_X,f_Y) = \iint g(x,y) \exp{-j2\pi(f_X x + f_Y y)}\, dx\,dy \tag{2.1-1}
$$



The inverse Fourier transform is



$$
g(x,y) = \iint G(f_X,f_Y) \exp{+j2\pi(f_X x + f_Y y)}\, df_X\,df_Y \tag{2.1-2}
$$



Here $x,y$ are spatial variables and $f_X,f_Y$ are spatial frequencies.

A commonly used sufficient set of existence conditions for Eq. (2.1-1) is:

1. $g(x,y)$ is [absolutely integrable](/notes/areas/mathematics/real_analysis/definitions/absolutely_integrable/) over the $(x,y)$ plane.
2. $g(x,y)$ has only a finite number of discontinuities and extrema in any finite region.
3. $g(x,y)$ has no infinite discontinuities.

These conditions are sufficient but not necessary, and are often violated by idealized
functions used in physical modeling.

The [Dirac delta function](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/) may be represented as the limiting form



$$
\delta(x) = \lim_{N \to \infty} N\exp(-\pi N^2 x^2) \tag{2.1-3}
$$



and its two-dimensional counterpart



$$
\delta(x,y) = \lim_{N \to \infty} N^2\exp[-\pi N^2(x^2+y^2)] \tag{2.1-4}
$$



Other commonly encountered non-integrable functions include



$$
g(x,y)=1, \qquad g(x,y)=\cos(2\pi f_X x) \tag{2.1-5}
$$



Such cases motivate the use of generalized Fourier transforms.

⸻

2.1.2 The Fourier Transform as a Decomposition

The inverse transform may be written



$$
g(x,y) = \iint G(f_X,f_Y) \exp{j2\pi(f_X x + f_Y y)}\, df_X\,df_Y \tag{2.1-8}
$$



which expresses g(x,y) as a superposition of complex exponentials. Each elementary
function has phase



$$
2\pi(f_X x + f_Y y)
$$



Zero-phase lines satisfy



$$
f_X x + f_Y y = n, \quad n\in\mathbb{Z} \tag{2.1-9}
$$



The direction angle $\theta$ of these lines is



$$
\theta = \arctan\left(\frac{f_Y}{f_X}\right) \tag{2.1-10}
$$



and the spatial period is



$$
L = \frac{1}{\sqrt{f_X^2 + f_Y^2}} \tag{2.1-11}
$$



⸻

2.1.3 Fourier Transform Theorems

Let



$$
\mathcal{F}\{g(x,y)\} = G(f_X,f_Y)
$$



1. **Linearity**



$$
\mathcal{F}{a g_1 + b g_2} = a G_1 + b G_2
$$



2. **Shift theorem**



$$
\mathcal{F}\{g(x-x_0,y-y_0)\} = G(f_X,f_Y) e^{-j2\pi(f_X x_0 + f_Y y_0)} \tag{2.1-13}
$$



3. **[Rayleigh (Parseval) theorem](/notes/areas/mathematics/functional_analysis/definitions/parseval_theorem/)**



$$
\iint |g(x,y)|^2 dx\, dy = \iint |G(f_X,f_Y)|^2 df_X\, df_Y \tag{2.1-14}
$$



4. **[Convolution theorem](/notes/areas/mathematics/real_analysis/definitions/convolution/)**



$$
\mathcal{F}{g*h} = G \cdot H \tag{2.1-15}
$$



5. **Autocorrelation theorem**



$$
\mathcal{F}{g \star g^*} = |G|^2 \tag{2.1-16}
$$



6. **Rotation theorem**

If $g(r,\theta) \leftrightarrow G(\rho,\phi)$, then rotation by $\theta_0$ in space produces the same rotation in frequency:



$$
G(\rho,\phi-\theta_0) \tag{2.1-18}
$$



7. **Fourier integral theorem**

At points of continuity,



$$
\mathcal{F}^{-1}{\mathcal{F}[g]} = g \tag{2.1-19}
$$



8. **Similarity theorem (Scaling)**

If the spatial coordinates are scaled by constants $a$ and $b$:



$$
\mathcal{F}\{g(ax, by)\} = \frac{1}{|ab|} G\left(\frac{f_X}{a}, \frac{f_Y}{b}\right) \tag{2.1-12}
$$



Stretching the function in space compresses its spectrum in frequency (and vice versa). The amplitude scales inversely with the product $|ab|$ to preserve energy.

9. **Shear theorem**

For a shear transformation in the $x$-direction:



$$
\mathcal{F}\{g(x + \alpha y, y)\} = G(f_X, f_Y - \alpha f_X)
$$



A shear in spatial coordinates produces a corresponding shear in frequency coordinates. This is important in analyzing tilted or skewed optical systems.

⸻

2.1.4 Separable Functions

If



$$
g(x,y) = g_x(x) g_y(y) \tag{2.1-20}
$$



then



$$
G(f_X,f_Y) = G_X(f_X) G_Y(f_Y) \tag{2.1-22}
$$



⸻

2.1.5 Functions with Circular Symmetry: Fourier–Bessel Transforms

A function is circularly symmetric if



$$
g(r,\theta) = g_R(r) \tag{2.1-25}
$$



The Fourier transform becomes the Fourier-Bessel transform:



$$
G(\rho) = 2\pi \int_0^\infty r\, g_R(r) J_0(2\pi r \rho)\, dr \tag{2.1-32}
$$



where J_0 is the zeroth-order [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/).

⸻

2.1.6 Some Frequently Used Functions and Their Transforms

**Rectangle Function (rect)**

The one-dimensional rectangle function is defined as:



$$
\mathrm{rect}(x) = \begin{cases} 1 & |x| \leq \frac{1}{2} \\ 0 & \text{otherwise} \end{cases}
$$



Its Fourier transform is the sinc function:



$$
\mathcal{F}\{\mathrm{rect}(x)\} = \mathrm{sinc}(f_X)
$$



**Sinc Function**



$$
\mathrm{sinc}(x) = \frac{\sin(\pi x)}{\pi x}
$$



Note: The sinc function equals 1 at $x=0$ and has zeros at all nonzero integers. Its Fourier transform is the rect function:



$$
\mathcal{F}\{\mathrm{sinc}(x)\} = \mathrm{rect}(f_X)
$$



**Signum Function (sgn)**



$$
\mathrm{sgn}(x) = \begin{cases} +1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}
$$



Its Fourier transform (in the generalized sense):



$$
\mathcal{F}\{\mathrm{sgn}(x)\} = \frac{1}{j\pi f_X}
$$



**Triangle Function (tri)**



$$
\mathrm{tri}(x) = \begin{cases} 1 - |x| & |x| \leq 1 \\ 0 & |x| > 1 \end{cases}
$$



The triangle function is the [convolution](/notes/areas/mathematics/real_analysis/definitions/convolution/) of a rect with itself:



$$
\mathrm{tri}(x) = \mathrm{rect}(x) * \mathrm{rect}(x)
$$



Its Fourier transform:



$$
\mathcal{F}\{\mathrm{tri}(x)\} = \mathrm{sinc}^2(f_X)
$$



**[Comb Function](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) (Shah Function)**

The [comb function](/notes/areas/electrical_engineering/physical_optics/definitions/dirac_comb/) is an infinite series of equally spaced [delta functions](/notes/areas/mathematics/functional_analysis/definitions/dirac_delta_function/):



$$
\mathrm{comb}(x) = \sum_{n=-\infty}^{\infty} \delta(x - n)
$$



This function is its own Fourier transform:



$$
\mathcal{F}\{\mathrm{comb}(x)\} = \mathrm{comb}(f_X)
$$



The comb function is fundamental to sampling theory. Multiplying a function by comb samples it at integer intervals.

**Circle Function (circ)**

The two-dimensional circle function:



$$
\mathrm{circ}(r) = \begin{cases} 1 & r \leq 1 \\ 0 & r > 1 \end{cases}
$$



where $r = \sqrt{x^2 + y^2}$. This represents a circular aperture of unit radius.

Its Fourier-Bessel transform involves the first-order [Bessel function](/notes/areas/mathematics/functional_analysis/definitions/bessel_function/):



$$
\mathcal{B}\{\mathrm{circ}(r)\} = \frac{J_1(2\pi\rho)}{\rho} \tag{2.1-36}
$$



where $\rho = \sqrt{f_X^2 + f_Y^2}$. This result is central to diffraction theory for circular apertures.

**Gaussian Function**



$$
g(x) = e^{-\pi x^2}
$$



The Gaussian is its own [Fourier transform](/notes/areas/mathematics/functional_analysis/definitions/fourier_transform/) (with appropriate normalization):



$$
\mathcal{F}\{e^{-\pi x^2}\} = e^{-\pi f_X^2}
$$



This self-transform property makes Gaussians particularly useful in optics. In two dimensions:



$$
\mathcal{F}\{e^{-\pi(x^2 + y^2)}\} = e^{-\pi(f_X^2 + f_Y^2)}
$$



**Table of Common Fourier Transform Pairs**

| Function $g(x)$ | Transform $G(f_X)$ |
|-----------------|-------------------|
| $\mathrm{rect}(x)$ | $\mathrm{sinc}(f_X)$ |
| $\mathrm{sinc}(x)$ | $\mathrm{rect}(f_X)$ |
| $\mathrm{tri}(x)$ | $\mathrm{sinc}^2(f_X)$ |
| $\mathrm{comb}(x)$ | $\mathrm{comb}(f_X)$ |
| $e^{-\pi x^2}$ | $e^{-\pi f_X^2}$ |
| $\mathrm{sgn}(x)$ | $\frac{1}{j\pi f_X}$ |
| $\delta(x)$ | $1$ |
| $1$ | $\delta(f_X)$ |
| $e^{j2\pi f_0 x}$ | $\delta(f_X - f_0)$ |
| $\cos(2\pi f_0 x)$ | $\frac{1}{2}[\delta(f_X - f_0) + \delta(f_X + f_0)]$ |
| $\sin(2\pi f_0 x)$ | $\frac{1}{2j}[\delta(f_X - f_0) - \delta(f_X + f_0)]$ |

⸻

2.2 Local Spatial Frequency and Space-Frequency Localization

2.2.1 Local Spatial Frequencies

For a general complex function $g(x,y)$, we can write:



$$
g(x,y) = |g(x,y)| e^{j\phi(x,y)} \tag{2.2-1}
$$



where $|g(x,y)|$ is the amplitude and $\phi(x,y)$ is the phase.

The **local spatial frequencies** are defined as the spatial rates of change of phase:



$$
f_X^{(\ell)}(x,y) = \frac{1}{2\pi} \frac{\partial \phi}{\partial x} \tag{2.2-2}
$$





$$
f_Y^{(\ell)}(x,y) = \frac{1}{2\pi} \frac{\partial \phi}{\partial y} \tag{2.2-3}
$$



**Physical Interpretation:**

For a simple complex exponential $g(x,y) = e^{j2\pi(f_0 x + g_0 y)}$:
- The phase is $\phi(x,y) = 2\pi(f_0 x + g_0 y)$
- The local frequencies are constant: $f_X^{(\ell)} = f_0$, $f_Y^{(\ell)} = g_0$

For more complex functions, the local frequency varies with position, representing how the "instantaneous" oscillation rate changes across the function.

**Example: Quadratic Phase (Chirp)**

Consider a quadratic phase function:



$$
g(x) = e^{j\pi \alpha x^2} \tag{2.2-4}
$$



The local frequency is:



$$
f_X^{(\ell)}(x) = \frac{1}{2\pi} \frac{d}{dx}(\pi \alpha x^2) = \alpha x \tag{2.2-5}
$$



The local frequency increases linearly with position. This is called a **chirp** function, important in pulse compression and synthetic aperture radar.

2.2.2 The Wigner Distribution Function

The **Wigner distribution function** provides a joint space-frequency representation of a signal. For a one-dimensional function $g(x)$:



$$
W_g(x, f_X) = \int_{-\infty}^{\infty} g\left(x + \frac{x'}{2}\right) g^*\left(x - \frac{x'}{2}\right) e^{-j2\pi f_X x'} dx' \tag{2.2-6}
$$



**Properties of the Wigner Distribution:**

1. **Real-valued**: $W_g(x, f_X)$ is always real, though it can be negative.

2. **Marginal distributions**:
   - Integrating over frequency yields the intensity: $\int W_g(x, f_X) df_X = |g(x)|^2$
   - Integrating over space yields the power spectrum: $\int W_g(x, f_X) dx = |G(f_X)|^2$

3. **Energy**:


$$
\iint W_g(x, f_X) dx\, df_X = \int |g(x)|^2 dx = \int |G(f_X)|^2 df_X \tag{2.2-7}
$$



4. **Shift properties**:
   - Spatial shift: $g(x-x_0) \to W_g(x-x_0, f_X)$
   - Frequency shift: $g(x)e^{j2\pi f_0 x} \to W_g(x, f_X - f_0)$

**Uncertainty Principle:**

The Wigner distribution illustrates the fundamental trade-off between spatial and frequency localization. A function cannot be simultaneously localized in both space and frequency. The uncertainty relation:



$$
\Delta x \cdot \Delta f_X \geq \frac{1}{4\pi} \tag{2.2-8}
$$



where $\Delta x$ and $\Delta f_X$ are the standard deviations in space and frequency respectively.

The Gaussian function achieves the minimum uncertainty product (equality in the above relation), making it the optimally localized function in the joint space-frequency domain.

**Two-Dimensional Wigner Distribution:**



$$
W_g(x, y; f_X, f_Y) = \iint g\left(x+\frac{x'}{2}, y+\frac{y'}{2}\right) g^*\left(x-\frac{x'}{2}, y-\frac{y'}{2}\right) e^{-j2\pi(f_X x' + f_Y y')} dx'\, dy' \tag{2.2-9}
$$



⸻

2.3 Linear Systems

A system \mathcal{S}\{\cdot\} maps an input g_1(x,y) to an output g_2(x,y):



$$
g_2(x,y) = \mathcal{S}{g_1(x,y)} \tag{2.3-1}
$$



⸻

2.3.1 Linearity and the Superposition Integral

A system is linear if



$$
\mathcal{S}{a p + b q} = a\mathcal{S}{p} + b\mathcal{S}{q} \tag{2.3-2}
$$



Using the sifting property of the delta function,



$$
g_1(x,y) = \iint g_1(\xi,\eta), \delta(x-\xi,y-\eta), d\xi d\eta \tag{2.3-3}
$$



Substitution yields the [superposition](/notes/areas/electrical_engineering/signals_systems/definitions/superposition/) integral:



$$
g_2(x,y) = \iint g_1(\xi,\eta), \mathcal{S}{\delta(x-\xi,y-\eta)}, d\xi d\eta \tag{2.3-5}
$$



⸻

2.3.2 Invariant Linear Systems: [Transfer Functions](/notes/areas/electrical_engineering/signals_systems/definitions/transfer_function/)

If the [impulse response](/notes/areas/electrical_engineering/signals_systems/definitions/impulse_response/) is shift invariant,



$$
h(x,y;\xi,\eta) = h(x-\xi,y-\eta)
$$



then



$$
g_2(x,y) = g_1(x,y) * h(x,y) \tag{2.3-9}
$$



Taking Fourier transforms,



$$
G_2(f_X,f_Y) = H(f_X,f_Y) G_1(f_X,f_Y) \tag{2.3-10}
$$



where



$$
H(f_X,f_Y) = \iint h(\xi,\eta) e^{-j2\pi(f_X \xi + f_Y \eta)} d\xi\, d\eta \tag{2.3-11}
$$



⸻

2.4 Two-Dimensional Sampling Theory

2.4.1 The [Whittaker–Shannon Sampling Theorem](/notes/areas/electrical_engineering/signals_systems/definitions/whittaker-shannon_sampling_theorem/)

Sampling on a rectangular lattice gives



$$
g_s(x,y) = \mathrm{comb}\left(\frac{x}{X}\right) \mathrm{comb}\left(\frac{y}{Y}\right) g(x,y) \tag{2.4-1}
$$



The spectrum is



$$
G_s(f_X,f_Y) = \frac{1}{XY} \sum_{n,m} G\left(f_X-\frac{n}{X}, f_Y-\frac{m}{Y}\right) \tag{2.4-2}
$$



Exact recovery requires



$$
X \le \frac{1}{B_x}, \qquad Y \le \frac{1}{B_y} \tag{2.4-3}
$$



⸻

2.4.2 Oversampling, Undersampling, and Aliasing

Oversampling creates greater separation between spectral replicas. Undersampling causes
overlap, producing aliasing, which prevents exact reconstruction.

⸻

2.4.3 Space–Bandwidth Product

If g(x,y) occupies region L_x \times L_y and has bandwidth B_x \times B_y, the
space–bandwidth product is



$$
N = L_x L_y B_x B_y \tag{2.4-6}
$$



This quantity represents the number of degrees of freedom of the function.

⸻

2.5 Discrete Fourier Transform

The **Discrete Fourier Transform (DFT)** is the computational tool used to numerically evaluate Fourier transforms. It operates on sampled data and produces sampled frequency information.

2.5.1 Definition of the DFT

For a sequence of $N$ complex samples $\{g_n\}$ where $n = 0, 1, \ldots, N-1$, the DFT is defined as:



$$
G_m = \sum_{n=0}^{N-1} g_n \, e^{-j2\pi mn/N} \tag{2.5-1}
$$



for $m = 0, 1, \ldots, N-1$.

The inverse DFT recovers the original samples:



$$
g_n = \frac{1}{N} \sum_{m=0}^{N-1} G_m \, e^{j2\pi mn/N} \tag{2.5-2}
$$



2.5.2 Relationship to the Continuous Fourier Transform

Consider sampling a continuous function $g(x)$ at $N$ points with spacing $\Delta x$:



$$
g_n = g(n \Delta x), \quad n = 0, 1, \ldots, N-1 \tag{2.5-3}
$$



The DFT approximates samples of the continuous Fourier transform at frequencies:



$$
f_{X,m} = \frac{m}{N \Delta x}, \quad m = 0, 1, \ldots, N-1 \tag{2.5-4}
$$



The frequency spacing is:



$$
\Delta f = \frac{1}{N \Delta x} = \frac{1}{L} \tag{2.5-5}
$$



where $L = N \Delta x$ is the total length of the sampled region.

**Key relationships:**
- Spatial sampling interval: $\Delta x$
- Number of samples: $N$
- Total spatial extent: $L = N \Delta x$
- Frequency sampling interval: $\Delta f = 1/L$
- Maximum frequency (Nyquist): $f_{X,\max} = 1/(2\Delta x)$

2.5.3 Properties of the DFT

1. **Periodicity**: The DFT treats the input as one period of a periodic sequence with period $N$:


$$
g_{n+N} = g_n, \quad G_{m+N} = G_m \tag{2.5-6}
$$



2. **Linearity**:


$$
\mathrm{DFT}\{a g_n + b h_n\} = a G_m + b H_m \tag{2.5-7}
$$



3. **Shift theorem**: A circular shift in the spatial domain introduces a linear phase in frequency:


$$
\mathrm{DFT}\{g_{n-n_0}\} = G_m \, e^{-j2\pi m n_0/N} \tag{2.5-8}
$$



4. **[Convolution theorem](/notes/areas/mathematics/real_analysis/definitions/convolution/)**: Multiplication in one domain corresponds to circular convolution in the other:


$$
\mathrm{DFT}\{g_n \cdot h_n\} = \frac{1}{N} G_m \circledast H_m \tag{2.5-9}
$$



where $\circledast$ denotes circular convolution.

5. **[Parseval's theorem](/notes/areas/mathematics/functional_analysis/definitions/parseval_theorem/)**:


$$
\sum_{n=0}^{N-1} |g_n|^2 = \frac{1}{N} \sum_{m=0}^{N-1} |G_m|^2 \tag{2.5-10}
$$



2.5.4 The Fast Fourier Transform (FFT)

Direct computation of the DFT requires $O(N^2)$ complex multiplications. The **Fast Fourier Transform** is an algorithm that computes the DFT in $O(N \log N)$ operations by exploiting symmetries in the DFT matrix.

For $N = 2^p$ (power of 2), the FFT recursively decomposes the DFT:



$$
G_m = \sum_{n=0}^{N/2-1} g_{2n} \, e^{-j2\pi m(2n)/N} + \sum_{n=0}^{N/2-1} g_{2n+1} \, e^{-j2\pi m(2n+1)/N} \tag{2.5-11}
$$





$$
G_m = G_m^{(\text{even})} + e^{-j2\pi m/N} G_m^{(\text{odd})} \tag{2.5-12}
$$



This decomposition reduces the problem to two DFTs of length $N/2$, applied recursively.

**Computational efficiency:**

| Method | Operations |
|--------|------------|
| Direct DFT | $N^2$ |
| FFT | $\frac{N}{2} \log_2 N$ |

For $N = 1024$: Direct = 1,048,576 operations; FFT = 5,120 operations (200× speedup).

2.5.5 Two-Dimensional DFT

For an $N \times M$ array of samples $g_{n,k}$:



$$
G_{m,l} = \sum_{n=0}^{N-1} \sum_{k=0}^{M-1} g_{n,k} \, e^{-j2\pi(mn/N + lk/M)} \tag{2.5-13}
$$



The 2D DFT is separable and can be computed as successive 1D transforms along rows and columns.

2.5.6 Practical Considerations

**Zero-padding**: Adding zeros to the input sequence increases the density of frequency samples without changing the underlying spectral content. This provides interpolation in the frequency domain but does not increase true resolution.

**Windowing**: To reduce spectral leakage from truncating an infinite signal, the data is often multiplied by a window function (Hamming, Hanning, Blackman, etc.) before computing the DFT.

**[Aliasing](/notes/areas/electrical_engineering/signals_systems/definitions/whittaker-shannon_sampling_theorem/)**: If the continuous signal is not properly band-limited before sampling, high-frequency components fold back into the computed spectrum (aliasing).

**Centering**: The DFT output places zero frequency at index 0. For visualization, the spectrum is often shifted so that zero frequency appears at the center (using fftshift operations).

⸻

2.6 Projection-Slice Theorem

The **Projection-Slice Theorem** (also called the Fourier Slice Theorem or Central Slice Theorem) establishes a fundamental relationship between projections of a function and slices of its Fourier transform.

2.6.1 Statement of the Theorem

Consider a two-dimensional function $g(x,y)$ with Fourier transform $G(f_X, f_Y)$.

A **projection** of $g$ onto the $x$-axis is:



$$
p_0(x) = \int_{-\infty}^{\infty} g(x, y) \, dy \tag{2.6-1}
$$



The one-dimensional Fourier transform of this projection is:



$$
P_0(f_X) = \int_{-\infty}^{\infty} p_0(x) \, e^{-j2\pi f_X x} \, dx \tag{2.6-2}
$$



**The theorem states:**



$$
P_0(f_X) = G(f_X, 0) \tag{2.6-3}
$$



That is, the 1D Fourier transform of the projection equals the 2D Fourier transform evaluated along the corresponding slice through the origin.

**Proof:**



$$
P_0(f_X) = \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} g(x,y) \, dy \right] e^{-j2\pi f_X x} \, dx
$$





$$
= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x,y) \, e^{-j2\pi f_X x} \, dx \, dy
$$





$$
= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x,y) \, e^{-j2\pi(f_X x + 0 \cdot y)} \, dx \, dy = G(f_X, 0) \tag{2.6-4}
$$



2.6.2 Projections at Arbitrary Angles

For a projection at angle $\theta$, define rotated coordinates:



$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} \tag{2.6-5}
$$



The projection at angle $\theta$:



$$
p_\theta(x') = \int_{-\infty}^{\infty} g(x' \cos\theta - y' \sin\theta, \, x' \sin\theta + y' \cos\theta) \, dy' \tag{2.6-6}
$$



By the rotation property of Fourier transforms, the generalized projection-slice theorem states:



$$
P_\theta(f) = G(f \cos\theta, \, f \sin\theta) \tag{2.6-7}
$$



The 1D transform of the projection at angle $\theta$ equals the 2D transform evaluated along a line through the origin at angle $\theta$.

2.6.3 Applications

**Computed Tomography (CT):**

In CT imaging, X-ray projections are measured at many angles around an object. Each projection provides a slice of the 2D Fourier transform. By measuring enough projections:

1. Collect projection data $p_\theta(x')$ for many angles $\theta$
2. Compute 1D Fourier transforms to obtain slices $G(f\cos\theta, f\sin\theta)$
3. Interpolate these radial slices onto a Cartesian grid
4. Apply 2D inverse Fourier transform to reconstruct $g(x,y)$

This is the basis for **filtered back-projection** algorithms used in medical CT scanners.

**Synthetic Aperture Radar (SAR):**

SAR systems exploit motion of the radar platform to synthesize a large aperture. The projection-slice theorem relates the radar returns to the ground scene through Fourier relationships.

**Electron Microscopy:**

Cryo-electron microscopy uses projections of molecular structures at different orientations. The projection-slice theorem enables 3D reconstruction of protein structures.

2.6.4 Three-Dimensional Extension

For a 3D function $g(x,y,z)$ with 3D Fourier transform $G(f_X, f_Y, f_Z)$:

A 2D projection (integral along the $z$-axis):



$$
p(x,y) = \int_{-\infty}^{\infty} g(x,y,z) \, dz \tag{2.6-8}
$$



Has 2D Fourier transform:



$$
P(f_X, f_Y) = G(f_X, f_Y, 0) \tag{2.6-9}
$$



The 2D transform of a planar projection equals a central slice of the 3D transform.

⸻

2.7 Phase Retrieval from Fourier Magnitude

In many physical measurements, only the magnitude (intensity) of a Fourier transform can be measured—the phase information is lost. **Phase retrieval** addresses the inverse problem of recovering a function from its Fourier magnitude alone.

2.7.1 The Phase Problem

Given measurements of $|G(f_X, f_Y)|^2$ (the power spectrum or intensity), can we recover $g(x,y)$?

The Fourier transform can be written:



$$
G(f_X, f_Y) = |G(f_X, f_Y)| e^{j\phi(f_X, f_Y)} \tag{2.7-1}
$$



where $\phi(f_X, f_Y)$ is the phase. Measuring only $|G|$ leaves $\phi$ unknown.

**Why phase matters:**

The phase of a Fourier transform carries crucial structural information about the function. Two functions with the same Fourier magnitude but different phases can look completely different. In fact, experiments show that swapping the phases of two images while keeping their magnitudes produces results that resemble the image whose phase was used—demonstrating that phase dominates structural appearance.

2.7.2 Uniqueness and Ambiguities

Without additional constraints, the phase problem is severely underdetermined. Known ambiguities include:

1. **Spatial shift**: If $g(x,y) \to G(f_X, f_Y)$, then $g(x-x_0, y-y_0) \to G(f_X, f_Y) e^{-j2\pi(f_X x_0 + f_Y y_0)}$
   - Shifting in space only changes the phase, not the magnitude

2. **Conjugate reflection**: $g^*(-x, -y)$ has the same Fourier magnitude as $g(x,y)$

3. **Global phase**: $g(x,y) e^{j\phi_0}$ has the same magnitude for any constant $\phi_0$

Under certain conditions, uniqueness can be established:
- **Finite support**: If $g(x,y)$ is known to be nonzero only within a finite region, and this region is "sufficiently small" relative to the sampling, the solution is unique (up to trivial ambiguities)
- **Oversampling**: Sampling the Fourier magnitude at twice the Nyquist rate provides additional constraints

2.7.3 Iterative Phase Retrieval Algorithms

**Gerchberg-Saxton Algorithm:**

For problems where both $|g(x,y)|$ and $|G(f_X, f_Y)|$ are known (e.g., in electron microscopy):

1. Start with initial guess $g^{(0)}(x,y)$ using known magnitude and random phase
2. Fourier transform: $G^{(k)} = \mathcal{F}\{g^{(k)}\}$
3. Replace magnitude with measured value: $G'^{(k)} = |G_{\text{measured}}| e^{j \arg(G^{(k)})}$
4. Inverse transform: $g'^{(k)} = \mathcal{F}^{-1}\{G'^{(k)}\}$
5. Replace magnitude with measured value: $g^{(k+1)} = |g_{\text{measured}}| e^{j \arg(g'^{(k)})}$
6. Repeat until convergence

**Fienup's Hybrid Input-Output (HIO) Algorithm:**

For problems with only the Fourier magnitude known, but with a support constraint (knowledge that $g = 0$ outside some region $S$):

1. Start with initial guess $g^{(0)}$
2. Fourier transform: $G^{(k)} = \mathcal{F}\{g^{(k)}\}$
3. Replace magnitude: $G'^{(k)} = |G_{\text{measured}}| e^{j \arg(G^{(k)})}$
4. Inverse transform: $g'^{(k)} = \mathcal{F}^{-1}\{G'^{(k)}\}$
5. Apply constraint:


$$
g^{(k+1)}(x,y) = \begin{cases} g'^{(k)}(x,y) & (x,y) \in S \text{ and } g'^{(k)} \text{ satisfies constraints} \\ g^{(k)}(x,y) - \beta g'^{(k)}(x,y) & \text{otherwise} \end{cases} \tag{2.7-2}
$$



where $\beta \approx 0.9$ is a feedback parameter.

6. Repeat until convergence

The HIO algorithm typically converges faster and more reliably than simple projection algorithms.

2.7.4 Applications

**X-ray Crystallography:**

Determining molecular structures from X-ray diffraction patterns. The diffraction pattern gives $|G|^2$, but phase information is lost. Techniques like molecular replacement, isomorphous replacement, and anomalous scattering help resolve the phase problem.

**Coherent Diffraction Imaging (CDI):**

Imaging nanoscale objects using coherent X-rays or electrons. By oversampling the diffraction pattern, iterative algorithms can recover the object's structure without lenses.

**Adaptive Optics:**

Wavefront sensing in astronomical telescopes and laser systems often involves phase retrieval from intensity measurements.

**Optical Coherence:**

Phase retrieval is fundamental to holography, interferometry, and coherence measurements in optical systems.

2.7.5 Recent Developments

Modern approaches to phase retrieval include:

- **Ptychography**: Scanning a probe across the sample and using overlapping measurements to provide redundancy
- **Compressed sensing**: Exploiting sparsity assumptions to reduce required measurements
- **Deep learning**: Neural networks trained to estimate phase from magnitude measurements
- **Convex relaxation**: Reformulating the problem as a semidefinite program (e.g., PhaseLift algorithm)
