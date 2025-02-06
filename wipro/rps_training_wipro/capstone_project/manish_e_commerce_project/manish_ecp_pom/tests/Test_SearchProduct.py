import time
import pytest
from manish_ecp_pom.apps.pages.SearchProductPage import SearchProduct


@pytest.mark.usefixtures("driver")
def test_search_product(driver):
    search_page = SearchProduct(driver)
    time.sleep(2)

    search_page.click_search_products("Fancy Green Top")
    time.sleep(2)

