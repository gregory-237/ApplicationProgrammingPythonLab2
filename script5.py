import pandas as pd


def next_data_generator(csv_filename):
    data = pd.read_csv(csv_filename, parse_dates=['Date'], names=['Date', 'Dollar_Rate'])
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values(by='Date')

    def next():
        nonlocal data
        while not data.empty:
            next_data = data.iloc[0]
            data = data.iloc[1:]
            return f"{next_data['Date'].date()}",f"{next_data['Dollar_Rate']}"
        return None

    return next


next_fn = next_data_generator("dataset.csv")
while True:
    next_data = next_fn()
    if next_data is None:
        break
    print(next_data)
