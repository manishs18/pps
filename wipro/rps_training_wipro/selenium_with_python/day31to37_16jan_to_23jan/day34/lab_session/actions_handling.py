from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

act = ActionChains(driver)

# add_remove_ele_text_link = driver.find_element(By.XPATH,"//a[normalize-space()='Add/Remove Elements']")
# act.click(add_remove_ele_text_link)
# time.sleep(3)
# driver.back()
broken_images = driver.find_element(By.XPATH,"//a[normalize-space()='Broken Images']")
act.double_click(broken_images).perform()
time.sleep(3)
driver.back()

# entry_ad_text_link = driver.find_element(By.XPATH, "//a[normalize-space()='Entry Ad']")
# act.context_click(entry_ad_text_link).perform()
# time.sleep(3)
# driver.back()
checkboxex_text_link = driver.find_element(By.XPATH, "//a[normalize-space()='Checkboxes']")
act.context_click(checkboxex_text_link).perform()
time.sleep(3)
driver.back()

drag_n_drop_text_link = driver.find_element(By.XPATH, "//a[normalize-space()='Drag and Drop']")
drag_n_drop_text_link.click()

time.sleep(3)
src = driver.find_element(By.XPATH,"//div[@id='column-a']")
des = driver.find_element(By.XPATH,"//div[@id='column-b']")
time.sleep(2)
act.drag_and_drop(src,des).perform()
driver.back()

