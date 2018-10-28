import numpy as np
import pandas as pd
import scipy.signal as signal
from numpy import diff
np.set_printoptions(threshold=np.inf)


def n_beats(time, filtdat):
    """Find the number of beats in an ECG strip

        Args:
            time: list of time values from an ECG signal
            filtdat: array of filtered voltage values from an ECG signal

        Returns:
            loc: tuple with the locations where the ECG signal slope is
            above a threshold
            dif: tuple with the differences between the locations in "loc"
            num_beats: number of detected heart beats in the ECG strip

    """
    count = 1
    dt = diff(time)
    # dv = diff(voltage)
    dv = diff(filtdat)
    dvdt = dv/dt
    # print(dvdt)
    pos = [x for x in dvdt if x > 0]
    # print(pos)
    avg = np.mean(pos)
    stdev = np.std(pos)
    threshold = avg + stdev
    # print(threshold)
    loc = np.where(dvdt > threshold)
    dif = diff(loc)
    avdif = np.mean(dif)
    # print(avdif)
    # print(dif)
    for x in np.nditer(dif):
        if x >= avdif:
            count += 1
    num_beats = count
    print(num_beats)
    # print(type(filtdat))
    return loc, dif, num_beats
