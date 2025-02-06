import pytest
import time
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.ProductsPage import Products


@pytest.mark.usefixtures("driver")
def test_add_to_cart(driver):
    product_page = Products(driver)
    time.sleep(2)

    register_page = RegisterPage(driver)
    time.sleep(2)

    home_page = HomePage(driver)
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 300)")

    # Add product 1
    product_page.click_add_product()
    time.sleep(2)
    home_page.click_panda_shirt()
    time.sleep(2)
    home_page.click_continue_shopping()
    time.sleep(2)

    # Add product 2
    driver.execute_script("window.scrollBy(0, 300)")
    product_page.click_add_product()
    time.sleep(2)
    home_page.click_panda_shirt()
    time.sleep(2)
    home_page.click_continue_shopping()
    time.sleep(2)

    home_page.click_cart()
    time.sleep(2)

    product_page.quantity()
    time.sleep(2)