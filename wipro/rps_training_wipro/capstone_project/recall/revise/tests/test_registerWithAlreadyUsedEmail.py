from revise.pages.registerPage import RegisterPage
import time


def test_already_exits_credentials(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()
    home_page_btn.signUp_login_btns()
    home_page_btn.sign_up("manish18", "manish18@gmail.com")
    home_page_btn.already_user_email_exits()
    time.sleep(2)