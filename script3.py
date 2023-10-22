import pandas as pd

df = pd.read_csv('dataset.csv', parse_dates=['Date'], names=['Date', 'Dollar_Rate'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')
weekly_data = []
for name, group in df.set_index('Date').groupby(pd.Grouper(freq='W')):
    weekly_data.append(group.apply(lambda x: [str(x.name)[:10], str(x['Dollar_Rate'])], axis=1).values.tolist())


def split_by_weeks(weeks_data) -> None:
    """Splitting file by weeks"""
    for week in weeks_data:
        if week:
            with open(f'script3/{week[0][0].replace("-", "")}_{week[-1][0].replace("-", "")}.csv', 'w') as f:
                for day in week:
                    f.write(f'{day[0]},{day[1]}\n')


if __name__ == "__main__":
    split_by_weeks(weekly_data)
