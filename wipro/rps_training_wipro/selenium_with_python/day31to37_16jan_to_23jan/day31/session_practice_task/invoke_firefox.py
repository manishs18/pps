from selenium import webdriver

option = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=option)
driver.maximize_window()
driver.get('https://ogmt.koyeb.app/')