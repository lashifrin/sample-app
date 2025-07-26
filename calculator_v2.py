from typing import Union, Optional

class Calculator:
    """Simple calculator class with basic arithmetic operations.

    Attributes:
        none

    Methods:
        add(a: float, b: float) -> float: Add two numbers.
        subtract(a: float, b: float) -> Union[float, None]: Subtract two numbers and handle division by zero.
        multiply(a: float, b: float) -> float: Multiply two numbers.
        divide(a: float, b: float) -> Union[float, None]: Divide two numbers and handle division by zero.
    """

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> Union[float, None]:
        """Subtract two numbers and handle division by zero."""
        if b == 0:
            return None
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> Union[float, None]:
        """Divide two numbers and handle division by zero."""
        if b == 0:
            return None
        return a / b

def main() -> None:
    """Entry point for demonstrating calculator usage."""
    calc = Calculator()
    print(f"Addition: {calc.add(3, 5)}")
    print(f"Subtraction (with zero as denominator): {calc.subtract(3, 0)}")
    print(f"Multiplication: {calc.multiply(3, 5)}")
    print(f"Division (with non-zero denominator): {calc.divide(3, 2)}")
    print(f"Division (with zero as denominator): {calc.divide(3, 0)}")

if __name__ == "__main__":
    main()