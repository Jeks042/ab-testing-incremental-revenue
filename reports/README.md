# Decision Reports

This folder contains the completed decision record for the experiment: the evidence used to approve the operating treatment, the commercial assumptions applied to that decision, and the reasons the personalised targeting model was not approved for deployment.

## Executive decision

**Men's E-Mail is the recommended operating treatment when campaign economics clear the documented threshold. The current personalised targeting policy should not be deployed.**

The recommendation is supported by the randomised experiment, direct treatment comparison, commercial sensitivity analysis and held-out policy evaluation.

## `executive_decision_memo.md`

The executive memo summarises the business recommendation for a Marketing and Finance audience.

It brings together the primary treatment effect, contribution economics, targeting decision and the key assumptions that could change the recommendation.

At the reference scenario of **40% contribution margin** and **£0.10 contact cost**, Men's E-Mail generated approximately **£208 incremental profit per 1,000 eligible customers**.

## `validation_findings.md`

This report documents the experiment-integrity review completed before treatment effects were estimated.

The 64,000-customer population passed the allocation, schema, missing-value, outcome-consistency and baseline-balance checks required for the primary intention-to-treat analysis.

**Decision:** proceed with all 64,000 source rows.

## `main_effect_findings.md`

This report presents the main causal treatment effects and the initial commercial recommendation.

Men's E-Mail increased spend per eligible customer by approximately **£0.77** versus No E-Mail; Women's E-Mail increased spend by approximately **£0.42**. Both effects were positive, but Men's E-Mail had the stronger commercial profile and wider cost buffer.

## `segment_findings.md`

This report tests whether treatment effects differ across pre-specified customer characteristics.

The analysis found no reliable interaction evidence after multiplicity adjustment across recency, prior spend, channel, geography, customer status or merchandise affinity.

**Decision:** do not create a manual segment-specific treatment rule from the observed subgroup patterns.

## `targeting_findings.md`

This report evaluates personalised treatment policies against the strongest fixed benchmark on a held-out randomised sample.

The profit-aware policy produced a positive point estimate of approximately **£18 per 1,000 customers** versus Men's E-Mail to all, but the 95% bootstrap interval included both meaningful downside and upside.

**Decision:** keep personalisation exploratory. The model did not demonstrate sufficiently reliable incremental profit to justify deployment.

## Reporting standard

Across the decision record, observed outcomes, causal treatment effects and commercial assumptions are kept separate. Incremental claims are based on randomised comparisons, and model-based policy value is only treated as deployable when it improves on the strongest fixed treatment with adequate precision.

Supporting methodology: [methodology and limitations](../docs/methodology_and_limitations.md).
