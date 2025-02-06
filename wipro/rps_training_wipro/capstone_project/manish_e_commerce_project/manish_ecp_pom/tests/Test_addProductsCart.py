import pytest
import time
import random
import string
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage


random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
dynamic_username = f"{random_suffix}"
dynamic_email = f"{random_suffix}@example.com"

@pytest.mark.usefixtures("driver")
def test_add_products(driver):
    home_page = HomePage(driver)
    time.sleep(2)

    # Add products to cart
    driver.execute_script("window.scrollBy(0, 1000)")
    home_page.click_panda_shirt()
    time.sleep(3)
    home_page.click_continue_shopping()
    time.sleep(2)
    driver.execute_script("window.scrollBy(1000, 0)")
    home_page.click_cart()

    # Checking the Cart for checkout
    time.sleep(2)
    home_page.proceed_to_cart()
    time.sleep(2)
    home_page.click_register_login()
    time.sleep(2)

    # Signup
    register_page = RegisterPage(driver)
    time.sleep(2)
    register_page.enter_signup(dynamic_username, dynamic_email)
    time.sleep(2)

    # Details of user
    register_page.enter_details("manish111", "Manish", "Singhh", "",
                                "India", "India", "India", "654321", "7654321")
    # # Details of user
    # register_page.enter_details("jhon@27", "Jhon", "Mark", "Canada",
    #                             "Canada", "Canada", "Canada", "123456", "123695487")
    time.sleep(2)
    register_page.click_continue()
    time.sleep(2)

    home_page.click_cart()
    time.sleep(2)

    home_page.proceed_to_cart()
    time.sleep(2)

    register_page.place_order()
    time.sleep(2)

    # register_page.continue_on_cart()
    # time.sleep(2)

    # login
    # register_page.enter_login("jhon123@gmail.com", "jhon@27")
    # time.sleep(2)

    # payment
    register_page.enter_payment("Manish Singh","987654321123","987","01","2026")
    time.sleep(2)

    # Download invoice
    register_page.download_invoice()
    time.sleep(2)

    register_page.delete_account()
    time.sleep(2)





