import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-5, 2), -3)
        self.assertEqual(self.calc.add(-5, -2), -7)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-5, 2), -7)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-4, -3), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-5, 2), -10)
        self.assertEqual(self.calc.multiply(5, 2), 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(4, -2), -2)
        self.assertEqual(self.calc.divide(4, 2), 2)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
        self.assertEqual(self.calc.modulo(10, 3), 1)
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
        

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()