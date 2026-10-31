#!/usr/bin/env python3
"""Generate reproducible Phase 2 figures from the confirmatory episode CSV.

Column mapping is inferred conservatively. Review columns and output diagnostics.
No values are fabricated, interpolated, or extracted from paper figures.
"""
from pathlib import Path
import re
import json
import warnings

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "results/v2/confirmatory_v1/episodes.csv"
OUT = ROOT / "results/v2/figures_final"
OUT.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid", context="talk")
plt.rcParams.update({
    "figure.figsize": (10, 6),
    "savefig.dpi": 300,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

if not CSV.exists():
    raise SystemExit(f"Missing input CSV: {CSV}")

df = pd.read_csv(CSV)
if df.empty:
    raise SystemExit("Input CSV is empty.")

def norm(s):
    return re.sub(r"[^a-z0-9]+", "_", str(s).lower()).strip("_")

cols = {c: norm(c) for c in df.columns}

def find_col(candidates, required=False, label="column"):
    for c in df.columns:
        n = cols[c]
        if any(re.search(p, n) for p in candidates):
            return c
    if required:
        raise SystemExit(
            f"Cannot infer {label}. Actual columns are:\n" +
            "\n".join(map(str, df.columns)) +
            "\nEdit the column mapping in generate_figures.py."
        )
    return None

# Avoid confusing generic "seed" with a scenario ID or episode ID.
method = find_col(
    [r"^method$", r"^agent$", r"^policy$", r"^algorithm$",
     r"routing_method", r"baseline_name", r"model_name"],
    required=True, label="method/algorithm"
)
load = find_col(
    [r"^load$", r"offered_load", r"traffic_load", r"load_factor"],
    required=True, label="traffic-load column"
)
metric = find_col(
    [r"^success_rate$", r"^delivery_rate$", r"^success$",
     r"^episode_success$", r"^completed_fraction$",
     r"^served_fraction$", r"^acceptance_rate$"],
    label="success metric"
)
seed = find_col([r"^seed$", r"training_seed", r"model_seed"])
scenario = find_col([r"^scenario_id$", r"^scenario$", r"test_case_id"])
episode = find_col([r"^episode$", r"episode_id$"])
steps = find_col([r"^steps_trained$", r"^timesteps$", r"^total_timesteps$"])
reward = find_col([r"^reward$", r"episode_reward$", r"mean_reward$"])
latency = find_col([r"^latency$", r"^delay$", r"end_to_end_delay"])
loss = find_col([r"^packet_loss$", r"loss_rate$", r"drop_rate$"])
util = find_col([r"^max_link_utilization$", r"^max_utilization$",
                 r"^link_utilization$", r"^utilization$"])

# Save a transparent inventory of the data schema and missingness.
schema = {
    "input_csv": str(CSV),
    "rows": int(len(df)),
    "columns": [
        {"name": str(c), "dtype": str(df[c].dtype),
         "missing": int(df[c].isna().sum()),
         "unique_non_null": int(df[c].nunique(dropna=True))}
        for c in df.columns
    ],
    "inferred_columns": {
        "method": method, "load": load, "success_metric": metric,
        "seed": seed, "scenario": scenario, "episode": episode,
        "steps": steps, "reward": reward, "latency": latency,
        "packet_loss": loss, "utilization": util,
    },
}
(OUT / "data_schema.json").write_text(json.dumps(schema, indent=2))
df.groupby([method, load], dropna=False).size().rename("n").reset_index().to_csv(
    OUT / "row_counts_by_method_load.csv", index=False
)

print(f"Input rows: {len(df):,}")
print(f"Methods: {df[method].nunique(dropna=True)}")
print(f"Loads: {sorted(df[load].dropna().unique().tolist(), key=str)}")
print(f"Columns: {list(df.columns)}")
print(f"Inferred metric: {metric!r}")

def save(fig, filename):
    fig.tight_layout()
    fig.savefig(OUT / filename, bbox_inches="tight")
    plt.close(fig)
    print("Wrote", OUT / filename)

# Figure 1: experimental design / sample counts.
counts = df.groupby([load, method], dropna=False).size().reset_index(name="rows")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=counts, x=load, y="rows", hue=method, ax=ax)
ax.set(title="Confirmatory evaluation coverage", xlabel="Traffic load",
       ylabel="Recorded evaluation rows")
ax.legend(title="Method", bbox_to_anchor=(1.02, 1), loc="upper left")
save(fig, "fig01_evaluation_coverage.png")

# Figure 2: success metric, if it can be identified.
if metric:
    plot = df[[method, load, metric]].copy()
    plot[metric] = pd.to_numeric(plot[metric], errors="coerce")
    plot = plot.dropna()
    if not plot.empty:
        summary = plot.groupby([load, method])[metric].agg(
            mean="mean", std="std", n="count"
        ).reset_index()
        summary["se"] = summary["std"] / np.sqrt(summary["n"].clip(lower=1))
        summary.to_csv(OUT / "success_metric_summary.csv", index=False)

        fig, ax = plt.subplots(figsize=(12, 7))
        sns.lineplot(data=plot, x=load, y=metric, hue=method,
                     marker="o", estimator="mean", errorbar=("ci", 95), ax=ax)
        ax.set(title=f"{metric.replace('_', ' ').title()} by traffic load",
               xlabel="Traffic load", ylabel=metric.replace("_", " ").title())
        ax.legend(title="Method", bbox_to_anchor=(1.02, 1), loc="upper left")
        save(fig, "fig02_success_by_load.png")

        fig, ax = plt.subplots(figsize=(12, 7))
        sns.boxplot(data=plot, x=load, y=metric, hue=method, ax=ax,
                    showfliers=False)
        ax.set(title=f"Distribution of {metric.replace('_', ' ')}",
               xlabel="Traffic load", ylabel=metric.replace("_", " ").title())
        ax.legend(title="Method", bbox_to_anchor=(1.02, 1), loc="upper left")
        save(fig, "fig03_success_distributions.png")
    else:
        print("WARNING: success metric found but contains no usable numeric values.")
else:
    print("WARNING: no obvious success metric column found; figures 2-3 skipped.")

# Additional performance metrics are plotted only if matching columns exist.
for col, title, filename in [
    (reward, "Recorded reward by traffic load", "fig04_reward_by_load.png"),
    (latency, "Recorded latency/delay by traffic load", "fig05_latency_by_load.png"),
    (loss, "Recorded packet loss by traffic load", "fig06_packet_loss_by_load.png"),
    (util, "Recorded link utilization by traffic load", "fig07_utilization_by_load.png"),
]:
    if col:
        tmp = df[[method, load, col]].copy()
        tmp[col] = pd.to_numeric(tmp[col], errors="coerce")
        tmp = tmp.dropna()
        if not tmp.empty:
            fig, ax = plt.subplots(figsize=(12, 7))
            sns.lineplot(data=tmp, x=load, y=col, hue=method,
                         marker="o", estimator="mean", errorbar=("ci", 95), ax=ax)
            ax.set(title=title, xlabel="Traffic load", ylabel=col.replace("_", " "))
            ax.legend(title="Method", bbox_to_anchor=(1.02, 1), loc="upper left")
            save(fig, filename)

# Scenario-level paired comparisons: only if the CSV includes a scenario ID
# and the success metric was inferred. This is descriptive, not a replacement
# for the project's preregistered statistical analysis.
if scenario and metric:
    tmp = df[[scenario, method, load, metric]].copy()
    tmp[metric] = pd.to_numeric(tmp[metric], errors="coerce")
    tmp = tmp.dropna(subset=[scenario, method, load, metric])
    wide = tmp.pivot_table(index=[scenario, load], columns=method,
                           values=metric, aggfunc="mean")
    wide.to_csv(OUT / "scenario_level_metric_wide.csv")
    print("Wrote scenario-level comparison table (no new inferential tests run).")

# Training curve, if the confirmatory file itself includes training steps.
if steps and (reward or metric):
    y = reward or metric
    tmp = df[[steps, method, y]].copy()
    tmp[steps] = pd.to_numeric(tmp[steps], errors="coerce")
    tmp[y] = pd.to_numeric(tmp[y], errors="coerce")
    tmp = tmp.dropna()
    if not tmp.empty:
        fig, ax = plt.subplots(figsize=(12, 7))
        sns.lineplot(data=tmp, x=steps, y=y, hue=method,
                     estimator="mean", errorbar=("ci", 95), ax=ax)
        ax.set(title=f"Training progress: {y}", xlabel="Training steps", ylabel=y)
        save(fig, "fig08_training_curve.png")

print("\nFinished figure generation.")
print("Figures are descriptive. Confirm inferential statistics against the")
print("pre-existing preregistered analysis files before using in a paper.")
