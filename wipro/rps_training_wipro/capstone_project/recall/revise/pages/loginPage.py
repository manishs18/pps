from selenium.webdriver.common.by import By
from revise.pages.basePage import BasePage
from revise.pages.registerPage import RegisterPage


class LoginPage(BasePage):

    login_to_account_text_visible = (By.XPATH, "//h2[normalize-space()='Login to your account']")

    email_address_input = (By.XPATH, "//input[@data-qa='login-email']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    login_btn = (By.XPATH, "//button[normalize-space()='Login']")

    loggedin_with_username = (By.XPATH, "//b[normalize-space()='manish18']")
    loggedin_with_username_id = (By.XPATH, "//b[normalize-space()='manishhss18000']")
    loggedin_with_username_with_id = (By.XPATH, "//b[normalize-space()='manishhhsssss180']")

    incorect_invalid_email_pwd_text = (By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")

    logout_btn = (By.XPATH, "//a[normalize-space()='Logout']")

    # RegisterPage.verify_home_page()
    # RegisterPage.signUp_login_btns()
    
    def verify_login_acc_text_visible(self):
        self.is_displayed(*self.login_to_account_text_visible)

    def login_with_credentials(self, email, password):
        self.send_keys(*self.email_address_input, email)
        self.send_keys(*self.password_input, password)
        self.click(*self.login_btn)

    def verify_incorrect_email_pwd_text_visible(self):
        self.is_displayed(*self.incorect_invalid_email_pwd_text)

    def verify_loggedIn_with_username(self):
        self.is_displayed(*self.loggedin_with_username)

    def verify_loggedIn_with_username_id(self):
        self.is_displayed(*self.loggedin_with_username_id)

    def verify_loggedIn_with_username_with_id(self):
        self.is_displayed(*self.loggedin_with_username_with_id)

    def logoutUser(self):
        self.click(*self.logout_btn)
