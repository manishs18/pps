import pytest
from selenium import webdriver
from lab_session.pages.basepage import BasePage
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    time.sleep(4)

def test_open_url(driver):
    base_page = BasePage(driver)
    base_page.open_url("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/"
    time.sleep(4)
