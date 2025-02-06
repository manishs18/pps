'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from labSession_seleniumProject.myApp.lab_sessionAuthenticationValidation import login, add_item_to_cart  # Absolute import

@pytest.fixture(scope="function")
def setup_driver():
    """Fixture to initialize and close WebDriver."""
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.smoke
@pytest.mark.regression
def test_add_to_cart(setup_driver):
    """Test adding an item to the cart."""
    driver = setup_driver
    try:
        login(driver)
        add_item_to_cart(driver)
        
        # Check if the item is in the cart by verifying the cart item count
        cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart.click()
        
        cart_count = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        assert cart_count == "1", f"Expected cart count to be '1', but got {cart_count}."
    except Exception as e:
        pytest.fail(f"Test failed due to: {e}")
'''