import csv
import pandas as pd
from pandas import read_csv

def load_CSV():
    filename = 'test_data1.csv'
    df = pd.read_csv(filename, delimiter = ',', header = None)
    tme = df.iloc[:,0]
    time = [float(i) for i in tme]
    volt = df.iloc[:,1]
    voltage = [float(i) for i in volt]
    return tme, time, volt, voltage
    #print(df)