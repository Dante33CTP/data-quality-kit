import unittest

import pandas as pd

from utilities.validate_formats import check_type

class TestCheckType(unittest.TestCase):
    def setUp(self):
        # Crear un DataFrame de ejemplo para usar en las pruebas
        self.df = pd.DataFrame({
            'numeric_column': [1, 2, 3, 4, 5],
            'text_column': ['a', 'b', 'c', 'd', 'e'],
            'mixed_column': [1, 'b', 3, 'd', 5]
        })

    def test_numeric_column_ok(self):
        # Testea si todos los valores en 'numeric_column' son del tipo int
        result = check_type(self.df, 'numeric_column', int)
        self.assertTrue(result)

    def test_text_column_ok(self):
        # Testea si todos los valores en 'text_column' son del tipo str
        result = check_type(self.df, 'text_column', str)
        self.assertTrue(result)

    def test_mixed_column_ko(self):
        # Testea si algunos valores en 'mixed_column' no son del tipo int
        result = check_type(self.df, 'mixed_column', int)
        self.assertFalse(result)

    def test_nonexistent_column(self):
        # Testea si la función devuelve False cuando la columna no existe
        result = check_type(self.df, 'nonexistent_column', int)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
