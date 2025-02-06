from tut3.myApp.sample import add
import pytest
import sys

@pytest.mark.skip(reason="just wanna skip it")
def test_add_num():
    assert add(1, 2) == 3

@pytest.mark.skipif(sys.version_info > (3, 7), reason="use python 3.7 or less")  
def test_add_str():
    assert add("m", "k") == "mk"


@pytest.mark.xfail(sys.platform == "win32", reason="dont run on windows")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()
