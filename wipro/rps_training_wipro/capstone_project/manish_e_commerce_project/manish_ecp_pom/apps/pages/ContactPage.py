from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.BasePage import BasePage


class Contact(BasePage):
    CONTACT_US_BTN = (By.XPATH, "//a[normalize-space()='Contact us']")
    GET_IN_TOUCH = (By.XPATH, "//h2[normalize-space()='Get In Touch']")
    NAME = (By.XPATH, "//input[@placeholder='Name']")
    EMAIL = (By.XPATH, "//input[@placeholder='Email']")
    SUBJECT = (By.XPATH, "//input[@placeholder='Subject']")
    TEXT_AREA = (By.XPATH, "//textarea[@id='message']")
    UPLOAD = (By.XPATH, "//input[@name='upload_file']")
    SUBMIT_BTN = (By.XPATH, "//input[@name='submit']")

    HOME_BTN = (By.XPATH, "//span[normalize-space()='Home']")

    def click_contact_us(self):
        self.click(*self.CONTACT_US_BTN)

    def verify_get_in_touch(self):
        assert self.driver.find_element(*self.GET_IN_TOUCH).is_displayed(), "'Get in Touch' is visible."

    def contact_us_form(self, name, email, subject, textarea, upload):
        self.send_keys(*self.NAME, name)
        self.send_keys(*self.EMAIL, email)
        self.send_keys(*self.SUBJECT, subject)
        self.send_keys(*self.TEXT_AREA, textarea)
        self.send_keys(*self.UPLOAD, upload)

    def alert_popup(self):
        self.click(*self.SUBMIT_BTN)
        alt = self.driver.switch_to.alert
        alt.accept()
        self.click(*self.HOME_BTN)
