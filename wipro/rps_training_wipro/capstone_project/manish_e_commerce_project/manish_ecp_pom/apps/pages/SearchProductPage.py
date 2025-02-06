from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage

class SearchProduct(BasePage):
    PRODUCT_BTN = (By.XPATH, "(//a[@href='/products'])[1]")
    SEARCH_PRODUCT = (By.XPATH, "//input[@id='search_product']")
    # FANCY_GREEN_TOP = (By.XPATH, "(//p[contains(text(),'Fancy Green Top')])[2]")
    SUBMIT_SEARCH = (By.XPATH, "//button[@id='submit_search']")
    FANCY_GREEN_TOP = (By.LINK_TEXT, "Add to cart")

    def click_search_products(self, search):
        self.click(*self.PRODUCT_BTN)
        self.send_keys(*self.SEARCH_PRODUCT, search)
        self.click(*self.SUBMIT_SEARCH)
        self.driver.execute_script("window.scrollBy(0, 400)")

    def add_cart_product(self):
        self.click(*self.FANCY_GREEN_TOP)
