from revise.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class VerifyProductsnDetails(BasePage):
    product_btn = (By.XPATH, "//a[@href='/products']")

    verify_on_allProducts_page = (By.XPATH, "//h2[@class='title text-center']")
    category_list_product = (By.XPATH, "//h2[normalize-space()='Category']")
    brand_list_product = (By.XPATH, "//h2[normalize-space()='Brands']")

    first_product_btn = (By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]")

    product_name = (By.XPATH, "//h2[normalize-space()='Blue Top']")
    category = (By.XPATH, "//p[normalize-space()='Category: Women > Tops']")
    price = (By.XPATH, "//span[normalize-space()='Rs. 500']")
    availability = (By.XPATH, "//b[normalize-space()='Availability:']")
    condition = (By.XPATH, "//b[normalize-space()='Condition:']")
    brand = (By.XPATH, "//b[normalize-space()='Brand:']")

    search_input = (By.XPATH, "//input[@id='search_product']")
    search_btn = (By.XPATH, "//button[@id='submit_search']")

    searched_products = (By.XPATH, "//h2[@class='title text-center']")

    # 21 test case xpath
    write_your_review_text = (By.XPATH, "//a[normalize-space()='Write Your Review']")
    name_input = (By.XPATH, "//input[@id='name']")
    email_input = (By.XPATH, "//input[@id='email']")
    add_review_input = (By.XPATH, "//textarea[@id='review']")
    review_submit_btn = (By.XPATH, "//button[@id='button-review']")
    verify_success_msg_review_popup = (By.XPATH, "//span[normalize-space()='Thank you for your review.']")


    def clickProductBtn(self):
        self.click(*self.product_btn)

    def verfiyOnProductsPages(self):
        self.is_displayed(*self.verify_on_allProducts_page)

    def listProducts(self):
        self.is_displayed(*self.category_list_product)
        self.is_displayed(*self.brand_list_product)

    def clickFirstProduct(self):
        self.click(*self.first_product_btn)

    def verifyFirstProductDetails(self):
        self.is_displayed(*self.product_name)
        self.is_displayed(*self.category)
        self.is_displayed(*self.price)
        self.is_displayed(*self.availability)
        self.is_displayed(*self.condition)
        self.is_displayed(*self.brand)

    def searchProduct(self, productName):
        self.send_keys(*self.search_input, productName)
        self.click(*self.search_btn)
        self.is_displayed(*self.searched_products)


# 21 test case function
    def verfiy_write_review_text(self):
        self.is_displayed(*self.write_your_review_text)

    def fill_review_from(self, name, email, review):
        self.send_keys(*self.name_input, name)
        self.send_keys(*self.email_input, email)
        self.send_keys(*self.add_review_input, review)
        self.click(*self.review_submit_btn)
        self.is_displayed(*self.verify_success_msg_review_popup)
