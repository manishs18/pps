from revise.pages.registerPage import RegisterPage
from revise.pages.verifyProductQuantityInCart import VerifyProductOnCart
import time


def test_verify_product_quantity_on_cart(driver):
    home_page_btn = RegisterPage(driver)
    time.sleep(2)
    home_page_btn.verify_home_page()
    
    verify_cart_product = VerifyProductOnCart(driver)
    time.sleep(2)
    verify_cart_product.verify_product_opened()
    time.sleep(2)
    verify_cart_product.verify_product_details()
    time.sleep(2)
    verify_cart_product.verify_product_dispaly_on_cart()