# Reproducing

Python version / OS: TODO.   Install: `pip install -r requirements.txt`.

Order (run from `phase2/`):
1. `python scripts/x_00_static_audit.py`
2. `python scripts/x_01_check_env_and_checkpoints.py`
3. `python scripts/x_02_diag_checkpoints.py`
4. `python scripts/x_03_diag_baselines.py`
5. `python scripts/x_04_train_agent_a.py`
6. `python scripts/x_05_freeze.py`
7. `python scripts/x_06_confirmatory_eval.py --run`
8. `python scripts/x_07_poison_eval.py --preset <smoke|pilot|full> --run`
9. `python scripts/x_08_analyze.py`
10. `python scripts/x_09_plot_results.py`

Tests: `pytest phase2/tests`.   Verify evidence: `cd phase2/results/v2 && sha256sum -c SHA256SUMS.txt`.
Exact flags: TODO (copy from `docs/02_EXPERIMENT_PROTOCOL.md`).
