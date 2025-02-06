from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains, Keys

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://ogmt.koyeb.app/")
time.sleep(2)

act = ActionChains(driver)   

login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Log In']")
login_btn.click()

email = driver.find_element(By.XPATH, '''//button[@type="//input[@id='loginusername']"]''')
seriesofactions = act.move_to_element(email).key_down(Keys.SHIFT).send_keys("manish12@gmail.com") 
seriesofactions.perform()           