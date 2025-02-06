import pytest
import time
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("driver")
def test_registered_user_with_existing_email(driver):
    register_page = RegisterPage(driver)
    time.sleep(2)
    register_page.click_signin_btn()
    time.sleep(2)

    register_page.enter_signup("manish11", "manish123j@gmail.com")
    time.sleep(2)
