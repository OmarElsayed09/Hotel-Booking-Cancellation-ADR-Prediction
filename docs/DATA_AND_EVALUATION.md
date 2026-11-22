# Data provenance and evaluation notes

The project contains several hotel reservation CSV datasets and a derived merged file.

## Important limitations

- The input data reflect historical hotel bookings from approximately 2015–2018. They are not representative of current demand without fresh validation.
- Multiple source datasets may overlap. Check exact and near-duplicate bookings **across all datasets** before splitting to avoid data leakage.
- Check target availability at the intended prediction time and remove post-booking or post-cancellation information.
- Keep chronological holdouts, and assess model performance separately by hotel, channel, date range, and relevant populations.
- Evaluate probability calibration and cancellation-class recall, not accuracy alone.
- The repository's stored metrics represent recorded runs; they have not been independently reproduced in this review.
- The merged CSV is a large derived artifact; consider rebuilding it from source inputs and documenting licenses rather than committing additional generated datasets.

## Deployment gate

Before advising revenue-management decisions, validate on recent property-specific data, compare against simple baselines, inspect fairness and error costs, and monitor drift. This is an educational prototype, not a live revenue-management tool.
