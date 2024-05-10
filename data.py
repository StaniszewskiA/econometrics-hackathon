import pandas as pd

class Data:
    def __repr__(self) -> str:
        "Klasa do pracy na plikach .csv"

    def __init__(self, root, filename) -> None:
        self.root = root
        self.filename = filename

    def read_csv_from_root(self) -> None:
        file_root = self.root + "/" + self.filename
        df = pd.read_csv(file_root)
        return df