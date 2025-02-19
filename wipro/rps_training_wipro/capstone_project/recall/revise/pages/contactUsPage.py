from revise.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class ContactUsForm(BasePage):
    contact_us_btn = (By.XPATH, "//a[normalize-space()='Contact us']")

    getInTouch_text = (By.XPATH, "//h2[normalize-space()='Get In Touch']")

    name_inp_form = (By.XPATH, "//input[@placeholder='Name']")
    email_inp_form = (By.XPATH, "//input[@placeholder='Email']")
    subject_inp_form = (By.XPATH, "//input[@placeholder='Subject']")
    msg_inp_form = (By.XPATH, "//textarea[@id='message']")
    choose_file_btn = (By.XPATH, "//input[@name='upload_file']")

    submit_btn = (By.XPATH, "//input[@name='submit']")

    success_verify_submittion_text = (By.XPATH, "//div[@class='status alert alert-success']")
    # <div class="status alert alert-success" style="display: block;">Success! Your details have been submitted successfully.</div>
    home_btn = (By.XPATH, "//a[normalize-space()='Home']")

    def clickContactUsBtn(self):
        self.click(*self.contact_us_btn)

    def verify_getInTouch(self):
        self.is_displayed(*self.getInTouch_text)
    
    def fill_form(self, name, email, subject, msg, upload):
        self.send_keys(*self.name_inp_form, name)
        self.send_keys(*self.email_inp_form, email)
        self.send_keys(*self.subject_inp_form, subject)
        self.send_keys(*self.msg_inp_form, msg)
        self.send_keys(*self.choose_file_btn, upload)
        self.click(*self.submit_btn)
        alert_popup_accept = self.driver.switch_to.alert
        alert_popup_accept.accept()
    
    def verify_success_popup(self):
        self.is_displayed(*self.success_verify_submittion_text)
        self.click(*self.home_btn)
        



    