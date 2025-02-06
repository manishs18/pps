from unittest import mock
import pytest
from tut9.myApp.sample import guess_number

@pytest.mark.parametrize("input, expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("tut9.myApp.sample.roll_dice")
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess_number(3) == "You won!"
    mock_roll_dice.assert_called_once()

@mock.patch("tut9.myApp.sample.requests.get")
def test_get_ip():
    mock_requests_get.return_value = mock.Mock(name="mock response", **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})

    assert get_ip() ="0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")

