import unittest

import pandas as pd

from utilities.validate_nulls import check_nulls

class TestCheckNulls(unittest.TestCase):
    def setUp(self):
        self.df_ok = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        })
        self.df_with_nulls = pd.DataFrame({
            'id': [1, 2, 3, None, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        })

    def test_no_nulls_ok(self):
        result = check_nulls(self.df_ok, 'id')
        self.assertTrue(result)

    def test_with_nulls_ko(self):
        result = check_nulls(self.df_with_nulls, 'id')
        self.assertFalse(result)

    def test_nonexistent_column(self):
        result = check_nulls(self.df_ok, 'nonexistent_column')
        self.assertFalse(result)

    def test_invalid_field_name_type(self):
        result = check_nulls(self.df_ok, 123)  # Passing an integer instead of string
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
