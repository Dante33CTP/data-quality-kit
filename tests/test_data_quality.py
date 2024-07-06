import unittest
import pandas as pd
from utilities.data_quality import df_is_empty

class TestDfIsEmpty(unittest.TestCase):
    
    def test_empty_dataframe(self):
        df = pd.DataFrame()
        self.assertTrue(df_is_empty(df))
    
    def test_non_empty_dataframe(self):
        df = pd.DataFrame({'col1': [1, 2, 3]})
        self.assertFalse(df_is_empty(df))
    
    def test_non_empty_dataframe_with_index(self):
        df = pd.DataFrame({'col1': [1, 2, 3]}, index=[0, 1, 2])
        self.assertFalse(df_is_empty(df))

if __name__ == '__main__':
    unittest.main()
