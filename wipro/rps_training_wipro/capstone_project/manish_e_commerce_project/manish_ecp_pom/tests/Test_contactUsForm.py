import pytest
import time
from manish_ecp_pom.apps.pages.ContactPage import Contact


@pytest.mark.usefixtures("driver")
def test_valid_login(driver):
    contact_page = Contact(driver)
    time.sleep(2)

    contact_page.click_contact_us()
    time.sleep(2)

    contact_page.verify_get_in_touch()
    time.sleep(2)

    contact_page.contact_us_form("Manish","Manish123@gmail.com", "feedback",
                                 "Nice product.", r"C:\Users\mkuma\OneDrive\Desktop\my_repo\ManishDTA\capstone_project\manish_e_commerce_project\manish_ecp_pom\tests\manishdoc.png")
    time.sleep(2)

    contact_page.alert_popup()
    time.sleep(2)

