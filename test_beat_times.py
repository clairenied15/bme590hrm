from beat_times_bme590hrm import beat_times 
import numpy


def test_beat_times():
    s = beat_times(list(range(1,101)),
                   [[3,4,5,18,19,20,30,32,34,55,57,59,73,76,77,92,93,94]],
                   numpy.array([1,1,13,1,1,10,2,2,21,2,2,14,3,1,15,1,1]))
    assert s == [6,21,35,60,78,95]
