from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def verify_home_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "slider"))
        )
        print("Home page is visible successfully")

    def scroll_to_footer(self):
        footer = self.driver.find_element(By.XPATH, "//footer[@id='footer']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)

    def verify_subscription_text(self):
        subscription_text = self.driver.find_element(By.XPATH, "//h2[text()='Subscription']")
        assert subscription_text.is_displayed(), "Subscription text not found in footer"
        print("Subscription text found in footer")

    def enter_email_and_subscribe(self, email):
        email_input = self.driver.find_element(By.ID, "susbscribe_email")
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)


