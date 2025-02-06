from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager")
time.sleep(2) 

add_customer_button = driver.find_element(By.XPATH, "//button[@ng-class='btnClass1']")
add_customer_button.click()
time.sleep(2)

first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
post_code = driver.find_element(By.XPATH, "//input[@placeholder='Post Code']")

first_name.send_keys("Manish")
last_name.send_keys("Singh")
post_code.send_keys("12345")
time.sleep(1)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
time.sleep(1)

alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(1)

time.sleep(2)
open_account = driver.find_element(By.XPATH, "//button[@ng-click='openAccount()']")
open_account.click()
time.sleep(2)

username_dropdown = driver.find_element(By.ID, "userSelect")
time.sleep(2)
select_user = Select(username_dropdown)
select_user.select_by_visible_text('Manish Singh')
time.sleep(3)

currency_dropdown = driver.find_element(By.XPATH, "//select[@id='currency']")
time.sleep(2)
currency_select = Select(currency_dropdown)
currency_select.select_by_value("Rupee")
time.sleep(3)

process_button = driver.find_element(By.XPATH, "//button[@type='submit']")
time.sleep(3)
process_button.click()
time.sleep(3)

alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(1)

customers_tab = driver.find_element(By.XPATH, "//button[@ng-click='showCust()']")
customers_tab.click()
time.sleep(3)

search_customer = driver.find_element(By.XPATH, "//input[@type='text']")
time.sleep(3)

search_customer.send_keys("Manish Singh")
time.sleep(3)
if search_customer.is_displayed():
    time.sleep(3)
    print("Customer name Manish Singh is Present")
else:
    print("No such customer name Manish Singh exist.")

