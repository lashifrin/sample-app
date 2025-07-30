from __future__ import annotations
from typing import Union, Optional
from math import sqrt
from functools import reduce

class AdvancedCalculator:
    """Advanced Calculator class for performing advanced mathematical operations.

    Attributes:
        _num1 (float): First number in the operation.
        _num2 (float, optional): Second number in the operation. Defaults to None.

    Raises:
        ValueError: If an operation involves division by zero or negative base for factorial.
        TypeError: If an operation involves complex numbers.
    """

    def __init__(self, num1: Union[float, complex]):
        self._num1 = num1
        self._num2 = None

    def add(self, num2: Union[float, complex]) -> float:
        """Adds the provided number to the current number."""
        if isinstance(num2, complex):
            raise TypeError("Complex numbers are not supported for addition.")
        return self._num1 + num2

    def subtract(self, num2: Union[float, complex]) -> float:
        """Subtracts the provided number from the current number."""
        if isinstance(num2, complex):
            raise TypeError("Complex numbers are not supported for subtraction.")
        return self._num1 - num2

    def multiply(self, num2: Union[float, complex]) -> float:
        """Multiplies the provided number with the current number."""
        if isinstance(num2, complex):
            raise TypeError("Complex numbers are not supported for multiplication.")
        return self._num1 * num2

    def divide(self, num2: Union[float, complex]) -> float:
        """Divides the current number by the provided number."""
        if num2 == 0.0:
            raise ValueError("Division by zero is not allowed.")
        if isinstance(num2, complex):
            raise TypeError("Complex numbers are not supported for division.")
        return self._num1 / num2

    def square_root(self) -> Optional[float]:
        """Calculates the square root of the current number."""
        if self._num1 < 0.0:
            raise ValueError("Negative numbers do not have real square roots.")
        return sqrt(self._num1)

    def power(self, exponent: int) -> float:
        """Raises the current number to the provided power."""
        if exponent <= 0:
            raise ValueError("Exponent must be a positive integer.")
        return self._num1 ** exponent

    def factorial(self) -> int:
        """Calculates the factorial of the current number."""
        if not isinstance(self._num1, int):
            raise TypeError("Factorial can only be calculated for integers.")
        if self._num1 < 0:
            raise ValueError("Negative numbers do not have factorials.")
        return reduce((lambda a, b: a * b), range(1, self._num1 + 1))

    def fibonacci(self, n: int) -> int:
        """Calculates the Fibonacci series up to the provided number.

        Args:
            n (int): The position of the desired Fibonacci number in the series.

        Raises:
            ValueError: If the provided number is less than 1.
        """
        if n <= 0:
            raise ValueError("The provided number must be greater than zero.")
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 2):
                a, b = b, a + b
            return b