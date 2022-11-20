"""Test config and app/client fixtures for pytest integration testing."""

import pytest

from api import create_app
from ..config import TestConfig


@pytest.fixture
def client():
    """Initialize Flask app for testing client requests."""

    app = create_app(config=TestConfig)
    with app.test_client() as client:
        yield client
