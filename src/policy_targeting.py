"""Held-out policy evaluation for the three-arm Hillstrom experiment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

ARM_ORDER = ["No E-Mail", "Mens E-Mail", "Womens E-Mail"]
NUMERIC_FEATURES = ["recency", "history", "mens", "womens", "newbie"]
CATEGORICAL_FEATURES = ["history_segment", "zip_code", "channel"]
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES


@dataclass(frozen=True)
class TargetingResult:
    train_frame: pd.DataFrame
    test_frame: pd.DataFrame
    transformed_train: np.ndarray
    transformed_test: np.ndarray
    potential_outcomes: pd.DataFrame
    models: dict[str, RandomForestRegressor]
    preprocessor: ColumnTransformer


def split_experiment(
    frame: pd.DataFrame,
    test_size: float = 0.30,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Create a treatment-stratified holdout split."""
    train, test = train_test_split(
        frame,
        test_size=test_size,
        random_state=random_state,
        stratify=frame["segment"],
    )
    return train.reset_index(drop=True), test.reset_index(drop=True)


def build_preprocessor() -> ColumnTransformer:
    """Create a deterministic pre-treatment feature transformer."""
    return ColumnTransformer(
        transformers=[
            ("numeric", "passthrough", NUMERIC_FEATURES),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                CATEGORICAL_FEATURES,
            ),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )


def fit_t_learner(
    frame: pd.DataFrame,
    test_size: float = 0.30,
    random_state: int = 42,
) -> TargetingResult:
    """Fit one non-negative spend model per randomized arm."""
    train, test = split_experiment(frame, test_size, random_state)
    preprocessor = build_preprocessor()
    transformed_train = preprocessor.fit_transform(train[FEATURES])
    transformed_test = preprocessor.transform(test[FEATURES])

    models: dict[str, RandomForestRegressor] = {}
    predictions: dict[str, np.ndarray] = {}

    for offset, arm in enumerate(ARM_ORDER):
        arm_mask = train["segment"].eq(arm).to_numpy()
        model = RandomForestRegressor(
            n_estimators=180,
            max_depth=10,
            min_samples_leaf=60,
            max_features=0.80,
            n_jobs=-1,
            random_state=random_state + offset,
        )
        model.fit(
            transformed_train[arm_mask],
            train.loc[arm_mask, "spend"].to_numpy(float),
        )
        models[arm] = model
        predictions[arm] = np.clip(
            model.predict(transformed_test),
            a_min=0.0,
            a_max=None,
        )

    potential_outcomes = pd.DataFrame(predictions, index=test.index)
    return TargetingResult(
        train_frame=train,
        test_frame=test,
        transformed_train=transformed_train,
        transformed_test=transformed_test,
        potential_outcomes=potential_outcomes,
        models=models,
        preprocessor=preprocessor,
    )


def fixed_policy(size: int, arm: str) -> np.ndarray:
    """Return one arm for every customer."""
    if arm not in ARM_ORDER:
        raise ValueError(f"Unknown arm: {arm}")
    return np.full(size, arm, dtype=object)


def best_revenue_policy(potential_outcomes: pd.DataFrame) -> np.ndarray:
    """Choose the arm with the highest predicted spend for each customer."""
    return potential_outcomes[ARM_ORDER].idxmax(axis=1).to_numpy()


def profit_aware_policy(
    potential_outcomes: pd.DataFrame,
    contribution_margin: float,
    contact_cost: float,
) -> np.ndarray:
    """Choose the arm with the highest predicted contribution net of contact cost."""
    if not 0 <= contribution_margin <= 1:
        raise ValueError("Contribution margin must be between 0 and 1.")
    if contact_cost < 0:
        raise ValueError("Contact cost cannot be negative.")

    net_values = potential_outcomes[ARM_ORDER].mul(contribution_margin)
    net_values.loc[:, ["Mens E-Mail", "Womens E-Mail"]] -= contact_cost
    return net_values.idxmax(axis=1).to_numpy()


def capacity_policy(
    potential_outcomes: pd.DataFrame,
    contribution_margin: float,
    contact_cost: float,
    capacity: float,
) -> np.ndarray:
    """Treat the highest-value customers up to capacity; otherwise send no email."""
    if not 0 <= capacity <= 1:
        raise ValueError("Capacity must be between 0 and 1.")

    control_value = potential_outcomes["No E-Mail"].to_numpy() * contribution_margin
    active_values = (
        potential_outcomes[["Mens E-Mail", "Womens E-Mail"]]
        .mul(contribution_margin)
        .sub(contact_cost)
    )
    best_active_arm = active_values.idxmax(axis=1).to_numpy()
    best_active_value = active_values.max(axis=1).to_numpy()
    incremental_net_value = best_active_value - control_value

    policy = fixed_policy(len(potential_outcomes), "No E-Mail")
    eligible = np.flatnonzero(incremental_net_value > 0)
    maximum_contacts = int(np.floor(capacity * len(policy)))
    if maximum_contacts <= 0 or eligible.size == 0:
        return policy

    ranked = eligible[np.argsort(incremental_net_value[eligible])[::-1]]
    selected = ranked[:maximum_contacts]
    policy[selected] = best_active_arm[selected]
    return policy


