# Analytical Design

## Experimental population

The analysis used all **64,000 customers** assigned in the Hillstrom email experiment across Men's E-Mail, Women's E-Mail and No E-Mail control.

No records were excluded from the primary intention-to-treat population.

## Experiment integrity

Before treatment effects were estimated, the source was reviewed for schema consistency, missing values, invalid binary values, impossible monetary values, treatment allocation, baseline balance and consistency between visit, conversion and spend outcomes.

The allocation test showed no evidence of sample-ratio mismatch (`p = 0.9037`), and the largest absolute standardised mean difference across reviewed numeric and binary pre-treatment variables was **0.0086**.

The 6,562 exact row matches were retained because the source contains no unique customer identifier; identical observed records are therefore not sufficient evidence of duplicate customers.

## Outcome hierarchy

**Spend per eligible customer** was treated as the primary commercial outcome.

Visit rate and conversion rate were supporting outcomes. Average order value among converters was reported descriptively but was not used as the primary causal metric because conversion is itself affected by treatment.

## Treatment-effect estimation

Men's E-Mail and Women's E-Mail were each compared with No E-Mail using absolute effects, confidence intervals and hypothesis tests appropriate to the outcome type.

Related comparison families used Holm adjustment to reduce false-positive risk from multiple testing.

Men's E-Mail and Women's E-Mail were also compared directly. Treatment superiority was not inferred from separate treatment-versus-control significance tests.

## Segment analysis

Treatment heterogeneity was assessed across pre-treatment customer characteristics including recency, prior spend, channel, geography, customer status and merchandise affinity.

Segment-level point estimates were treated as descriptive until supported by joint treatment-by-segment interaction tests. None of the six pre-specified interaction families remained significant after multiplicity adjustment, so no manual segment-specific treatment policy was approved.

## Commercial evaluation

Causal spend effects were translated into commercial outcomes using explicit contribution-margin and contact-cost assumptions.

The commercial model separated observed revenue from incremental revenue and reported profit per 1,000 eligible customers, break-even contact cost and sensitivity across margin and cost scenarios.

At the reference scenario of **40% contribution margin** and **£0.10 contact cost**, Men's E-Mail generated approximately **£208 incremental profit per 1,000 customers**.

## Personalised policy evaluation

Customer-level treatment policies used pre-treatment features only.

The dataset was divided using a treatment-stratified **70/30 train-holdout split**, leaving **19,200 randomised customers** for policy evaluation.

Separate outcome models were fitted for each treatment arm. Candidate policies were then compared with fixed policies using inverse-propensity and doubly robust estimators on the holdout sample.

Men's-send-to-all was the explicit operating benchmark because the full experiment had already established it as the strongest fixed treatment.

Paired bootstrap intervals were used to quantify uncertainty around policy-profit differences. The profit-aware policy produced a positive point estimate but its interval included zero and meaningful downside, so it was not approved for deployment.

## Reporting controls

Across the analysis:

- observed outcomes were kept separate from causal effects;
- causal effects were kept separate from commercial assumptions;
- subgroup findings required interaction evidence;
- predictive accuracy was not treated as evidence of policy value; and
- personalised treatment was required to outperform the strongest fixed benchmark on held-out randomised data with adequate precision.
