from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nikhil =webdriver.EdgeOptions()
avinash = webdriver.Edge(options=nikhil)
avinash.get("https://rahulshettyacademy.com/angularpractice/")
avinash.maximize_window()
time.sleep(5)

username = avinash.find_element(By.NAME, value="name")
username.send_keys("Manish")
time.sleep(5)

# username = driver.find_element(By.NAME, value="email")
# username.send_keys("manish123@gmai.com")
                        
# username = driver.find_element(By.ID, value="exampleInputPassword")
# username.send_keys("12345")

# username = driver.find_element(By.XPATH, value="//input[@value='Submit']")
# submit.click()

# time.sleep(5)
