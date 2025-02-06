import pytest
import time
from selenium import webdriver
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage
from manish_ecp_pom.apps.pages.Locators import Locators


@pytest.mark.usefixtures("driver")
def test_logout(driver):
    home_page = HomePage(driver)
    time.sleep(2)

    register_page = RegisterPage(driver)
    time.sleep(2)

    register_page.click_signin_btn()
    time.sleep(2)

    register_page.enter_login("manish123@gmail.com", "manish11")
    time.sleep(2)

    locator = Locators(driver)
    locator.click_logout()
    time.sleep(2)

