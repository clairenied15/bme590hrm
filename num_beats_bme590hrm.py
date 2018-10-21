import numpy as np
from numpy import diff
np.set_printoptions(threshold=np.inf)
import pandas as pd
import scipy.signal as signal


def n_beats(time, filtdat):
    """Find the number of beats in an ECG strip
	
	Args:
	    time: array of time values from an ECG signal
		filtdat: array of filtered voltage values from an ECG signal
	
	Returns:
	    loc: tuple with the locations where the ECG signal slope is above a threshold
		dif: tuple with the differences between the locations in "loc"
		num_beats: number of detected heart beats in the ECG strip
	
	"""
    count = 1
    dt = diff(time)
    #dv = diff(voltage)
    dv = diff(filtdat)
    dvdt = dv/dt
    pos = [x for x in dvdt if x > 0]
    avg = np.mean(pos)
    stdev = np.std(pos)
    threshold = avg + 2*stdev
    loc = np.where(dvdt > threshold)
    dif = diff(loc)	
    avdif = np.mean(dif)
    for x in np.nditer(dif):
        if x > avdif:
            count += 1
    num_beats = count
    #print(filtdat)
    return loc, dif, num_beats