from revise.pages.registerPage import RegisterPage
from revise.pages.verifyAllProductsnDetailsPage import VerifyProductsnDetails
import time


def test_search_product(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()

    verify_product = VerifyProductsnDetails(driver)
    verify_product.clickProductBtn()
    verify_product.verfiyOnProductsPages()
    verify_product.searchProduct("Blue Top")