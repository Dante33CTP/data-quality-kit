import unittest

import pandas as pd

from utilities.check_pk_duplicates import check_no_duplicates  # Asegúrate de reemplazar 'utilities.data_quality' con la ruta correcta a tu módulo

class TestCheckNoDuplicates(unittest.TestCase):
    def setUp(self):
        # Crear un DataFrame de ejemplo para usar en las pruebas
        self.df_ok = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        })
        self.df_duplicated = pd.DataFrame({
            'id': [1, 2, 2, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        })

    def test_no_duplicates_ok(self):
        # Prueba si no hay valores duplicados en la columna 'id'
        result = check_no_duplicates(self.df_ok, 'id')
        self.assertTrue(result)

    def test_duplicates_ko(self):
        # Prueba si la función devuelve False cuando hay valores duplicados en la columna 'id'
        result = check_no_duplicates(self.df_duplicated, 'id')
        self.assertFalse(result)

    def test_nonexistent_column(self):
        # Prueba si la función devuelve False cuando la columna no existe
        result = check_no_duplicates(self.df_ok, 'nonexistent_column')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
    