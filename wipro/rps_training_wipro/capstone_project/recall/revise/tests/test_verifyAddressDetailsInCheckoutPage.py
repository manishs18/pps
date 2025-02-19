from revise.pages.registerPage import RegisterPage
from revise.pages.verifyAllProductsnDetailsPage import VerifyProductsnDetails
from revise.pages.addProductsInCart import AddToCart
from revise.pages.placeOrderRegisterWhileCheckout import ProceedPlaceOrder
import time



def test_verfiy_address_details_in_checkout_page(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()
    home_page_btn.signUp_login_btns()
    home_page_btn.sign_up("manishhhs188800", "manishhhs188800@gmail.com")
    time.sleep(2)
    home_page_btn.signUp_details("manishhhs188800@123", "manishhssssss", "Singhshsssss", "wiprob1, noida, sector62", "wiprob2, banglore, sarjapur", "Bihar", "gpg", "841405", "6283526137")
    time.sleep(3)
    home_page_btn.click_continue_btn()
    home_page_btn.verfiy_logged_with_usernames_id()

    add_product_in_cart = AddToCart(driver)
    add_product_in_cart.add_to_cart()
    add_product_in_cart.verify_products_added_to_cart()

    proceed_checkout_verfiy_address = ProceedPlaceOrder(driver)
    proceed_checkout_verfiy_address.click_proceed_checkout()
    proceed_checkout_verfiy_address.verify_review_addressdetails_n_order()
    # proceed_order.verify_account_deleted()