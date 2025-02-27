from webappsecurity.pages.loginPage import LoginPage
import time



def test_payee_bills(driver):
    login_page = LoginPage(driver)
    login_page.login_with_valid_cred("username", "password")
    login_page.pay_bills("100", "paying 100$ to weels fargo from savings")