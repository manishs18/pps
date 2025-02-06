from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://demoqa.com/browser-windows")
time.sleep(2)



driver.execute_script("window.scrollBy(0, 350)")

time.sleep(2)

newtab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
newtab.click()

time.sleep(2)

windows = driver.window_handles

driver.switch_to.window(windows[1])
driver.maximize_window()

time.sleep(2)

gettext = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(gettext.text)

driver.switch_to.window(windows[0])
newtab.is_displayed()

time.sleep(2)

newwindow = driver.find_element(By.XPATH, "//button[@id='windowButton']")
newwindow.click()

time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])

time.sleep(2)

gettext1 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(gettext1.text)

driver.switch_to.window(windows[0])

time.sleep(2)

newwindowmessage = driver.find_element(By.XPATH, "//button[@id='messageWindowButton']")
newwindowmessage.click()

time.sleep(5)

windows = driver.window_handles

driver.switch_to.window(windows[1])


time.sleep(4)

gettext2 = driver.find_element(By.CSS_SELECTOR, "body")
print(gettext2.text)

driver.switch_to.window(windows[0])
newwindowmessage.is_displayed()

time.sleep(2)

driver.close()