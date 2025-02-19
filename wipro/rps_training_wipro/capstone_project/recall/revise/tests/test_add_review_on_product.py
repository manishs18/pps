from revise.pages.registerPage import RegisterPage
from revise.pages.addProductsInCart import AddToCart
from revise.pages.verifyAllProductsnDetailsPage import VerifyProductsnDetails
from revise.pages.loginPage import LoginPage


def test_add_review_on_product(driver):
    verify_product = VerifyProductsnDetails(driver)
    verify_product.clickProductBtn()
    verify_product.verfiyOnProductsPages()
    verify_product.clickFirstProduct()
    verify_product.verfiy_write_review_text()
    verify_product.fill_review_from("Manish Kumar Singh", "manish18@gmail.com", "blue top is not good my gf is said not interested towards this product colour and quality")