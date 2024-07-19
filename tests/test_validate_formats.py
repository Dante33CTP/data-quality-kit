import unittest

import pandas as pd

from tests.global_test_data import df_global

from utilities.validate_formats import check_type_format

class TestCheckTypeFormat(unittest.TestCase):

    def test_valid_type(self):
        # Prueba si la función retorna True cuando todos los valores de 'column1' son de tipo int
        result_int = check_type_format(df_global, 'column1', int)
        self.assertTrue(result_int)

        # Prueba si la función retorna True cuando todos los valores de 'column3' son de tipo str
        result_str = check_type_format(df_global, 'column3', str)
        self.assertTrue(result_str)

    def test_invalid_type(self):
        # Prueba si la función retorna False cuando no todos los valores de 'column2' son de tipo int
        result_invalid = check_type_format(df_global, 'column2', int)
        self.assertFalse(result_invalid)

    def test_nonexistent_column(self):
        # Prueba si la función lanza un ValueError cuando la columna no existe
        with self.assertRaises(ValueError):
            check_type_format(df_global, 'nonexistent_column', int)


if __name__ == '__main__':
    unittest.main()
