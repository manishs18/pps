from revise.pages.registerPage import RegisterPage
from revise.pages.verifySubscriptionOnHomePage import VerifySubscription
import time


def test_verify_subscription_on_homePage(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()

    verify_subscription = VerifySubscription(driver)
    verify_subscription.scroll_down_footer()
    verify_subscription.verify_subscription_on_homepage("manishs@gmail.com")


def test_verify_subscription_on_cartPage(driver):
    home_page_btn = RegisterPage(driver)
    home_page_btn.verify_home_page()

    verify_subscription = VerifySubscription(driver)
    verify_subscription.verify_subscription_on_cartpage("manishs@gmail.com")