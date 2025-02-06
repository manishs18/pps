import time
import pytest
from manish_ecp_pom.apps.pages.ScrollPage import ScrollPage

@pytest.mark.usefixtures("driver")
def test_scroll_with_arrow(driver):
    scroll_page = ScrollPage(driver)
    time.sleep(2)

    # Step 1: Verify the home page is visible successfully
    assert "Automation Exercise" in driver.title

    # Step 2: Scroll down to 'SUBSCRIPTION' and verify its visibility
    subscription_element = scroll_page.scroll_to_subscription()
    time.sleep(2)
    assert scroll_page.is_subscription_visible()

    # Step 3: Click on the 'Arrow' button at bottom right to move up
    scroll_page.click_scroll_up_arrow()
    time.sleep(2)  # Wait for scroll to top

    # Step 4: Verify 'Full-Fledged practice website for Automation Engineers' text is visible
    assert scroll_page.is_full_fledged_text_visible()
