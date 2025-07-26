# string_utils.py

import re

DOCSTRING = '''
Module containing utilities for working with strings. This module provides a function to reverse a string and count vowels in the given string.
'''

__all__ = ['reverse_string', 'count_vowels']

# Constants
VOWELS = set('aeiou')

def reverse_string(input_string: str) -> str:
    """
    Reverses the given string.

    Parameters:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return input_string[::-1]

def count_vowels(input_string: str) -> int:
    """
    Counts the number of vowels in a given string.

    Parameters:
        input_string (str): The string to be searched for vowels.

    Returns:
        int: The count of vowels in the given string.
    """
    return sum(1 for char in re.findall('[aeiouAEIOU]', input_string))

def main():
    """
    Example usage demonstrating reverse_string and count_vowels functions.
    """
    example_str = "Hello, World!"
    reversed_example_str = reverse_string(example_str)
    vowel_count = count_vowels(example_str)

    print(f"Reversed String: {reversed_example_str}")
    print(f"Vowel Count: {vowel_count}")

if __name__ == "__main__":
    main()