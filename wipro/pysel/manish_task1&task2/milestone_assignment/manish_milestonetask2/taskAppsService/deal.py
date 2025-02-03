# service/deal.py
class Deal:
    """Model representing a Deal object."""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
