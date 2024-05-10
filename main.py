import pandas as pd

from data import Data
from utils import Utils

def main():
    my_root = "./Dane"
    my_filename = "dane_close.csv"

    data = Data(my_root, my_filename)
    utils = Utils(my_root, my_filename)

    print(data.read_csv_from_root().head())
    print(utils.moving_average().head(200))
    print(utils.moving_average().columns)

    # substraction
    utils.substract_value_12_26()
    print(utils.substract_value_12_26().head(200))
    print(utils.substract_value_12_26().columns)

    # signal lane
    print(utils.signal_lane().columns)
    print(utils.signal_lane().head(200))

    # MCAD, signal lane
    print(utils.MACD_signal_lane_combined().columns)

def buy_or_sell(date, hour, price, company) -> pd.DataFrame:
    pass

if __name__ == '__main__':
    main()