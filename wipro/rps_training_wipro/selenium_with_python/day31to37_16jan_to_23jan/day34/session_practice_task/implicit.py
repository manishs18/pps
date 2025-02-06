from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
import time

# Initialize WebDriver for Edge
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://jqueryui.com/checkboxradio/")
driver.implicitly_wait(5)
# time.sleep(2)

# Identify the frame as a web element
fr = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(fr)

# driver.switch_to.frame(0)
# time.sleep(3)

radio = driver.find_element(By.XPATH, value="//label[@for='radio-1']")
radio.click()
# time.sleep(3)