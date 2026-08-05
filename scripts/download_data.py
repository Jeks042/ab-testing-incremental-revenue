"""Download and validate the Hillstrom email experiment dataset.

The raw file is stored locally and excluded from version control. The script
tries the original MineThatData host first and then the verified compressed
copy used by scikit-uplift.
"""

from __future__ import annotations

import hashlib
import sys
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Final

import pandas as pd
import requests


@dataclass(frozen=True)
class DataSource:
    name: str
    url: str
    compression: str | None = None
    md5: str | None = None


SOURCES: Final = (
    DataSource(
        name="original MineThatData host",
        url=(
            "http://www.minethatdata.com/"
            "Kevin_Hillstrom_MineThatData_"
            "E-MailAnalytics_DataMiningChallenge_2008.03.20.csv"
        ),
    ),
    DataSource(
        name="scikit-uplift S3 mirror",
        url=(
            "https://hillstorm1.s3.us-east-2.amazonaws.com/"
            "hillstorm_no_indices.csv.gz"
        ),
        compression="gzip",
        md5="a68a81291f53a14f4e29002629803ba3",
    ),
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


def _download(source: DataSource, timeout: int = 90) -> bytes:
    response = requests.get(source.url, timeout=timeout)
    response.raise_for_status()
    content = response.content

    if source.md5:
        observed = hashlib.md5(content).hexdigest()  # noqa: S324 - integrity only
        if observed != source.md5:
            raise ValueError(
                f"Checksum mismatch: expected {source.md5}, observed {observed}."
            )
    return content


def _read_content(content: bytes, compression: str | None) -> pd.DataFrame:
    return pd.read_csv(BytesIO(content), compression=compression)


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
    for source in SOURCES:
        try:
            print(f"Downloading from {source.name}...")
            content = _download(source)
            frame = _read_content(content, source.compression)
            _validate_frame(frame)
            frame.to_csv(OUTPUT_PATH, index=False)
            print(f"Saved validated dataset to {OUTPUT_PATH}")
            print(frame["segment"].value_counts().to_string())
            return 0
        except Exception as exc:  # noqa: BLE001 - report each source failure clearly
            errors.append(f"{source.name}: {exc}")

    print("Unable to download a valid dataset from the configured sources.")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
