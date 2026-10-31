# Phase 2 scientific review checklist

This checklist is a review record, not a claim that the study has passed review.

## Literature and method alignment
- [ ] Extract and review each supplied PDF; record exact bibliographic metadata.
- [ ] Identify each paper's topology, traffic model, objective, baselines, RL algorithm,
      seeds, training budget, metrics, and statistical methods.
- [ ] Separate findings reported by prior papers from results generated in this project.
- [ ] Verify each claim against the paper text, not its title or abstract alone.

## Dataset and environment
- [ ] Verify the exact NSFNET-bw archive/version and file-level provenance.
- [ ] Resolve the raw dataset license or document the maintainer response.
- [ ] Document the 14-node / 21-link topology and all capacity units.
- [ ] Explain how the 60 flows per episode and synthetic traffic scenarios were generated.
- [ ] Verify load definitions and the independence of train, validation, and test scenarios.
- [ ] Record all simulator assumptions, routing constraints, seeds, and tie-breaking rules.

## Methods and reproducibility
- [ ] Verify frozen config hash and complete core-code hash using the project's own freeze function.
- [ ] Verify checkpoint hashes, training steps, early-stopping rule, and framework versions.
- [ ] Confirm the confirmatory CSV contains the intended methods, loads, and scenario IDs.
- [ ] Confirm the preregistered analysis script generated the reported statistics.
- [ ] Re-run no training unless a specific reproducibility defect is identified.

## Statistics and interpretation
- [ ] Confirm the unit of analysis and pairing structure.
- [ ] Check confidence-interval construction and whether scenarios/seeds are independent.
- [ ] Verify primary comparisons, multiple-comparison handling, and effect sizes.
- [ ] Report negative and inconclusive results as well as improvements.
- [ ] Do not claim the DRL method is superior to a baseline where it is not.
- [ ] Distinguish a plateau under an early-stopping rule from proof of convergence.

## Figures and release
- [ ] Generate plots only from recorded data with units and sample counts.
- [ ] Keep exploratory analyses clearly labelled as exploratory.
- [ ] Reconcile every manuscript number with a saved analysis table.
- [ ] Include environment, configuration, data provenance, and license notes.
- [ ] Do not begin poisoning experiments until the clean baseline is scientifically reviewed.
