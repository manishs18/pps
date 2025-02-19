from selenium.webdriver.common.by  import By
from revise.pages.basePage import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class RegisterPage(BasePage):

    #homepage xpath for verify
    homepage_element = (By.XPATH, "//img[@alt='Website for automation practice']")

    #homepage page xpath for signup/login
    signUp_login_btn = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    username_input = (By.XPATH, "//input[@placeholder='Name']")
    email_id_input = (By.XPATH, "//input[@data-qa='signup-email']")
    signUp_btn = (By.XPATH, "//button[normalize-space()='Signup']")

    # enter account information xpath
    mr_radio_btn = (By.XPATH, "//input[@id='id_gender1']")
    password_input = (By.XPATH, "//input[@id='password']")
    date_dropdown = (By.XPATH, "//select[@id='days']")
    month_dropdown = (By.XPATH, "//select[@id='months']")
    year_dropdown = (By.XPATH, "//select[@id='years']")
    signup_newletters_checkbox = (By.XPATH, "//input[@id='newsletter']")
    special_offers_partners_checkbox = (By.XPATH, "//input[@id='optin']")
    
    #address information xpath
    first_name = (By.XPATH, "//input[@id='first_name']")
    last_name = (By.XPATH, "//input[@id='last_name']")
    company_name = (By.XPATH, "//input[@id='company']")
    company_address1 = (By.XPATH, "//input[@id='address1']")
    company_address2 = (By.XPATH, "//input[@id='address2']")
    country_name = (By.XPATH, "//select[@id='country']")
    state_name = (By.XPATH, "//input[@id='state']")
    city_name = (By.XPATH, "//input[@id='city']")
    zipcode_id = (By.XPATH, "//input[@id='zipcode']")
    mobile_number = (By.XPATH, "//input[@id='mobile_number']")

    create_account_btn =(By.XPATH, "//button[normalize-space()='Create Account']")

    username_n_email_already_exits = (By.XPATH, "//p[normalize-space()='Email Address already exist!']")

    continue_btn = (By.XPATH, "//a[@class='btn btn-primary']")

    loggedin_with_username = (By.XPATH, "//b[normalize-space()='manishhhhsss180']")
    loggedin_with_usernames_id = (By.XPATH, "//b[normalize-space()='manishhhs188800']")

    def verify_home_page(self):
        self.is_displayed(*self.homepage_element)
    
    def signUp_login_btns(self):
        self.click(*self.signUp_login_btn)

    def sign_up(self, username, email):
        self.send_keys(*self.username_input, username)
        self.send_keys(*self.email_id_input, email)
        self.click(*self.signUp_btn)

    def signUp_details(self, password, first_name, last_name, address1, address2, state, city, zipcode, mobile_number):
        self.click(*self.mr_radio_btn)
        self.send_keys(*self.password_input, password)

        date_select_drpdwn = self.wait_for_element(*self.date_dropdown)
        select_date = Select(date_select_drpdwn)
        select_date.select_by_visible_text('12')

        month_select_drpdwn = self.wait_for_element(*self.month_dropdown)
        select_month = Select(month_select_drpdwn)
        select_month.select_by_visible_text('May')

        year_select_drpdwn = self.wait_for_element(*self.year_dropdown)
        select_year = Select(year_select_drpdwn)
        select_year.select_by_visible_text('2020')

        self.click(*self.signup_newletters_checkbox)
        self.click(*self.special_offers_partners_checkbox)

        self.send_keys(*self.first_name, first_name)
        self.send_keys(*self.last_name, last_name)
        self.send_keys(*self.company_address1, address1)
        self.send_keys(*self.company_address2, address2)

        country_select_drpdwn = self.wait_for_element(*self.country_name)
        select_country = Select(country_select_drpdwn)
        select_country.select_by_visible_text('India')

        self.send_keys(*self.state_name, state)
        self.send_keys(*self.city_name, city)
        self.send_keys(*self.zipcode_id, zipcode)
        self.send_keys(*self.mobile_number, mobile_number)
        self.click(*self.create_account_btn)

    def already_user_email_exits(self):
        self.is_displayed(*self.username_n_email_already_exits)

    def click_continue_btn(self):
        self.click(*self.continue_btn)
        
    def verfiy_logged_with_username(self):
        self.is_displayed(*self.loggedin_with_username)

    def verfiy_logged_with_usernames_id(self):
        self.is_displayed(*self.loggedin_with_usernames_id)



