import unittest

import pandas as pd

from tests.global_test_data import df_global

from utilities.check_pk_duplicates import check_no_duplicates

class TestDataQuality(unittest.TestCase):

    def test_no_duplicates(self):
        # Prueba si la función retorna False cuando no hay duplicados en la columna 'id'
        result = check_no_duplicates(df_global, 'id')
        self.assertFalse(result)

        # Prueba si la función retorna True cuando hay duplicados en la columna 'duplicated_ids'
        result_duplicated = check_no_duplicates(df_global, 'duplicated_ids')
        self.assertTrue(result_duplicated)

    def test_nonexistent_column(self):
        # Prueba si la función lanza un ValueError cuando la columna no existe
        with self.assertRaises(ValueError) as context:
            check_no_duplicates(df_global, 'nonexistent_column')
        self.assertEqual(str(context.exception), 'Error: The column "nonexistent_column" is not in the DataFrame.')

if __name__ == '__main__':
    unittest.main()

