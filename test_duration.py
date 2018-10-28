from duration_bme590hrm import duration_hrm


def test_duration():
    s = duration_hrm(list(range(0, 101)))
    assert s == 100
