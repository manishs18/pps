from revise.pages.registerPage import RegisterPage
from revise.pages.verifySubscriptionOnHomePage import VerifySubscription
import time


def test_verfiy_products_details_on_page(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()

    verify_subscription = VerifySubscription(driver)
    time.sleep(3)
    verify_subscription.scroll_down_footer()
    time.sleep(3)
    verify_subscription.verify_subs_text_without_arrow_btn()
    time.sleep(3)
    verify_subscription.scroll_up()
    time.sleep(3)
    verify_subscription.verify_fledge_text_without_arrow_btn()
    time.sleep(3)