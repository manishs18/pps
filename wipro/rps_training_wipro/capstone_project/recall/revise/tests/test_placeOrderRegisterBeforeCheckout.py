from revise.pages.registerPage import RegisterPage
from revise.pages.addProductsInCart import AddToCart
from revise.pages.placeOrderRegisterWhileCheckout import ProceedPlaceOrder
from revise.pages.loginPage import LoginPage
import time


def test_place_order_before_checkout(driver):
    signup_btn = RegisterPage(driver)
    signup_btn.verify_home_page()
    signup_btn.signUp_login_btns()
    signup_btn.sign_up("manishhss18000", "manishhss18000@gmail.com")
    time.sleep(2)
    signup_btn.signUp_details("manishhss18000@123", "manishhssss", "Singhshsss", "wiprob1, noida, sector62", "wiprob2, banglore, sarjapur", "Bihar", "gpg", "841405", "6283526137")
    time.sleep(3)
    
    verify_logged_username = LoginPage(driver)
    verify_logged_username.verify_loggedIn_with_username_id()

    place_order = AddToCart(driver)
    place_order.clickProductBtn()
    place_order.add_to_cart()
    place_order.verify_products_added_to_cart()

    proceed_order = ProceedPlaceOrder(driver)
    proceed_order.click_proceed_checkout()

    proceed_order.verify_review_addressdetails_n_order()
    proceed_order.comment_n_place_order("Manish continuosly doing order from your platform due to reason platfrom providing good product")
    proceed_order.payment_details("Manish Singh", '123456789987', '123', '03', '2028')
    proceed_order.verify_order_placed_successfully()
    # proceed_order.verify_account_deleted()
