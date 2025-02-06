from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()

driver.get("https://www.tutorialspoint.com/selenium/practice/date-picker.php")
time.sleep(3)


time.sleep(3)
select_date_time_btn_box = driver.find_element(By.ID, "datetimepicker1")
select_date_time_btn_box.click()
time.sleep(3)

btn_nxt_month = driver.find_element(By.XPATH, "//span[@class='flatpickr-next-month']")
btn_nxt_month.click()
time.sleep(3)
btn_nxt_month.click()
time.sleep(3)
 
choose_date = driver.find_element(By.XPATH, '//span[@aria-label="March 11, 2025"]')
choose_date.click()
time.sleep(3)

choose_hour = driver.find_element(By.XPATH, "//input[@aria-label='Hour']")
choose_hour.send_keys("4")
time.sleep(3)

choose_minutes = driver.find_element(By.XPATH, "//input[@aria-label='Minute']")
choose_minutes.send_keys("20")
time.sleep(3)

choose_am_pm= driver.find_element(By.XPATH, '//span[@class="flatpickr-am-pm"]')
choose_am_pm.click()
time.sleep(3)

driver.execute_script("window.scrollBy(0,-600)")
time.sleep(3)

driver.quit()
