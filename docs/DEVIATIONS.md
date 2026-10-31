# Deviations from the pre-specified protocol
Complete every TODO from `project_summary.txt` before submitting the paper.

| # | Deviation | Date | Reason | Affected outputs | Required disclosure |
|---|-----------|------|--------|------------------|---------------------|
| 1 | Inference changed from a bootstrap-tail p-value to a one-sample t-test over model-seed means (multi-model) or a paired scenario sign-flip test (single model). Output key `p_boot` is retained but is NOT a bootstrap p-value. | TODO | TODO | `phase2/results/confirmatory_v1/analysis` (original) vs `analysis_v2_valid_tests` (+ `analysis_provenance.json`) | Report both; describe v2 as a correction |
| 2 | Source edited after the freeze (`parts.py`, `sim.py`); snapshots in `docs/evidence/pre_freeze_restore/` | 2026-10-31 | TODO | TODO: were results regenerated afterwards? | State the code-hash discrepancy as a limitation unless proven resolved |
| 3 | Several poisoning runs exist (smoke, pilot, pilot_fresh, reduced, full, optimized). Only a run whose manifest status is "completed" with the expected row counts supports a claim. | TODO | TODO | `phase2/results/deliverables/metadata/*` | Name the run behind every table/figure |
| 4 | Exploratory seed-42 poisoning variant existed in the overlay tree | TODO | exploratory | not confirmatory | Label exploratory |
