from tutorial.apps.simpleapp import add

def test_add_num():
    result = add(1,3)
    assert result == 4
   