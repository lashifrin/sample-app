# math_operations.py

import operator
from typing import Union

# Constants for error messages
NEGATIVE_ZERO = "Cannot perform operation on negative zero"
DIVIDE_BY_ZERO = "Division by zero is not allowed"

def add(a: float, b: Union[float, int]) -> float:
    """Add two numbers.

    Args:
        a (float): first number
        b (Union[float, int]): second number

    Returns:
        float: sum of the two numbers
    """
    return a + b

def subtract(a: float, b: Union[float, int]) -> float:
    """Subtract one number from another.

    Args:
        a (float): minuend
        b (Union[float, int]): subtrahend

    Returns:
        float: difference of the two numbers
    """
    return a - b

def multiply(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """Multiply two numbers.

    Args:
        a (Union[float, int]): first number
        b (Union[float, int]): second number

    Returns:
        Union[float, int]: product of the two numbers
    """
    return a * b

def divide(a: float, b: Union[float, int]) -> Union[float, int]:
    """Divide one number by another.

    Args:
        a (float): dividend
        b (Union[float, int]): divisor

    Returns:
        Union[float, int]: quotient of the two numbers
    """
    if b == 0:
        raise ValueError(DIVIDE_BY_ZERO)

    return a / b

def main():
    """Example usage of mathematical operations."""
    print("Addition:", add(3.14, 2))
    print("Subtraction:", subtract(5, 2))
    print("Multiplication:", multiply(3, 4))
    print("Division:", divide(6, 2))
    print("Division by zero error handling:", divide(6, 0))

if __name__ == "__main__":
    main()