from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()  
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)

file_path = r"C:\Users\mkuma\OneDrive\Desktop\manish.png"
choose_file_button = driver.find_element(By.ID, "file-upload")  
choose_file_button.send_keys(file_path)  

upload_button = driver.find_element(By.ID, "file-submit") 
upload_button.click()

time.sleep(2)
driver.quit()
