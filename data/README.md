# Data

## Experiment population

The analysis uses the Hillstrom email marketing experiment published through the MineThatData E-Mail Analytics and Data Mining Challenge. The dataset contains **64,000 customers** allocated approximately equally across three randomised arms:

- `Mens E-Mail`
- `Womens E-Mail`
- `No E-Mail`

Customer characteristics were measured before treatment. Website visit, conversion and spend were observed after treatment and used as experiment outcomes.

Original experiment description: [MineThatData E-Mail Analytics and Data Mining Challenge](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)

## Data used in the analysis

| Field | Analytical role | Description |
|---|---|---|
| `recency` | Pre-treatment | Months since last purchase |
| `history_segment` | Pre-treatment | Prior-year spend band |
| `history` | Pre-treatment | Customer spend in the prior year |
| `mens` | Pre-treatment | Previous purchase of men's merchandise |
| `womens` | Pre-treatment | Previous purchase of women's merchandise |
| `zip_code` | Pre-treatment | Urban, suburban or rural classification |
| `newbie` | Pre-treatment | New-customer indicator |
| `channel` | Pre-treatment | Prior purchase channel |
| `segment` | Treatment | Randomised email treatment or control |
| `visit` | Outcome | Website visit during the outcome period |
| `conversion` | Outcome | Purchase during the outcome period |
| `spend` | Primary commercial outcome | Spend during the outcome period |

## Validation outcome

The source data passed the experiment-integrity review before treatment effects were estimated:

- **64,000 rows** and the expected 12-field schema were reconciled.
- No missing cells or invalid binary values were found.
- No negative spend values or outcome-consistency exceptions were identified.
- Treatment allocation showed no evidence of sample-ratio mismatch (`p = 0.9037`).
- Baseline differences across the reviewed pre-treatment variables were immaterial; the largest absolute standardised mean difference was **0.0086**.
- **6,562 exact row matches** were retained because the source contains no customer identifier and identical observed records cannot be assumed to represent duplicate customers.

The primary analysis therefore uses the full **64,000-customer intention-to-treat population** with no row exclusions.

See [experiment-integrity findings](../reports/validation_findings.md) for the complete review.

## Provenance and reproducibility

The raw CSV is not committed to the repository. `scripts/download_data.py` retrieves the source data and validates the expected schema and row count before analysis. When the original MineThatData host is unavailable, the script uses the compressed Hillstrom copy referenced by scikit-uplift and verifies that fallback against its published MD5 checksum.

The project does not claim ownership of the underlying dataset. All analysis, validation logic, commercial modelling and reporting in this repository were produced from the published experiment data.
