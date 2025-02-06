import pytest
import time
import random
import string
from selenium import webdriver
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage
from manish_ecp_pom.apps.pages.Locators import Locators


@pytest.fixture
def driver():
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    yield driver

    driver.quit()


random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
dynamic_username = f"{random_suffix}"
dynamic_email = f"{random_suffix}@example.com"


def test_register_user(driver):
    register_page = RegisterPage(driver)
    time.sleep(2)

    locator = Locators(driver)
    time.sleep(2)

    register_page.click_signin_btn()
    time.sleep(2)

    register_page.verify_home_page_visible()

    register_page.enter_signup("manishs1234", "manish1234@gmail.com")
    time.sleep(2)

    # Details of user
    register_page.enter_details("manish1234", "Manishss", "Singhss", "India",
                                "India", "India", "India", "231435", "231425464")
    time.sleep(2)

    register_page.click_continue()
    time.sleep(2)

    locator.click_logout()
    time.sleep(2)
