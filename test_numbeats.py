from num_beats_bme590hrm import n_beats
import numpy as np

def test_num_beats():
    #n = 5
    #arr = numpy.array([n-7, n-5, n-1, n+4, n+12, n+10, n+6, n+4, n+3, n+2])
    #s = n_beats(list(range(1,51)),numpy.tile(arr,n))
    s = n_beats(list(np.arange(0,5,0.1)), np.array([-0.5,-0.3,0,0.6,1.9,4,2.7,1.7,1.2,1,-0.5,-0.3,0,0.7,1.7,4,2.5,1.7,1.2,1,-0.7,-0.4,0,0.8,1.8,4,2.5,1.7,1.2,1,-0.5,-0.3,0,0.7,1.7,4,2.5,1.7,1.2,1,-0.5,-0.3,0,0.7,1.7,4,2.5,1.7,1.2,1]))
    assert s[2] == 5