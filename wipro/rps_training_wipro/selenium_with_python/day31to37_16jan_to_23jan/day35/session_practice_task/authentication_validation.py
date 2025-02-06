from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import configparser
# import properties

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)  
driver.maximize_window()
# driver.get(base_url)

config = configparser.ConfigParser()
config.read("C:\\Users\\mkuma\\OneDrive\\Desktop\\my_repo\\ManishDTA\\selenium_with_python\\day31to37_16jan_to_23jan\\day35\\session_practice_task\\config.properties")

base_url = config.get("setting", "base_url")
username = config.get("setting", "username")
password = config.get("setting", "password")
driver.get(base_url)

time.sleep(2)

signin= driver.find_element(By.XPATH, value='//button[@class="btn btn-primary mx-1"]')
signin.click()
time.sleep(4)

username = driver.find_element(By.ID, "loginusername")
username.send_keys(username)
time.sleep(3)

password = driver.find_element(By.ID, "loginpassword")
password.send_keys(password)    
time.sleep(3)

submit = driver.find_element(By.ID, "gridCheck1")
submit.click()
time.sleep(3)

login= driver.find_element(By.XPATH, value='//button[@class="btn btn-success"]')
login.click()
time.sleep(3)

driver.quit()
