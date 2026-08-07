# Methodology, Decision Controls and Limitations

## Experimental population

The analysis used all **64,000 customers** assigned in the Hillstrom email experiment. No records were excluded from the primary intention-to-treat population.

## Experiment integrity

The source was validated for expected schema and row count, missing values, invalid binary values, non-negative monetary fields, consistency between visit, conversion and spend, treatment allocation and baseline balance.

The chi-square sample-ratio test showed no evidence of material allocation failure (`p = 0.9037`). The largest absolute standardised mean difference across reviewed numeric and binary pre-treatment variables was **0.0086**.

Exact row matches were retained because the source does not include a unique customer identifier. Matching observed fields are not sufficient evidence that records represent the same customer.

## Treatment-effect estimation

Spend per eligible customer was the primary commercial outcome. Visit rate and conversion rate were supporting outcomes.

Binary outcomes were evaluated using absolute risk differences, confidence intervals and two-sample proportion tests. Spend effects were evaluated using differences in means with uncertainty estimates appropriate to the highly skewed outcome distribution.

Related comparison families used Holm adjustment to reduce false-positive risk from multiple testing.

Men's E-Mail and Women's E-Mail were compared directly; treatment superiority was not inferred from separate significance tests against control.

## Segment analysis

Customer segments were defined exclusively from pre-treatment characteristics.

Treatment heterogeneity was assessed through joint treatment-by-segment interaction tests. Statistical significance within one subgroup was not interpreted as evidence that treatment effects differed from other subgroups.

None of the six pre-specified interaction families remained significant after multiplicity adjustment, so no manual segment-specific treatment rule was approved.

## Commercial model

Commercial value was calculated from the estimated causal spend effect rather than observed treatment-arm revenue:

```text
incremental spend per eligible customer × contribution margin
− contact cost per treated customer
− any additional treatment-specific cost
```

Published commercial results state the contribution-margin and contact-cost assumptions used. At the reference scenario of **40% contribution margin** and **£0.10 contact cost**, Men's E-Mail generated approximately **£208 incremental profit per 1,000 eligible customers**.

## Personalised policy evaluation

The targeting analysis used only pre-treatment customer characteristics.

A treatment-stratified **70/30 train-holdout split** was used. Separate outcome models were fitted for No E-Mail, Men's E-Mail and Women's E-Mail, and candidate treatment policies were evaluated on the **19,200-customer randomised holdout**.

Policy value was estimated using inverse-propensity and doubly robust estimators. Paired bootstrap intervals compared candidate-policy profit with Men's-send-to-all, the strongest fixed treatment established by the full experiment.

Predictive diagnostics and feature importance were kept separate from causal policy-value evidence.

The profit-aware policy produced a positive point estimate, but its 95% bootstrap interval included zero and economically meaningful downside. The policy was therefore not approved for deployment.

## Decision controls

The completed analysis applied the following controls throughout:

- intention-to-treat populations were preserved for causal comparisons;
- observed revenue was not labelled incremental;
- spend per eligible customer remained the primary commercial outcome;
- confidence intervals and effect sizes were interpreted alongside p-values;
- direct treatment superiority required a head-to-head comparison;
- subgroup policies required interaction evidence;
- predictive accuracy was not treated as evidence of causal treatment value; and
- personalised policies were required to outperform the strongest fixed benchmark on held-out randomised data with adequate precision.

## Limitations

1. The experiment represents one retailer, one campaign context and one outcome window; external validity is not guaranteed.
2. The source does not include a unique customer identifier, preventing independent verification of repeated-looking records.
3. Spend is rare, zero-inflated and highly skewed, making customer-level treatment ranking considerably less precise than average treatment-effect estimation.
4. Segment and targeting analyses divide the available sample and therefore have lower precision than the overall experiment.
5. Commercial conclusions depend on contribution margin, contact cost and any treatment-specific costs that were not directly observed in the dataset.
6. The held-out targeting analysis estimates policy value retrospectively; prospective randomisation is required before claiming operational incremental profit from the candidate personalised policy.
7. Changes in customer mix, campaign creative, market conditions or contact economics could change the preferred treatment and should trigger re-evaluation.
