import pandas as pd
import numpy as np


def split_to_x_and_y(limit):
    """Splitting file to X.csv and Y.csv files"""
    for i in range(limit):
        f_dates.write(f'{dates[i]}\n')
        f_courses.write(f'{courses[i]}\n')
    f_dates.close()
    f_courses.close()


f = pd.read_csv("dataset.csv", sep=',', header=None)
f_dates = open('X.csv', 'w')
f_courses = open('Y.csv', 'w')
dates = np.asarray(f[0])
courses = np.asarray(f[1])


if __name__ == "__main__":
    split_to_x_and_y(len(dates))
