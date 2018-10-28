import json
import numpy as np
from dictionary_bme590hrm import hrm_dictionary


def test_json():
    s = hrm_dictionary([1, 2.1, 3.2, 4.4, 5.3], 5, 5.76,
                       (-0.54, 4.68), 52.083, "testdat.csv")
    expected_data = {
        "beats (numpy array of times when a beat occurred)":
                [1, 2.1, 3.2, 4.4, 5.3],
        "num_beats (number of detected beats in the ECG strip)": 5,
        "duration (time duration of the ECG strip)": 5.76,
        "voltage_extremes (tuple when minimum and maximum lead voltages)":
                           [-0.54, 4.68],
        "mean_hr_bpm (estimated average heart rate)": 52.083
        }
    with open(s) as f:
        data = json.load(f)
    assert data == expected_data
