from revise.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class VerifyProductOnCart(BasePage):
    view_product8 = (By.XPATH, '//a[@href="/product_details/8"]')

    product8_name = (By.XPATH, "//h2[normalize-space()='Fancy Green Top']")
    category_details = (By.XPATH, "//p[normalize-space()='Category: Women > Tops']")
    rating = (By.XPATH, "//img[@src='/static/images/product-details/rating.png']")
    product_price = (By.XPATH, "//span[normalize-space()='Rs. 700']")
    product_availability = (By.XPATH, "//b[normalize-space()='Availability:']")
    # in_stock = (By.XPATH, "//div[@class='product-details']//p[1]")
    product_conditions = (By.XPATH, "//b[normalize-space()='Condition:']")
    # new_condtions = (By.XPATH, "//body//section//p[3]")
    product_brand = (By.XPATH, "//b[normalize-space()='Brand:']")
    # brand = (By.XPATH, "//div[@class='product-details']//p[1]")
    quantiity = (By.XPATH, "//input[@id='quantity']")
    # <input type="number" name="quantity" id="quantity" value="1" min="1" fdprocessedid="5ft8ne">
    add_to_cart_btn = (By.XPATH, "//button[@type='button']")

    continue_shoping_btn = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")

    cart_btn = (By.LINK_TEXT, "Cart")

    product_cart_quantity = (By.XPATH, "//button[@class='disabled']")

    total_price_product = (By.XPATH, "//p[@class='cart_total_price']")


    def verify_product_opened(self):
        self.click(*self.view_product8)
    
    def verify_product_details(self):
        self.is_displayed(*self.product8_name)
        self.is_displayed(*self.category_details)
        self.is_displayed(*self.rating)
        self.is_displayed(*self.product_price)
        self.is_displayed(*self.product_availability)
        self.is_displayed(*self.product_conditions)
        self.is_displayed(*self.product_brand)
        self.click(*self.quantiity)
        self.click(*self.quantiity)
        self.click(*self.add_to_cart_btn)
        self.click(*self.continue_shoping_btn)

    def verify_product_dispaly_on_cart(self):
        self.click(*self.cart_btn)
        self.is_displayed(*self.product_price)
        self.is_displayed(*self.product_cart_quantity)
        self.is_displayed(*self.total_price_product)
