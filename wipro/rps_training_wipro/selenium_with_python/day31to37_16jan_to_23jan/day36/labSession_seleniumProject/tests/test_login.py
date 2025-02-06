import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Fixture to initialize and close WebDriver for each test
@pytest.fixture(scope="function")
def setup_driver():
    """Fixture to initialize and close WebDriver."""
    # Set up Edge browser options
    options = webdriver.EdgeOptions()
    # Initialize the WebDriver for Edge
    driver = webdriver.Edge(options=options)
    driver.maximize_window()  
    yield driver 
    driver.quit()  
    time.sleep(4)

# Smoke and Regression test to login and add item to the cart
@pytest.mark.smoke
@pytest.mark.regression
def test_login_and_add_to_cart(setup_driver):
    """Test login and adding item to cart."""
    driver = setup_driver  # Get the driver instance from the fixture
    driver.get('https://www.saucedemo.com/')  

    # Wait until the username field is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user-name")))
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("standard_user")  

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce") 

    login = driver.find_element(By.NAME, "login-button")
    login.click()  
    time.sleep(4)

    # Wait until the "add-to-cart" button is visible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "add-to-cart-sauce-labs-backpack")))
    addCart = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
    addCart.click()  # Add the item to the cart
    time.sleep(2)

    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()  # Navigate to the cart
    time.sleep(2)

    # Assert that the cart contains 1 item
    assert "1" in driver.page_source, "Item was not added to the cart"

# Sanity test for the checkout process
@pytest.mark.sanity
def test_checkout_process(setup_driver):
    """Test the checkout process after adding an item to the cart."""
    driver = setup_driver  # Get the driver instance from the fixture
    driver.get('https://www.saucedemo.com/') 

    # Login process
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("standard_user") 

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce") 

    login = driver.find_element(By.NAME, "login-button")
    login.click() 
    time.sleep(4)

    # Add item to cart
    addCart = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
    addCart.click()
    time.sleep(2)

    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()  # Navigate to the cart
    time.sleep(2)

    # Proceed to checkout
    checkout = driver.find_element(By.NAME, "checkout")
    checkout.click()
    time.sleep(2)

    # Enter checkout details
    firstname = driver.find_element(By.NAME, "firstName")
    firstname.send_keys("Manish")

    lastname = driver.find_element(By.NAME, "lastName")
    lastname.send_keys("Shrestha")

    postalcode = driver.find_element(By.NAME, "postalCode")
    postalcode.send_keys("123564")

    cont = driver.find_element(By.XPATH, "//input[@id='continue']")
    cont.click()  
    time.sleep(2)

    finish = driver.find_element(By.NAME, "finish")
    finish.click()  
    time.sleep(2)

    # Wait for the "Thank you for your order!" message and verify it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Thank you for your order!']")))
    assert "Thank you for your order!" in driver.page_source, "Checkout process failed"
    time.sleep(2)

# Test to demonstrate skipping functionality in pytest
@pytest.mark.skipif(True, reason="Skipping for demonstration")
def test_skipped_case():
    """Test case to demonstrate skipping functionality."""
    assert False, "This test is skipped." 

time.sleep(4)
# Parallel execution test 1
@pytest.mark.parallel
def test_parallel_case_1(setup_driver):
    """Test case for parallel execution example 1."""
    driver = setup_driver  
    driver.get('https://www.saucedemo.com/')  
    assert "Swag Labs" in driver.title  

time.sleep(4)
# Parallel execution test 2
@pytest.mark.parallel
def test_parallel_case_2(setup_driver):
    """Test case for parallel execution example 2."""
    driver = setup_driver  
    driver.get('https://www.saucedemo.com/')  
    assert "Swag Labs" in driver.title 

time.sleep(4)
# Smoke test for error handling when a non-existent element is searched
@pytest.mark.smoke
def test_error_handling(setup_driver):
    """Test error handling for non-existent elements."""
    driver = setup_driver  
    driver.get('https://www.saucedemo.com/') 
    try:
        # Attempt to find a non-existent element
        non_existent_element = driver.find_element(By.NAME, "non-existent")
    except NoSuchElementException as e:
        print(f"Error encountered: {str(e)}")  # Log the error
        assert "Unable to locate element" in str(e)  # Assert that the error message is correct


























































