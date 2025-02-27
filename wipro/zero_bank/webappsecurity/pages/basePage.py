from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def wait_for_element(self, by, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located((by, locator)))
        except TimeoutException:
            raise Exception(f"Element with locator '{locator}' and type '{by}' was not found within the timeout.")

    def click(self, by, locator):
        element = self.wait_for_element(by, locator)
        element.click()

    def send_keys(self, by, locator, text):
        element = self.wait_for_element(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        element = self.wait_for_element(by, locator)
        return element.text
    
    def get_dropdown(self, by, locator):
        dropdown_element = self.wait_for_element(by, locator)
        return Select(dropdown_element)
    
    def is_displayed(self, by, locator):  # Fixed method name
        try:
            element = self.wait_for_element(by, locator)
            return element.is_displayed()
        except Exception:
            return False