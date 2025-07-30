"""
Email validator module for handling email validation.

This module provides a function to validate an email address using Python's built-in libraries.
It handles common edge cases and returns `None` if the input is not a string.

:author: Your Name
:version: 1.0.0
"""

from __future__ import annotations
from typing import Union, Optional
import re

class EmailValidator:
    """
    Class to validate email addresses using regular expressions.
    """

    def __init__(self):
        self._pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def validate(self, email: str) -> Optional[str]:
        """
        Validate an email address using regular expressions.

        :param email: The input email to be validated.
        :return: None if the input is not a string, and the validated email otherwise.
        """
        if not isinstance(email, str):
            return None
        match = re.fullmatch(self._pattern, email)
        if match:
            return email.lower()
        return None