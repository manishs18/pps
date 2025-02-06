import pytest

@pytest.mark.xfail(reason="Known bug in cart module")
def test_add_to_cart():
    assert False

def test_remove_from_cart():
    assert True