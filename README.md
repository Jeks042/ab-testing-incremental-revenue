# A/B Testing and Incremental Revenue

A decision-focused experimentation case study using the Hillstrom email marketing dataset.

> **Project status:** Core analysis is complete. The project is now moving into executive reporting, dashboard production and portfolio publication.

## Business decision

A retail marketing director must decide:

- whether an email campaign creates genuine incremental value;
- which treatment should be preferred;
- whether the result is statistically reliable and commercially worthwhile;
- whether customer-level targeting improves profit beyond the strongest fixed treatment; and
- when contact cost, margin or customer response makes no email more profitable than sending.

The analysis moves beyond conversion reporting by connecting randomized experimental evidence to revenue, contribution margin, contact cost and treatment-policy decisions.

## Final analytical decision

**Use Men's E-Mail as the operating treatment for eligible customers when the documented contribution-margin and contact-cost threshold is met. Do not deploy the current personalised targeting model.**

Relative to No E-Mail:

- Men's E-Mail increased spend per eligible customer by **0.770** (95% CI: **0.484 to 1.052**).
- Women's E-Mail increased spend per eligible customer by **0.424** (95% CI: **0.152 to 0.686**).

In the direct head-to-head comparison, Men's E-Mail outperformed Women's E-Mail on:

- visit rate: **+3.14 percentage points**;
- conversion rate: **+0.37 percentage points**; and
- spend per eligible customer: **+0.345** (95% CI: **0.044 to 0.666**, Holm-adjusted p = **0.0305**).

The pre-specified segment interaction tests did not support a hand-built targeting rule. On the 19,200-customer randomized holdout, the personalised policies had positive point estimates but did not reliably outperform Men's E-Mail to all:

- highest predicted spend policy: **+28.7 profit units per 1,000**, 95% bootstrap interval **-120.2 to +170.6**;
- profit-aware policy: **+18.3 per 1,000**, 95% bootstrap interval **-129.1 to +155.4**.

Because both intervals include zero and meaningful negative outcomes, personalisation remains exploratory rather than deployable.

See:

- [`reports/validation_findings.md`](reports/validation_findings.md)
- [`reports/main_effect_findings.md`](reports/main_effect_findings.md)
- [`reports/segment_findings.md`](reports/segment_findings.md)
- [`reports/targeting_findings.md`](reports/targeting_findings.md)

## Commercial interpretation

At a 40% contribution margin and contact cost of 0.10 per customer, the point-estimate incremental profit per 1,000 eligible customers was approximately:

- **Men's E-Mail: 208**
- **Women's E-Mail: 70**

Using the lower 95% revenue-effect bound under the same assumptions, both treatments remained positive, but the Women's treatment had a much narrower cost buffer.

If Men's and Women's emails have the same delivery cost, the direct spend advantage for Men's E-Mail is worth approximately **138 additional contribution units per 1,000 contacted customers** at a 40% margin, before fixed or treatment-specific creative costs.

## Dataset

The project uses Kevin Hillstrom's MineThatData email experiment. The published dataset contains 64,000 customers allocated approximately equally across:

- `Mens E-Mail`
- `Womens E-Mail`
- `No E-Mail` control

Customer characteristics were recorded before treatment. Outcomes observed after treatment include website visit, conversion and spend.

Original source: [MineThatData E-Mail Analytics and Data Mining Challenge](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)

The raw dataset is not committed to this repository. The download script retrieves and validates a local copy.

## Analytical phases

### Phase 1 — Experiment integrity — complete

- Schema and data validation
- Missing values and exact row matches
- Treatment allocation and sample-ratio mismatch test
- Baseline balance
- Outcome consistency
- Formal go/no-go decision

### Phase 2 — Average treatment effects — complete

- Visit, conversion and spend effects versus control
- Absolute and relative lift
- Confidence intervals and hypothesis tests
- Multiplicity adjustment
- Number needed to treat

