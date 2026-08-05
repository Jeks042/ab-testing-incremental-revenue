"""Core summaries and treatment-effect estimates for the experiment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd
from scipy.stats import norm, ttest_ind
from statsmodels.stats.proportion import proportions_ztest


@dataclass(frozen=True)
class BinaryEffect:
    treatment: str
    control: str
    outcome: str
    treatment_rate: float
    control_rate: float
    absolute_lift: float
    relative_lift: float | None
    ci_low: float
    ci_high: float
    z_statistic: float
    p_value: float


@dataclass(frozen=True)
class ContinuousEffect:
    treatment: str
    control: str
    outcome: str
    treatment_mean: float
    control_mean: float
    mean_difference: float
    welch_t_statistic: float
    welch_p_value: float
    bootstrap_ci_low: float
    bootstrap_ci_high: float


def arm_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """Create a transparent descriptive summary by treatment arm."""
    grouped = frame.groupby("segment", observed=True)
    summary = grouped.agg(
        customers=("segment", "size"),
        visits=("visit", "sum"),
        visit_rate=("visit", "mean"),
        conversions=("conversion", "sum"),
        conversion_rate=("conversion", "mean"),
        total_revenue=("spend", "sum"),
        revenue_per_customer=("spend", "mean"),
    )

    converter_aov = grouped.apply(
        lambda group: group.loc[group["conversion"] == 1, "spend"].mean(),
        include_groups=False,
    )
    summary["average_order_value"] = converter_aov
    summary["zero_spend_share"] = grouped["spend"].apply(
        lambda values: float((values == 0).mean())
    )
    return summary.reset_index()


def binary_treatment_effect(
    frame: pd.DataFrame,
    treatment: str,
    control: str,
    outcome: str,
    confidence: float = 0.95,
) -> BinaryEffect:
    """Estimate a risk difference with a Wald interval and z-test."""
    if outcome not in {"visit", "conversion"}:
        raise ValueError("Binary outcome must be 'visit' or 'conversion'.")

    treated = frame.loc[frame["segment"] == treatment, outcome].astype(int)
    control_values = frame.loc[frame["segment"] == control, outcome].astype(int)

    treatment_rate = float(treated.mean())
    control_rate = float(control_values.mean())
    difference = treatment_rate - control_rate
    relative_lift = (
        difference / control_rate if control_rate != 0 else None
    )

    standard_error = np.sqrt(
        treatment_rate * (1 - treatment_rate) / len(treated)
        + control_rate * (1 - control_rate) / len(control_values)
    )
    z_critical = norm.ppf(1 - (1 - confidence) / 2)
    ci_low = difference - z_critical * standard_error
    ci_high = difference + z_critical * standard_error

    statistic, p_value = proportions_ztest(
        count=np.array([treated.sum(), control_values.sum()]),
        nobs=np.array([len(treated), len(control_values)]),
        alternative="two-sided",
    )

    return BinaryEffect(
        treatment=treatment,
        control=control,
        outcome=outcome,
        treatment_rate=treatment_rate,
        control_rate=control_rate,
        absolute_lift=float(difference),
        relative_lift=float(relative_lift) if relative_lift is not None else None,
        ci_low=float(ci_low),
        ci_high=float(ci_high),
        z_statistic=float(statistic),
        p_value=float(p_value),
    )


def _bootstrap_mean_difference(
    treated: np.ndarray,
    control: np.ndarray,
    iterations: int,
    confidence: float,
    random_state: int,
) -> tuple[float, float]:
    rng = np.random.default_rng(random_state)
    differences = np.empty(iterations, dtype=float)

    for index in range(iterations):
        treated_sample = rng.choice(treated, size=len(treated), replace=True)
        control_sample = rng.choice(control, size=len(control), replace=True)
        differences[index] = treated_sample.mean() - control_sample.mean()

    tail = (1 - confidence) / 2
    return (
        float(np.quantile(differences, tail)),
        float(np.quantile(differences, 1 - tail)),
    )


def continuous_treatment_effect(
    frame: pd.DataFrame,
    treatment: str,
    control: str,
    outcome: str = "spend",
    bootstrap_iterations: int = 2_000,
    confidence: float = 0.95,
    random_state: int = 42,
) -> ContinuousEffect:
    """Estimate a mean difference with Welch and bootstrap uncertainty."""
    treated = frame.loc[frame["segment"] == treatment, outcome].to_numpy(float)
    control_values = frame.loc[frame["segment"] == control, outcome].to_numpy(float)

    statistic, p_value = ttest_ind(
        treated,
        control_values,
        equal_var=False,
        nan_policy="raise",
    )
    ci_low, ci_high = _bootstrap_mean_difference(
        treated,
        control_values,
        iterations=bootstrap_iterations,
        confidence=confidence,
        random_state=random_state,
    )

    return ContinuousEffect(
        treatment=treatment,
        control=control,
        outcome=outcome,
        treatment_mean=float(treated.mean()),
        control_mean=float(control_values.mean()),
        mean_difference=float(treated.mean() - control_values.mean()),
        welch_t_statistic=float(statistic),
        welch_p_value=float(p_value),
        bootstrap_ci_low=ci_low,
        bootstrap_ci_high=ci_high,
    )


def main_effect_table(
    frame: pd.DataFrame,
    treatments: Iterable[str] = ("Mens E-Mail", "Womens E-Mail"),
    control: str = "No E-Mail",
) -> pd.DataFrame:
    """Return the core visit, conversion and spend effects in one table."""
    records: list[dict[str, object]] = []

    for treatment in treatments:
        for outcome in ("visit", "conversion"):
            effect = binary_treatment_effect(frame, treatment, control, outcome)
            records.append(
                {
                    "treatment": treatment,
                    "control": control,
                    "outcome": outcome,
                    "treatment_mean": effect.treatment_rate,
                    "control_mean": effect.control_rate,
                    "absolute_lift": effect.absolute_lift,
                    "relative_lift": effect.relative_lift,
                    "ci_low": effect.ci_low,
                    "ci_high": effect.ci_high,
                    "p_value": effect.p_value,
                    "method": "two-sample proportion z-test",
                }
            )

        spend_effect = continuous_treatment_effect(frame, treatment, control)
        records.append(
            {
                "treatment": treatment,
                "control": control,
                "outcome": "spend",
                "treatment_mean": spend_effect.treatment_mean,
                "control_mean": spend_effect.control_mean,
                "absolute_lift": spend_effect.mean_difference,
                "relative_lift": (
                    spend_effect.mean_difference / spend_effect.control_mean
                    if spend_effect.control_mean != 0
                    else None
                ),
                "ci_low": spend_effect.bootstrap_ci_low,
                "ci_high": spend_effect.bootstrap_ci_high,
                "p_value": spend_effect.welch_p_value,
                "method": "Welch test with bootstrap interval",
            }
        )

    return pd.DataFrame.from_records(records)
