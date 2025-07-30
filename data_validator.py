"""
Data Validator module to validate data structures.
"""
from typing import Dict, Any

class DataValidator:
    """
    Class for validating data structures.
    """

    def __init__(self):
        self._errors = []

    def add_error(self, error: str) -> None:
        """
        Add an error message to the list of errors.

        Args:
            error (str): The error message to be added.
        """
        self._errors.append(error)

    def is_valid(self) -> bool:
        """
        Check if there are any errors in validation.

        Returns:
            True if no errors, False otherwise.
        """
        return not self._errors

    def validate(self, data: Dict[str, Any]) -> None:
        """
        Validate the provided data dictionary.

        Args:
            data (Dict[str, Any]): The data to be validated.
        """
        required_keys = ['key1', 'key2']  # Add your required keys here

        missing_keys = set(required_keys) - set(data.keys())
        if missing_keys:
            for key in missing_keys:
                self.add_error(f"Missing required key '{key}'.")

        # Add more validation checks as necessary