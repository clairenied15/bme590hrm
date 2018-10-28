from bpfilter_bme590hrm import butter_bandpass
from bpfilter_bme590hrm import butter_bandpass_filter
from num_beats_bme590hrm import n_beats
from beat_times_bme590hrm import beat_times
from mean_bpm_bme590hrm import mean_bpm
from duration_bme590hrm import duration_hrm
from readCSV_bme590hrm import load_CSV
from new_readCSV_bme590hrm import new_load_CSV
from volt_extremes_bme590hrm import volt_extremes
from dictionary_bme590hrm import hrm_dictionary


def main():
    """Run all of the functions to find the mean heart rate,
    voltage extremes, duration, number of beats, and beat times
    for an imported ECG signal

    """
    try:
        time, voltage, filename, df = load_CSV()
    except FileNotFoundError:
        filename = input("Input filename  ")
        time, voltage, df = new_load_CSV(filename)
    fs = 1000.0
    lowcut = 0.5
    highcut = 150.0
    butter_bandpass(lowcut, highcut, fs, order=5)
    filtdat = butter_bandpass_filter(voltage, lowcut, highcut, fs, order=5)
    voltage_extremes = volt_extremes(filtdat)
    loc, dif, num_beats = n_beats(time, filtdat)
    beats = beat_times(time, loc, dif)
    duration = duration_hrm(time)
    try:
        mean_hr_bpm = mean_bpm(inmin=None, num_beats, duration)
    except TypeError:
        mean_hr_bpm = mean_bpm(inmin=None, num_beats, duration)
    hrm_dictionary(beats, num_beats, duration, voltage_extremes,
                   mean_hr_bpm, filename)

if __name__ == "__main__":
    main()
