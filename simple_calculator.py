# Simple Calculator
# Provides add and multiply functions for basic arithmetic operations

import typing as ty

class Calculator:
    """
    A simple calculator class to perform addition and multiplication.
    """

    def __init__(self):
        pass

    def add(self, a: ty.Union[int, float], b: ty.Union[int, float]) -> ty.Union[int, float]:
        """
        Add two numbers and return the result.

        :param a: The first number.
        :param b: The second number.
        :return: The sum of the provided numbers.
        """
        try:
            return a + b
        except TypeError as e:
            raise ValueError("Both arguments must be numeric.") from e

    def multiply(self, a: ty.Union[int, float], b: ty.Union[int, float]) -> ty.Union[int, float]:
        """
        Multiply two numbers and return the product.

        :param a: The first number.
        :param b: The second number.
        :return: The product of the provided numbers.
        """
        if a == 0 or b == 0:
            raise ValueError("At least one argument must not be zero.")

        try:
            return a * b
        except TypeError as e:
            raise ValueError("Both arguments must be numeric.") from e

# Example usage in the main function
def main():
    calculator = Calculator()
    print(f"Result of 5 + 3: {calculator.add(5, 3)}")
    print(f"Result of 2 * 4: {calculator.multiply(2, 4)}")

if __name__ == "__main__":
    main()