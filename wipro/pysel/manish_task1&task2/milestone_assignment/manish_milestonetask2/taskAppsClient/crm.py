# client/crm.py
from manish_milestonetask2.simple_api_client import SimpleAPIClient

class CRMApiClient(SimpleAPIClient):
    """Singleton-based CRM API Client."""
    _instances = {}

    def __new__(cls, api_key, root_api_url):
        key = (api_key, root_api_url)
        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)
        return cls._instances[key]

    def __init__(self, api_key=None, root_api_url=None):
        if not getattr(self, '_initialized', False):
            self.api_key = api_key
            self.root_api_url = root_api_url
            self._initialized = True

    def call(self, method, **kwargs):
        """Facade to the parent `_call` method."""
        return self._call(method, **kwargs)
