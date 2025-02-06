from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Edge WebDriver with optional settings
optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()

# Open the target URL
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
time.sleep(2)

date_picker = driver.find_element(By.XPATH, '//*[@id="datepicker"]')
date_picker.click()
time.sleep(2)


next_arrow = driver.find_element(By.XPATH, "//a[@title='Next']")
next_arrow.click()
time.sleep(2)

date_to_select = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//a[text()='15']")
date_to_select.click()
time.sleep(2)

driver.quit()
