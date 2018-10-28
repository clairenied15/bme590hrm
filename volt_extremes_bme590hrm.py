def volt_extremes(filtdat):
    """Find the maximum and minimum voltage values for
    the filtered ECG signal

        Args:
            filtdat: array of filtered voltage values from
	    imported ECG signal

        Returns:
            voltage_extremes: tuple containing minimum and
	    maximum lead voltages from ECG signal

    """
    max_volt = max(filtdat)
    min_volt = min(filtdat)
    voltage_extremes = (min_volt, max_volt)
    # print(max_volt)
    # print(min_volt)
    print(voltage_extremes)
    return voltage_extremes
