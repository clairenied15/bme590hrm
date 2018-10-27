# bme590hrm
The heart rate monitor is made up of multiple py files:

readCSV_bme590hrm.py (reads time and voltage data from a CSV file),
bpfilter_bme590hrm.py (filters voltage data using a butterworth bandpass filter),
duration_bme590hrm.py (finds the duration of the ECG strip),
volt_extremes_bme590hrm.py (finds the maximum and minimum voltages in the ECG strip),
beat_times_bme590hrm.py (finds the time when each beat occurred),
mean_bpm_bme590hrm.py (finds the mean heart rate in bpm),
num_beats_bme590hrm.py (counts the total number of beats in the ECG strip),
dictionary_bme590hrm.py (makes a dictionary with the number of beats, beat times, duration, voltage extremes, and mean heart rate outputted from the other functions and outputs it as a JSON file)

These files can all be run together using the main_bme590hrm.py file. Running this main py file will go through and run all of the function files at one time and create a dictionary with the outputs. 

The unit test for the bandpass filter (test_bpfilter.py) is not working as the RMS of the inputted voltage isn't always close to the RMS for the outputted filtered voltage. There may be a problem with the filter. 
