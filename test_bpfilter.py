from bpfilter_bme590hrm import butter_bandpass_filter
from math import*
import numpy as np

def test_filter():
    freq = 20
    #x1 = 0
    #x2 = 10
    #tm = [x*0.2 for x in range(2*x1, 2*x2+1)]
    #t = [float(i) for i in tm]
    t = np.arange(0,5*pi,pi/4)
    voltage = np.sin(2*pi*freq*t)
    #voltage = np.transpose(voltage)
    lowcut = 0.5
    highcut = 150
    fs = 500
    s = butter_bandpass_filter(voltage, lowcut, highcut, fs, order=5)
    print(s)
    assert np.absolute(s.all()) == 1