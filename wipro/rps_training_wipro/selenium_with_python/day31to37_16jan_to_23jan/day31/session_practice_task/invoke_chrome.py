from selenium import webdriver

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

driver.maximize_window()
driver.get('https://ogmt.koyeb.app/')

