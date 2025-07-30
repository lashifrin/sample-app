from __future__ import annotations
import sys

def fibonacci(n: int) -> tuple[int, Exception|None]:
    """Calculate the Fibonacci sequence up to n.

    This function calculates and returns the Fibonacci sequence up to n,
    where n is a non-negative integer. If an error occurs during calculation,
    an exception will be raised.

    Args:
        n (int): Number of terms in the Fibonacci sequence.

    Returns:
        Tuple of two integers: The first element is the calculated number,
        and the second element is either the next Fibonacci number or an exception.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    sequence = [0, 1]
    while len(sequence) <= n:
        next_num = sum(sequence[-2:-1])
        sequence.append(next_num)

    if len(sequence) > n + 1:
        sequence = tuple(sequence[:n + 1])

    return sequence[-1], None