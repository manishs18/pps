import pytest
from selenium import webdriver
from ecp_pom.apps.homePage import HomePage
from ecp_pom.apps.cartSubscriptionPage import CartPage


class TestCartSubscription:

    @pytest.fixture()
    def driver(self):
        # Setup browser
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=option)
        driver.maximize_window()
        driver.get('https://www.automationexercise.com/')
        yield driver
        driver.quit()  # Close browser after test

    def test_verify_subscription_in_cart(self, driver):
        # Step 4: Navigate to Cart page
        cart_page = CartPage(driver)
        cart_page.click_cart()

        # Step 4: Scroll down to footer
        cart_page.scroll_to_footer()

        # Step 5: Verify 'Subscription' text
        cart_page.verify_subscription_text()

        # Step 6: Enter email and click subscribe
        cart_page.enter_email_and_subscribe("test@example.com")


if __name__ == "__main__":
    pytest.main()
