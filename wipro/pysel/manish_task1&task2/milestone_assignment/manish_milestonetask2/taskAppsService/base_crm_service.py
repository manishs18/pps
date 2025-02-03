# service/base_crm_service.py
class BaseCRMService:
    """Base class for CRM services."""
    def __init__(self, api_url):
        self.api_url = api_url
