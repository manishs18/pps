from selenium.webdriver.common.by import By

from ecp_pom.apps.basePage import BasePage


class Contactus(BasePage):
    ContactUS_Button = (By.XPATH,"//a[normalize-space()='Contact us']")
    Name =(By.XPATH,"//input[@placeholder='Name']")
    Email = (By.XPATH,"//input[@placeholder='Email']")
    Subject = (By.XPATH,"//input[@placeholder='Subject']")
    Message = (By.XPATH,"//textarea[@placeholder='Your Message Here']")
    Upload =(By.XPATH,"//input[@name='upload_file']")
    Submit_Button = (By.XPATH,"//input[@name='submit']")
    Success_text = (By.XPATH,"//div[@class='status alert alert-success']")
    Home_Button =(By.XPATH,"//a[contains(text(),'Home')]")
    def Click_Contactus(self):
        self.click(*self.ContactUS_Button)

    def send_data(self,name,email,subject,message,upload):
        self.send_keys(*self.Name,name)
        self.send_keys(*self.Email, email)
        self.send_keys(*self.Subject, subject)
        self.send_keys(*self.Message, message)
        self.send_keys(*self.Upload,upload)
        self.click(*self.Submit_Button)

    def check_form_status(self):
        return self.get_text(*self.Success_text)

    def click_Home(self):
        self.click(*self.Home_Button)

