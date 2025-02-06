from selenium import webdriver
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://ogmt.koyeb.app/")

#navigate back

time.sleep(3)
driver.back()

#navigate forward
time.sleep(3)
driver.forward()

#refresh the page
time.sleep(3)
driver.refresh()

time.sleep(3)
driver.close()
