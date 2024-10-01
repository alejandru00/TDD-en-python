
import unittest
from src.calculadora import Calculator

class Test_Calculator(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculator()

    def test_factorial(self):
        self.assertEqual(self.calculadora.factorial(3), 6)      # Para comprobar que el resultado de la función factorial es correcto

    def test_factorial_cero(self):
        self.assertEqual(self.calculadora.factorial(0), 1)

    def test_factorial_negativos(self):
        with self.assertRaises(ValueError):     # Para comprobar que se lanza una excepción
            self.calculadora.factorial(-1)
