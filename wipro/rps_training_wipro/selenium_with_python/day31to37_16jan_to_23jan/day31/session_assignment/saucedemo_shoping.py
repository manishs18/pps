from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

time.sleep(2)
username = driver.find_element(By.NAME, "user-name")
username.send_keys("standard_user")

time.sleep(2)

password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

time.sleep(2)
login = driver.find_element(By.NAME, "login-button")
login.click()

time.sleep(2)
addCart = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
addCart.click()

time.sleep(2) 
cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()

checkout = driver.find_element(By.NAME, "checkout")
checkout.click()

time.sleep(2)
firstname = driver.find_element(By.NAME, "firstName")
firstname.send_keys("Manish")

time.sleep(2)
lastname = driver.find_element(By.NAME, "lastName")
lastname.send_keys("Shrestha")

time.sleep(2)
postalcode = driver.find_element(By.NAME, "postalCode")
postalcode.send_keys("123564")

time.sleep(2)
cont = driver.find_element(By.XPATH, "//input[@id='continue']")
cont.click()

time.sleep(2)
finish = driver.find_element(By.NAME, "finish")
finish.click()
time.sleep(2)

driver.quit()
