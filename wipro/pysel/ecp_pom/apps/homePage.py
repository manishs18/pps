from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from ecp_pom.apps.basePage import BasePage


class HomePage(BasePage):
        login_singupbutton = (By.XPATH,"//a[normalize-space()='Signup / Login']")
        signuptext = (By.XPATH,"//h2[normalize-space()='New User Signup!']")
        signUp_name = (By.XPATH,"//input[@name='name']")
        signUp_email = (By.CSS_SELECTOR,"input[data-qa='signup-email']")
        signUp_Button = (By.XPATH,"//button[normalize-space()='Signup']")
        accountinfo = (By.XPATH,"//b[normalize-space()='Enter Account Information']")
        radiobox  = (By.XPATH,"//input[@id='id_gender1']")
        PASSWORD = (By.XPATH,"//input[@id='password']")
        Date = (By.XPATH,"//select[@id='days']")
        Month =(By.XPATH,"//select[@id='months']")
        Year = (By.XPATH, "//select[@id='years']")
        checkbox1 = (By.XPATH,"//input[@id='newsletter']")
        checkbox2 = (By.XPATH,"//input[@id='optin']")
        First_name = (By.XPATH,"//input[@name='first_name']")
        Last_name = (By.XPATH,"//input[@name='last_name']")
        Company = (By.XPATH,"//input[@name='company']")
        Address = (By.XPATH,"//input[@name='address1']")
        State = (By.XPATH,"//input[@id='state']")
        City = (By.XPATH,"//input[@id='city']")
        Zipcode  = (By.XPATH,"//input[@id='zipcode']")
        Mobile  = (By.XPATH,"//input[@id='mobile_number']")
        CreateAccount = (By.XPATH,"//button[normalize-space()='Create Account']")
        Successmsg = (By.XPATH,"//b[normalize-space()='Account Created!']")
        Con_button = (By.XPATH,"//a[contains(text(),'Continue')]")
        Check_username_text = (By.CSS_SELECTOR,"ul[class='nav navbar-nav'] li a b")
        Delete_Acc = (By.XPATH,"//a[normalize-space()='Delete Account']")
        Delete_Status = (By.XPATH,"//b[normalize-space()='Account Deleted!']")
        ExistUser = (By.XPATH,"//p[normalize-space()='Email Address already exist!']")
        TestCase_Button =(By.XPATH,"//a[normalize-space()='Test Cases']")
        TestCase_text = (By.XPATH,"//b[normalize-space()='Test Cases']")

        def check_HomePage(self):
            return self.get_page_title()

        def click_login_signUp(self):
            self.click(*self.login_singupbutton)

        def check_sigUptext(self):
            return self.get_text(*self.signuptext)

        def enter_signUpname(self,name):
            self.send_keys(*self.signUp_name,name)

        def enter_signUpemail(self, email):
            self.send_keys(*self.signUp_email, email)

        def click_signUp(self):
            self.click(*self.signUp_Button)
        def check_accountinfo(self):
            return self.get_text(*self.accountinfo)


        def click_radio(self):
            self.click(*self.radiobox)

        def enter_password(self,password):
            self.send_keys(*self.PASSWORD,password)

        def enter_date(self,date):
            dropdown = self.get_dropdown(*self.Date)
            dropdown.select_by_visible_text(date)

        def enter_month(self,month):
            dropdown = self.get_dropdown(*self.Month)
            dropdown.select_by_visible_text(month)

        def enter_year(self, year):
            dropdown = self.get_dropdown(*self.Year)
            dropdown.select_by_visible_text(year)

        def click_checkbox(self):
            self.click(*self.checkbox1)
            self.click(*self.checkbox2)

        def enter_accountdetails(self,fname,lname,company,address,state,city,zipcode,mobile):
            self.send_keys(*self.First_name,fname)
            self.send_keys(*self.Last_name, lname)
            self.send_keys(*self.Company, company)
            self.send_keys(*self.Address, address)
            self.send_keys(*self.State, state)
            self.send_keys(*self.City, city)
            self.send_keys(*self.Zipcode, zipcode)
            self.send_keys(*self.Mobile, mobile)
            self.click(*self.CreateAccount)

        def check_acc_create(self):
            return self.get_text(*self.Successmsg)

        def click_continue(self):
            self.click(*self.Con_button)

        def check_username(self):
            return self.get_text(*self.Check_username_text)

        def click_delete(self):
            self.click(*self.Delete_Acc)

        def check_deletestatus(self):
            return self.get_text(*self.Delete_Status)

        def check_existUser(self):
            return self.get_text(*self.ExistUser)

        def click_TestCase(self):
            self.click(*self.TestCase_Button)

        def check_Navigate(self):
            return self.get_text(*self.TestCase_text)
























































# from selenium.webdriver.common.by import By
# from ecp_pom.apps.basePage import BasePage

# class HomePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.signup_login_btn = (By.XPATH, '//a[@href="/login"]')

#     def click_signup_login(self):
#         self.click(self.signup_login_btn)
