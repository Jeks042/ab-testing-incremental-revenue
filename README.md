# A/B Testing and Incremental Revenue

A decision-focused experimentation case study using the Hillstrom email marketing dataset.

> **Project status:** Experiment integrity passed. Average treatment-effect and profit-sensitivity analysis is now in progress.

## Business decision

A retail marketing director must decide:

- whether an email campaign creates genuine incremental value;
- which treatment should be preferred;
- whether the result is statistically reliable and commercially worthwhile;
- which customers should be contacted when campaign capacity is limited; and
- when contact cost, margin or customer response makes suppression more profitable than sending.

The analysis is designed to move beyond reporting conversion rates. It connects experimental evidence to revenue, contribution margin, contact cost and targeting decisions.

## Validation decision

The experiment passed the integrity review and all 64,000 assigned customers remain in the primary intention-to-treat analysis.

The review found:

- no missing values or invalid binary fields;
- no negative or internally inconsistent outcome values;
- no evidence of sample-ratio mismatch;
- very small baseline differences across treatment arms; and
- no evidence supporting deletion of exact row matches in the absence of a customer identifier.

See [`reports/validation_findings.md`](reports/validation_findings.md) for the formal go decision and the treatment-allocation and balance evidence.

## Dataset

The project uses Kevin Hillstrom's MineThatData email experiment. The published dataset contains 64,000 customers allocated approximately equally across:

- `Mens E-Mail`
- `Womens E-Mail`
- `No E-Mail` control

Customer characteristics were recorded before treatment. Outcomes observed after treatment include website visit, conversion and spend.

Original source: [MineThatData E-Mail Analytics and Data Mining Challenge](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)

The raw dataset is not committed to this repository. Run the download script described below to retrieve and validate a local copy.

## Questions the project will answer

1. Did either email treatment increase visit rate, conversion rate or revenue per eligible customer?
2. How large and precise were the estimated treatment effects?
3. Are statistically significant effects also commercially meaningful?
4. How do contribution margin and contact cost change the decision?
5. Do treatment effects vary across defensible customer segments?
6. Can a targeting policy improve incremental profit relative to send-to-all?

## Analytical plan

### Phase 1 — Experiment integrity — complete

- Schema and data-type validation
- Missing values and exact row matches
- Treatment allocation and sample-ratio mismatch test
- Baseline balance across pre-treatment variables
- Outcome consistency checks
- Formal go/no-go decision

### Phase 2 — Average treatment effects — in progress

For each treatment versus control:

- Visit-rate difference
- Conversion-rate difference
- Revenue-per-customer difference
- Absolute and relative lift
- Confidence intervals and hypothesis tests
- Multiplicity-aware interpretation
- Practical versus statistical significance

### Phase 3 — Commercial evaluation

- Incremental revenue
- Contribution-margin sensitivity
- Contact-cost sensitivity
- Break-even economics
- Profit under send-to-all and selective-treatment policies

### Phase 4 — Heterogeneous effects and targeting

- Pre-specified segment effects
- Exploratory subgroup analysis with clear caveats
- Rule-based targeting benchmark
- Model-based uplift extension
- Gain and uplift curves
- Capacity-constrained treatment policy

## Analytical safeguards

- All assigned customers remain in the intention-to-treat analysis.
- Treatment assignment is kept separate from outcomes and pre-treatment covariates.
- Post-treatment fields are never used as targeting features.
- Revenue per eligible customer is the primary commercial outcome.
- Confidence intervals and effect sizes are interpreted alongside p-values.
- Subgroup findings require interaction evidence rather than separate significance tests.
- A statistically significant result is not automatically called profitable.
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
│   └── 02_experiment_analysis.ipynb
├── reports/
│   ├── dashboard_plan.md
│   ├── executive_memo_plan.md
│   └── validation_findings.md
├── scripts/
│   ├── download_data.py
│   ├── run_experiment_analysis.py
│   └── run_validation.py
├── sql/
│   ├── 01_quality_checks.sql
│   └── 02_experiment_summary.sql
└── src/
    ├── __init__.py
    ├── data_validation.py
    ├── experiment_metrics.py
    └── profit_model.py
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

## Current build checklist

- [x] Define the business decision
- [x] Create repository structure
- [x] Add reproducible download and validation framework
- [x] Download and profile the raw data
- [x] Complete experiment-integrity checks
- [ ] Estimate overall treatment effects
- [ ] Build commercial sensitivity model
- [ ] Complete segment and targeting analysis
- [ ] Build executive dashboard
- [ ] Publish decision memo and final recommendation

## Author

**Chukwujekwu Joseph Ezema**  
[Portfolio](https://jeks042.github.io/) · [LinkedIn](https://www.linkedin.com/in/chukwujekwu-joseph-ezema-7b1624129/) · [GitHub](https://github.com/Jeks042)
