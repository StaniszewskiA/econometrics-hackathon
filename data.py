import pandas as pd

class Data:
    def __repr__(self) -> str:
        "Klasa do pracy na plikach .csv"

    def __init__(self, root) -> None:
        self.root = root

    def read_csv_from_root(self):
        pass