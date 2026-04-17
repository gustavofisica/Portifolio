"""
notebook_style.py
-----------------
Custom matplotlib/seaborn theme matching the physics-to-ai-lab portfolio.
Usage:
    import sys; sys.path.append('../src')
    from notebook_style import apply_style, COLORS, PALETTE
    apply_style()
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

# ── Palette ───────────────────────────────────────────────────────────────────
COLORS = {
    "bg":       "#0e141b",
    "card":     "#1c232d",
    "primary":  "#2563eb",
    "light":    "#3b82f6",
    "accent":   "#60a5fa",
    "muted":    "#93c5fd",
    "neutral":  "#94a3b8",
    "text":     "#e2e8f0",
    "border":   "#1e3a5f",
    "success":  "#22c55e",
    "warning":  "#f59e0b",
    "danger":   "#ef4444",
}

PALETTE = [
    "#2563eb", "#3b82f6", "#60a5fa",
    "#93c5fd", "#22c55e", "#f59e0b",
    "#ef4444", "#a78bfa", "#34d399",
]

# ── Apply style ───────────────────────────────────────────────────────────────
def apply_style(figsize=(12, 5), base_size=11):
    mpl.rcParams.update({
        # Font settings
        "font.size":            base_size,
        "font.family":          "sans-serif",
        "text.color":           COLORS["text"],
        # Figure
        "figure.facecolor":     COLORS["card"],
        "figure.figsize":       figsize,
        "figure.dpi":           120,
        # Axes
        "axes.facecolor":       COLORS["bg"],
        "axes.edgecolor":       COLORS["border"],
        "axes.labelcolor":      COLORS["text"],
        "axes.labelsize":       base_size,
        "axes.titlesize":       base_size + 2,
        "axes.titlecolor":      COLORS["text"],
        "axes.titlepad":        12,
        "axes.grid":            True,
        "axes.spines.top":      False,
        "axes.spines.right":    False,
        # Grid
        "grid.color":           COLORS["border"],
        "grid.linewidth":       0.5,
        "grid.alpha":           0.4,
        # Ticks
        "xtick.color":          COLORS["neutral"],
        "ytick.color":          COLORS["neutral"],
        "xtick.labelsize":      base_size - 1,
        "ytick.labelsize":      base_size - 1,
        # Legend
        "legend.facecolor":     COLORS["card"],
        "legend.edgecolor":     COLORS["border"],
        "legend.labelcolor":    COLORS["text"],
        "legend.fontsize":      base_size - 1,
        # Lines
        "lines.linewidth":      2,
        "lines.markersize":     6,
        # Savefig
        "savefig.facecolor":    COLORS["card"],
        "savefig.bbox":         "tight",
        "savefig.dpi":          150,
    })

    try:
        import seaborn as sns
        sns.set_palette(PALETTE)
        sns.set_style("darkgrid", {
            "axes.facecolor":   COLORS["bg"],
            "figure.facecolor": COLORS["card"],
            "grid.color":       COLORS["border"],
        })
    except ImportError:
        pass

    plt.rcParams["axes.prop_cycle"] = mpl.cycler(color=PALETTE)
