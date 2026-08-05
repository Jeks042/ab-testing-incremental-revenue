"""Direct treatment comparison and pre-specified segment-effect analysis."""

from __future__ import annotations

from typing import Iterable

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import t, ttest_ind
from statsmodels.stats.multitest import multipletests

from src.experiment_metrics import main_effect_table


DEFAULT_SEGMENT_VARIABLES = [
    "recency_band",
    "history_segment",
    "channel",
    "zip_code",
    "customer_status",
    "merchandise_affinity",
]


def add_predefined_segments(frame: pd.DataFrame) -> pd.DataFrame:
    """Create documented segments using pre-treatment fields only."""
    result = frame.copy()

    result["recency_band"] = pd.cut(
        result["recency"],
        bins=[0, 3, 6, 9, 12],
        labels=["1-3 months", "4-6 months", "7-9 months", "10-12 months"],
        include_lowest=True,
        ordered=True,
    )
    result["customer_status"] = np.where(
        result["newbie"].eq(1), "New", "Established"
    )

    conditions = [
        result["mens"].eq(1) & result["womens"].eq(1),
        result["mens"].eq(1) & result["womens"].eq(0),
        result["mens"].eq(0) & result["womens"].eq(1),
    ]
    choices = ["Both", "Mens only", "Womens only"]
    result["merchandise_affinity"] = np.select(
        conditions,
        choices,
        default="Neither",
    )
    return result


def direct_treatment_comparison(frame: pd.DataFrame) -> pd.DataFrame:
    """Compare the two active treatments directly on all main outcomes."""
    table = main_effect_table(
        frame,
        treatments=("Mens E-Mail",),
        control="Womens E-Mail",
    ).copy()
    table["holm_p_value_across_outcomes"] = multipletests(
        table["p_value"].to_numpy(),
        method="holm",
    )[1]
    table["interval_excludes_zero"] = (
        (table["ci_low"] > 0) | (table["ci_high"] < 0)
    )
    return table


def _welch_interval(
    treated: pd.Series,
    control: pd.Series,
    confidence: float = 0.95,
) -> tuple[float, float, float, float]:
    treated_values = treated.dropna().to_numpy(float)
    control_values = control.dropna().to_numpy(float)

    n_treatment = len(treated_values)
    n_control = len(control_values)
    if n_treatment < 2 or n_control < 2:
        return np.nan, np.nan, np.nan, np.nan

    variance_treatment = treated_values.var(ddof=1)
    variance_control = control_values.var(ddof=1)
    standard_error = np.sqrt(
        variance_treatment / n_treatment + variance_control / n_control
    )
    difference = treated_values.mean() - control_values.mean()

    if standard_error == 0:
        return float(difference), float(difference), np.inf, 1.0

    numerator = (
        variance_treatment / n_treatment + variance_control / n_control
    ) ** 2
    denominator = (
        (variance_treatment / n_treatment) ** 2 / (n_treatment - 1)
        + (variance_control / n_control) ** 2 / (n_control - 1)
    )
    degrees_of_freedom = numerator / denominator
    critical_value = t.ppf(1 - (1 - confidence) / 2, degrees_of_freedom)

    _, p_value = ttest_ind(
        treated_values,
        control_values,
        equal_var=False,
        nan_policy="raise",
    )
    return (
        float(difference - critical_value * standard_error),
        float(difference + critical_value * standard_error),
        float(degrees_of_freedom),
        float(p_value),
    )


def segment_spend_effects(
    frame: pd.DataFrame,
    segment_variables: Iterable[str] = DEFAULT_SEGMENT_VARIABLES,
    treatments: Iterable[str] = ("Mens E-Mail", "Womens E-Mail"),
    control: str = "No E-Mail",
) -> pd.DataFrame:
    """Estimate exploratory spend effects within pre-specified segments."""
    records: list[dict[str, object]] = []

    for segment_variable in segment_variables:
        if segment_variable not in frame.columns:
            raise ValueError(f"Missing segment variable: {segment_variable}")

        levels = frame[segment_variable].dropna().unique().tolist()
        for level in levels:
            subset = frame.loc[frame[segment_variable] == level]
            control_values = subset.loc[
                subset["segment"] == control,
                "spend",
            ]

            for treatment in treatments:
                treated_values = subset.loc[
                    subset["segment"] == treatment,
                    "spend",
                ]
                ci_low, ci_high, degrees_of_freedom, p_value = _welch_interval(
                    treated_values,
                    control_values,
                )
                treatment_mean = float(treated_values.mean())
                control_mean = float(control_values.mean())
                effect = treatment_mean - control_mean

                records.append(
                    {
                        "segment_variable": segment_variable,
                        "segment_level": str(level),
                        "treatment": treatment,
                        "control": control,
                        "treatment_customers": len(treated_values),
                        "control_customers": len(control_values),
                        "treatment_spend_per_customer": treatment_mean,
                        "control_spend_per_customer": control_mean,
                        "incremental_spend_per_customer": effect,
                        "relative_lift": (
                            effect / control_mean if control_mean != 0 else np.nan
                        ),
                        "ci_low": ci_low,
                        "ci_high": ci_high,
                        "welch_degrees_of_freedom": degrees_of_freedom,
                        "p_value": p_value,
                        "incremental_revenue_per_1000": effect * 1_000,
                    }
                )

    table = pd.DataFrame.from_records(records)
    table["holm_p_value_within_segment_variable"] = np.nan

    for _, index in table.groupby("segment_variable").groups.items():
        adjusted = multipletests(
            table.loc[index, "p_value"].to_numpy(),
            method="holm",
        )[1]
        table.loc[index, "holm_p_value_within_segment_variable"] = adjusted

    table["interval_excludes_zero"] = (
        (table["ci_low"] > 0) | (table["ci_high"] < 0)
    )
    return table


def interaction_tests(
    frame: pd.DataFrame,
    segment_variables: Iterable[str] = DEFAULT_SEGMENT_VARIABLES,
) -> pd.DataFrame:
    """Jointly test treatment-by-segment interactions for spend."""
    records: list[dict[str, object]] = []

    for segment_variable in segment_variables:
        formula = (
            "spend ~ C(segment, Treatment(reference='No E-Mail')) "
            f"* C({segment_variable})"
        )
        model = smf.ols(formula, data=frame).fit(cov_type="HC2")
        parameter_names = list(model.params.index)
        interaction_names = [name for name in parameter_names if ":" in name]

        if not interaction_names:
            records.append(
                {
                    "segment_variable": segment_variable,
                    "interaction_terms": 0,
                    "wald_statistic": np.nan,
                    "degrees_of_freedom": np.nan,
                    "p_value": np.nan,
                }
            )
            continue

        restriction = np.zeros((len(interaction_names), len(parameter_names)))
        for row, name in enumerate(interaction_names):
            restriction[row, parameter_names.index(name)] = 1

        test = model.wald_test(restriction, scalar=True)
        records.append(
            {
                "segment_variable": segment_variable,
                "interaction_terms": len(interaction_names),
                "wald_statistic": float(test.statistic),
                "degrees_of_freedom": int(len(interaction_names)),
                "p_value": float(test.pvalue),
            }
        )

    table = pd.DataFrame.from_records(records)
    table["holm_p_value_across_segment_variables"] = multipletests(
        table["p_value"].fillna(1.0).to_numpy(),
        method="holm",
    )[1]
    return table
