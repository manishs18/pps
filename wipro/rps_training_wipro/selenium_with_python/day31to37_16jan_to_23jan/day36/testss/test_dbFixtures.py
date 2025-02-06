import pytest

@pytest.fixture
def dbconnection():
    # Simulating a database connection setup
    print("Setting up database connection")
    connection = "Mock DB Connection"
    yield connection
    # Simulating closing the database connection
    print("Closing database connection")

@pytest.mark.usefixtures('dbconnection')
def test_createquery():
    print("table is created")

@pytest.mark.usefixtures("dbconnection")
def test_deletequery():
    print("table is deleted")

@pytest.mark.usefixtures('dbconnection')
def test_selectquery():
    print("table is selected")
