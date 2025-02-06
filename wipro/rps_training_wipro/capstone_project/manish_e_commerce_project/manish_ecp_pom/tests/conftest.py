import pytest
import time
from selenium import webdriver

@pytest.fixture
def driver():
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    yield driver

    driver.quit()