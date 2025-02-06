import time

from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage

class Brand(BasePage):
    POLO = (By.XPATH, "//a[@href='/brand_products/Polo']")
    BABYHUG = (By.XPATH, "//a[@href='/brand_products/Babyhug']")


    def click_brand(self):
        self.click(*self.POLO)
        time.sleep(2)
        self.click(*self.BABYHUG)
