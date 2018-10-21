import numpy as np
from numpy import diff
np.set_printoptions(threshold=np.inf)
import pandas as pd
import scipy.signal as signal


def n_beats(time, filtdat):
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