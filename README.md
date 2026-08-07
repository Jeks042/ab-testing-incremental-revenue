# A/B Testing and Incremental Revenue

## Executive decision

**Deploy Men's E-Mail to eligible customers when the stated margin and contact-cost assumptions are met. Do not deploy the current personalised targeting policy.**

This project evaluates a 64,000-customer randomised email experiment for a retail marketing business. It connects treatment effects to incremental revenue, contribution margin, contact cost, and held-out policy performance—so the recommendation is commercially defensible, not just statistically significant.

## Decision evidence

| Question | Finding | Decision implication |
|---|---|---|
| Which treatment creates the strongest incremental value? | Men's E-Mail produced **£0.77** incremental spend per eligible customer versus No E-Mail; Women's E-Mail produced **£0.42**. | Use Men's E-Mail as the operating treatment. |
| Is Men's E-Mail meaningfully stronger than Women's E-Mail? | Men's E-Mail delivered a **£0.35** higher spend per eligible customer (95% CI: **£0.04 to £0.67**). | The direct advantage is supported by the experiment. |
| Is the result commercially viable? | At **40% contribution margin** and **£0.10 contact cost per customer**, Men's E-Mail generates approximately **£207.93 incremental profit per 1,000 customers**. | The campaign remains profitable under the stated scenario. |
| Should the business personalise treatment? | Held-out profit-aware targeting had a positive point estimate (**+£18.25 per 1,000** versus Men's E-Mail to all), but its 95% bootstrap interval included zero and meaningful downside. | Keep targeting exploratory; do not deploy it. |

## Executive dashboard

### 1. Executive decision

![Executive Decision dashboard](dashboard/Executive%20Decision.png)

### 2. Experiment evidence

![Experiment Evidence dashboard](dashboard/Experiment%20Evidence.png)

### 3. Commercial sensitivity

![Commercial Sensitivity dashboard](dashboard/Commercial%20Sensitivity.png)

### 4. Targeting decision

![Targeting Decision dashboard](dashboard/Targeting%20Decision.png)

## What was delivered

- Randomised-experiment validation across 64,000 customers and three balanced treatment arms.
- Incremental effects for visits, conversion, and spend, with confidence intervals and multiple-testing controls.
- Direct Men's-versus-Women's treatment comparison.
- Commercial sensitivity analysis covering contribution margin, contact cost, break-even thresholds, and profit per 1,000 customers.
- Held-out evaluation of fixed and personalised targeting policies using inverse-propensity, doubly robust, and bootstrap methods.
- A four-page Power BI executive dashboard built for decision-making and stakeholder communication.

## Method and decision safeguards

The analysis uses intention-to-treat estimates and pre-treatment customer variables only. It treats spend per eligible customer as the primary commercial outcome, distinguishes predictive performance from causal policy value, and requires personalised policies to outperform the strongest fixed treatment on held-out randomised data with adequate precision.

Supporting analysis and documentation:

- [Experiment validation findings](reports/validation_findings.md)
- [Main treatment-effect findings](reports/main_effect_findings.md)
- [Segment-analysis findings](reports/segment_findings.md)
- [Targeting-policy findings](reports/targeting_findings.md)
- [Methodology and limitations](docs/methodology_and_limitations.md)
- [Three-minute project walkthrough](docs/walkthrough_script.md)
- [Interview defence guide](docs/interview_guide.md)

## Technology

**Power BI · Python · SQL · Pandas · scikit-learn · Statistical inference · Causal policy evaluation**

## Author

**Chukwujekwu Joseph Ezema**  
[Portfolio](https://jeks042.github.io/) · [LinkedIn](https://www.linkedin.com/in/chukwujekwu-joseph-ezema-7b1624129/) · [GitHub](https://github.com/Jeks042)
