from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)

# Brocolli = driver.find_element(By.XPATH, "//img[@alt='Brocolli - 1 Kg']")

add_card_btn1 = driver.find_element(By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]")
add_card_btn1.click()
time.sleep(3)

add_card_btn2 = driver.find_element(By.XPATH, "//div[2]//div[3]//button[1]")
add_card_btn2.click()
time.sleep(3)

go_to_cart = driver.find_element(By.XPATH, "//img[@alt='Cart']")
go_to_cart.click()
time.sleep(3)


proced_to_checkbox = driver.find_element(
    By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")
proced_to_checkbox.click()
time.sleep(4)
