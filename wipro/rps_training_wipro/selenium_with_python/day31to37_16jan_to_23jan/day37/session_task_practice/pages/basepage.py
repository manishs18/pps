from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by, locator):
        # Corrected to pass a single tuple
        return self.wait.until(EC.visibility_of_element_located((by, locator)))
    
    def click(self, by, locator):
        element = self.wait_for_element(by, locator)
        element.click()
    
    def send_keys(self, by, locator, text):
        element = self.wait_for_element(by, locator)
        element.clear()
        element.send_keys(text)
