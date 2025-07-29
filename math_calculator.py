from __future__ import annotations
from typing import Union, Optional

class MathCalculator:
    """A simple calculator class."""

    def __init__(self):
        """Initializes the MathCalculator instance."""

    def add(self, a: float, b: float) -> float:
        """Adds two numbers.

        Raises ValueError if either number is not a float.
        """
        if not isinstance(a, float) or not isinstance(b, float):
            raise ValueError("Both arguments must be of type float.")
        return a + b

    def subtract(self, a: float, b: float) -> Union[float, None]:
        """Subtracts b from a.

        Returns None if a is less than b.
        Raises ValueError if either number is not a float.
        """
        if not isinstance(a, float) or not isinstance(b, float):
            raise ValueError("Both arguments must be of type float.")
        if a < b:
            return None
        return a - b

    def multiply(self, a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
        """Multiplies two numbers.

        Raises TypeError if either number is not an integer or float.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be of type int or float.")
        return a * b

    def divide(self, a: Union[float, int], b: Union[float, int]) -> Union[float, None]:
        """Divides a by b.

        Returns None if b is zero.
        Raises TypeError if either number is not an integer or float.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be of type int or float.")
        if b == 0:
            return None
        return a / b