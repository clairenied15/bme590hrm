import numpy as np
from numpy import diff


def beat_times(time, loc, dif):
    """Find all of the corresponding times when a heartbeat
        occurred for a given ECG signal

        Args:
            time: list of time values for an ECG signal
            loc: tuple with the locations where the ECG
                signal slope is above a threshold
            dif: tuple with the differences between the locations in "loc"

        Returns:
            beats: numpy array of times when a heartbeat occurred

        """
    locary = np.array(loc)
    loclist = locary.tolist()
    tmary = np.array(time)
    flat_list = []
    for sublist in loclist:
        for item in sublist:
            flat_list.append(item)
    btime = []
    for x in flat_list:
        btime.append(time[x])
    tdif = diff(btime)
    avdif = np.mean(tdif)
    stdvdif = np.std(tdif)
    thresh = avdif
    tloc = np.where(tdif > thresh)
    tloc = np.array(tloc)
    # add the last beat time to the array
    flat_tloc = []
    for sublist in tloc:
        for item in sublist:
            flat_tloc.append(item)
    last = np.ma.count(btime) - 1
    flat_tloc.append(last)
    beats = []
    for x in flat_tloc:
        beats.append(btime[x])
    # print(beats)
    # print(type(time))
    # print(type(loc))
    # print(type(dif))
    return beats
