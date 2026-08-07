# Treatment Effect and Commercial Value

## Decision

**Men's E-Mail was the strongest treatment against the No E-Mail control and provided the clearest commercial case under the tested economics.**

Both active treatments increased visits, conversions and spend per eligible customer. Men's E-Mail produced the larger effect on every primary and supporting outcome and retained a wider margin for delivery cost.

## Observed treatment performance

| Experiment arm | Customers | Visit rate | Conversion rate | Spend per customer | Average order value among converters |
|---|---:|---:|---:|---:|---:|
| No E-Mail | 21,306 | 10.62% | 0.57% | £0.653 | £114.00 |
| Men's E-Mail | 21,307 | 18.28% | 1.25% | £1.423 | £113.53 |
| Women's E-Mail | 21,387 | 15.14% | 0.88% | £1.077 | £121.89 |

The higher value from Men's E-Mail came primarily from increased response rather than larger orders. Women's E-Mail had the highest observed average order value among converters, but that descriptive difference is not itself a causal treatment effect.

## Incremental effects versus No E-Mail

### Men's E-Mail

| Outcome | Absolute effect | Relative lift | 95% confidence interval | Adjusted p-value |
|---|---:|---:|---:|---:|
| Visit rate | +7.66 percentage points | +72.1% | +7.00 to +8.32 points | < 0.001 |
| Conversion rate | +0.68 percentage points | +118.8% | +0.50 to +0.86 points | < 0.001 |
| Spend per eligible customer | +£0.770 | +117.9% | +£0.484 to +£1.052 | < 0.001 |

Approximately **13 customers** needed to receive Men's E-Mail for one additional visit and **147 customers** for one additional conversion.

### Women's E-Mail

| Outcome | Absolute effect | Relative lift | 95% confidence interval | Adjusted p-value |
|---|---:|---:|---:|---:|
| Visit rate | +4.52 percentage points | +42.6% | +3.89 to +5.16 points | < 0.001 |
| Conversion rate | +0.31 percentage points | +54.3% | +0.15 to +0.47 points | < 0.001 |
| Spend per eligible customer | +£0.424 | +65.0% | +£0.152 to +£0.686 | 0.0011 |

Approximately **22 customers** needed to receive Women's E-Mail for one additional visit and **321 customers** for one additional conversion.

## Commercial economics

The commercial model converts incremental spend into contribution after contact cost. Fixed campaign costs and any unobserved treatment-specific fulfilment or incentive costs are outside the model.

### Break-even contact cost per customer

| Treatment | Effect basis | 25% margin | 40% margin | 60% margin |
|---|---|---:|---:|---:|
| Men's E-Mail | Point estimate | £0.192 | £0.308 | £0.462 |
| Men's E-Mail | Lower 95% confidence bound | £0.121 | £0.194 | £0.290 |
| Women's E-Mail | Point estimate | £0.106 | £0.170 | £0.255 |
| Women's E-Mail | Lower 95% confidence bound | £0.038 | £0.061 | £0.091 |

At a **40% contribution margin** and **£0.10 contact cost per customer**, estimated incremental profit was approximately:

- **Men's E-Mail: £208 per 1,000 eligible customers**;
- **Women's E-Mail: £70 per 1,000 eligible customers**.

Using the lower 95% confidence bound for the spend effect, estimated profit remained positive at approximately **£94 per 1,000** for Men's E-Mail and **£11 per 1,000** for Women's E-Mail.

## Business interpretation

Men's E-Mail provided the stronger treatment-versus-control evidence and the wider commercial buffer. The campaign decision should therefore be based on incremental contribution rather than total observed revenue in the treatment arms.

The direct Men's-versus-Women's comparison and the decision on customer segmentation are recorded separately in [`segment_findings.md`](segment_findings.md). The completed analysis ultimately confirmed Men's E-Mail as the strongest fixed treatment.
