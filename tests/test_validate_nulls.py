import unittest
from pandas import DataFrame
from utilities.validate_nulls import check_nulls


class TestCheckNulls(unittest.TestCase):

    def setUp(self):
        self.df = DataFrame({
            'column1': [1, 2, 3],
            'column2': [1, None, 3],
            'column3': ['a', 'b', 'c']
        })

    def test_no_nulls(self):
        result = check_nulls(self.df, 'column1')
        self.assertEqual(result, 'OK')

    def test_with_nulls(self):
        result = check_nulls(self.df, 'column2')
        self.assertEqual(result, 'KO')

    def test_invalid_column_name(self):
        with self.assertRaises(ValueError):
            check_nulls(self.df, 'non_existent_column')

    def test_invalid_column_type(self):
        with self.assertRaises(TypeError):
            check_nulls(self.df, 123)

if __name__ == '__main__':
    unittest.main()
