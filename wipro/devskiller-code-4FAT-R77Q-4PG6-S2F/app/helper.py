import decimal


def quantize(value: decimal.Decimal) -> decimal.Decimal:
    return value.quantize(decimal.Decimal("0.0000"))
