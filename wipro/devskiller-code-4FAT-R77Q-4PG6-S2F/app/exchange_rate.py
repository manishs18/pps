import decimal
import typing

from app.currency import Currency
from app.rates import RATES


class QuotationError(Exception):
    pass

class ExchangeRateService:
    _rates = RATES

    def update_rate(self, currency: Currency, rate: decimal.Decimal):
        self._rates[currency] = rate

    def get_rate(self, currency: Currency) -> typing.Optional[decimal.Decimal]:
        try:
            return self._rates[currency]
        except KeyError:
            return None

    def quotation(
        self, origin: Currency, target: Currency
    ) -> typing.Optional[decimal.Decimal]:
        """Calculate the exchange rate between two currencies.
        
        Args:
            origin: The base currency
            target: The quote currency
            
        Returns:
            The exchange rate as a Decimal
            
        Raises:
            QuotationError: If either currency is invalid or rates are not available
        """
        origin_rate = self.get_rate(origin)
        target_rate = self.get_rate(target)
        
        if origin_rate is None or target_rate is None:
            raise QuotationError("Invalid currency or missing exchange rate")
            
        # Calculate the exchange rate: target_rate / origin_rate
        # This gives us how many units of target currency we get for 1 unit of origin currency
        return target_rate / origin_rate
