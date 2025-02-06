import pytest
import time
from selenium import webdriver
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage
from manish_ecp_pom.apps.pages.Locators import Locators


@pytest.mark.usefixtures("driver")
def test_remove_products_from_cart(driver):
    home_page = HomePage(driver)
    time.sleep(2)

    register_page = RegisterPage(driver)
    time.sleep(2)

    # Add products to cart
    driver.execute_script("window.scrollBy(0, 1000)")
    home_page.click_panda_shirt()
    time.sleep(3)
    home_page.click_continue_shopping()
    time.sleep(2)
    driver.execute_script("window.scrollBy(1000, 0)")
    home_page.click_cart()

    home_page.click_cart()
    time.sleep(2)

    locator = Locators(driver)
    locator.click_cart_quantity_delete()
    time.sleep(2)


