import pytest
from selenium import webdriver
from lab_session.pages.loginpage import LoginPage
from lab_session.pages.addtocartpage import AddCartPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    time.sleep(4)

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    yield driver
    time.sleep(4)

def test_add_item_to_cart(logged_in_driver):
    cart_page = AddCartPage(logged_in_driver)
    cart_page.add_item_to_cart()
    cart_page.open_cart()
    assert "cart.html" in logged_in_driver.current_url
    time.sleep(4)

def test_checkout_process(logged_in_driver):
    cart_page = AddCartPage(logged_in_driver)
    cart_page.add_item_to_cart()
    cart_page.open_cart()
    cart_page.proceed_to_checkout("Manish", "Singh", "560079")
    assert "checkout-complete.html" in logged_in_driver.current_url
    time.sleep(4)
