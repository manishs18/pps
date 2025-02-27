from webappsecurity.pages.loginPage import LoginPage
import time


def test_transfer_funds(driver):
    login_page = LoginPage(driver)
    login_page.login_with_valid_cred("username", "password")
    login_page.transfer_funds("100", "manish at now transfer 100$")