#!/usr/bin/env python3
"""
Generate all charts for "Something Big Already Happened" book.
Uses design system colors from _brand.yml for consistent dark-theme visuals.
Outputs PNG @300dpi and PDF for each chart.
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime

# ---------------------------------------------------------------------------
# Design system tokens
# ---------------------------------------------------------------------------
BG_PRIMARY = "#0D0D1A"
BG_SECONDARY = "#1A1A2E"
BG_CARD = "#16213E"
ACCENT = "#FF6B35"
ACCENT2 = "#6366F1"
TEXT_PRIMARY = "#E8E8F0"
TEXT_SECONDARY = "#9CA3AF"
TEXT_MUTED = "#6B7280"
BORDER = "#2D2D44"

STATUS_COLORS = {
    "Confirmed": "#22C55E",
    "Confirmed and accelerating": "#22C55E",
    "On track": "#22C55E",
    "Partially realized": ACCENT,
    "Realized": "#22C55E",
    "In progress": ACCENT,
    "Early signs": "#FACC15",
    "Early progress": "#FACC15",
    "Too early": TEXT_MUTED,
    "Too early to assess": TEXT_MUTED,
    "Very early": TEXT_MUTED,
}

ORG_COLORS = {
    "Anthropic": ACCENT,
    "OpenAI": "#22C55E",
    "Google DeepMind": "#3B82F6",
    "Meta": "#8B5CF6",
    "DeepSeek": "#EC4899",
    "Cognition": "#14B8A6",
    "ByteDance": "#F97316",
}

FONT_FAMILY = "DejaVu Sans"

# ---------------------------------------------------------------------------
# Print mode: --print flag produces grayscale-safe, white-bg charts
# ---------------------------------------------------------------------------
PRINT_MODE = "--print" in sys.argv

if PRINT_MODE:
    BG_PRIMARY = "#FFFFFF"
    BG_SECONDARY = "#F5F5F5"
    BG_CARD = "#FFFFFF"
    ACCENT = "#333333"
    ACCENT2 = "#777777"
    TEXT_PRIMARY = "#000000"
    TEXT_SECONDARY = "#444444"
    TEXT_MUTED = "#888888"
    BORDER = "#CCCCCC"

    STATUS_COLORS = {
        "Confirmed": "#222222",
        "Confirmed and accelerating": "#222222",
        "On track": "#222222",
        "Partially realized": "#555555",
        "Realized": "#222222",
        "In progress": "#555555",
        "Early signs": "#888888",
        "Early progress": "#888888",
        "Too early": "#BBBBBB",
        "Too early to assess": "#BBBBBB",
        "Very early": "#BBBBBB",
    }

    ORG_COLORS = {
        "Anthropic": "#000000",
        "OpenAI": "#444444",
        "Google DeepMind": "#777777",
        "Meta": "#999999",
        "DeepSeek": "#BBBBBB",
        "Cognition": "#555555",
        "ByteDance": "#333333",
    }

# ---------------------------------------------------------------------------
# Print mode helpers
# ---------------------------------------------------------------------------
EDGE_COLOR = "white" if not PRINT_MODE else "black"

ORG_MARKERS = {
    "Anthropic": "o",
    "OpenAI": "s",
    "Google DeepMind": "^",
    "Meta": "D",
    "DeepSeek": "v",
    "Cognition": "P",
    "ByteDance": "X",
}

STATUS_HATCHES = {
    "Confirmed": "",
    "Confirmed and accelerating": "",
    "On track": "",
    "Partially realized": "//",
    "Realized": "",
    "In progress": "//",
    "Early signs": "xx",
    "Early progress": "xx",
    "Too early": "..",
    "Too early to assess": "..",
    "Very early": "..",
}

BOTTLENECK_HATCHES = {"Computational": "", "Mixed": "//", "Physical": ".."}
INVEST_HATCHES = {"Announced": "", "Committed": "//", "Raised": "xx"}

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
if PRINT_MODE:
    OUT_DIR = os.path.join(ROOT, "images", "generated", "print")
else:
    OUT_DIR = os.path.join(ROOT, "images", "generated")
os.makedirs(OUT_DIR, exist_ok=True)


def apply_style():
    """Set global matplotlib style. Uses print-safe colors when --print is passed."""
    plt.rcParams.update({
        "figure.facecolor": BG_PRIMARY,
        "axes.facecolor": BG_CARD,
        "axes.edgecolor": BORDER,
        "axes.labelcolor": TEXT_PRIMARY,
        "axes.titlesize": 14,
        "axes.labelsize": 11,
        "axes.grid": True,
        "grid.color": BORDER,
        "grid.alpha": 0.5 if not PRINT_MODE else 0.3,
        "grid.linewidth": 0.75,
        "xtick.color": TEXT_SECONDARY,
        "ytick.color": TEXT_SECONDARY,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "text.color": TEXT_PRIMARY,
        "font.family": "sans-serif",
        "font.sans-serif": [FONT_FAMILY],
        "legend.facecolor": BG_SECONDARY,
        "legend.edgecolor": BORDER,
        "legend.fontsize": 9,
        "legend.labelcolor": TEXT_PRIMARY,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.facecolor": BG_PRIMARY,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.3,
        "axes.linewidth": 0.75,
        "lines.linewidth": 2.0,
    })


def save(fig, name):
    """Save figure as PNG and PDF."""
    png_path = os.path.join(OUT_DIR, f"{name}.png")
    pdf_path = os.path.join(OUT_DIR, f"{name}.pdf")
    fig.savefig(png_path)
    fig.savefig(pdf_path)
    plt.close(fig)
    print(f"  Saved {png_path}")
    print(f"  Saved {pdf_path}")


def parse_date_col(series):
    """Parse a date column that may have YYYY or YYYY-MM or YYYY-MM-DD formats."""
    dates = []
    for val in series:
        val = str(val).strip()
        if len(val) == 4:
            dates.append(pd.Timestamp(f"{val}-07-01"))
        elif len(val) == 7:
            dates.append(pd.Timestamp(f"{val}-15"))
        else:
            dates.append(pd.Timestamp(val))
    return dates


# ===========================================================================
# Chart 1: SWE-bench Timeline
# ===========================================================================
def chart_swe_bench():
    print("Generating swe-bench-timeline...")
    df = pd.read_csv(os.path.join(DATA_DIR, "swe-bench.csv"))
    df["dt"] = parse_date_col(df["date"])
    df = df.sort_values("dt")

    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Plot line
    ax.plot(df["dt"], df["score_pct"], color=ACCENT, linewidth=2, zorder=3)
    ax.fill_between(df["dt"], df["score_pct"], alpha=0.10, color=ACCENT, zorder=2)

    # Scatter points colored by org (use distinct markers in print mode)
    for _, row in df.iterrows():
        color = ORG_COLORS.get(row["organization"], TEXT_MUTED)
        marker = ORG_MARKERS.get(row["organization"], "o") if PRINT_MODE else "o"
        ax.scatter(row["dt"], row["score_pct"], color=color, s=40, zorder=4,
                   marker=marker, edgecolors=EDGE_COLOR, linewidths=0.4)

    # Annotate key models
    annotations = {
        "GPT-4 (RAG baseline)": ("right", (15, -10)),
        "Claude 3.5 Sonnet": ("right", (10, 8)),
        "o3": ("left", (-12, 8)),
        "Claude Opus 4.6 (Thinking)": ("left", (-12, -14)),
    }
    for _, row in df.iterrows():
        if row["model"] in annotations:
            ha, xytext = annotations[row["model"]]
            ax.annotate(
                row["model"], (row["dt"], row["score_pct"]),
                textcoords="offset points", xytext=xytext,
                fontsize=8, color=TEXT_PRIMARY, ha=ha,
                arrowprops=dict(arrowstyle="-", color=TEXT_MUTED, lw=0.6),
            )

    ax.set_title("SWE-bench Verified Score Progression", fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Score (%)")
    ax.set_xlabel("")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    fig.autofmt_xdate(rotation=30)
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter())

    # Legend for organizations
    handles = [Line2D([0], [0], marker=ORG_MARKERS.get(org, "o") if PRINT_MODE else "o",
                       color="w", markerfacecolor=c, markersize=7, label=org)
               for org, c in ORG_COLORS.items() if org in df["organization"].values]
    handles.append(Line2D([0], [0], marker="o", color="w", markerfacecolor=TEXT_MUTED,
                          markersize=7, label="Other"))
    ax.legend(handles=handles, loc="upper left", framealpha=0.8)

    save(fig, "swe-bench-timeline")


# ===========================================================================
# Chart 2: METR Autonomous Hours (Exponential)
# ===========================================================================
def chart_metr():
    print("Generating metr-exponential...")
    df = pd.read_csv(os.path.join(DATA_DIR, "metr-benchmarks.csv"))

    # Only plot measured/estimated data, not projections
    df = df[df["measurement_type"].isin(["measured", "estimated", "estimated_from_trend",
                                          "estimated_above_GPT4o_below_Claude37",
                                          "estimated_from_1.8x_Claude37",
                                          "projected_latest_frontier"])]
    df["dt"] = parse_date_col(df["date"])
    df = df.sort_values("dt")

    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Color measured vs estimated differently
    for _, row in df.iterrows():
        if "measured" in row["measurement_type"]:
            color = ACCENT
            marker = "o"
        elif row["measurement_type"] == "projected_latest_frontier":
            color = ACCENT2
            marker = "D"
        else:
            color = TEXT_SECONDARY
            marker = "s"
        ax.scatter(row["dt"], row["autonomous_hours"], color=color, s=60,
                   marker=marker, zorder=4, edgecolors=EDGE_COLOR, linewidths=0.5)

    # Connect with line
    ax.plot(df["dt"], df["autonomous_hours"], color=ACCENT, linewidth=1.5,
            alpha=0.6, zorder=3, linestyle="--")

    ax.set_yscale("log")
    ax.set_title("METR Autonomous Task Duration (Log Scale)", fontsize=14,
                 fontweight="bold", pad=12)
    ax.set_ylabel("Hours (log scale)")
    ax.set_xlabel("")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    fig.autofmt_xdate(rotation=30)

    # Annotate doubling period
    ax.annotate("~7-month doubling period", xy=(0.5, 0.92), xycoords="axes fraction",
                fontsize=10, color=ACCENT, ha="center", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_SECONDARY, edgecolor=ACCENT, alpha=0.9))

    # Annotate selected models
    label_models = ["Claude 3.5 Sonnet", "Claude Opus 4.5", "GPT-5"]
    for _, row in df.iterrows():
        if row["model_or_period"] in label_models:
            ax.annotate(
                f'{row["model_or_period"]}\n({row["autonomous_hours"]:.1f}h)',
                (row["dt"], row["autonomous_hours"]),
                textcoords="offset points", xytext=(12, 5),
                fontsize=7.5, color=TEXT_PRIMARY,
                arrowprops=dict(arrowstyle="-", color=TEXT_MUTED, lw=0.5),
            )

    # Y-axis formatting
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(
        lambda x, _: f"{x:.0f}h" if x >= 1 else f"{x*60:.0f}m"))

    # Legend
    handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor=ACCENT, markersize=8, label="Measured"),
        Line2D([0], [0], marker="s", color="w", markerfacecolor=TEXT_SECONDARY, markersize=8, label="Estimated"),
        Line2D([0], [0], marker="D", color="w", markerfacecolor=ACCENT2, markersize=8, label="Latest frontier"),
    ]
    ax.legend(handles=handles, loc="upper left", framealpha=0.8)

    save(fig, "metr-exponential")


# ===========================================================================
# Chart 3: Model Releases Timeline
# ===========================================================================
def chart_model_releases():
    print("Generating model-releases-timeline...")
    df = pd.read_csv(os.path.join(DATA_DIR, "model-releases.csv"))
    df["dt"] = parse_date_col(df["date"])
    df = df.sort_values("dt")

    fig, ax = plt.subplots(figsize=(11, 5))

    # Y = organization row, jitter within
    orgs = df["organization"].unique()
    org_y = {org: i for i, org in enumerate(orgs)}

    for _, row in df.iterrows():
        color = ORG_COLORS.get(row["organization"], TEXT_MUTED)
        y = org_y[row["organization"]]
        ax.scatter(row["dt"], y, color=color, s=80, zorder=4,
                   edgecolors=EDGE_COLOR, linewidths=0.5, alpha=0.9)

    ax.set_yticks(range(len(orgs)))
    ax.set_yticklabels(orgs, fontsize=9)
    ax.set_title("AI Model Releases Timeline (2024 - Feb 2026)", fontsize=14,
                 fontweight="bold", pad=12)
    ax.set_xlabel("")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    fig.autofmt_xdate(rotation=30)
    ax.set_ylim(-0.5, len(orgs) - 0.5)
    ax.invert_yaxis()

    # Add subtle horizontal lines
    for i in range(len(orgs)):
        ax.axhline(i, color=BORDER, linewidth=0.5, alpha=0.5, zorder=1)

    # Density annotation
    # Count releases per quarter
    df["quarter"] = df["dt"].dt.to_period("Q")
    counts = df.groupby("quarter").size()
    peak_q = counts.idxmax()
    ax.annotate(f"Peak: {counts.max()} releases in {peak_q}",
                xy=(0.98, 0.02), xycoords="axes fraction",
                fontsize=9, color=TEXT_SECONDARY, ha="right",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=BG_SECONDARY,
                          edgecolor=BORDER, alpha=0.9))

    save(fig, "model-releases-timeline")


# ===========================================================================
# Chart 4: Prediction Scorecard
# ===========================================================================
def chart_prediction_scorecard():
    print("Generating prediction-scorecard...")
    df = pd.read_csv(os.path.join(DATA_DIR, "prediction-scorecard.csv"))

    # Truncate long prediction text
    df["label"] = df["prediction"].str[:65] + df["prediction"].str[65:].apply(
        lambda x: "..." if len(x) > 0 else "")

    df = df.sort_values("realization_pct", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 8))

    bars = ax.barh(range(len(df)), df["realization_pct"], height=0.7, zorder=3)

    # Color bars by status (add hatching in print mode)
    for bar, (_, row) in zip(bars, df.iterrows()):
        color = STATUS_COLORS.get(row["status_feb_2026"], TEXT_MUTED)
        bar.set_color(color)
        bar.set_alpha(0.85)
        if PRINT_MODE:
            bar.set_hatch(STATUS_HATCHES.get(row["status_feb_2026"], ""))
            bar.set_edgecolor("#333333")

    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(df["label"], fontsize=7.5)
    ax.set_xlabel("Realization (%)")
    ax.set_title("Prediction Scorecard: How Much Has Come True?",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xlim(0, 100)
    ax.xaxis.set_major_formatter(mticker.PercentFormatter())

    # Add percentage labels on bars
    for i, (_, row) in enumerate(df.iterrows()):
        ax.text(row["realization_pct"] + 1.5, i, f'{row["realization_pct"]}%',
                va="center", fontsize=8, color=TEXT_PRIMARY)

    # Legend for statuses
    unique_statuses = df["status_feb_2026"].unique()
    handles = [mpatches.Patch(color=STATUS_COLORS.get(s, TEXT_MUTED), label=s, alpha=0.85)
               for s in unique_statuses]
    ax.legend(handles=handles, loc="lower right", framealpha=0.8, fontsize=8)

    fig.subplots_adjust(left=0.42)
    save(fig, "prediction-scorecard")


# ===========================================================================
# Chart 5: Job Displacement Events
# ===========================================================================
def chart_job_displacement():
    print("Generating job-displacement...")
    # Curated job displacement data from ai-timeline.csv and prediction-scorecard.csv
    events = [
        ("Tech layoffs 2024\n(industry-wide)", 152000, "2024"),
        ("AI-cited job cuts 2025", 55000, "2025"),
        ("Total tech layoffs 2024-2025\n(AI a growing factor)", 276000, "2024-2025"),
        ("5M white-collar jobs\nat risk (Microsoft Research)", 5000000, "Projected"),
    ]

    labels = [e[0] for e in events[:3]]  # Exclude projected for main bars
    values = [e[1] for e in events[:3]]

    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Main bars for actual events
    bars = ax.barh(range(len(labels)), values, height=0.55, zorder=3, color=ACCENT, alpha=0.85)

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=9)

    # Add count labels
    for i, val in enumerate(values):
        ax.text(val + max(values) * 0.02, i,
                f'{val:,}', va="center", fontsize=9, color=TEXT_PRIMARY)

    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1000:.0f}K"))

    ax.set_title("AI-Related Job Displacement (2024 - Early 2026)", fontsize=14,
                 fontweight="bold", pad=12)
    ax.set_xlabel("Workers Affected")

    # Add context annotations below the chart
    context_lines = [
        "Amodei: 50% of entry-level white-collar jobs at risk in 1-5 years",
        "Microsoft Research: 5M white-collar jobs facing extinction",
        "Worker AI concern: 28% (2024) \u2192 40% (2026)",
    ]
    for i, line in enumerate(context_lines):
        ax.annotate(line, xy=(0.02, -0.18 - i * 0.08), xycoords="axes fraction",
                    fontsize=8, color=TEXT_SECONDARY, ha="left")

    fig.subplots_adjust(left=0.28, bottom=0.32)
    save(fig, "job-displacement")


# ===========================================================================
# Chart 6: AI Investment Figures
# ===========================================================================
def chart_ai_investment():
    print("Generating ai-investment...")
    # Investment data extracted from timeline + scorecard
    investments = [
        ("Stargate\n(SoftBank/OpenAI/Oracle)", 500, "Announced"),
        ("Google\n(planned)", 100, "Announced"),
        ("Microsoft\n(2025 capex)", 80, "Committed"),
        ("Amazon\n(2025 capex)", 75, "Committed"),
        ("Meta\n(2025 capex)", 65, "Committed"),
        ("NVIDIA\n(2025 capex est.)", 50, "Committed"),
        ("Anthropic\nSeries F ($13B)", 13, "Raised"),
        ("Anthropic\n(MS+NVIDIA $15B)", 15, "Raised"),
        ("OpenAI\n$40B round", 40, "Raised"),
    ]

    labels = [x[0] for x in investments]
    values = [x[1] for x in investments]
    categories = [x[2] for x in investments]

    cat_colors = {"Announced": ACCENT, "Committed": ACCENT2, "Raised": "#22C55E"}

    fig, ax = plt.subplots(figsize=(10, 5.5))

    bars = ax.barh(range(len(labels)), values, height=0.65, zorder=3)
    for bar, cat in zip(bars, categories):
        bar.set_color(cat_colors[cat])
        bar.set_alpha(0.85)
        if PRINT_MODE:
            bar.set_hatch(INVEST_HATCHES.get(cat, ""))
            bar.set_edgecolor("#333333")

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlabel("Billions USD")
    ax.set_title("Major AI Investments (2025 - Early 2026)", fontsize=14,
                 fontweight="bold", pad=12)

    # Add value labels
    for i, val in enumerate(values):
        ax.text(val + 5, i, f"${val}B", va="center", fontsize=9, color=TEXT_PRIMARY)

    # Legend
    handles = [mpatches.Patch(color=c, label=l, alpha=0.85) for l, c in cat_colors.items()]
    ax.legend(handles=handles, loc="lower right", framealpha=0.8)

    ax.set_xlim(0, max(values) * 1.15)
    fig.subplots_adjust(left=0.22)
    save(fig, "ai-investment")


# ===========================================================================
# Chart 7: AI Timeline (Vertical)
# ===========================================================================
def chart_ai_timeline():
    print("Generating ai-timeline...")
    df = pd.read_csv(os.path.join(DATA_DIR, "ai-timeline.csv"))
    df["dt"] = parse_date_col(df["date"])
    df = df.sort_values("dt")

    # Filter to key events (High significance only) to keep chart readable
    df = df[df["significance"] == "High"].reset_index(drop=True)

    # Category colors
    cat_colors = {
        "model_release": ACCENT,
        "benchmark": ACCENT2,
        "funding": "#22C55E",
        "industry": "#FACC15",
        "policy": "#3B82F6",
        "safety": "#EC4899",
        "research": "#14B8A6",
    }

    fig, ax = plt.subplots(figsize=(10, 18))

    # Draw the central vertical spine
    y_positions = range(len(df))
    ax.vlines(x=0, ymin=-0.5, ymax=len(df) - 0.5, color=BORDER, linewidth=2, zorder=1)

    for i, (_, row) in enumerate(df.iterrows()):
        color = cat_colors.get(row["category"], TEXT_MUTED)
        side = 1 if i % 2 == 0 else -1  # Alternate left/right

        # Horizontal connector line
        ax.hlines(y=i, xmin=0, xmax=side * 0.15, color=color, linewidth=1.5, zorder=2)

        # Glowing dot on the spine
        ax.scatter(0, i, color=color, s=50, zorder=4, edgecolors=EDGE_COLOR, linewidths=0.5)

        # Date label on the spine side opposite to the text
        date_str = row["dt"].strftime("%b %Y") if hasattr(row["dt"], "strftime") else str(row["date"])
        ax.text(-side * 0.04, i, date_str, fontsize=7, color=TEXT_MUTED,
                ha="right" if side > 0 else "left", va="center")

        # Event text on the connector side
        event_text = row["event"]
        # Wrap long text
        if len(event_text) > 45:
            midpoint = event_text.rfind(" ", 0, 45)
            if midpoint > 0:
                event_text = event_text[:midpoint] + "\n" + event_text[midpoint + 1:]

        ax.text(side * 0.18, i, event_text, fontsize=7.5, color=TEXT_PRIMARY,
                ha="left" if side > 0 else "right", va="center",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=BG_SECONDARY,
                          edgecolor=color, alpha=0.85, linewidth=0.8))

    ax.set_title("AI Predictions & Events Timeline\nJanuary 2024 \u2013 February 2026",
                 fontsize=14, fontweight="bold", pad=16)

    # Remove axes chrome
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(len(df) - 0.5, -0.5)  # Chronological top-to-bottom
    ax.axis("off")

    # Legend for categories
    handles = [mpatches.Patch(color=c, label=cat.replace("_", " ").title(), alpha=0.85)
               for cat, c in cat_colors.items()]
    ax.legend(handles=handles, loc="lower center", framealpha=0.8, fontsize=8,
              ncol=4, bbox_to_anchor=(0.5, -0.02))

    fig.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.04)
    save(fig, "ai-timeline")


# ===========================================================================
# Chart 8: Recursive Improvement Loop (Model Release Acceleration)
# ===========================================================================
def chart_recursive_loop():
    print("Generating recursive-loop...")
    df = pd.read_csv(os.path.join(DATA_DIR, "model-releases.csv"))
    df["dt"] = parse_date_col(df["date"])
    df = df.sort_values("dt")

    # Focus on OpenAI GPT-5 family to show the compression
    gpt5_family = df[df["model_name"].str.contains("GPT-5", na=False)].copy()
    gpt5_family = gpt5_family.sort_values("dt").reset_index(drop=True)

    # Also pull Anthropic Claude 4 family for comparison
    claude4_family = df[df["model_name"].str.contains("Claude.*4", na=False)].copy()
    claude4_family = claude4_family.sort_values("dt").reset_index(drop=True)

    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(10, 9),
                                          gridspec_kw={"height_ratios": [3, 2]})

    # --- Top panel: Days between successive releases within each family ---
    families = [
        ("OpenAI GPT-5 Family", gpt5_family, ACCENT),
        ("Anthropic Claude 4 Family", claude4_family, ACCENT2),
    ]

    bar_width = 0.35
    max_gap = 0

    for idx, (label, fam, color) in enumerate(families):
        if len(fam) < 2:
            continue
        gaps = []
        labels = []
        for i in range(1, len(fam)):
            prev_name = fam.iloc[i - 1]["model_name"]
            curr_name = fam.iloc[i]["model_name"]
            delta_days = (fam.iloc[i]["dt"] - fam.iloc[i - 1]["dt"]).days
            # Shorten names for readability
            short_prev = prev_name.split(",")[0].strip()
            short_curr = curr_name.split(",")[0].strip()
            labels.append(f"{short_prev}\n\u2192 {short_curr}")
            gaps.append(delta_days)

        x = np.arange(len(gaps))
        offset = (idx - 0.5) * bar_width
        bars = ax_top.bar(x + offset, gaps, bar_width, color=color, alpha=0.85,
                          zorder=3, label=label)

        # Value labels on bars
        for bar, val in zip(bars, gaps):
            ax_top.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3,
                        f"{val}d", ha="center", va="bottom", fontsize=8,
                        color=TEXT_PRIMARY, fontweight="bold")

        if gaps:
            max_gap = max(max_gap, max(gaps))

        # Use OpenAI labels as the x-tick labels (they have the most releases)
        if idx == 0:
            ax_top.set_xticks(x)
            ax_top.set_xticklabels(labels, fontsize=7.5)

    ax_top.set_ylabel("Days Between Releases")
    ax_top.set_title("The Recursive Loop: Accelerating Model Release Cadence",
                     fontsize=14, fontweight="bold", pad=12)
    ax_top.set_ylim(0, max_gap * 1.25)
    ax_top.legend(loc="upper right", framealpha=0.8)

    # Add annotation about the compression
    ax_top.annotate(
        "GPT-5 \u2192 GPT-5.3-Codex: 4 releases in ~6 months\n"
        "GPT-5.3-Codex was instrumental in creating itself",
        xy=(0.02, 0.95), xycoords="axes fraction",
        fontsize=9, color=ACCENT, ha="left", va="top",
        bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_SECONDARY,
                  edgecolor=ACCENT, alpha=0.9, linewidth=0.8))

    # --- Bottom panel: Cumulative model releases over time (all orgs) ---
    df_sorted = df.sort_values("dt")
    df_sorted["cumcount"] = range(1, len(df_sorted) + 1)

    ax_bot.fill_between(df_sorted["dt"], df_sorted["cumcount"], alpha=0.10,
                        color=ACCENT, zorder=2)
    ax_bot.plot(df_sorted["dt"], df_sorted["cumcount"], color=ACCENT,
                linewidth=2, zorder=3)

    # Color points by org
    for _, row in df_sorted.iterrows():
        color = ORG_COLORS.get(row["organization"], TEXT_MUTED)
        ax_bot.scatter(row["dt"], row["cumcount"], color=color, s=30, zorder=4,
                       edgecolors=EDGE_COLOR, linewidths=0.4)

    ax_bot.set_ylabel("Cumulative Frontier Releases")
    ax_bot.set_xlabel("")
    ax_bot.set_title("Accelerating Pace of Frontier Model Releases",
                     fontsize=12, fontweight="bold", pad=10)
    ax_bot.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax_bot.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    fig.autofmt_xdate(rotation=30)

    # Org legend for bottom panel
    handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                       markersize=7, label=org)
               for org, c in ORG_COLORS.items() if org in df["organization"].values]
    ax_bot.legend(handles=handles, loc="upper left", framealpha=0.8, fontsize=8)

    fig.tight_layout(h_pad=3.0)
    save(fig, "recursive-loop")


# ===========================================================================
# Chart 9: November Revolution Timeline
# ===========================================================================
def chart_november_revolution():
    print("Generating november-revolution-timeline...")

    events = [
        (datetime(2025, 11, 17), "Grok 4.1", "xAI", "#EC4899"),
        (datetime(2025, 11, 18), "Gemini 3.0", "Google", ACCENT2),
        (datetime(2025, 11, 24), "Claude Opus 4.5", "Anthropic", ACCENT),
        (datetime(2025, 12, 4), "Gemini 3 Deep Think", "Google", ACCENT2),
        (datetime(2025, 12, 11), "GPT-5.2", "OpenAI", "#10B981"),
    ]

    fig, ax = plt.subplots(figsize=(12, 4))

    # Draw horizontal timeline spine
    dates = [e[0] for e in events]
    min_date = min(dates) - pd.Timedelta(days=3)
    max_date = max(dates) + pd.Timedelta(days=3)
    ax.hlines(y=0, xmin=min_date, xmax=max_date, color=BORDER, linewidth=3, zorder=1)

    # Alternate above/below placement
    y_offsets = [1.2, -1.2, 1.2, -1.2, 1.2]

    for i, (date, model, org, color) in enumerate(events):
        y_off = y_offsets[i]

        # Glowing dot on spine
        ax.scatter(date, 0, color=color, s=120, zorder=4,
                   edgecolors=EDGE_COLOR, linewidths=0.8)

        # Vertical connector
        ax.vlines(x=date, ymin=0, ymax=y_off * 0.7, color=color, linewidth=1.5,
                  zorder=2, linestyle="-")

        # Model label
        ax.text(date, y_off, f"{model}\n({org})",
                fontsize=10, fontweight="bold", color=TEXT_PRIMARY,
                ha="center", va="center" if y_off > 0 else "center",
                bbox=dict(boxstyle="round,pad=0.5", facecolor=BG_SECONDARY,
                          edgecolor=color, alpha=0.95, linewidth=1.5))

        # Date below/above the dot
        date_y = -0.35 if y_off > 0 else 0.35
        ax.text(date, date_y, date.strftime("%b %d"),
                fontsize=9, color=TEXT_SECONDARY, ha="center",
                va="top" if y_off > 0 else "bottom")

    ax.set_title("The November Revolution: 5 Frontier Models in 24 Days",
                 fontsize=14, fontweight="bold", pad=16)

    ax.set_xlim(min_date, max_date)
    ax.set_ylim(-2.2, 2.2)
    ax.axis("off")

    # Legend
    handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#EC4899",
               markersize=10, label="xAI"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor=ACCENT2,
               markersize=10, label="Google"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor=ACCENT,
               markersize=10, label="Anthropic"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#10B981",
               markersize=10, label="OpenAI"),
    ]
    ax.legend(handles=handles, loc="lower center", framealpha=0.8, fontsize=9,
              ncol=4, bbox_to_anchor=(0.5, -0.08))

    fig.subplots_adjust(bottom=0.15, top=0.85)
    save(fig, "november-revolution-timeline")


# ===========================================================================
# Chart 10: Five Levels of AI Coding
# ===========================================================================
def chart_five_levels():
    print("Generating five-levels...")

    levels = [
        ("Level 0", "Manual Coding\n(pre-AI)", 0),
        ("Level 1", "AI Assisted\nSpicy Autocomplete", 1),
        ("Level 2", "AI Pairing\n(~90% of devs here)", 2),
        ("Level 3", "Code Reviewer\n(transition point)", 3),
        ("Level 4", "PM Mode\n(spec \u2192 wait 12hrs \u2192 review)", 4),
        ("Level 5", "Dark Factory\n(no human sees code)", 5),
    ]

    fig, ax = plt.subplots(figsize=(12, 6))

    # Create stepped horizontal bars with increasing width to suggest progression
    n = len(levels)
    bar_widths = [2 + i * 1.8 for i in range(n)]
    y_positions = list(range(n - 1, -1, -1))  # Reverse so Level 0 is at bottom

    # Color gradient from muted to accent
    colors = [TEXT_MUTED, TEXT_SECONDARY, ACCENT2, ACCENT, "#10B981", "#22C55E"]

    for i, (label, desc, level) in enumerate(levels):
        y = y_positions[i]
        width = bar_widths[i]
        bar = ax.barh(y, width, height=0.7, left=0, color=colors[i],
                       alpha=0.85, zorder=3, edgecolor=BORDER, linewidth=0.5)

        # Level label inside bar
        ax.text(0.3, y, label, fontsize=11, fontweight="bold",
                color=TEXT_PRIMARY, va="center", zorder=5)

        # Description to the right of the bar
        ax.text(width + 0.3, y, desc, fontsize=9, color=TEXT_PRIMARY,
                va="center", zorder=5)

    # Annotations for where organizations are
    # "Most organizations: Level 1-2"
    ax.annotate(
        "Most organizations: Level 1\u20132",
        xy=(bar_widths[2] + 0.2, y_positions[2]),
        xytext=(bar_widths[2] + 4.5, y_positions[2] + 1.2),
        fontsize=10, color=ACCENT, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.5),
        bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_SECONDARY,
                  edgecolor=ACCENT, alpha=0.9))

    # "Frontier teams: Level 4-5"
    ax.annotate(
        "Frontier teams: Level 4\u20135",
        xy=(bar_widths[4] + 0.2, y_positions[4]),
        xytext=(bar_widths[4] + 3.0, y_positions[4] - 1.2),
        fontsize=10, color="#10B981", fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#10B981", lw=1.5),
        bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_SECONDARY,
                  edgecolor="#10B981", alpha=0.9))

    ax.set_title("Dan Shapiro's 5 Levels of AI Coding",
                 fontsize=14, fontweight="bold", pad=14)
    ax.set_xlim(0, max(bar_widths) + 8)
    ax.set_ylim(-0.8, n - 0.2)
    ax.axis("off")

    fig.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.06)
    save(fig, "five-levels")


# ===========================================================================
# Chart 11: AI Code Generation Percentage
# ===========================================================================
def chart_ai_code_percentage():
    print("Generating ai-code-percentage...")

    data = [
        ("Boris Cherny (personal)", 100),
        ("Anthropic internal", 90),
        ("Claude Code self-development", 90),
        ("Microsoft (est.)", 30),
        ("GitHub avg \u2013 Science study (US)", 29),
        ("Industry average (est.)", 25),
    ]

    # Sort descending
    data.sort(key=lambda x: x[1], reverse=True)
    labels = [d[0] for d in data]
    values = [d[1] for d in data]

    fig, ax = plt.subplots(figsize=(10, 5))

    # Assign colors: top 3 get accent colors, rest get secondary
    bar_colors = []
    for val in values:
        if val >= 90:
            bar_colors.append(ACCENT)
        elif val >= 30:
            bar_colors.append(ACCENT2)
        else:
            bar_colors.append(TEXT_SECONDARY)

    bars = ax.barh(range(len(labels)), values, height=0.6, zorder=3, alpha=0.85)
    for bar, color in zip(bars, bar_colors):
        bar.set_color(color)

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel("AI-Generated Code (%)")
    ax.set_title("AI Code Generation: Share of Code Written by AI",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xlim(0, 115)
    ax.xaxis.set_major_formatter(mticker.PercentFormatter())

    # Add percentage labels on bars
    for i, val in enumerate(values):
        ax.text(val + 1.5, i, f"{val}%", va="center", fontsize=10,
                color=TEXT_PRIMARY, fontweight="bold")

    # Dividing annotation
    ax.axvline(x=50, color=TEXT_MUTED, linewidth=1, linestyle="--", alpha=0.6, zorder=2)
    ax.text(51, len(labels) - 0.5, "50% threshold", fontsize=8,
            color=TEXT_MUTED, va="bottom", ha="left")

    fig.subplots_adjust(left=0.32)
    save(fig, "ai-code-percentage")


# ===========================================================================
# Chart 12: Compounding vs Linear Productivity
# ===========================================================================
def chart_compounding_vs_linear():
    print("Generating compounding-vs-linear...")

    months = np.linspace(0, 12, 200)

    # Linear (Vibe Coding): steady increase
    linear = 1.0 + months * 0.8

    # Compounding (Software Factory): exponential
    compounding = 1.0 * np.exp(months * 0.25)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Shaded area between curves (The Compounding Gap)
    ax.fill_between(months, linear, compounding, where=(compounding > linear),
                    alpha=0.12, color=ACCENT, zorder=2, label="_nolegend_")

    # Lines
    ax.plot(months, linear, color=ACCENT2, linewidth=2.5, zorder=3,
            label="Linear (Vibe Coding)", linestyle="--")
    ax.plot(months, compounding, color=ACCENT, linewidth=2.5, zorder=3,
            label="Compounding (Software Factory)")

    # Annotation for "The Compounding Gap"
    gap_month = 8
    gap_y = (1.0 * np.exp(gap_month * 0.25) + 1.0 + gap_month * 0.8) / 2
    ax.annotate(
        "The Compounding\nGap",
        xy=(gap_month, gap_y),
        fontsize=12, color=ACCENT, fontweight="bold", ha="center",
        bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_SECONDARY,
                  edgecolor=ACCENT, alpha=0.9))

    # Annotation at divergence point (~month 4)
    div_month = 4
    div_y = 1.0 * np.exp(div_month * 0.25)
    ax.annotate(
        "Teams that build tools\nfor building tools",
        xy=(div_month, div_y),
        xytext=(div_month + 2.5, div_y + 4),
        fontsize=9, color=TEXT_PRIMARY,
        arrowprops=dict(arrowstyle="->", color=TEXT_SECONDARY, lw=1.2),
        bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_SECONDARY,
                  edgecolor=ACCENT2, alpha=0.9))

    ax.set_title("Compounding vs. Linear Productivity Growth",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Time (months)")
    ax.set_ylabel("Relative Output")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 22)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}x"))
    ax.legend(loc="upper left", framealpha=0.8, fontsize=10)

    save(fig, "compounding-vs-linear")


# ===========================================================================
# Chart 13: Geopolitical Approaches
# ===========================================================================
def chart_geopolitical_approaches():
    print("Generating geopolitical-approaches...")

    categories = ["Speed / Deregulation", "Investment Scale", "Regulatory Framework",
                   "Open-Source Ecosystem", "Talent Pipeline", "Cost Efficiency"]
    us_scores = [9, 10, 3, 6, 8, 5]
    eu_scores = [4, 5, 10, 5, 6, 6]
    china_scores = [7, 6, 6, 8, 7, 10]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    us_scores += us_scores[:1]
    eu_scores += eu_scores[:1]
    china_scores += china_scores[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_facecolor(BG_CARD)

    ax.plot(angles, us_scores, "o-", linewidth=2, color="#22C55E", label="United States", markersize=6)
    ax.fill(angles, us_scores, alpha=0.1, color="#22C55E")
    ax.plot(angles, eu_scores, "s-", linewidth=2, color=ACCENT2, label="European Union", markersize=6)
    ax.fill(angles, eu_scores, alpha=0.1, color=ACCENT2)
    ax.plot(angles, china_scores, "^-", linewidth=2, color=ACCENT, label="China", markersize=6)
    ax.fill(angles, china_scores, alpha=0.1, color=ACCENT)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9, color=TEXT_PRIMARY)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=8, color=TEXT_MUTED)
    ax.spines["polar"].set_color(BORDER)
    ax.grid(color=BORDER, alpha=0.5)

    ax.set_title("AI Geopolitical Approaches: US vs EU vs China",
                 fontsize=14, fontweight="bold", pad=20, color=TEXT_PRIMARY)
    ax.legend(loc="lower right", bbox_to_anchor=(1.2, -0.05), framealpha=0.8)

    save(fig, "geopolitical-approaches")


# ===========================================================================
# Chart 14: Science Acceleration
# ===========================================================================
def chart_science_acceleration():
    print("Generating science-acceleration...")

    domains = [
        "Software\nEngineering", "Mathematics\n& Proofs", "Materials\nScience",
        "Drug Target\nIdentification", "Protein\nStructure", "Clinical\nTrials",
        "Biology\nExperiments", "Climate\nField Work"
    ]
    ai_acceleration = [85, 65, 50, 45, 80, 10, 15, 8]
    bottleneck_type = ["Computational", "Computational", "Mixed",
                       "Mixed", "Computational", "Physical",
                       "Physical", "Physical"]

    fig, ax = plt.subplots(figsize=(12, 6))

    colors = []
    for bt in bottleneck_type:
        if bt == "Computational":
            colors.append(ACCENT)
        elif bt == "Mixed":
            colors.append(ACCENT2)
        else:
            colors.append(TEXT_MUTED)

    bars = ax.bar(range(len(domains)), ai_acceleration, width=0.65,
                  color=colors, alpha=0.85, zorder=3, edgecolor=BORDER, linewidth=0.5)

    if PRINT_MODE:
        for bar, bt in zip(bars, bottleneck_type):
            bar.set_hatch(BOTTLENECK_HATCHES.get(bt, ""))
            bar.set_edgecolor("#333333")

    for i, val in enumerate(ai_acceleration):
        ax.text(i, val + 2, f"{val}%", ha="center", fontsize=10,
                color=TEXT_PRIMARY, fontweight="bold")

    ax.set_xticks(range(len(domains)))
    ax.set_xticklabels(domains, fontsize=9)
    ax.set_ylabel("Estimated AI Acceleration (%)")
    ax.set_title("AI Acceleration by Scientific Domain",
                 fontsize=14, fontweight="bold", pad=12)
    ax.set_ylim(0, 100)

    # Dividing line between computational and physical
    ax.axvline(x=4.5, color=TEXT_MUTED, linewidth=1, linestyle="--", alpha=0.6, zorder=2)
    ax.text(2.0, 95, "Computational\nBottleneck", ha="center", fontsize=10,
            color=ACCENT, fontweight="bold")
    ax.text(6.5, 95, "Physical\nBottleneck", ha="center", fontsize=10,
            color=TEXT_MUTED, fontweight="bold")

    # Legend
    handles = [
        mpatches.Patch(color=ACCENT, label="Computational", alpha=0.85),
        mpatches.Patch(color=ACCENT2, label="Mixed", alpha=0.85),
        mpatches.Patch(color=TEXT_MUTED, label="Physical", alpha=0.85),
    ]
    ax.legend(handles=handles, loc="upper right", framealpha=0.8)

    save(fig, "science-acceleration")


# ===========================================================================
# Main
# ===========================================================================
def main():
    print(f"Output directory: {OUT_DIR}")
    apply_style()

    chart_swe_bench()
    chart_metr()
    chart_model_releases()
    chart_prediction_scorecard()
    chart_job_displacement()
    chart_ai_investment()
    chart_ai_timeline()
    chart_recursive_loop()
    chart_november_revolution()
    chart_five_levels()
    chart_ai_code_percentage()
    chart_compounding_vs_linear()
    chart_geopolitical_approaches()
    chart_science_acceleration()

    print("\nAll charts generated successfully.")


if __name__ == "__main__":
    main()
