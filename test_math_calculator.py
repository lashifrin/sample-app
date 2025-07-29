import unittest
from math_calculator import MathCalculator

class TestMathCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = MathCalculator()
    
    def test_add_valid_floats(self):
        """Test adding two valid floats."""
        result = self.calc.add(2.0, 3.0)
        self.assertEqual(result, 5.0)
    
    def test_add_invalid_input(self):
        """Test adding with invalid input."""
        with self.assertRaises(ValueError):
            self.calc.add("string", 3.0)
    
    def test_divide_valid(self):
        """Test dividing valid numbers."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero(self):
        """Test division by zero returns None."""
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()