### Phase 3 — Commercial and direct-treatment evaluation — complete

- Contribution-margin and contact-cost sensitivity
- Break-even contact cost
- Profit per 1,000 customers
- Direct Men's-versus-Women's comparison

### Phase 4 — Segment effects — complete

- Pre-specified recency, prior-spend, channel, geography, status and affinity segments
- Segment-level spend estimates
- Joint treatment-by-segment interaction tests
- Multiplicity-aware rejection of unsupported rule-based targeting

### Phase 5 — Held-out targeting and policy value — complete

- Treatment-stratified 70/30 train-holdout split
- Separate outcome models for all three randomized arms
- Fixed and personalised policy benchmarks
- Inverse-propensity and doubly robust policy evaluation
- Paired bootstrap confidence intervals versus Men's-send-to-all
- Capacity-constrained policy analysis
- Margin and contact-cost sensitivity
- Non-deployment decision where model uplift was not reliably positive

## Analytical safeguards

- All assigned customers remain in the intention-to-treat analysis.
- Only pre-treatment variables are used for segmentation and targeting.
- Spend per eligible customer is the primary commercial outcome.
- Confidence intervals and effect sizes are interpreted alongside p-values.
- A significant effect inside one subgroup is not treated as evidence that subgroups differ.
- Predictive accuracy and feature importance are not presented as proof of causal or policy value.
- A personalised policy must beat Men's-send-to-all on held-out randomized data with adequate precision.
- Revenue observed among treated customers is not confused with incremental revenue caused by treatment.

## Repository structure

```text
ab-testing-incremental-revenue/
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── dashboard/
│   └── README.md
├── docs/
│   ├── analysis_plan.md
│   └── project_brief.md
├── notebooks/
│   ├── 01_data_validation.ipynb
│   ├── 02_experiment_analysis.ipynb
│   └── 03_targeting_policy.ipynb
├── reports/
│   ├── dashboard_plan.md
│   ├── executive_memo_plan.md
│   ├── main_effect_findings.md
│   ├── segment_findings.md
│   ├── targeting_findings.md
│   └── validation_findings.md
├── scripts/
│   ├── download_data.py
│   ├── run_experiment_analysis.py
│   ├── run_segment_analysis.py
│   ├── run_targeting_analysis.py
│   └── run_validation.py
├── sql/
│   ├── 01_quality_checks.sql
│   └── 02_experiment_summary.sql
└── src/
    ├── __init__.py
    ├── data_validation.py
    ├── experiment_metrics.py
    ├── policy_targeting.py
    ├── profit_model.py
    └── segment_analysis.py
```

## Local setup

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS or Linux
source .venv/bin/activate

pip install -r requirements.txt
python scripts/download_data.py
python scripts/run_validation.py
python scripts/run_experiment_analysis.py
python scripts/run_segment_analysis.py
python scripts/run_targeting_analysis.py
```

## Portfolio deliverables

- Reproducible Python analysis
- SQL validation and experiment-summary queries
- Executive dashboard
- Two-page decision memo
- Methodology and limitations note
- Three-minute walkthrough
- Interview questions and model answers
- Portfolio case-study page

## Build checklist

- [x] Define the business decision
- [x] Create repository structure
- [x] Add reproducible download and validation framework
- [x] Complete experiment-integrity checks
- [x] Estimate overall treatment effects
- [x] Build commercial sensitivity model
- [x] Complete direct treatment comparison
- [x] Complete pre-specified segment analysis
- [x] Complete held-out targeting analysis
- [ ] Build executive dashboard
- [ ] Publish decision memo and final recommendation
- [ ] Add portfolio case-study page and CV-ready project evidence

## Author

**Chukwujekwu Joseph Ezema**  
[Portfolio](https://jeks042.github.io/) · [LinkedIn](https://www.linkedin.com/in/chukwujekwu-joseph-ezema-7b1624129/) · [GitHub](https://github.com/Jeks042)
