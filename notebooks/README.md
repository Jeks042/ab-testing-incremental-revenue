# Analytical Notebooks

The notebooks document the completed analytical workflow behind the experiment decision. Core calculations are implemented in reusable functions under `src/`, while the notebooks provide a transparent review of the evidence and interpretation.

## `01_data_validation.ipynb`

This notebook establishes whether the randomised experiment is suitable for causal comparison before any treatment recommendation is made.

The review reconciles the 64,000-row source population, checks treatment allocation, missing values, outcome consistency and baseline balance, and records the decision to retain all source rows in the intention-to-treat population.

**Conclusion:** the experiment passed the integrity review and was suitable for treatment-effect estimation.

Supporting decision record: [validation findings](../reports/validation_findings.md).

## `02_experiment_analysis.ipynb`

This notebook evaluates the commercial effect of both email treatments relative to No E-Mail.

The analysis covers visit rate, conversion rate and spend per eligible customer, with confidence intervals, hypothesis tests and multiplicity-aware interpretation. Spend per eligible customer is treated as the primary commercial outcome.

**Key result:** Men's E-Mail increased spend by approximately **£0.77 per eligible customer** versus No E-Mail; Women's E-Mail increased spend by approximately **£0.42**. Men's E-Mail was also stronger in the direct treatment comparison.

Supporting decision record: [main treatment-effect findings](../reports/main_effect_findings.md).

## `03_targeting_policy.ipynb`

This notebook tests whether customer-level personalisation creates enough incremental value to replace the strongest fixed treatment.

The targeting analysis uses pre-treatment variables only, separates model fitting from held-out policy evaluation and compares personalised policies directly with Men's E-Mail to all. Inverse-propensity, doubly robust and bootstrap estimates are used to evaluate policy value rather than relying on predictive accuracy alone.

**Conclusion:** the personalised policies had positive point estimates but did not reliably outperform Men's E-Mail to all. The current model was therefore not approved for deployment.

Supporting decision record: [targeting-policy findings](../reports/targeting_findings.md).

## Segment analysis

Pre-specified segment and interaction analysis is implemented through `scripts/run_segment_analysis.py` and `src/segment_analysis.py` rather than a separate presentation notebook.

The interaction tests did not provide reliable evidence for a manually constructed segment-specific treatment rule after multiplicity adjustment.

Supporting decision record: [segment-analysis findings](../reports/segment_findings.md).

## Reproducibility

The notebooks are presentation and review layers, not the sole location of analytical logic. Reusable validation, treatment-effect, commercial and policy functions are maintained in `src/`, and the GitHub Actions workflows reproduce the key analysis tables from the published source data.
