# tests/test_crm_client.py
from manish_milestonetask2.taskAppsClient.crm import CRMApiClient

def test_crm_api_client_singleton():
    client1 = CRMApiClient('api_key', 'https://example.com/api')
    client2 = CRMApiClient('api_key', 'https://example.com/api')
    assert client1 is client2
