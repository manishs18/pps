import time

from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage

class ViewCategory(BasePage):
    WOMEN_CATEGORY = (By.XPATH, "//a[normalize-space()='Women']")
    DRESS = (By.XPATH, "(//a[contains(text(),'Dress')])[1]")
    MEN_CATEGORY = (By.XPATH, "//a[normalize-space()='Men']")
    TSHIRTS = (By.XPATH, "//a[normalize-space()='Tshirts']")


    def women_category(self):
        self.click(*self.WOMEN_CATEGORY)
        time.sleep(2)
        self.click(*self.DRESS)

    def men_category(self):
        self.click(*self.MEN_CATEGORY)
        self.click(*self.TSHIRTS)

