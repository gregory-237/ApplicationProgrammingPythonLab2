import pandas as pd

df = pd.read_csv('dataset.csv', parse_dates=['Date'], names=['Date', 'Dollar_Rate'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')
years_data = []
for name, group in df.set_index('Date').groupby(pd.Grouper(freq='Y')):
    years_data.append(group.apply(lambda x: [str(x.name)[:10], str(x['Dollar_Rate'])], axis=1).values.tolist())


def split_by_years(years_data_list) -> None:
    """Splitting file by years"""
    for year in years_data_list:
        with open(f'script2/{year[0][0].replace("-", "")}_{year[-1][0].replace("-", "")}.csv', 'w') as f:
            for day in year:
                f.write(f'{day[0]},{day[1]}\n')


if __name__ == "__main__":
    split_by_years(years_data)