def _policy_contributions(
    test_frame: pd.DataFrame,
    potential_outcomes: pd.DataFrame,
    policy: np.ndarray,
    propensity: float = 1 / 3,
) -> tuple[np.ndarray, np.ndarray]:
    """Return individual IPS and doubly robust spend contributions."""
    observed_arm = test_frame["segment"].to_numpy()
    observed_outcome = test_frame["spend"].to_numpy(float)
    policy = np.asarray(policy, dtype=object)

    arm_to_index = {arm: idx for idx, arm in enumerate(ARM_ORDER)}
    prediction_matrix = potential_outcomes[ARM_ORDER].to_numpy()
    observed_index = np.array([arm_to_index[arm] for arm in observed_arm])
    policy_index = np.array([arm_to_index[arm] for arm in policy])

    observed_prediction = prediction_matrix[
        np.arange(len(test_frame)), observed_index
    ]
    policy_prediction = prediction_matrix[
        np.arange(len(test_frame)), policy_index
    ]
    matches = observed_arm == policy

    ips = matches.astype(float) * observed_outcome / propensity
    doubly_robust = (
        policy_prediction
        + matches.astype(float)
        * (observed_outcome - observed_prediction)
        / propensity
    )
    return ips, doubly_robust


def evaluate_policy(
    test_frame: pd.DataFrame,
    potential_outcomes: pd.DataFrame,
    policy: np.ndarray,
    policy_name: str,
    contribution_margin: float,
    contact_cost: float,
) -> dict[str, float | str]:
    """Evaluate a fixed or personalised policy on randomized holdout data."""
    ips, doubly_robust = _policy_contributions(
        test_frame, potential_outcomes, policy
    )
    treated = np.asarray(policy) != "No E-Mail"
    treated_share = float(treated.mean())
    dr_spend = float(doubly_robust.mean())
    ips_spend = float(ips.mean())
    dr_profit = contribution_margin * dr_spend - contact_cost * treated_share
    ips_profit = contribution_margin * ips_spend - contact_cost * treated_share

    return {
        "policy": policy_name,
        "customers": len(test_frame),
        "treated_share": treated_share,
        "no_email_share": float((np.asarray(policy) == "No E-Mail").mean()),
        "mens_email_share": float((np.asarray(policy) == "Mens E-Mail").mean()),
        "womens_email_share": float((np.asarray(policy) == "Womens E-Mail").mean()),
        "ips_spend_per_customer": ips_spend,
        "dr_spend_per_customer": dr_spend,
        "ips_profit_per_customer": float(ips_profit),
        "dr_profit_per_customer": float(dr_profit),
        "dr_profit_per_1000": float(1000 * dr_profit),
        "contribution_margin": contribution_margin,
        "contact_cost": contact_cost,
    }


def policy_summary(
    result: TargetingResult,
    contribution_margin: float = 0.40,
    contact_cost: float = 0.10,
) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
    """Compare fixed, revenue-maximizing and profit-aware policies."""
    size = len(result.test_frame)
    policies = {
        "No E-Mail to all": fixed_policy(size, "No E-Mail"),
        "Mens E-Mail to all": fixed_policy(size, "Mens E-Mail"),
        "Womens E-Mail to all": fixed_policy(size, "Womens E-Mail"),
        "Model: highest predicted spend": best_revenue_policy(
            result.potential_outcomes
        ),
        "Model: profit-aware": profit_aware_policy(
            result.potential_outcomes,
            contribution_margin=contribution_margin,
            contact_cost=contact_cost,
        ),
    }

    records = [
        evaluate_policy(
            result.test_frame,
            result.potential_outcomes,
            policy,
            name,
            contribution_margin,
            contact_cost,
        )
        for name, policy in policies.items()
    ]
    summary = pd.DataFrame.from_records(records)
    mens_profit = float(
        summary.loc[
            summary["policy"].eq("Mens E-Mail to all"),
            "dr_profit_per_customer",
        ].iloc[0]
    )
    summary["dr_profit_uplift_vs_mens_per_customer"] = (
        summary["dr_profit_per_customer"] - mens_profit
    )
    summary["dr_profit_uplift_vs_mens_per_1000"] = (
        1000 * summary["dr_profit_uplift_vs_mens_per_customer"]
    )
    return summary.sort_values("dr_profit_per_customer", ascending=False), policies


def capacity_curve(
    result: TargetingResult,
    capacities: Iterable[float] = (0.10, 0.25, 0.50, 0.75, 1.00),
    contribution_margin: float = 0.40,
    contact_cost: float = 0.10,
) -> pd.DataFrame:
    """Evaluate a profit-ranked policy across contact-capacity limits."""
    mens_policy = fixed_policy(len(result.test_frame), "Mens E-Mail")
    mens = evaluate_policy(
        result.test_frame,
        result.potential_outcomes,
        mens_policy,
        "Mens E-Mail to all",
        contribution_margin,
        contact_cost,
    )
    records = []
    for capacity in capacities:
        policy = capacity_policy(
            result.potential_outcomes,
            contribution_margin,
            contact_cost,
            capacity,
        )
        record = evaluate_policy(
            result.test_frame,
            result.potential_outcomes,
            policy,
            f"Capacity {capacity:.0%}",
            contribution_margin,
            contact_cost,
        )
        record["capacity"] = capacity
        record["dr_profit_uplift_vs_mens_per_1000"] = (
            record["dr_profit_per_1000"] - mens["dr_profit_per_1000"]
        )
        records.append(record)
    return pd.DataFrame.from_records(records)


