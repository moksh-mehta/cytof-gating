from pathlib import Path

import pandas as pd
import pytest

from src.load import load_fcs

DATA = Path(__file__).parents[1] / "data" / "Levine_32dim_notransform.fcs"

# Skip every test in this file when the data isn't downloaded (data/ is not in the repo).
pytestmark = pytest.mark.skipif(
    not DATA.exists(),
    reason=f"{DATA.name} not found in data/. Download it from "
    "https://github.com/lmweber/benchmark-data-Levine-32-dim",
)

EXPECTED_ROWS = 265627
EXPECTED_COLUMNS = [
    "Time", "Cell_length", "DNA1", "DNA2", "CD45RA", "CD133", "CD19", "CD22",
    "CD11b", "CD4", "CD8", "CD34", "Flt3", "CD20", "CXCR4", "CD235ab", "CD45",
    "CD123", "CD321", "CD14", "CD33", "CD47", "CD11c", "CD7", "CD15", "CD16",
    "CD44", "CD38", "CD13", "CD3", "CD61", "CD117", "CD49d", "HLA-DR", "CD64",
    "CD41", "Viability", "file_number", "event_number", "label", "individual",
]


@pytest.fixture(scope="module")
def df():
    _, df = load_fcs(DATA)
    return df


def test_returns_dataframe(df):
    assert isinstance(df, pd.DataFrame)


def test_row_count(df):
    assert len(df) == EXPECTED_ROWS


def test_columns(df):
    assert list(df.columns) == EXPECTED_COLUMNS
