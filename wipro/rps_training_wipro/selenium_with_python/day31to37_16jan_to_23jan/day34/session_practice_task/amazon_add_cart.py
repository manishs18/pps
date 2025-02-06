from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
import time

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
time.sleep(2)

act = ActionChains(driver)

amazon_website = driver.find_element(By.XPATH, "//span[normalize-space()='Prime']")

act.click_and_hold(amazon_website).perform()
time.sleep(3)

driver.quit()
