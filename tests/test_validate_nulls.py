import unittest

import pandas as pd

from utilities.validate_nulls import check_nulls

class TestCheckNulls(unittest.TestCase):
    
    def setUp(self):
        data = {
            'column1': [1, 2, 3],
            'column2': [None, 2, 3],
            'column3': ['a', 'b', 'c']
        }
        self.df = pd.DataFrame(data)

    def test_nulls_present(self):
        self.assertTrue(check_nulls(self.df, 'column2'))

    def test_no_nulls(self):
        self.assertFalse(check_nulls(self.df, 'column1'))
        self.assertFalse(check_nulls(self.df, 'column3'))

    def test_invalid_column_name(self):
        with self.assertRaises(ValueError):
            check_nulls(self.df, 'non_existent_column')

    def test_invalid_column_type(self):
        with self.assertRaises(TypeError):
            check_nulls(self.df, 123)

if __name__ == '__main__':
    unittest.main()
