import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "spec(uid): Links test to a Spec-Node UID (e.g. PROJ-TC-001)"
    )
