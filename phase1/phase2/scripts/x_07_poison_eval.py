#!/usr/bin/env python3
"""Stage F - TEST-TIME TELEMETRY POISONING (prepared; DRY RUN by default, --run to execute). Threat model: docs/THREAT_MODEL.md.
Perturbs ONLY the utilization vector observed by a policy: obs = clip(true + delta, 0, 1), |delta_e| <= eps. True loads, capacities, traffic, reward and
model parameters are untouched; every episode is replay-verified and model parameter hashes are compared before/after.
Gates: presets 'pilot'/'full' need a valid freeze AND a completed confirmatory run (attack matrix is predeclared in the frozen config; no tuning).
Preset 'smoke' (3 scenarios, development set) only validates the pipeline; its numbers must not be interpreted or used to change the matrix.
Clean controls (attack 'clean') and the random_sign noise control at equal eps are always part of the matrix."""
import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
import numpy as np
from p2x import cli
from p2x.cli import log
from p2x.config import agent_models_dir, assert_not_protected, freeze_path, results_dir, scenarios
from p2x.manifest import RunManifest
from p2x.parts import merge_parts, part_name, verify_freeze, write_part
from p2x.policies import build_baselines
from p2x.rollout import InvariantViolation, load_model, param_sha256, run_baseline, run_model
from p2x.telemetry import make_telemetry

COST_S = {"model_replace": 0.08, "model_enhance": 0.04, "baseline": 0.01}      # per episode incl. counterfactual pass; extrapolated from legacy eval_clean.log, indicative only


def matrix_of(cfg, preset):
    p = cfg["poisoning"]["presets"][preset]
    cfgs = [("clean", 0.0)] + [(k, e) for k in cfg["poisoning"]["attacks"] for e in p["eps"]]
    return p, cfgs


def plan(cfg, preset, models_present, base_targets=None):
    p, cfgs = matrix_of(cfg, preset); n_ep = len(p["loads"]) * p["n_per_load"] * len(cfgs)
    nb = len(base_targets if base_targets is not None else cfg["poisoning"]["targets_baselines"]); est = nb * n_ep * COST_S["baseline"]
    for aid, seeds in models_present.items():
        g = next(a["agent"] for a in cfg["confirmatory"]["agents"] if a["id"] == aid); est += len(seeds) * n_ep * COST_S[f"model_{g}"]
    return dict(preset=preset, attack_configs=len(cfgs), episodes_per_target=n_ep, baseline_targets=nb, model_targets={k: len(v) for k, v in models_present.items()}, est_cpu_minutes=round(est / 60, 1))


