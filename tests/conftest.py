import os
import sys
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app, init_db


@pytest.fixture
def client(monkeypatch):

    test_db = "test.db"

    monkeypatch.setenv("DB_PATH", test_db)

    if os.path.exists(test_db):
        os.remove(test_db)

    init_db()

    client = TestClient(app)

    yield client

    if os.path.exists(test_db):
        os.remove(test_db)