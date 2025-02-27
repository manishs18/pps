from webappsecurity.pages.loginPage import LoginPage
import time



def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.login_with_valid_cred("username", "password")
    login_page.verify_logged_id_n_account_summary()


def test_verify_account_summary_page(driver):
    login_page = LoginPage(driver)
    login_page.login_with_valid_cred("username", "password")
    login_page.verify_logged_id_n_account_summary()
    login_page.account_summary_verification()

