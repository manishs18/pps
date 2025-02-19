from revise.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ViewCartBrandProduct(BasePage):
    products_btn = (By.XPATH, "//a[@href='/products']")
    brands_text = (By.XPATH, "//h2[normalize-space()='Brands']")
    polo_brands = (By.XPATH, "//a[@href='/brand_products/Polo']")
    polo_brands_page = (By.XPATH, "//h2[@class='title text-center']")
    mast_n_harbour_brands = (By.XPATH, "//a[@href='/brand_products/Mast & Harbour']")
    mast_n_harbour_brands_page = (By.XPATH, "//h2[@class='title text-center']")


    def click_products(self):
        self.click(*self.products_btn)

    def verify_polo_products(self):
        self.is_displayed(*self.brands_text)
        self.click(*self.polo_brands)
        self.is_displayed(*self.polo_brands_page)

    def verify_mast_n_harbour(self):
        self.click(*self.mast_n_harbour_brands)
        self.is_displayed(*self.mast_n_harbour_brands_page)