import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Set up Edge WebDriver options
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

# Open the target website
driver.maximize_window()
driver.get('https://jqueryui.com/checkboxradio/')

# Implicit wait
driver.implicitly_wait(2)
time.sleep(2)

# Switch to the iframe containing the radio buttons
fr = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(fr)
time.sleep(3)

radio = driver.find_element(By.XPATH, "//label[@for='radio-1']")

# Explicit wait to ensure the radio button is displayed
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda d: radio.is_displayed())
radio.click()
time.sleep(3)

# Quit the driver
driver.quit()
