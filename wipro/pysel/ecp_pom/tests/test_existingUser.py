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

    home_page = HomePage(driver)
    expected_title = "Automation Exercise"
    # Validate the title
    assert home_page.check_HomePage(), (
        f"Expected title '{expected_title}', but got '{home_page.get_page_title()}'"
    )
    home_page.click_login_signUp()
    expected_title = "Automation Exercise"
    # Validate the title
    assert home_page.check_HomePage(), (
        f"Expected title '{expected_title}', but got '{home_page.get_page_title()}'"
    )
    time.sleep(4)
    home_page.click_login_signUp()
    time.sleep(3)
    text = home_page.check_sigUptext()
    expected_text = "New User Signup!"
    if text == expected_text:
        print(f"Getting Expected Output {expected_text}")
    else:
        print("Different output")

    home_page.enter_signUpname("Prakhar")
    time.sleep(4)
    home_page.enter_signUpemail("wipro@gmail.com")
    time.sleep(4)
    home_page.click_signUp()
    text = home_page.check_existUser()
    if text.__contains__("exist"):
        print("User Already Registered")
