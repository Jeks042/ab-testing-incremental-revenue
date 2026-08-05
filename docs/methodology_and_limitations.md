# Methodology and Limitations

## Experimental population

The analysis uses all 64,000 assigned customers from the Hillstrom email experiment. No records were excluded from the primary intention-to-treat population.

## Integrity checks

The workflow validates:

- expected schema and row count;
- missing values and invalid binary values;
- non-negative monetary fields;
- consistency between visit, conversion and spend;
- treatment allocation through a chi-square sample-ratio test;
- baseline balance through standardized mean differences and categorical distributions.

Exact row matches are retained because the source has no customer identifier and matching observed fields do not prove duplicate customers.

## Average treatment effects

Binary outcomes are estimated through absolute risk differences, confidence intervals and two-sample proportion tests. Spend per eligible customer is estimated through differences in means, Welch tests and bootstrap confidence intervals.

Spend is the pre-specified primary commercial outcome. Visit and conversion are supporting outcomes. Related comparison families use Holm adjustment.

## Direct treatment comparison

Men's E-Mail and Women's E-Mail are compared directly. Superiority is not inferred from separate treatment-versus-control significance tests.

## Segment analysis

Segments are defined only from pre-treatment fields. Treatment heterogeneity is evaluated through joint treatment-by-segment interaction tests. Within-segment significance alone is not treated as evidence that segment effects differ.

## Commercial model

Incremental profit is calculated as:

```text
incremental spend per customer × contribution margin
- contact cost
- any additional variable or fixed campaign cost
```

Published commercial results state the margin and contact-cost assumptions. Observed arm revenue is not labelled incremental.

## Targeting analysis

The targeting stage uses a treatment-stratified 70/30 train-holdout split. Separate outcome models are fitted for No E-Mail, Men's E-Mail and Women's E-Mail using pre-treatment features only.

Candidate policies are evaluated on the randomized holdout through inverse-propensity and doubly robust estimators. Paired bootstrap intervals compare policy profit with Men's-send-to-all.

Predictive diagnostics and feature importance are reported separately from policy-value evidence.

## Key limitations

1. The experiment covers one retailer, one campaign context and one outcome window.
2. The source does not include a unique customer identifier.
3. Spend is rare, zero-inflated and highly skewed.
4. The direct experiment supports average treatment effects more strongly than customer-level treatment ranking.
5. Commercial conclusions depend on contribution margin, contact cost and unobserved treatment-specific costs.
6. Segment and targeting analyses divide the available sample and therefore have lower precision than the overall experiment.
7. A positive model-policy point estimate does not establish deployable incremental profit when its interval includes zero.
8. Prospective randomization is required before claiming that the candidate personalised policy improves profit in operation.
