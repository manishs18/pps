from revise.pages.basePage import BasePage
from selenium.webdriver.common.by import By


class VerifyTestCasePage(BasePage):
    test_case_btn = (By.XPATH, "//a[normalize-space()='Test Cases']")
    verify_test_case_page = (By.XPATH, "//span[contains(text(),'Below is the list of')]")

    def  navigate_to_testCasePage(self):
        self.click(*self.test_case_btn)
    
    def verify_u_r_testCaePage(self):
        self.is_displayed(*self.verify_test_case_page)