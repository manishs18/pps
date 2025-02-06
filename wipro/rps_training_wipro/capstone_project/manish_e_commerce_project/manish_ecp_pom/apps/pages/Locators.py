from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage


class Locators(BasePage):
    CART_QUANTITY_DELETE = (By.XPATH, "//a[@class='cart_quantity_delete']")
    LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[contains(text(),'Account Deleted!')]")

    TESTCASES_BTN = (By.XPATH, "//a[contains(text(),'Test Cases')]")

    def click_cart_quantity_delete(self):
        self.click(*self.CART_QUANTITY_DELETE)

    def click_logout(self):
        self.click(*self.LOGOUT)

    def verify_account_deleted_visible(self):
        assert self.driver.find_element(*self.ACCOUNT_DELETED_TEXT).is_displayed(), "'Account Deleted!' is not visible."

    def click_testcases_btn(self):
        self.click(*self.TESTCASES_BTN)
