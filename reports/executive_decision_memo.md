# Executive Decision Memo

## Decision

**Deploy Men's E-Mail as the operating treatment for eligible customers when campaign economics clear the documented threshold. Do not deploy the current personalised targeting policy.**

The randomised experiment shows that Men's E-Mail created the strongest incremental commercial value of the tested treatments. It increased spend per eligible customer by **£0.77 versus No E-Mail** and by **£0.35 versus Women's E-Mail**. The personalised policy produced a positive point estimate on held-out data, but the uncertainty around that uplift was too wide to support deployment.

## Commercial impact

At the reference scenario of a **40% contribution margin** and **£0.10 contact cost per customer**:

| Treatment | Incremental spend vs control | Estimated profit per 1,000 | Break-even contact cost |
|---|---:|---:|---:|
| Men's E-Mail | £0.770 per customer | ~£208 | £0.308 |
| Women's E-Mail | £0.424 per customer | ~£70 | £0.170 |

Using the lower 95% confidence bound for the revenue effect, estimated profit remained positive for both treatments, but Men's E-Mail retained a materially wider cost buffer.

## Evidence behind the decision

The experiment included **64,000 customers** allocated across Men's E-Mail, Women's E-Mail and No E-Mail control. Treatment allocation and baseline checks supported causal comparison.

Relative to No E-Mail, Men's E-Mail increased:

- visit rate by **7.66 percentage points**;
- conversion rate by **0.68 percentage points**; and
- spend per eligible customer by **£0.770**.

Women's E-Mail also created positive incremental value, but the direct head-to-head comparison favoured Men's E-Mail. Men's E-Mail delivered **£0.345 more spend per eligible customer** than Women's E-Mail, with a 95% confidence interval of **£0.044 to £0.666** and a Holm-adjusted p-value of **0.0305**.

## Why personalisation was not approved

Personalised treatment policies were evaluated on a **19,200-customer randomised holdout**, separate from the data used to fit the outcome models.

| Candidate policy | Profit uplift vs Men's-send-to-all | 95% bootstrap interval |
|---|---:|---:|
| Highest predicted spend | +£28.7 per 1,000 | -£120.2 to +£170.6 |
| Profit-aware policy | +£18.3 per 1,000 | -£129.1 to +£155.4 |

Both intervals include zero and economically meaningful downside. The analysis therefore does not establish that model-based personalisation improves profit beyond Men's E-Mail to all.

## Operating recommendation

- Use Men's E-Mail where expected incremental contribution exceeds contact and campaign cost.
- Continue to use spend per eligible customer as the primary commercial outcome, with visits and conversions as supporting measures.
- Keep the current targeting model in research rather than production.
- Test any future personalised policy prospectively against Men's-send-to-all through direct randomisation.

## Decision boundaries

The recommendation is specific to the observed retailer, campaign context and outcome window. The source does not contain a unique customer identifier, spend is rare and highly skewed, and the commercial result depends on contribution margin, contact cost and any fixed or treatment-specific campaign costs not observed in the dataset.
