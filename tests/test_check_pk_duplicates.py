import unittest

import pandas as pd

from utilities.check_pk_duplicates import check_no_duplicates 


class TestCheckNoDuplicates(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame to use in the tests
        self.df_ok = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        })
        self.df_duplicated = pd.DataFrame({
            'id': [1, 2, 2, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        })

    def test_no_duplicates_ok(self):
        # Test if there are no duplicate values in the 'id' column
        result = check_no_duplicates(self.df_ok, 'id')
        self.assertEqual(result, 'OK: No duplicate values in the primary key column')

    def test_duplicates_ko(self):
        # Test if the function raises a ValueError when there are duplicate values in the 'id' column
        with self.assertRaises(ValueError) as context:
            check_no_duplicates(self.df_duplicated, 'id')
        self.assertEqual(str(context.exception), 'KO: Duplicate values found in the primary key column "id"')

    def test_nonexistent_column(self):
        # Test if the function raises a ValueError when the column does not exist
        with self.assertRaises(ValueError) as context:
            check_no_duplicates(self.df_ok, 'nonexistent_column')
        self.assertEqual(str(context.exception), 'Error: The primary key column "nonexistent_column" is not in the DataFrame')

if __name__ == '__main__':
    unittest.main()
