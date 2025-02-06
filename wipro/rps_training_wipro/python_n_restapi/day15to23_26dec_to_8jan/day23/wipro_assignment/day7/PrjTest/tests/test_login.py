import pytest
def login(username, password):
    return username == "admin" and password == "password"


def test_login_success():
    assert login("admin", "password") == True

def test_login_failure():
    assert login("user", "pass") == False