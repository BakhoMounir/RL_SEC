# Phase 2 Final Reproducibility Audit

Audit time (UTC): 2026-10-28T22:16:02.469431+00:00
Repository HEAD: 8884d1a3a4a68e2945eb71ea2c7fef3d803cbb17

## Frozen artifacts
- Confirmatory CSV: `/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/results/v2/confirmatory_v1/episodes.csv`
- CSV SHA-256: `e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73`
- Rows: 72000; methods: A_600k, A_legacy_150k, B_legacy_150k, greedy_widest, minhop, shortest_feasible, shortest_feasible_k, unit_weight_dijkstra, util_weight_dijkstra; loads: [1.0, 1.5, 2.0, 3.0]
- Frozen checkpoints verified: 30/30
- Recorded core-code hash: `2164ee0acd69c28461406400b54143f154833fbbd480a7098e71796e53b7b714`
- Recomputed core-code hash: `f11d47980dbff877cb789a11fb0a78b9459149d672a9008c84422111c8caefdd`

## Checks
- PASS — Confirmatory CSV exists: /media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/results/v2/confirmatory_v1/episodes.csv
- PASS — Manifest exists: /media/bakhom/New Volume/Research/RL_Sec/practical/files/routing-poisoning-phase2-handover/results/v2/confirmatory_v1/manifest.json
- PASS — Freeze exists: /media/bakhom/New Volume/Research/RL_Sec/practical/files/routing-poisoning-phase2-handover/results/v2/freeze.json
- PASS — Lock exists: /media/bakhom/New Volume/Research/RL_Sec/practical/files/routing-poisoning-phase2-handover/results/v2/confirmatory_v1/LOCK.json
- PASS — CSV required columns present: missing=[]
- PASS — CSV has expected 72,000 rows: rows=72000
- PASS — CSV has four expected load levels: [1.0, 1.5, 2.0, 3.0]
- PASS — CSV has method labels: ['A_600k', 'A_legacy_150k', 'B_legacy_150k', 'greedy_widest', 'minhop', 'shortest_feasible', 'shortest_feasible_k', 'unit_weight_dijkstra', 'util_weight_dijkstra']
- PASS — Configuration matches freeze: actual=2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec; recorded=2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec
- PASS — Topology matches freeze: actual=fe497b0bce187d1b7fe454e92c8778357dfa21ef2587878723d7d43d52824e7e; recorded=fe497b0bce187d1b7fe454e92c8778357dfa21ef2587878723d7d43d52824e7e
- PASS — Lock configuration agrees with freeze: lock=2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec; freeze=2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec
- PASS — Lock evaluation range present: 'test_confirmatory_v2'
- PASS — Lock specifies 500 scenarios per load: 500
- PASS — All frozen checkpoints verify: verified=30/30
- FAIL — CSV matches manifest hash: actual=e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73; recorded=None
- FAIL — Recorded core-code hash independently reproduced: actual=f11d47980dbff877cb789a11fb0a78b9459149d672a9008c84422111c8caefdd; recorded=2164ee0acd69c28461406400b54143f154833fbbd480a7098e71796e53b7b714
- FAIL — Existing Phase 2 tests pass: ==================================== ERRORS ====================================
_____________ ERROR collecting phase2/tests/test_x_config_seeds.py _____________
ImportError while importing test module '/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/tests/test_x_config_seeds.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
phase2/tests/test_x_config_seeds.py:4: in <module>
    from p2x import config as C
E   ModuleNotFoundError: No module named 'p2x'
____________ ERROR collecting phase2/tests/test_x_pipeline_stub.py _____________
ImportError while importing test module '/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/tests/test_x_pipeline_stub.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
phase2/tests/test_x_pipeline_stub.py:6: in <module>
    from p2.sim import Network
E   ModuleNotFoundError: No module named 'p2'
__________ ERROR collecting phase2/tests/test_x_policies_telemetry.py __________
ImportError while importing test module '/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/tests/test_x_policies_telemetry.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
phase2/tests/test_x_policies_telemetry.py:3: in <module>
    from p2.baselines import BASELINES
E   ModuleNotFoundError: No module named 'p2'
_________ ERROR collecting phase2/tests/test_x_stats_train_manifest.py _________
ImportError while importing test module '/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/tests/test_x_stats_train_manifest.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
phase2/tests/test_x_stats_train_manifest.py:4: in <module>
    from p2x import analysis
E   ModuleNotFoundError: No module named 'p2x'
=========================== short test summary info ============================
ERROR phase2/tests/test_x_config_seeds.py
ERROR phase2/tests/test_x_pipeline_stub.py
ERROR phase2/tests/test_x_policies_telemetry.py
ERROR phase2/tests/test_x_stats_train_manifest.py
!!!!!!!!!!!!!!!!!!! Interrupted: 4 errors during collection !!!!!!!!!!!!!!!!!!!!
4 errors in 0.57s
- CAVEAT — Dataset provenance/license: Still unresolved; do not claim verified identity/license or redistribute source data.
- CAVEAT — Training framework versions: Frozen checkpoints document multiple PyTorch builds; report as a reproducibility caveat.
- CAVEAT — Scientific scope: Do not start poisoning experiments until clean baseline and claims are reviewed.

## Interpretation and restrictions
- This audit does not rerun training or modify frozen outputs.
- A hash mismatch means source identity is not fully verified; it does not by itself prove the benchmark results are wrong.
- Dataset identity, provenance, and redistribution rights remain unresolved until independently confirmed.
- Report the PyTorch build variation for checkpoints as a reproducibility limitation.
- Interpret the learned agents against all baselines; do not claim general superiority without appropriate statistical evidence.
- Do not begin poisoning experiments until the clean baseline review is complete.

## Overall status
NOT FULLY VERIFIED — REVIEW FAILURES BELOW



## Corrected follow-up audit (2026-10-28T22:16:52.720478+00:00)

- Confirmatory CSV SHA-256: `e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73`
- Pytest exit code with explicit package import paths: `0`
- The original frozen code-hash discrepancy remains unresolved.
- Dataset provenance and licensing remain unresolved.
- Frozen benchmark results, checkpoint files, freeze records, and lock records were not modified.
