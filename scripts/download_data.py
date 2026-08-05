"""Download and validate the Hillstrom email experiment dataset.

The raw file is stored locally and excluded from version control. The script
tries the original MineThatData host first and then a GitHub-hosted copy used
in the CausalML examples repository.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Final

import pandas as pd
import requests

PRIMARY_URL: Final = (
    "http://www.minethatdata.com/"
    "Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv"
)
FALLBACK_URL: Final = (
    "https://raw.githubusercontent.com/uber/causalml/master/examples/data/hillstrom.csv"
)
OUTPUT_PATH: Final = Path("data/raw/hillstrom.csv")
EXPECTED_ROWS: Final = 64_000
EXPECTED_COLUMNS: Final = {
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
}
EXPECTED_SEGMENTS: Final = {"Mens E-Mail", "Womens E-Mail", "No E-Mail"}


def _download(url: str, timeout: int = 60) -> bytes:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.content


def _validate_frame(frame: pd.DataFrame) -> None:
    missing_columns = EXPECTED_COLUMNS.difference(frame.columns)
    unexpected_columns = set(frame.columns).difference(EXPECTED_COLUMNS)

    if missing_columns:
        raise ValueError(f"Missing expected columns: {sorted(missing_columns)}")
    if unexpected_columns:
        raise ValueError(f"Unexpected columns: {sorted(unexpected_columns)}")
    if len(frame) != EXPECTED_ROWS:
        raise ValueError(
            f"Expected {EXPECTED_ROWS:,} rows but received {len(frame):,}."
        )

    observed_segments = set(frame["segment"].dropna().unique())
    if observed_segments != EXPECTED_SEGMENTS:
        raise ValueError(
            "Treatment labels do not match the expected experiment arms. "
            f"Observed: {sorted(observed_segments)}"
        )

    for column in ("mens", "womens", "newbie", "visit", "conversion"):
        invalid = set(frame[column].dropna().unique()).difference({0, 1})
        if invalid:
            raise ValueError(f"Column {column!r} contains invalid values: {invalid}")

    if (frame["history"] < 0).any() or (frame["spend"] < 0).any():
        raise ValueError("Negative monetary values were found in the source file.")


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    if OUTPUT_PATH.exists():
        existing = pd.read_csv(OUTPUT_PATH)
        _validate_frame(existing)
        print(f"Validated existing file: {OUTPUT_PATH} ({len(existing):,} rows)")
        return 0

    errors: list[str] = []
    for source_name, url in (
        ("original MineThatData host", PRIMARY_URL),
        ("CausalML GitHub fallback", FALLBACK_URL),
    ):
        try:
            print(f"Downloading from {source_name}...")
            content = _download(url)
            temporary_path = OUTPUT_PATH.with_suffix(".tmp")
            temporary_path.write_bytes(content)
            frame = pd.read_csv(temporary_path)
            _validate_frame(frame)
            temporary_path.replace(OUTPUT_PATH)
            print(f"Saved validated dataset to {OUTPUT_PATH}")
            print(frame["segment"].value_counts().to_string())
            return 0
        except Exception as exc:  # noqa: BLE001 - report each source failure clearly
            errors.append(f"{source_name}: {exc}")
            temporary_path = OUTPUT_PATH.with_suffix(".tmp")
            if temporary_path.exists():
                temporary_path.unlink()

    print("Unable to download a valid dataset from the configured sources.")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
