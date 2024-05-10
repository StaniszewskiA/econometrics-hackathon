import pandas as pd

class Data:
    def __repr__(self) -> str:
        "Klasa do pracy na plikach .csv"

    def __init__(self, root, filename) -> None:
        self.root = root
        self.filename = filename

    def read_csv_from_root(self) -> None:
        file_root = self.root + "/" + self.filename
        df = pd.read_csv(file_root, sep=";")
        return df
    
    def data_period_calculator(self) -> None:
        df = self.read_csv_from_root()
        return df["data"].max() - df["data"].min() + 1
    
    def buy_or_sell(data: pd.DataFrame) -> pd.DataFrame:
        signal_columns = [col for col in data.columns if 'signal' in col]
        #macd_columns = [col for col in data.columns if 'macd' in col]
 
        macd: pd.Series = data["macd_lane"]
        signal: pd.Series = data["signal_lane"]
        already_bought = {company: False for company in signal_columns}

        columns = ["Spółka", "Sygnał"]

        result_df: pd.DataFrame = pd.DataFrame(columns=columns) 

        for company in signal_columns:
            for index, row in data.iterrows():
                if macd[company][index] == signal[company][index]:
                    if (macd[company][index - 1] < signal[company][index - 1]) and already_bought[company]:
                        result_df.at[index, "Sygnał"] = "Sprzedawaj"
                    elif macd[company][index - 1] > signal[company][index - 1]:
                        already_bought[company] = True
                        result_df.at[index, "Sygnał"] = "Kupuj"
                else:
                    result_df.at[index, "Sygnał"] = ""

            result_df.loc[result_df["Sygnał"].notnull(), "Spółka"] = company[:3]

        return result_df
                    
