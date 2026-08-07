# Analytical Decision Rationale

This document records the principal analytical choices that shaped the final recommendation and the reasons those choices were retained in the completed analysis.

## Primary commercial outcome

**Spend per eligible customer** was selected as the primary outcome because it captures the commercial effect across everyone randomised, including customers who did not convert.

This preserves the intention-to-treat comparison and avoids conditioning the primary analysis on a post-treatment event.

## Average order value

Average order value was reported descriptively among converters but was not treated as the principal causal metric.

Because conversion can itself be changed by treatment, restricting the comparison to converters can select different customer populations across experiment arms. The business decision therefore remained anchored to spend across all eligible customers.

## Randomisation credibility

Treatment allocation, baseline balance and outcome consistency were reviewed before effect estimation.

The sample-ratio test returned `p = 0.9037`, the largest absolute standardised mean difference was **0.0086**, and categorical distributions differed only marginally across arms. These checks supported use of the full randomised population for the primary causal comparisons.

## Exact row matches

The **6,562 exact row matches** were retained.

The source does not provide a unique customer identifier and includes several categorical and low-cardinality fields. Identical observed records therefore do not establish that the same customer was duplicated. Removing them would introduce an unsupported assumption and alter the randomised arm totals.

## Multiple comparisons

Spend per eligible customer was pre-specified as the primary commercial outcome, with visit and conversion treated as supporting outcomes.

Holm adjustment was applied within related comparison families, and effect sizes and confidence intervals were interpreted alongside adjusted p-values. The treatment decision was not based on whichever comparison happened to produce the smallest p-value.

## Direct treatment selection

Men's E-Mail was not declared superior simply because it had stronger treatment-versus-control estimates.

The two active treatments were tested directly. Men's E-Mail exceeded Women's E-Mail by approximately **£0.35 spend per eligible customer**, with a 95% confidence interval of approximately **£0.04 to £0.67** and Holm-adjusted `p = 0.0305`.

That direct comparison supported Men's E-Mail as the operating treatment.

## Segment policy decision

No manual segment rule was approved.

Individual subgroup point estimates were not treated as evidence of heterogeneity unless treatment effects differed across segment levels. Joint treatment-by-segment interaction tests were therefore used across six pre-specified customer dimensions.

None remained significant after multiplicity adjustment, so observed subgroup patterns were retained as descriptive rather than converted into operating rules.

## Personalised targeting decision

The personalised policy was evaluated against **Men's E-Mail to all**, not against No E-Mail or a weaker treatment.

A treatment-stratified 70/30 train-holdout design was used, and policy value was estimated on the 19,200-customer randomised holdout using inverse-propensity and doubly robust estimators.

The profit-aware policy showed a point uplift of approximately **£18 per 1,000 customers**, but its 95% bootstrap interval ranged from approximately **-£129 to +£155**.

Because the interval included no improvement and meaningful downside, the model was not approved for deployment.

## Feature importance

Historical spend and recency were the strongest predictive features in the fitted outcome models.

Those importances were treated as model diagnostics only. They do not establish that the features cause treatment response and were not used to justify a manual targeting rule.

## Operating recommendation

The completed evidence supports **Men's E-Mail as the fixed operating treatment when campaign economics clear the documented threshold**.

The simpler policy was preferred because it had stronger experimental support than the personalised alternative. Model complexity was not treated as a business benefit unless it produced demonstrable incremental policy value.

## Measurement requirement

Any future personalised policy should be evaluated prospectively against the current fixed benchmark, with the commercial outcome and treatment rule defined before measurement.

Operational monitoring should keep spend per eligible customer, campaign cost, contribution margin, visit and conversion effects, customer-mix changes and campaign fatigue visible so the decision can be reassessed when conditions change.
