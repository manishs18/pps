from revise.pages.registerPage import RegisterPage
from revise.pages.addProductsInCart import AddToCart



def test_add_to_cart_product(driver):
    signup_btn = RegisterPage(driver)
    signup_btn.verify_home_page()

    addtocart = AddToCart(driver)
    addtocart.clickProductBtn()
    addtocart.add_to_cart()
    addtocart.verify_products_added_to_cart()