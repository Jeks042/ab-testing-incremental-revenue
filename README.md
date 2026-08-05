# A/B Testing and Incremental Revenue

A decision-focused experimentation case study using the Hillstrom email marketing dataset.

> **Project status:** Experiment integrity, average treatment effects, direct treatment comparison and pre-specified segment analysis are complete. Held-out targeting and policy evaluation are now in progress.

## Business decision

A retail marketing director must decide:

- whether an email campaign creates genuine incremental value;
- which treatment should be preferred;
- whether the result is statistically reliable and commercially worthwhile;
- which customers should be contacted when campaign capacity is limited; and
- when contact cost, margin or customer response makes no email more profitable than sending.

The analysis moves beyond reporting conversion rates by connecting randomized experimental evidence to revenue, contribution margin, contact cost and treatment-policy decisions.

## Current decision

**Men's E-Mail is the strongest fixed treatment in the experiment.**

Relative to No E-Mail:

- Men's E-Mail increased spend per eligible customer by **0.770** (95% CI: **0.484 to 1.052**).
- Women's E-Mail increased spend per eligible customer by **0.424** (95% CI: **0.152 to 0.686**).

In the direct head-to-head comparison, Men's E-Mail also outperformed Women's E-Mail:

- visit rate: **+3.14 percentage points**;
- conversion rate: **+0.37 percentage points**; and
- spend per eligible customer: **+0.345** (95% CI: **0.044 to 0.666**, Holm-adjusted p = **0.0305**).

The segment analysis did not find reliable treatment-effect differences after multiplicity adjustment. Therefore:

- Men's-send-to-all remains the fixed-policy benchmark;
- subgroup tables are not used to create a hand-built targeting rule; and
- personalised targeting must prove its value on held-out randomized data before it can replace the fixed benchmark.

See:

- [`reports/validation_findings.md`](reports/validation_findings.md)
- [`reports/main_effect_findings.md`](reports/main_effect_findings.md)
- [`reports/segment_findings.md`](reports/segment_findings.md)

## Commercial interpretation

At a 40% contribution margin and contact cost of 0.10 per customer, the point-estimate incremental profit per 1,000 eligible customers was approximately:

- **Mens E-Mail: 208**
- **Womens E-Mail: 70**

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
- Multiplicity-aware decision on rule-based targeting

### Phase 5 — Held-out targeting and policy value — in progress

- Treatment-stratified 70/30 train-holdout split
- Separate outcome models for all three randomized arms
- No-email, fixed-treatment and personalised policy benchmarks
- Inverse-propensity and doubly robust policy evaluation
- Paired bootstrap confidence intervals versus Men's-send-to-all
- Capacity-constrained policy analysis
- Margin and contact-cost sensitivity

## Analytical safeguards

- All assigned customers remain in the intention-to-treat analysis.
- Only pre-treatment variables are used for segmentation and targeting.
- Spend per eligible customer is the primary commercial outcome.
- Confidence intervals and effect sizes are interpreted alongside p-values.
- A significant effect inside one subgroup is not treated as evidence that subgroups differ.
- Predictive accuracy is not presented as proof of causal or policy value.
- A personalised policy must beat Men's-send-to-all on held-out randomized data.
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

## Planned portfolio deliverables

- Reproducible Python analysis
- SQL validation and experiment-summary queries
- Power BI executive report
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
- [ ] Complete held-out targeting analysis
- [ ] Build executive dashboard
- [ ] Publish decision memo and final recommendation

## Author

**Chukwujekwu Joseph Ezema**  
[Portfolio](https://jeks042.github.io/) · [LinkedIn](https://www.linkedin.com/in/chukwujekwu-joseph-ezema-7b1624129/) · [GitHub](https://github.com/Jeks042)
