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

def test_check_testcase_navigation(driver):
    hp = HomePage(driver)
    hp.click_TestCase()
    text = hp.check_Navigate()
    assert text.__contains__("TEST") == True

