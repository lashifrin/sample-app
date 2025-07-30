"""Test client module."""

from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict, List

import pytest
import requests

from your_project_name import constants as cst
from your_project_name import exceptions as exc
from your_project_name.client import Client

# Define fixtures
@pytest.fixture(scope="function")
def client() -> Client:
    """Fixture to create a client instance for testing."""
    return Client()

@pytest.fixture(scope="module")
def test_data():
    """Fixture to provide test data."""
    return {
        "test_data_1": {"key_1": "value_1"},
        # Add more test data as needed
    }

# Define tests
def test_successful_request(client: Client, test_data: Dict[str, Any]) -> None:
    """Test successful API request."""
    # Replace this with the expected API endpoint and parameters based on your testing requirements.
    response = client.get(cst.API_ENDPOINT)

    assert response.status_code == 200
    assert json.loads(response.content)["data"] == test_data["test_data_1"]

def test_unsuccessful_request(client: Client, test_data: Dict[str, Any]) -> None:
    """Test unsuccessful API request."""
    # Replace this with the expected API endpoint and parameters based on your testing requirements.
    response = client.get(cst.UNSUCCESSFUL_API_ENDPOINT)

    assert response.status_code != 200
    assert json.loads(response.content)["message"] == cst.TEST_UNSUCCESSFUL_REQUEST_MESSAGE

def test_client_raises_exception(client: Client) -> None:
    """Test that client raises expected exceptions."""
    with pytest.raises(exc.CustomException):
        client.do_something_that_raises_an_exception()