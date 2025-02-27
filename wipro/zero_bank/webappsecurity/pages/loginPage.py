from webappsecurity.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


class LoginPage(BasePage):
    signin_btn = (By.XPATH, "//button[@id='signin_button']")
    login_input_btn = (By.XPATH, "//input[@id='user_login']")
    pwd_input_btn = (By.XPATH, "//input[@id='user_password']")
    checkbox_select = (By.XPATH, "//input[@id='user_remember_me']")
    submit_signin_btn = (By.XPATH, "//input[@name='submit']")
    online_bank_link_text = (By.XPATH, "//strong[normalize-space()='Online Banking']")
    account_summary_link_text = (By.XPATH, "//span[@id='account_summary_link']")
    check_loogged_with_username = (By.XPATH, "//a[normalize-space()='username']")
# 2nd test xpath
    cash_accounts_text = (By.XPATH, "//h2[normalize-space()='Cash Accounts']")
    savings_accounts_link_text = (By.LINK_TEXT, "Savings")
    savings_accounts_balance_text = (By.XPATH, "//td[normalize-space()='$1000']")
    credit_account_text = (By.XPATH, "//h2[normalize-space()='Credit Accounts']")
    checking_link_text = (By.XPATH, "//a[normalize-space()='Checking']")
    checking_balance_text = (By.XPATH, "//td[normalize-space()='$-500.2']")
    credit_card_link_text = (By.XPATH, "//a[normalize-space()='Credit Card']")
    credit_card_balance_text = (By.XPATH, "//td[normalize-space()='$-265']")
# 3rd test xpath
    transfer_funds_link_text = (By.XPATH, "//span[@id='transfer_funds_link']")
    select_from_account_arrow_btn = (By.XPATH, "//select[@id='tf_fromAccountId']")
    to_account_arrow_btn = (By.XPATH, "//select[@id='tf_toAccountId']")
    amount_input_btn = (By.XPATH, "//input[@id='tf_amount']")
    description_input_btn = (By.XPATH, "//input[@id='tf_description']")
    continue_btn = (By.XPATH, "//button[@id='btn_submit']")
    submit_btn = (By.XPATH, "//button[@id='btn_submit']")
    success_transfer_popup_msg = (By.XPATH, "//div[@class='alert alert-success']")

# 4th test xpath
    pay_bills_link_text = (By.XPATH, "//span[@id='pay_bills_link']")
    payee_select_arrow_dropdwb_btn = (By.XPATH, "//select[@id='sp_payee']")
    account_select_arrow_dropdwn_btn = (By.XPATH, "//select[@id='sp_account']")
    amt_input_btn = (By.XPATH, "//input[@id='sp_amount']")
    date_input_btn = (By.XPATH, "//input[@id='sp_date']")
    date_right_btn = (By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']")
    descriptions_input_btn = (By.XPATH, "//input[@id='sp_description']")
    pay_btn = (By.XPATH, "//input[@id='pay_saved_payees']")
    success_pay_popup_msg = (By.XPATH, "//span[@title='$ 100 payed to payee sprint']")

# 5th test xpath
    account_activity_link_text = (By.XPATH, "//span[@id='account_activity_link']")
    select_dropdwn_account = (By.XPATH, "//select[@id='aa_accountId']")
    find_transactions_link_text = (By.XPATH, "//a[normalize-space()='Find Transactions']")
    description_search_input_box = (By.XPATH, "//input[@id='aa_description']")
    find_btn = (By.XPATH, "//button[@type='submit']")
    desc_transaction_verify_text = (By.NAME, "CAR PAYMENT")
    date_transaction_verify_text = (By.NAME, "2012-09-01")
    withdrawal_amt_text = (By.NAME, "1548")

    def login_with_valid_cred(self, id, pwd):
        self.click(*self.signin_btn)
        self.send_keys(*self.login_input_btn, id)
        self.send_keys(*self.pwd_input_btn, pwd)
        self.click(*self.checkbox_select)
        self.click(*self.submit_signin_btn)

    def verify_logged_id_n_account_summary(self):
        self.is_displayed(*self.online_bank_link_text)
        self.click(*self.online_bank_link_text)
        self.is_displayed(*self.account_summary_link_text)
        self.click(*self.account_summary_link_text)
        self.is_displayed(*self.check_loogged_with_username)
    
    def account_summary_verification(self):
        self.is_displayed(*self.cash_accounts_text)
        self.is_displayed(*self.savings_accounts_link_text)
        self.is_displayed(*self.savings_accounts_balance_text)
        self.is_displayed(*self.credit_account_text)
        self.is_displayed(*self.checking_link_text)
        self.is_displayed(*self.checking_balance_text)
        self.is_displayed(*self.credit_card_link_text)
        self.is_displayed(*self.credit_card_balance_text)

    def transfer_funds(self, amt, desc):
        self.click(*self.transfer_funds_link_text)

        select_from_drpdwn = self.wait_for_element(*self.select_from_account_arrow_btn)
        select_savings = Select(select_from_drpdwn)
        select_savings.select_by_index(1)

        select_credit = self.get_dropdown(*self.to_account_arrow_btn)
        select_credit.select_by_index(5)

        self.send_keys(*self.amount_input_btn, amt)
        self.send_keys(*self.description_input_btn, desc)

        self.click(*self.continue_btn)
        self.click(*self.submit_btn)
        self.is_displayed(*self.success_transfer_popup_msg)

    def pay_bills(self, amount, description):
        self.click(*self.online_bank_link_text)
        self.click(*self.pay_bills_link_text)

        select_payee = self.get_dropdown(*self.payee_select_arrow_dropdwb_btn)
        select_payee.select_by_visible_text("Wells Fargo")

        select_froms_drpdwn = self.wait_for_element(*self.account_select_arrow_dropdwn_btn)
        select_accounts = Select(select_froms_drpdwn)
        select_accounts.select_by_visible_text("Savings")

        self.send_keys(*self.amt_input_btn, amount)

        # self.click(*self.date_input_btn)
        # self.click(*self.date_right_btn)
        # date_select_drpdwn = self.wait_for_element(*self.date_input_btn)
        # select_date = Select(date_select_drpdwn)
        # select_date.select_by_visible_text('12')

        self.send_keys(*self.date_input_btn,"2025-01-22")

        self.send_keys(*self.descriptions_input_btn, description)
        self.click(*self.pay_btn)
        self.is_displayed(*self.success_pay_popup_msg)

    def searchForTransactions(self, search_ip_transaction):
        self.click(*self.online_bank_link_text)
        self.click(*self.account_activity_link_text)

        select_account_from_drpdwn = self.wait_for_element(*self.select_dropdwn_account)
        select_savings = Select(select_account_from_drpdwn)
        select_savings.select_by_index(2)

        self.click(*self.find_transactions_link_text)
        self.send_keys(*self.description_search_input_box, search_ip_transaction)
        self.click(*self.find_btn)
        self.is_displayed(*self.desc_transaction_verify_text)
        self.is_displayed(*self.date_transaction_verify_text)
        self.is_displayed(*self.withdrawal_amt_text)



