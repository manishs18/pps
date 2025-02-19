from selenium.webdriver.common.by import By
from revise.pages.basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class  ViewCategoriesProduct(BasePage):
    categories_text = (By.XPATH, "//h2[normalize-space()='Category']")
    women_categories = (By.XPATH, "//a[normalize-space()='Women']")
    dress_women_categories = (By.XPATH, "//div[@id='Women']//a[contains(text(),'Dress')]")
    women_dress_product_text = (By.XPATH, "//h2[@class='title text-center']")
    men_categories = (By.XPATH, "//a[normalize-space()='Men']")
    tshirt_men_categories = (By.XPATH, "//a[normalize-space()='Tshirts']")
    men_tshirt_product_text = (By.XPATH, "//h2[@class='title text-center']")

    def verify_categories(self):
        self.is_displayed(*self.categories_text)

    def click_women_categories(self):
        self.click(*self.women_categories)
        self.click(*self.dress_women_categories)
        self.is_displayed(*self.women_dress_product_text)

    def click_men_categories(self):
        self.click(*self.men_categories)
        self.click(*self.tshirt_men_categories)
        self.is_displayed(*self.men_tshirt_product_text)