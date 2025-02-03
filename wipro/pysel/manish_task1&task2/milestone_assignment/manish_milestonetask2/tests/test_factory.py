# tests/test_factory.py
import os
from manish_milestonetask2.factory import api_crm_client_factory
from manish_milestonetask2.taskAppsClient.crm import CRMApiClient
from manish_milestonetask2.taskAppsClient.dummy_api import DummyAPIClient

def test_factory_returns_dummy_client(monkeypatch):
    monkeypatch.setenv('ENV', 'testing')
    client = api_crm_client_factory()
    assert isinstance(client, DummyAPIClient)

def test_factory_returns_crm_client(monkeypatch):
    monkeypatch.delenv('ENV', raising=False)
    client = api_crm_client_factory()
    assert isinstance(client, CRMApiClient)
