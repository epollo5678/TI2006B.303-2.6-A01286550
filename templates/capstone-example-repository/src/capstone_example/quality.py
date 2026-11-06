"""Small examples of reusable, testable data-quality checks."""

import pandas as pd


def require_columns(frame: pd.DataFrame, required: set[str]) -> None:
    """Raise a clear error when an analysis table is missing required columns."""
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
