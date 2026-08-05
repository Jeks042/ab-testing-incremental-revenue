"""Run held-out treatment-policy analysis and export decision tables."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_validation import load_data
from src.policy_targeting import (
    bootstrap_policy_uplift,
    capacity_curve,
    feature_importance,
    fit_t_learner,
    model_diagnostics,
    policy_sensitivity,
    policy_summary,
)

DATA_PATH = PROJECT_ROOT / "data/raw/hillstrom.csv"
OUTPUT_DIR = PROJECT_ROOT / "reports/targeting_tables"
REFERENCE_MARGIN = 0.40
REFERENCE_CONTACT_COST = 0.10


def main() -> None:
    frame = load_data(DATA_PATH)
    result = fit_t_learner(frame, test_size=0.30, random_state=42)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    summary, policies = policy_summary(
        result,
        contribution_margin=REFERENCE_MARGIN,
        contact_cost=REFERENCE_CONTACT_COST,
    )
    capacity = capacity_curve(
        result,
        contribution_margin=REFERENCE_MARGIN,
        contact_cost=REFERENCE_CONTACT_COST,
    )
    sensitivity = policy_sensitivity(result)
    diagnostics = model_diagnostics(result)
    importance = feature_importance(result)
    intervals = bootstrap_policy_uplift(
        result,
        policies,
        contribution_margin=REFERENCE_MARGIN,
        contact_cost=REFERENCE_CONTACT_COST,
        iterations=500,
        random_state=42,
    )

    profit_policy = policies["Model: profit-aware"]
    recommendation_share = (
        __import__("pandas")
        .Series(profit_policy, name="recommended_arm")
        .value_counts()
        .rename("customers")
        .to_frame()
    )
    recommendation_share["share"] = (
        recommendation_share["customers"] / len(profit_policy)
    )
    recommendation_share = recommendation_share.reset_index()

    split_summary = __import__("pandas").DataFrame(
        {
            "population": ["training", "holdout"],
            "customers": [len(result.train_frame), len(result.test_frame)],
            "share": [len(result.train_frame) / len(frame), len(result.test_frame) / len(frame)],
        }
    )

    summary.to_csv(OUTPUT_DIR / "policy_summary.csv", index=False)
    capacity.to_csv(OUTPUT_DIR / "capacity_policy_curve.csv", index=False)
    sensitivity.to_csv(OUTPUT_DIR / "policy_sensitivity.csv", index=False)
    diagnostics.to_csv(OUTPUT_DIR / "model_diagnostics.csv", index=False)
    importance.to_csv(OUTPUT_DIR / "feature_importance.csv", index=False)
    intervals.to_csv(OUTPUT_DIR / "policy_bootstrap_intervals.csv", index=False)
    recommendation_share.to_csv(
        OUTPUT_DIR / "treatment_recommendation_share.csv", index=False
    )
    split_summary.to_csv(OUTPUT_DIR / "holdout_split_summary.csv", index=False)

    print("Reference policy comparison:")
    print(summary.to_string(index=False))
    print("\nBootstrap profit uplift versus Men's-send-to-all:")
    print(intervals.to_string(index=False))
    print("\nCapacity-constrained policy results:")
    print(capacity.to_string(index=False))
    print("\nProfit-aware recommendation shares:")
    print(recommendation_share.to_string(index=False))
    print(f"\nSaved targeting tables to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
