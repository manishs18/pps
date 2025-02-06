import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


optional = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=optional)
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/")

# for drop down selection we have select class
# select by visible class
# select by value
# select by index

dropdown = driver.find_elements(By.ID, value= 'Cucumber')
sel = Select(dropdown)

# select by visible text
time.sleep(5)
sel.select_by_visible_text("option1")

# select by value text
time.sleep(5)
sel.select_by_value("Option2")

# select by index
time.sleep(5)
sel.select_by_index(3)

time.sleep(5)
driver.close()