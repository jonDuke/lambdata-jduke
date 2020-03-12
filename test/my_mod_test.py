# test/my_mod_test.py

import unittest
import my_lambdata.my_mod as my_mod
import pandas as pd


class TestModMethods(unittest.TestCase):

    def test_add_column(self):
        df = pd.DataFrame({'A': range(10), 'B': range(10, 20)})
        new_col = range(0, 20, 2)
        df = my_mod.add_column(new_col, df, 'C')

        # check that we have a new column
        self.assertEqual(len(df.columns), 3)

        # check that the new column is what we expect
        self.assertEqual(df['C'].to_list(), list(new_col))


if __name__ == '__main__':
    unittest.main()
