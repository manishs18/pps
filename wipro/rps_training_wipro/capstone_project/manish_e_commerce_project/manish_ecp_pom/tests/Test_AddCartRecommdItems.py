import time
import pytest
from manish_ecp_pom.apps.pages.RecommditemsPage import RecommendedItems
from manish_ecp_pom.apps.pages.HomePage import HomePage

@pytest.mark.usefixtures("driver")
def test_recommended_items(driver):
    recommend_page = RecommendedItems(driver)
    time.sleep(2)

    home_page = HomePage(driver)
    time.sleep(2)

    recommend_page.recommended_item()
    time.sleep(2)
    home_page.click_continue_shopping()
    time.sleep(2)

    home_page.click_cart()
    time.sleep(2)
