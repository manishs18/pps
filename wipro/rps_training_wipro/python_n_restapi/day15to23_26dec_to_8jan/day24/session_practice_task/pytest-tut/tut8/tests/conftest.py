import pytest
from datetime import datetime
from tut8.myApp.sample import Student


@pytest.fixture
def dummy_student(request):
    return Student("nikhil", datetime(2000, 1, 1), "coe", request.param)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)
    return _make_dummy_student