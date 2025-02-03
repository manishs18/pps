from selenium.webdriver.common.by import By
from ecp_pom.apps.basePage import BasePage


class LoginPage(BasePage):
    Login_singupbutton = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    Logintext = (By.XPATH,"//h2[normalize-space()='Login to your account']")
    Email = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH,"//button[normalize-space()='Login']")
    Check_username_text = (By.CSS_SELECTOR, "ul[class='nav navbar-nav'] li a b")
    Alert = (By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']")
    Logout_Button = (By.XPATH,"//a[normalize-space()='Logout']")
    def click_login_signUp(self):
        self.click(*self.Login_singupbutton)

    def check_login_text(self):
        return self.get_text(*self.Logintext)

    def enter_email(self,username):
        self.send_keys(*self.Email,username)

    def enter_password(self,password):
        self.send_keys(*self.PASSWORD,password)

    def click_loginup(self):
        self.click(*self.LOGIN_BUTTON)

    def check_username(self):
        return self.get_text(*self.Check_username_text)

    def check_status(self):
        return self.get_text(*self.Alert)

    def click_logout(self):
        self.click(*self.Logout_Button)






































































# from selenium.webdriver.common.by import By
# from ecp_pom.apps.basePage import BasePage
# import time

# class LoginPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.user_name = (By.XPATH, "//input[@placeholder='Name']")
#         self.signup_email_field = (By.XPATH, "//input[@data-qa='signup-email']")
#         self.login_email_field = (By.XPATH, "//input[@data-qa='login-email']")
#         self.password_field = (By.XPATH, "//input[@placeholder='Password']")
#         self.login_btn = (By.XPATH, '//button[@data-qa="login-button"]')
#         # logout_btn = (By.XPATH, "//a[text()='Logout']")
#         self.sign_up_btn = (By.XPATH, "//button[normalize-space()='Signup']")
    
    
#     def signUp(self, name, email):
#         self.enter_text(self.user_name, name)
#         self.enter_text(self.signup_email_field, email)
#         self.click(self.sign_up_btn)
#         time.sleep(10)
        


#     def login(self, email, password):
#         self.enter_text(self.login_email_field, email)
#         self.enter_text(self.password_field, password)
#         self.click(self.login_btn)

#     # def is_logged_in(self):
#     #     return self.wait_for_element(self.logout_btn).is_displayed()


