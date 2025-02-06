import pytest
import time
from selenium.webdriver.common.by import By
from manish_ecp_pom.apps.pages.ProductsPage import Products


details = {
    "product_name": "Blue Top",
    "category": "Category: Women > Tops",
    "price": "Rs. 500",
    "availability": "Availability",
    "condition": "Condition",
    "brand": "Brand"
}

@pytest.mark.usefixtures("driver")
def test_products_page(driver):

    product_page = Products(driver)
    time.sleep(2)

    product_page.click_products()
    time.sleep(2)

    # Verify that each detail is visible
    for detail_id, detail_name in details.items():
        try:
            # Locate the element by ID, XPath, or CSS Selector (adjust based on your HTML)
            element = driver.find_element(By.ID, detail_id)
            assert element.is_displayed(), f"{detail_name} is not visible"
            print(f"{detail_name} is visible: {element.text}")
        except Exception as e:
            print(f"Failed to verify {detail_name}: {e}")