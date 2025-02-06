import pytest
import time
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage


username = "manish321@gmail.com"
password = "manish@11"

@pytest.mark.usefixtures("driver")
def test_invalid_login(driver):
    register_page = RegisterPage(driver)
    time.sleep(2)
    register_page.click_signin_btn()
    time.sleep(2)

    register_page.enter_login(username, password)
    time.sleep(2)

    register_page.verify_logged_in_as_visible()
    time.sleep(2)
