import unittest
import pandas as pd
from utilities.validate_formats import check_type


class TestCheckType(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame to use in the tests
        self.df = pd.DataFrame({
            'numeric_column': [1, 2, 3, 4, 5],
            'text_column': ['a', 'b', 'c', 'd', 'e'],
            'mixed_column': [1, 'b', 3, 'd', 5]
        })

    def test_numeric_column_ok(self):
        # Test if all values in the 'numeric_column' are of type int
        result = check_type(self.df, 'numeric_column', int)
        self.assertEqual(result, 'OK: All records are of the specified type')

    def test_text_column_ok(self):
        # Test if all values in the 'text_column' are of type str
        result = check_type(self.df, 'text_column', str)
        self.assertEqual(result, 'OK: All records are of the specified type')

    def test_mixed_column_ko(self):
        # Test if the function raises a ValueError when there are different data types in the column
        with self.assertRaises(ValueError) as context:
            check_type(self.df, 'mixed_column', int)
        self.assertEqual(str(context.exception), 'KO: At least one record is not of the specified type')

    def test_nonexistent_column(self):
        # Test if the function raises a ValueError when the column does not exist
        with self.assertRaises(ValueError) as context:
            check_type(self.df, 'nonexistent_column', int)
        self.assertEqual(str(context.exception), 'Error: The column nonexistent_column is not in the DataFrame')

if __name__ == '__main__':
    unittest.main()
