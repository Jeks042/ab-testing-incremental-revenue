"""Run direct treatment and pre-specified segment-effect analysis."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_validation import load_data
from src.segment_analysis import (
    add_predefined_segments,
    direct_treatment_comparison,
    interaction_tests,
    segment_spend_effects,
)

DATA_PATH = PROJECT_ROOT / "data/raw/hillstrom.csv"
OUTPUT_DIR = PROJECT_ROOT / "reports/segment_tables"


def main() -> None:
    frame = add_predefined_segments(load_data(DATA_PATH))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    direct = direct_treatment_comparison(frame)
    segment_effects = segment_spend_effects(frame)
    interactions = interaction_tests(frame)

    direct.to_csv(OUTPUT_DIR / "direct_treatment_comparison.csv", index=False)
    segment_effects.to_csv(OUTPUT_DIR / "segment_spend_effects.csv", index=False)
    interactions.to_csv(OUTPUT_DIR / "segment_interaction_tests.csv", index=False)

    segment_definitions = frame[
        [
            "recency",
            "recency_band",
            "history_segment",
            "channel",
            "zip_code",
            "newbie",
            "customer_status",
            "mens",
            "womens",
            "merchandise_affinity",
        ]
    ].drop_duplicates()
    segment_definitions.to_csv(
        OUTPUT_DIR / "segment_definition_examples.csv",
        index=False,
    )

    print("Direct treatment comparison:")
    print(direct.to_string(index=False))
    print("\nJoint interaction tests:")
    print(interactions.to_string(index=False))
    print("\nLargest observed segment spend effects:")
    print(
        segment_effects.sort_values(
            "incremental_spend_per_customer",
            ascending=False,
        )
        .head(20)
        .to_string(index=False)
    )
    print(f"\nSaved analysis tables to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
