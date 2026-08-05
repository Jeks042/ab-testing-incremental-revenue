# Analysis Plan

## 1. Experiment-integrity review

### 1.1 File and schema checks

- Confirm expected row and column counts.
- Validate column names and data types.
- Confirm binary fields contain only valid values.
- Check missing values, duplicated rows and impossible numeric values.
- Reconcile every exclusion to the source row count.

### 1.2 Treatment assignment

- Count customers by treatment arm.
- Compare observed allocation with the expected one-third split.
- Perform a chi-square sample-ratio mismatch test.
- Investigate any material allocation difference before estimating effects.

### 1.3 Baseline balance

Assess pre-treatment balance for:

- recency;
- prior-year spend;
- prior men's and women's merchandise purchase;
- new-customer status;
- channel;
- zip-code classification; and
- history segment.

Report standardised mean differences for numeric and binary fields and distribution comparisons for categorical fields. Statistical significance alone will not define imbalance because large samples can make trivial differences significant.

### 1.4 Outcome consistency

- Confirm visit and conversion are binary.
- Confirm spend is non-negative.
- Reconcile positive spend with conversion status.
- Report, rather than silently repair, records where conversion and visit do not align with expected behaviour.

## 2. Descriptive experiment summary

For each arm, report:

- customers assigned;
- visit count and rate;
- conversion count and rate;
- total revenue;
- revenue per eligible customer;
- average order value among converters; and
- zero-spend share.

## 3. Average treatment effects

### Binary outcomes

For visit and conversion:

- absolute risk difference;
- relative lift;
- confidence interval for the difference;
- two-sample proportion test; and
- number needed to treat when meaningful.

### Continuous outcome

For spend per eligible customer:

- difference in means;
- Welch test as a reference;
- non-parametric or randomisation-based sensitivity;
- bootstrap confidence interval; and
- distribution-aware interpretation because spend is zero-inflated and skewed.

## 4. Multiplicity and decision hierarchy

The primary commercial outcome is revenue per eligible customer. Visit and conversion are supporting outcomes. Men's and women's treatments will each be compared with control. Secondary treatment-to-treatment and subgroup comparisons will be interpreted with multiplicity in mind.

The final recommendation will not be based on the smallest p-value.

## 5. Power and precision

- Calculate confidence-interval width for each main effect.
- Estimate minimum detectable effect using the realised sample sizes.
- Distinguish evidence of no meaningful effect from insufficient precision.
- Avoid presenting retrospective power as a substitute for confidence intervals.

## 6. Segment effects

### Pre-specified dimensions

- recency band;
- prior spend band;
- channel;
- new versus established customer;
- prior merchandise affinity; and
- geography type.

For each segment:

- sample size by arm;
- treatment effect;
- confidence interval;
- interaction test where appropriate; and
- commercial effect under common assumptions.

Subgroup significance in one segment and non-significance in another will not, by itself, be treated as evidence that effects differ.

## 7. Commercial model

For each treatment and scenario:

```text
Incremental profit
= recipients × incremental revenue per customer × contribution margin
− recipients × contact cost
− treatment-specific fixed or variable cost
```

Report:

- break-even contact cost;
- break-even contribution margin;
- profit per 1,000 eligible customers;
- expected profit under capacity constraints; and
- sensitivity ranges rather than one unsupported point estimate.

## 8. Targeting extension

Benchmarks:

1. Contact nobody
2. Send to all eligible customers
3. Use the best overall treatment
4. Apply transparent business rules
5. Apply a model-based treatment policy

The targeting analysis will use only pre-treatment features. Performance will be assessed on held-out data using uplift and profit curves. Predictive conversion accuracy will not be used as the primary policy metric.

## 9. Reporting

The final executive output will clearly separate:

- facts observed in the experiment;
- estimated causal effects;
- commercial assumptions;
- recommended action;
- uncertainty and sensitivity; and
- limitations affecting external validity.
