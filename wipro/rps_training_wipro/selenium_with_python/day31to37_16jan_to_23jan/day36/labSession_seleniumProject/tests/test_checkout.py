'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from labSession_seleniumProject.myApp.lab_sessionAuthenticationValidation import login, add_item_to_cart, checkout  # Absolute import

@pytest.fixture(scope="function")
def setup_driver():
    """Fixture to initialize and close WebDriver."""
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.sanity
def test_checkout_process(setup_driver):
    """Test the checkout process."""
    driver = setup_driver
    try:
        login(driver)
        add_item_to_cart(driver)
        checkout(driver, firstname="Manish", lastname="Shrestha", postalcode="123564")
        
        # Check if the order is confirmed by looking for a confirmation message or element
        confirmation_message = driver.find_element(By.XPATH, "//h2[contains(text(), 'THANK YOU FOR YOUR ORDER')]")
        assert confirmation_message.is_displayed(), "Checkout process failed. Confirmation message not displayed."
    except Exception as e:
        pytest.fail(f"Test failed due to: {e}")
'''