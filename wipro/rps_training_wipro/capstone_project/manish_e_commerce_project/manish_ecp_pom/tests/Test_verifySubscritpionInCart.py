import time
import pytest
from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.SubscriptionPage import Subscription
from manish_ecp_pom.apps.pages.HomePage import HomePage

@pytest.mark.usefixtures("driver")
def test_verify_subscription(driver):
    home_page = HomePage(driver)
    time.sleep(2)
    subscription_page = Subscription(driver)
    time.sleep(2)

    home_page.click_cart()
    time.sleep(2)

    SUBSCRIPTION = driver.find_element(By.XPATH, "//h2[normalize-space()='Subscription']")
    driver.execute_script("arguments[0].scrollIntoView();", SUBSCRIPTION)
    time.sleep(2)

    subscription_page.move_to_subscription("manish123@gmail.com")
    time.sleep(2)