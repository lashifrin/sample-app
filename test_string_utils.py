# string_utils_test.py

import unittest
from unittest.mock import patch
from string_utils import reverse_string, count_vowels

class TestStringUtils(unittest.TestCase):
    """Tests for the string_utils module."""

    def test_reverse_string(self):
        """Test reversing a string."""

        # Normal case
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")

        # Empty string
        self.assertEqual(reverse_string(""), "")

        # Single character string
        self.assertEqual(reverse_string("a"), "a")

    def test_count_vowels(self):
        """Test counting vowels in a string."""

        # Normal case
        self.assertEqual(count_vowels("Hello, World!"), 3)

        # Empty string
        self.assertEqual(count_vowels(""), 0)

        # String with only vowels
        self.assertEqual(count_vowels("aeiouAEIOU"), 11)

    @patch('re.findall')
    def test_count_vowels_with_error(self, mock_findall):
        """Test handling of errors in count_vowels."""

        # Mocking an exception from re.findall
        mock_findall.side_effect = Exception("Mock error")

        with self.assertRaises(Exception) as context:
            count_vowels("Invalid regex pattern")

        self.assertEqual(str(context.exception), "Mock error")

if __name__ == "__main__":
    unittest.main()