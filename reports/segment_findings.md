# Direct Treatment Comparison and Segment Findings

## Decision summary

**Men's E-Mail is statistically superior to Women's E-Mail on visit rate, conversion rate and spend per eligible customer in the overall experiment.**

However, the pre-specified segment interaction tests do not provide reliable evidence that treatment effects differ across recency, prior-spend band, channel, geography, customer status or merchandise affinity after multiplicity adjustment.

The project should therefore retain **Men's E-Mail as the default fixed policy** and should not implement a hand-built segment rule from these subgroup tables. The next stage will evaluate model-based and capacity-constrained policies on held-out randomized data.

## Direct Men's-versus-Women's comparison

| Outcome | Men's E-Mail | Women's E-Mail | Absolute advantage for Men's | Relative advantage | 95% confidence interval | Holm-adjusted p-value |
|---|---:|---:|---:|---:|---:|---:|
| Visit rate | 18.28% | 15.14% | +3.14 percentage points | +20.7% | +2.43 to +3.84 points | < 0.001 |
| Conversion rate | 1.25% | 0.88% | +0.37 percentage points | +41.8% | +0.17 to +0.56 points | < 0.001 |
| Spend per eligible customer | 1.423 | 1.077 | +0.345 | +32.1% | +0.044 to +0.666 | 0.0305 |

The spend comparison is the most important result because spend per eligible customer is the pre-specified primary commercial outcome. Its confidence interval excludes zero and remains significant after adjusting across the three direct outcome comparisons.

If both treatments have the same delivery cost, the additional spend advantage of Men's E-Mail translates to approximately **0.138 additional contribution per contacted customer at a 40% contribution margin**, or about **138 per 1,000 customers**, before fixed or treatment-specific creative costs.

## Segment interaction evidence

A segment-specific policy requires evidence that treatment effects differ across segment levels, not merely that an effect is statistically significant inside one subgroup.

| Segment variable | Joint interaction p-value | Holm-adjusted p-value | Interpretation |
|---|---:|---:|---|
| Customer status | 0.0516 | 0.3094 | Suggestive before adjustment, not reliable after multiplicity control |
| History segment | 0.0526 | 0.3094 | Suggestive before adjustment, not reliable after multiplicity control |
| Merchandise affinity | 0.1417 | 0.5667 | No reliable heterogeneity evidence |
| Channel | 0.3151 | 0.9454 | No reliable heterogeneity evidence |
| Geography type | 0.4313 | 0.9454 | No reliable heterogeneity evidence |
| Recency band | 0.6450 | 0.9454 | No reliable heterogeneity evidence |

None of the joint interaction tests remains significant after adjustment across the six pre-specified segment variables.

## Exploratory subgroup patterns

Several subgroup point estimates are commercially interesting, including:

- Men's E-Mail among customers with both men's and women's prior merchandise affinity;
- Men's E-Mail among multichannel customers;
- Men's E-Mail among customers active within the previous three months;
- positive effects for both treatments among customers with prior-year spend of 500 to 750; and
- a stronger observed Men's effect among new customers.

These are **exploratory patterns**, not deployable rules. A large effect or small within-subgroup p-value does not prove that the subgroup responds differently from the rest of the population. The relevant joint interaction tests did not support that stronger claim.

Two Women's E-Mail subgroup estimates were negative in the 200 to 350 and 350 to 500 prior-spend bands, but both confidence intervals included zero and the overall history-segment interaction was not reliable. These estimates should not be used to suppress the Women's treatment for those bands.

## Policy implication

The evidence supports the following hierarchy:

1. **Default fixed policy:** Men's E-Mail to all eligible customers when its incremental contribution exceeds delivery cost.
2. **Alternative fixed policy:** Women's E-Mail remains value-creating relative to no email, but is inferior overall under the observed experiment.
3. **Rule-based segmentation:** not justified by the current interaction evidence.
4. **Model-based targeting:** may be explored only with held-out evaluation and an explicit benchmark against Men's-send-to-all.
5. **No-email option:** must remain available when predicted incremental contribution does not cover contact cost.

## Limitations carried forward

- Segment estimates are less precise than the overall effects because the randomized sample is divided into smaller cells.
- Multiplicity increases the risk of apparently attractive but non-replicable subgroup results.
- The segment analysis is explanatory and does not establish out-of-sample policy value.
- A targeting model must use pre-treatment features only and must be evaluated on data that were not used to fit it.
- Any profit comparison requires explicit contribution-margin and treatment-cost assumptions.
