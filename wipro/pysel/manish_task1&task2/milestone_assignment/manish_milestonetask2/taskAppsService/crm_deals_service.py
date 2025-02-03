# service/crm_deals_service.py
import requests
from manish_milestonetask2.taskAppsService.base_crm_service import BaseCRMService
from .deal import Deal

class CRMDealsService(BaseCRMService):
    """Service to interact with CRM deals API."""

    def get(self, deal_id: str):
        """Fetch a specific deal by ID."""
        response = requests.get(f"{self.api_url}/deals/{deal_id}")
        if response.status_code == 200:
            return Deal(**response.json())
        response.raise_for_status()

    def get_list(self):
        """Fetch a list of all deals."""
        response = requests.get(f"{self.api_url}/deals")
        if response.status_code == 200:
            return [Deal(**deal) for deal in response.json()]
        response.raise_for_status()

    def create(self, data: dict):
        """Create a new deal."""
        response = requests.post(f"{self.api_url}/deals", json=data)
        if response.status_code == 201:
            return Deal(**response.json())
        response.raise_for_status()
