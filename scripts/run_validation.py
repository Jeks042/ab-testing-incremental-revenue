"""Run experiment-integrity checks and export review-ready tables."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.data_validation import load_data, numeric_balance_table, validate_data

DATA_PATH = Path("data/raw/hillstrom.csv")
OUTPUT_DIR = Path("reports/tables")


def main() -> None:
    frame = load_data(DATA_PATH)
    report = validate_data(frame)
    balance = numeric_balance_table(frame)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    report_dict = report.to_dict()
    (OUTPUT_DIR / "validation_report.json").write_text(
        json.dumps(report_dict, indent=2, default=str),
        encoding="utf-8",
    )

    pd.Series(report_dict, name="value").rename_axis("check").reset_index().to_csv(
        OUTPUT_DIR / "validation_report.csv",
        index=False,
    )

    allocation = (
        frame["segment"].value_counts().rename("customers").to_frame()
    )
    allocation["allocation_pct"] = allocation["customers"] / len(frame)
    allocation.reset_index(names="segment").to_csv(
        OUTPUT_DIR / "treatment_allocation.csv",
        index=False,
    )

    balance.assign(
        absolute_smd=balance["standardised_mean_difference"].abs()
    ).sort_values("absolute_smd", ascending=False).to_csv(
        OUTPUT_DIR / "numeric_balance.csv",
        index=False,
    )

    for field in ("history_segment", "zip_code", "channel"):
        table = pd.crosstab(
            frame[field],
            frame["segment"],
            normalize="columns",
        )
        table.to_csv(OUTPUT_DIR / f"categorical_balance_{field}.csv")

    print("Validation completed.")
    print(json.dumps(report_dict, indent=2, default=str))
    print("\nLargest absolute standardised mean differences:")
    print(
        balance.assign(
            absolute_smd=balance["standardised_mean_difference"].abs()
        )
        .sort_values("absolute_smd", ascending=False)
        .head(10)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
