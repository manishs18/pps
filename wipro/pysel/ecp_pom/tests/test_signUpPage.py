import time

import pytest
from selenium import webdriver
from ecp_pom.apps.homePage import HomePage


@pytest.fixture()
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://www.automationexercise.com/')
    yield driver
    driver.quit()


def test_home_page(driver):
    home_page = HomePage(driver)
    expected_title = "Automation Exercise"
    # Validate the title
    assert home_page.check_HomePage(), (
        f"Expected title '{expected_title}', but got '{home_page.get_page_title()}'"
    )
    # home_page = HomePage(driver)
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
    home_page.enter_signUpemail("adass@gmail.com")
    time.sleep(4)
    home_page.click_signUp()
    time.sleep(3)
    text = home_page.check_accountinfo()
    assert text == "ENTER ACCOUNT INFORMATION"
    time.sleep(3)
    home_page.click_radio()
    time.sleep(3)
    home_page.enter_password('qwerty@123')
    time.sleep(3)
    home_page.enter_date("11")
    time.sleep(1)
    home_page.enter_month("June")
    time.sleep(1)
    home_page.enter_year("2013")
    time.sleep(4)
    home_page.click_checkbox()
    time.sleep(3)
    home_page.enter_accountdetails("Prakhar","Gupta","Wipro","BTMLayout,Banglore","KT","Banglaore","234312","9848532324")
    time.sleep(4)
    text = home_page.check_acc_create()
    assert "ACCOUNT CREATED!" == text
    home_page.click_continue()
    time.sleep(5)
    text = home_page.check_username()
    print(text)
    time.sleep(4)
    home_page.click_delete()
    text = home_page.check_deletestatus()
    print(text)
