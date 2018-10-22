import json

def hrm_dictionary(beats, num_beats, duration, voltage_extremes, mean_hr_bpm, filename):
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
