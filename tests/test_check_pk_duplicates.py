import unittest

import pandas as pd

from utilities.check_pk_duplicates import check_no_duplicates 

class TestCheckNoDuplicates(unittest.TestCase):
    
    def setUp(self):
        self.df_with_duplicates = pd.DataFrame({
            'id': [1, 2, 3, 3],
            'name': ['Alice', 'Bob', 'Charlie', 'Charlie'],
            'age': [25, 30, 35, 35]
        })
        
        self.df_no_duplicates = pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [25, 30, 35]
        })

    def test_duplicates_present(self):
        self.assertTrue(check_no_duplicates(self.df_with_duplicates, 'id'))

    def test_no_duplicates(self):
        self.assertFalse(check_no_duplicates(self.df_no_duplicates, 'id'))

    def test_invalid_column_name(self):
        with self.assertRaises(ValueError):
            check_no_duplicates(self.df_with_duplicates, 'non_existent_column')

if __name__ == '__main__':
    unittest.main()
