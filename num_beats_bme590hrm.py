from readCSV_bme590hrm import voltage
from readCSV_bme590hrm import volt
from readCSV_bme590hrm import time
import numpy as np
from numpy import diff
np.set_printoptions(threshold=np.inf)
import pandas as pd
import scipy.signal as signal


def num_beats():
    count = 1
    dt = diff(time)
    dv = diff(voltage)
    dvdt = dv/dt
    pos = [x for x in dvdt if x > 0]
    avg = np.mean(pos)
    stdev = np.std(pos)
    threshold = avg + 2*stdev
    loc = np.where(dvdt > threshold)
    dif = diff(loc)	
    for x in np.nditer(dif):
        if x > 3:
            count += 1
    num_beats = count
    #df = pd.Series(volt)
    #volt_corr = df.autocorr()
    
	#print(num_beats)
    #print(loc)
    #np.save('num_beats_bme590hrm.npy',array1=loc,array2=dif)
    
