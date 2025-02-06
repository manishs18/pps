from selenium.webdriver.common.by import By
from lab_session.pages.basepage import BasePage

class AddCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.NAME, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.checkout_button = (By.NAME, "checkout")
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.postal_code_field = (By.NAME, "postalCode")
        self.continue_button = (By.XPATH, "//input[@id='continue']")
        self.finish_button = (By.NAME, "finish")

    def add_item_to_cart(self):
        self.click_element(self.add_to_cart_button)

    def open_cart(self):
        self.click_element(self.cart_icon)

    def proceed_to_checkout(self, first_name, last_name, postal_code):
        self.click_element(self.checkout_button)
        self.enter_text(self.first_name_field, first_name)
        self.enter_text(self.last_name_field, last_name)
        self.enter_text(self.postal_code_field, postal_code)
        self.click_element(self.continue_button)
        self.click_element(self.finish_button)
