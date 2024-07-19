import unittest

from tests.global_test_data import df_global

from utilities.validate_nulls import check_nulls

class TestCheckNulls(unittest.TestCase):
    
    def setUp(self):
        self.df_with_nulls = df_global.copy()
        self.df_no_nulls = df_global.dropna(subset=['column2'])

    def test_nulls_present(self):
        self.assertTrue(check_nulls(self.df_with_nulls, 'column2'))

    def test_no_nulls(self):
        self.assertFalse(check_nulls(self.df_no_nulls, 'column1'))
        self.assertFalse(check_nulls(self.df_no_nulls, 'column3'))

    def test_invalid_column_name(self):
        with self.assertRaises(ValueError):
            check_nulls(self.df_with_nulls, 'non_existent_column')

    def test_invalid_column_type(self):
        with self.assertRaises(TypeError):
            check_nulls(self.df_with_nulls, 123)

if __name__ == '__main__':
    unittest.main()
