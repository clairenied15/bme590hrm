from readCSV_bme590hrm import voltage

def volt_extremes(filtdat):
    max_volt = max(filtdat)
    min_volt = min(filtdat)
    voltage_extremes = (min_volt, max_volt)
    #print(max_volt)
    #print(min_volt)
    print(voltage_extremes)
    return voltage_extremes