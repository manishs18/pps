import unittest


class TestCurrencyEnumIsMember(unittest.TestCase):
    def test_currency_exists(self):
        assert self._execute_sut("EUR") is True

    def setUp(self):
        from app.currency import Currency

        self._sut = Currency.is_member

    def _execute_sut(self, value):
        return self._sut(value)
