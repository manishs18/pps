from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException

try:
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.maximize_window()

    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    time.sleep(2)

    act = ActionChains(driver)

    try:
        amazon_website = driver.find_element(By.XPATH, "//span[normalize-space()='Prime']")
        act.click_and_hold(amazon_website).perform()
        time.sleep(3)
    except NoSuchElementException:
        print("The element 'Prime' was not found on the page.")
    except Exception as e:
        print(f"An error occurred while performing the action: {e}")
    finally:
        act.release().perform()

except WebDriverException as e:
    print(f"WebDriver error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    driver.quit()
