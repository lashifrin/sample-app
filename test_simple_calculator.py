import pytest
from simple_calculator import Calculator

def test_calculator_initialization():
    """
    Test initializing an instance of the Calculator class.
    """
    calc = Calculator()
    assert isinstance(calc, Calculator)

def test_add_basic():
    """
    Test adding two numbers with positive values.
    """
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_add_with_negative():
    """
    Test adding two negative numbers and a positive/negative number with another.
    """
    calc = Calculator()
    result1 = calc.add(-2, -3)
    assert result1 == -5
    result2 = calc.add(5, -3)
    assert result2 == 2

def test_add_with_float():
    """
    Test adding two float numbers.
    """
    calc = Calculator()
    result = calc.add(3.14, 2.71828)
    assert result == pytest.approx(5.862568)

def test_add_type_error():
    """
    Test raising ValueError when TypeError occurs in add method.
    """
    with pytest.raises(ValueError):
        calc = Calculator()
        calc.add("invalid", 3)

def test_multiply_basic():
    """
    Test multiplying two numbers with positive values.
    """
    calc = Calculator()
    result = calc.multiply(5, 3)
    assert result == 15

def test_multiply_with_zero():
    """
    Test multiplying two zero numbers and a number with another non-zero value.
    """
    calc = Calculator()
    result1 = calc.multiply(0, 3)
    assert result1 == 0
    result2 = calc.multiply(5, 0)
    assert result2 == 0
    result3 = calc.multiply(5, -3)
    assert result3 == -15

def test_multiply_with_float():
    """
    Test multiplying two float numbers.
    """
    calc = Calculator()
    result = calc.multiply(3.14, 2.71828)
    assert result == pytest.approx(8.60599938)

def test_multiply_type_error():
    """
    Test raising ValueError when TypeError occurs in multiply method.
    """
    with pytest.raises(ValueError):
        calc = Calculator()
        calc.multiply("invalid", 3)
```

To run these tests, make sure you have pytest installed and save this file as `test_simple_calculator.py`. Then execute the following command in your terminal or command prompt:

```bash
pytest test_simple_calculator.py