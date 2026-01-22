import os
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.colors as mcolors

import numpy as np
from numba import njit

@njit(fastmath=True)
def compute_attractor(xs, ys, a, b, c, d):
    x, y = 0.1, 0.0
    for i in range(xs.shape[0]):
        xn = np.sin(a * y) + c * np.cos(a * x)
        yn = np.sin(b * x) + d * np.cos(b * y)
        x, y = xn, yn
        xs[i] = x
        ys[i] = y

def main():
    libertinus_math_path = os.path.expanduser('~/.local/share/fonts/LibertinusMath-Regular.otf')
    font_name = 'Libertinus Math'

    if os.path.exists(libertinus_math_path):
        try:
            fm.fontManager.addfont(libertinus_math_path)
            print(f"Registered font: {libertinus_math_path}")
            matplotlib.rcParams['font.family'] = [font_name, 'serif']
            matplotlib.rcParams['mathtext.fontset'] = 'custom'
            matplotlib.rcParams['mathtext.rm'] = font_name
            matplotlib.rcParams['mathtext.it'] = font_name
            matplotlib.rcParams['mathtext.bf'] = font_name
            print(f"Matplotlib configured to use '{font_name}' for equations.")
        except Exception as e:
            print(f"Error registering or configuring {font_name}: {e}")
            print("Falling back to 'serif' for equation text.")
            matplotlib.rcParams['font.family'] = ['serif']
            matplotlib.rcParams['mathtext.fontset'] = 'cm'
    else:
        print(f"Warning: {font_name} font not found at {libertinus_math_path}. Ensure it's installed or check the path.")
        print("Falling back to 'serif' for equation text.")
        matplotlib.rcParams['font.family'] = ['serif']
        matplotlib.rcParams['mathtext.fontset'] = 'cm'


    n_points = 300_000_000
    burn_in  =  10_000
    a, b, c, d = 1.8, -1.9, 1.0, 1.5

    xs = np.empty(n_points, dtype=np.float64)
    ys = np.empty(n_points, dtype=np.float64)

    t0 = time.perf_counter()
    compute_attractor(xs, ys, a, b, c, d)
    t1 = time.perf_counter()

    xs = xs[burn_in:]
    ys = ys[burn_in:]

    print(f"Computed {n_points} points in {t1 - t0:.2f} s.")
    print(f"x ∈ [{xs.min():.3f}, {xs.max():.3f}], y ∈ [{ys.min():.3f}, {ys.max():.3f}]")

    dark_bg = '#111111'
    fig = plt.figure(figsize=(12, 8), facecolor=dark_bg)
    ax  = fig.add_axes((0, 0, 1, 1), facecolor=dark_bg)
    x_min, x_max = -2.5, 2.5
    y_min, y_max = -2.5, 2.5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.axis('off')

    H, xedges, yedges = np.histogram2d(xs, ys, bins=2000, range=[[x_min, x_max], [y_min, y_max]])

    ax.imshow(
        H.T,
        origin='lower',
        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
        cmap='inferno',
        norm=mcolors.LogNorm(vmin=1),
        aspect='auto',
        interpolation='bilinear'
    )

    eq_text = (
        r"$x_{t+1} = \sin(%.1f y_t) + %.1f \cos(%.1f x_t)$" "\n"
        r"$y_{t+1} = \sin(%.1f x_t) + %.1f \cos(%.1f y_t)$"
    ) % (a, c, a, b, d, b)

    fig.text(
        0.01, 0.99, eq_text,
        color='#BF40BF',
        fontsize=16,
        va='top',
        ha='left',
        alpha=0.8
    )

    interval_text = (
        r"$x \in [%.3f, %.3f]$" "\n"
        r"$y \in [%.3f, %.3f]$"
    ) % (xs.min(), xs.max(), ys.min(), ys.max())

    fig.text(
        0.01, 0.92,
        interval_text,
        color='#BF40BF',
        fontsize=14,
        va='top',
        ha='left',
        alpha=0.8
    )

    outpath = 'clifford_attractor.png'

    plt.savefig(
        outpath,
        dpi=300,
        bbox_inches='tight',
        pad_inches=0,
        facecolor=fig.get_facecolor()
    )
    plt.close(fig)

if __name__ == '__main__':
    main()
