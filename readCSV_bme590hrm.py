import csv
import pandas as pd
from pandas import read_csv

df = pd.read_csv('test_data1.csv', delimiter = ',', header = None)
tme = df.iloc[:,0]
time = [float(i) for i in tme]
volt = df.iloc[:,1]
voltage = [float(i) for i in volt]
data = voltage
#print(df)