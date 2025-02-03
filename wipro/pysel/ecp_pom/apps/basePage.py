from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self,by,locator):
        return self.wait.until(EC.visibility_of_element_located((by,locator)))

    def click(self,by,locator):
        element = self.wait_for_element(by,locator)
        element.click()

    def send_keys(self,by,locator,text):
        element = self.wait_for_element(by,locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        return self.wait_for_element(locator, timeout).text

    def get_page_title(self):
        return self.driver.title

    def get_dropdown(self, by, locator):
            dropdown_element = self.wait_for_element(by, locator)
            return Select(dropdown_element)

    def find_elements(self, by, locator, timeout=10):
        return self.wait.until(
            EC.presence_of_all_elements_located((by, locator)))




























































# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver


# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver

#     def open_url(self, url):
#         self.driver.get(url)

#     def find_element(self, locator, timeout=10):
#         return WebDriverWait(self.driver, timeout).until(
#             EC.presence_of_element_located(locator)
#         )

#     def wait_for_element(self, locator, timeout=10):
#         return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

#     def click(self, locator):
#         """Click on an element identified by a locator tuple."""
#         element = self.wait_for_element(locator)
#         element.click()

#     def click_element(self, locator, timeout=10):
#         element = self.find_element(locator, timeout)
#         element.click()

#     def enter_text(self, locator, text):
#         """Enter text into an input field identified by a locator tuple."""
#         element = self.wait_for_element(locator)
#         element.clear()
#         element.send_keys(text)

#     def enter_text(self, locator, text, timeout=10):
#         element = self.find_element(locator, timeout)
#         element.send_keys(text)

#     def get_dropdown(self, locator):
#         """Retrieve a dropdown element."""
#         return self.wait_for_element(locator)

#     def get_text(self, locator, timeout=10):
#         """Get text from an element."""
#         return self.wait_for_element(locator, timeout).text
    
