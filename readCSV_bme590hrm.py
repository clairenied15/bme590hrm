import csv
import pandas as pd
from pandas import read_csv

def load_CSV():
    """ Load in a csv file with time and voltage ECG data
	
	Args:
	    None
	
	Returns:
	    time: an array of the time data
		voltage: an array of the voltage data 
		
	"""
    filename = 'test_data1.csv'
    df = pd.read_csv(filename, delimiter = ',', header = None)
    tme = df.iloc[:,0]
    time = [float(i) for i in tme]
    volt = df.iloc[:,1]
    voltage = [float(i) for i in volt]
    return time, voltage
    #print(df)