def policy_sensitivity(
    result: TargetingResult,
    contribution_margins: Iterable[float] = (0.25, 0.40, 0.60),
    contact_costs: Iterable[float] = (0.05, 0.10, 0.20),
) -> pd.DataFrame:
    """Evaluate the profit-aware policy across business assumptions."""
    records = []
    size = len(result.test_frame)
    for margin in contribution_margins:
        for cost in contact_costs:
            policy = profit_aware_policy(result.potential_outcomes, margin, cost)
            candidate = evaluate_policy(
                result.test_frame,
                result.potential_outcomes,
                policy,
                "Model: profit-aware",
                margin,
                cost,
            )
            mens = evaluate_policy(
                result.test_frame,
                result.potential_outcomes,
                fixed_policy(size, "Mens E-Mail"),
                "Mens E-Mail to all",
                margin,
                cost,
            )
            candidate["dr_profit_uplift_vs_mens_per_1000"] = (
                candidate["dr_profit_per_1000"] - mens["dr_profit_per_1000"]
            )
            records.append(candidate)
    return pd.DataFrame.from_records(records)


def model_diagnostics(result: TargetingResult) -> pd.DataFrame:
    """Report outcome-model diagnostics without treating them as policy evidence."""
    records = []
    for arm in ARM_ORDER:
        mask = result.test_frame["segment"].eq(arm).to_numpy()
        actual = result.test_frame.loc[mask, "spend"].to_numpy(float)
        predicted = result.potential_outcomes.loc[mask, arm].to_numpy(float)
        records.append(
            {
                "arm": arm,
                "test_customers": int(mask.sum()),
                "observed_mean_spend": float(actual.mean()),
                "predicted_mean_spend": float(predicted.mean()),
                "mae": float(mean_absolute_error(actual, predicted)),
                "rmse": float(mean_squared_error(actual, predicted) ** 0.5),
            }
        )
    return pd.DataFrame.from_records(records)


def feature_importance(result: TargetingResult) -> pd.DataFrame:
    """Average treatment-arm feature importance as a descriptive diagnostic."""
    feature_names = result.preprocessor.get_feature_names_out()
    records = []
    for arm, model in result.models.items():
        for feature, importance in zip(feature_names, model.feature_importances_):
            records.append(
                {
                    "arm": arm,
                    "feature": feature,
                    "importance": float(importance),
                }
            )
    frame = pd.DataFrame.from_records(records)
    return (
        frame.groupby("feature", as_index=False)["importance"]
        .mean()
        .rename(columns={"importance": "mean_importance_across_arms"})
        .sort_values("mean_importance_across_arms", ascending=False)
    )


def bootstrap_policy_uplift(
    result: TargetingResult,
    policies: dict[str, np.ndarray],
    contribution_margin: float = 0.40,
    contact_cost: float = 0.10,
    iterations: int = 500,
    random_state: int = 42,
) -> pd.DataFrame:
    """Bootstrap paired profit differences versus Men's-send-to-all."""
    rng = np.random.default_rng(random_state)
    n = len(result.test_frame)
    baseline_policy = policies["Mens E-Mail to all"]
    _, baseline_dr = _policy_contributions(
        result.test_frame,
        result.potential_outcomes,
        baseline_policy,
    )
    baseline_treated = (baseline_policy != "No E-Mail").astype(float)
    baseline_contribution = (
        contribution_margin * baseline_dr - contact_cost * baseline_treated
    )

    records = []
    for name, policy in policies.items():
        _, policy_dr = _policy_contributions(
            result.test_frame,
            result.potential_outcomes,
            policy,
        )
        treated = (policy != "No E-Mail").astype(float)
        policy_contribution = (
            contribution_margin * policy_dr - contact_cost * treated
        )
        individual_difference = policy_contribution - baseline_contribution
        point = float(individual_difference.mean())
        draws = np.empty(iterations, dtype=float)
        for index in range(iterations):
            sample = rng.integers(0, n, size=n)
            draws[index] = individual_difference[sample].mean()
        records.append(
            {
                "policy": name,
                "profit_uplift_vs_mens_per_customer": point,
                "profit_uplift_vs_mens_per_1000": 1000 * point,
                "bootstrap_ci_low_per_1000": 1000 * float(np.quantile(draws, 0.025)),
                "bootstrap_ci_high_per_1000": 1000 * float(np.quantile(draws, 0.975)),
                "bootstrap_iterations": iterations,
            }
        )
    return pd.DataFrame.from_records(records)
