import time
import pytest
from selenium import webdriver
from ecp_pom.apps.homePage import HomePage
from ecp_pom.apps.loginPage import LoginPage


@pytest.fixture()
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://www.automationexercise.com/')
    yield driver
    driver.quit()

def test_vaild_login_user(driver):
    lp = LoginPage(driver)
    lp.click_login_signUp()
    text = lp.check_login_text()
    print(text)
    print(text.__contains__("Login to your account"))
    lp.enter_email("wipro@gmail.com")
    time.sleep(2)
    lp.enter_password("qwerty@123")
    time.sleep(2)
    lp.click_loginup()
    time.sleep(2)
    text = lp.check_username()
    print(text)



def test_inVaild_login_user(driver):
    lp  = LoginPage(driver)
    lp.click_login_signUp()
    text = lp.check_login_text()
    print(text.__contains__("Login to your account"))
    lp.enter_email("gm@gmail.com")
    time.sleep(2)
    lp.enter_password("gahsdgajj")
    time.sleep(2)
    lp.click_loginup()
    time.sleep(2)
    text = lp.check_status()
    print(text)
