# factory.py
import os
from manish_milestonetask2.taskAppsClient.crm import CRMApiClient
from manish_milestonetask2.taskAppsClient.dummy_api import DummyAPIClient
from .settings import API_KEY, API_URL

def api_crm_client_factory():
    """Factory function to return the appropriate CRM API client."""
    if os.getenv('ENV') == 'testing':
        return DummyAPIClient()
    return CRMApiClient(API_KEY, API_URL)
