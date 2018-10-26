from bpfilter_bme590hrm import butter_bandpass_filter
from math import*
import numpy as np

def test_filter():
    freq = 20.0
    #x1 = 0
    #x2 = 10
    #tm = [x*0.2 for x in range(2*x1, 2*x2+1)]
    #t = [float(i) for i in tm]
    t = np.arange(0,5*pi,pi/20)
    voltage = np.sin(2*pi*freq*t)
    v_rms = np.sqrt(np.mean(voltage**2))
    #voltage = np.transpose(voltage)
    lowcut = 0.5
    highcut = 150.0
    fs = 1000.0
    s = butter_bandpass_filter(voltage, lowcut, highcut, fs, order=5)
    s_rms = np.sqrt(np.mean(s**2))
    perror = abs((s_rms-v_rms)/v_rms) * 100
    print(voltage)
    print(s)
    assert perror <= 10