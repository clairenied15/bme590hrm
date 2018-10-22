from volt_extremes_bme590hrm import volt_extremes
import numpy

def test_volt_extremes():
    s = volt_extremes(numpy.array([-3,3,7,1,10,-1,12,8,9]))
    assert s == (-3,12)