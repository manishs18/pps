from revise.pages.registerPage import RegisterPage
from revise.pages.verifyAllProductsnDetailsPage import VerifyProductsnDetails
from revise.pages.addProductsInCart import AddToCart
from revise.pages.placeOrderRegisterWhileCheckout import ProceedPlaceOrder
import time



def test_download_invoice_after_purchase_order(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()

    add_product_in_cart = AddToCart(driver)
    add_product_in_cart.add_to_cart()
    add_product_in_cart.verify_products_added_to_cart()

    proceed_order = ProceedPlaceOrder(driver)
    proceed_order.click_proceed_checkout()
    proceed_order.click_register_login()

    home_page_btn.sign_up("manishhhhsss180", "manishhhhsss180@gmail.com")
    time.sleep(2)
    home_page_btn.signUp_details("manishhhhsss180@123", "manishhssss", "Singhshsss", "wiprob1, noida, sector62", "wiprob2, banglore, sarjapur", "Bihar", "gpg", "841405", "6283526137")
    time.sleep(3)

    home_page_btn.click_continue_btn()
    home_page_btn.verfiy_logged_with_username()

    proceed_order.click_cart_btn()
    proceed_order.click_proceed_checkout()
    proceed_order.verify_review_addressdetails_n_order()
    proceed_order.comment_n_place_order("manish continuosly doing order from your platform due to reason platfrom providing good product")
    proceed_order.payment_details("manish singh", '123456789987', '123', '03', '2028')
    proceed_order.verify_order_placed_successfully()
    proceed_order.download_invoice()
    proceed_order.click_continue_btn()
    # proceed_order.verify_account_deleted()