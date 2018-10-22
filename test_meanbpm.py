from mean_bpm_bme590hrm import mean_bpm

def test_mean_bpm():
    s = mean_bpm(5,5)
    assert s == 60
	