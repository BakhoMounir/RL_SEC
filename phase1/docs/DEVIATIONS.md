# Deviations from the pre-specified protocol (complete before submitting the paper)

| # | Deviation | When | Why | Affected outputs | Disclosure in paper |
|---|-----------|------|-----|------------------|---------------------|
| 1 | Inference changed: bootstrap-tail p-value -> one-sample t over model-seed means (multi-model) / paired scenario sign-flip (single model). Key `p_boot` retained but is NOT a bootstrap p-value. | TODO date | TODO | `analysis/` (original) vs `analysis_v2_valid_tests/` | Report both; state v2 is a correction |
| 2 | Post-freeze edits to `parts.py` and `sim.py` (see `docs/evidence/pre_freeze_restore_20261031/`) | 2026-10-31 | TODO | TODO: were results regenerated afterwards? | TODO |
| 3 | Poisoning runs: pilot / reduced / optimized / full. Only runs with manifest status "completed" support claims. | TODO | TODO | `phase2/results/deliverables/metadata/*` | State exactly which run each table uses |
| 4 | Seed-42 exploratory poisoning script (`x_07_poison_eval_seed42_exploratory.py`) | TODO | exploratory | not confirmatory | Label exploratory |
| 5 | Code-hash discrepancy between validation tree and overlay | TODO | TODO | `freeze.json` combined hash | State as limitation |
