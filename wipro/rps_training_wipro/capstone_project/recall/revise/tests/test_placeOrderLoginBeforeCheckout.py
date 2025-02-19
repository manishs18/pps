from revise.pages.registerPage import RegisterPage
from revise.pages.addProductsInCart import AddToCart
from revise.pages.placeOrderRegisterWhileCheckout import ProceedPlaceOrder
from revise.pages.loginPage import LoginPage
import time


def test_place_order_login_before_checkout(driver):
    signup_btn = RegisterPage(driver)
    signup_btn.verify_home_page()
    signup_btn.signUp_login_btns()

    verify_logged_username = LoginPage(driver)
    verify_logged_username.login_with_credentials("manish18@gmail.com", "manish18@123")
    verify_logged_username.verify_loggedIn_with_username()

    place_order = AddToCart(driver)
    place_order.clickProductBtn()
    place_order.add_to_cart()
    place_order.verify_products_added_to_cart()

    proceed_order = ProceedPlaceOrder(driver)
    proceed_order.click_proceed_checkout()
    # proceed_order.click_register_login()

    # proceed_order.click_cart_btn()
    # proceed_order.click_proceed_checkout()
    proceed_order.verify_review_addressdetails_n_order()
    proceed_order.comment_n_place_order("manish continuosly doing order from your platform due to reason platfrom providing good product")
    proceed_order.payment_details("manish singh", '123456789987', '123', '03', '2028')
    proceed_order.verify_order_placed_successfully()
