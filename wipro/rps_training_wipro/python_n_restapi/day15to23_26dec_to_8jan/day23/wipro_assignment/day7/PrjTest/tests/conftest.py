import pytest

@pytest.fixture
def db_connection():
    print("Connecting to the database")
    yield
    print("Disconnecting from the database")