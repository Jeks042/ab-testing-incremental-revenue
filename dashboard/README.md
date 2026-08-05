# Executive Dashboard

The completed analysis is ready for executive reporting and Power BI implementation.

## Decision to communicate

**Use Men's E-Mail as the operating treatment when campaign economics clear the threshold. Do not deploy the current personalised targeting model.**

## Dashboard pages

### 1. Executive Decision

- Recommended treatment and action
- Incremental spend per customer
- Profit per 1,000 under selected assumptions
- Break-even contact cost
- Targeting deployment status

### 2. Experiment Evidence

- Treatment allocation and integrity checks
- Visit, conversion and spend outcomes by arm
- Treatment effects with confidence intervals
- Direct Men's-versus-Women's comparison

### 3. Commercial Sensitivity

- Contribution-margin and contact-cost scenarios
- Point estimate and lower-confidence-bound profit
- Break-even economics
- Assumptions displayed beside outputs

### 4. Targeting Decision

- Fixed and personalised policy comparison
- Bootstrap intervals versus Men's-send-to-all
- Capacity-constrained policy curve
- Recommendation share and model diagnostics
- Explicit non-deployment decision

## Build resources

- [`power_bi_build_guide.md`](power_bi_build_guide.md)
- [`../reports/executive_decision_memo.md`](../reports/executive_decision_memo.md)
- [`../reports/targeting_findings.md`](../reports/targeting_findings.md)

## Design controls

- Lead with the decision rather than the methodology.
- Use absolute effects alongside relative lift.
- Keep observed revenue, incremental revenue and assumed profit distinct.
- Display confidence intervals with effect and policy estimates.
- Keep commercial assumptions visible.
- Do not imply that model feature importance is causal.
- Do not claim proven model-based incremental revenue where the policy interval includes zero.
