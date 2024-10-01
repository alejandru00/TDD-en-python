
import math

class Calculator:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def factorial(self, numero):
        if numero < 0:
            raise ValueError("El factorial no está definido para números negativos")
        elif numero == 0:
            return 1
        fact = 1
        for i in range(1, numero + 1):
            fact *= i
        return fact
