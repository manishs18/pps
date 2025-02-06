from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
time.sleep(2)

rows = driver.find_elements(By.XPATH, "//table[@id = 'customers']/tbody/tr")
for i in rows:
    print(i.text)
time.sleep(3)

cols = driver.find_elements(By.XPATH, "//table[@id = 'customers']/tbody/tr[2]/td")
for j in cols:
    print(j.text)

time.sleep(3)

celldata = driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr[6]/td[3]")
print(celldata)