import pandas as pd

from data import Data
from utils import Utils

def main():
    my_root = "./Dane"
    my_filename = "dane_close.csv"

    my_data = Data(my_root, my_filename)
    my_utils = Utils(my_root, my_filename)

    print(my_data.read_csv_from_root().head())
    print(my_utils.moving_average().head(200))
    print(my_utils.moving_average().columns)

    # substraction
    my_utils.substract_value_12_26()
    print(my_utils.substract_value_12_26().head(200))
    print(my_utils.substract_value_12_26().columns)

    # signal lane
    print(my_utils.signal_lane().columns)
    print(my_utils.signal_lane().head(200))

    # print last 200 rows of MACD and signal lane
    print(my_utils.MACD_signal_lane_combined().tail(300))

    # figure
    my_utils.figure_creator()

def buy_or_sell(date, hour, price, company) -> pd.DataFrame:
    pass

if __name__ == '__main__':
    main()