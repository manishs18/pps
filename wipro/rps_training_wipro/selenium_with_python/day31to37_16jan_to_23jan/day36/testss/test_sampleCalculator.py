import pytest

# @pytest.fixture()
def add(a, b):
    return a + b

def test_add():
    result = add(10, 5)
    assert result == 15