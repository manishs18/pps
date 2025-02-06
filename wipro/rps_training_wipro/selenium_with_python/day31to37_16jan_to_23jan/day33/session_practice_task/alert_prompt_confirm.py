from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

infoalert_button = driver.find_element(By.XPATH, "//button[onclick='jsAlert()']")
infoalert_button.click()

alt = driver.switch_to.alert
alt.accept()
time.sleep(2)

confirmalert_button = driver.find_element(By.XPATH, "//button[onclick='jsConfirm()']")
confirmalert_button.click()

alt = driver.switch_to.alert
alt.accept()
time.sleep(2)

promptalert_button = driver.find_element(By.XPATH, "//button[onclick='jsPrompt()']")
promptalert_button.click()

alt = driver.switch_to.alert
alert_text = alt.text
print("Alert text:", alert_text)

alt.send_keys("Manish Singh Be Alert!............")
alt.accept()
time.sleep(2)

driver.quit()