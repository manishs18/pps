import pytest
from selenium import webdriver
from ecp_pom.apps.subscriptionPage import HomePage


class TestSubscription:

    @pytest.fixture()
    def driver(self):
        # Setup browser
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=option)
        driver.maximize_window()
        driver.get('https://www.automationexercise.com/')
        yield driver
        driver.quit()  # Close browser after test

    def test_verify_subscription(self, driver):
        # Instantiate HomePage with the driver
        home_page = HomePage(driver)

        # Step 3: Verify home page visibility
        home_page.verify_home_page()

        # Step 4: Scroll down to footer
        home_page.scroll_to_footer()

        # Step 5: Verify 'Subscription' text
        home_page.verify_subscription_text()

        # Step 6: Enter email and click subscribe
        home_page.enter_email_and_subscribe("test@example.com")



if __name__ == "__main__":
    pytest.main()
