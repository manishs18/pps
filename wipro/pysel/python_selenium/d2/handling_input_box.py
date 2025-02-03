from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nikhil =webdriver.EdgeOptions()
avinash = webdriver.Edge(options=nikhil)
avinash.get("https://ogmt.koyeb.app/")
avinash.maximize_window()
time.sleep(5)

signin= avinash.find_element(By.XPATH, '//input[@type="search"]')
signin.send_keys("Manish")
time.sleep(5)
