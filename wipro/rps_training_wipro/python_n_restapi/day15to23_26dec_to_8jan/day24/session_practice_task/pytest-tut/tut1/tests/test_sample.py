from tut1.myApp.sample import add

def test_add_num():
    assert add(1, 2) == 3
def test_add_str():
    assert add("m", "k") == "mk"

class TestAdd:
    def test_add_num(self):
        assert add(1, 2) == 3
    def test_add_str(self):
        assert add("m", "k") == "mk"