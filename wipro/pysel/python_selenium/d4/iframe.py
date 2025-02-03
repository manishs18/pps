from selenium import webdriver
from selenium.webdriver.common.by import By
import time


optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get("https://demoqa.com/frames")
time.sleep(2)

fr = driver.find_element(By.ID, "frame1")
# driver.switch_to.frame(fr)

driver.switch_to.frame(0)
time.sleep(3)

text = driver.find_element(By.ID, value="sampleHeading")
trr = text.is_displayed()
print(trr)
# driver.switch_to.frame(0)
time.sleep(3)

# fr1 = driver.find_element(By.ID, "frame2")
# driver.switch_to.frame(fr1)

# # driver.switch_to.frame(0)
# # time.sleep(3)

# text1 = driver.find_element(By.ID, value="sampleHeading")
# driver.switch_to.frame(0)
# time.sleep(3)