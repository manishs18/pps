from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/")
time.sleep(2)

checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
count = len(checkbox_list)
print(count)

time.sleep(2)
for checkbox in checkbox_list:
    time.sleep(2)
    if not (checkbox.is_selected()):
        checkbox.click()
        print("Checkbox is selected")
time.sleep(2)
username = driver.find_element(By.XPATH, value="//button[@type='submit']")
username.click()

driver.close()

