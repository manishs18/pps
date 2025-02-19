from revise.pages.registerPage import RegisterPage
from revise.pages.addProductsInCart import AddToCart
from revise.pages.placeOrderRegisterWhileCheckout import ProceedPlaceOrder
from revise.pages.loginPage import LoginPage
import time


def test_remove_product_from_cart(driver):
    signup_btn = RegisterPage(driver)
    signup_btn.verify_home_page()

    place_order = AddToCart(driver)
    place_order.clickProductBtn()
    place_order.add_to_cart()
    place_order.verify_products_added_to_cart()
    place_order.remove_product_from_cart()
    place_order.verify_cart_empty()

