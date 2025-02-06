import pytest
import time
from manish_ecp_pom.apps.pages.Locators import Locators


@pytest.mark.usefixtures("driver")
def test_testcases_page(driver):
    locator_page = Locators(driver)
    time.sleep(3)

    locator_page.click_testcases_btn()
    time.sleep(2)