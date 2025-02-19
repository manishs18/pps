import pytest
from selenium import webdriver
from revise.pages.registerPage import RegisterPage
# from tests.conftest import driver
import time
import string


# @pytest.fixture
# def driver():
#     option = webdriver.EdgeOptions()
#     driver = webdriver.Edge(options=option)
#     driver.maximize_window()
#     driver.get("https://automationexercise.com/")

#     yield driver
#     driver.quit()

def test_signUp_login_btn(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()
    home_page_btn.signUp_login_btns()
    home_page_btn.sign_up("maniishhhs18", "maniishhhs18@gmail.com")
    time.sleep(2)
    home_page_btn.signUp_details("maniishhhs18@123", "manishhsssss", "Singhshssss", "wiprob1, noida, sector62", "wiprob2, banglore, sarjapur", "Bihar", "gpg", "841405", "6283526137")
    time.sleep(3)

