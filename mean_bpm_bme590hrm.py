def mean_bpm(num_beats,duration):
    """Find the average heart rate (in bpm) for a given ECG signal
	
	Args:
	    num_beats: number of detected heart beats in an ECG strip
		duration: the duration of the ECG signal (in seconds)
	
	Returns:
	    bpm: average heart rate in beats per minute
	
	"""
    inmin = input("Input number of minutes   ")
    print(type(inmin))
    if inmin.isalpha(): 
        raise TypeError("Input must be a number")
    inmin = float(inmin)
    sec = inmin * 60
    ratio = sec/duration
    nbeats = num_beats * ratio
    dur = duration * ratio
    bps = nbeats/dur
    mean_hr_bpm = bps*60
    #print(type(mean_hr_bpm))
    return mean_hr_bpm
