# RL_SEC: telemetry poisoning of RL-based routing

Research code, audit trail and paper sources for studying telemetry-poisoning attacks on
PPO-based routing agents (NSFNet-style topologies, SDN/WAN traffic engineering).

**Status:** TODO. State exactly which stages are complete (clean confirmatory stage; poisoning stage:
smoke / pilot / full) and cite `docs/RESULTS_INDEX.md`. Pilot results are not confirmatory results.

## Repository layout
| Path | Contents |
|------|----------|
| `phase1/` | Original prototype, checksummed originals (`originals/`), re-run of the original script (`audit/original_script_rerun/`) |
| `phase2/src/p2`, `phase2/src/p2x` | Simulator and the pre-specified evaluation pipeline |
| `phase2/scripts/` | `x_00 ... x_09` pipeline stages (audit, diagnostics, train, freeze, confirmatory eval, poisoning eval, analysis, plots) |
| `phase2/tests/`, `phase2/tools/` | Test suite and the final clean-stage audit tool |
| `phase2/configs/` | Experiment configuration |
| `phase2/docs/` | Protocol, threat model, methodology audit, verification and provenance notes |
| `phase2/results/v2/` | Frozen clean-stage evidence: `freeze.json`, `SHA256SUMS.txt`, audits, final figures |
| `phase2/results/confirmatory_v1/` | Confirmatory episodes with BOTH analyses: original and `analysis_v2_valid_tests` |
| `phase2/results/deliverables/` | Final reports, manifests, tables and figures from the poisoning/clean stages |
| `docs/` | Deviations, reproduction steps, results index, audit evidence |
| `paper/` | Manuscript sources |

## Read this before citing any result
`docs/DEVIATIONS.md` lists every departure from the pre-specified protocol, including the post-hoc
revision of the statistical tests, post-freeze code edits, and which poisoning runs are pilots.

## Reproduce
See `docs/REPRODUCING.md`. `make test` runs the tests; `make verify` checks the frozen evidence checksums.
`MANIFEST_sha256.txt` lists the hash of every file in this repository.

## Data and licenses
Datasets are not redistributed. See `DATA_LICENSES.md`. Code license: TODO (add a `LICENSE` file before wider release).

## Citation
See `CITATION.cff`.
