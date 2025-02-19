from revise.pages.basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class ProceedPlaceOrder(BasePage):
    proceed_to_checkout_btn = (By.XPATH, "//a[@class='btn btn-default check_out']")
    register_login_btn = (By.XPATH, "//u[normalize-space()='Register / Login']")
    cart_btn = (By.LINK_TEXT, "Cart")
    address_details_text = (By.XPATH, "//h2[normalize-space()='Address Details']")
    verify_address_details_text = (By.XPATH, "//div[@xpath='2']")
    review_your_order_text = (By.XPATH, "//h2[normalize-space()='Review Your Order']")
    verify_review_your_order_text = (By.XPATH, "//div[@id='cart_info']")
    desc_text_comment_box = (By.XPATH, "//textarea[@name='message']")
    place_order_btn = (By.XPATH, "//a[@class='btn btn-default check_out']")
    name_on_card_input = (By.XPATH, "//input[@name='name_on_card']")
    card_no_input = (By.XPATH, "//input[@name='card_number']")
    cv_input = (By.XPATH, "//input[@placeholder='ex. 311']")
    month_input = (By.XPATH, "//input[@placeholder='MM']")
    year_input = (By.XPATH, "//input[@placeholder='YYYY']")
    pay_n_confirm_order_btn = (By.XPATH, "//button[@id='submit']")
    congratulation_order_success_popup = (By.XPATH, "//p[normalize-space()='Congratulations! Your order has been confirmed!']")
    delete_account_btn = (By.XPATH, "//a[normalize-space()='Delete Account']")
    # verify_account_deleted_popup = (By.XPATH, "")

    download_invoice_btn = (By.XPATH, "//a[@class='btn btn-default check_out']")
    continue_btn = (By.LINK_TEXT, "Continue")
    


    def click_proceed_checkout(self):
        self.click(*self.proceed_to_checkout_btn)
    
    def click_register_login(self):
        self.click(*self.register_login_btn)

    def click_cart_btn(self):
        self.click(*self.cart_btn)

    def verify_review_addressdetails_n_order(self):
        self.is_displayed(*self.address_details_text)
        self.is_displayed(*self.verify_address_details_text)
        self.is_displayed(*self.review_your_order_text)
        self.is_displayed(*self.verify_review_your_order_text)

    def comment_n_place_order(self, comment):
        self.send_keys(*self.desc_text_comment_box, comment)
        self.click(*self.place_order_btn)

    def payment_details(self, card_name, card_no, cv_no, month, year):
        self.send_keys(*self.name_on_card_input, card_name)
        self.send_keys(*self.card_no_input, card_no)
        self.send_keys(*self.cv_input, cv_no)
        self.send_keys(*self.month_input, month)
        self.send_keys(*self.year_input, year)
        self.click(*self.pay_n_confirm_order_btn)

    def verify_order_placed_successfully(self):
        self.is_displayed(*self.congratulation_order_success_popup)

    def download_invoice(self):
        self.click(*self.download_invoice_btn)
    
    def click_continue_btn(self):
        self.click(*self.continue_btn)

    # def verify_account_deleted(self):
    #     self.click(*self.delete_account_btn)
    #     self.is_displayed(*self.verify_account_deleted_popup)