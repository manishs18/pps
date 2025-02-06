from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://ogmt.koyeb.app/")
time.sleep(3)

ogmt_website = driver.find_element(By.XPATH, "//p[contains(text(),'This Site is')]//a[@href='#'][normalize-space()='OGMT']")
driver.execute_script("arguments[0].scrollIntoView();", ogmt_website)
time.sleep(3)
ogmt_website.click()

driver.back()
time.sleep(3)

driver.execute_script("window.scrollTo(0, -1000)")
time.sleep(3)

driver.execute_script("window.scrollTo(0, 500)")