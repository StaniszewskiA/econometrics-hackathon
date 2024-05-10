import pandas as pd
from data import Data

class Utils(Data):
    def __init__(self, root, filename) -> None:
        Data.__init__(self, root, filename)

    def __repr__(self) -> str:
        "Klasa do pracy na danych w plikach, głównie wykresy"

    def create_plot(self, data: pd.DataFrame, col: str) -> None:
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
    
    def substract_value_12_26(self) -> pd.DataFrame: # MACD lane
        df = self.moving_average()
        
        for col in df.columns:
            if col.endswith("_average_12"):
                col_12 = col[:len(col) - 11]
                new_col_name = f"{col_12}_substract"
                df[new_col_name] = df[col] - df[f"{col_12}_average_26"]

        return df
    
    def signal_lane(self) -> pd.DataFrame:
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
    
    def cumulated_rate_of_return(transactions: pd.DataFrame) -> float:
        sum: float = 1.0

        for index, row in transactions.iterrows():
            p_k = row["Kupno"]
            p_s = row["Sprzedaż"]
            sum *= (1 + Utils.rate_of_return(p_k, p_s))

        return sum - 1

    @staticmethod
    def rate_of_return(p_k: float, p_s: float) -> float:
        return (p_s - p_k) / p_k
    
    def MACD_signal_lane_combined(self) -> pd.DataFrame:
        df_ema = self.signal_lane()
        df_ema = df_ema.filter(like="_ema")

        # change ema columns names to signal_lane
        df_ema.columns = [col.replace("_ema", "_signal_lane") for col in df_ema.columns]

        df_substract = self.substract_value_12_26()
        df_substract = df_substract.filter(like="_substract")

        # change substract columns names to MACD_lane
        df_substract.columns = [col.replace("_substract", "_MACD_lane") for col in df_substract.columns]

        df_merged = pd.concat([df_ema, df_substract], axis=1)

        # cleaning, delete columns with data and czas
        df_merged = df_merged.drop(columns=["data_signal_lane", "czas_signal_lane", "data_MACD_lane", "czas_MACD_lane"])

        # addint columns with data i czas from original df, move them to the beginning
        df = self.read_csv_from_root()
        df = df[["data", "czas"]]
        df_merged = pd.concat([df, df_merged], axis=1)

        return df_merged
