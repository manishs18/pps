# tests/test_crm_deals_service.py
import requests
from unittest.mock import patch
from manish_milestonetask2.taskAppsService.crm_deals_service import CRMDealsService
from manish_milestonetask2.taskAppsService.deal import Deal

@patch('requests.get')
def test_crm_deals_service_get(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "name": "Test Deal"}
    service = CRMDealsService("https://example.com/api")
    deal = service.get(deal_id="1")
    assert isinstance(deal, Deal)
    assert deal.id == 1
    assert deal.name == "Test Deal"

@patch('requests.post')
def test_crm_deals_service_create(mock_post):
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {"id": 2, "name": "New Deal"}
    service = CRMDealsService("https://example.com/api")
    deal = service.create(data={"name": "New Deal"})
    assert isinstance(deal, Deal)
    assert deal.id == 2
    assert deal.name == "New Deal"
