from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CSS_SELECTOR, "body > header:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")

    def click_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        ).click()
        print("Navigated to the Cart page")

    def scroll_to_footer(self):
        footer = self.driver.find_element(By.XPATH, "//footer[@id='footer']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)

    def verify_subscription_text(self):
        subscription_text = self.driver.find_element(By.XPATH, "//input[@id='susbscribe_email']")
        assert subscription_text.is_displayed(), "Subscription text not found in footer"
        print("Subscription text found in footer")

    def enter_email_and_subscribe(self, email):
        email_input = self.driver.find_element(By.ID, "susbscribe_email")
        email_input.send_keys(email)
        email_input.submit()
