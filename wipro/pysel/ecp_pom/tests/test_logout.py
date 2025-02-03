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

def test_logout_user(driver):
    lp = LoginPage(driver)
    home_page = HomePage(driver)
    expected_title = "Automation Exercise"
    # Validate the title
    assert home_page.check_HomePage(), (
        f"Expected title '{expected_title}', but got '{home_page.get_page_title()}'"
    )
    lp.click_login_signUp()
    text = lp.check_login_text()
    text.__contains__("Login to your account")
    lp.enter_email("wipro@gmail.com")
    time.sleep(2)
    lp.enter_password("qwerty@123")
    time.sleep(2)
    lp.click_loginup()
    time.sleep(2)
    text = lp.check_username()
    print(text.__contains__("Prakhar"))
    lp.click_logout()
    time.sleep(2)



