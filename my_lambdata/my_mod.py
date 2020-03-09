# my_lambdata/my_mod.py

import pandas as pd
import numpy as np

def say_hello():
    """ says hello """
    print('Hello there!')


def add_column(data, dataframe, col_name):
    """
    takes a list (data) and adds it as a new column to dataframe

    param col_name = the name of the new column

    returns the modified dataframe

    note: 
    - if len(data) is less than len(dataframe), the remaining rows will be NaN
    - if len(data) is more than len(dataframe), the extra rows of data will be cut off
    """

    data = pd.Series(data)
    df = dataframe.copy()
    df[col_name] = data
    return df


def train_test_split(dataframe, test_ratio=.3):
    """
    Takes a dataframe and returns a random train/test split

    param test_ratio: the percentage of data to put into the test portion
        - must be between 0.0 and 1.0

    returns: train, test
    """

    # ensure test_ratio is [0,1]
    if (test_ratio > 1.0) | (test_ratio >= 0):
        raise ValueError('test_ratio must be between 0.0 and 1.0')

    # shuffle the dataframe to ensure a random split
    df = dataframe.copy()
    df = df.reindex(np.random.permutation(df.index))

    # return the split
    cutoff = int(len(df) * test_ratio)
    return df[:-cutoff], df[-cutoff:]


def train_val_test_split(dataframe, val_ratio=.2, test_ratio=.2):
    """
    Takes a dataframe and returns a random train/validate/test split

    param test_ratio: the percentage of data to put into the test portion
        - must be between 0.0 and 1.0
    
    param val_ratio: the percentage of data to put into the validation portion
        - must be between 0.0 and 1.0
    
    test_ratio + val_ratio must also be <= 1.0
        - if test_ratio + val_ratio == 1, train will be empty

    returns: train, validate, test
    """

    # ensure test_ratio is [0,1]
    if (test_ratio > 1.0) | (test_ratio < 0):
        raise ValueError('test_ratio must be between 0.0 and 1.0')

    # ensure val_ratio is [0,1]
    if (val_ratio > 1.0) | (val_ratio < 0):
        raise ValueError('test_ratio must be between 0.0 and 1.0')

    # ensure test + val <= 1
    if (test_ratio + val_ratio > 1.0):
        raise ValueError('test_ratio + val_ratio must be <= 1.0')

    # shuffle the dataframe to ensure a random split
    df = dataframe.copy()
    df = df.reindex(np.random.permutation(df.index))

    # return the split
    test_cutoff = int(len(df) * test_ratio) 
    val_cutoff = int(len(df) * val_ratio) + test_cutoff

    return df[:-val_cutoff], df[-val_cutoff:-test_cutoff], df[-test_cutoff:]
