from day36.myApps.area import *
from pytest import approx

import pytest

class TestArea:
    def test_circle(self):
        assert circle(14) == approx(615.75, rel=1e-2)

    def test_square(self):
        assert square(2) == 4

    def test_rectangle(self):
        assert rectangle(2, 4) == 8

    def test_parallelogram(self):
        assert parallelogram(2, 4) == 8
