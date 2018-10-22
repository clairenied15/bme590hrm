def duration_hrm(time):
    """Find the duration of an ECG strip by subtracting the initial time from the final time
	
	Args:
	    time: list of time values read from a CSV file
	
	Returns:
	    duration: the duration of the imported ECG signal (in seconds)
	
	"""
    duration = time[-1] - time[0]
    #print(time[-1])
    #print(time[0])
    print(duration)
    return duration

