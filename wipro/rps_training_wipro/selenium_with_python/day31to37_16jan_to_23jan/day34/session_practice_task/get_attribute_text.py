from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(2)

element = driver.find_element(By.ID, 'twotabsearchtextbox')
text1 = element.text
print(text1)
time.sleep(3)

typetext = element.get_attribute("type")
print(typetext)
time.sleep(3)

idtext = element.get_attribute("id")
print(idtext)
time.sleep(3)

element = driver.find_element(By.ID, 'Search Amazon.in') #placeholder
text1 = element.text
print(text1)
time.sleep(3)

typetext = element.get_attribute("type")
print(typetext)
time.sleep(3)

idtext = element.get_attribute("id")
print(idtext)
time.sleep(3)

element = driver.find_element(By.ID, 'Search Amazon.in') #aria-label
text1 = element.text
print(text1)
time.sleep(3)

typetext = element.get_attribute("type")
print(typetext)
time.sleep(3)

idtext = element.get_attribute("id")
print(idtext)
time.sleep(3)