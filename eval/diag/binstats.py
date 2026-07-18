"""Shared bin labeling/ordering for the offline stats_by_* scripts."""


def bin_label(edges, k):
    for lo, hi in zip(edges, edges[1:]):
        if lo <= k < hi:
            return f"{lo}-{hi - 1}" if hi - 1 > lo else f"{lo}"
    return f"{edges[-1]}+"


def order(lbl):
    return (1e9,) if lbl == "untraceable" else (int(lbl.split("-")[0].rstrip("+")),)
