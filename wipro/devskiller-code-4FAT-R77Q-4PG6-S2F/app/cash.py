import decimal

import typing

from app.currency import Currency
from app.factories import exchange_rate_service_factory
from app.exceptions import ExchangeRateUnknownError, InvalidCurrencyError
from app.helper import quantize

CashOrNumber = typing.Union[int, decimal.Decimal, "Cash"]


class Cash:
    __slots__ = "_amount", "_currency", "_exchange_rate_service"
    _target_currency = None  # Add class-level target currency

    def __init__(
        self, amount: typing.Union[str, decimal.Decimal], currency: Currency
    ) -> None:
        if not isinstance(currency, Currency) or not Currency.is_member(currency.value):
            raise InvalidCurrencyError

        self._amount = decimal.Decimal(amount)
        self._currency = currency
        self._exchange_rate_service = exchange_rate_service_factory()

    @property
    def amount(self) -> decimal.Decimal:
        return quantize(self._amount)

    @property
    def currency(self) -> Currency:
        return self._currency

    def __repr__(self) -> str:
        return f"{self.amount} {self.currency.name}"

    def __lt__(self, other: CashOrNumber) -> bool:
        if isinstance(other, Cash):
            # Convert both to target currency if set, otherwise to self's currency
            target = self._target_currency or self.currency
            converted_self = self.to(target)
            converted_other = other.to(target)
            return converted_self.amount < converted_other.amount
        return self.amount < self._get_amount(other)

    def __le__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount <= amount

    def __gt__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount > amount

    def __ge__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount >= amount

    def __eq__(self, other: CashOrNumber) -> bool:
        if isinstance(other, Cash):
            # Convert both to target currency if set, otherwise to self's currency
            target = self._target_currency or self.currency
            converted_self = self.to(target)
            converted_other = other.to(target)
            return converted_self.amount == converted_other.amount
        return self.amount == self._get_amount(other)

    def __ne__(self, other: CashOrNumber) -> bool:
        return not self == other

    def __bool__(self):
        return bool(self._amount)

    def __add__(self, other: CashOrNumber) -> "Cash":
        if isinstance(other, Cash):
            # Convert other to self's currency before adding
            target = self._target_currency or self.currency
            converted_self = self.to(target)
            converted_other = other.to(target)
            amount = converted_self.amount + converted_other.amount
            return Cash(amount, target)
        
        # For non-Cash numbers, add directly and convert if needed
        amount = self.amount + self._get_amount(other)
        target = self._target_currency or self.currency
        result = Cash(amount, self.currency)
        return result.to(target) if target != self.currency else result

    def __radd__(self, other: CashOrNumber) -> "Cash":
        return self.__add__(other)

    def __neg__(self) -> "Cash":
        return Cash(-self._amount, self.currency)

    def __pos__(self) -> "Cash":
        return Cash(+self._amount, self.currency)

    def __abs__(self) -> "Cash":
        return Cash(abs(self._amount), self.currency)

    def __sub__(self, other: CashOrNumber) -> "Cash":
        if isinstance(other, Cash):
            # Convert other to self's currency before subtracting
            target = self._target_currency or self.currency
            converted_self = self.to(target)
            converted_other = other.to(target)
            amount = converted_self.amount - converted_other.amount
            return Cash(amount, target)
            
        # For non-Cash numbers, subtract directly and convert if needed
        amount = self.amount - self._get_amount(other)
        target = self._target_currency or self.currency
        result = Cash(amount, self.currency)
        return result.to(target) if target != self.currency else result

    def __rsub__(self, other: CashOrNumber) -> "Cash":
        return (-self).__add__(other)

    def to(self, target_currency: Currency) -> "Cash":
        """Convert cash amount to target currency using exchange rate service.
        
        Args:
            target_currency: The currency to convert to
            
        Returns:
            A new Cash instance with the converted amount
            
        Raises:
            ExchangeRateUnknownError: If exchange rate is not available
        """
        if target_currency is None or target_currency == self.currency:
            return Cash(self.amount, self.currency)
            
        try:
            rate = self._exchange_rate_service.quotation(self.currency, target_currency)
            new_amount = self.amount * rate
            return Cash(new_amount, target_currency)
        except Exception as e:
            # Re-raise appropriate exception
            raise ExchangeRateUnknownError(f"Failed to convert {self.currency} to {target_currency}: {str(e)}")

    def __matmul__(self, target_currency: Currency) -> "Cash":
        """Implement the @ operator for currency conversion.
        
        Args:
            target_currency: The currency to convert to
            
        Returns:
            A new Cash instance with the converted amount
        """
        return self.to(target_currency)

    def _get_amount(self, other: CashOrNumber) -> decimal.Decimal:
        if isinstance(other, Cash):
            target = self._target_currency or self.currency
            converted_other = other.to(target)
            return converted_other.amount
        return decimal.Decimal(str(other))


class TargetCurrency:
    def __init__(self, currency: Currency) -> None:
        self.currency = currency
        self._previous_target = None

    def __enter__(self) -> None:
        self._previous_target = Cash._target_currency
        Cash._target_currency = self.currency

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        Cash._target_currency = self._previous_target
