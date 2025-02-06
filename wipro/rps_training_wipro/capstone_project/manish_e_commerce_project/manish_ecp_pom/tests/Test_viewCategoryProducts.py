import time
import pytest
from manish_ecp_pom.apps.pages.ViewCategoryPage import ViewCategory

@pytest.mark.usefixtures("driver")
def test_view_category_products(driver):
    view_category = ViewCategory(driver)
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 200)")
    view_category.women_category()
    time.sleep(2)

    view_category.men_category()
    time.sleep(2)