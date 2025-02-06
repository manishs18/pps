from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage

class Subscription(BasePage):
    SUBSCRIPTION = (By.XPATH, "//h2[normalize-space()='Subscription']")
    SUB_EMAIL = (By.XPATH, "//input[@id='susbscribe_email']")
    ARROW_BTN = (By.XPATH, "//i[@class='fa fa-arrow-circle-o-right']")

    def move_to_subscription(self, email):
        self.send_keys(*self.SUB_EMAIL, email)
        self.click(*self.ARROW_BTN)

