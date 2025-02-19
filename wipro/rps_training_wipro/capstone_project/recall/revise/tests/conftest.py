from selenium import webdriver
import time
import pytest


@pytest.fixture
def driver():
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    yield driver
    driver.quit()
