import csv
import pandas as pd
from pandas import read_csv


def load_CSV():
    """ Load in a csv file with time and voltage ECG data

        Args:
            None

        Returns:
            time: a list of the time data
            voltage: a list of the voltage data 

    """
    filename = 'test_data1.csv'
    df = pd.read_csv(filename, delimiter = ',', header = None)
    l = len(df.columns)
    tme = df.iloc[:, 0]
    time = [float(i) for i in tme]
    volt = df.iloc[:, 1]
    voltage = [float(i) for i in volt]
    # print(type(voltage))
    return time, voltage, filename, df
