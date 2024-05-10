"""
This module plot data for chosen company
"""

import pandas as pd

def plot_data_from_column(data: str, separator: str, col: str) -> None:
    df: pd.DataFrame = pd.read_csv(data, sep=separator)
    df[col].plot()
