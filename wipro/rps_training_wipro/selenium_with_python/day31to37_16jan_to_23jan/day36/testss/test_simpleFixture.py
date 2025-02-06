import pytest

@pytest.fixture()
def data():
    return 42


#test case
def test_sampledata(data):
    assert data == 42