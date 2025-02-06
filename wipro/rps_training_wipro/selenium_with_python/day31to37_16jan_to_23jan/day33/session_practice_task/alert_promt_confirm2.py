from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
time.sleep(2)

alert_with_ok_button = driver.find_element(By.XPATH, '//a[@href="#OKTab"]')
alert_with_ok_button.click()

alt = driver.switch_to.alert
alt.accept()
time.sleep(4)

alert_with_ok_n_cancel_button = driver.find_element(By.XPATH, '//a[@href="#CancelTab"]')
alert_with_ok_n_cancel_button.click()

alt = driver.switch_to.alert
alt.dismiss()
time.sleep(4)

alert_with_text_button = driver.find_element(By.XPATH, '//a[@href="#Textbox"]')
alert_with_text_button.click()

alt = driver.switch_to.alert
alt.send_keys("Manish Singh Be Alert!............")
alt.accept()
time.sleep(4)

driver.quit()
