from unittest import mock
from unittest.mock import call
from tut10.myApp.sample import random_sum, silly

@mock.patch("tut10.myApp.sample.random.randint")
def test_random_sum():
    mock_randint.side_effects = [3, 4]
    assert random_sum() == 7
    mock_randit.assert_calls(calls=[call(1, 10), call(1, 7)])




@mock.patch("tut10.myApp.sample.random.randint")
@mock.patch("tut10.myApp.sample.time.time")
@mock.patch("tut10.myApp.sample.requests.get")
def test_silly(mock_requests_get, mock_time, mock_randint):
    test_params = {
        "timestamp": 123,
        "number": 5
    }
    mock_time.return_value = test_params['timestamp']
    mock_randint.return_value = 5
    mock_requests_get = mock. Mock(**{"status_code": 200, "json.return_value": {"args: test_params"}})
    assert silly() == test_params