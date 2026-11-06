import pandas as pd
import pytest

from capstone_example.quality import require_columns


def test_require_columns_accepts_complete_frame():
    require_columns(pd.DataFrame({"kpi": [1]}), {"kpi"})


def test_require_columns_reports_missing_columns():
    with pytest.raises(ValueError, match="Missing"):
        require_columns(pd.DataFrame({"kpi": [1]}), {"kpi", "date"})
