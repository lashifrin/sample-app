from typing import Union
import math
import operator
from unittest.mock import patch

from math_operations import add, subtract, multiply, divide, NEGATIVE_ZERO, DIVIDE_BY_ZERO

def test_add():
    """Test addition of two numbers."""
    assert add(3.14, 2) == pytest.approx(5.14)
    assert add(-2.71, 8.67) == pytest.approx(5.96)
    assert add(0.0, -1.0) == -1.0
    assert add(-0.0, 1.0) == 1.0

def test_add_edge_cases():
    """Test edge cases for addition."""
    with pytest.raises(TypeError):
        add("string", 42)
    with pytest.raises(TypeError):
        add(3, "other")

def test_subtract():
    """Test subtraction of one number from another."""
    assert subtract(5, 2) == 3
    assert subtract(-2.71, 8.67) == -11.38
    assert subtract(0.0, -1.0) == 1.0
    assert subtract(-0.0, 1.0) == -1.0

def test_subtract_edge_cases():
    """Test edge cases for subtraction."""
    with pytest.raises(TypeError):
        subtract("string", 42)
    with pytest.raises(TypeError):
        subtract(3, "other")

def test_multiply():
    """Test multiplication of two numbers."""
    assert multiply(3, 4) == 12
    assert multiply(-2.71, 8.67) == -23.5092
    assert multiply(0.0, -1.0) == 0.0
    assert multiply(-0.0, 1.0) == 0.0

def test_multiply_edge_cases():
    """Test edge cases for multiplication."""
    with pytest.raises(TypeError):
        multiply("string", 42)
    with pytest.raises(TypeError):
        multiply(3, "other")

def test_divide():
    """Test division of one number by another."""
    assert divide(6, 2) == 3.0
    assert divide(-8.175, 4.0) == -2.04375
    assert divide(1.0 / 3.0, 2.0) == 0.33333333333333337

def test_divide_edge_cases():
    """Test edge cases for division."""
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
    with pytest.raises(TypeError):
        divide("string", 42)
    with pytest.raises(TypeError):
        divide(3, "other")

def test_divide_negative_zero():
    """Test division by negative zero."""
    with pytest.raises(ValueError):
        divide(-6, -0.0)

def test_main():
    """Test main function."""
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_has_calls([
            call("Addition: 5.14"),
            call("Subtraction: 3"),
            call("Multiplication: 12"),
            call("Division: 3"),
            call(f"Division by zero error handling: {DIVIDE_BY_ZERO}"),
        ])