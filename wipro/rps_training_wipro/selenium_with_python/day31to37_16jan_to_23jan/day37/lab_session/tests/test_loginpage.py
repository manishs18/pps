import pytest
from selenium import webdriver
from lab_session.pages.loginpage import LoginPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    time.sleep(4)

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    time.sleep(4)
