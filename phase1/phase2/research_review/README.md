# Phase 2 research review package

- `generate_figures.py`: generates figures from the confirmatory CSV.
- `data_schema.json`: input schema, data types, missingness, and inferred columns.
- `row_counts_by_method_load.csv`: evaluation coverage.
- `paper_text/`: text extracted from supplied PDFs when `pdftotext` was available.
- `DATASET_PROVENANCE.md`: provenance and licensing status.
- `SCIENTIFIC_REVIEW_CHECKLIST.md`: review tasks and sign-off checklist.

Figures are generated under `phase2/results/v2/figures_final/`.
Review `data_schema.json` before interpreting any plot. If the script cannot infer
a metric, it skips that figure rather than inventing data.
