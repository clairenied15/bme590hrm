import json

def hrm_dictionary(beats, num_beats, duration, voltage_extremes, mean_hr_bpm, filename):
    metrics = {beats: "numpy array of times when a beat occurred",
                num_beats: "number of detected beats in the ECG strip",
                duration: "time duration of the ECG strip",
                voltage_extremes: "tuple containing minimum and maximum lead voltages",
                mean_hr_bpm: "estimated average heart rate"}
    #return metrics
    with open(filename.json, 'w') as fp:
    json.dump(metrics, fp)
