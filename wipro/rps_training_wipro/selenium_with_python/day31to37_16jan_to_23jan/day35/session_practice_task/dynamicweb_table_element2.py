from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://cosmocode.io/automation-practice-webtable/")
time.sleep(2)


rows = driver.find_elements(By.XPATH, "//table[@id = 'countries']/tbody/tr")
print(len(rows))

time.sleep(2)

#identify the number of coluens

cols = driver.find_elements(By.XPATH, "//table[@id = 'countries']/tbody/tr[2]/td")
print(len(cols))

before_xpath="//table[@id = 'countries']/tbody/tr["

after_xpath="]/td[2]"

for i in range(2, len(rows)+1):
    firstnames = driver.find_element(By. XPATH, before_xpath+str(i)+after_xpath).text
    print(firstnames)
    time.sleep(4)
    if firstnames.__contains__("Austria"):
        driver.find_element(By.XPATH, "//table/tbody/tr["+str(i)+"]/td[1]/input").click()
        time.sleep(3)
        break