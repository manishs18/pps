import pytest

@pytest.fixture
def openclosebrowser():
    # Simulate opening a browser
    print("Browser is opened")
    browser = "Mock Browser Instance"
    yield browser
    # Simulate closing a browser
    print("Browser is closed")

@pytest.mark.usefixtures('openclosebrowser')
def test_login():
    print("enter username")
    print("enter password")
    print("Click on login button")

@pytest.mark.usefixtures('openclosebrowser')
def test_logout():
    print("user is logged out")
