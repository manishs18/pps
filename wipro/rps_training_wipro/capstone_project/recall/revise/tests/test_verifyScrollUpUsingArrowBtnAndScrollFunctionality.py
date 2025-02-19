from revise.pages.registerPage import RegisterPage
from revise.pages.verifyAllProductsnDetailsPage import VerifyProductsnDetails
from revise.pages.verifySubscriptionOnHomePage import VerifySubscription
import time


def test_verfiy_products_details_on_page(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()

    verify_subscription = VerifySubscription(driver)
    verify_subscription.scroll_down_footer()
    verify_subscription.verify_subs_fledge_text_using_arrow_btn()