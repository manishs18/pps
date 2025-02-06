from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/horizontal-scroll.php")
time.sleep(3)

time.sleep(5)
scroll_element = driver.find_element(By.CLASS_NAME, "horizan-scroll")
driver.execute_script("arguments[0].scrollLeft += 300;", scroll_element)

time.sleep(5)
driver.execute_script("arguments[0].scrollLeft -= 300;", scroll_element)

time.sleep(5)
driver.close()

driver.quit()