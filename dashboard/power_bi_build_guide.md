# Power BI Executive Dashboard Build Guide

## Purpose

Build a four-page report that explains the business decision, the randomized evidence, the commercial thresholds and the targeting non-deployment decision without requiring the audience to inspect the notebooks.

## Recommended pages

### 1. Executive Decision

**Decision question:** Which campaign should be operated?

Visuals:

- recommendation card: Men's E-Mail approved;
- spend lift versus control by treatment;
- direct Men's-versus-Women's spend advantage and confidence interval;
- profit per 1,000 customers at selected assumptions;
- break-even contact cost;
- targeting status card: do not deploy.

Required callout:

> Men's E-Mail is the strongest supported operating treatment. Personalised targeting did not reliably beat this benchmark on held-out randomized data.

### 2. Experiment Evidence

Visuals:

- assigned customers by arm;
- visit rate, conversion rate and spend per eligible customer by arm;
- absolute treatment effects with confidence intervals;
- direct treatment comparison;
- experiment-integrity status indicators.

Controls:

- show absolute lift beside relative lift;
- identify spend per eligible customer as the primary outcome;
- keep average order value descriptive rather than causal.

### 3. Commercial Sensitivity

Visuals:

- contribution-margin and contact-cost heatmap;
- profit per 1,000 by treatment;
- break-even contact-cost table;
- point estimate versus lower-confidence-bound scenarios.

Suggested slicers:

- contribution margin;
- contact cost;
- treatment;
- effect basis: point estimate or lower confidence bound.

### 4. Targeting Decision

Visuals:

- held-out policy ranking versus Men's-send-to-all;
- bootstrap interval for policy profit uplift;
- capacity policy curve;
- recommendation share across Men's, Women's and No E-Mail;
- model diagnostics and a limitations callout.

Required warning:

> Positive policy point estimates are not deployment evidence when the confidence interval includes zero and meaningful losses.

## Suggested model

### Tables

- `TreatmentEffects`: one row per comparison and outcome;
- `ArmSummary`: one row per randomized arm;
- `CommercialSensitivity`: one row per treatment, margin and contact-cost scenario;
- `PolicyEvaluation`: one row per held-out policy;
- `PolicyIntervals`: one row per policy benchmark comparison;
- `CapacityAnalysis`: one row per capacity level;
- `ModelDiagnostics`: one row per randomized arm;
- `FeatureImportance`: one row per feature.

These tables can remain disconnected when they represent separate analytical outputs. Use explicit measures rather than forcing artificial relationships.

## Core DAX measures

```DAX
Selected Margin = SELECTEDVALUE(CommercialSensitivity[contribution_margin], 0.40)

Selected Contact Cost = SELECTEDVALUE(CommercialSensitivity[contact_cost], 0.10)

Profit per 1,000 = MAX(CommercialSensitivity[dr_profit_per_1000])

Policy Uplift vs Mens = MAX(PolicyEvaluation[dr_profit_uplift_vs_mens_per_1000])

Spend Lift = MAX(TreatmentEffects[absolute_lift])

CI Width = MAX(TreatmentEffects[ci_high]) - MAX(TreatmentEffects[ci_low])

Deployment Status =
IF(
    MAX(PolicyIntervals[bootstrap_ci_low_per_1000]) > 0,
    "Candidate for deployment",
    "Do not deploy"
)
```

## Visual formatting rules

- Use one accent colour for Men's E-Mail and a secondary neutral colour for Women's E-Mail.
- Keep No E-Mail visually subdued.
- Use a diverging scale for profit uplift around zero.
- Show confidence intervals wherever an effect or policy comparison is presented.
- Put assumptions beside profit outputs rather than in a hidden methods page.
- Do not use model feature importance as a causal explanation.

## Reconciliation checks

Before publishing, confirm:

- all treatment-arm counts sum to 64,000;
- the direct spend advantage is 0.345 and reconciles to 1.423 minus 1.077 after rounding;
- Men's profit per 1,000 at 40% margin and 0.10 contact cost is approximately 208;
- the profit-aware held-out policy uplift is +18.3 per 1,000 with interval -129.1 to +155.4;
- every targeting page names Men's-send-to-all as the benchmark;
- the final recommendation does not claim proven model-based incremental revenue.
