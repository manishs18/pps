import os
import json
from tut5.myApp.sample import save_dict

def test_save_dict(tmpdir, capsys):
    filepath  = os.path.join(tmpdir, "test.json")
    _dict = {"a": 1, "b": 2}
    
    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "saved\n"