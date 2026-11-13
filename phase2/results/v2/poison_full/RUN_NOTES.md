# Poisoning run - deviations and procedure

**Run:** phase2/results/v2/poison_full/ | **Date:** 2026-11-13 | **Operator:** Mustafa

**Requested by Dr. Mariam:** one complete poisoning run - all 10 seeds, loads 2.0 and 3.0, eps in {0.1, 0.2, 0.4}, 300 scenarios; include utilisation-weighted Dijkstra. Scope confirmed later: A_600k alone is enough for this paper.

## What was run

| Parameter | Value |
|---|---|
| Preset | full |
| Agent | A_600k, seeds 42-51 (10) |
| Baselines | shortest_feasible, greedy_widest, shortest_feasible_k, util_weight_dijkstra, minhop, unit_weight_dijkstra |
| Loads | 2.0, 3.0 |
| Scenarios per load | 300 (test_poison_v2) |
| eps | 0.1, 0.2, 0.4 |
| Attacks | random_sign (noise control), bias_all_plus, bias_all_minus, conceal_topk, fake_topk |
| Attack configs | 16 (1 clean + 5 x 3) |
| Rows | 153,600 |
| Wall time | 5,703 s |

Invariants in manifest.json: all_replay_ok = true, all_caps_ok = true, max_delta_over_budget = 5.55e-17. 16/16 target-seed pairs validated. Status: pre-declared Stage F run.

## Deviations from the repository as published

Three changes were required before the run could start. All are recorded here; none were silent.

### 1. Line endings (no file content changed)

On a Windows clone, core.autocrlf=true rewrote line endings, so every recorded SHA-256 failed: topology, core-code and config. Fixed with: git config core.autocrlf false, then git rm --cached -r . and git reset --hard. After this the topology hash (fe497b0b...), core-code hash (2164ee0a...) and config hash (2c2a530d...) all matched the published freeze exactly. No file content was modified by this step.

### 2. phase2/configs/x_experiments.json

| Field | Before | After | Reason |
|---|---|---|---|
| poisoning.presets.full.loads | [1.0, 1.5, 2.0, 3.0] | [2.0, 3.0] | Dr. Mariam specified these two loads |
| poisoning.targets_models | A_600k, A_legacy_150k, B_legacy_150k | A_600k | A_600k alone is enough |
| confirmatory.agents[].optional | A_600k: true; legacy: false | A_600k: false; legacy: true | The legacy agents are absent from the repo (see 3); A_600k is the one agent present and required |

targets_baselines was NOT changed: util_weight_dijkstra was already in the list, so the second request needed no edit.

### 3. phase2/results/v2/freeze.json

The published freeze recorded absolute paths from the author machine (/media/bakhom/New Volume/...), which verify_freeze resolves literally, so the checkpoint check failed here.

The freeze was regenerated with the project own tool - python phase2/scripts/x_05_freeze.py --overwrite --yes - not edited by hand. This was permitted because confirmatory_v1/LOCK.json does not exist. The regenerated freeze writes relative paths (results/v2/models/replace_600k/seed42/best.zip) and carries the new config hash (b9b43f0a...). Topology and core-code hashes are unchanged.

Before regenerating, every checkpoint was verified by content: A_600k 10/10 files matched the SHA-256 recorded in the published freeze, so the files are byte-identical to the author copies; only the path strings differed.

A_legacy_150k and B_legacy_150k are absent from the repository (0/10 checkpoints each; no results/models/ directory exists). The regenerated freeze records them through the project own mechanism, with the note: A_legacy_150k: 0/10 seeds present -> treated as ABSENT (primary comparisons P1/P2 will be not-computed). This is the documented behaviour for optional agents, not a suppression.

## Results

Analysis command: python phase2/scripts/x_08_analyze.py --stage poison --preset full. Outputs in poison_full/analysis/.

Under the project pre-declared criterion - attack success requires the crossed CI of (attacked - clean) to exclude 0 AND the contrast against random_sign at equal eps to exclude 0 - no attack succeeded at either load, at any eps.

Summary for A_600k:

- The strongest degradation in the whole table comes from the noise control: random_sign at eps 0.4 gives -4.50 pp (load 2.0) and -3.79 pp (load 3.0). No targeted attack exceeds it.
- conceal_topk at eps 0.2, load 2.0: -1.755 pp [-1.94, -1.56], but the contrast against noise is -0.086 pp [-0.29, +0.13], p = 0.406 - indistinguishable from noise.
- fake_topk at eps 0.2, load 2.0: +0.099 pp [0.00, 0.20] - the accepted ratio rises under attack; contrast +1.768 pp, i.e. the targeted attack is markedly weaker than noise.
- bias_all_minus at eps 0.1, load 3.0: +0.251 pp [0.14, 0.36] - also an improvement.
- Decision-flip rates follow the same pattern: random_sign flips the most decisions (28.0% at eps 0.4) and fake_topk the fewest (10.3%). fake_topk at eps 0.2 flips 4.85% of decisions while improving the ratio, which separates decisions changed from attack succeeded.

Reading: the degradation observed under perturbation is consistent with loss of telemetry accuracy, not with attacker targeting. Within this threat model (non-adaptive, observation-only, bounded per-edge offsets), targeted poisoning does not beat random noise.

## Reproducing

    git config core.autocrlf false
    python phase2/scripts/x_07_poison_eval.py --preset full
    python phase2/scripts/x_07_poison_eval.py --preset full --run
    python phase2/scripts/x_08_analyze.py --stage poison --preset full

Environment: Python 3.12.10, torch 2.11.0+cu128, stable-baselines3 2.9.0, gymnasium 1.4.0, numpy 2.5.4, pandas 3.1.1, on Windows. Checkpoints load on CPU, as fixed in rollout.py.

Note: poison_full/parts/ (the 16 intermediate per-target CSVs, 51.9 MB) is git-ignored; its content is fully contained in episodes.csv.
