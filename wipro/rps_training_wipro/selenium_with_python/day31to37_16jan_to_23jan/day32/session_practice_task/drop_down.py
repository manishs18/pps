import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# for drop down selection we have select class
# select by visible class
# select by value
# select by index

dropdown = driver.find_element(By.ID, value='dropdown-class-example')
dropdown.click()
sel = Select(dropdown)

# select by visible text
time.sleep(5)
sel.select_by_visible_text("Option1")

# select by value text
time.sleep(5)
sel.select_by_value("option2")

# select by index
time.sleep(5)
sel.select_by_index(3)

time.sleep(5)
driver.close()