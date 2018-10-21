from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(voltage, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filtdat = lfilter(b, a, voltage)
    return filtdat

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 1000.0
    lowcut = 0.5
    highcut = 150.0