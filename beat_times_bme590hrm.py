import numpy as np
from numpy import diff
from readCSV_bme590hrm import time

def beat_times(loc,dif):
    tloc = np.where(dif < 3)
    tlocn = np.delete(tloc, 0, 0)
    locary = np.array(loc)
    loclist = locary.tolist()
    tmary = np.array(time)
    #btme = [time[x] for x in loclist]
    lints = [int(i) for i in loclist]
    for x in lints:
        btime = time[x]
    #for x in locary:
     #   btime = time[x]
    #rep = diff(tlocn)
    #oneary = np.array([1])
    #strt = np.insert(stpplus,0,oneary)
    #stp = np.where(dif > 3)
    #stp = np.delete(stp, 0, 0)
    #strt = stp + 1
    #strt = np.insert(strt,0,0)
    #nd = np.ma.count(loc)
    #stp = np.append(stp, nd-1)
    #loclist = list(loc)
    #for x in strt:
     #   for y in stp:
      #      splitloc = loc[x:y]
    
    print(time)
            # find where x<3 and average each group 
			# maybe make arays/lists for each beat
