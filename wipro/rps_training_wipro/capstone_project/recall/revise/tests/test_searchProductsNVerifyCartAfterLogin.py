from revise.pages.registerPage import RegisterPage
from revise.pages.addProductsInCart import AddToCart
from revise.pages.verifyAllProductsnDetailsPage import VerifyProductsnDetails
from revise.pages.loginPage import LoginPage


def test_search_Products_n_verify_cart_after_login(driver):
    verify_product = VerifyProductsnDetails(driver)
    verify_product.clickProductBtn()
    verify_product.verfiyOnProductsPages()
    verify_product.searchProduct("Blue Top")
    click_add_to_cart = AddToCart(driver)
    click_add_to_cart.view_product1_btn()
    click_add_to_cart.add_to_cart_searched_product()
    click_add_to_cart.click_continue_shoping_btn()
    verify_product.clickProductBtn()
    verify_product.verfiyOnProductsPages()
    verify_product.searchProduct("Men Tshirt")
    click_add_to_cart.view_product2_btn()
    click_add_to_cart.add_to_cart_searched_product()
    click_add_to_cart.click_continue_shoping_btn()
    click_add_to_cart.click_cart_btn()
    click_add_to_cart.verify_products_added_to_cart()
    signup_btn = RegisterPage(driver)
    signup_btn.signUp_login_btns()
    login_btn = LoginPage(driver)
    login_btn.login_with_credentials("manish18@gmail.com", "manish18@123")
    click_add_to_cart.click_cart_btn()
    click_add_to_cart.verify_products_added_to_cart()
    click_add_to_cart.remove_product_from_cart()
    click_add_to_cart.verify_cart_empty()