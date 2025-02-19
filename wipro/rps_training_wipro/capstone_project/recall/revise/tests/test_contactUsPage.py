from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from revise.pages.registerPage import RegisterPage
from revise.pages.contactUsPage import ContactUsForm
import time
import pytest


def test_contact_us_form(driver):
    signup_btn = RegisterPage(driver)
    form_submission = ContactUsForm(driver)

    signup_btn.verify_home_page()
    form_submission.clickContactUsBtn()
    form_submission.verify_getInTouch()
    form_submission.fill_form("manish", "manish@gmail.com", "always weeping for ex-gf", "Beacuse i have no job, so thats why she reject, she said u r future begger.", r"C:\Users\mkuma\OneDrive\Desktop\recall\revise\Screenshot 2025-02-15 030027.png")
    form_submission.verify_success_popup()
