from revise.pages.registerPage import RegisterPage
from revise.pages.loginPage import LoginPage


def test_logout(driver):

    signup_btn = RegisterPage(driver)
    login_btn = LoginPage(driver)

    signup_btn.verify_home_page()
    signup_btn.signUp_login_btns()

    login_btn.verify_login_acc_text_visible()
    login_btn.login_with_credentials("manish18@gmail.com", "manish18@123")
    login_btn.logoutUser()
    login_btn.verify_login_acc_text_visible()
