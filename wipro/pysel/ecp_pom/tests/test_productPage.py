# import time
# import pytest
# from selenium import webdriver

# from POM.Pages.Product_Page import ProductPage
# from POM.Pages.homepage import HomePage
# from POM.Pages.loginPage import LoginPage


# @pytest.fixture()
# def driver():
#     option = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=option)
#     driver.maximize_window()
#     driver.get('https://www.automationexercise.com/')
#     yield driver
#     driver.quit()


# def test_product(driver):
#     hp = HomePage(driver)
#     text = hp.get_page_title()
#     print(text.__contains__("Automation Exercise"))
#     product = ProductPage(driver)
#     product.click_product()
#     text = product.check_display()
#     time.sleep(3)
#     print(text.__contains__("ALL PRODUCTS"))
#     total = product.check_display_Product()
#     if len(total) > 0:
#         print("Product Displayed")
#     else:
#         print("not Displayed")
#     time.sleep(3)
#     # product_name, category, available, condition, brand = product.details_Product()
#     # print(product_name.is_displayed())





import pytest
from selenium import webdriver
from ecp_pom.apps.productPage import ProductPage
from ecp_pom.apps.homePage import HomePage

@pytest.fixture()
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://www.automationexercise.com/')
    yield driver
    driver.quit()

def test_product(driver):
    # Verify homepage
    hp = HomePage(driver)
    assert "Automation Exercise" in hp.get_page_title(), "Homepage title does not match"

    # Navigate to products
    product = ProductPage(driver)
    product.click_product()
    assert "ALL PRODUCTS" in product.check_display(), "Failed to navigate to ALL PRODUCTS page"

    # Verify products list
    total = product.check_display_Product()
    assert len(total) > 0, "Products are not displayed"

    # View first product details
    product_name, category, available, condition, brand = product.details_Product()

    # Assertions with expected values
    assert product_name == "Blue Top"
    assert category == "Category: Women > Tops"
    assert available == "Availability: In Stock"
    assert condition == "Condition: New"
    assert brand == "Brand: Polo"