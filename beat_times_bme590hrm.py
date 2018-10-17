import numpy as np
#from num_beats_bme590hrm import loc
#from num_beats_bme590hrm import dif
from num_beats_bme590hrm import num_beats

def main():
    beat_times()

def beat_times():
    #for x in np.nditer(dif):
     #   if x < 3:
    dat = np.load('num_beats_bme590hrm.npy')
    loc = dat['array1']
    dif = dat['array2']
    tloc = np.where(dif < 3)
    print(loc)
            # find where x<3 and average each group 
if __name__ == "__main__":
    main()