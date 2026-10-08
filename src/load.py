"""Load and profile the Levine 32-marker CyTOF FCS file."""

import fcsparser


def load_fcs(path):
    """Read an FCS file.

    Returns a tuple (meta, df): meta is a dict of the file's header
    keywords, df is a pandas DataFrame with one row per cell (event)
    and one column per channel.
    """
    meta, df = fcsparser.parse(path)
    return meta, df


def profile(df):
    """Summary statistics per column (count, mean, std, min, quartiles, max).

    Transposed so each channel is a row, which is easier to read with
    many columns.
    """
    return df.describe().T
