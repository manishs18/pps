import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Initialize the WebDriver instance
    driver = webdriver.Edge()  # Use Edge browser
    driver.maximize_window()
    yield driver  # Provide the driver instance to the test
    driver.quit()  # Quit the driver after the test
