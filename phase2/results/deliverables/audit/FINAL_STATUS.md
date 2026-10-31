# Phase 2 final status

## Verified
- Frozen checkpoint records: 30/30 matched their recorded SHA-256 hashes.
- Clean confirmatory CSV: 72,000 rows; original SHA-256:
  e5257ccfa3e8b56661f35833fc894ee9b0bda06c2adf79f25552d442d7f83b73
- Completed poisoning pilot: 16,500 rows; original SHA-256:
  990b21741f7d1ea3a60d506ad6f6467fdb74dd220e01d92b2c87fca98cfcefaf

## Not completed or unresolved
- Full multi-load poisoning evaluation did not complete successfully.
- The original code-tree hash and recomputed code-tree hash discrepancy remains unresolved.
- Dataset provenance and redistribution/licensing terms require verification.
- The completed poisoning pilot is exploratory/pilot evidence, not proof of general robustness.
- Do not claim exact reproducibility until the code-tree discrepancy is resolved.
- Do not present failed runs as experimental results.
