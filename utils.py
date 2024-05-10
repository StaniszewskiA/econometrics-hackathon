from data import Data

class Utils(Data):
    def __init__(self, root, filename) -> None:
        Data.__init__(self, root, filename)

    def __repr__(self) -> str:
        "Klasa do pracy na danych w plikach, głównie wykresy"

    def create_plot():
        pass

    def moving_average(self):
        df = self.read_csv_from_root()

        window_size = 3
        for column in df.columns:
            ma = df[column].rolling(window=window_size).mean()
            
            new_column_name = f"{column}_average"
            df[new_column_name] = ma

        return df