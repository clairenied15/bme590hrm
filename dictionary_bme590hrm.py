import json

def hrm_dictionary(beats, num_beats, duration, voltage_extremes, mean_hr_bpm, filename):
    """Create a dictionary with the different values found for the ECG signal
	
	Args:
	    beats: list of times when a heart beat occurred
		num_beats: total number of detected heart beats in the ECG strip
		duration: time duration of the ECG strip 
		voltage_extremes: tuple with the maximum and minimum lead voltage values
		mean_hr_bpm: mean heart rate in beats per minute
		filename: name of the CSV file the ECG data is being read from
	
	Returns:
	    jname: json file with the dictionary for the ECG values in it
	
	"""
    metrics = {
        "beats (numpy array of times when a beat occurred)": beats,
        "num_beats (number of detected beats in the ECG strip)": num_beats,
        "duration (time duration of the ECG strip)": duration,
        "voltage_extremes (tuple containing minimum and maximum lead voltages)": voltage_extremes,
        "mean_hr_bpm (estimated average heart rate)": mean_hr_bpm
	}
    #return metrics
    jname = filename + ".json"
    print(jname)
    with open(jname, 'w') as fp:
        json.dump(metrics, fp)
	return jname
