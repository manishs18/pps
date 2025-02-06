import pytest
import time
from manish_ecp_pom.apps.pages.SearchProductPage import SearchProduct
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage
from manish_ecp_pom.apps.pages.Locators import Locators


username = "manish123@gmail.com"
password = "manish11"

@pytest.mark.usefixtures("driver")
def test_search_product_verify_cart(driver):
    home_page = HomePage(driver)
    search_page = SearchProduct(driver)
    time.sleep(2)

    search_page.click_search_products("Fancy Green Top")
    time.sleep(2)

    search_page.add_cart_product()
    time.sleep(2)

    home_page.click_continue_shopping()
    time.sleep(2)

    home_page.click_cart()
    time.sleep(2)

    register_page = RegisterPage(driver)
    time.sleep(2)
    register_page.click_signin_btn()
    time.sleep(2)

    register_page.enter_login(username, password)
    time.sleep(2)

    home_page.click_cart()
    time.sleep(2)

    locator = Locators(driver)
    locator.click_cart_quantity_delete()
    time.sleep(2)

