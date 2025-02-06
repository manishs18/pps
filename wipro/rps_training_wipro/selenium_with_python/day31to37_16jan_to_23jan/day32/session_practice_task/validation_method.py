from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://ogmt.koyeb.app/")

time.sleep(2)
element = driver.find_element(By.XPATH, "//a[@href='/blog']")
if (element.is_displayed()):
    element.click()
    time.sleep(4)
    print("Element is displayed")
else:
    print("Element is not displayed")

