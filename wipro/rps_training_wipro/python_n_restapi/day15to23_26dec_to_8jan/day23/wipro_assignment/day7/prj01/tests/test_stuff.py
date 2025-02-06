import pytest

class Stuff:
    def prep(self):
        self.foo = 1
        self.bar = 2

def test_foo_updates():
    mystuff = Stuff()
    mystuff.prep()
    assert 1 == mystuff.foo
    mystuff.foo = 300
    assert 300 == mystuff.foo



