import time
import pytest
from selenium import webdriver

from ecp_pom.apps.contactUsPage import Contactus
from ecp_pom.apps.homePage import HomePage
from ecp_pom.apps.loginPage import LoginPage


@pytest.fixture()
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://www.automationexercise.com/')
    yield driver
    driver.quit()

def test_contacts_us(driver):
    contact_us = Contactus(driver)
    contact_us.Click_Contactus()
    contact_us.send_data("Prakhar","wipro@gmail.com","Regadring Joining","I want to know About dates",r"C:\Users\mkuma\OneDrive\Desktop\CapstoneProject\CapstoneProject\POM\TestCases")
    time.sleep(3)
    alert = driver.switch_to.alert
    alert.accept()
    text = contact_us.check_form_status()
    if text.__contains__("Success!"):
        print("Success")

    else:
        print("Not Submitted")
    contact_us.click_Home()
    time.sleep(4)




