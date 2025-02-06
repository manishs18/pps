from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")

# Form filling

time.sleep(2)
firstname = driver.find_element(By.ID, "first-name")
firstname.send_keys("Manish")

time.sleep(2)
lastname = driver.find_element(By.ID, "last-name")
lastname.send_keys("Singh")

time.sleep(2)
jobtitle = driver.find_element(By.ID, "job-title")
jobtitle.send_keys("SDE")

time.sleep(2)
radiobtn = driver.find_element(By.ID, "radio-button-2")
radiobtn.click()

time.sleep(2)
checkbox = driver.find_element(By.ID, "checkbox-1")
checkbox.click()

time.sleep(2)
dropdown1 = driver.find_element(By.XPATH, "//select[@id='select-menu']")
sel = Select(dropdown1)
time.sleep(2)
sel.select_by_value("1")

# time.sleep(2)
# date = driver.find_element(By.XPATH, "//td[@class='today day']")
# date.click()

time.sleep(3)
submit = driver.find_element(By.XPATH, "//a[@role='button']")
submit.click()


time.sleep(4)
driver.close()

# alt = driver.switch_to.alert
# alt.accept()
