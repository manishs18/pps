import pytest
import time
from manish_ecp_pom.apps.pages.ProductsPage import Products


@pytest.mark.usefixtures("driver")
def test_add_review_on_product(driver):
    product_page = Products(driver)
    time.sleep(2)

    product_page.click_products()
    time.sleep(2)

    product_page.write_review("manish", "manish123@gmail.com", "Good quality!")
    time.sleep(2)