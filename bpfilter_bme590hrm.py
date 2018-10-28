from scipy.signal import butter, lfilter


def butter_bandpass(lowcut, highcut, fs, order=5):
    """Create a butterworth bandpass filter

        Args:
            lowcut: low frequency cutoff
            highcut: high frequency cutoff
            fs: sampling frequency
            order: filter order (power)

        Returns:
            b, a: butterworth bandpass filter coefficients

    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(voltage, lowcut, highcut, fs, order=5):
    """Filter data with a bandpass, butterworth filter
	
	Args:
	    voltage: array of voltage data from an ECG signal
		lowcut: low frequency cutoff
		highcut: high frequency cutoff
		fs: sampling frequency
		order: filter order (power)
	
	Returns:
	    filtdat: array of filtered voltage data
	
	"""
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filtdat = lfilter(b, a, voltage)
    return filtdat
