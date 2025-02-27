from enum import Enum


class Currency(Enum):
    PLN = "PLN"
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    NOK = "NOK"
    USD = "USD"
    ZAR = "ZAR"

    @classmethod
    def is_member(cls, value: str) -> bool:
        """Check if the given currency code is a valid member of the Currency enum.

        Args:
            value (str): The currency code to check.

        Returns:
            bool: True if the currency code is valid, False otherwise.
        """
        return value in [currency.value for currency in cls]
