from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://jqueryui.com/")
time.sleep(2)

act = ActionChains(driver)

drag_n_drop_text_link = driver.find_element(By.XPATH, "//a[normalize-space()='Droppable']")
drag_n_drop_text_link.click()

time.sleep(3)
src = driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")
des = driver.find_element(By.XPATH,"//div[@id='droppable']")

time.sleep(2)
act.drag_and_drop_by_offset(src,des).perform()
driver.back()

