from webappsecurity.pages.loginPage import LoginPage
import time



def test_payee_bills(driver):
    login_page = LoginPage(driver)
    login_page.login_with_valid_cred("username", "password")
    login_page.searchForTransactions("CAR PAYMENT")