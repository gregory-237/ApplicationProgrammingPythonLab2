import pandas as pd
from os import listdir
from os.path import isfile, join
from datetime import datetime

need_data = str(input())


def get_data_1(date):
    """Reading Dollar rates from dataset.csv"""
    df = pd.read_csv('dataset.csv', names=['Date', 'Dollar_Rate'])
    try:
        return df[df.Date == date].Dollar_Rate.item()
    except:
        return None


print(get_data_1(need_data))


def get_data_2(date):
    """Reading Dollar rates from Y.csv using X.csv"""
    df1 = pd.read_csv('X.csv', names=['Date'])
    try:
        idx = df1[df1.Date == date].Date.index[0]
        df2 = pd.read_csv('Y.csv', names=['Dollar_Rate'])
        return df2.at[idx, 'Dollar_Rate']
    except:
        return None


print(get_data_2(need_data))


def get_data_3(date):
    """Reading Dollar rates from folder script2"""
    path = ''
    folder = [f for f in listdir('script2') if isfile(join('script2', f))]
    try:
        for file in folder:
            if date[:4] == file[:4]:
                path = file
        df = pd.read_csv(f'script2/{path}', names=['Date', 'Dollar_Rate'])
        return df[df.Date == date].Dollar_Rate.item()
    except:
        return None


print(get_data_3(need_data))


def get_data_4(date):
    """Reading Dollar rates from folder script3"""
    date_dt = datetime(int(date[:4]), int(date[5:7]), int(date[8:10]))
    folder = [f for f in listdir('script3') if isfile(join('script3', f))]
    try:
        for file in folder:
            date_start, date_end = (datetime(int(file[:4]), int(file[4:6]), int(file[6:8])),
                                    datetime(int(file[9:13]), int(file[13:15]), int(file[15:17])))
            if date_start <= date_dt <= date_end:
                df = pd.read_csv(f'script3/{file}', names=['Date', 'Dollar_Rate'])
                return df[df.Date == date].Dollar_Rate.item()
    except:
        return None


print(get_data_4(need_data))





















