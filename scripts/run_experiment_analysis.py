"""Estimate main experiment effects and export review-ready tables."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.stats.multitest import multipletests

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_validation import load_data, validate_data
from src.experiment_metrics import arm_summary, main_effect_table
from src.profit_model import sensitivity_table

DATA_PATH = PROJECT_ROOT / "data/raw/hillstrom.csv"
OUTPUT_DIR = PROJECT_ROOT / "reports/analysis_tables"
CONTROL = "No E-Mail"
TREATMENTS = ("Mens E-Mail", "Womens E-Mail")


def add_decision_fields(effects: pd.DataFrame) -> pd.DataFrame:
    """Add precision, multiplicity and practical interpretation fields."""
    result = effects.copy()
    result["ci_width"] = result["ci_high"] - result["ci_low"]
    result["interval_excludes_zero"] = (
        (result["ci_low"] > 0) | (result["ci_high"] < 0)
    )

    result["holm_p_value_within_outcome"] = np.nan
    for _, indexes in result.groupby("outcome").groups.items():
        adjusted = multipletests(
            result.loc[indexes, "p_value"].to_numpy(),
            alpha=0.05,
            method="holm",
        )[1]
        result.loc[indexes, "holm_p_value_within_outcome"] = adjusted

    result["number_needed_to_treat"] = np.where(
        result["outcome"].isin(["visit", "conversion"])
        & (result["absolute_lift"] > 0),
        1 / result["absolute_lift"],
        np.nan,
    )
    return result


def build_profit_sensitivity(effects: pd.DataFrame) -> pd.DataFrame:
    """Translate spend effects and uncertainty bounds into profit scenarios."""
    records: list[pd.DataFrame] = []
    spend_effects = effects.loc[effects["outcome"] == "spend"]

    for row in spend_effects.itertuples(index=False):
        for estimate_name, estimate in (
            ("lower_95_ci", row.ci_low),
            ("point_estimate", row.absolute_lift),
            ("upper_95_ci", row.ci_high),
        ):
            scenarios = sensitivity_table(
                recipients=1_000,
                incremental_revenue_per_customer=float(estimate),
                contribution_margins=(0.25, 0.40, 0.60),
                contact_costs=(0.00, 0.05, 0.10, 0.25, 0.50),
            )
            scenarios.insert(0, "treatment", row.treatment)
            scenarios.insert(1, "control", row.control)
            scenarios.insert(2, "effect_estimate", estimate_name)
            records.append(scenarios)

    return pd.concat(records, ignore_index=True)


def main() -> None:
    frame = load_data(DATA_PATH)
    validation = validate_data(frame)

    if validation.rows != 64_000:
        raise ValueError("Analysis stopped: source row count does not equal 64,000.")
    if validation.missing_cells != 0:
        raise ValueError("Analysis stopped: missing values were found.")
    if validation.sample_ratio_p_value < 0.01:
        raise ValueError("Analysis stopped: possible sample-ratio mismatch.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    summary = arm_summary(frame)
    effects = add_decision_fields(
        main_effect_table(frame, treatments=TREATMENTS, control=CONTROL)
    )
    profit = build_profit_sensitivity(effects)

    summary.to_csv(OUTPUT_DIR / "arm_summary.csv", index=False)
    effects.to_csv(OUTPUT_DIR / "main_treatment_effects.csv", index=False)
    profit.to_csv(OUTPUT_DIR / "profit_sensitivity_per_1000.csv", index=False)

    primary = effects.loc[effects["outcome"] == "spend"].copy()
    primary.to_csv(OUTPUT_DIR / "primary_revenue_effects.csv", index=False)

    print("Main experiment analysis completed.")
    print("\nArm summary:")
    print(summary.to_string(index=False))
    print("\nMain treatment effects:")
    print(effects.to_string(index=False))


if __name__ == "__main__":
    main()
