from selenium import webdriver

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()


driver.get("https://ogmt.koyeb.app/")

# get title of the web page
title = driver.title
print(title)

# get page source return the html code of the web page
pagesource = driver.page_source
print(pagesource)

#get current url
current_url = driver.current_url
print(current_url)

driver.close()

#driver.quit()


