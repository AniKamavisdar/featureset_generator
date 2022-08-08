import pandas as pd


class IDF:

    def __init__(self):
        self.data = pd.DataFrame()
        self.schema = None

    def store_idf(self, data):
        self.data = pd.DataFrame(data)
        self.schema = self.data.columns

    def get_data(self):
        return self.data

    def get_schema(self):
        return self.schema
