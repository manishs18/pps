from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

driver.get_screenshot_as_file("C:\Users\mkuma\OneDrive\Desktop\manish.png")

driver.save_screenshot("C:\Users\mkuma\OneDrive\Desktop\my_repo\ManishDTA\selenium_with_python\day31to37_16jan_to_23jan\day34\session_practice_task\manish.png")