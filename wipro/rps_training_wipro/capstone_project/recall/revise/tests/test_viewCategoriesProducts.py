from revise.pages.viewCategoriesProducts import ViewCategoriesProduct


def test_view_categories_product(driver):
    vcp = ViewCategoriesProduct(driver)
    vcp.verify_categories()
    vcp.click_women_categories()
    vcp.click_men_categories()