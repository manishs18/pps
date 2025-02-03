# client/dummy_api.py
class DummyAPIClient:
    """Dummy API client for testing purposes."""
    def call(self, method, **kwargs):
        return {"message": f"Dummy client called with method {method} and args {kwargs}"}
