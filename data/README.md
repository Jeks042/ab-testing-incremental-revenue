# Data

## Source

This project uses the Hillstrom email marketing experiment published by Kevin Hillstrom through the MineThatData E-Mail Analytics and Data Mining Challenge.

Original description:

- https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html

Direct source file used by the download script:

- http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv

A GitHub-hosted copy maintained in the CausalML examples repository is used only as a fallback when the original host is unavailable.

## Local file policy

The raw CSV is not committed to this repository. This keeps the repository lightweight and preserves a clear distinction between source data and analysis code.

Run:

```bash
python scripts/download_data.py
```

The script will save the validated file to:

```text
data/raw/hillstrom.csv
```

## Expected fields

| Field | Role | Description |
|---|---|---|
| `recency` | Pre-treatment | Months since last purchase |
| `history_segment` | Pre-treatment | Band of prior-year customer spend |
| `history` | Pre-treatment | Customer spend in the prior year |
| `mens` | Pre-treatment | Whether the customer previously purchased men's merchandise |
| `womens` | Pre-treatment | Whether the customer previously purchased women's merchandise |
| `zip_code` | Pre-treatment | Urban, suburban or rural classification |
| `newbie` | Pre-treatment | Whether the customer was new during the prior year |
| `channel` | Pre-treatment | Prior purchase channel |
| `segment` | Treatment | Men's email, women's email or no-email control |
| `visit` | Post-treatment outcome | Website visit during the outcome period |
| `conversion` | Post-treatment outcome | Purchase during the outcome period |
| `spend` | Post-treatment outcome | Customer spend during the outcome period |

## Data-handling principles

- The raw file is never edited in place.
- Cleaning decisions will be reproducible and documented.
- Known spelling inconsistencies in source categories will be preserved in raw data and standardised only in processed data.
- Post-treatment outcomes will not be used as targeting features.
- Treatment allocation and baseline balance will be checked before effect estimation.
- Any row exclusions will be counted, justified and reconciled to the original row total.

## Provenance note

The portfolio analysis will cite the original MineThatData publication. No claim is made that this repository created or owns the underlying dataset.
