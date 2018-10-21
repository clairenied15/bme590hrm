import numpy as np
from numpy import diff

def beat_times(time,loc,dif):
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
    thresh = avdif + stdvdif
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
    # find where above the threshold and look at the location before that because peak of beat should be the last 
    print(beats)
            # find where x<3 and average each group 
			# maybe make arays/lists for each beat