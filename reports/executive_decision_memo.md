# Executive Decision Memo

## Recommendation

**Use Men's E-Mail as the operating treatment for eligible customers when campaign economics clear the documented threshold. Do not deploy the current personalised targeting model.**

## Evidence

The randomized experiment included 64,000 customers across Men's E-Mail, Women's E-Mail and No E-Mail control.

Relative to control:

- Men's E-Mail increased visit rate by 7.66 percentage points, conversion rate by 0.68 points and spend per eligible customer by 0.770.
- Women's E-Mail increased visit rate by 4.52 percentage points, conversion rate by 0.31 points and spend per eligible customer by 0.424.

In the direct head-to-head comparison, Men's E-Mail exceeded Women's E-Mail by:

- 3.14 percentage points on visit rate;
- 0.37 percentage points on conversion rate; and
- 0.345 spend units per eligible customer, with a 95% confidence interval of 0.044 to 0.666 and Holm-adjusted p-value of 0.0305.

## Commercial interpretation

At a 40% contribution margin and contact cost of 0.10 per customer:

- Men's E-Mail generated approximately 208 incremental profit units per 1,000 eligible customers.
- Women's E-Mail generated approximately 70 per 1,000.
- Men's E-Mail had a break-even contact cost of 0.308, compared with 0.170 for Women's E-Mail.

Using the lower 95% confidence bound, the estimated profit remained positive for both treatments, but the Women's treatment had a materially narrower cost buffer.

## Targeting decision

A treatment-stratified 70/30 train-holdout split was used to evaluate personalised policies on 19,200 unseen randomized customers.

The two candidate policies produced:

- highest predicted spend: +28.7 profit units per 1,000 versus Men's-send-to-all, 95% bootstrap interval -120.2 to +170.6;
- profit-aware policy: +18.3 per 1,000, interval -129.1 to +155.4.

Both intervals include zero and economically meaningful losses. The current model therefore does not provide sufficiently precise evidence to replace the strongest fixed policy.

## Action plan

1. Use Men's E-Mail when expected incremental contribution exceeds contact and campaign cost.
2. Continue measuring spend per eligible customer as the primary outcome.
3. Do not use the current model for customer assignment.
4. Prospectively test any future personalised policy against Men's-send-to-all through direct randomization.

## Key limitations

- Results apply to one retailer, campaign context and outcome window.
- The source lacks a unique customer identifier.
- Spend is rare, zero-inflated and highly skewed.
- Commercial conclusions depend on margin, contact cost and unobserved campaign costs.
- The targeting model has not demonstrated prospective incremental profit.
