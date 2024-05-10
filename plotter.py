"""
This module plot data for chosen company
"""

import pandas as pd

def plot_data_from_column(data: pd.DataFrame, col: pd.Series) -> None:
    data[col].plot()
