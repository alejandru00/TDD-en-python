
import unittest
from src.calculadora import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        self.calculadora = ScientificCalculator()

    def test_myfactorial(self):
        self.assertEqual(self.calculadora.factorial(3), 6)      # Para comprobar que el resultado de la función factorial es correcto

    def test_factorial_zero(self):
        self.assertEqual(self.calculadora.factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):     # Para comprobar que se lanza una excepción
            self.calculadora.factorial(-1)
