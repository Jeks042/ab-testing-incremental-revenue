# Executive Dashboard

The Power BI report presents the final business decision from the Hillstrom email experiment: **use Men's E-Mail as the operating treatment when campaign economics clear the documented threshold, and do not deploy the current personalised targeting policy.**

The report is structured around the questions a Marketing or Finance stakeholder would need answered before approving a campaign decision.

## Executive Decision

![Executive Decision](Executive%20Decision.png)

Men's E-Mail was the strongest tested treatment. Relative to No E-Mail, it increased spend per eligible customer by **£0.77**. Under the reference scenario of a **40% contribution margin** and **£0.10 contact cost per customer**, the estimated incremental profit was approximately **£208 per 1,000 eligible customers**.

The page brings the treatment recommendation, incremental spend, commercial value and targeting decision into one view so the action is clear before the supporting detail is reviewed.

## Experiment Evidence

![Experiment Evidence](Experiment%20Evidence.png)

The experiment included **64,000 customers** across Men's E-Mail, Women's E-Mail and No E-Mail. Treatment allocation and baseline checks supported the randomised comparison.

Both active treatments created incremental value versus control, with Men's E-Mail producing the stronger commercial result:

- **Men's E-Mail vs No E-Mail:** +£0.77 spend per eligible customer.
- **Women's E-Mail vs No E-Mail:** +£0.42 spend per eligible customer.
- **Men's E-Mail vs Women's E-Mail:** +£0.35 spend per eligible customer, with a 95% confidence interval of approximately £0.04 to £0.67.

Visit and conversion effects are shown as supporting outcomes; spend per eligible customer remains the primary commercial measure.

## Commercial Sensitivity

![Commercial Sensitivity](Commercial%20Sensitivity.png)

The commercial view translates the causal treatment effect into contribution economics rather than treating observed revenue as profit.

At the reference scenario:

- Men's E-Mail generated approximately **£208 incremental profit per 1,000 customers**.
- Women's E-Mail generated approximately **£70 per 1,000 customers**.
- Men's E-Mail remained viable under a wider range of margin and contact-cost assumptions.

The sensitivity analysis shows where contact cost or lower contribution margin would change the decision, keeping the business assumptions visible alongside the recommendation.

## Targeting Decision

![Targeting Decision](Targeting%20Decision.png)

Personalised targeting was evaluated on a held-out randomised sample rather than approved on predictive performance alone.

The profit-aware policy produced a positive point estimate of approximately **£18 per 1,000 customers** versus Men's E-Mail to all, but its 95% bootstrap interval ranged from approximately **-£129 to +£155**. The highest-predicted-spend policy showed the same pattern: a positive point estimate with substantial uncertainty.

**Decision: do not deploy the personalised policy.** Men's E-Mail to all remains the operating benchmark until a future experiment demonstrates reliable incremental policy value.

## Supporting analysis

- [Executive decision memo](../reports/executive_decision_memo.md)
- [Main treatment-effect findings](../reports/main_effect_findings.md)
- [Segment-analysis findings](../reports/segment_findings.md)
- [Targeting-policy findings](../reports/targeting_findings.md)
- [Methodology and limitations](../docs/methodology_and_limitations.md)
