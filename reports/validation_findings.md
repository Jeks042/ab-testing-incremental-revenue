# Experiment Integrity and Analysis Population

## Outcome

**The experiment passed the integrity review and all 64,000 assigned customers were retained for the primary intention-to-treat analysis.**

Treatment allocation, baseline balance and outcome-consistency checks supported causal comparison of Men's E-Mail and Women's E-Mail with the No E-Mail control.

## Validation summary

| Check | Result | Decision implication |
|---|---:|---|
| Source rows | 64,000 | Reconciled to the published experiment size |
| Source columns | 12 | Expected schema present |
| Missing cells | 0 | No missing-data treatment required |
| Invalid binary values | 0 | Binary fields valid |
| Negative prior spend | 0 | No impossible historical values |
| Negative outcome spend | 0 | No impossible outcome values |
| Positive spend without conversion | 0 | Outcome fields internally consistent |
| Conversion without positive spend | 0 | Outcome fields internally consistent |
| Conversion without visit | 0 | Outcome fields internally consistent |
| Sample-ratio test | chi-square 0.2025; p = 0.9037 | No evidence of treatment-allocation failure |

## Treatment allocation

| Experiment arm | Customers | Allocation |
|---|---:|---:|
| No E-Mail | 21,306 | 33.29% |
| Men's E-Mail | 21,307 | 33.29% |
| Women's E-Mail | 21,387 | 33.42% |

The largest arm differed from the smallest by 81 customers. This was immaterial relative to the 64,000-customer sample and consistent with random assignment.

## Baseline balance

Pre-treatment characteristics were closely aligned across the three arms. The largest absolute standardised mean difference among the reviewed numeric and binary variables was **0.0086**.

The largest observed percentage-point differences across categorical variables were also small:

- channel: **0.84 percentage points**;
- history segment: **0.68 percentage points**; and
- geography type: **0.58 percentage points**.

These differences did not indicate a meaningful randomisation failure.

## Exact row matches

The source contains **6,562 exact row matches**, equivalent to **10.25%** of records. They were retained in the primary analysis.

The dataset has no unique customer identifier and contains several categorical or low-cardinality fields. Identical observed rows therefore cannot be confirmed as duplicate customers. Removing them would impose an unsupported assumption, alter treatment-arm totals and potentially distort the randomised comparison.

The records are described as **exact row matches**, not confirmed duplicates.

## Final analysis population

- Intention-to-treat population: **64,000 customers**.
- Excluded rows: **0**.
- Primary comparisons: Men's E-Mail vs No E-Mail; Women's E-Mail vs No E-Mail.
- Primary commercial outcome: **spend per eligible customer**.
- Supporting outcomes: **visit rate** and **conversion rate**.

## Analytical boundaries

The integrity review supports causal inference within this experiment, not automatic generalisation to other retailers, periods or creative treatments. The absence of a customer identifier prevents independent verification of repeated records, and commercial recommendations remain conditional on explicit margin, contact-cost and campaign-cost assumptions.
