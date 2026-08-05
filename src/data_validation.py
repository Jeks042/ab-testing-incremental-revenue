"""Data-quality and randomisation checks for the Hillstrom experiment."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.stats import chisquare

EXPECTED_COLUMNS = [
    "recency",
    "history_segment",
    "history",
    "mens",
    "womens",
    "zip_code",
    "newbie",
    "channel",
    "segment",
    "visit",
    "conversion",
    "spend",
]
TREATMENT_ORDER = ["No E-Mail", "Mens E-Mail", "Womens E-Mail"]
BINARY_COLUMNS = ["mens", "womens", "newbie", "visit", "conversion"]


@dataclass(frozen=True)
class ValidationReport:
    rows: int
    columns: int
    duplicate_rows: int
    missing_cells: int
    invalid_binary_values: dict[str, list[Any]]
    negative_history_rows: int
    negative_spend_rows: int
    positive_spend_without_conversion: int
    conversion_without_positive_spend: int
    conversion_without_visit: int
    treatment_counts: dict[str, int]
    sample_ratio_chi2: float
    sample_ratio_p_value: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_data(path: str | Path = "data/raw/hillstrom.csv") -> pd.DataFrame:
    """Load the raw experiment file without altering source values."""
    frame = pd.read_csv(path)
    missing = sorted(set(EXPECTED_COLUMNS).difference(frame.columns))
    unexpected = sorted(set(frame.columns).difference(EXPECTED_COLUMNS))
    if missing or unexpected:
        raise ValueError(
            f"Schema mismatch. Missing={missing or 'none'}; "
            f"unexpected={unexpected or 'none'}."
        )
    return frame.loc[:, EXPECTED_COLUMNS].copy()


def treatment_allocation_test(frame: pd.DataFrame) -> tuple[pd.Series, float, float]:
    """Compare observed treatment counts with an equal three-arm allocation."""
    counts = frame["segment"].value_counts().reindex(TREATMENT_ORDER, fill_value=0)
    expected = np.repeat(len(frame) / len(TREATMENT_ORDER), len(TREATMENT_ORDER))
    statistic, p_value = chisquare(counts.to_numpy(), f_exp=expected)
    return counts, float(statistic), float(p_value)


def validate_data(frame: pd.DataFrame) -> ValidationReport:
    """Return transparent quality checks without silently repairing records."""
    invalid_binary_values: dict[str, list[Any]] = {}
    for column in BINARY_COLUMNS:
        invalid = sorted(set(frame[column].dropna().unique()).difference({0, 1}))
        invalid_binary_values[column] = invalid

    counts, statistic, p_value = treatment_allocation_test(frame)

    report = ValidationReport(
        rows=len(frame),
        columns=frame.shape[1],
        duplicate_rows=int(frame.duplicated().sum()),
        missing_cells=int(frame.isna().sum().sum()),
        invalid_binary_values=invalid_binary_values,
        negative_history_rows=int((frame["history"] < 0).sum()),
        negative_spend_rows=int((frame["spend"] < 0).sum()),
        positive_spend_without_conversion=int(
            ((frame["spend"] > 0) & (frame["conversion"] != 1)).sum()
        ),
        conversion_without_positive_spend=int(
            ((frame["conversion"] == 1) & (frame["spend"] <= 0)).sum()
        ),
        conversion_without_visit=int(
            ((frame["conversion"] == 1) & (frame["visit"] != 1)).sum()
        ),
        treatment_counts={key: int(value) for key, value in counts.items()},
        sample_ratio_chi2=statistic,
        sample_ratio_p_value=p_value,
    )
    return report


def standardised_mean_difference(
    treated: pd.Series, control: pd.Series
) -> float:
    """Calculate the standardised mean difference for a numeric/binary field."""
    treated_values = treated.dropna().astype(float)
    control_values = control.dropna().astype(float)
    pooled_variance = (
        treated_values.var(ddof=1) + control_values.var(ddof=1)
    ) / 2
    if pooled_variance <= 0 or np.isnan(pooled_variance):
        return 0.0
    return float(
        (treated_values.mean() - control_values.mean())
        / np.sqrt(pooled_variance)
    )


def numeric_balance_table(
    frame: pd.DataFrame,
    columns: list[str] | None = None,
    control_label: str = "No E-Mail",
) -> pd.DataFrame:
    """Summarise pre-treatment numeric balance against the control arm."""
    columns = columns or ["recency", "history", "mens", "womens", "newbie"]
    control = frame.loc[frame["segment"] == control_label]
    records: list[dict[str, Any]] = []

    for treatment in [label for label in TREATMENT_ORDER if label != control_label]:
        treated = frame.loc[frame["segment"] == treatment]
        for column in columns:
            records.append(
                {
                    "treatment": treatment,
                    "control": control_label,
                    "variable": column,
                    "treatment_mean": treated[column].mean(),
                    "control_mean": control[column].mean(),
                    "standardised_mean_difference": standardised_mean_difference(
                        treated[column], control[column]
                    ),
                }
            )

    return pd.DataFrame.from_records(records)
