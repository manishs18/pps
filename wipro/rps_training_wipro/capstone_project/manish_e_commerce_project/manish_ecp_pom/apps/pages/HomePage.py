from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage

class HomePage(BasePage):

    # locators for Home page, Add products to cart
    ADD_PANDA_SHIRT = (By.LINK_TEXT, "Add to cart")
    CONTINUE_SHOPPING = (By.XPATH, "//button[normalize-space()='Continue Shopping']")
    CART = (By.LINK_TEXT, "Cart")
    PROCEED_TO_CART = (By.XPATH, "//a[normalize-space()='Proceed To Checkout']")
    REGISTER_LOGIN = (By.XPATH, "//u[normalize-space()='Register / Login']")

    # methods or the page actions on the Add products to cart
    def click_panda_shirt(self):
        self.click(*self.ADD_PANDA_SHIRT)

    def click_continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)

    def click_cart(self):
        self.click(*self.CART)

    def proceed_to_cart(self):
        self.click(*self.PROCEED_TO_CART)

    def click_register_login(self):
        self.click(*self.REGISTER_LOGIN)



