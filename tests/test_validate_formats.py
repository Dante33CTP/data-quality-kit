import unittest

import pandas as pd

from utilities.validate_formats import check_type

class TestCheckType(unittest.TestCase):
    
    def setUp(self):
        # Crear un DataFrame de ejemplo directamente
        self.df = pd.DataFrame({
            'id': [1, 2, None, 4],
            'name': ['Alice', 'Bob', 'Charlie', None],
            'age': [25, 30, 35, 40]
        })

    def test_correct_type_int(self):
        # Verifica que todos los valores no nulos en 'age' sean del tipo int
        self.assertTrue(check_type(self.df, 'age', int))

    def test_correct_type_str(self):
        # Verifica que todos los valores no nulos en 'name' sean del tipo str
        self.assertTrue(check_type(self.df, 'name', str))

    def test_invalid_type(self):
        # Verifica que no todos los valores no nulos en 'id' sean del tipo bool
        self.assertFalse(check_type(self.df, 'id', bool))

    def test_invalid_column_name(self):
        # Verifica que se lance ValueError si el nombre de la columna no existe
        with self.assertRaises(ValueError):
            check_type(self.df, 'non_existent_column', int)

if __name__ == '__main__':
    unittest.main()
