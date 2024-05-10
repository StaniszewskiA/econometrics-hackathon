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
    
    def buy_or_sell(data: pd.DataFrame, price_data: pd.DataFrame) -> pd.DataFrame:
        signal_columns = [col for col in data.columns if 'signal' in col]
        macd_columns = [col for col in data.columns if 'MACD' in col]
 
        companies = set()
        pairs_by_company = {}

        for signal_col in signal_columns:
            company = signal_col.split('_')[0]
            companies.add(company)
            if company not in pairs_by_company:
                pairs_by_company[company] = []

            for macd_col in macd_columns:
                if macd_col.startswith(company):
                    pairs_by_company[company].append((signal_col, macd_col))
        
        result_df = pd.DataFrame(index=data.index, columns=["Sygnał", "Spółka"])
        already_bought = {}

        for company, pairs in pairs_by_company.items():
            for signal_col, macd_col in pairs:
                signal_values = data[signal_col]
                macd_values = data[macd_col]
                for i in range(1, len(data)):
                    if signal_values.iloc[i] == macd_values.iloc[i]:

        return result_df
                    
