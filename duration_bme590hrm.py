from readCSV_bme590hrm import time

def duration_hrm():
    duration = time[-1] - time[0]
    #print(time[-1])
    #print(time[0])
    print(duration)
    return duration

