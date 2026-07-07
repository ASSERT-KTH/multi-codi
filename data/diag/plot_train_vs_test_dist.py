"""Train pool (codi_train_full, filter <=3072) vs CRUXEval-O test set (cruxeval_codi):
grouped-bar distribution comparison across four complexity axes, from per-sample RAW
values (data/diag/dist_raw.npz, built by extract_dist_raw.py).

Requirements this figure meets:
  1. paper-standard scientific styling (clean marks, recessive grid, direct labels);
  2. fine bins with the long tail kept SEGMENTED to each dataset's max (no "3072+"
     catch-all) -- so extreme test samples appear at their true location;
  3. every bar labelled with BOTH within-set share (%) and absolute count (n).
Run from codi_trace/:  python -m data.diag.plot_train_vs_test_dist
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# dataviz reference palette: categorical slot 1 (blue) / slot 2 (aqua), CVD-ordered.
TRAIN, TEST = "#2a78d6", "#1baf7a"
INK, SEC, MUTED, GRID, AXCOL = "#0b0b0b", "#52514e", "#898781", "#e4e3dc", "#c3c2b7"

INF = np.inf
# (title, axis-key, bin edges [half-open, last open], integer-label?)
PANELS = [
    ("Number of frames  (latent spans)", "frames",
     [1, 2, 3, 4, 5, 7, 11, 21, 41, 81, 161, INF], True),
    ("Number of local variables", "nvars",
     [1, 2, 3, 4, 5, 6, 7, 9, 13, INF], True),
    ("Avg length of locals per frame  (tokens)", "locals_len",
     [0, 8, 12, 16, 20, 24, 32, 48, 80, INF], False),
    ("Total trace length  (tokens)", "trace_len",
     [0, 256, 512, 1024, 1536, 2048, 3072, 4096, 6144, 8192, 12288, INF], False),
]


def resolve_edges(edges, top):
    """Replace the open-ended top bin (INF) with the data maximum, so the last
    interval carries an explicit upper bound instead of a '161+' catch-all."""
    return [top if x is INF else x for x in edges]


def labels_for(edges, is_int):
    out = []
    for lo, hi in zip(edges, edges[1:]):
        if is_int and hi - 1 == lo:
            out.append(f"{lo:g}")
        elif is_int:
            out.append(f"{lo:g}–{hi:g}" if hi == edges[-1] else f"{lo:g}–{hi - 1:g}")
        else:
            out.append(f"{lo:g}–{hi:g}")
    return out


def binned(vals, edges):
    e = np.array(edges, dtype=float)
    e[-1] += 1e-6  # np.histogram right edge is inclusive; keep the max in the last bin
    counts, _ = np.histogram(vals, bins=e)
    return counts, counts / counts.sum()


def main():
    d = np.load("data/diag/dist_raw.npz")
    fig, axes = plt.subplots(2, 2, figsize=(15.5, 9.6))
    fig.patch.set_facecolor("white")

    for ax, (title, key, edges, is_int) in zip(axes.ravel(), PANELS):
        tr = d["train_" + key].astype(float)
        te = d["crux_" + key].astype(float)
        if key == "nvars":  # drop re-trace failures (encoded as -1)
            tr, te = tr[tr >= 0], te[te >= 0]
        top = int(np.ceil(max(tr.max(), te.max())))  # explicit upper bound of the last bin
        edges_n = resolve_edges(edges, top)
        labels = labels_for(edges_n, is_int)
        c_tr, p_tr = binned(tr, edges_n)
        c_te, p_te = binned(te, edges_n)
        x = np.arange(len(labels))
        w = 0.42
        ymax = max(p_tr.max(), p_te.max())

        b1 = ax.bar(x - w / 2, p_tr, w, color=TRAIN, zorder=3,
                    label=f"Train pool  ≤ 3072 tok   (n = {len(tr):,})")
        b2 = ax.bar(x + w / 2, p_te, w, color=TEST, zorder=3,
                    label=f"CRUXEval-O test set   (n = {len(te):,})")

        for bars, props, cnts, col in ((b1, p_tr, c_tr, TRAIN), (b2, p_te, c_te, TEST)):
            for r, p, c in zip(bars, props, cnts):
                if c == 0:
                    continue
                pct = f"{p * 100:.1f}%" if p >= 0.001 else "<0.1%"
                ax.text(r.get_x() + r.get_width() / 2, p + ymax * 0.015,
                        f"{pct}\nn={c:,}", ha="center", va="bottom", rotation=90,
                        fontsize=6.3, color=col, linespacing=0.95)

        ax.set_title(title, fontsize=13, fontweight="bold", color=INK, pad=7, loc="left")
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=8.8, color=SEC,
                           rotation=32 if len(labels) > 9 else 0, ha="right" if len(labels) > 9 else "center")
        ax.set_ylim(0, ymax * 1.42)
        ax.set_ylabel("within-set share", fontsize=9.8, color=SEC)
        ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
        ax.tick_params(axis="y", labelsize=8.5, labelcolor=MUTED)
        ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
        ax.set_axisbelow(True)
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.spines["bottom"].set_color(AXCOL)
        ax.tick_params(length=0)
        ax.legend(loc="upper right", fontsize=9, frameon=False)

    fig.suptitle("Training pool vs CRUXEval-O test set — trace-complexity distributions",
                 fontsize=16.5, fontweight="bold", color=INK, x=0.008, ha="left", y=0.99)
    fig.text(0.008, 0.952,
             "Bars = within-set share; each bar also labelled with its absolute count (n). "
             "Bins stay fine and the tail is kept segmented to each set's maximum — note the "
             "test set's trace-length tail out to ≈28k tokens that the ≤3072-filtered training pool lacks.",
             fontsize=10.3, color=SEC, ha="left")

    fig.tight_layout(rect=[0, 0, 1, 0.935])
    for ext in ("png", "pdf"):
        out = f"data/diag/train_vs_test_dist.{ext}"
        fig.savefig(out, dpi=170, facecolor="white", bbox_inches="tight")
        print("wrote", out)


if __name__ == "__main__":
    main()
