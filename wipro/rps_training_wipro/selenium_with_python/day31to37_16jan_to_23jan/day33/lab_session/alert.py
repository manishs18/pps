from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
time.sleep(2)

alert_button = driver.find_element(By.XPATH, '//button[@onclick="showAlert()"]')
alert_button.click()

alt = driver.switch_to.alert
alt.accept()
time.sleep(3)

clickme_button1 = driver.find_element(By.XPATH, "//button[@onclick='myMessage()']")
clickme_button1.click()
time.sleep(10)

alt = driver.switch_to.alert
alt.accept()
time.sleep(5)

clickme_button2 = driver.find_element(By.XPATH, "//button[@onclick='myDesk()']")
clickme_button2.click()

alt = driver.switch_to.alert
alt.accept()
time.sleep(5)

clickme_button3 = driver.find_element(By.XPATH, "//button[@onclick='myPromp()']")
clickme_button3.click()

alt = driver.switch_to.alert
alt.send_keys("Manish Singh Be Alert!............")
alt.accept()
time.sleep(5)

driver.quit()

# driver.quit()
