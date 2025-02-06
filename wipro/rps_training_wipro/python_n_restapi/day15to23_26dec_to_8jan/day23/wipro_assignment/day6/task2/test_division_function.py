# test_division_function.py
import pytest
from division_function import divide_numbers

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(-10, 2) == -5
    
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide_numbers(10, 0)
