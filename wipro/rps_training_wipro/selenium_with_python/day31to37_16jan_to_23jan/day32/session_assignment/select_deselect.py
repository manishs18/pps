import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://grotechminds.com/multiple-select/")

time.sleep(3)
drpdown1 = driver.find_element(By.ID,"automobiles")

sel = Select(drpdown1)

time.sleep(5)
sel.select_by_value("motorcycle")
time.sleep(5)
sel.select_by_value("sedan")
time.sleep(5)

sel.select_by_value("hatchback")
time.sleep(5)

sel.deselect_all()
time.sleep(3)
driver.close()