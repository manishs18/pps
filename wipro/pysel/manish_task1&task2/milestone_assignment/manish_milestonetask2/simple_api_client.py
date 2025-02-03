# simple_api_client.py

import requests

class SimpleAPIClient:
    """Base class for handling REST API calls."""

    def _call(self, method, endpoint, **kwargs):
        """Perform an HTTP request."""
        url = f"{self.root_api_url}/{endpoint}"
        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.api_key}"  # Assuming Bearer token authentication

        response = requests.request(method, url, headers=headers, **kwargs)

        if response.status_code in {200, 201}:
            return response.json()
        response.raise_for_status()
