# Reproducing evidence

## Model and dataset tests

The `model-unit-tests.yml` workflow installs the project's requirements and runs `tests/test_prediction.py`, including booking validation, batch inference with controlled models, and time-splitting checks.

## Existing metrics

`models/metrics_summary.json` contains historical recorded metrics; this review has **not retrained or independently replicated** those numbers. `python scripts/verify_metrics.py` writes an auditable SHA256 and metadata file. That proves which metrics file was inspected, **not** that the values are correct.

To reproduce predictive performance, execute the training pipeline in a documented Python environment against the versioned source datasets, then compare the resulting artifacts to the original metrics with the same chronological split. Document any difference and test for cross-source overlap.

## Demo captures

Launch the FastAPI UI with the project's README commands after training or providing trusted local model artifacts, then capture actual browser screenshots. Do not present the UI screenshot as evidence of accurate predictions unless you also test a real input-output interaction.

No synthetic prediction screenshots or invented measured scores are included here.
