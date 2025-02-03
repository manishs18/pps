'''
The Metro Bank provides various types of loans such as car loans, business loans and house loans to its account holders. 
Write a python program to implement the following

requirements:

-> Initialize the following variables with appropriate input values: 
   account number, account balance, salary, loan_type, loan_amount_expected and customer_emi_expected.
-> The account number should be of 4 digits and its first digit should be 1.
-> The customer should have a minimum balance of Rupees 1 Lakh in the account.
-> If the above rules are valid, determine the eligible loan amount 
   and the EMI that the bank can provide to its customers based on their salary and the loan type they expect to avail.
-> The bank would provide the loan, only if the loan amount and the number of EMI's 
   requested by the customer is less than or equal to the loan amount and the number of EMI's decided by the bank respectively.

Display appropriate error messages for all invalid data. If all the business rules are satisfied, 
then display account number, eligible and requested loan amount and EMI's Test your code by providing different values for the input variables.

Salary   Loan type    Eligible loan amount     No. of EMI's required to repay
>25000   Car          500000                   36
>50000   House        6000000                  60
>75000   Business     7500000                  84

'''

def calculate_loan(account_number, account_balance, salary, loan_type, loan_amount_expected, customer_emi_expected):
    if len(str(account_number)) != 4 or str(account_number)[0] != '1':
        print("Invalid account number")
        return
    
    if account_balance < 100000:
        print("Insufficient account balance")
        return
    
    eligible_loan_amount = 0
    eligible_emi = 0
    
    if loan_type == "Car" and salary > 25000:
        eligible_loan_amount = 500000
        eligible_emi = 36
    elif loan_type == "House" and salary > 50000:
        eligible_loan_amount = 6000000
        eligible_emi = 60
    elif loan_type == "Business" and salary > 75000:
        eligible_loan_amount = 7500000
        eligible_emi = 84
    else:
        print("Invalid loan type or salary not sufficient")
        return
    
    if loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= eligible_emi:
        print("Account number:", account_number)
        print("Eligible loan amount:", eligible_loan_amount)
        print("Requested loan amount:", loan_amount_expected)
        print("Eligible EMI:", eligible_emi)
        print("Requested EMI:", customer_emi_expected)
    else:
        print("The requested loan amount or EMI exceeds eligibility")

calculate_loan(1001, 150000, 30000, "Car", 400000, 30)  # Valid case
calculate_loan(2001, 150000, 30000, "Car", 400000, 30)  # Invalid account number
calculate_loan(1001, 90000, 30000, "Car", 400000, 30)   # Insufficient account balance
calculate_loan(1001, 150000, 20000, "Car", 400000, 30)  # Salary not sufficient
calculate_loan(1001, 150000, 80000, "Business", 8000000, 90)  # Loan exceeds eligibility

