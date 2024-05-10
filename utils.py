import pandas as pd
from data import Data

class Utils(Data):
    def __init__(self, root, filename) -> None:
        Data.__init__(self, root, filename)

    def __repr__(self) -> str:
        "Klasa do pracy na danych w plikach, głównie wykresy"

    def create_plot(data: pd.DataFrame, col: str) -> None:
        data[col].plot()

    def moving_average(self):
        df = self.read_csv_from_root()
        df2 = df.copy()

        window_size_1 = 12
        window_size_2 = 26

        for column in df.columns:
            ma1 = df[column].rolling(window=window_size_1).mean()
            ma2 = df2[column].rolling(window=window_size_2).mean()
            
            new_column_name_1 = f"{column}_average_{window_size_1}"
            new_column_name_2 = f"{column}_average_{window_size_2}"
            df[new_column_name_1] = ma1
            df2[new_column_name_2] = ma2

        # Usuń pierwsze 62 kolumny z df2
        df2 = df2.iloc[:, 62:]

        # Połącz oba DataFrame'y
        merged_df = pd.concat([df, df2], axis=1)

        return merged_df
    
    def substract_value_12_26(self):
        df = self.moving_average()
        
        for col in df.columns:
            if col.endswith("_average_12"):
                col_12 = col[:len(col) - 11]
                new_col_name = f"{col_12}_substract"
                df[new_col_name] = df[col] - df[f"{col_12}_average_26"]

        return df
    
    def signal_lane(self):
        n = len(self.substract_value_12_26())
        k = 2 / (n + 1)

        df = self.substract_value_12_26()
        new_df = df.iloc[:, :62]

        # calculate EMAs for every column in new_df
        for col in new_df.columns:
            new_column_name = f"{col}_ema"
            new_df[new_column_name] = new_df[col].ewm(span=n, adjust=False).mean()

        # save only ema columns
        new_df = new_df.filter(like="_ema")

        # merge new_df with df
        df = pd.concat([df, new_df], axis=1)

        return df
