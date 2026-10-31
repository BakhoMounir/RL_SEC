# Phase 2: Clean Routing and Telemetry-Poisoning Evaluation

Generated UTC: 2026-10-28T22:31:49.685859+00:00

## Executive summary

This report analyzes the existing clean confirmatory benchmark and completed poisoning pilot. No agent was retrained and no new experimental outcomes were fabricated.

- Frozen checkpoints verified by SHA-256: **30/30**
- Clean confirmatory rows: **72,000**
- Completed poisoning pilot rows: **16,500**
- Clean result SHA-256: `e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73`
- Pilot result SHA-256: `990b21741f7d1ea3a60d506ad6f6467fdb74dd220e01d92b2c87fca98cfcefaf`

## Clean benchmark

Methods present: A_600k, A_legacy_150k, B_legacy_150k, greedy_widest, minhop, shortest_feasible, shortest_feasible_k, unit_weight_dijkstra, util_weight_dijkstra

Loads present: 1.0, 1.5, 2.0, 3.0

The raw clean benchmark is retained unchanged. Derived numeric summaries and an acceptance-ratio plot are produced only when the required columns exist. Results should be interpreted by metric and load; performance against one baseline does not establish universal superiority.

## Poisoning pilot

Methods present: A_600k, A_legacy_150k, B_legacy_150k, greedy_widest, minhop, shortest_feasible, shortest_feasible_k, unit_weight_dijkstra, util_weight_dijkstra

Attack labels present: bias_all_minus@0.2, bias_all_minus@0.4, bias_all_plus@0.2, bias_all_plus@0.4, clean, conceal_topk@0.2, conceal_topk@0.4, fake_topk@0.2, fake_topk@0.4, random_sign@0.2, random_sign@0.4

The existing pilot is limited in scope and is not a substitute for a full multi-load, multi-seed evaluation. It should be presented as pilot evidence, not as proof of general robustness.

## Run statuses recorded in existing manifests

```json
{
  "poison_A600k_reduced": "failed",
  "poison_A600k_seed42_exploratory": "failed",
  "poison_full": "failed",
  "poison_full_optimized": "failed",
  "poison_pilot": "completed",
  "poison_pilot_fresh": "completed",
  "poison_smoke": "completed"
}
```

Failed full runs are not treated as completed scientific results.

## Reproducibility and limitations

1. Original source CSVs, checkpoint files, freeze records, and manifests were not modified.
2. The original confirmatory manifest records code-tree hash `2164ee0acd69c28461406400b54143f154833fbbd480a7098e71796e53b7b714`. A previous audit reported a different recomputed code-tree hash. This discrepancy remains unresolved; do not claim exact code-tree reproducibility until it is explained.
3. Dataset provenance and redistribution/license terms still need verification.
4. The pilot does not support broad claims about all attack settings, traffic loads, or model seeds.
5. No full poisoning experiment was rerun by this recovery script.

## Output files

- `tables/checkpoint_verification.csv`
- `tables/clean_numeric_summary.csv` (if numeric fields were available)
- `tables/clean_acceptance_summary.csv` (if acceptance columns were available)
- `tables/poison_pilot_summary.csv`
- Existing pilot analysis CSVs copied into `tables/` when available
- `figures/clean_acceptance_by_load.png` and pilot metric plot when supported by the data
- `audit/recovery_run.log`
