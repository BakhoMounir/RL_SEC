# Phase 2 Pre-Poisoning Audit

- Timestamp UTC: 20261031T103333Z
- Repository: `/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation`
- Gate status: **BLOCKED**
- PASS: 27
- REVIEW: 10
- FAIL: 4
- Poisoning executed: No
- Training executed: No
- Historical results modified: No

## Check results

- **PASS** — `manifest:diag_checkpoints_enhance/per_model.csv`: SHA-256 verified: 5e918f5e2991681b0d61be14fe59e81011f9b30803330fb13413cf16117bba20
- **PASS** — `manifest:diag_enhance_local/per_model.csv`: SHA-256 verified: c96a859a7da5af37966c6a2e4456a58b5424eebf2c681c2284a1187f4432f3f5
- **PASS** — `manifest:diag_checkpoints_replace/per_model.csv`: SHA-256 verified: 46a46ca578b1173e96bc7d3b95984da12fe9a2a2bf786865f743584b65667510
- **PASS** — `manifest:diag_replace_local/per_model.csv`: SHA-256 verified: f7855d00fd751f0470a21064382a614b42aa495a71d0b19dbd675534d0b7dfee
- **PASS** — `manifest:env_check/checkpoint_integrity.csv`: SHA-256 verified: 3ec3b2168acc49aba757f592f4da305e7d19b0b7caae70dad6454a60c5e4eb55
- **PASS** — `manifest:env_check_local/checkpoint_integrity.csv`: SHA-256 verified: 3ec3b2168acc49aba757f592f4da305e7d19b0b7caae70dad6454a60c5e4eb55
- **PASS** — `restored:diag_checkpoints_enhance/per_model.csv`: Current file matches verified original hash
- **PASS** — `source:diag_checkpoints_enhance/per_model.csv`: Handover source matches expected hash
- **PASS** — `backup:diag_checkpoints_enhance/per_model.csv`: Previous version preserved; SHA-256=0a68a4df13734cb0e5ac27a6e3d156181f4065727a2a389aeb59e1e4cfd69bf9
- **PASS** — `restored:diag_checkpoints_replace/per_model.csv`: Current file matches verified original hash
- **PASS** — `source:diag_checkpoints_replace/per_model.csv`: Handover source matches expected hash
- **PASS** — `backup:diag_checkpoints_replace/per_model.csv`: Previous version preserved; SHA-256=73bffbfe12286e85c765dbbac5e4666eec66f070bde58599b4603bb527ba50e1
- **PASS** — `restored:env_check/checkpoint_integrity.csv`: Current file matches verified original hash
- **PASS** — `source:env_check/checkpoint_integrity.csv`: Handover source matches expected hash
- **PASS** — `backup:env_check/checkpoint_integrity.csv`: Previous version preserved; SHA-256=48230d36e3faf868d23e71b9b0a4367c3fb2b762b5f681a8618dc35e11bcd240
- **PASS** — `confirmatory_csv_hash`: e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73
- **FAIL** — `confirmatory_required_columns`: Missing columns: ['agent', 'scenario_id', 'seed']
- **PASS** — `confirmatory_row_count`: Observed 72000; expected historical benchmark count 72000
- **FAIL** — `confirmatory_duplicate_keys`: 71996
- **FAIL** — `confirmatory_missing_required`: 72000
- **PASS** — `confirmatory_replay`: bad rows=0
- **PASS** — `confirmatory_capacity`: bad rows=0
- **PASS** — `confirmatory_delivery_ratio`: materially out-of-range rows=0
- **REVIEW** — `freeze:phase2/results/v2/freeze.json`: Freeze metadata readable; immutable verification still requires the original freeze verifier and its exact historical inputs
- **REVIEW** — `freeze:FINAL_DELIVERABLES/metadata/freeze.json`: Freeze metadata readable; immutable verification still requires the original freeze verifier and its exact historical inputs
- **PASS** — `git_head`: 8884d1a3a4a68e2945eb71ea2c7fef3d803cbb17
- **REVIEW** — `git_worktree`: Dirty
- **FAIL** — `pytest_full_suite`: Exit code=2; log=/media/bakhom/New Volume/Research/RL_Sec/practical/phase2-validation/FINAL_DELIVERABLES/audit/pre_poisoning_gate_20261031T103333Z/pytest.log

==================================== ERRORS ====================================
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
4 errors in 0.22s

- **PASS** — `final_figures`: 7 PNG files found
- **PASS** — `deliverables:FINAL_DELIVERABLES`: 129 files inventoried
- **PASS** — `deliverables:phase2/FINAL_DELIVERABLES`: 14 files inventoried
- **REVIEW** — `poison_run:poison_pilot`: status=completed; manifest=FINAL_DELIVERABLES/audit/prewrite_20261029_190553/poison_pilot/manifest.json
- **REVIEW** — `poison_run:poison_pilot_fresh`: status=completed; manifest=FINAL_DELIVERABLES/audit/prewrite_20261029_190553/poison_pilot_fresh/manifest.json
- **REVIEW** — `poison_run:full`: status=failed; manifest=FINAL_DELIVERABLES/audit/full_poisoning_20261028T223445Z/full/manifest.json
- **REVIEW** — `poison_run:poison_smoke`: Not found at expected path
- **REVIEW** — `poison_run:poison_A600k_seed42_exploratory`: Not found at expected path
- **PASS** — `documentation:DATASET_PROVENANCE.md`: Exists; 1420 characters; review terms found=[]
- **PASS** — `documentation:02_EXPERIMENT_PROTOCOL.md`: Exists; 5564 characters; review terms found=[]
- **PASS** — `documentation:SCIENTIFIC_REVIEW_CHECKLIST.md`: Exists; 2468 characters; review terms found=[]
- **REVIEW** — `runner:x_07_poison_eval.py`: Not found
- **REVIEW** — `runner:rollout.py`: Source exists; output-part reuse, validation, and merge behavior require explicit code review

## Interpretation

This audit checks available artifacts and reproducibility metadata. It does not establish dataset redistribution rights, scientific validity, convergence, or permission to begin poisoning experiments.

A human review of all REVIEW items is required before poisoning.
