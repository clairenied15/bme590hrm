from bpfilter_bme590hrm import butter_bandpass
from bpfilter_bme590hrm import butter_bandpass_filter
from num_beats_bme590hrm import n_beats
from beat_times_bme590hrm import beat_times
from mean_bpm_bme590hrm import mean_bpm
from duration_bme590hrm import duration_hrm
from readCSV_bme590hrm import load_CSV
from volt_extremes_bme590hrm import volt_extremes

def main():
    time, voltage = load_CSV()
    fs = 1000.0
    lowcut = 0.5
    highcut = 150.0
    butter_bandpass(lowcut, highcut, fs, order=5)
    filtdat = butter_bandpass_filter(voltage, lowcut, highcut, fs, order=5)
    voltage_extremes = volt_extremes(filtdat)
    loc, dif, num_beats = n_beats(time,filtdat)
    beat_times(time, loc, dif)
    duration = duration_hrm(time)
    mean_bpm(num_beats, duration)
	
if __name__ == "__main__":
    main()