def execute(cfg, a, net, sha, loader=load_model, hash_fn=param_sha256):
    import csv

    P = cfg["poisoning"]
    p, cfgs = matrix_of(cfg, a.preset)
    smoke = a.preset == "smoke"
    k = P["k_edges"]
    ids = {x["id"]: x for x in cfg["confirmatory"]["agents"]}

    if getattr(a, "run", False) and getattr(a, "targets", None):
        cli.die("--targets is disabled for execution: partial poisoning runs cannot be finalized safely")

    if smoke:
        heur_p = results_dir(cfg, "diag_baselines", "heuristic_selection.json")
        heur = json.loads(heur_p.read_text())["selected"] if heur_p.is_file() else dict(
            p=1.0, floor=0.1, infeasible_multiplier=1.0
        )
        present = {
            t: [
                seed for seed in p["model_seeds"]
                if (agent_models_dir(ids[t]) / f"seed{seed}" / f"{ids[t]['ckpt']}.zip").is_file()
            ]
            for t in P["targets_models"]
        }
    else:
        try:
            fr = verify_freeze(cfg, freeze_path(cfg), sha, ROOT)
        except ValueError as e:
            cli.die(f"freeze check failed: {e}")
        cm = results_dir(cfg, cfg["confirmatory"]["run_id"], "manifest.json")
        if not cm.is_file() or json.loads(cm.read_text()).get("status") != "completed":
            cli.die("confirmatory evaluation has not completed; poisoning is gated on a finished clean stage")
        heur = fr["heuristic"]
        present = {
            t: [
                seed for seed in p["model_seeds"]
                if str(seed) in fr["models"].get(t, {})
            ]
            for t in P["targets_models"]
        }

    present = {
        t: seeds for t, seeds in present.items()
        if seeds and not getattr(a, "baselines_only", False)
    }
    base_targets = list(P["targets_baselines"])

    pl = plan(cfg, a.preset, present, base_targets)
    log.info("PLAN %s", json.dumps(pl))

    if not a.run:
        log.info("DRY RUN - nothing executed. Add --run.")
        return None

    out = Path(a.out or results_dir(cfg, f"poison_{a.preset}")).resolve()
    try:
        assert_not_protected(cfg, out)
    except Exception as e:
        cli.die(f"unsafe poisoning output path: {e}")

    # This stage intentionally does not support resume yet. Never mix old
    # parts with a new run, even when --overwrite was supplied.
    if out.exists():
        if not out.is_dir():
            cli.die(f"poisoning output path is not a directory: {out}")
        if any(out.iterdir()):
            cli.die(
                f"poisoning output directory is not empty: {out}. "
                "Choose a new output directory; automatic resume is disabled."
            )
    else:
        out.mkdir(parents=True, exist_ok=False)

    parts = out / "parts"
    parts.mkdir()
    scens = scenarios(cfg, p["range"], p["loads"], p["n_per_load"], p["role"])
    bl = build_baselines(heur)
    expected_rows_per_target = len(scens) * len(cfgs)

    expected_parts = [
        part_name(target, -1) for target in base_targets
    ] + [
        part_name(target, seed)
        for target, seeds in present.items()
        for seed in seeds
    ]

    expected_targets = {
        (target, -1) for target in base_targets
    } | {
        (target, seed)
        for target, seeds in present.items()
        for seed in seeds
    }

    def episode_rows(target, seed, runner):
        rows = []
        for kind, eps in cfgs:
            for i, load, scenario in scens:
                tele = make_telemetry(kind, eps, k, scenario.seed, load)
                metrics = runner(scenario, tele, kind != "clean")
                if metrics["tele_max_abs_delta"] > eps + 1e-9:
                    raise InvariantViolation(
                        f"perturbation {metrics['tele_max_abs_delta']} exceeds budget {eps}"
                    )
                rows.append(dict(
                    method=target,
                    model_seed=seed,
                    attack=("clean" if kind == "clean" else f"{kind}@{eps:g}"),
                    kind=kind,
                    eps=eps,
                    k_edges=k,
                    scenario_idx=i,
                    scenario_seed=scenario.seed,
                    load=load,
                    **metrics,
                ))
        return rows

    with RunManifest(
        out / "manifest.json",
        f"x_07_poison_eval[{a.preset}]",
        cfg,
        vars(a),
        seeds={"scenarios": f"{p['range']}[0:{p['n_per_load']}) x loads {p['loads']}"},
        extra={
            "topology_sha256": sha,
            "plan": pl,
            "heuristic": heur,
            "status_of_results": "pipeline check only" if smoke else "pre-declared Stage F run",
            "expected_rows_per_target": expected_rows_per_target,
            "expected_parts": sorted(expected_parts),
        },
    ) as mf:
        for target in base_targets:
            part = parts / part_name(target, -1)
            rows = episode_rows(
                target, -1,
                lambda sc, tele, cf, f=bl[target]:
                    run_baseline(net, f, sc, telemetry=tele, counterfactual=cf),
            )
            write_part(part, rows)
            log.info("done baseline %s", target)

        for target, seeds in present.items():
            for seed in seeds:
                model = loader(agent_models_dir(ids[target]), seed, ids[target]["ckpt"])
                before_hash = hash_fn(model)
                group = ids[target]["agent"]
                rows = episode_rows(
                    target, seed,
                    lambda sc, tele, cf, m=model, g=group:
                        run_model(net, g, m, sc, telemetry=tele, counterfactual=cf),
                )
                if hash_fn(model) != before_hash:
                    raise InvariantViolation(
                        f"model parameters changed during poisoned evaluation: {target} seed {seed}"
                    )
                for row in rows:
                    row["param_sha_prefix"] = before_hash[:12]
                    row["param_unchanged"] = True
                write_part(parts / part_name(target, seed), rows)
                log.info("done %s seed %s", target, seed)

        # Enforce the exact part set before using the historical merger.
        actual_parts = {path.name for path in parts.glob("*.csv")}
        expected_part_set = set(expected_parts)

        missing_parts = expected_part_set - actual_parts
        unexpected_parts = actual_parts - expected_part_set

        if missing_parts or unexpected_parts:
            raise InvariantViolation(
                f"part-set mismatch: missing={sorted(missing_parts)}, "
                f"unexpected={sorted(unexpected_parts)}"
            )

        n = merge_parts(parts, out / "episodes.csv")

        # Validate each part's row count and identity before marking the run complete.
        for filename in expected_parts:
            path = parts / filename
            with path.open(newline="", encoding="utf-8") as fh:
                part_rows = list(csv.DictReader(fh))
            if len(part_rows) != expected_rows_per_target:
                raise InvariantViolation(
                    f"{filename}: expected {expected_rows_per_target} rows, got {len(part_rows)}"
                )
            if not part_rows:
                raise InvariantViolation(f"{filename}: empty part")
            identity = {
                (row["method"], int(row["model_seed"]))
                for row in part_rows
            }
            if len(identity) != 1 or next(iter(identity)) not in expected_targets:
                raise InvariantViolation(f"{filename}: target/seed identity mismatch: {identity}")
            if next(iter(identity)) != (
                part_rows[0]["method"], int(part_rows[0]["model_seed"])
            ):
                raise InvariantViolation(f"{filename}: inconsistent target/seed identity")

        expected_total = expected_rows_per_target * len(expected_parts)
        if n != expected_total:
            raise InvariantViolation(
                f"merged row count mismatch: expected {expected_total}, got {n}"
            )

        with (out / "episodes.csv").open(newline="", encoding="utf-8") as fh:
            merged_rows = list(csv.DictReader(fh))

        if len(merged_rows) != expected_total:
            raise InvariantViolation("merged CSV row count does not match the expected total")

        observed_targets = {
            (row["method"], int(row["model_seed"])) for row in merged_rows
        }
        if observed_targets != expected_targets:
            raise InvariantViolation(
                f"target/seed coverage mismatch: expected {expected_targets}, got {observed_targets}"
            )

        replay_ok = all(row["replay_ok"] == "True" for row in merged_rows)
        caps_ok = all(row["caps_ok"] == "True" for row in merged_rows)
        max_delta_over_budget = max(
            float(row["tele_max_abs_delta"]) - float(row["eps"])
            for row in merged_rows
        )

        if not replay_ok:
            raise InvariantViolation("one or more episodes failed replay verification")
        if not caps_ok:
            raise InvariantViolation("one or more episodes failed perturbation-cap verification")
        if max_delta_over_budget > 1e-9:
            raise InvariantViolation(
                f"maximum perturbation exceeded budget by {max_delta_over_budget}"
            )

        mf.add_output(out / "episodes.csv")
        mf.set("n_rows", n)
        mf.set("invariants", dict(
            all_replay_ok=replay_ok,
            all_caps_ok=caps_ok,
            max_delta_over_budget=max_delta_over_budget,
        ))
        mf.set("validated_target_seed_pairs", sorted(
            [list(x) for x in observed_targets]
        ))

    return out


def main():
    ap = cli.add_common(argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter))
    ap.add_argument("--preset", choices=["smoke", "pilot", "full"], default="smoke"); ap.add_argument("--run", action="store_true")
    ap.add_argument("--baselines-only", action="store_true", help="skip trained models (no torch needed)")
    ap.add_argument("--targets", nargs="+", default=None, help="restrict to these target ids (split a long run across processes; parts are resumable)")
    a = ap.parse_args(); cli.setup(a.verbose); cfg = cli.get_cfg(a.config); net, sha = cli.real_network(cfg)
    if a.run and not a.baselines_only:
        try:
            import stable_baselines3  # noqa
        except ImportError:
            cli.die("torch / stable-baselines3 not importable; activate the project venv (or use --baselines-only).")
    execute(cfg, a, net, sha)


if __name__ == "__main__":
    main()
