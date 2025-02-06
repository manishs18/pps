import pytest
from selenium import webdriver
from session_task_practice.pages.loginpage import LoginPage

@pytest.fixture
def driver():
    optional = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=optional)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Perform Login
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

@pytest.mark.skip
def test_social_media_links(driver):
    # Social media locators
    social_media_links = {
        "LinkedIn": "//a[contains(@href, 'linkedin')]",
        "Facebook": "//a[contains(@href, 'facebook')]",
        "Twitter": "//a[contains(@href, 'twitter')]",
        "YouTube": "//a[contains(@href, 'youtube')]"
    }

    for platform, xpath in social_media_links.items():
        # Find the social media link element
        social_media_icon = driver.find_element(By.XPATH, "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']//*[name()='svg']//*[name()='g' and contains(@fill,'currentCol')]//*[name()='path' and contains(@class,'st0')]")
        
        # Ensure the element is displayed
        assert social_media_icon.is_displayed(), f"{platform} icon is not displayed."
        
        # Get the href attribute of the link
        href = social_media_icon.get_attribute("href")
        print(f"{platform} link: {href}")

        # Verify the href is correct
        assert platform.lower() in href.lower(), f"Unexpected URL for {platform} link."