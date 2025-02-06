import pytest

@pytest.fixture(scope='function')
def openclosebrowser():
    print("open the browser")

    yield
    print("close the browser")

@pytest.mark.usefixtures("openclosebrowser")
def test_login():
    print("enter username")
    print("enter password")
    print("click on login button")

@pytest.mark.usefixtures('openclosebrowser')
def test_logout():
    print("user is logged out")