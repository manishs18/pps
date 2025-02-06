
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(3)

radio_btn1 = driver.find_element(By.NAME, value="radioButton")
radio_btn1.click()
time.sleep(2)

check_box_option1 = driver.find_element(By.ID, value="checkBoxOption1")
check_box_option1.click()
time.sleep(2)   

driver.close()




