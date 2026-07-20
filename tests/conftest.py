"""Shared pytest fixtures for the SP test suite."""

import pytest

from sp.app import app as flask_app


@pytest.fixture
def client():
    """Provide a Flask test client."""
    flask_app.config.update({"TESTING": True})
    with flask_app.test_client() as client:
        yield client
