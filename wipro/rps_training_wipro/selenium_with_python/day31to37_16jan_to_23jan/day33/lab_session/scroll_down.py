from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://ogmt.koyeb.app/")
# driver.get("https://www.tutorialspoint.com/selenium/practice/scroll-down.php")
time.sleep(3)


# driver.execute_script("window.scrollTo(0, -1000)")
# time.sleep(3)

driver.execute_script("window.scrollTo(0, 1500)")
time.sleep(3)