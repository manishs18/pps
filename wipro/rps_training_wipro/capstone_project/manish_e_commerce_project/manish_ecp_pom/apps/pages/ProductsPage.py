import time

from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage


class Products(BasePage):
    PRODUCT_BTN = (By.XPATH, "(//a[@href='/products'])[1]")
    VIEW_PRODUCT = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    QUANTITY = (By.XPATH, "//button[normalize-space()='2']")

    WRITE_YOUR_REVIEW = (By.XPATH, "//a[normalize-space()='Write Your Review']")
    YOUR_NAME = (By.XPATH, "//input[@id='name']")
    YOUR_EMAIL = (By.XPATH, "//input[@id='email']")
    REVIEW = (By.XPATH, "//textarea[@id='review']")
    SUBMIT_BTN = (By.XPATH, "//button[@id='button-review']")


    def click_products(self):
        self.click(*self.PRODUCT_BTN)
        time.sleep(2)
        self.click(*self.VIEW_PRODUCT)

    def click_add_product(self):
        self.click(*self.PRODUCT_BTN)

    def quantity(self):
        self.click(*self.QUANTITY)

    def write_review(self, name, email, review):
        self.click(*self.WRITE_YOUR_REVIEW)
        self.send_keys(*self.YOUR_NAME, name)
        self.send_keys(*self.YOUR_EMAIL, email)
        self.send_keys(*self.REVIEW, review)
        self.click(*self.SUBMIT_BTN)


