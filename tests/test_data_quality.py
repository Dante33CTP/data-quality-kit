import unittest

import pandas as pd

from tests.global_test_data import df_global

from utilities.data_quality import df_is_empty

class TestValidateFormats(unittest.TestCase):
    
    def setUp(self):
        # Extender el DataFrame global según las necesidades del test
        self.df_empty = df_global.copy().iloc[0:0]  # DataFrame vacío
        self.df_full = df_global.copy()  # DataFrame lleno

    def test_df_is_empty(self):
        self.assertTrue(df_is_empty(self.df_empty))
        self.assertFalse(df_is_empty(self.df_full))

if __name__ == '__main__':
    unittest.main()

