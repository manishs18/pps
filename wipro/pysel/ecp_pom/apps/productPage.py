from pycparser.c_ast import Return
from selenium.webdriver.common.by import By
from ecp_pom.apps.basePage import BasePage


class ProductPage(BasePage):
    Product_Button = (By.XPATH,"//a[@href='/products']")
    Product_page = (By.CSS_SELECTOR,"h2[class='title text-center']")
    Product_List = (By.XPATH,"//div[@class='productinfo text-center']")
    First_Product = (By.XPATH,"//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]")
    Product_Name = (By.XPATH,"//h2[normalize-space()='Blue Top']")
    Category = (By.XPATH,"//p[normalize-space()='Category: Women > Tops']")
    Available = (By.XPATH,"//b[normalize-space()='Availability:']")
    Condition =(By.XPATH,"//b[normalize-space()='Condition:']")
    Brand = (By.XPATH,"//b[normalize-space()='Brand:']")
    def click_product(self):
        self.click(*self.Product_Button)
    def check_display(self):
        return self.get_text(*self.Product_page)
    def check_display_Product(self):
        return self.find_elements(*self.Product_List)
    def details_Product(self):
        self.click(*self.First_Product)
        product_name =self.get_text(*self.Product_Name)
        category = self.wait_for_element(*self.Category)
        available = self.wait_for_element(*self.Available)
        condition = self.wait(*self.Condition)
        brand = self.wait_for_element(*self.Brand)
        return product_name,category,available,condition,brand


