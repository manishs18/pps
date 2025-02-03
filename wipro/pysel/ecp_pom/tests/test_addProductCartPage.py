import pytest
from selenium import webdriver
from ecp_pom.apps.homePage import HomePage
from ecp_pom.apps.addProductCartPage import ProductPage

@pytest.fixture
def driver():
    # Setup WebDriver (using Chrome as an example)
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_products_to_cart(driver):
    # Navigate to homepage
    driver.get("http://automationexercise.com")

    # Verify homepage is visible
    assert "Automation Exercise" in driver.title

    # Step 4: Navigate to Products page
    product_page = ProductPage(driver)
    product_page.click_products()

    # Step 5-6: Hover over first product, add to cart, and continue shopping
    product_page.hover_and_add_to_cart(
        product_page.first_product,
        product_page.first_add_to_cart_button
    )
    product_page.click_continue_shopping()

    # Step 7-8: Hover over second product and add to cart
    product_page.hover_and_add_to_cart(
        product_page.second_product,
        product_page.second_add_to_cart_button
    )
    product_page.click_view_cart()

    # Step 9: Verify both products are added to the cart
    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
    assert len(cart_items) == 2
    # Step 10: Verify prices, quantity, and total price
    first_product_price = driver.find_element(By.CSS_SELECTOR, "(tr[id='product-1'] td[class='cart_price'] p")
    second_product_price = driver.find_element(By.CSS_SELECTOR, "tr[id='product-3'] td[class='cart_price'] p")
    assert first_product_price.text == "Rs. 1500"
    assert second_product_price.text == "Rs. 1000"
