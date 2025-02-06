from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://testuserautomation.github.io/WebTable/")
time.sleep(2)

rows = driver.find_elements(By.XPATH, "//table[@xpath ='1']/tbody/tr")
for i in rows:
    print(i.text)
time.sleep(3)

cols = driver.find_elements(By.XPATH, "//table[@xpath ='1']/tbody/tr[2]/td")
for j in cols:
    print(j.text)

time.sleep(3)

# celldata = driver.find_element(By.XPATH, "//table[@xpath ='1']/tbody/tr[3]/td[2]")
# print(celldata)

before_xpath = '//table/tbody/tr['
after_xpath = ']/td[2]'

for i in range(2, len(rows)+1):
    firstnames = driver.find_element(By.XPATH, before_xpath+str(i)+after_xpath).text
    print(firstnames)
    time.sleep(6)
    
    if(firstnames.__contains__("will")):
        driver.find_element(By.XPATH, "//table/tbody/tr[' +str(i)+']/td[1]/input").click()
        time.sleep(2)
        break