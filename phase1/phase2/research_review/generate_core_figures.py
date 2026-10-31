from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[2]
CSV = ROOT / "phase2/results/v2/confirmatory_v1/episodes.csv"
OUT = ROOT / "phase2/results/v2/figures_final"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(CSV, low_memory=False)

required = {
    "method", "load", "accepted_offered_ratio",
    "blocked_volume_ratio", "mean_hops_per_flow",
    "mean_utilization", "max_utilization"
}
missing = required - set(df.columns)
if missing:
    raise SystemExit(f"Missing expected columns: {sorted(missing)}")

for col in required - {"method"}:
    df[col] = pd.to_numeric(df[col], errors="coerce")

sns.set_theme(style="whitegrid", context="paper", font_scale=1.15)

metrics = [
    ("accepted_offered_ratio", "Accepted / offered traffic ratio",
     "fig02_accepted_offered_ratio.png", (0, 1.05)),
    ("blocked_volume_ratio", "Blocked traffic volume ratio",
     "fig03_blocked_volume_ratio.png", (0, 1.05)),
    ("mean_hops_per_flow", "Mean hops per flow",
     "fig04_mean_hops_per_flow.png", None),
    ("mean_utilization", "Mean link utilization",
     "fig05_mean_utilization.png", None),
    ("max_utilization", "Maximum link utilization",
     "fig06_max_utilization.png", None),
]

for metric, ylabel, filename, ylim in metrics:
    plot_data = df.dropna(subset=["method", "load", metric])
    if plot_data.empty:
        print(f"SKIP {metric}: no valid numeric values")
        continue

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(
        data=plot_data,
        x="load",
        y=metric,
        hue="method",
        marker="o",
        errorbar=None,
        ax=ax
    )
    ax.set(
        xlabel="Offered traffic load",
        ylabel=ylabel,
        title=f"{ylabel} across traffic loads"
    )
    if ylim:
        ax.set_ylim(*ylim)
    ax.legend(title="Method", bbox_to_anchor=(1.02, 1), loc="upper left")
    fig.tight_layout()
    fig.savefig(OUT / filename, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {filename}")

summary = (
    df.groupby(["method", "load"], dropna=False)
      .agg(
          rows=("accepted_offered_ratio", "size"),
          accepted_ratio_mean=("accepted_offered_ratio", "mean"),
          accepted_ratio_sd=("accepted_offered_ratio", "std"),
          blocked_ratio_mean=("blocked_volume_ratio", "mean"),
          mean_hops=("mean_hops_per_flow", "mean"),
          mean_utilization=("mean_utilization", "mean"),
          max_utilization=("max_utilization", "mean"),
          saturated_links_mean=("saturated_links", "mean"),
      )
      .reset_index()
)
summary.to_csv(OUT / "descriptive_summary_by_method_load.csv", index=False)
print("Wrote descriptive_summary_by_method_load.csv")
print(f"Input rows: {len(df):,}; methods: {df['method'].nunique()}; "
      f"loads: {sorted(df['load'].dropna().unique())}")
