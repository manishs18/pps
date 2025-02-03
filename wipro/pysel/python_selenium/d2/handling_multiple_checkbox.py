from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nikhil =webdriver.EdgeOptions()
avinash = webdriver.Edge(options=nikhil)
avinash.get("https://rahulshettyacademy.com/AutomationPractice/")
avinash.maximize_window()
time.sleep(2)

parent_checkbox= avinash.find_elements(By.XPATH, value="//input[@type='checkbox']")
time.sleep(2)

for i in parent_checkbox:
    if i == parent_checkbox[1]:
        i.click()
time.sleep(2)



