"""API Client handling functions."""

from __future__ import annotations
from typing import Any, Dict, Union
import requests

class ApiClient:
    """A simple API client class.

    Args:
        base_url (str): The base URL for the API.
    """

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get(self, path: str, params: Union[Dict[str, Any], None] = None, **kwargs) -> requests.Response:
        """Send a GET request to the specified path."""
        response = requests.get(self.base_url + path, params=params, **kwargs)
        self._check_response_status(response)
        return response

    def post(self, path: str, json: Union[Dict[str, Any], None] = None, **kwargs) -> requests.Response:
        """Send a POST request to the specified path."""
        response = requests.post(self.base_url + path, json=json, **kwargs)
        self._check_response_status(response)
        return response

    def _check_response_status(self, response: requests.Response):
        """Check the response status code."""
        if response.status_code not in [200, 201]:
            raise Exception(f"Unexpected status code: {response.status_code}")