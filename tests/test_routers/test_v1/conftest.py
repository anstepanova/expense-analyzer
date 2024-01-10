"""Fixtures for testing v1 routers."""


import pytest
from fastapi.testclient import TestClient

from expense_analyzer.main import app


@pytest.fixture
def test_client():
    """Test client for routers."""
    yield TestClient(app)
