import time
import pytest
from manish_ecp_pom.apps.pages.BrandPage import Brand

@pytest.mark.usefixtures("driver")
def test_brand(driver):
    brand_page = Brand(driver)
    time.sleep(2)

    brand_page.click_brand()
    time.sleep(2)