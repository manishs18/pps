from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from manish_ecp_pom.apps.pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class RegisterPage(BasePage):

    # locators for Registration page
    USERNAME = (By.XPATH, "//input[@placeholder='Name']")
    EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP = (By.XPATH, "//button[normalize-space()='Signup']")
    RADIO_BTN = (By.XPATH, "//label[normalize-space()='Mr.']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    DAY_DROPDOWN = (By.XPATH, "//select[@id='days']")
    # day = Select(DAY_DROPDOWN)
    MONTH_DROPDOWN = (By.XPATH, "//select[@id='months']")
    # month = Select(MONTH_DROPDOWN)
    YEAR_DROPDOWN = (By.XPATH, "//select[@id='years']")
    # yr = Select(YEAR_DROPDOWN)
    NEWSLETTER_CHECKBOX = (By.ID, 'newsletter')
    OFFERS_CHECKBOX = (By.ID, 'optin')
    FIRST_NAME = (By.XPATH, "//input[@id='first_name']")
    LAST_NAME = (By.XPATH, "//input[@id='last_name']")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, 'address2')
    COUNTRY_DROPDOWN = (By.XPATH, "//select[@id='country']")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_AC_BTN = (By.XPATH, "//button[contains(text(), 'Create Account')]")
    CONTINUE_BTN = (By.XPATH, "//a[normalize-space()='Continue']")

    SIGN_IN_BTN = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    CONTINUE_ON_CART = (By.XPATH, "//button[normalize-space()='Continue On Cart']")

    # Login locators
    EMAIL_LOGIN = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_LOGIN = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    # Payment gateway locators
    PLACE_ORDER = (By.XPATH, "//a[normalize-space()='Place Order']")
    NAME_ON_CARD = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NO = (By.XPATH, "//input[@name='card_number']")
    CVV = (By.XPATH, "//input[@placeholder='ex. 311']")
    EXPIRATION = (By.XPATH, "//input[@placeholder='MM']")
    YEAR = (By.XPATH, "//input[@placeholder='YYYY']")
    PAY_AND_CONFIRM = (By.XPATH, "//button[@id='submit']")

    # locators of download invoice, delete a/c, continue_after_delete_btn
    DOWNLOAD_INVOICE = (By.XPATH, "//a[normalize-space()='Download Invoice']")
    DELETE_AC = (By.XPATH, "//a[normalize-space()='Delete Account']")
    CONTINUE_AFTER_DELETE = (By.LINK_TEXT, "Continue")


    # methods or the page actions on the Add products to cart
    def enter_signup(self, username, email):
        self.send_keys(*self.USERNAME, username)
        self.send_keys(*self.EMAIL, email)
        self.click(*self.SIGNUP)


    def enter_details(self, password, firstname, lastname, address1, address2, state, city, zipcode, mobileno):
        self.click(*self.RADIO_BTN)
        self.send_keys(*self.PASSWORD, password)

        # Date of Birth
        # self.click(*self.DAY_DROPDOWN)
        # self.click(*self.day.select_by_value("5"))
        # self.click(*self.MONTH_DROPDOWN)
        # self.click(*self.month.select_by_value("January"))
        # self.click(*self.YEAR_DROPDOWN)
        # self.click(*self.yr.select_by_value("2025"))

        self.click(*self.NEWSLETTER_CHECKBOX)
        self.click(*self.OFFERS_CHECKBOX)

        # First name, last name, address
        self.send_keys(*self.FIRST_NAME, firstname)
        self.send_keys(*self.LAST_NAME, lastname)
        self.send_keys(*self.ADDRESS1, address1)
        self.send_keys(*self.ADDRESS2, address2)
        self.click(*self.COUNTRY_DROPDOWN)
        self.send_keys(*self.STATE, state)
        self.send_keys(*self.CITY, city)
        self.send_keys(*self.ZIPCODE, zipcode)
        self.send_keys(*self.MOBILE_NUMBER, mobileno)
        self.click(*self.CREATE_AC_BTN)

    def verify_home_page_visible(self):
        assert "Automation Exercise" in self.driver.title, "Home page is not visible."

    def verify_logged_in_as_visible(self):
        assert self.driver.find_element(*self.LOGGED_IN_TEXT).is_displayed(), "'Logged in as username' is not visible."

    def click_continue(self):
        self.click(*self.CONTINUE_BTN)
        # self.click(*self.SIGN_IN_BTN)

    def continue_on_cart(self):
        self.click(*self.CONTINUE_ON_CART)

    def click_signin_btn(self):
        self.click(*self.SIGN_IN_BTN)

    def enter_login(self, username, password):
        self.send_keys(*self.EMAIL_LOGIN, username)
        self.send_keys(*self.PASSWORD_LOGIN, password)
        self.click(*self.LOGIN_BTN)

    def place_order(self):
        self.click(*self.PLACE_ORDER)

    def enter_payment(self, name_on_card, card_no, cvv, expiration, year):
        self.send_keys(*self.NAME_ON_CARD, name_on_card)
        self.send_keys(*self.CARD_NO, card_no)
        self.send_keys(*self.CVV, cvv)
        self.send_keys(*self.EXPIRATION, expiration)
        self.send_keys(*self.YEAR, year)
        self.click(*self.PAY_AND_CONFIRM)

    def download_invoice(self):
        self.click(*self.DOWNLOAD_INVOICE)

    def delete_account(self):
        self.click(*self.DELETE_AC)
        self.click(*self.CONTINUE_AFTER_DELETE)
