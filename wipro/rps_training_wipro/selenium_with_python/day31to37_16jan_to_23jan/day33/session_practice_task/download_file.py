from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()  
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(2)

file_link = driver.find_element(By.LINK_TEXT, "//a[@href='download/manish.png']") 
file_link.click()
time.sleep(5)


driver.quit()
