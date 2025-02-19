from revise.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


class VerifySubscription(BasePage):
    subscription_text = (By.XPATH, "//h2[normalize-space()='Subscription']")
    email_input = (By.XPATH, "//input[@id='susbscribe_email']")
    email_submit_btn = (By.XPATH, "//i[@class='fa fa-arrow-circle-o-right']")
    verify_success_msg_popup = (By.XPATH, "//div[@class='alert-success alert']")
    cart_btn = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]")
    scroll_btn_down_side_for_up_side = (By.XPATH, "//i[@class='fa fa-angle-up']")
    full_fledge_automation_engineers_text = (By.XPATH, "//div[@class='item active']//h2[contains(text(),'Full-Fledged practice website for Automation Engin')]")



    def scroll_down_footer(self):
        element = self.driver.find_element(*self.subscription_text) 
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("window.scrollBy(0, 1400)")   

    def scroll_up(self):
        element = self.driver.find_element(*self.full_fledge_automation_engineers_text) 
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("window.scrollBy(1400, 0)")  

    def verify_subscription_on_homepage(self, email):
        self.is_displayed(*self.subscription_text)
        self.send_keys(*self.email_input, email)
        self.click(*self.email_submit_btn)
        self.is_displayed(*self.verify_success_msg_popup)

    def verify_subscription_on_cartpage(self, email):
        self.click(*self.cart_btn)
        element = self.driver.find_element(*self.subscription_text) 
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("window.scrollBy(0, -100)")
        self.is_displayed(*self.subscription_text)
        self.send_keys(*self.email_input, email)
        self.click(*self.email_submit_btn)
        self.is_displayed(*self.verify_success_msg_popup)

    def verify_subs_fledge_text_using_arrow_btn(self):
        self.is_displayed(*self.subscription_text)
        self.click(*self.scroll_btn_down_side_for_up_side)
        self.is_displayed(*self.full_fledge_automation_engineers_text)

    def verify_subs_text_without_arrow_btn(self):
        self.is_displayed(*self.subscription_text)
        
    def verify_fledge_text_without_arrow_btn(self):
        self.is_displayed(*self.full_fledge_automation_engineers_text)