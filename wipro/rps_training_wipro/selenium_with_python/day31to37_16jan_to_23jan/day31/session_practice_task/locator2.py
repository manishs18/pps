from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)  
driver.maximize_window()

driver.get('https://ogmt.koyeb.app/')

time.sleep(2)

signin= driver.find_element(By.XPATH, value='//button[@class="btn btn-primary mx-1"]')
signin.click()
time.sleep(4)

username = driver.find_element(By.ID, "loginusername")
username.send_keys("mkuma")
time.sleep(3)

password = driver.find_element(By.ID, "loginpassword")
password.send_keys("admin123")
time.sleep(3)

submit = driver.find_element(By.ID, "gridCheck1")
submit.click()
time.sleep(3)

login= driver.find_element(By.XPATH, value='//button[@class="btn btn-success"]')
login.click()
time.sleep(3)

driver.quit()
