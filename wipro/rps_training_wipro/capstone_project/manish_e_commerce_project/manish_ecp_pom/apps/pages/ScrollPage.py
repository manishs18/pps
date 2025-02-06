from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from manish_ecp_pom.apps.pages.BasePage import BasePage

class ScrollPage(BasePage):

    # Locators
    subscription_locator = (By.XPATH, "//h2[normalize-space()='Subscription']")
    full_fledged_text_locator = (By.XPATH, "//h2[contains(text(),'Full-Fledged practice website for Automation Engineers')]")
    scroll_arrow_locator = (By.ID, "scrollUp")

    # Methods
    def scroll_to_subscription(self):
        subscription_element = self.driver.find_element(*self.subscription_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", subscription_element)
        return subscription_element

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def is_subscription_visible(self):
        return self.driver.find_element(*self.subscription_locator).is_displayed()

    def is_full_fledged_text_visible(self):
        return self.driver.find_element(*self.full_fledged_text_locator).is_displayed()

    def click_scroll_up_arrow(self):
        """Clicks on the scroll-up arrow button."""
        arrow_button = self.driver.find_element(*self.scroll_arrow_locator)
        ActionChains(self.driver).move_to_element(arrow_button).click().perform()

