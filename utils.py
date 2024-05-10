import pandas as pd

from data import Data

class Utils(Data):
    def __init__(self, root, filename) -> None:
        Data.__init__(self, root, filename)

    def __repr__(self) -> str:
        return "Klasa do pracy na danych w plikach, głównie wykresy"

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
