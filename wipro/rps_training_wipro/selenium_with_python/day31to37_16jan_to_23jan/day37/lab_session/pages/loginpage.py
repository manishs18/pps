from selenium.webdriver.common.by import By
from lab_session.pages.basepage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.NAME, "user-name")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.NAME, "login-button")

    def login(self, username, password):
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click_element(self.login_button)
