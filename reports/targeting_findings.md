# Held-Out Targeting and Policy-Value Findings

## Decision summary

**Do not deploy the personalised targeting model. Retain Men's E-Mail to all eligible customers as the evidence-based operating policy, subject to the previously established break-even economics.**

The personalised policies produced modest positive point estimates on the 30% randomized holdout, but neither improvement was statistically reliable relative to Men's E-Mail to all:

- highest predicted spend policy: **+28.7 profit units per 1,000 customers**, 95% bootstrap interval **-120.2 to +170.6**;
- profit-aware policy: **+18.3 per 1,000**, 95% bootstrap interval **-129.1 to +155.4**.

Both intervals include zero and economically meaningful negative values. The experiment therefore does not support replacing the strongest fixed policy with model-based personalisation.

## Holdout design

| Population | Customers | Share |
|---|---:|---:|
| Training | 44,800 | 70% |
| Randomized holdout | 19,200 | 30% |

The split was stratified by randomized treatment arm. All policy-value comparisons were evaluated on the holdout rather than the data used to fit the outcome models.

## Reference policy comparison

Reference commercial assumptions:

- contribution margin: **40%**;
- contact cost: **0.10 per contacted customer**.

| Policy | Treated share | DR spend per customer | DR profit per 1,000 | Uplift vs Men's-send-to-all |
|---|---:|---:|---:|---:|
| Model: highest predicted spend | 87.84% | 1.270 | 420.2 | +28.7 |
| Model: profit-aware | 80.58% | 1.226 | 409.8 | +18.3 |
| Men's E-Mail to all | 100.00% | 1.229 | 391.6 | Benchmark |
| Women's E-Mail to all | 100.00% | 1.191 | 376.6 | -15.0 |
| No E-Mail to all | 0.00% | 0.740 | 296.1 | -95.5 |

The point estimates rank the model policies above the fixed Men's policy, but policy selection must be based on uncertainty as well as ranking.

## Bootstrap uncertainty versus Men's E-Mail to all

| Policy | Point uplift per 1,000 | 95% bootstrap interval | Decision |
|---|---:|---:|---|
| Highest predicted spend | +28.7 | -120.2 to +170.6 | Not reliable |
| Profit-aware | +18.3 | -129.1 to +155.4 | Not reliable |
| Women's E-Mail to all | -15.0 | -216.7 to +174.4 | Holdout comparison is imprecise |
| No E-Mail to all | -95.5 | -253.9 to +105.3 | Holdout comparison is imprecise |

The full 64,000-customer experiment previously established that Men's E-Mail outperformed Women's E-Mail and No E-Mail overall. These wider holdout intervals do not reverse that evidence; they show that a 19,200-customer policy-evaluation sample is noisy for rare, highly skewed spend outcomes.

## Profit-aware recommendations

At the reference assumptions, the model recommended:

| Recommended arm | Customers | Share |
|---|---:|---:|
| Men's E-Mail | 10,232 | 53.29% |
| Women's E-Mail | 5,239 | 27.29% |
| No E-Mail | 3,729 | 19.42% |

This allocation is a model output, not a deployable customer policy. The holdout evidence does not show that these assignments outperform Men's E-Mail to all with sufficient confidence.

## Capacity-constrained policies

| Maximum contact capacity | Actual treated share | DR profit per 1,000 | Point uplift vs Men's-send-to-all |
|---|---:|---:|---:|
| 10% | 10.00% | 294.5 | -97.0 |
| 25% | 25.00% | 347.8 | -43.8 |
| 50% | 50.00% | 357.0 | -34.6 |
| 75% | 75.00% | 416.2 | +24.7 |
| 100% | 80.58% | 409.8 | +18.3 |

The 75% policy has the highest point estimate, but no paired bootstrap interval was produced for each capacity point. It must therefore remain exploratory. The results do show that aggressive capacity reduction to 50% or below would sacrifice expected profit under the reference assumptions.

## Commercial sensitivity

Across contribution margins of 25%, 40% and 60% and contact costs of 0.05, 0.10 and 0.20, the profit-aware policy had positive point-estimate uplift over Men's-send-to-all ranging from approximately **10.0 to 54.9 per 1,000 customers**.

These are sensitivity point estimates, not proof of robust improvement. Reusing the same fitted policy framework across scenarios does not remove the uncertainty shown by the bootstrap comparison.

## Model diagnostics

| Arm | Holdout customers | Observed mean spend | Predicted mean spend | MAE | RMSE |
|---|---:|---:|---:|---:|---:|
| No E-Mail | 6,392 | 0.739 | 0.630 | 1.353 | 10.690 |
| Men's E-Mail | 6,392 | 1.241 | 1.541 | 2.740 | 15.668 |
| Women's E-Mail | 6,416 | 1.196 | 1.030 | 2.200 | 16.415 |

Spend is rare, zero-inflated and highly skewed, which produces large prediction errors relative to the mean. The Men's model overpredicts average spend on its observed holdout arm, while the No E-Mail and Women's models underpredict. Doubly robust policy evaluation reduces reliance on the models but does not make unstable treatment ranking disappear.

## Feature importance

Historical spend contributed approximately **49.4%** of mean model importance and recency approximately **18.0%**. The remaining importance was distributed across customer status, merchandise affinity, channel, geography and history bands.

Feature importance describes how the predictive models split the data. It is not evidence that a variable causes treatment response or that it should be used as a manual targeting rule.

## Final targeting conclusion

1. Men's E-Mail remains the strongest fixed policy supported by the full randomized experiment.
2. The personalised policies are promising only as exploratory research.
3. Their estimated profit uplift is too imprecise for deployment.
4. The model should not be presented as having created proven incremental revenue.
5. A future experiment could prospectively randomize customers between the Men's-send-to-all policy and the candidate personalised policy to measure policy lift directly.
6. Until then, the operational recommendation is Men's E-Mail to all customers for whom the campaign clears the documented margin and contact-cost threshold.
