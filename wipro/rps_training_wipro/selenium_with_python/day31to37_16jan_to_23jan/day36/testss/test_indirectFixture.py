import pytest

# Define a fixture that takes arguments
@pytest.fixture()
def square(request):
    return request.param * 2

# Use the indirect parameterization to pass the arguments
@pytest.mark.parametrize("square", [1, 2, 3], indirect=True)
def test_square(square):
    assert square in [2, 4, 6]
