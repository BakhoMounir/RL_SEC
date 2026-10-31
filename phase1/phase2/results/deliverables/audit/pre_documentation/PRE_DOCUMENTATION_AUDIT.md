# Pre-documentation audit

- Created (UTC): 2026-10-31T13:01:36.020800+00:00
- Project: `/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation`
- Overall: **REVIEW REQUIRED: inspect scientific and documentation warnings**
- Counts: {'PASS': 43, 'WARN': 6}

## Findings

- **PASS — Experiment config exists**: /media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/configs/x_experiments.json
- **PASS — Experiment config SHA-256**: 2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec
- **PASS — Configured traffic loads**: [1.0, 1.5, 2.0, 3.0]
- **PASS — Freeze record exists**: /media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/phase2/results/v2/freeze.json
- **PASS — Freeze/config hash agreement**: freeze=2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec; actual=2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec
- **PASS — Freeze topology hash recorded**: fe497b0bce187d1b7fe454e92c8778357dfa21ef2587878723d7d43d52824e7e
- **PASS — Freeze core hash recorded**: 2164ee0acd69c28461406400b54143f154833fbbd480a7098e71796e53b7b714
- **PASS — Freeze record fields**: ['config_sha256', 'core_code_sha256', 'created_utc', 'environment', 'heuristic', 'heuristic_source', 'models', 'notes', 'topology_sha256']
- **PASS — Clean confirmatory manifest status**: completed
- **PASS — Clean confirmatory CSV SHA-256**: path=/media/bakhom/New Volume/Research/RL_Sec/practical/files/routing-poisoning-phase2-handover/results/v2/confirmatory_v1/episodes.csv; actual=e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73; expected=e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73
- **PASS — Clean confirmatory row count**: 72000; expected=72000
- **PASS — Clean confirmatory load coverage**: ['1.0', '1.5', '2.0', '3.0']
- **PASS — Clean confirmatory methods**: ['A_600k', 'A_legacy_150k', 'B_legacy_150k', 'greedy_widest', 'minhop', 'shortest_feasible', 'shortest_feasible_k', 'unit_weight_dijkstra', 'util_weight_dijkstra']
- **PASS — Clean confirmatory model seeds**: column=model_seed; values=['-1', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51']
- **PASS — Clean confirmatory duplicate identities**: 0 duplicate rows; identity=['method', 'model_seed', 'load', 'scenario_seed']
- **PASS — Clean manifest/config hash**: 2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec
- **PASS — Clean agent coverage**: {'A_legacy_150k': 10, 'A_600k': 10, 'B_legacy_150k': 10}
- **PASS — Ten seeds per agent**: {'A_600k': [42, 43, 44, 45, 46, 47, 48, 49, 50, 51], 'A_legacy_150k': [42, 43, 44, 45, 46, 47, 48, 49, 50, 51], 'B_legacy_150k': [42, 43, 44, 45, 46, 47, 48, 49, 50, 51]}
- **PASS — Pilot manifest status**: completed
- **PASS — Pilot CSV SHA-256**: path=/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/FINAL_DELIVERABLES/pilot_20261031/episodes.csv; actual=990b21741f7d1ea3a60d506ad6f6467fdb74dd220e01d92b2c87fca98cfcefaf; expected=990b21741f7d1ea3a60d506ad6f6467fdb74dd220e01d92b2c87fca98cfcefaf
- **PASS — Pilot row count**: 16500; expected=16500
- **PASS — Pilot load coverage**: ['2.0']
- **PASS — Pilot methods**: ['A_600k', 'A_legacy_150k', 'B_legacy_150k', 'greedy_widest', 'minhop', 'shortest_feasible', 'shortest_feasible_k', 'unit_weight_dijkstra', 'util_weight_dijkstra']
- **PASS — Pilot model seeds**: column=model_seed; values=['-1', '42', '43', '44']
- **PASS — Pilot duplicate identities**: 0 duplicate rows; identity=['method', 'model_seed', 'load', 'scenario_seed', 'attack', 'eps']
- **PASS — Pilot manifest/config hash**: 2c2a530d649f947b791d33c7c0de58ad9da0e138e9532ca159cf1b24e7eb34ec
- **PASS — Pilot invariant: all_replay_ok**: True
- **PASS — Pilot invariant: all_caps_ok**: True
- **PASS — Pilot perturbation budget**: 5.551115123125783e-17
- **WARN — Pilot scenario scope**: seeds={'scenarios': 'test_poison_v2[0:100) x loads [2.0]'}; exploratory, load 2.0 only
- **PASS — Source file: phase2/src/p2/sim.py**: exists=True; sha256=12e3a20e6e53b60de45204d367ee730e51b7e2205e1265cff10c1da6b307a63f
- **PASS — Source file: phase2/src/p2x/parts.py**: exists=True; sha256=cdbbf1dfba9e77fc9fc111c8652b24b6484de1e96c7ef80923cf2733e0e1a360
- **PASS — Source file: phase2/src/p2x/stats.py**: exists=True; sha256=0eca3bb62e5cf7ead0cffa7692353114f57673c9ad0f8929b183f7974bb65f63
- **PASS — Source file: phase2/src/p2x/manifest.py**: exists=True; sha256=a1ad91b0fc12408b40532e6adfc1390ed2ee968ffc8fd7d75d5a785f42f5afa8
- **PASS — Source file: phase2/scripts/x_07_poison_eval.py**: exists=True; sha256=b827f44646c5e7851d97fa4851464bfe98ee3a531df8b360213eaee402cf789d
- **PASS — Artifact: FINAL_DELIVERABLES/pilot_20261031/PILOT_ANALYSIS.txt**: present
- **PASS — Artifact: FINAL_DELIVERABLES/pilot_20261031/manifest.json**: present
- **PASS — Artifact: FINAL_DELIVERABLES/pilot_20261031/episodes.csv**: present
- **PASS — Artifact: phase2/results/v2/confirmatory_v1/manifest.json**: present
- **PASS — Artifact: phase2/results/v2/freeze.json**: present
- **PASS — Artifact: phase2/docs/THREAT_MODEL.md**: present
- **WARN — Artifact: phase2/README.md**: not found at this path
- **PASS — Artifact: PHASE1_REPORT.md**: present
- **PASS — Artifact: PHASE1_STATUS.md**: present
- **PASS — Artifact: reports/AUDIT_REPORT.md**: present
- **WARN — Phase 2 test suite**: Only known compatibility/boundary failures observed: ['test_episode_metrics_clamp_floating_point_ratio_boundary', 'test_merge_parts_rejects_duplicate_expected_names', 'test_merge_parts_rejects_empty_and_malformed_parts', 'test_merge_parts_requires_exact_expected_files']
- **WARN — Dataset provenance/licensing**: NSFNET-bw provenance and redistribution terms require documentary verification
- **WARN — Poisoning generalization**: Pilot is load-2.0 only with three training seeds; not multi-load confirmation
- **WARN — Statistical inference**: Pilot descriptive means are not a substitute for predeclared inferential analysis

## Interpretation

- Clean confirmatory benchmark and poisoning pilot are separate stages.
- The pilot covers load 2.0 only and three training seeds per agent variant.
- Pilot observations are exploratory, not multi-load confirmation.
- Known test compatibility issues must not be confused with benchmark integrity.
- Dataset provenance/licensing and statistical methodology need human review.
- This audit does not modify frozen source files, experiment outputs, or configuration.