''' import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from labSession_seleniumProject.myApp.lab_sessionAuthenticationValidation import login, add_item_to_cart  # Absolute Import

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
def test_login(setup_driver):
    """Test for logging in."""
    driver = setup_driver
    login(driver)
    # Check if login was successful
    assert "Swag Labs" in driver.title, "Login failed"
'''






































'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Fixture for setting up and tearing down the WebDriver
@pytest.fixture(scope="module")
def setup_driver():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)  # Replace with actual path
    driver.maximize_window()
    yield driver  # Yield the driver to the test function
    driver.quit()


# Test Group 1: Smoke Tests
@pytest.mark.smoke
@pytest.mark.basic
def test_open_page(setup_driver):
    """Test opening the website."""
    driver = setup_driver
    driver.get('https://ogmt.koyeb.app/')
    time.sleep(2)
    assert "OGMT" in driver.title  # Replace with actual title


@pytest.mark.smoke
@pytest.mark.basic
def test_login_page_navigation(setup_driver):
    """Test navigating to the login page."""
    driver = setup_driver
    driver.get('https://ogmt.koyeb.app/')
    signin = driver.find_element(By.XPATH, '//button[@class="btn btn-primary mx-1"]')
    signin.click()
    time.sleep(2)
    assert "Login" in driver.page_source


# Test Group 2: Regression Tests
@pytest.mark.regression
def test_valid_login(setup_driver):
    """Test successful login with valid credentials."""
    driver = setup_driver
    driver.get('https://ogmt.koyeb.app/')
    signin = driver.find_element(By.XPATH, '//button[@class="btn btn-primary mx-1"]')
    signin.click()
    time.sleep(2)

    username = driver.find_element(By.ID, "loginusername")
    username.send_keys("mkuma")

    password = driver.find_element(By.ID, "loginpassword")
    password.send_keys("admin123")

    submit = driver.find_element(By.ID, "gridCheck1")
    submit.click()
    time.sleep(2)

    login = driver.find_element(By.XPATH, '//button[@class="btn btn-success"]')
    login.click()
    time.sleep(3)

    assert "Login" in driver.page_source  # Replace with actual post-login validation


# Test Group 3: Skip Test
@pytest.mark.skip(reason="Feature not implemented yet.")
def test_feature_to_be_skipped():
    """This test is skipped intentionally."""
    pass


# Test Group 4: Test with Conditional Skip
@pytest.mark.skipif("some_condition", reason="Skipping due to condition.")
def test_skip_due_to_condition():
    """Test skipped due to condition."""
    assert True




# Test Group 5: Additional Test with Grouping
@pytest.mark.sanity
@pytest.mark.regression
def test_logout_functionality(setup_driver):
    """Test logout functionality."""
    driver = setup_driver
    driver.get('https://ogmt.koyeb.app/')
    signin = driver.find_element(By.XPATH, '//button[@class="btn btn-primary mx-1"]')
    signin.click()
    time.sleep(2)

    username = driver.find_element(By.ID, "loginusername")
    username.send_keys("mkuma")

    password = driver.find_element(By.ID, "loginpassword")
    password.send_keys("admin123")

    submit = driver.find_element(By.ID, "gridCheck1")
    submit.click()
    time.sleep(2)

    login = driver.find_element(By.XPATH, '//button[@class="btn btn-success"]')
    login.click()
    time.sleep(3)

    assert "https://ogmt.koyeb.app/userlogin" in driver.page_source  # Replace with actual post-login validation

    # Logout
    logout_button = driver.find_element(By.ID, "logout")
    logout_button.click()
    time.sleep(2)
    assert "Login" in driver.page_source  # Replace with actual post-logout validation


# Test with Grouping and Parallel Execution (using pytest-xdist)
@pytest.mark.sanity
@pytest.mark.regression
def test_sanity_and_regression(setup_driver):
    """Test both sanity and regression groupings."""
    driver = setup_driver
    driver.get('https://ogmt.koyeb.app/')
    time.sleep(2)
    assert "OGMT" in driver.title
    driver.quit()


@pytest.mark.skip
def test_valid_login(auth_validation):
    """Test valid login."""
    auth_validation.open_app("https://ogmt.koyeb.app/")

    # Perform login
    auth_validation.login(username="mkuma", password="admin123")

    # Assert that login was successful
    assert auth_validation.is_logged_in(), "Login failed or post-login validation failed."
'''