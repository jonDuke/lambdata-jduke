# my_lambdata/my_script.py

import my_lambdata.my_mod as my_mod
import pandas as pd

df = pd.DataFrame({'A': range(10), 'B': range(10, 20)})

print("original dataframe:")
print(df.head(10))

print('\nadding a column:')
new_col = range(0, 20, 2)
df = my_mod.add_column(new_col, df, 'C')
print(df.head(10))

print('\nperforming a train/val/test split:')
train, val, test = my_mod.train_val_test_split(df)
print('train:', train.head())
print('val:', val.head())
print('test:', test.head())
