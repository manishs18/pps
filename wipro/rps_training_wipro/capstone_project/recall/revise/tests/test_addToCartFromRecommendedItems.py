from selenium.webdriver.common.action_chains import ActionChains
from revise.pages.addToCartFromRecommendedItems import AddToCartFromRecommendedItems

def test_add_to_cart_from_recommended_items(driver):
    verify_items_recommended = AddToCartFromRecommendedItems(driver)
    verify_items_recommended.scroll_down_footer()
    verify_items_recommended.verify_recommended_item_text_visible()