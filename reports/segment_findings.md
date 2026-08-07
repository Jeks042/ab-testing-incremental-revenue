# Treatment Selection and Segment Evidence

## Decision

**Men's E-Mail outperformed Women's E-Mail overall, while the segment analysis did not provide reliable evidence for a rule-based targeting strategy.**

The direct treatment comparison supported Men's E-Mail on visit rate, conversion rate and spend per eligible customer. Pre-specified interaction tests across recency, prior spend, channel, geography, customer status and merchandise affinity did not remain significant after multiplicity adjustment.

Men's E-Mail therefore remained the fixed operating benchmark, and no hand-built segment rule was approved.

## Direct Men's-versus-Women's comparison

| Outcome | Men's E-Mail | Women's E-Mail | Advantage for Men's | 95% confidence interval | Holm-adjusted p-value |
|---|---:|---:|---:|---:|---:|
| Visit rate | 18.28% | 15.14% | +3.14 percentage points | +2.43 to +3.84 points | < 0.001 |
| Conversion rate | 1.25% | 0.88% | +0.37 percentage points | +0.17 to +0.56 points | < 0.001 |
| Spend per eligible customer | £1.423 | £1.077 | +£0.345 | +£0.044 to +£0.666 | 0.0305 |

Spend per eligible customer was the primary commercial outcome. Its confidence interval excluded zero after adjustment across the three direct comparisons.

At a **40% contribution margin**, and assuming equal delivery cost for the two treatments, the £0.345 spend advantage equates to approximately **£138 additional contribution per 1,000 contacted customers**, before fixed or treatment-specific creative costs.

## Segment evidence

A segment-specific operating rule would require evidence that treatment effects genuinely differed across segment levels. The joint interaction tests did not support that conclusion.

| Segment variable | Joint interaction p-value | Holm-adjusted p-value | Decision |
|---|---:|---:|---|
| Customer status | 0.0516 | 0.3094 | No reliable heterogeneity evidence |
| History segment | 0.0526 | 0.3094 | No reliable heterogeneity evidence |
| Merchandise affinity | 0.1417 | 0.5667 | No reliable heterogeneity evidence |
| Channel | 0.3151 | 0.9454 | No reliable heterogeneity evidence |
| Geography type | 0.4313 | 0.9454 | No reliable heterogeneity evidence |
| Recency band | 0.6450 | 0.9454 | No reliable heterogeneity evidence |

None of the six pre-specified segment variables provided interaction evidence strong enough to justify changing treatment by segment.

## Exploratory patterns

Some subgroup point estimates were commercially interesting, including stronger observed Men's E-Mail effects among multichannel customers, recently active customers, new customers and customers with both men's and women's merchandise affinity.

Those patterns were retained as exploratory evidence only. They were not converted into operating rules because the corresponding interaction tests did not establish reliable treatment-effect differences.

The same principle applied to negative Women's E-Mail estimates in selected prior-spend bands: the confidence intervals included zero and the overall history-segment interaction was not reliable.

## Policy implication

The segment analysis established a clear hierarchy:

1. **Men's E-Mail** remained the strongest fixed treatment for eligible customers when campaign economics were positive.
2. **Women's E-Mail** remained value-creating relative to No E-Mail but was inferior overall.
3. **Rule-based segmentation** was not supported by the interaction evidence.
4. **Model-based personalisation** required separate held-out policy evaluation before any deployment decision.

The held-out targeting decision is documented in [`targeting_findings.md`](targeting_findings.md).

## Decision boundaries

Segment estimates are less precise than the overall treatment effects because the randomised sample is divided into smaller cells. Multiple subgroup comparisons also increase the risk of apparently attractive but non-replicable patterns. For that reason, subgroup point estimates were not treated as deployment evidence without supporting interaction tests.
