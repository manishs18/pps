import pytest
import time
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage


username = "manish123@gmail.com"
password = "manish11"

@pytest.mark.usefixtures("driver")
def test_valid_login(driver):
    home_page = HomePage(driver)
    time.sleep(2)

    register_page = RegisterPage(driver)
    time.sleep(2)
    register_page.click_signin_btn()
    time.sleep(2)

    register_page.enter_login(username, password)
    time.sleep(2)

    register_page.verify_logged_in_as_visible()
    time.sleep(2)
