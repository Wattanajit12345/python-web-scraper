import pandas as pd


class TableStatics:

    def __init__(self, data: list):
        self.data = data
        self.df = pd.DataFrame()

    def create_table(self) -> pd.DataFrame:
        # self.df ####
        # |      P - tag     | Count words "Thailand: |
        # | ---------------- | ---------------------- |
        # | Thailand,[b] ... |          1             |
        return self.df

    def save_to_excel(self, path_name: str):
        self.df.to_excel(path_name)
