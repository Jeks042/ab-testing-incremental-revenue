# Experiment-Integrity Review

## Decision

**GO — proceed to average treatment-effect estimation using all 64,000 source rows.**

The treatment allocation, baseline covariates and outcome-consistency checks support causal comparison of the two email treatments with the no-email control group.

## Evidence reviewed

| Check | Result | Interpretation |
|---|---:|---|
| Source rows | 64,000 | Matches the published experiment size used by the project |
| Source columns | 12 | Expected schema present |
| Missing cells | 0 | No missing-data treatment required |
| Invalid binary values | 0 | Binary fields contain only 0 and 1 |
| Negative prior spend | 0 | No impossible negative history values |
| Negative outcome spend | 0 | No impossible negative outcome values |
| Positive spend without conversion | 0 | Outcome fields are internally consistent |
| Conversion without positive spend | 0 | Outcome fields are internally consistent |
| Conversion without visit | 0 | Outcome fields are internally consistent |
| Sample-ratio test | chi-square 0.2025; p = 0.9037 | No evidence that allocation departed materially from the expected equal three-arm split |

## Treatment allocation

| Experiment arm | Customers | Allocation |
|---|---:|---:|
| No E-Mail | 21,306 | 33.29% |
| Mens E-Mail | 21,307 | 33.29% |
| Womens E-Mail | 21,387 | 33.42% |

The largest arm differs from the smallest by 81 customers. This difference is immaterial relative to the 64,000-customer sample and is consistent with random assignment.

## Baseline balance

The largest absolute standardised mean difference among the reviewed numeric and binary pre-treatment variables is **0.0086**, far below conventional material-imbalance thresholds.

Categorical distributions are also closely aligned. The largest observed percentage-point range across arms is:

- channel: 0.84 percentage points;
- history segment: 0.68 percentage points; and
- geography type: 0.58 percentage points.

These differences are operationally small and do not suggest a meaningful randomisation failure.

## Exact row matches

The validation report identifies **6,562 exact row matches** (10.25% of rows). They will **not** be removed.

The source has no customer identifier and several fields are categorical or low-cardinality. Two different customers can therefore legitimately share the same complete observed profile and outcomes. Treating every matching row as a duplicate customer would impose an unsupported assumption, change treatment-arm totals and potentially bias treatment-effect estimates.

The project will describe these records as **exact row matches**, not confirmed duplicate customers. A sensitivity check may compare estimates after collapsing exact rows, but the primary analysis will preserve all source records.

## Analysis population

- Primary intention-to-treat population: all 64,000 assigned customers.
- Excluded rows: 0.
- Treatment comparisons: Mens E-Mail versus No E-Mail; Womens E-Mail versus No E-Mail.
- Primary commercial outcome: spend per eligible customer.
- Supporting outcomes: visit rate and conversion rate.

## Limitations carried forward

- There is no customer identifier for independently verifying repeated records.
- The experiment supports causal inference within this sample and campaign context; it does not by itself establish that the same effects will generalise to other retailers, periods or creative treatments.
- Commercial recommendations require explicit contribution-margin, contact-cost and campaign-cost assumptions.
