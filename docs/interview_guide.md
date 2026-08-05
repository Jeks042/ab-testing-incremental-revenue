# Interview Questions and Model Answers

## 1. Why did you use spend per eligible customer as the primary outcome?

Spend per eligible customer captures the commercial effect across everyone randomized, including customers who did not convert. It preserves the intention-to-treat comparison and avoids conditioning on a post-treatment event such as conversion.

## 2. Why not use average order value as the main metric?

Average order value is calculated only among converters. Conversion is affected by treatment, so comparing order value among converters can introduce selection bias. I reported it descriptively but did not use it as the main causal outcome.

## 3. How did you check whether randomization was credible?

I reviewed treatment counts, performed a sample-ratio mismatch test and assessed pre-treatment balance. The allocation test had p = 0.9037, the largest absolute standardized mean difference was 0.0086, and categorical distributions differed by less than one percentage point across arms.

## 4. Why did you retain the 6,562 exact row matches?

The dataset has no customer identifier and includes several categorical or low-cardinality fields. Different customers can therefore share the same observed profile and outcome. Calling those rows confirmed duplicates would be unsupported, so I retained all assigned records and documented the limitation.

## 5. What is the difference between observed revenue and incremental revenue?

Observed revenue is the total spend recorded in a treatment arm. Incremental revenue is the difference that treatment caused relative to the counterfactual control outcome. The randomized comparison estimates that causal difference.

## 6. How did you handle multiple comparisons?

I defined spend per eligible customer as the primary outcome, treated visit and conversion as supporting outcomes and applied Holm adjustment within related comparison families. I interpreted effect sizes and confidence intervals alongside adjusted p-values.

## 7. Why can you say Men's E-Mail is superior to Women's E-Mail?

I tested the two active treatments directly rather than inferring superiority from separate treatment-versus-control results. The direct spend difference was 0.345 per customer, with a 95% confidence interval of 0.044 to 0.666 and Holm-adjusted p = 0.0305.

## 8. Why did you reject the subgroup rules?

A significant treatment effect inside one subgroup does not prove that treatment effects differ between subgroups. I used joint treatment-by-segment interaction tests and adjusted across the six pre-specified segment variables. None remained significant after adjustment.

## 9. How did you evaluate the targeting model?

I used a treatment-stratified 70/30 train-holdout split, fitted separate spend models for each randomized arm and evaluated fixed and personalised policies on the holdout using inverse-propensity and doubly robust estimators. Men's-send-to-all was the explicit benchmark.

## 10. Why did you not deploy the model when its point estimate was positive?

The profit-aware model estimated +18.3 profit units per 1,000 customers, but the 95% bootstrap interval was -129.1 to +155.4. That interval includes no improvement and meaningful losses, so the evidence was not precise enough to justify replacing the fixed policy.

## 11. What did model feature importance tell you?

Historical spend and recency were the most influential predictive features. However, feature importance only describes how the model generated predictions. It does not show that those variables cause treatment response or justify manual targeting.

## 12. How would you improve the targeting analysis?

I would prospectively randomize customers between Men's-send-to-all and the candidate policy, pre-register the commercial outcome and policy rule, increase sample size, and use treatment-specific costs. I would also test models designed for zero-inflated spend and assess stability across time.

## 13. What was the most important business conclusion?

The strongest business decision was not the most complex model. The randomized evidence supported Men's E-Mail as a profitable fixed treatment, while the personalised model did not demonstrate reliable policy improvement. The project therefore chose the simpler policy with stronger evidence.

## 14. What would you monitor after launch?

I would monitor eligible-customer counts, delivery cost, spend per eligible customer, visit and conversion lift, confidence intervals, margin assumptions, campaign fatigue and any drift in customer mix. I would preserve a control or structured test design for continued causal measurement.

## 15. What technical skills does this project demonstrate?

It demonstrates experiment validation, causal treatment-effect estimation, confidence intervals, multiple-testing control, commercial sensitivity analysis, segment interaction testing, held-out policy evaluation, inverse-propensity and doubly robust estimation, bootstrap uncertainty, Python, SQL and dashboard design.
