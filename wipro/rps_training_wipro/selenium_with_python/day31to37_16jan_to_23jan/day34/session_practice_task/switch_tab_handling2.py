from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(3)
parenthandle = driver.current_window_handle
print(parenthandle)

time.sleep(2)

clickhere = driver.find_element(By.XPATH, "//a[contains(text(),'Click Here')]")
clickhere.click()

windows = driver.window_handles
print(windows)

driver.switch_to.window(windows[1])

time.sleep(2)
driver.maximize_window()

text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
print(text)

driver.switch_to.window(parenthandle)
time.sleep(2)

driver.quit()