import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def driver():
    """Setup Selenium WebDriver"""
    driver = webdriver.Chrome()  # Replace with your WebDriver path/config
    yield driver
    driver.quit()

def test_homepage(driver):
    """Test homepage loads successfully"""
    url = "https://example.com"  # Replace with your target website
    driver.get(url)
    assert "Example Domain" in driver.title, "Homepage title did not match"

def test_login_functionality(driver):
    """Test login functionality"""
    url = "https://example.com/login"  # Replace with your login URL
    driver.get(url)
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("testpassword")
    driver.find_element(By.ID, "loginButton").click()
    assert "Dashboard" in driver.title, "Login failed or dashboard title mismatch"

def test_invalid_login(driver):
    """Test invalid login handling"""
    url = "https://example.com/login"  # Replace with your login URL
    driver.get(url)
    driver.find_element(By.ID, "username").send_keys("invaliduser")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "loginButton").click()
    error_message = driver.find_element(By.ID, "errorMessage").text
    assert "Invalid credentials" in error_message, "Error message did not display"
