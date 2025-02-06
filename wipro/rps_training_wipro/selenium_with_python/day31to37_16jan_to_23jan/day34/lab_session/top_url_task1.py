from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


try:
    # Initialize Edge WebDriver with optional settings
    optional = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=optional)
    driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    act = ActionChains(driver)
    time.sleep(4)
    hold = driver.find_element(By.ID,'mousehover')
    time.sleep(3)
    driver.execute_script('arguments[0].scrollIntoView()',hold)
    top = driver.find_element(By.XPATH,"//a[contains(text(),'Top')]")
    time.sleep(3)
    seriesfactions = act.move_to_element(hold).click().move_to_element(top).click()
    seriesfactions.perform()
    time.sleep()

    str = driver.current_url
    print(str)
    if "top" in str:
        print(True)
    else:
        print(False)

except Exception as e:
    print(e)


