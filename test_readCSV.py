from readCSV_bme590hrm import load_CSV
import pandas as pd
from pandas import read_csv


def test_read_CSV():
    s = load_CSV()
    df = s[3]
    numcols = len(df.columns)
    assert numcols == 2
    
