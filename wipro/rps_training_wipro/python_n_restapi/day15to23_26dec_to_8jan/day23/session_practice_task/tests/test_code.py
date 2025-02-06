from module import code


def add (a,b):
    return a+b


def test_add():
    assert code.add(1,2) == 3
    