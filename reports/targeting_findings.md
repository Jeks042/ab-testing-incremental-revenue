# Targeting Policy Evaluation

## Decision

**Do not deploy the personalised targeting model. Men's E-Mail to all eligible customers remains the evidence-based operating policy when campaign economics clear the established threshold.**

The personalised policies ranked slightly above Men's-send-to-all on point estimates, but neither demonstrated a sufficiently precise profit advantage on held-out randomised data. The evidence supports continued experimentation, not production deployment.

## Held-out policy comparison

The targeting analysis used a treatment-stratified **70/30 train-holdout split**. Outcome models were fitted on 44,800 customers and policy value was evaluated on **19,200 unseen randomised customers**.

Reference commercial assumptions:

- contribution margin: **40%**;
- contact cost: **£0.10 per contacted customer**.

| Policy | Treated share | DR spend per customer | DR profit per 1,000 | Uplift vs Men's-send-to-all |
|---|---:|---:|---:|---:|
| Highest predicted spend | 87.84% | £1.270 | £420.2 | +£28.7 |
| Profit-aware | 80.58% | £1.226 | £409.8 | +£18.3 |
| Men's E-Mail to all | 100.00% | £1.229 | £391.6 | Benchmark |
| Women's E-Mail to all | 100.00% | £1.191 | £376.6 | -£15.0 |
| No E-Mail to all | 0.00% | £0.740 | £296.1 | -£95.5 |

Point estimates alone did not determine the deployment decision.

## Uncertainty versus the fixed benchmark

| Policy | Point uplift per 1,000 | 95% bootstrap interval | Decision |
|---|---:|---:|---|
| Highest predicted spend | +£28.7 | -£120.2 to +£170.6 | Do not deploy |
| Profit-aware | +£18.3 | -£129.1 to +£155.4 | Do not deploy |
| Women's E-Mail to all | -£15.0 | -£216.7 to +£174.4 | Holdout estimate imprecise |
| No E-Mail to all | -£95.5 | -£253.9 to +£105.3 | Holdout estimate imprecise |

Both personalised-policy intervals include zero and economically meaningful downside. This is insufficient evidence to replace the strongest fixed treatment.

The wider holdout intervals for Women's E-Mail and No E-Mail do not overturn the full-experiment results, which established Men's E-Mail as the strongest overall treatment. They reflect the greater uncertainty of policy evaluation on a smaller sample with a rare, highly skewed spend outcome.

## Profit-aware recommendation mix

At the reference assumptions, the model assigned:

| Recommended arm | Customers | Share |
|---|---:|---:|
| Men's E-Mail | 10,232 | 53.29% |
| Women's E-Mail | 5,239 | 27.29% |
| No E-Mail | 3,729 | 19.42% |

This allocation is a model recommendation, not an approved operating policy. The held-out evidence did not demonstrate that these assignments reliably improve profit over Men's E-Mail to all.

## Capacity analysis

| Maximum contact capacity | Actual treated share | DR profit per 1,000 | Point uplift vs Men's-send-to-all |
|---|---:|---:|---:|
| 10% | 10.00% | £294.5 | -£97.0 |
| 25% | 25.00% | £347.8 | -£43.8 |
| 50% | 50.00% | £357.0 | -£34.6 |
| 75% | 75.00% | £416.2 | +£24.7 |
| 100% | 80.58% | £409.8 | +£18.3 |

The 75% capacity policy had the highest point estimate, but a policy-specific paired bootstrap interval was not available for each capacity point. It was therefore retained as exploratory evidence rather than an operating recommendation.

The analysis also showed that restricting contact to 50% of customers or fewer would reduce expected profit under the reference assumptions.

## Commercial sensitivity

Across contribution margins of **25%, 40% and 60%** and contact costs of **£0.05, £0.10 and £0.20**, the profit-aware model produced positive point-estimate uplift over Men's-send-to-all ranging from approximately **£10 to £55 per 1,000 customers**.

These sensitivity results show how the ranking changes under different business assumptions; they do not remove the uncertainty observed in the bootstrap evaluation.

## Model evidence

Spend was rare, zero-inflated and highly skewed, which limited the precision of customer-level treatment ranking.

| Arm | Holdout customers | Observed mean spend | Predicted mean spend | MAE | RMSE |
|---|---:|---:|---:|---:|---:|
| No E-Mail | 6,392 | £0.739 | £0.630 | 1.353 | 10.690 |
| Men's E-Mail | 6,392 | £1.241 | £1.541 | 2.740 | 15.668 |
| Women's E-Mail | 6,416 | £1.196 | £1.030 | 2.200 | 16.415 |

Historical spend accounted for approximately **49.4%** of mean model feature importance and recency for approximately **18.0%**. These values describe predictive model behaviour; they are not evidence that those variables cause treatment response.

## Operating implication

- Keep **Men's E-Mail to all eligible customers** as the operating benchmark when its incremental contribution exceeds campaign cost.
- Keep the personalised model in research rather than production.
- Do not present the model as having generated proven incremental revenue.
- If personalisation is revisited, test the candidate policy prospectively against Men's-send-to-all through direct randomisation and evaluate incremental profit as the decision metric.
