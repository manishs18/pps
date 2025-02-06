import pytest
@pytest.fixture()
def is_prime(n=11):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def test_prime(is_prime):
    assert is_prime == True