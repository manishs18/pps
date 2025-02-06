from selenium import webdriver

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)  
driver.get("https://ogmt.koyeb.app/")
driver.maximize_window()