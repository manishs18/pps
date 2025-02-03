from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://demoqa.com/browser-windows")

time.sleep(3)
parenthandle = driver.current_window_handle
print(parenthandle)

time.sleep(2)
new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
new_tab.click()

windows = driver.window_handles
driver.switch_to.window(windows[1])

time.sleep(2)
driver.maximize_window()

text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(text.is_displayed())

driver.switch_to.window(parenthandle)
time.sleep(2)

######
new_window_tab = driver.find_element(By.XPATH, "//button[@id='windowButton']")
new_window_tab.click()

windows = driver.window_handles
driver.switch_to.window(windows[1])

time.sleep(2)
driver.maximize_window()

windows_text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(windows_text.is_displayed())

driver.switch_to.window(parenthandle)
time.sleep(2)

####
new_window_msg_tab = driver.find_element(By.XPATH, "//button[@id='messageWindowButton']")
new_window_msg_tab.click()

windows = driver.window_handles
driver.switch_to.window(windows[1])

time.sleep(2)
driver.maximize_window()

windows_text = driver.find_element(By.XPATH, "id attribute is not available for this element")
print(windows_text.is_displayed())

driver.switch_to.window(parenthandle)
time.sleep(2)
driver.quit()