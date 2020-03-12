# test/alt_mod_test.py
# an alternative to unittests using pytest

import my_lambdata.my_mod as my_mod
import pandas as pd


# function names must begin with "test_" for pytest to recognize it
def test_add_column():
    df = pd.DataFrame({'A': range(10), 'B': range(10, 20)})
    new_col = range(0, 20, 2)
    df = my_mod.add_column(new_col, df, 'C')

    # check that we have a new column
    assert len(df.columns) == 3

    # check that the new column is what we expect
    assert df['C'].to_list() == list(new_col)
