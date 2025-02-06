
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

username = driver.find_element(By.NAME, value="username")
username.send_keys("Admin")
                        
username = driver.find_element(By.ID, value="password")
username.send_keys("admin123")

username = driver.find_element(By.XPATH, value="//button[@type='submit']")
username.click()
#multiselectors checkbox and
checkbox_list = driver.find_elements(By.XPATH, "//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon']")
count = len(checkbox_list)
print(count)

#itereate through the list of checkboxes
time.sleep(2)
for checkbox in checkbox_list(range):
    time.sleep(2)
    checkbox.click()

time.sleep(2)

driver.close()


