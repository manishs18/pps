from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://demo.guru99.com/test/drag_drop.html")
time.sleep(2)

act = ActionChains(driver)

time.sleep(3)
src = driver.find_element(By.XPATH,"//section[@id='g-container-main']//li[4]//a[1]")
des = driver.find_element(By.XPATH,"//ol[@id='amt7']//li[@class='placeholder']")
act.drag_and_drop(src,des).perform()

time.sleep(3)
src = driver.find_element(By.XPATH,"//a[normalize-space()='BANK']")
des = driver.find_element(By.XPATH,"//ol[@id='bank']//li[@class='placeholder']")
time.sleep(2)
act.drag_and_drop(src,des).perform()

time.sleep(2)
src = driver.find_element(By.XPATH,"//a[normalize-space()='SALES']")
des = driver.find_element(By.XPATH,"//ol[@id='loan']//li[@class='placeholder']")
time.sleep(2)
act.drag_and_drop(src,des).perform()

time.sleep(2)
src = driver.find_element(By.XPATH,"//li[@id='credit0']//a[@class='button button-orange'][normalize-space()='-5000']")
des = driver.find_element(By.XPATH,"//ol[@id='amt8']//li[@class='placeholder']")
act.drag_and_drop(src,des).perform()
driver.back()

