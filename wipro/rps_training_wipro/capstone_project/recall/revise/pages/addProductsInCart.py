from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from revise.pages.basePage import BasePage


class AddToCart(BasePage):
    product_btn = (By.XPATH, "//a[@href='/products']")
    view_product1 = (By.XPATH, '//a[@href="/product_details/1"]')
    view_product2 = (By.XPATH, '//a[@href="/product_details/2"]')
    addtocart_btn = (By.XPATH, "//button[@type='button']")
    continue_shoping_btn = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    cart_btn = (By.LINK_TEXT, "Cart")
    product1_price = (By.XPATH, "//td[@class='cart_price']//p[contains(text(),'Rs. 400')]")
    product1_quantity = (By.XPATH, "//tr[@id='product-2']//button[@class='disabled'][normalize-space()='1']")
    product1_total = (By.XPATH, "//p[@class='cart_total_price'][normalize-space()='Rs. 400']")
    product2_price = (By.XPATH, "//td[@class='cart_price']//p[contains(text(),'Rs. 1000')]")
    product2_quantity = (By.XPATH, "//tr[@id='product-3']//button[@class='disabled'][normalize-space()='1']")
    product2_total = (By.XPATH, "//p[@class='cart_total_price'][normalize-space()='Rs. 1000']")
    cross_to_remove_product1_btn = (By.XPATH, "//tr[@id='product-1']//i[@class='fa fa-times']")
    cross_to_remove_product2_btn = (By.XPATH, "//tr[@id='product-2']//i[@class='fa fa-times']")
    verfiy_cart_empty_text = (By.XPATH, "//b[normalize-space()='Cart is empty!']")


    def clickProductBtn(self):
        self.click(*self.product_btn)

    def add_to_cart(self):
        self.click(*self.view_product1)
        self.click(*self.addtocart_btn)
        self.click(*self.continue_shoping_btn)
        self.click(*self.product_btn)
        self.click(*self.view_product2)
        self.click(*self.addtocart_btn)
        self.click(*self.continue_shoping_btn)
        self.click(*self.cart_btn)
    
    def verify_products_added_to_cart(self):
        self.is_displayed(*self.view_product1)
        self.is_displayed(*self.view_product2)
        self.is_displayed(*self.product1_price)
        self.is_displayed(*self.product1_quantity)
        self.is_displayed(*self.product1_total)
        self.is_displayed(*self.product2_price)
        self.is_displayed(*self.product2_quantity)
        self.is_displayed(*self.product2_total)

    def remove_product_from_cart(self):
        self.click(*self.cross_to_remove_product1_btn)
        self.click(*self.cross_to_remove_product2_btn)

    def verify_cart_empty(self):
        self.is_displayed(*self.verfiy_cart_empty_text)

# for 20 test case function
    def view_product1_btn(self):
        self.click(*self.view_product1)

    def view_product2_btn(self):
        self.click(*self.view_product2)

    def add_to_cart_searched_product(self):
        self.click(*self.addtocart_btn)

    def click_continue_shoping_btn(self):
        self.click(*self.continue_shoping_btn)
    
    def click_cart_btn(self):
        self.click(*self.cart_btn)

    