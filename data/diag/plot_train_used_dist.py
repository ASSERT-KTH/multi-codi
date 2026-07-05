"""Training pool actually used (<=3072, 55483) vs cruxeval eval benchmark (800),
grouped-bar comparison across four axes. Shows training is harder/longer than eval.
Usage: python -m data.diag.plot_train_used_dist  (or run the file directly)
Source: data/diag/DISTRIBUTIONS.md (top tables = cruxeval, "训练实际使用的数据" = train-used).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# dataviz reference palette: slot1 blue (train-used) / slot2 aqua (cruxeval)
USED, CRUX = "#2a78d6", "#1baf7a"
INK, SEC, MUTED, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"

# each panel: (title, bins, train-used shares, cruxeval shares)
PANELS = [
    ("Num of Frames",
     ["2", "3", "4", "5-6", "7-10", "11-20", "21+"],
     [.036, .097, .103, .142, .150, .202, .269],
     [.106, .176, .135, .126, .158, .169, .130]),
    ("Num of Vars",
     ["1", "2", "3", "4", "5", "6+"],
     [.071, .128, .238, .259, .144, .160],
     [.144, .260, .289, .185, .088, .035]),
    ("Avg len of locals by token",
     ["0-7", "8-11", "12-15", "16-23", "24-31", "32+"],
     [.093, .132, .204, .387, .138, .045],
     [.133, .259, .243, .296, .054, .016]),
    ("Total len of trace by token",
     ["0-255", "256-511", "512-1023", "1024-2047", "2048-3071", "3072+"],
     [.336, .226, .231, .163, .044, .000],
     [.555, .209, .164, .048, .013, .012]),
]

fig, axes = plt.subplots(2, 2, figsize=(12, 8.2))
fig.patch.set_facecolor("white")

for ax, (title, bins, used, crux) in zip(axes.ravel(), PANELS):
    x = np.arange(len(bins))
    w = 0.40
    b1 = ax.bar(x - w / 2, used, w, color=USED, label="train-used <=3072 (55483)", zorder=3)
    b2 = ax.bar(x + w / 2, crux, w, color=CRUX, label="cruxeval eval (800)", zorder=3)

    for bars, vals, col in ((b1, used, USED), (b2, crux, CRUX)):
        for r, v in zip(bars, vals):
            txt = "0" if v == 0 else f"{v:.3f}".lstrip("0")
            ax.text(r.get_x() + r.get_width() / 2, v + 0.008, txt,
                    ha="center", va="bottom", fontsize=7.5, color=col, fontweight="bold")

    ax.set_title(title, fontsize=12.5, fontweight="bold", color=INK, pad=8, loc="left")
    ax.set_xticks(x)
    ax.set_xticklabels(bins, fontsize=9.5, color=SEC)
    ax.set_ylim(0, 0.6)
    ax.set_yticks(np.arange(0, 0.61, 0.1))
    ax.set_yticklabels([f"{t:.1f}".lstrip("0") or "0" for t in np.arange(0, 0.61, 0.1)],
                       fontsize=9, color=MUTED)
    ax.set_ylabel("within-source share", fontsize=9.5, color=SEC)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#c3c2b7")
    ax.tick_params(length=0)

axes[0, 0].legend(loc="upper right", fontsize=9.5, frameon=False)

fig.suptitle("Training pool actually used (55483)  vs  cruxeval eval benchmark (800)",
             fontsize=15, fontweight="bold", color=INK, x=0.01, ha="left", y=0.985)
fig.text(0.01, 0.945,
         "Training distribution is harder than eval: the pyx-dominated pool sits at more frames / "
         "more vars / longer locals & traces than cruxeval, which is short and narrow.",
         fontsize=10.5, color=SEC, ha="left")

fig.tight_layout(rect=[0, 0, 1, 0.93])
out = __file__.rsplit("/", 1)[0] + "/train_used_dist.png"
fig.savefig(out, dpi=160, facecolor="white", bbox_inches="tight")
print("wrote", out)
