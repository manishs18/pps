from selenium.webdriver.common.by import By
from selenium import webdriver
from session_task_practice.pages.basepage import BasePage

class LoginPage(BasePage):

    # Locators for the login page
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Methods or the page actions on the login page
    def enter_username(self, username):
        self.send_keys(*self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys(*self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)