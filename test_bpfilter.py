import numpy as np
from bpfilter_bme590hrm import butter_bandpass_filter
from math import*


def test_filter():
    freq = 140.0
    t = np.arange(0, 5*pi, pi/20)
    voltage = np.sin(2*pi*freq*t)
    v_rms = np.sqrt(np.mean(voltage**2))
    # voltage = np.transpose(voltage)
    lowcut = 0.5
    highcut = 150.0
    fs = 1000.0
    s = butter_bandpass_filter(voltage, lowcut, highcut, fs, order=5)
    s_rms = np.sqrt(np.mean(s**2))
    perror = abs((s_rms-v_rms)/v_rms) * 100
    # print(voltage)
    # print(s)
    assert perror <= 10
