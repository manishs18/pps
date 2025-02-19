from revise.pages.viewAndCartBrandProduct import ViewCartBrandProduct


def test_view_and_cart_brand_product(driver):
    verify_ViewCartBrandProduct = ViewCartBrandProduct(driver)
    verify_ViewCartBrandProduct.click_products()
    verify_ViewCartBrandProduct.verify_polo_products()
    verify_ViewCartBrandProduct.verify_mast_n_harbour()