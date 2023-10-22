import pandas as pd

class DataIterator:
    def __init__(self, csv_filename):
        self.data = pd.read_csv(csv_filename, parse_dates=['Date'], names=['Date', 'Dollar_Rate'])
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data = self.data.sort_values(by='Date')

    def next(self):
        while not self.data.empty:
            next_data = self.data.iloc[0]
            self.data = self.data.iloc[1:]
            return f"{next_data['Date'].date()}, {next_data['Dollar_Rate']}"
        return None

# Использование
iterator = DataIterator("dataset.csv")
while True:
    next_data = iterator.next()
    if next_data is None:
        break
    print(next_data)
