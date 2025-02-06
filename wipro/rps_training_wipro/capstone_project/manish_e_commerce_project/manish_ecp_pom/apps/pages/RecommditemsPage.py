import time
from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage

class RecommendedItems(BasePage):
    RECOMD_TEXT = (By.XPATH, "//h2[normalize-space()='recommended items']")
    TSHIRT = (By.XPATH, "(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[70]")

    def recommended_item(self):
        self.click(*self.RECOMD_TEXT)
        self.click(*self.TSHIRT)

