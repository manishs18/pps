import pytest
import time
import random
import string
from manish_ecp_pom.apps.pages.HomePage import HomePage
from manish_ecp_pom.apps.pages.RegisterPage import RegisterPage
from manish_ecp_pom.apps.pages.ProductsPage import Products


random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
dynamic_username = f"{random_suffix}"
dynamic_email = f"{random_suffix}@example.com"

@pytest.mark.usefixtures("driver")
def test_add_products(driver):
    home_page = HomePage(driver)
    time.sleep(2)
    register_page = RegisterPage(driver)
    time.sleep(2)

    register_page.click_signin_btn()
    time.sleep(2)

    register_page.verify_home_page_visible()

    register_page.enter_signup(dynamic_username, dynamic_email)
    time.sleep(2)

    # Details of user
    register_page.enter_details("manish111", "Jhon", "Mark", "Canada",
                                "Canada", "Canada", "Canada", "123456", "123695487")
    time.sleep(2)

    register_page.click_continue()
    time.sleep(2)

    product_page = Products(driver)
    product_page.click_add_product()
    time.sleep(2)

    # Add products to cart
    home_page.click_panda_shirt()
    time.sleep(3)
    home_page.click_continue_shopping()
    time.sleep(2)
    home_page.click_cart()

    home_page.proceed_to_cart()
    time.sleep(2)

    # Delete Account
    register_page.delete_account()
    time.sleep(2)





