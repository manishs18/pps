from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_page_button = (By.CSS_SELECTOR, "a[href='/products']")
        self.first_product = (By.CSS_SELECTOR, "a[href='/product_details/1']")
        self.first_add_to_cart_button = (By.CSS_SELECTOR, "button[type='button']")
        self.second_product = (By.CSS_SELECTOR, "a[href='/product_details/3']")
        self.second_add_to_cart_button = (By.CSS_SELECTOR, "button[type='button']")
        self.continue_shopping_button = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
        self.view_cart_button = (By.CSS_SELECTOR, ".btn-view-cart")

    def click_products(self):
        """Navigate to the Products page."""
        products_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.products_page_button)
        )
        products_button.click()

    def hover_and_add_to_cart(self, product_locator, add_to_cart_locator):
        """Hover over a product and add it to the cart."""
        # Wait for the product to be visible
        product_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(product_locator)
        )

        # Hover over the product
        ActionChains(self.driver).move_to_element(product_element).perform()

        # Wait for 'Add to Cart' button to be clickable
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(add_to_cart_locator)
        )

        # Click 'Add to Cart'
        add_to_cart_button.click()

    def click_continue_shopping(self):
        """Click the 'Continue Shopping' button."""
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_shopping_button)
        )
        continue_button.click()

    def click_view_cart(self):
        """Click the 'View Cart' button."""
        view_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.view_cart_button)
        )
        view_cart_button.click()
