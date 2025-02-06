from tut2.myApp.sample import validate_age
import pytest

def test_validate_age():
    validate_age(9)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than Zero!"):
        validate_age(-2)
