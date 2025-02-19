from revise.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class AddToCartFromRecommendedItems(BasePage):
    recommended_items_text = (By.XPATH, "//h2[normalize-space()='recommended items']")
    blue_top_recommended_item = (By.XPATH, "//div[@class='item active']//div[1]//div[1]//div[1]//div[1]//a[1]")
    continue_shopping_btn = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    cart_btn = (By.LINK_TEXT, "Cart")


    def scroll_down_footer(self):
        element = self.driver.find_element(*self.recommended_items_text) 
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("window.scrollBy(0, -1000)")  

    def verify_recommended_item_text_visible(self):
        self.is_displayed(*self.recommended_items_text)
        self.click(*self.blue_top_recommended_item)
        self.click(*self.continue_shopping_btn)
        self.click(*self.cart_btn)
        self.is_displayed(*self.blue_top_recommended_item)