import pandas as pd

from data import Data
from utils import Utils

def main():
    my_root = "./Dane"
    my_filename = "dane_close.csv"

    data = Data(my_root, my_filename)
    utils = Utils(my_root, my_filename)

    print(data.read_csv_from_root().head())
    print(utils.moving_average().head())
    print(data.data_period_calculator())

def buy_or_sell(date, hour, price, company) -> pd.DataFrame:
    pass

if __name__ == '__main__':
    main()