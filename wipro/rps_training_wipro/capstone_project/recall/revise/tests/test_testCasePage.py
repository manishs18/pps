from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from revise.pages.registerPage import RegisterPage
from revise.pages.testCasePage import VerifyTestCasePage
import time 
import pytest


def test_verify_testCasePage(driver):
    signup_btn = RegisterPage(driver)
    verifyTestCasePage = VerifyTestCasePage(driver)

    signup_btn.verify_home_page()

    verifyTestCasePage.navigate_to_testCasePage()
    verifyTestCasePage.verify_u_r_testCaePage()