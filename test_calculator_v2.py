# calculator_v2_test.py
from unittest.mock import Mock
from typing import Union, Optional
import pytest
from calculator_v2 import Calculator, main

def test_calculator_add():
    """Test addition operation of the calculator."""
    calc = Calculator()
    assert calc.add(3, 5) == 8
    assert calc.add(-1, -1) == -2
    assert calc.add(0, 0) == 0

def test_calculator_subtract():
    """Test subtraction operation of the calculator."""
    calc = Calculator()
    assert calc.subtract(3, 5) is None
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(3, 2) == 1

def test_calculator_multiply():
    """Test multiplication operation of the calculator."""
    calc = Calculator()
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(-1, -1) == 1
    assert calc.multiply(0, 0) == 0
    assert calc.multiply(3, 0) == 0

def test_calculator_divide():
    """Test division operation of the calculator."""
    with pytest.raises(TypeError):
        Calculator().divide("a", 5)
    with pytest.raises(TypeError):
        Calculator().divide(3, "b")
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(3, 0)

    calc = Calculator()
    assert calc.divide(3, 2) == 1.5
    assert calc.divide(-3, -2) == 1.5
    assert calc.divide(-3, 2) == -1.5
    assert calc.divide(0, 2) is None